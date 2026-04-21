#!/usr/bin/env python3
"""
Fix og:url to match canonical URL in HTML files.
Ensures consistency between canonical and og:url meta tags.
"""

import os
import re
import glob

def fix_og_url_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find canonical URL
    canonical_match = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', content, re.IGNORECASE)
    if not canonical_match:
        print(f"No canonical found in {filepath}")
        return False

    canonical_url = canonical_match.group(1)

    # Find og:url
    og_url_match = re.search(r'<meta[^>]*property="og:url"[^>]*content="([^"]*)"', content, re.IGNORECASE)
    if not og_url_match:
        print(f"No og:url found in {filepath}")
        return False

    og_url = og_url_match.group(1)

    if canonical_url == og_url:
        return False  # Already consistent

    # Replace og:url with canonical
    old_meta = og_url_match.group(0)
    new_meta = old_meta.replace(og_url, canonical_url)

    content = content.replace(old_meta, new_meta)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed {filepath}: og:url changed from {og_url} to {canonical_url}")
    return True

def main():
    # Get all HTML files
    html_files = glob.glob('*.html')

    fixed_count = 0
    for filepath in html_files:
        if fix_og_url_in_file(filepath):
            fixed_count += 1

    print(f"\nFixed {fixed_count} files.")

if __name__ == '__main__':
    main()