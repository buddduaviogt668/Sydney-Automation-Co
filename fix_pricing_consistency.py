#!/usr/bin/env python3
"""
Fix pricing consistency across all HTML pages to match index.html.
Correct pricing:
  - $650 + GST total callout
  - $200 + GST paid upfront (site fee)
  - $150/hr + GST, 3-hour minimum ($450 + GST)
"""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Replacements: (old_text, new_text)
# Order matters — more specific first
REPLACEMENTS = [
    # Old pricing table entries missing "+ GST"
    (r'\$150/hr\b(?!\s*\+\s*GST)', '$150/hr + GST'),
    
    # "3 hours ($450)" → "3-hour minimum ($450 + GST)"
    (r'3\s*hours?\s*\(\$450\)', '3-hour minimum ($450 + GST)'),
    
    # "$450 + GST (3hr min)" — ensure consistent form
    # Already correct if it has + GST, skip
    
    # "Book $200 Diagnostic Visit" → correct CTA text
    (r'Book \$200 Diagnostic Visit', 'Book Online — $200 + GST Site Fee'),
    
    # "$200 Diagnostic Fee" → "$200 + GST Site Fee"
    (r'\$200 Diagnostic Fee\b', '$200 + GST Site Fee'),
    
    # Minimum Call-Out: 3 hours ($450) pattern in list items
    (r'(Minimum Call-Out:</strong>\s*)3 hours \(\$450\)', r'\g<1>3 hours ($450 + GST)'),
    
    # "3-hour minimum ($450)" without "+ GST"  
    (r'3-hour minimum \(\$450\)(?!\s*\+\s*GST)', '3-hour minimum ($450 + GST)'),

    # "min 3 hrs" style in older content
    (r'\$155/hr \(Min 3 Hrs\)', '$150/hr + GST (Min 3 Hrs)'),

    # "3 hours ($450 + GST)" → ensure consistent
    # Already correct, skip
    
    # old billing text: "bill hourly at $150/hr" without GST
    (r'bill(?:s|ed)?\s+hourly\s+at\s+\$150/hr(?!\s*\+)', 'billed hourly at $150/hr + GST'),
]

# Track changes
total_files_changed = 0
total_replacements = 0

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content
    changes = 0

    for pattern, replacement in REPLACEMENTS:
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            changes += n
            content = new_content

    if content != original:
        with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
            f.write(content)
        return changes
    return 0


def main():
    global total_files_changed, total_replacements

    html_files = []
    for fname in os.listdir(ROOT):
        if fname.endswith('.html'):
            html_files.append(os.path.join(ROOT, fname))

    # Also check subdirectories
    for subdir in ['blog', 'tech-library']:
        subpath = os.path.join(ROOT, subdir)
        if os.path.isdir(subpath):
            for fname in os.listdir(subpath):
                if fname.endswith('.html'):
                    html_files.append(os.path.join(subpath, fname))

    print(f"Scanning {len(html_files)} HTML files...")

    for filepath in sorted(html_files):
        changes = fix_file(filepath)
        if changes > 0:
            total_files_changed += 1
            total_replacements += changes
            print(f"  Fixed {changes:2d} item(s): {os.path.relpath(filepath, ROOT)}")

    print(f"\nDone: {total_replacements} replacements across {total_files_changed} files.")


if __name__ == '__main__':
    main()
