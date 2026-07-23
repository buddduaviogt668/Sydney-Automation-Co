import os
import json

with open('seo/page_categories.json') as f:
    cats = json.load(f)

def fmt_name(slug):
    """Convert slug to readable label."""
    if slug == "tech-library.html":
        return "Search Technical Library (480+ Guides)"
    return slug.replace('-', ' ').replace('cbus', 'C-Bus').replace('dynalite', 'Dynalite').replace('nsw', 'NSW').replace('sydney', 'Sydney').replace('afss', 'AFSS').title()

def build_link_grid(pages, base_url="https://sydneyautomationco.com.au"):
    html = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">\n'
    for p in pages:
        label = fmt_name(p)
        html += f'  <a href="/{p}" style="display:block;background:#0e1f3d;border:1px solid #1a2a4a;border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.borderColor=\'#f07020\';this.style.color=\'#f07020\'" onmouseout="this.style.borderColor=\'#1a2a4a\';this.style.color=\'#a8c0e0\'">{label}</a>\n'
    html += '</div>\n'
    return html

sections = [
    {
        "id": "core",
        "icon": "⚡",
        "title": "Core Services",
        "desc": "Our primary accredited service pillars covering C-Bus programming, Dynalite programming, emergency repairs, and AFSS compliance across Greater Sydney.",
        "pages": cats["core"]
    },
    {
        "id": "strategic",
        "icon": "🎯",
        "title": "Specialist Hubs & Strategic Resources",
        "desc": "Competitor migration guides, system rescue protocols, second opinion audits, architect specification portals, electrician partner programs, and interactive cost calculators.",
        "pages": cats["strategic"]
    },
    {
        "id": "fault",
        "icon": "🚨",
        "title": "Emergency Fault Code Diagnostics",
        "desc": "Dedicated diagnostic pages for every critical C-Bus and Dynalite error symptom — from flashing PCI indicator LEDs to buzzing relay contactors and toolkit connection failures.",
        "pages": cats["fault"]
    },
    {
        "id": "tech-library",
        "icon": "📚",
        "title": "Technical Troubleshooting Library (480+ Guides)",
        "desc": "Detailed component-level troubleshooting guides for every combination of Clipsal C-Bus and Signify Dynalite hardware parts and failure symptoms.",
        "pages": ["tech-library.html"]
    },
    {
        "id": "commercial",
        "icon": "🏢",
        "title": "Commercial, Strata & Warehouse Hubs",
        "desc": "Specialized service hubs for strata managers, building managers, facility directors, operations managers, and warehouse logistics teams across NSW.",
        "pages": cats["commercial"]
    },
    {
        "id": "blogs",
        "icon": "📰",
        "title": "Expert Articles & Local Authority Blogs",
        "desc": "In-depth technical articles, area-specific guides, and industry thought leadership covering residential, commercial, strata, and regional NSW markets.",
        "pages": cats["blogs"]
    },
    {
        "id": "cbus",
        "icon": "🔷",
        "title": "C-Bus Programmer — Suburb Service Pages",
        "desc": "Accredited Clipsal C-Bus programming, repair, and maintenance services across every major suburb and region of Greater Sydney and NSW.",
        "pages": cats["cbus"]
    },
    {
        "id": "dynalite",
        "icon": "💡",
        "title": "Signify Dynalite Programmer — Suburb Service Pages",
        "desc": "Accredited Signify Dynalite programming, DyNet commissioning, and keypad configuration services across every major suburb and region of Greater Sydney and NSW.",
        "pages": cats["dynalite"]
    },
    {
        "id": "dynalite_repair",
        "icon": "🛠️",
        "title": "Dynalite Regional Repair Services",
        "desc": "Dedicated Signify Dynalite repair and emergency programming support across Regional NSW including the Southern Highlands, Illawarra, and Central Coast.",
        "pages": cats["dynalite_repair"]
    }
]

# Build the full hub page
sections_html = ""
for s in sections:
    sections_html += f"""
<section id="{s['id']}" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">{s['icon']}</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">{s['title']}</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">{s['desc']}</p>
    </div>
  </div>
  {build_link_grid(s['pages'])}
</section>
"""

total = sum(len(s['pages']) for s in sections)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>All Services Hub | Sydney Automation Co. | {total}+ C-Bus &amp; Dynalite Pages</title>
  <meta name="description" content="Complete directory of all {total}+ C-Bus, Dynalite, DALI, strata, commercial, and warehouse lighting automation services by Sydney Automation Co. across NSW."/>
  <link rel="canonical" href="https://sydneyautomationco.com.au/services-hub"/>
  <meta property="og:url" content="https://sydneyautomationco.com.au/services-hub"/>
  <meta property="og:title" content="All Services Hub | Sydney Automation Co."/>
  <meta property="og:description" content="The complete directory of all {total}+ accredited C-Bus, Dynalite, and DALI services by Sydney Automation Co. across NSW."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:'Inter',sans-serif;background:#070f1e;color:#e0e0e0;line-height:1.6}}
    a{{color:#f07020;text-decoration:none}}
    a:hover{{text-decoration:underline}}
    .nav-bar{{background:rgba(7,15,30,0.97);border-bottom:1px solid #1a2a4a;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}}
    .nav-logo{{font-family:'Barlow Condensed',sans-serif;font-size:22px;font-weight:900;color:#fff}}
    .nav-logo span{{color:#f07020}}
    .nav-links{{display:flex;gap:24px;list-style:none}}
    .nav-links a{{color:#a8c0e0;font-size:14px;font-weight:600;transition:color 0.2s}}
    .nav-links a:hover{{color:#f07020;text-decoration:none}}
    .hero{{background:linear-gradient(135deg,#0e1f3d 0%,#071629 60%,#0a0f1e 100%);padding:80px 24px 60px;text-align:center;border-bottom:1px solid #1a2a4a}}
    .hero h1{{font-family:'Barlow Condensed',sans-serif;font-size:clamp(32px,5vw,60px);font-weight:900;color:#fff;margin-bottom:16px;line-height:1.05}}
    .hero h1 span{{color:#f07020}}
    .hero p{{font-size:17px;color:#a8c0e0;max-width:600px;margin:0 auto 28px;line-height:1.8}}
    .toc{{background:#0a1628;border:1px solid #1a2a4a;border-radius:12px;padding:28px;margin:40px auto;max-width:1100px;display:flex;flex-wrap:wrap;gap:12px}}
    .toc a{{background:#132647;border:1px solid #2a4a80;border-radius:6px;padding:8px 16px;font-size:13px;font-weight:600;color:#a8c0e0;text-decoration:none;transition:all 0.2s}}
    .toc a:hover{{background:#f07020;border-color:#f07020;color:#fff}}
    .content{{max-width:1100px;margin:0 auto;padding:60px 24px}}
    .cta-bar{{background:linear-gradient(135deg,#f07020,#cc5500);padding:48px 24px;text-align:center;margin-top:60px}}
    .cta-bar h2{{font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,42px);font-weight:900;color:#fff;margin-bottom:12px}}
    .cta-bar p{{color:rgba(255,255,255,0.85);font-size:16px;margin-bottom:24px}}
    .cta-btn{{background:#fff;color:#f07020;font-weight:900;font-size:17px;padding:14px 32px;border-radius:8px;text-decoration:none;display:inline-block}}
    .footer{{background:#040c1a;border-top:1px solid #1a2a4a;padding:32px 24px;text-align:center;color:#6a8cb5;font-size:13px}}
    @media(max-width:700px){{.nav-links{{display:none}}}}
  </style>
</head>
<body>

<nav class="nav-bar">
  <div class="nav-logo">Sydney Automation <span>Co.</span></div>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/c-bus-programmer-sydney">C-Bus</a></li>
    <li><a href="/dynalite-programmer-sydney">Dynalite</a></li>
    <li><a href="/c-bus-repairs-sydney">Repairs</a></li>
    <li><a href="/afss-testing-sydney">AFSS</a></li>
    <li><a href="/about-sydney-automation-co">About</a></li>
  </ul>
</nav>

<div class="hero">
  <h1>The Complete<br/><span>Sydney Automation Co. Services Hub</span></h1>
  <p>Your one-stop directory to all {total}+ accredited C-Bus, Signify Dynalite, DALI-2, strata, commercial, warehouse, and suburb-specific lighting automation services across Greater Sydney and Regional NSW.</p>
  <p style="font-size:14px;color:#6a8cb5;margin-top:-12px;">Serving <strong style="color:#f07020">418+ locations</strong> across NSW · Emergency: <a href="tel:0422469739" style="color:#f07020;font-weight:700">0422 469 739</a> · <a href="https://cbusnotworking.com.au" target="_blank" style="color:#f07020;font-weight:700">cbusnotworking.com.au</a></p>
</div>

<div class="toc">
  <strong style="color:#fff;font-size:14px;align-self:center;margin-right:8px;">Jump to:</strong>
  <a href="#core">Core Services</a>
  <a href="#strategic">Specialist Hubs</a>
  <a href="#fault">Fault Diagnostics</a>
  <a href="#tech-library">Technical Library</a>
  <a href="#commercial">Commercial & Strata</a>
  <a href="#blogs">Expert Blogs</a>
  <a href="#cbus">C-Bus Suburbs</a>
  <a href="#dynalite">Dynalite Suburbs</a>
  <a href="#dynalite_repair">Regional Repairs</a>
</div>

<div class="content">
{sections_html}
</div>

<div class="cta-bar">
  <h2>Can't Find Your Suburb or Service?</h2>
  <p>Call us directly — we service every corner of Greater Sydney and Regional NSW.</p>
  <a class="cta-btn" href="tel:0422469739">📞 0422 469 739</a>
  &nbsp;&nbsp;
  <a style="color:rgba(255,255,255,0.85);font-size:15px;font-weight:600;display:inline-block;margin-top:12px;" href="https://cbusnotworking.com.au" target="_blank">Emergency Breakdown → cbusnotworking.com.au</a>
</div>

<footer class="footer">
  <p>© 2025 Sydney Automation Co. | ABN: Available on request | Licensed Electrical Contractor NSW | Menai NSW 2234</p>
  <p style="margin-top:8px"><a href="/">Home</a> · <a href="/c-bus-programmer-sydney">C-Bus Programming</a> · <a href="/dynalite-programmer-sydney">Dynalite Programming</a> · <a href="/c-bus-repairs-sydney">Repairs</a> · <a href="/about-sydney-automation-co">About Us</a></p>
</footer>

</body>
</html>"""

with open('services-hub.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"SUCCESS: services-hub.html generated with {total} linked service pages.")
