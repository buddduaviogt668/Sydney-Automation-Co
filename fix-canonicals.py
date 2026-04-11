import os
import re

HTML_DIR = "."

updated = []
skipped = []

for root, dirs, files in os.walk(HTML_DIR):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.github', 'dist', 'mnt']]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            original = content

            # Fix canonical tags: www -> non-www
            content = content.replace(
                'href="https://www.sydneyautomationco.com.au',
                'href="https://sydneyautomationco.com.au'
            )
            # Fix og:url tags: www -> non-www
            content = content.replace(
                'content="https://www.sydneyautomationco.com.au',
                'content="https://sydneyautomationco.com.au'
            )

            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated.append(fpath)
            else:
                skipped.append(fpath)
        except OSError:
            pass

print(f"✅ Updated: {len(updated)} files")
print(f"⏭️  Skipped: {len(skipped)} files")
