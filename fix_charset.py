#!/usr/bin/env python3
"""
fix_charset.py
Scans all .html files in a directory tree and ensures:
1. Files are saved as UTF-8
2. <meta charset="UTF-8"> is the FIRST tag inside <head>
"""

import os
import re
import sys

def fix_file(filepath):
    # Try reading as UTF-8 first, fall back to latin-1
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original_encoding = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
        original_encoding = 'latin-1'

    original = content

    # Remove any existing charset meta tags (all variations)
    content = re.sub(
        r'<meta\s+charset=["\']?[^"\'>\s]+["\']?\s*/?>',
        '',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<meta\s+http-equiv=["\']Content-Type["\'][^>]*>',
        '',
        content,
        flags=re.IGNORECASE
    )

    # Insert <meta charset="UTF-8"> as the very first thing inside <head>
    content = re.sub(
        r'(<head[^>]*>)',
        r'\1\n    <meta charset="UTF-8">',
        content,
        count=1,
        flags=re.IGNORECASE
    )

    # Always write back as UTF-8
    if content != original or original_encoding != 'utf-8':
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, original_encoding
    return False, original_encoding


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    fixed = []
    skipped = []

    for dirpath, dirnames, filenames in os.walk(root):
        # Skip node_modules, .git etc
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '.vercel')]
        for filename in filenames:
            if filename.lower().endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                changed, enc = fix_file(filepath)
                if changed:
                    fixed.append(f"  FIXED ({enc} → utf-8): {filepath}")
                else:
                    skipped.append(filepath)

    print(f"\n✅ Fixed {len(fixed)} files:")
    for f in fixed:
        print(f)
    print(f"\n⏭️  Already correct: {len(skipped)} files")
    print("\nDone. Push to GitHub to deploy.")

if __name__ == '__main__':
    main()
