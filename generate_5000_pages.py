import os
import re
from datetime import datetime

DIR = r"C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"

VERTICALS = [
    "Pubs Clubs and RSLs",
    "Schools and Learning Hubs",
    "Shopping Centres and Malls",
    "Boutique Retailers and Showrooms",
    "Hospitals and Medical Centres",
    "High-Rise Strata and Luxury Apartments",
    "Industrial Logistics and Warehousing",
    "Government and Heritage Buildings",
    "Corporate Offices and Towers",
    "Data Centres and Tech Hubs"
]

HUBS = [
    "Sydney CBD", "North Sydney", "Parramatta", "Alexandria", "Macquarie Park",
    "Surry Hills", "Newtown", "Penrith", "Cronulla", "Manly",
    "Bondi Junction", "Chatswood", "Liverpool", "Blacktown", "Campbelltown",
    "Bankstown", "Hurstville", "Castle Hill", "Ryde", "Mascot"
]

SYSTEMS = ["C-Bus", "Dynalite", "DALI-2"]

FAULTS = [
    "Automated schedule and timeclock drift",
    "Emergency lighting AFSS non-compliance",
    "Network burden and communication crashes",
    "Daylight harvesting and sensor failure"
]

def clean_url(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s\-]+', '-', s)
    return s.strip('-')

BASE_TEMPLATE_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://sydneyautomationco.com.au/{slug}">
    <link rel="stylesheet" href="/style.css">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Sydney Automation Co.",
      "description": "{description}",
      "url": "https://sydneyautomationco.com.au/{slug}",
      "telephone": "+61422469739",
      "areaServed": {{
        "@type": "Place",
        "name": "{hub}",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{hub}",
          "addressRegion": "NSW",
          "addressCountry": "AU"
        }}
      }},
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "Commercial Automation Services for {vertical}",
        "itemListElement": [
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "{h1}"}}}}
        ]
      }}
    }}
    </script>

    <script type="application/ld+json">
    {faq_schema}
    </script>

    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #0a1628; color: #a8c0e0; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        header {{ background-color: #001f3d; color: #fff; padding: 1rem 0; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2.5em; }}
        .hero {{ background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url('/images/hero-bg.jpg') no-repeat center center/cover; color: #fff; padding: 100px 0; text-align: center; }}
        .hero h2 {{ font-size: 2.6em; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.2em; margin-bottom: 30px; max-width: 800px; margin-left: auto; margin-right: auto; }}
        .cta-button {{ background-color: #f07020; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }}
        .section {{ padding: 60px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        .section h3 {{ color: #fff; font-size: 1.9em; margin-bottom: 20px; }}
        .section p {{ font-size: 1.05em; margin-bottom: 16px; }}
        .faq-item {{ background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); padding: 24px; margin-bottom: 16px; border-radius: 8px; }}
        .faq-item h4 {{ color: #fff; margin-top: 0; font-size: 1.1em; }}
        .faq-item p {{ margin: 0; }}
        .services-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 24px; }}
        .service-card {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(240,112,32,0.2); border-radius: 8px; padding: 20px; }}
        .service-card h4 {{ color: #f07020; margin-top: 0; }}
        .alert-bar {{ background: rgba(240,112,32,0.15); border-left: 4px solid #f07020; padding: 20px; margin: 30px 0; border-radius: 4px; }}
        .cta-block {{ background: linear-gradient(135deg, rgba(240,112,32,0.1) 0%, rgba(77,166,255,0.05) 100%); border: 2px solid #f07020; border-radius: 12px; padding: 30px; margin: 40px 0; text-align: center; }}
        .cta-block h3 {{ color: #fff; margin-top: 0; }}
        .cta-block .cta-button {{ display: inline-block; font-size: 16px; padding: 15px 40px; border-radius: 8px; }}
        .trust-points {{ color: #4da6ff; font-size: 13px; margin-top: 15px; }}
        footer {{ background-color: #001f3d; color: #a8c0e0; text-align: center; padding: 20px 0; margin-top: 40px; }}
    </style>
</head>
<body>
  <div id="sticky-cta-bar" style="
    position:fixed;top:0;left:0;right:0;z-index:99999;
    background:linear-gradient(90deg,#0a2240 0%,#1a3a6e 100%);
    display:flex;align-items:center;justify-content:center;gap:16px;
    padding:10px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.4);
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  ">
    <span style="color:#f0c040;font-size:13px;font-weight:600;white-space:nowrap;">
      ⚡ Enterprise-Grade Automation Support — Available Today
    </span>
    <a href="tel:0422469739" style="
      background:#e8330a;color:#fff;text-decoration:none;
      padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;
      white-space:nowrap;transition:background 0.2s;
    " onclick="gtag&&gtag('event','click',{{event_category:'CTA',event_label:'sticky-call'}})">
      📞 Call George
    </a>
    <a href="/book-service" style="
      background:#fff;color:#0a2240;text-decoration:none;
      padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;
      white-space:nowrap;border:2px solid #fff;
    " onclick="gtag&&gtag('event','click',{{event_category:'CTA',event_label:'sticky-book'}})">
      Book Online →
    </a>
    <button onclick="document.getElementById('sticky-cta-bar').style.display='none'" style="
      background:none;border:none;color:rgba(255,255,255,0.5);
      cursor:pointer;font-size:18px;line-height:1;margin-left:8px;padding:0;
    " aria-label="Close">×</button>
  </div>
  <style>
    body {{ padding-top: 44px !important; }}
    @media (max-width: 600px) {{
      #sticky-cta-bar {{ flex-wrap: wrap; gap: 8px; padding: 8px 12px; }}
      #sticky-cta-bar span {{ font-size: 11px; }}
      #sticky-cta-bar a {{ font-size: 12px; padding: 6px 12px; }}
      body {{ padding-top: 72px !important; }}
      nav {{ top: 72px !important; }}
    }}
  </style>

    <header>
        <div class="container">
            <h1>Sydney Automation Co.</h1>
            <p>Certified B2B Automation Specialists</p>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container">
                <h2>{h1}</h2>
                <p>{hero_desc}</p>
                <a href="/book-service" class="cta-button">Book Your Priority Call-Out &#8594;</a>
            </div>
        </section>

        <div class="container">
            <div class="alert-bar">
                <p style="color: #fff; font-weight: 700; font-size: 16px;">&#9888;&#65039; {system} Emergency in {hub}? Call Now: <span style="color: #f07020; font-size: 18px;">0422 469 739</span></p>
                <p style="color: #a8c0e0; margin-top: 8px; font-size: 14px;">Certified automation technicians. Fast SLA-backed response for {vertical} in {hub}.</p>
            </div>
        </div>

        <section class="section">
            <div class="container">
                {body_html}
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>Frequently Asked Questions — {vertical}</h3>
                {faq_html}
            </div>
        </section>

        <div class="container">
            <div class="cta-block">
                <h3>Secure Your Facilities in {hub} Today</h3>
                <p style="color: #a8c0e0; font-size: 16px; margin-bottom: 20px;">Don't let {fault} disrupt your operations or void your compliance.</p>
                <a href="/book-service" class="cta-button">Book B2B Service &amp; Pay Deposit &#8594;</a>
                <p class="trust-points">&#10003; Priority commercial response &nbsp;|&nbsp; &#10003; Certified technicians &nbsp;|&nbsp; &#10003; Tax invoices provided</p>
            </div>
        </div>
    </main>

<div class="section" style="background:#0a1828; border-top:1px solid #2a4a80;">
  <div class="container">
    <div class="section-header">
      <div class="tag">Transparent B2B Pricing</div>
      <h2>Pricing &amp; Call-Out <span class="accent">Guarantee</span></h2>
      <p class="dim" style="max-width:540px;margin:0 auto">Clear upfront commercial rates with no hidden fees.</p>
    </div>
    
    <div class="grid-2" style="gap:32px; align-items: stretch; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); margin-top: 24px;">
      <div class="card" style="background:#0e1f3d; padding: 24px; border-radius: 8px;">
        <h3 style="margin-bottom:16px;">Commercial Rate Card</h3>
        <ul class="check-list" style="list-style: none; padding: 0;">
          <li style="margin-bottom: 8px;">&#10003; <strong style="color:#f0f4ff;">Consultation &amp; Diagnosis:</strong> $150/hr</li>
          <li style="margin-bottom: 8px;">&#10003; <strong style="color:#f0f4ff;">Programming &amp; Integration:</strong> $150/hr</li>
          <li style="margin-bottom: 8px;">&#10003; <strong style="color:#f0f4ff;">Emergency / AFSS Compliance:</strong> $150/hr + 15% premium</li>
          <li style="margin-bottom: 8px;">&#10003; <strong style="color:#f0f4ff;">Minimum Call-Out:</strong> 3 hours ($450)</li>
        </ul>
        <div style="margin-top:24px; padding:16px; background:rgba(240,112,32,0.1); border-left:3px solid #f07020; border-radius:4px;">
          <h4 style="color:#f07020; font-size:14px; margin-bottom:8px;">B2B Compliance Guarantee</h4>
          <p style="font-size:13px; color:#a8c0e0; line-height:1.5;">We hold active accreditations, full public liability, and provide complete documentation for facility management compliance records.</p>
        </div>
      </div>
      
      <div class="card" style="background:#0e1f3d; padding: 24px; border-radius: 8px;">
        <h3 style="margin-bottom:16px;">Our Commercial Call-Out Guarantee</h3>
        <p class="dim" style="font-size:15px; line-height:1.7; margin-bottom:16px;">We arrive on-site fully equipped with manufacturer diagnostic toolkits and standard replacement commercial modules.</p>
        <p class="dim" style="font-size:15px; line-height:1.7; margin-bottom:24px;">No work proceeds without approval from site management. We resolve complex faults faster to minimize business downtime.</p>
        
        <div class="btns" style="display: flex; gap: 16px; flex-wrap: wrap;">
          <a href="/book-service" class="cta-button" style="padding: 10px 20px;">Book $450 Diagnostic Call</a>
          <a href="tel:0422469739" class="cta-button" style="background: transparent; border: 2px solid #f07020; padding: 8px 18px;">Call 0422 469 739</a>
        </div>
      </div>
    </div>
  </div>
</div>

<footer>
        <div class="container">
            <p>&copy; 2026 Sydney Automation Co. ABN 61 136 364 150. All rights reserved. Servicing {vertical} in {hub}.</p>
            <p><a href="tel:+61422469739" style="color: #f07020;">0422 469 739</a> &nbsp;|&nbsp; <a href="mailto:george@sydneyautomationco.com.au" style="color: #4da6ff;">george@sydneyautomationco.com.au</a></p>
        </div>
    </footer>
</body>
</html>"""


def get_content(vertical, hub, system, fault):
    title = f"{system} {fault} Repair for {vertical} in {hub} | Sydney Automation Co."
    description = f"Expert B2B {system} support for {vertical} dealing with {fault} in {hub}. SLA-backed commercial automation services. Call 0422 469 739."
    h1 = f"{system} Solutions for {fault} in {hub}"
    hero_desc = f"Specialized support for {vertical}. We rapidly diagnose and resolve {fault} to ensure your {hub} facility remains compliant and fully operational."
    
    body_html = f"""<h3>Enterprise-Grade {system} Support for {vertical}</h3>
                <p>In {hub}, {vertical} rely heavily on stable lighting control systems to maintain safety, ambience, and productivity. When you experience {fault}, generic electricians often lack the diagnostic tools required to bring the {system} network back online without business disruption.</p>
                <p>As specialists in B2B automation support, Sydney Automation Co. provides rapid-response fault finding tailored for {vertical}. We understand the compliance and operational urgencies unique to {hub}.</p>"""
    
    q1 = f"How quickly can you address {fault} for {vertical} in {hub}?"
    a1 = f"We offer priority commercial response times for businesses in {hub}. Our technicians are fully equipped to diagnose and repair {system} errors during the initial call-out."
    q2 = f"Are your {system} services compliant with commercial regulations for {vertical}?"
    a2 = f"Yes. We hold all necessary accreditations and insurances required to service {vertical}, ensuring complete documentation and compliance reporting after repairing {fault}."
    
    faq_schema = f"""{{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "{q1}",
          "acceptedAnswer": {{"@type": "Answer", "text": "{a1}"}}
        }},
        {{
          "@type": "Question",
          "name": "{q2}",
          "acceptedAnswer": {{"@type": "Answer", "text": "{a2}"}}
        }}
      ]
    }}"""
    
    faq_html = f"""<div class="faq-item"><h4>{q1}</h4><p>{a1}</p></div>
                   <div class="faq-item"><h4>{q2}</h4><p>{a2}</p></div>"""
                   
    return title, description, h1, hero_desc, body_html, faq_schema, faq_html


def main():
    generated_files = []
    
    for vertical in VERTICALS:
        for hub in HUBS:
            for system in SYSTEMS:
                for fault in FAULTS:
                    slug = clean_url(f"{vertical}-{hub}-{system}-{fault}")
                    title, description, h1, hero_desc, body_html, faq_schema, faq_html = get_content(vertical, hub, system, fault)
                    
                    html_content = BASE_TEMPLATE_START.format(
                        title=title, description=description, slug=slug, hub=hub,
                        h1=h1, hero_desc=hero_desc, body_html=body_html,
                        faq_schema=faq_schema, faq_html=faq_html,
                        system=system, vertical=vertical, fault=fault
                    )
                    filename = f"{slug}.html"
                    filepath = os.path.join(DIR, filename)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(html_content)
                    generated_files.append(filename)
                
    print(f"Generated {len(generated_files)} juggernaut pages.")
    
    # Update sitemap.xml
    sitemap_xml_path = os.path.join(DIR, "sitemap.xml")
    if os.path.exists(sitemap_xml_path):
        with open(sitemap_xml_path, "r", encoding="utf-8", errors="replace") as f:
            xml_content = f.read()
        
        urls_to_add = []
        date_str = datetime.now().strftime("%Y-%m-%d")
        for filename in generated_files:
            url = f"https://sydneyautomationco.com.au/{filename.replace('.html', '')}"
            if url not in xml_content:
                urls_to_add.append(
                    f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{date_str}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n  </url>"
                )
        
        if urls_to_add:
            url_block = "\n".join(urls_to_add)
            xml_content = xml_content.replace("</urlset>", url_block + "\n</urlset>")
            with open(sitemap_xml_path, "w", encoding="utf-8", errors="replace") as f:
                f.write(xml_content)
            print(f"Added {len(urls_to_add)} URLs to sitemap.xml")

    # Update sitemap.html
    sitemap_html_path = os.path.join(DIR, "sitemap.html")
    if os.path.exists(sitemap_html_path):
        with open(sitemap_html_path, "r", encoding="utf-8", errors="replace") as f:
            html_content = f.read()
            
        links_to_add = []
        for filename in generated_files:
            url = f"/{filename.replace('.html', '')}"
            if url not in html_content:
                title = filename.replace("-", " ").replace(".html", "").title()
                links_to_add.append(f'<li><a href="{url}">{title}</a></li>')
                
        if links_to_add:
            link_block = "\n".join(links_to_add)
            html_content = html_content.replace("</ul>", link_block + "\n</ul>", 1)
            with open(sitemap_html_path, "w", encoding="utf-8", errors="replace") as f:
                f.write(html_content)
            print(f"Added {len(links_to_add)} URLs to sitemap.html")

if __name__ == "__main__":
    main()
