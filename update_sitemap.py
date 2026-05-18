import xml.etree.ElementTree as ET
import datetime

# Define namespace
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')

tree = ET.parse("sitemap.xml")
root = tree.getroot()

# The namespace
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

new_pages = [
    "automation-sydney",
    "hospitality-automation-sydney",
    "cbus-programming-chatswood",
    "lighting-control-rose-bay",
    "smart-home-installation-bellevue-hill",
    "c-bus-programmer-caringbah",
    "c-bus-programmer-engadine",
    "c-bus-programmer-eastern-suburbs"
]

existing_urls = [url.find('sm:loc', ns).text for url in root.findall('sm:url', ns)]

added = 0
for page in new_pages:
    loc = f"https://sydneyautomationco.com.au/{page}"
    if loc not in existing_urls:
        url_elem = ET.SubElement(root, "url")
        loc_elem = ET.SubElement(url_elem, "loc")
        loc_elem.text = loc
        
        lastmod_elem = ET.SubElement(url_elem, "lastmod")
        lastmod_elem.text = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        priority_elem = ET.SubElement(url_elem, "priority")
        priority_elem.text = "0.80"
        added += 1

if added > 0:
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Added {added} pages to sitemap")
else:
    print("No new pages to add")
