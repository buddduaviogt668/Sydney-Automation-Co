import os

blogs = [
    "blog-cbus-not-working-repair-guide.html",
    "blog-dynalite-repairs-electrician-sydney.html",
    "blog-dali-lighting-control-system-repair.html",
    "blog-smart-home-automation-sydney-installers.html",
    "blog-car-park-lighting-upgrades-sydney.html",
    "blog-smart-light-switch-replacement-sydney.html"
]

# sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

for blog in blogs:
    url = f"https://sydneyautomationco.com.au/{blog.replace('.html', '')}"
    if url not in sitemap:
        block = f"""
  <url>
    <loc>{url}</loc>
    <lastmod>2026-05-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""
        sitemap = sitemap.replace("</urlset>", block + "\n</urlset>")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

# sitemap.html
with open("sitemap.html", "r", encoding="utf-8") as f:
    sitemap_html = f.read()

for blog in blogs:
    url = f"/{blog.replace('.html', '')}"
    if url not in sitemap_html:
        title = blog.replace("blog-", "").replace(".html", "").replace("-", " ").title()
        link = f'<li><a href="{url}">{title}</a></li>'
        # Add after other blogs if possible
        if '<li><a href="/blog' in sitemap_html:
            # find last blog link
            idx = sitemap_html.rfind('<li><a href="/blog')
            end_idx = sitemap_html.find('</li>', idx) + 5
            sitemap_html = sitemap_html[:end_idx] + "\n" + link + sitemap_html[end_idx:]
        else:
            sitemap_html = sitemap_html.replace("</ul>", link + "\n</ul>", 1)

with open("sitemap.html", "w", encoding="utf-8") as f:
    f.write(sitemap_html)

print("Added new blogs to sitemaps.")
