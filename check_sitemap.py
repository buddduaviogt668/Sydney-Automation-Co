import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

missing = []
for file in files:
    slug = file.replace('.html', '')
    if slug == 'index':
        url = "https://sydneyautomationco.com.au/"
    else:
        url = f"https://sydneyautomationco.com.au/{slug}"
    
    if url not in sitemap:
        missing.append(url)

if not missing:
    print("All HTML pages are in the sitemap.")
else:
    print(f"Missing {len(missing)} pages from sitemap:")
    for url in missing:
        print(url)
