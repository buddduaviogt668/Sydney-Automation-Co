import os
import xml.etree.ElementTree as ET
import datetime

# Define namespace
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')

tree = ET.parse("sitemap.xml")
root = tree.getroot()

ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
existing_urls = [url.find('sm:loc', ns).text for url in root.findall('sm:url', ns) if url.find('sm:loc', ns) is not None]

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
exclude = ['404.html', 'suburb-directory-snippet.html']

added = 0
for f in html_files:
    if f in exclude:
        continue
    
    # Special case: index.html -> https://sydneyautomationco.com.au/
    if f == 'index.html':
        loc = "https://sydneyautomationco.com.au/"
    else:
        loc = f"https://sydneyautomationco.com.au/{f[:-5]}"
        
    if loc not in existing_urls:
        url_elem = ET.SubElement(root, "url")
        loc_elem = ET.SubElement(url_elem, "loc")
        loc_elem.text = loc
        
        lastmod_elem = ET.SubElement(url_elem, "lastmod")
        lastmod_elem.text = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        priority = "0.80"
        if f.startswith('c-bus-programmer-') or f.startswith('dynalite-programmer-'):
            priority = "0.70"
        elif f == 'index.html':
            priority = "1.00"
            
        priority_elem = ET.SubElement(url_elem, "priority")
        priority_elem.text = priority
        added += 1

if added > 0:
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"SUCCESS: Added {added} missing pages to sitemap.xml")
else:
    print("Sitemap is already up to date. No new pages to add.")
