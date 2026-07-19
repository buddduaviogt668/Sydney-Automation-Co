import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

to_remove = [
    "cbus-not-working-sydney.html",
    "cbus-fault-finding-sydney.html",
    "c-bus-repairs-sydney.html",
    "dynalite-not-working-sydney.html",
    "dynalite-fault-finding-sydney-common-faults.html"
]

# Update sitemap.xml
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    for rm in to_remove:
        # Remove <url> block containing this page
        # Regex to match <url>...rm...</url>
        pattern = r"<url>\s*<loc>[^<]*" + re.escape(rm) + r"[^<]*</loc>.*?</url>"
        xml_content = re.sub(pattern, "", xml_content, flags=re.DOTALL)
        
    with open(sitemap_xml, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    print("Cleaned sitemap.xml")

# Update sitemap.html
sitemap_html = os.path.join(DIR, "sitemap.html")
if os.path.exists(sitemap_html):
    with open(sitemap_html, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # We will remove list items containing the hrefs
    # e.g. <li><a href="rm">...</a></li>
    for rm in to_remove:
        pattern = r"<li>\s*<a href=\"/?" + re.escape(rm) + r"\">.*?</a>\s*</li>"
        html_content = re.sub(pattern, "", html_content, flags=re.DOTALL)
        
        # also try without .html extension in hrefs
        rm_no_ext = rm.replace(".html", "")
        pattern2 = r"<li>\s*<a href=\"/?" + re.escape(rm_no_ext) + r"\">.*?</a>\s*</li>"
        html_content = re.sub(pattern2, "", html_content, flags=re.DOTALL)
        
    with open(sitemap_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Cleaned sitemap.html")
