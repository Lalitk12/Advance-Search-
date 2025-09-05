#!/usr/bin/env python3
"""
Google Advanced Query Generator (OSINT / Security Research Aid)
Author: YourName
License: MIT

⚠️ DISCLAIMER
This tool is for ethical research, OSINT, and educational purposes only.
Do not use it to target systems without explicit authorization.
"""

import argparse
import urllib.parse
import json
import csv
from datetime import datetime

# ------------------ PRESETS ------------------ #
PRESETS = {
    "quick": [
        'site:{domain}',
        '"{org}" site:{domain}',
        '"{org}" "{domain}"'
    ],
    "site_mapping": [
        'site:{domain} -www.{domain}',
        'site:*.{domain}',
        'intitle:index.of site:{domain}'
    ],
    "public_docs": [
        'site:{domain} filetype:pdf OR filetype:docx OR filetype:xlsx',
        'site:{domain} ext:txt OR ext:log'
    ],
    "exposed_dirs": [
        'intitle:"index of" "{domain}"',
        'site:{domain} inurl:backup OR inurl:old OR inurl:archive'
    ],
    "code_sharing": [
        'site:pastebin.com "{domain}"',
        'site:github.com "{org}"',
        '"{org}" "api_key" OR "password"'
    ],
    "login_admin": [
        'site:{domain} inurl:admin',
        'site:{domain} intitle:"login"',
        '"{org}" intitle:"portal"'
    ],
    "public_contacts": [
        '"{org}" email',
        '"{org}" contact us" site:{domain}',
        '"{org}" phone site:{domain}'
    ],
    "leaks_news": [
        '"{org}" "data leak"',
        '"{org}" "breach"'
    ],
    "cloud_storage": [
        'site:s3.amazonaws.com "{org}"',
        'site:blob.core.windows.net "{org}"',
        'site:drive.google.com "{org}"'
    ]
}

# ------------------ HELPERS ------------------ #
def build_query(template, org, domain, after=None, before=None):
    q = template.format(org=org, domain=domain)
    if after:
        q += f" after:{after}"
    if before:
        q += f" before:{before}"
    return q

def make_url(engine, query):
    encoded = urllib.parse.quote(query)
    if engine == "google":
        return f"https://www.google.com/search?q={encoded}"
    elif engine == "bing":
        return f"https://www.bing.com/search?q={encoded}"
    elif engine == "ddg":
        return f"https://duckduckgo.com/?q={encoded}"
    else:
        return query

# ------------------ MAIN ------------------ #
def main():
    parser = argparse.ArgumentParser(
        description="Generate advanced Google/Bing/DDG queries for OSINT / auditing"
    )
    parser.add_argument("--org", required=True, help="Organization name")
    parser.add_argument("--domain", required=True, help="Domain (e.g. example.com)")
    parser.add_argument("--preset", nargs="+", choices=list(PRESETS.keys()), default=["quick"],
                        help="Which preset(s) to use")
    parser.add_argument("--custom", nargs="*", help="Custom queries to include")
    parser.add_argument("--after", help="Limit results after date (YYYY-MM-DD)")
    parser.add_argument("--before", help="Limit results before date (YYYY-MM-DD)")
    parser.add_argument("--engine", choices=["google", "bing", "ddg"], default="google")
    parser.add_argument("--out", help="Export queries to CSV or JSON")
    args = parser.parse_args()

    all_queries = []

    # Generate from presets
    for p in args.preset:
        for t in PRESETS[p]:
            q = build_query(t, args.org, args.domain, args.after, args.before)
            all_queries.append(q)

    # Add custom
    if args.custom:
        all_queries.extend(args.custom)

    # Deduplicate
    all_queries = list(dict.fromkeys(all_queries))

    # Print with URLs
    for q in all_queries:
        print(f"[{args.engine.upper()}] {q}")
        print(f"   → {make_url(args.engine, q)}\n")

    # Export
    if args.out:
        if args.out.endswith(".json"):
            with open(args.out, "w", encoding="utf-8") as f:
                json.dump(all_queries, f, indent=2)
        elif args.out.endswith(".csv"):
            with open(args.out, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["query", "url"])
                for q in all_queries:
                    writer.writerow([q, make_url(args.engine, q)])
        print(f"[+] Exported {len(all_queries)} queries to {args.out}")

if __name__ == "__main__":
    main()
