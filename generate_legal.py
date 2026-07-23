import os
import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract from <head> to end of <nav> and start of <div class="page">
header_pattern = re.compile(r'(.*?<div class="page">)', re.DOTALL)
header_match = header_pattern.search(html)
header = header_match.group(1) if header_match else ''

# Extract footer
footer_pattern = re.compile(r'(<!-- Repair & Emergency Links -->.*|<!-- ===== PREMIUM TESTIMONIALS CAROUSEL ===== -->.*|<footer.*?>.*)', re.DOTALL)
footer_match = footer_pattern.search(html)
footer = footer_match.group(1) if footer_match else ''

# Clean up header title
header_privacy = header.replace('<title>About George Skarmoutsos', '<title>Privacy Policy')
header_terms = header.replace('<title>About George Skarmoutsos', '<title>Terms of Service')
header_sitemap = header.replace('<title>About George Skarmoutsos', '<title>HTML Sitemap')

privacy_content = """
<div class="hero"><div class="container">
<h1>Privacy Policy</h1>
<p class="lead">Last updated: May 2026</p>
</div></div>
<div class="section"><div class="container article-body" style="max-width:800px;margin:0 auto">
<h2>1. Information We Collect</h2>
<p>Sydney Automation Co. collects personal information when you contact us, request a quote, or use our services. This may include your name, phone number, email address, property address, and details about your automation systems.</p>
<h2>2. How We Use Your Information</h2>
<p>We use your information exclusively to provide lighting automation services, communicate regarding appointments, issue invoices, and manage service warranties. We do not sell or rent your personal information to third parties.</p>
<h2>3. Data Security</h2>
<p>We implement appropriate technical and organizational measures to protect your personal data against unauthorized access, alteration, disclosure, or destruction.</p>
<h2>4. Contact Us</h2>
<p>If you have any questions about our Privacy Policy, please contact us at <a href="tel:0422469739">0422 469 739</a> or via our contact form.</p>
</div></div>
</div>
"""

with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(header_privacy + privacy_content + footer)

terms_content = """
<div class="hero"><div class="container">
<h1>Terms of Service</h1>
<p class="lead">Last updated: May 2026</p>
</div></div>
<div class="section"><div class="container article-body" style="max-width:800px;margin:0 auto">
<h2>1. Acceptance of Terms</h2>
<p>By engaging Sydney Automation Co. for any services, you agree to be bound by these Terms of Service. All engagements are subject to a fixed-price scope provided prior to commencement.</p>
<h2>2. Service Delivery</h2>
<p>We provide specialist programming and maintenance for Clipsal C-Bus and Dynalite systems. We partner with licensed electrical contractors for any 240V electrical works required.</p>
<h2>3. Warranties</h2>
<p>All genuine Schneider Electric and Signify hardware supplied and installed by us is covered by the respective manufacturer warranties. Our programming and workmanship carry a 12-month guarantee.</p>
<h2>4. Limitation of Liability</h2>
<p>Sydney Automation Co. is not liable for indirect, incidental, or consequential damages arising from the use or inability to use our services or the hardware we install.</p>
</div></div>
</div>
"""

with open('terms-of-service.html', 'w', encoding='utf-8') as f:
    f.write(header_terms + terms_content + footer)

print("Generated Privacy Policy and Terms of Service.")

# Generate Sitemap HTML and XML
files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('404.html')]
files.sort()

sitemap_links = ""
xml_links = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in files:
    slug = file.replace('.html', '')
    if slug == 'index':
        slug = ''
        file = ''
    else:
        file = '/' + slug
        
    sitemap_links += f'<li><a href="{file}">{slug.replace("-", " ").title() if slug else "Home"}</a></li>\n'
    xml_links += f'  <url>\n    <loc>https://sydneyautomationco.com.au{file}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>{"1.0" if not slug else "0.8"}</priority>\n  </url>\n'

xml_links += '</urlset>'

sitemap_html = f"""
<div class="hero"><div class="container">
<h1>HTML Sitemap</h1>
</div></div>
<div class="section"><div class="container article-body" style="max-width:800px;margin:0 auto">
<ul>
{sitemap_links}
</ul>
</div></div>
</div>
"""

with open('sitemap.html', 'w', encoding='utf-8') as f:
    f.write(header_sitemap + sitemap_html + footer)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml_links)

print("Generated HTML and XML Sitemaps.")

# Ensure robots.txt exists and points to sitemap
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: https://sydneyautomationco.com.au/sitemap.xml\n")
print("Generated robots.txt")

