#!/usr/bin/env python3
"""Refresh per-paper Google Scholar citation counts in _data/citations.yml.

Run by .github/workflows/deploy.yml on its daily schedule (and on a manual run);
the workflow commits the file back to the repository when the counts change.

Google Scholar has no API and refuses requests from GitHub's servers, so the
counts are read through SerpApi's Google Scholar Author API when the SERPAPI_KEY
environment variable is set (a repository secret; one search per run). Without
the key the public profile page is fetched directly, which works from a home
network but not from GitHub.

On any failure the script exits non-zero WITHOUT touching the file, so the site
keeps showing the last committed numbers. No third-party packages are needed.
"""

import datetime
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

SOCIALS = "_data/socials.yml"
OUTPUT = "_data/citations.yml"
MIN_ROWS = 10  # fewer parsed papers than this means we did not get the real page


def scholar_user_id():
    with open(SOCIALS) as f:
        m = re.search(r"^scholar_userid:\s*([\w-]+)", f.read(), re.M)
    if not m:
        sys.exit(f"no scholar_userid in {SOCIALS}")
    return m.group(1)


def fetch(user):
    url = f"https://scholar.google.com/citations?user={user}&hl=en&cstart=0&pagesize=100"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def parse(page, user):
    papers = {}
    for row in page.split('<tr class="gsc_a_tr">')[1:]:
        row = row.split("</tr>")[0]
        pid = re.search(r"citation_for_view=" + re.escape(user) + r":([\w-]+)", row)
        title = re.search(r'class="gsc_a_at"[^>]*>(.*?)</a>', row, re.S)
        cites = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>', row)
        year = re.search(r'class="gsc_a_h[^"]*"[^>]*>(\d{4})<', row)
        if not (pid and title and cites):
            continue
        papers[f"{user}:{pid.group(1)}"] = {
            "citations": int(cites.group(1) or 0),
            "title": html.unescape(re.sub(r"<[^>]+>", "", title.group(1))).strip(),
            "year": year.group(1) if year else "",
        }
    return papers


def fetch_serpapi(user, key):
    """One SerpApi search: the author's articles, up to 100, with citation counts."""
    query = urllib.parse.urlencode(
        {"engine": "google_scholar_author", "author_id": user, "hl": "en", "num": 100, "api_key": key}
    )
    with urllib.request.urlopen("https://serpapi.com/search.json?" + query, timeout=60) as r:
        data = json.load(r)
    if data.get("error"):
        raise RuntimeError(data["error"])
    papers = {}
    for art in data.get("articles", []):
        cid = art.get("citation_id") or ""
        if not cid.startswith(user + ":"):
            continue
        papers[cid] = {
            "citations": int((art.get("cited_by") or {}).get("value") or 0),
            "title": (art.get("title") or "").strip(),
            "year": str(art.get("year") or ""),
        }
    return papers


def previous_total():
    if not os.path.exists(OUTPUT):
        return 0
    with open(OUTPUT) as f:
        return sum(int(n) for n in re.findall(r"^\s+citations:\s*(\d+)", f.read(), re.M))


def write(papers):
    q = lambda s: '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'
    lines = [
        "# Google Scholar citation counts, keyed by <scholar user id>:<paper id>.",
        "# Refreshed at build time by scripts/fetch_scholar_citations.py; the copy",
        "# committed here is the fallback used when Scholar refuses the request.",
        "metadata:",
        f"  last_updated: {q(datetime.date.today().isoformat())}",
        "papers:",
    ]
    for key in sorted(papers):
        p = papers[key]
        lines += [
            f"  {q(key)}:",
            f"    citations: {p['citations']}",
            f"    title: {q(p['title'])}",
            f"    year: {q(p['year'])}",
        ]
    new = "\n".join(lines) + "\n"
    body = lambda text: [l for l in text.splitlines() if "last_updated" not in l]
    if os.path.exists(OUTPUT):
        with open(OUTPUT) as f:
            if body(f.read()) == body(new):
                return False
    with open(OUTPUT, "w") as f:
        f.write(new)
    return True


def main():
    user = scholar_user_id()
    key = os.environ.get("SERPAPI_KEY", "").strip()
    source = "SerpApi" if key else "Google Scholar directly"
    try:
        papers = fetch_serpapi(user, key) if key else parse(fetch(user), user)
    except Exception as e:  # network error, 403/429, bad key, ...
        # never echo the request URL: it contains the API key
        reason = f"HTTP {e.code}" if hasattr(e, "code") else (str(e) if isinstance(e, RuntimeError) or not key else type(e).__name__)
        sys.exit(f"request via {source} failed ({reason}); keeping existing {OUTPUT}")
    total = sum(p["citations"] for p in papers.values())
    if len(papers) < MIN_ROWS:
        sys.exit(f"only got {len(papers)} papers via {source}; keeping existing {OUTPUT}")
    if total < 0.8 * previous_total():
        sys.exit(f"total {total} is far below the previous {previous_total()}; keeping existing {OUTPUT}")
    changed = write(papers)
    print(f"{len(papers)} papers, {total} citations in total, via {source}; "
          + (f"updated {OUTPUT}" if changed else "no change"))


if __name__ == "__main__":
    main()
