import os

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"
BASE = "https://sydneyautomationco.com.au"

# Add to sitemap.xml
xml_path = os.path.join(DIR, "sitemap.xml")
if os.path.exists(xml_path):
    content = open(xml_path, encoding='utf-8').read()
    if '/accessibility' not in content:
        url_block = """
  <url>
    <loc>https://sydneyautomationco.com.au/accessibility</loc>
    <lastmod>2026-05-26</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>"""
        content = content.replace("</urlset>", url_block + "\n</urlset>")
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Added /accessibility to sitemap.xml")
    else:
        print("/accessibility already in sitemap.xml")

# Add to sitemap.html
html_path = os.path.join(DIR, "sitemap.html")
if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    if '/accessibility' not in content:
        link = '\n<li><a href="/accessibility">Accessibility Statement</a></li>'
        # Insert near privacy-policy entry
        if '/privacy-policy' in content:
            content = content.replace(
                '<li><a href="/privacy-policy"',
                link + '\n<li><a href="/privacy-policy"',
                1
            )
        else:
            content = content.replace("</ul>", link + "\n</ul>", 1)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Added /accessibility to sitemap.html")
    else:
        print("/accessibility already in sitemap.html")

print("Done.")
