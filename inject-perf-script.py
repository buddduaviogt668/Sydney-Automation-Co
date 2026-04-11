#!/usr/bin/env python3
"""
inject-perf-script.py
=====================
Adds <script src="/perf-optimise.js" defer></script> before </body>
in every .html file in the current directory and subdirectories.

HOW TO USE:
1. Clone your repo locally (or open terminal in your repo folder)
2. Copy this script into the ROOT of your repo
3. Run: python3 inject-perf-script.py
4. Check the output — it will tell you exactly which files were updated
5. Commit and push to GitHub

SAFE TO RUN MULTIPLE TIMES — it checks if the tag already exists before adding it.
"""

import os
import glob

SCRIPT_TAG = '<script src="/perf-optimise.js" defer></script>'
INJECT_BEFORE = '</body>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Skip if already injected
    if 'perf-optimise.js' in content:
        return 'skipped'

    # Skip if no </body> tag
    if INJECT_BEFORE not in content:
        return 'no-body-tag'

    # Inject before </body>
    updated = content.replace(INJECT_BEFORE, f'{SCRIPT_TAG}\n{INJECT_BEFORE}', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated)

    return 'updated'

def main():
    # Find all HTML files in current directory and subdirectories
    html_files = glob.glob('**/*.html', recursive=True) + glob.glob('*.html')
    html_files = list(set(html_files))  # deduplicate
    html_files.sort()

    updated = []
    skipped = []
    no_body = []

    for filepath in html_files:
        result = process_file(filepath)
        if result == 'updated':
            updated.append(filepath)
        elif result == 'skipped':
            skipped.append(filepath)
        elif result == 'no-body-tag':
            no_body.append(filepath)

    print(f"\n✅ UPDATED ({len(updated)} files):")
    for f in updated:
        print(f"   {f}")

    if skipped:
        print(f"\n⏭️  SKIPPED — already has perf-optimise.js ({len(skipped)} files):")
        for f in skipped:
            print(f"   {f}")

    if no_body:
        print(f"\n⚠️  NO </body> TAG FOUND ({len(no_body)} files) — check these manually:")
        for f in no_body:
            print(f"   {f}")

    print(f"\nDone. {len(updated)} files updated, {len(skipped)} skipped, {len(no_body)} need manual check.")
    print("\nNext step: git add -A && git commit -m 'perf: inject perf-optimise.js across all pages' && git push")

if __name__ == '__main__':
    main()
