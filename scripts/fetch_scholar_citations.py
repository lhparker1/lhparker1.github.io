#!/usr/bin/env python3
"""Refresh per-paper Google Scholar citation counts in _data/citations.yml.

Run at build time by .github/workflows/deploy.yml (and so on every push and on
the weekly schedule). Google Scholar has no API and sometimes refuses automated
requests; when that happens this script exits non-zero WITHOUT touching the
file, so the site keeps showing the last numbers committed to the repository.

No third-party packages: the public profile page is fetched and parsed directly.
"""

import datetime
import html
import os
import re
import sys
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
    with open(OUTPUT, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    user = scholar_user_id()
    try:
        page = fetch(user)
    except Exception as e:  # network error, 403/429, ...
        sys.exit(f"Scholar request failed ({e}); keeping existing {OUTPUT}")
    papers = parse(page, user)
    total = sum(p["citations"] for p in papers.values())
    if len(papers) < MIN_ROWS:
        sys.exit(f"only parsed {len(papers)} papers (blocked or page changed); keeping existing {OUTPUT}")
    if total < 0.8 * previous_total():
        sys.exit(f"parsed total {total} is far below the previous {previous_total()}; keeping existing {OUTPUT}")
    write(papers)
    print(f"wrote {len(papers)} papers, {total} citations in total, to {OUTPUT}")


if __name__ == "__main__":
    main()
