"""
rebuild_sitemap.py
Scans every .html file in the project root and blog/ directory,
builds a complete sitemap.xml from scratch, and writes it.
Run this after any page generation to keep the sitemap in perfect sync.
"""

import os
import glob
from datetime import datetime

BASE_DIR = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'
BASE_URL = 'https://sydneyautomationco.com.au'
TODAY = datetime.now().strftime('%Y-%m-%d')

# Pages that should have highest priority
HIGH_PRIORITY_PATTERNS = [
    'index.html', 'about.html', 'blog.html', 'book-service.html',
    'automation-sydney.html', 'afss-emergency-lighting-services.html',
    'accessibility.html', 'automation-companies-sydney.html',
    '404.html',  # will be excluded
]

# Pages to exclude from sitemap
EXCLUDE = {
    'test.html', 'old_index.html', '404.html',
    'about-sydney-automation-co.html',  # duplicate of about
}

# Python scripts - not pages
SCRIPT_EXTENSIONS = {'.py', '.json', '.xml', '.txt', '.md', '.jpg', '.png',
                     '.jpeg', '.gif', '.svg', '.ico', '.css', '.js', '.woff',
                     '.woff2', '.ttf', '.eot', '.map', '.log'}

def get_priority(filename):
    name = os.path.basename(filename)
    # Core pages
    if name in ('index.html', 'about.html', 'book-service.html',
                 'automation-sydney.html', 'afss-emergency-lighting-services.html',
                 'blog.html', 'automation-companies-sydney.html'):
        return '1.0', 'weekly'
    # Hub/sector pages
    if any(kw in name for kw in [
        'lighting-automation-sydney', 'cbus-dynalite-repair-sydney',
        'dynalite-repair-sydney', 'hub', 'services', 'sector'
    ]):
        return '0.8', 'monthly'
    # Blog posts
    if name.startswith('blog-') or 'blog/' in filename:
        return '0.7', 'monthly'
    # Suburb-level pages
    if any(kw in name for kw in [
        'c-bus-repair', 'c-bus-specialist', 'dynalite-programming',
        'emergency-lighting', 'lighting-control'
    ]):
        return '0.7', 'monthly'
    # Generated fault detail pages
    return '0.6', 'monthly'

def get_url_path(filepath, base_dir):
    rel = os.path.relpath(filepath, base_dir).replace('\\', '/')
    # index.html maps to /
    if rel == 'index.html':
        return '/'
    # blog/xxx.html maps to /blog/xxx
    if rel.startswith('blog/'):
        return '/' + rel[:-5]  # strip .html
    # standard pages: strip .html
    return '/' + rel[:-5]

# Collect all HTML files
all_html = []

# Root-level html files
for f in glob.glob(os.path.join(BASE_DIR, '*.html')):
    name = os.path.basename(f)
    if name not in EXCLUDE:
        all_html.append(f)

# Blog subdirectory
blog_dir = os.path.join(BASE_DIR, 'blog')
if os.path.isdir(blog_dir):
    for f in glob.glob(os.path.join(blog_dir, '*.html')):
        name = os.path.basename(f)
        if name not in EXCLUDE:
            all_html.append(f)

print(f'Found {len(all_html)} HTML pages to include in sitemap')

# Build sitemap XML
entries = []
for filepath in sorted(all_html):
    url_path = get_url_path(filepath, BASE_DIR)
    full_url = BASE_URL + url_path
    priority, changefreq = get_priority(filepath)
    entries.append(
        f'  <url>\n'
        f'    <loc>{full_url}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        f'  </url>'
    )

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

{chr(10).join(entries)}

</urlset>"""

sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print(f'Done: sitemap.xml rebuilt with {len(entries)} URLs')
print(f'   File size: {os.path.getsize(sitemap_path) / 1024:.1f} KB')
print(f'   Saved to: {sitemap_path}')
