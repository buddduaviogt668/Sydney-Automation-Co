#!/usr/bin/env python3
"""
fix_head_structure.py
Fixes all <head> structure issues across HTML files:
1. Ensures <meta charset="UTF-8"> is first in <head>
2. Moves any <title>, <link rel="canonical">, <meta robots> that are outside <head> into <head>
3. Adds missing canonical tags (uses the filename to construct the canonical URL)
4. Fixes files saved in non-UTF-8 encoding
"""

import os
import re
import sys
from urllib.parse import urljoin

BASE_URL = "https://sydneyautomationco.com.au/"

def extract_tag(content, pattern):
    """Find and remove a tag from content, return (tag_string, content_without_tag)"""
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        tag = match.group(0)
        content = content[:match.start()] + content[match.end():]
        return tag, content
    return None, content

def fix_file(filepath):
    changes = []

    # Read file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        enc = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
        enc = 'latin-1'
        changes.append('re-encoded to UTF-8')

    original = content

    # --- 1. Remove any existing charset meta (we'll re-add it first) ---
    content = re.sub(r'<meta\s+charset=["\']?[^"\'>\s]+["\']?\s*/?>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+http-equiv=["\']Content-Type["\'][^>]*>', '', content, flags=re.IGNORECASE)

    # --- 2. Extract <title> from anywhere outside <head> ---
    # First find what's inside head
    head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.IGNORECASE | re.DOTALL)
    if not head_match:
        return False, changes  # Can't fix without a <head>

    head_content = head_match.group(1)
    body_and_rest = content[head_match.end():]

    # Check if title is missing from head but exists in body
    has_title_in_head = bool(re.search(r'<title[^>]*>.*?</title>', head_content, re.IGNORECASE | re.DOTALL))
    title_in_body_match = re.search(r'<title[^>]*>.*?</title>', body_and_rest, re.IGNORECASE | re.DOTALL)

    rescued_title = None
    if not has_title_in_head and title_in_body_match:
        rescued_title = title_in_body_match.group(0)
        body_and_rest = body_and_rest[:title_in_body_match.start()] + body_and_rest[title_in_body_match.end():]
        changes.append('moved <title> into <head>')

    # --- 3. Extract canonical from body if missing from head ---
    has_canonical_in_head = bool(re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', head_content, re.IGNORECASE))
    canonical_in_body_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', body_and_rest, re.IGNORECASE)

    rescued_canonical = None
    if not has_canonical_in_head and canonical_in_body_match:
        rescued_canonical = canonical_in_body_match.group(0)
        body_and_rest = body_and_rest[:canonical_in_body_match.start()] + body_and_rest[canonical_in_body_match.end():]
        changes.append('moved canonical into <head>')
    elif not has_canonical_in_head:
        # Build canonical from filename
        filename = os.path.basename(filepath)
        slug = filename.replace('.html', '')
        if slug in ('index', ''):
            canonical_url = BASE_URL
        else:
            canonical_url = BASE_URL + slug
        rescued_canonical = f'<link rel="canonical" href="{canonical_url}">'
        changes.append(f'added missing canonical: {canonical_url}')

    # --- 4. Extract meta robots from body if outside head ---
    robots_in_body_match = re.search(r'<meta[^>]+name=["\']robots["\'][^>]*>', body_and_rest, re.IGNORECASE)
    rescued_robots = None
    if robots_in_body_match:
        rescued_robots = robots_in_body_match.group(0)
        body_and_rest = body_and_rest[:robots_in_body_match.start()] + body_and_rest[robots_in_body_match.end():]
        changes.append('moved meta robots into <head>')

    # --- 5. Rebuild <head> with charset first ---
    new_head_parts = ['<meta charset="UTF-8">']
    if rescued_title:
        new_head_parts.append(rescued_title)
    if rescued_canonical:
        new_head_parts.append(rescued_canonical)
    if rescued_robots:
        new_head_parts.append(rescued_robots)

    # Clean up head_content (remove extra blank lines)
    head_content = head_content.strip()

    new_head_content = '\n    '.join(new_head_parts) + '\n    ' + head_content

    # Reconstruct full document
    head_open = re.search(r'<head[^>]*>', content, re.IGNORECASE).group(0)
    content = re.sub(
        r'<head[^>]*>.*?</head>',
        f'{head_open}\n    {new_head_content}\n</head>',
        content,
        count=1,
        flags=re.IGNORECASE | re.DOTALL
    )
    # Re-attach fixed body
    head_end = re.search(r'</head>', content, re.IGNORECASE)
    if head_end:
        content = content[:head_end.end()] + body_and_rest

    changes.append('charset inserted first in <head>')

    if content != original or enc != 'utf-8':
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, changes


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    fixed = []
    clean = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '.vercel')]
        for filename in filenames:
            if not filename.lower().endswith('.html'):
                continue
            filepath = os.path.join(dirpath, filename)
            changed, changes = fix_file(filepath)
            if changed:
                fixed.append((filepath, changes))
            else:
                clean += 1

    print(f"\n✅ Fixed {len(fixed)} files:")
    for fp, ch in fixed:
        print(f"  {fp}")
        for c in ch:
            print(f"    → {c}")

    print(f"\n⏭️  Already clean: {clean} files")
    print("\nDone. Push to GitHub to deploy.")

if __name__ == '__main__':
    main()
