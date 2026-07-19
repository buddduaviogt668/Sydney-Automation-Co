import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

# First, discover the actual sitemap link pattern used in footers
patterns_found = {}
for fname in os.listdir(DIR):
    if not fname.endswith('.html'):
        continue
    try:
        fpath = os.path.join(DIR, fname)
        content = open(fpath, encoding='utf-8').read()
        if 'footer-copy' in content and 'sitemap' in content.lower():
            m = re.search(r'<a href="/sitemap[^"]*"[^>]*>[^<]+</a>', content)
            if m:
                patterns_found[m.group(0)] = patterns_found.get(m.group(0), 0) + 1
    except Exception:
        pass

print("Patterns found in footers:")
for p, c in sorted(patterns_found.items(), key=lambda x: -x[1]):
    print(f"  ({c}x) {p}")

# Now inject the accessibility link after the sitemap link, everywhere it doesn't already exist
count = 0
for fname in os.listdir(DIR):
    if not fname.endswith('.html'):
        continue
    try:
        fpath = os.path.join(DIR, fname)
        content = open(fpath, encoding='utf-8').read()
        
        # Skip if accessibility link already present
        if '/accessibility' in content:
            continue
        
        # Target: <a href="/sitemap.xml" ...>Sitemap</a>
        orig = content
        # Pattern 1 - sitemap.xml with onmouseout style
        content = re.sub(
            r'(<a href="/sitemap\.xml"[^>]*>Sitemap</a>)',
            r'\1 &middot; <a href="/accessibility" onmouseout="this.style.color=\'#6a8cb5\'" onmouseover="this.style.color=\'#f07020\'" style="color:#6a8cb5">Accessibility</a>',
            content
        )
        # Pattern 2 - sitemap.html
        if content == orig:
            content = re.sub(
                r'(<a href="/sitemap\.html"[^>]*>Sitemap</a>)',
                r'\1 &middot; <a href="/accessibility" onmouseout="this.style.color=\'#6a8cb5\'" onmouseover="this.style.color=\'#f07020\'" style="color:#6a8cb5">Accessibility</a>',
                content
            )
        
        if content != orig:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error on {fname}: {e}")

print(f"\nAdded accessibility link to {count} pages.")
