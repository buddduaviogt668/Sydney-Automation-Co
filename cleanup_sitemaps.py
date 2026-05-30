import re

d = [
    'cbus-repair-wetherill-park-industrial.html', 
    'industrial-automation-lighting-smithfield.html', 
    'industrial-lighting-control-western-sydney.html', 
    'blog-western-sydney-warehouse-lighting-repairs.html', 
    'warehouse-energy-optimization-cbus-dynalite.html', 
    'warehouse-lighting-automation-sydney.html', 
    'warehouse-lighting-control-eastern-creek.html'
]

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    xml = f.read()

for item in d:
    xml = re.sub(r'<url>\s*<loc>[^<]*' + item + r'[^<]*</loc>.*?</url>', '', xml, flags=re.DOTALL)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)

with open('sitemap.html', 'r', encoding='utf-8') as f:
    html = f.read()

for item in d:
    html = re.sub(r'<li>\s*<a href="[^"]*' + item + r'[^"]*">.*?</a>\s*</li>', '', html, flags=re.DOTALL | re.IGNORECASE)

with open('sitemap.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleaned up sitemaps.")
