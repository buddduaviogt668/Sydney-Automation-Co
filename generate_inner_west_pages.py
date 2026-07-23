import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

inner_west_suburbs = [
    {"name": "Balmain", "slug": "balmain"},
    {"name": "Leichhardt", "slug": "leichhardt"},
    {"name": "Newtown", "slug": "newtown"},
    {"name": "Marrickville", "slug": "marrickville"},
    {"name": "Haberfield", "slug": "haberfield"},
    {"name": "Annandale", "slug": "annandale"},
    {"name": "Glebe", "slug": "glebe"},
    {"name": "Rozelle", "slug": "rozelle"},
    {"name": "Lilyfield", "slug": "lilyfield"},
    {"name": "Drummoyne", "slug": "drummoyne"},
    {"name": "Five Dock", "slug": "five-dock"},
    {"name": "Strathfield", "slug": "strathfield"},
    {"name": "Burwood", "slug": "burwood"},
    {"name": "Concord", "slug": "concord"}
]

generated_urls = []

# Templates
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

for loc in inner_west_suburbs:
    name = loc['name']
    slug = loc['slug']
    
    # 1. Smart Home
    generate(
        f"smart-home-automation-{slug}.html", 
        smart_home_template,
        f"Smart Home Automation {name} | C-Bus & Dynalite Experts",
        f"Premium smart home automation upgrades, repairs, and programming in {name}. Specialists in C-Bus and Philips Dynalite.",
        f"Smart Home Automation in {name}"
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
        f"Expert Philips Dynalite repair and fault finding in {name}. Same-day response for luxury residential and commercial systems.",
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

# Update Sitemaps
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    for url in generated_urls:
        if url not in xml:
            url_block = f"\n  <url>\n    <loc>https://sydneyautomation.com.au/{url}</loc>\n    <lastmod>2026-05-25</lastmod>\n    <priority>0.75</priority>\n  </url>"
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

print(f"Generated {len(generated_urls)} Inner West pages and updated sitemaps.")
