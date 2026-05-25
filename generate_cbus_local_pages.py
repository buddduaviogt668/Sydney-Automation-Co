import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

locations = [
    {"name": "Earlwood", "slug": "earlwood"},
    {"name": "Maroubra", "slug": "maroubra"},
    {"name": "Bellevue Hill", "slug": "bellevue-hill"},
    {"name": "The Rocks", "slug": "the-rocks"},
    {"name": "Cronulla", "slug": "cronulla"}
]

generated_urls = []

# Generate C-Bus Repairs pages
repair_template_path = os.path.join(DIR, "cbus-repair-sydney.html")
with open(repair_template_path, 'r', encoding='utf-8') as f:
    repair_template = f.read()

for loc in locations:
    filename = f"cbus-repair-{loc['slug']}.html"
    filepath = os.path.join(DIR, filename)
    
    # Simple replacement: assume template uses "Sydney" and we replace with location name
    # But wait, cbus-repair-sydney.html might have "Sydney" 50 times in various contexts.
    # It's better to replace specific meta tags and H1 to be safe, but a blanket replace is often used for these localized SEO builds.
    
    # We will do a tailored replacement for key tags to ensure quality.
    content = repair_template
    
    # 1. Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>C-Bus Repair {loc["name"]} | Emergency Fault Finding & Service</title>', content)
    
    # 2. Update Meta Description
    content = re.sub(r'name="description" content=".*?"', f'name="description" content="Expert C-Bus repair and fault finding in {loc["name"]}. Same-day response for residential and commercial lighting control systems."', content)
    
    # 3. Update H1
    content = re.sub(r'<h1>.*?</h1>', f'<h1>C-Bus Repair & Service in {loc["name"]}</h1>', content)
    
    # 4. Light replacement in the first intro paragraph (if possible, or just append a strong location signal)
    # We'll just trust the H1 and Meta to do the heavy lifting for local SEO.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    generated_urls.append(filename)


# Generate C-Bus Programmer for Electrician pages
partner_template_path = os.path.join(DIR, "electrician-partner-cbus-dynalite-programming.html")
with open(partner_template_path, 'r', encoding='utf-8') as f:
    partner_template = f.read()
    
for loc in locations:
    filename = f"cbus-programmer-electrician-{loc['slug']}.html"
    filepath = os.path.join(DIR, filename)
    
    content = partner_template
    
    # 1. Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>C-Bus Programmer for Electricians in {loc["name"]} | B2B Partnership</title>', content)
    
    # 2. Update Meta Description
    content = re.sub(r'name="description" content=".*?"', f'name="description" content="Are you an electrician in {loc["name"]} with a C-Bus project? Partner with Sydney\'s leading white-label C-Bus programmers."', content)
    
    # 3. Update H1
    content = re.sub(r'<h1>.*?</h1>', f'<h1>C-Bus Programmer for Electricians in {loc["name"]}</h1>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    generated_urls.append(filename)

# Update Sitemaps
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    for url in generated_urls:
        if url not in xml:
            url_block = f"\n  <url>\n    <loc>https://sydneyautomation.com.au/{url}</loc>\n    <lastmod>2026-05-25</lastmod>\n    <priority>0.80</priority>\n  </url>"
            xml = xml.replace("</urlset>", f"{url_block}\n</urlset>")
            
    with open(sitemap_xml, 'w', encoding='utf-8') as f:
        f.write(xml)

sitemap_html = os.path.join(DIR, "sitemap.html")
if os.path.exists(sitemap_html):
    with open(sitemap_html, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for url in generated_urls:
        if url not in html:
            title = url.replace("-", " ").replace(".html", "").title()
            link_html = f'\n<li><a href="/{url}">{title}</a></li>'
            html = html.replace("</ul>", f"{link_html}\n</ul>", 1)
            
    with open(sitemap_html, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Generated {len(generated_urls)} localized pages and updated sitemaps.")
