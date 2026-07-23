import re
import os

# ── 1. Fix "13 Reviews" across any remaining HTML files ──────────────────────
files_to_fix = [
    'cbus-dynalite-upgrade-guide.html',
    'products.html',
    'services-hub.html',
    'terms-of-service.html',
    'old_index.html',
]
for f in files_to_fix:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    updated = content.replace('13 Reviews', '14 Reviews').replace('(13 Reviews)', '(14 Reviews)')
    if updated != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(updated)
        print(f'Fixed: {f}')
    else:
        print(f'No change needed: {f}')

print("\nAll 13→14 review fixes done.")
