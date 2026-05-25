import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

# 1. DELETE ORPHANED DYNALITE PAGE
dynalite_not_working = os.path.join(DIR, "dynalite-not-working-sydney.html")
if os.path.exists(dynalite_not_working):
    os.remove(dynalite_not_working)
    print(f"Deleted {dynalite_not_working}")

# 2. FIX CANNIBALIZATION IN HOSPITALITY PAGE
hospitality_path = os.path.join(DIR, "hospitality-automation-sydney.html")
if os.path.exists(hospitality_path):
    with open(hospitality_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_title = "<title>C-Bus Programmer Sydney | Accredited Clipsal Specialist</title>"
    new_title = "<title>Hospitality Automation Sydney | C-Bus & Dynalite for Hotels & Restaurants</title>"
    content = content.replace(old_title, new_title)
    
    with open(hospitality_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed title cannibalization on hospitality-automation-sydney.html")

# 3. GENERATE INNER CITY PAGES
inner_city = [
    {"name": "Sydney CBD", "slug": "sydney-cbd"},
    {"name": "Surry Hills", "slug": "surry-hills"},
    {"name": "Darlinghurst", "slug": "darlinghurst"},
    {"name": "Redfern", "slug": "redfern"},
    {"name": "Pyrmont", "slug": "pyrmont"},
    {"name": "Ultimo", "slug": "ultimo"},
    {"name": "Haymarket", "slug": "haymarket"},
    {"name": "Potts Point", "slug": "potts-point"},
    {"name": "Woolloomooloo", "slug": "woolloomooloo"},
    {"name": "Paddington", "slug": "paddington"},
    {"name": "Alexandria", "slug": "alexandria"},
    {"name": "Waterloo", "slug": "waterloo"},
    {"name": "Zetland", "slug": "zetland"}
]

generated_urls = []

with open(os.path.join(DIR, "smart-home-automation-cremorne.html"), 'r', encoding='utf-8') as f:
    smart_home_template = f.read()
    
with open(os.path.join(DIR, "cbus-repair-sydney.html"), 'r', encoding='utf-8') as f:
    cbus_repair_template = f.read()

with open(os.path.join(DIR, "dynalite-repair-sydney.html"), 'r', encoding='utf-8') as f:
    dynalite_repair_template = f.read()

with open(os.path.join(DIR, "electrician-partner-cbus-dynalite-programming.html"), 'r', encoding='utf-8') as f:
    partner_template = f.read()

def generate(filename, template, title, meta, h1):
    filepath = os.path.join(DIR, filename)
    content = template
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'name="description" content=".*?"', f'name="description" content="{meta}"', content)
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{h1}</h1>', content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    generated_urls.append(filename)

for loc in inner_city:
    name = loc['name']
    slug = loc['slug']
    
    # 1. Smart Home / Strata Automation (Inner City has high Strata concentration)
    generate(
        f"smart-home-automation-{slug}.html", 
        smart_home_template,
        f"Smart Home & Strata Automation {name} | C-Bus & Dynalite",
        f"Premium smart home and luxury strata automation upgrades, repairs, and programming in {name}. Specialists in C-Bus and Philips Dynalite.",
        f"Smart Home & Strata Automation in {name}"
    )
    
    # 2. C-Bus Repair
    generate(
        f"cbus-repair-{slug}.html",
        cbus_repair_template,
        f"C-Bus Repair {name} | Emergency Fault Finding & Service",
        f"Expert C-Bus repair and fault finding in {name}. Same-day response for residential and commercial lighting control systems.",
        f"C-Bus Repair & Service in {name}"
    )
    
    # 3. Dynalite Repair
    generate(
        f"dynalite-repair-{slug}.html",
        dynalite_repair_template,
        f"Dynalite Repair {name} | Emergency Fault Finding & Service",
        f"Expert Philips Dynalite repair and fault finding in {name}. Same-day response for luxury apartments and commercial systems.",
        f"Dynalite Repair & Service in {name}"
    )
    
    # 4. Electrician Partner
    generate(
        f"cbus-programmer-electrician-{slug}.html",
        partner_template,
        f"C-Bus Programmer for Electricians in {name} | B2B Partnership",
        f"Are you an electrician in {name} with a C-Bus project? Partner with Sydney's leading white-label C-Bus programmers.",
        f"C-Bus Programmer for Electricians in {name}"
    )

# 4. UPDATE SITEMAPS
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

print(f"Generated {len(generated_urls)} Inner City pages and updated sitemaps.")
