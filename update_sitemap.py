import os

sitemap_path = 'sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# New entries
new_urls = [
    "https://sydneyautomationco.com.au/blog-ai-cbus-fault-finding-sydney",
    "https://sydneyautomationco.com.au/blog-future-automation-sydney-2026",
    "https://sydneyautomationco.com.au/blog-how-to-partner-cbus-programmer",
    "https://sydneyautomationco.com.au/blog-sutherland-shire-cbus-value-2026",
    "https://sydneyautomationco.com.au/blog-why-consultants-switch-rapix-cbus"
]

# Find the last </urlset>
last_line_idx = -1
for i, line in enumerate(lines):
    if '</urlset>' in line:
        last_line_idx = i
        break

if last_line_idx != -1:
    new_entries = []
    for url in new_urls:
        new_entries.append('  <url>\n')
        new_entries.append(f'    <loc>{url}</loc>\n')
        new_entries.append('    <lastmod>2026-05-06</lastmod>\n')
        new_entries.append('    <changefreq>weekly</changefreq>\n')
        new_entries.append('    <priority>0.7</priority>\n')
        new_entries.append('  </url>\n')
    
    lines = lines[:last_line_idx] + new_entries + lines[last_line_idx:]

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Sitemap updated with blog posts.")
