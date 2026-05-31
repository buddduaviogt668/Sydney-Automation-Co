sitemap_xml = open("sitemap.xml", "r", encoding="utf-8").read()
sitemap_html = open("sitemap.html", "r", encoding="utf-8").read()

url = "https://sydneyautomationco.com.au/case-study-cbus-repair-henley"
if url not in sitemap_xml:
    block = f"\n  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-05-31</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
    sitemap_xml = sitemap_xml.replace("</urlset>", block + "\n</urlset>")
    
path = "/case-study-cbus-repair-henley"
if path not in sitemap_html:
    title = "Case Study: C-Bus Repair in Henley"
    link = f'<li><a href="{path}">{title}</a></li>'
    sitemap_html = sitemap_html.replace("</ul>", link + "\n</ul>", 1)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
with open("sitemap.html", "w", encoding="utf-8") as f:
    f.write(sitemap_html)
