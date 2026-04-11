#!/usr/bin/env python3
"""
fix-google-fonts.py
===================
Replaces the render-blocking Google Fonts <link> tag with an async
preload version across all HTML files.

Finds any Google Fonts link that loads Barlow and replaces it with:
- preconnect hints
- async preload (non-blocking)
- noscript fallback

SAFE TO RUN MULTIPLE TIMES — checks before modifying.
"""

import os
import glob
import re

OLD_PATTERN = re.compile(
    r'<link[^>]*href=["\']https://fonts\.googleapis\.com/css2\?[^"\']*Barlow[^"\']*["\'][^>]*>',
    re.IGNORECASE
)

NEW_TAGS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&family=Barlow+Condensed:wght@700;800&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&family=Barlow+Condensed:wght@700;800&display=swap"></noscript>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Skip if already fixed
    if 'onload="this.onload=null' in content:
        return 'skipped'

    # Skip if no Google Fonts Barlow link
    if not OLD_PATTERN.search(content):
        return 'no-match'

    updated = OLD_PATTERN.sub(NEW_TAGS, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated)

    return 'updated'

def main():
    html_files = list(set(glob.glob('**/*.html', recursive=True) + glob.glob('*.html')))
    html_files.sort()

    updated, skipped, no_match = [], [], []

    for filepath in html_files:
        result = process_file(filepath)
        if result == 'updated':
            updated.append(filepath)
        elif result == 'skipped':
            skipped.append(filepath)
        elif result == 'no-match':
            no_match.append(filepath)

    print(f"\n✅ UPDATED ({len(updated)} files):")
    for f in updated:
        print(f"   {f}")

    if skipped:
        print(f"\n⏭️  SKIPPED — already fixed ({len(skipped)} files)")

    if no_match:
        print(f"\n⚠️  NO FONTS LINK FOUND ({len(no_match)} files) — may use different font or no fonts:")
        for f in no_match:
            print(f"   {f}")

    print(f"\nDone. {len(updated)} files updated.")

if __name__ == '__main__':
    main()
