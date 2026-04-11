#!/usr/bin/env python3
"""
inject-perf-script.py
=====================
Does two things across all HTML files:
1. Injects <script src="/perf-optimise.js" defer></script> before </body>
2. Replaces blocking Google Fonts link with async preload version

SAFE TO RUN MULTIPLE TIMES - checks before modifying.
"""

import os
import glob
import re

SCRIPT_TAG = '<script src="/perf-optimise.js" defer></script>'
INJECT_BEFORE = '</body>'

OLD_FONTS = re.compile(
    r'<link[^>]*href=["\']https://fonts\.googleapis\.com/css2\?[^"\']*Barlow[^"\']*["\'][^>]*>',
    re.IGNORECASE
)

NEW_FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&family=Barlow+Condensed:wght@700;800&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&family=Barlow+Condensed:wght@700;800&display=swap"></noscript>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # Fix 1: inject perf script before </body>
    if 'perf-optimise.js' not in content:
        if INJECT_BEFORE in content:
            content = content.replace(INJECT_BEFORE, SCRIPT_TAG + '\n' + INJECT_BEFORE, 1)
            changed = True

    # Fix 2: async Google Fonts
    if 'onload="this.onload=null' not in content:
        if OLD_FONTS.search(content):
            content = OLD_FONTS.sub(NEW_FONTS, content)
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return 'updated'
    return 'skipped'

def main():
    html_files = list(set(glob.glob('**/*.html', recursive=True) + glob.glob('*.html')))
    html_files.sort()

    updated, skipped = [], []

    for filepath in html_files:
        result = process_file(filepath)
        if result == 'updated':
            updated.append(filepath)
        else:
            skipped.append(filepath)

    print(f"\nUpdated {len(updated)} files, skipped {len(skipped)} files.")
    if updated:
        print("Next: git add -A && git commit -m 'perf: fonts async + perf script sitewide' && git push")

if __name__ == '__main__':
    main()
