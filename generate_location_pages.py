import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

def update_file(filename, old_str, new_str):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Titlecase replace
    content = content.replace(old_str, new_str)
    # Lowercase replace for urls/meta
    content = content.replace(old_str.lower(), new_str.lower())
    # Uppercase
    content = content.replace(old_str.upper(), new_str.upper())
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Update Residential pages
update_file('smart-home-automation-earlwood.html', 'Cremorne', 'Earlwood')
update_file('smart-home-automation-maroubra.html', 'Cremorne', 'Maroubra')

# 2. Update B2B / Partner pages
def make_partner_page(filename, location_name):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Update title
    old_title = "<title>Electrician Partner Program | White-Label C-Bus Programming</title>"
    new_title = f"<title>Electrician Partner Program {location_name} | White-Label C-Bus & Dynalite Programming</title>"
    content = content.replace(old_title, new_title)
    
    # Update meta description
    old_meta = 'name="description" content="Partner with Sydney\'s leading C-Bus and Dynalite programmers"'
    new_meta = f'name="description" content="Partner with {location_name}\'s leading C-Bus and Dynalite programmers"'
    content = content.replace(old_meta, new_meta)
    
    # Update H1
    old_h1 = "<h1>White-Label C-Bus & Dynalite Programming</h1>"
    new_h1 = f"<h1>White-Label C-Bus & Dynalite Programming in {location_name}</h1>"
    content = content.replace(old_h1, new_h1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

make_partner_page('electrician-partner-the-rocks.html', 'The Rocks')
make_partner_page('electrician-partner-cronulla.html', 'Cronulla')

# 3. Add to sitemaps
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    new_urls = [
        "smart-home-automation-earlwood.html",
        "smart-home-automation-maroubra.html",
        "electrician-partner-the-rocks.html",
        "electrician-partner-cronulla.html"
    ]
    
    for url in new_urls:
        if url not in xml:
            url_block = f"\n  <url>\n    <loc>https://sydneyautomation.com.au/{url}</loc>\n    <lastmod>2026-05-25</lastmod>\n    <priority>0.80</priority>\n  </url>"
            # Insert before </urlset>
            xml = xml.replace("</urlset>", f"{url_block}\n</urlset>")
            
    with open(sitemap_xml, 'w', encoding='utf-8') as f:
        f.write(xml)

sitemap_html = os.path.join(DIR, "sitemap.html")
if os.path.exists(sitemap_html):
    with open(sitemap_html, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for url in new_urls:
        if url not in html:
            title = url.replace("-", " ").replace(".html", "").title()
            link_html = f'\n<li><a href="/{url}">{title}</a></li>'
            # Insert before </ul></div> (approximate, let's just insert at the end of the first ul)
            html = html.replace("</ul>", f"{link_html}\n</ul>", 1)
            
    with open(sitemap_html, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully generated location pages and updated sitemaps.")
