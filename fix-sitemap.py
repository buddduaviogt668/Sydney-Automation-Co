import os
import re
from datetime import date

HTML_DIR = "."
SITEMAP_PATH = "./sitemap.xml"

# Find all HTML files
urls = []
for root, dirs, files in os.walk(HTML_DIR):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.github', 'dist', 'mnt']]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        # Convert path to URL
        rel = os.path.relpath(fpath, HTML_DIR).replace('\\', '/')
        if rel == 'index.html':
            url = 'https://www.sydneyautomationco.com.au/'
        else:
            url = f'https://www.sydneyautomationco.com.au/{rel}'
        urls.append(url)

# Sort for consistency
urls.sort()

# Build sitemap XML
today = date.today().strftime('%Y-%m-%d')
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for url in urls:
    # Set priority based on URL importance
    if url == 'https://www.sydneyautomationco.com.au/':
        priority = '1.0'
    elif any(k in url for k in ['c-bus-programmer-sydney', 'dynalite-programmer-sydney', 
                                  'cbus-repair-sydney', 'emergency-repair', 'cbus-fault-finding-sydney',
                                  'dynalite-repair-sydney', 'cbus-specialist-sydney']):
        priority = '0.9'
    else:
        priority = '0.8'
    lines.append(f'  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append(f'    <changefreq>weekly</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append(f'  </url>')
lines.append('</urlset>')

sitemap_content = '\n'.join(lines)

with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"✅ Sitemap written with {len(urls)} URLs (all www)")
