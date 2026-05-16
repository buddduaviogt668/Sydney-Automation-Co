#!/usr/bin/env python3
"""
fix_head_structure.py
Tailored for: https://github.com/buddduaviogt668/Sydney-Automation-Co
"""

import os
import re
import sys
from urllib.parse import urljoin

# Your actual production domain
BASE_URL = "https://sydneyautomationco.com.au/"

def fix_file(filepath, root_dir):
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        enc = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
        enc = 'latin-1'
        changes.append('re-encoded to UTF-8')

    original_content = content

    # 1. Split document into Prefix, Head, and Suffix
    head_match = re.search(r'(<head[^>]*>)(.*?)(</head>)', content, re.IGNORECASE | re.DOTALL)
    if not head_match:
        return False, changes 

    prefix = content[:head_match.start()]
    head_open = head_match.group(1)
    head_inner = head_match.group(2)
    head_close = head_match.group(3)
    suffix = content[head_match.end():]

    # 2. Remove existing charset/content-type tags from head to avoid duplicates
    head_inner = re.sub(r'<meta\s+charset=["\']?[^"\'>\s]+["\']?\s*/?>', '', head_inner, flags=re.IGNORECASE)
    head_inner = re.sub(r'<meta\s+http-equiv=["\']Content-Type["\'][^>]*>', '', head_inner, flags=re.IGNORECASE)

    # 3. Rescue Tags from Body (Suffix)
    
    # Rescue Title
    title_match = re.search(r'<title[^>]*>.*?</title>', suffix, re.IGNORECASE | re.DOTALL)
    rescued_title = None
    if not re.search(r'<title[^>]*>.*?</title>', head_inner, re.IGNORECASE | re.DOTALL) and title_match:
        rescued_title = title_match.group(0)
        suffix = suffix[:title_match.start()] + suffix[title_match.end():]
        changes.append('moved <title> into <head>')

    # Rescue/Create Canonical
    canonical_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', suffix, re.IGNORECASE)
    rescued_canonical = None
    if not re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', head_inner, re.IGNORECASE) and canonical_match:
        rescued_canonical = canonical_match.group(0)
        suffix = suffix[:canonical_match.start()] + suffix[canonical_match.end():]
        changes.append('moved canonical into <head>')
    elif not re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', head_inner, re.IGNORECASE):
        # SEO Improvement: Remove .html extension for a cleaner URL
        rel_path = os.path.relpath(filepath, root_dir)
        slug = rel_path.replace('.html', '').replace('\\', '/')
        if slug == 'index' or slug == '.':
            canonical_url = BASE_URL
        else:
            canonical_url = urljoin(BASE_URL, slug)
        
        rescued_canonical = f'<link rel="canonical" href="{canonical_url}">'
        changes.append(f'added clean canonical: {canonical_url}')

    # Rescue Robots
    robots_match = re.search(r'<meta[^>]+name=["\']robots["\'][^>]*>', suffix, re.IGNORECASE)
    rescued_robots = None
    if robots_match:
        rescued_robots = robots_match.group(0)
        suffix = suffix[:robots_match.start()] + suffix[robots_match.end():]
        changes.append('moved meta robots into <head>')

    # 4. Reconstruct Head
    # Order: Charset -> Title -> Canonical -> Robots -> Rest of head
    new_head_top = ['<meta charset="UTF-8">']
    if rescued_title: new_head_top.append(rescued_title)
    if rescued_canonical: new_head_top.append(rescued_canonical)
    if rescued_robots: new_head_top.append(rescued_robots)

    combined_head_inner = "\n    " + "\n    ".join(new_head_top) + "\n    " + head_inner.strip() + "\n"
    
    final_content = f"{prefix}{head_open}{combined_head_inner}{head_close}{suffix}"

    if final_content != original_content or enc != 'utf-8':
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        return True, changes
    
    return False, changes

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    fixed_count = 0
    clean_count = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '.vercel', '__pycache__')]
        for filename in filenames:
            if not filename.lower().endswith('.html'):
                continue
            filepath = os.path.join(dirpath, filename)
            changed, changes = fix_file(filepath, root)
            if changed:
                fixed_count += 1
                print(f"✅ Fixed: {filepath}")
                for c in changes: print(f"    → {c}")
            else:
                clean_count += 1

    print(f"\nSummary: {fixed_count} files fixed, {clean_count} files already clean.")

if __name__ == '__main__':
    main()
