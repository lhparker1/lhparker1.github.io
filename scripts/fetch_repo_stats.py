#!/usr/bin/env python3
"""Fetch star counts and descriptions for the repos in _data/code.yml.

Run by the deploy workflow before the site is built. Writes _data/repo_stats.json, which the Code
page reads; any repo that can't be fetched keeps the values written in _data/code.yml.
"""
import json
import os
import re
import urllib.request

repos = re.findall(r"^\s*repo:\s*(\S+)\s*$", open("_data/code.yml", encoding="utf-8").read(), re.M)
token = os.environ.get("GITHUB_TOKEN")
stats = {}
for repo in repos:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "site-build"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        stats[repo] = {"stars": d.get("stargazers_count"), "description": d.get("description") or ""}
        print(f"{repo}: {stats[repo]['stars']} stars")
    except Exception as e:  # keep the build going; the page falls back to _data/code.yml
        print(f"{repo}: not fetched ({e})")

with open("_data/repo_stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)
