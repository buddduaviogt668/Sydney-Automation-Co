
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text) # Remove non-alphanumeric characters
    text = re.sub(r'\s+', '-', text) # Replace spaces with hyphens
    text = re.sub(r'-+', '-', text) # Replace multiple hyphens with single
    return text.strip('-')

def generate_page(title, filename, repo_path):
    page_path = os.path.join(repo_path, filename)
    if not os.path.exists(page_path):
        # Basic HTML template - this will be replaced with actual content later
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="width=device-width,initial-scale=1.0" name="viewport">
    <meta content="C-Bus Programmer Sydney. Accredited C-Bus Programmer based in Menai, Sutherland Shire. Call 0422 469 739." name="description"/>
    <link href="https://sydneyautomationco.com.au/c-bus-programmer-sydney" rel="canonical"/>
    <title>{title} | Sydney Automation Co</title>
    <link href="/favicon.png" rel="icon" type="image/png"/>
    <link href="/favicon.png" rel="apple-touch-icon"/>
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link as="style" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&amp;family=Barlow+Condensed:wght@700;800&amp;display=swap" onload="this.onload=null;this.rel=\'stylesheet\'" rel="preload"/>
    <noscript><link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600&amp;family=Barlow+Condensed:wght@700;800&amp;display=swap" rel="stylesheet"/></noscript>
    <meta content="99c59ffacd177339" name="google-site-verification"/>
    <meta content="website" property="og:type"/>
    <meta content="https://sydneyautomationco.com.au/c-bus-programmer-sydney" property="og:url"/>
    <meta content="C-Bus Programmer Sydney | Accredited Clipsal Specialist" property="og:title"/>
    <meta content="Accredited C-Bus Programmer based in Menai, Sutherland Shire. C-Bus fault finding, programming, commissioning and system design across Greater Sydney. Same-day callouts. Call 0422 469 739." property="og:description"/>
    <meta content="https://sydneyautomationco.com.au/og-image.jpg" property="og:image"/>
    <meta content="en_AU" property="og:locale"/>
    <meta content="Sydney Automation Co." property="og:site_name"/>
    <meta content="summary_large_image" name="twitter:card"/>
    <meta content="AU-NSW" name="geo.region"/>
    <meta content="Menai, Sutherland Shire, Sydney" name="geo.placename"/>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Sydney Automation Co.",
      "url": "https://sydneyautomationco.com.au/c-bus-programmer-sydney",
      "telephone": "+61422469739",
      "email": "service@sydneyautomationco.com.au",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Menai",
        "addressLocality": "Menai",
        "addressRegion": "NSW",
        "postalCode": "2234",
        "addressCountry": "AU"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": -34.0167,
        "longitude": 151.0167
      }},
      "openingHoursSpecification": [
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "07:00",
          "closes": "18:00"
        }}
      ],
      "priceRange": "$$",
      "areaServed": "Sydney",
      "sameAs": [
        "https://www.facebook.com/profile.php?id=61570407305417",
        "https://www.instagram.com/sydneyautomationco/",
        "https://www.linkedin.com/company/sydney-automation-co/"
      ]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sydneyautomationco.com.au/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "C-Bus Programmer Sydney",
          "item": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"
        }}
      ]
    }}
    </script>
    <meta content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" name="robots"/>
    <style>
    /* DROPDOWN NAV */
    nav{{position:fixed;top:40px;left:0;right:0;z-index:1000;background:rgba(14,31,61,0.97);border-bottom:1px solid #2a4a80;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between;font-family:\'Barlow\',sans-serif}}
    .logo{{font-family:\'Barlow Condensed\',sans-serif;font-weight:900;text-transform:uppercase;line-height:1;cursor:pointer;display:inline-flex;flex-direction:column;text-decoration:none;color:inherit}}
    .logo-main{{font-size:20px;color:#fff;letter-spacing:1.5px;display:block}}
    .logo-line{{height:2px;background:#f07020;margin:4px 0;width:100%}}
    .logo-sub{{font-size:9px;color:#a8c0e0;letter-spacing:3px}}
    .nav-links{{display:flex;align-items:center;gap:2px;flex-wrap:nowrap}}
    .nav-links>a,.nav-dd-trigger{{font-size:13px;font-weight:600;color:#a8c0e0;padding:6px 10px;border-radius:6px;white-space:nowrap;transition:color 0.2s,background 0.2s;text-decoration:none;cursor:pointer;background:none;border:none;font-family:\'Barlow\',sans-serif;display:flex;align-items:center;gap:4px}}
    .nav-links>a:hover,.nav-dd-trigger:hover,.nav-links>a.active,.nav-dd-trigger.active{{color:#f0f4ff;background:rgba(240,112,32,0.15)}}
    .nav-cta{{background:#f07020!important;color:#fff!important;border-radius:8px;padding:8px 16px!important;font-size:13px;font-weight:700;text-decoration:none;white-space:nowrap}}
    .nav-cta:hover{{background:#ff8533!important}}
    .nav-dd{{position:relative}}
    .nav-dd-trigger::after{{content:\'▾\';font-size:10px;opacity:0.6}}
    .nav-dd-panel{{display:none;position:absolute;top:calc(100% + 8px);left:0;min-width:240px;background:#0d1e3c;border:1px solid #2a4a80;border-radius:10px;padding:8px;z-index:2000;box-shadow:0 8px 32px rgba(0,0,0,0.4)}}
    </style>
</head>
<body>
    <main>
        <h1>{title}</h1>
        <p>This is a placeholder page for {title}. Content will be added soon.</p>
    </main>
</body>
</html>
"""
        with open(page_path, "w", encoding="utf-8") as outfile:
            outfile.write(html_content)
        print(f"Generated missing page: {page_path}")
    else:
        print(f"Page already exists: {page_path}")

missing_pages_info = [
    ("KNX Protocol Explained: Integration & Programming for Sydney Projects", "knx-protocol-explained-integration-sydney.html"),
    ("DALI-2 Lighting Control: Implementation & Compliance in Commercial Buildings", "dali-2-lighting-control-commercial-buildings.html"),
    ("Smart Home ROI Calculator: Increase Property Value & Save Energy in Sydney", "smart-home-roi-calculator-sydney.html"),
    ("Invisible Automation & Heritage Retrofitting for Paddington & Glebe Homes", "invisible-automation-heritage-retrofitting-sydney.html"),
]

repo_path = "/home/ubuntu/Sydney-Automation-Co"

for title, filename in missing_pages_info:
    generate_page(title, filename, repo_path)

print("Missing page generation script finished.")
