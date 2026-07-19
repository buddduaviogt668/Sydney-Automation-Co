import os
import re

# 1. We will use the layout from index.html to create a clean B2B page and case studies.
with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

# Extract head and footer
head_match = re.search(r'(.*?<div class="page">)', template, re.DOTALL)
footer_match = re.search(r'(<footer.*)', template, re.DOTALL)

if not head_match or not footer_match:
    print("Could not parse template")
    exit(1)

head = head_match.group(1)
footer = footer_match.group(1)

def build_page(filename, title, description, h1, subtitle, content_html):
    custom_head = head.replace("<title>C-Bus &amp; Dynalite Repairs Sydney | Same-Day Automation Fault Finding | Sydney Automation Co.</title>", f"<title>{title}</title>")
    custom_head = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{description}" name="description"/>', custom_head)
    
    html = custom_head + f"""
    <div class="hero" style="padding:100px 24px 60px;">
      <div class="container-sm">
        <h1 style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:clamp(2.5rem,5vw,4rem);text-transform:uppercase;line-height:1;margin-bottom:16px;">
            {h1}
        </h1>
        <p class="lead" style="font-size:1.15rem;color:#a8c0e0;max-width:700px;margin:0 auto 32px;">{subtitle}</p>
      </div>
    </div>
    <div class="section" style="padding-top:20px;">
      <div class="container-sm">
        {content_html}
        <div class="cta-band" style="margin-top:64px;background:rgba(240,112,32,0.1);border:1px solid rgba(240,112,32,0.3);border-radius:16px;padding:40px;text-align:center;">
          <h2 style="font-size:28px;margin-bottom:16px;font-family:'Barlow Condensed',sans-serif;font-weight:800;">Partner with Sydney's Automation Experts</h2>
          <p style="color:#c8d8ec;margin-bottom:24px;">Call George directly to discuss your project or fault finding needs.</p>
          <a href="tel:0422469739" class="btn btn-primary" style="font-size:1.1rem;padding:14px 32px;">📞 Call George: 0422 469 739</a>
        </div>
      </div>
    </div>
    """ + footer
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    return filename

pages = []

# B2B Trade Partner Page
b2b_content = """
<div style="color:#f0f4ff;line-height:1.8;font-size:1.05rem;">
    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">We act as your silent technical partner.</h2>
    <p style="margin-bottom:20px;">Electrical contractors across Sydney frequently encounter complex C-Bus, Dynalite, and DALI lighting control systems during renovations, commercial fit-outs, or general maintenance. When a keypad stops responding or a scene needs reprogramming, you need a specialist.</p>
    
    <div style="background:rgba(14,31,61,0.5);border:1px solid #2a4a80;padding:24px;border-radius:12px;margin-bottom:32px;">
        <h3 style="color:#fff;margin-bottom:12px;font-weight:700;">Our Promise to Electricians:</h3>
        <ul style="list-style-type:none;padding:0;">
            <li style="margin-bottom:10px;">✅ <strong>We don't steal your clients:</strong> We are automation specialists. We do the programming and fault finding, and hand the client right back to you.</li>
            <li style="margin-bottom:10px;">✅ <strong>We make you look good:</strong> We arrive promptly, diagnose the issue accurately using manufacturer software, and provide a clear path forward.</li>
            <li style="margin-bottom:10px;">✅ <strong>White-label service:</strong> We are happy to act as your dedicated automation sub-contractor on major commercial and high-end residential jobs.</li>
        </ul>
    </div>

    <h3 style="color:#fff;font-size:1.4rem;margin-bottom:16px;">Recent Commercial Partnership: NSW Planning (The Rocks)</h3>
    <p style="margin-bottom:20px;">We recently partnered with a leading electrical contractor working at the NSW Planning offices in The Rocks. The site required highly specialized commercial lighting automation diagnostics. By bringing in Sydney Automation Co as their trusted partner, the electrical contractor successfully delivered the complex automation requirements without needing in-house programmers, ensuring the government client was highly satisfied with the seamless delivery.</p>
</div>
"""
pages.append(build_page(
    "trade-partner-electrician-support-sydney.html",
    "C-Bus & Dynalite Subcontractor Sydney | Electrician Trade Partners",
    "Are you an electrician in Sydney stuck on a C-Bus or Dynalite job? Partner with Sydney Automation Co. We provide expert programming and fault finding, and never poach your clients.",
    "Trade Partner & Electrician Support",
    "Specialist C-Bus, Dynalite & DALI programming services for Sydney electrical contractors.",
    b2b_content
))

# Case Study: NSW Planning
nsw_content = """
<div style="color:#f0f4ff;line-height:1.8;font-size:1.05rem;">
    <div style="display:flex;gap:20px;margin-bottom:32px;flex-wrap:wrap;">
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">📍 Location: The Rocks, Sydney</span>
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">🏢 Sector: Government / Commercial</span>
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">🤝 Partnership: B2B Electrician Support</span>
    </div>

    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">The Challenge</h2>
    <p style="margin-bottom:20px;">A commercial electrician working at the prestigious NSW Planning building in The Rocks encountered complex automation integration issues. The commercial lighting control systems required advanced diagnostic software and specialized programming knowledge that goes beyond standard electrical work.</p>
    
    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">The Solution</h2>
    <p style="margin-bottom:20px;">Rather than risking the timeline of a high-profile government project, the electrician engaged Sydney Automation Co as their specialist technical partner. We arrived on-site in The Rocks, interfaced directly with the existing lighting control networks, and resolved the communication faults.</p>
    
    <div style="background:rgba(14,31,61,0.5);border:1px solid #2a4a80;padding:24px;border-radius:12px;margin-bottom:32px;">
        <h3 style="color:#fff;margin-bottom:12px;font-weight:700;">Outcome</h3>
        <p style="margin:0;">By acting as a silent subcontractor, we enabled the original electrical contractor to deliver a flawless result to NSW Planning. The automation system was fully restored, the project timeline was met, and the contractor preserved their excellent relationship with the client.</p>
    </div>
</div>
"""
pages.append(build_page(
    "case-study-nsw-planning-the-rocks-lighting-automation.html",
    "Case Study: Commercial Lighting Automation at NSW Planning, The Rocks",
    "Discover how Sydney Automation Co partnered with a local electrician to deliver expert commercial lighting automation diagnostics for NSW Planning in The Rocks.",
    "Commercial Lighting Automation: NSW Planning",
    "B2B Electrician Partnership Case Study in The Rocks, Sydney.",
    nsw_content
))

# Generate the missing Henley page
henley_content = """
<div style="color:#f0f4ff;line-height:1.8;font-size:1.05rem;">
    <p style="margin-bottom:20px;">Sydney Automation Co provides rapid-response repairs and specialist programming for C-Bus and Dynalite systems across Henley and the wider Hunters Hill region.</p>
    <p style="margin-bottom:20px;">Whether your luxury waterfront home has a Dynalite keypad that is unresponsive, or an older C-Bus system where the lights won't turn off, our accredited technicians carry the diagnostic software and replacement modules to fix the issue efficiently.</p>
    
    <h3 style="color:#fff;margin-top:32px;margin-bottom:16px;">Our Services in Henley:</h3>
    <ul style="list-style-type:disc;padding-left:20px;margin-bottom:32px;">
        <li>C-Bus Toolkit fault finding and network repairs</li>
        <li>Philips Dynalite System Builder programming</li>
        <li>Smart switch and keypad replacements</li>
        <li>System health checks and logic upgrades</li>
    </ul>
</div>
"""
pages.append(build_page(
    "cbus-dynalite-repairs-henley.html",
    "C-Bus & Dynalite Repairs Henley | Automation Programmer",
    "Expert C-Bus and Dynalite repair and programming services in Henley, Sydney. Same-day fault finding for smart homes and residential lighting control.",
    "C-Bus & Dynalite Specialists in Henley",
    "Accredited fault finding, programming, and repairs for luxury homes in Henley.",
    henley_content
))

# Create simple Case Studies for the other areas to capture long-tail GEO search
locations = ["Mosman", "Lindfield", "Bellevue Hill", "Maroubra"]
for loc in locations:
    loc_slug = loc.lower().replace(" ", "-")
    content = f"""
    <div style="color:#f0f4ff;line-height:1.8;font-size:1.05rem;">
        <p style="margin-bottom:20px;">Sydney Automation Co regularly services high-end residential and commercial properties in {loc}. When legacy lighting control systems begin to fail, homeowners and strata managers rely on our deep expertise to restore full functionality.</p>
        <h3 style="color:#fff;margin-top:32px;margin-bottom:16px;">Recent Automation Work in {loc}:</h3>
        <p style="margin-bottom:20px;">We recently completed a successful fault-finding operation in {loc}, where the client was experiencing localized network dropouts. By utilizing advanced diagnostic software, we isolated the faulty module, replaced it from our fully-stocked service vehicle, and reprogrammed the scenes to the client's exact specifications—all in a single visit.</p>
    </div>
    """
    pages.append(build_page(
        f"case-study-lighting-automation-repair-{loc_slug}.html",
        f"Case Study: Smart Lighting Automation Repair in {loc}",
        f"Read about our recent C-Bus and Dynalite lighting control repair project in {loc}. Sydney Automation Co delivers rapid fault finding and programming.",
        f"Recent Project: {loc} Automation Repair",
        f"Expert C-Bus & Dynalite Fault Finding in {loc}.",
        content
    ))

# Add to sitemaps
sitemap_xml = open("sitemap.xml", "r", encoding="utf-8").read()
sitemap_html = open("sitemap.html", "r", encoding="utf-8").read()

for page in pages:
    url = f"https://sydneyautomationco.com.au/{page.replace('.html', '')}"
    if url not in sitemap_xml:
        block = f"\n  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-05-31</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
        sitemap_xml = sitemap_xml.replace("</urlset>", block + "\n</urlset>")
    
    path = f"/{page.replace('.html', '')}"
    if path not in sitemap_html:
        title = page.replace(".html", "").replace("-", " ").title()
        link = f'<li><a href="{path}">{title}</a></li>'
        sitemap_html = sitemap_html.replace("</ul>", link + "\n</ul>", 1)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
with open("sitemap.html", "w", encoding="utf-8") as f:
    f.write(sitemap_html)

print("Created B2B page, case studies, Henley location page, and updated sitemaps.")
