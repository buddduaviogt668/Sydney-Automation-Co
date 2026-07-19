#!/usr/bin/env python3
"""Generate 16 service pages from hospitality-automation-sydney.html template."""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("hospitality-automation-sydney.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find split points
emer_arrow = html.index("Emergency Repair \u2192")
tag_end = html.index("</a>", emer_arrow) + 4
for _ in range(3):
    tag_end = html.index("</div>", tag_end) + 6
PREFIX = html[:tag_end]
PREFIX_END = tag_end

ORIG_TITLE = '<title>Hospitality Automation Sydney 2026 | C-Bus & Dynalite for Hotels & Restaurants</title>'
ORIG_META = '<meta content="C-Bus Programmer Sydney. Accredited C-Bus Programmer based in Menai, Sutherland Shire. Call 0422 469 739." name="description"/>'
ORIG_CANONICAL = '<link rel="canonical" href="https://sydneyautomationco.com.au/hospitality-automation-sydney"/>'
ORIG_H1 = '<h1>C-Bus Programming<br/><span class="accent">&amp; Commissioning</span></h1>'
ORIG_LEAD = '<p class="lead">Accredited C-Bus Programmers. Same-day fault finding. Fixed-price programming. Based in Menai \u2014 covering all of Greater <a href="/" style="color:#fff; text-decoration:underline;">Sydney</a>.</p>'
ORIG_LEDE_KW = '<p class="lede-kw" style="font-size:0.9em;color:#a8c0e0;margin-top:0.5rem;">Need urgent repairs? Our <a href="/cbus-fault-finder" style="font-weight:700;color:#f07020;text-decoration:underline;">Interactive Fault Finder</a> handles diagnostic assessment in seconds.</p>'

body_start = html.index('<div class="section" style="background:#001428">', PREFIX_END)
suffix_start = html.index("<!-- Competitive Dominance Section -->")
BODY_TPL_BEFORE = html[body_start:suffix_start]
SUFFIX = html[suffix_start:]

seo_comment = SUFFIX.index("<!-- SEO INTERNAL LINKING BOOST -->")
seo_div = SUFFIX.index('<div style="background:#0b1628;', seo_comment)
inner = SUFFIX.index("</div>", seo_div) + 6
outer = SUFFIX.index("</div>", inner) + 6
SEO_END = outer

faq_start = SUFFIX.index('<section class="faq-section"')
faq_end = SUFFIX.index("</section>", faq_start) + 10

BEFORE_SEO = SUFFIX[:seo_comment]
BETWEEN_SEO_FAQ = SUFFIX[SEO_END:faq_start]
AFTER_FAQ = SUFFIX[faq_end:]

def sec1(topic, heading, p1, p2, features, c1t, c1d, c2t, c2d, c3t, c3d):
    feat_lis = "\n".join("<li>" + f + "</li>" for f in features)
    return (
        '<div class="section" style="background:#001428">\n'
        '<div class="container">\n'
        '<div class="grid-2" style="align-items:center;gap:48px">\n'
        '<div>\n'
        '    <div class="tag" style="background: rgba(240,112,32,0.1); color: #f07020; border: 1px solid rgba(240,112,32,0.3);">' + topic + '</div>\n'
        '    <h2 style="font-family: \'Barlow Condensed\', sans-serif; font-size: 42px; margin-bottom: 24px;">' + heading + '</h2>\n'
        '    <p style="color:#a8c0e0;line-height:1.8;margin-bottom:16px; font-size: 17px;">' + p1 + '</p>\n'
        '    <p style="color:#a8c0e0;line-height:1.8;margin-bottom:24px; font-size: 17px;">' + p2 + '</p>\n'
        '<h3 style="margin-bottom:12px">Key features:</h3>\n'
        '<ul style="color:#a8c0e0;padding-left:18px;line-height:2;margin-bottom:24px">\n' + feat_lis + '\n</ul>\n'
        '</div>\n<div>\n'
        '<div class="card" style="margin-bottom:16px">\n<div class="tag" style="margin-bottom:12px">Service</div>\n<h3>' + c1t + '</h3>\n<p style="color:#a8c0e0;font-size:14px;line-height:1.7">' + c1d + '</p>\n</div>\n'
        '<div class="card" style="margin-bottom:16px">\n<div class="tag" style="margin-bottom:12px">Experience</div>\n<h3>' + c2t + '</h3>\n<p style="color:#a8c0e0;font-size:14px;line-height:1.7">' + c2d + '</p>\n</div>\n'
        '<div class="card">\n<div class="tag" style="margin-bottom:12px">Coverage</div>\n<h3>' + c3t + '</h3>\n<p style="color:#a8c0e0;font-size:14px;line-height:1.7">' + c3d + '</p>\n</div>\n'
        '</div>\n</div>\n</div>\n</div>'
    )

def sec2(cards):
    items = ""
    for icon, title, desc, link in cards:
        items += (
            '<div class="card">\n<div class="icon-box">' + icon + '</div>\n'
            '<h3>' + title + '</h3>\n'
            '<p class="dim" style="font-size:14px;line-height:1.7">' + desc + '</p>\n'
            '<a href="' + link + '" onmouseout="this.style.color=\'#f07020\'" onmouseover="this.style.color=\'#ff8533\'" style="color:#f07020;font-weight:700;font-size:14px;text-decoration:none">Learn More \u2192</a>\n</div>\n'
        )
    return (
        '<div class="section">\n<div class="container">\n<div class="section-header">\n'
        '<h2>' + cards[0][1] + ' <span class="accent">' + cards[0][1] + '</span></h2>\n'
        '<p class="dim">Professional ' + cards[0][1].lower() + ' services across Greater Sydney.</p>\n</div>\n<div class="grid-3">\n'
        + items + '</div>\n</div>\n</div>'
    )

def sec3(items):
    cards = ""
    for icon, text in items:
        cards += '<div class="card" style="padding:16px 20px"><p style="font-weight:600">' + icon + ' ' + text + '</p></div>\n'
    return (
        '<div class="section" style="background:#001428">\n<div class="container">\n<div class="section-header">\n'
        '<h2>Why Choose Sydney Automation Co. <span class="accent">for ' + items[0][1] + '</span></h2>\n'
        '<p class="dim">Every project benefits from our deep technical expertise, local knowledge and commitment to quality.</p>\n</div>\n<div class="grid-3">\n'
        + cards + '</div>\n</div>\n</div>'
    )

def sec4(suburbs=None):
    if suburbs is None:
        suburbs = ["Menai", "Sutherland", "Miranda", "Cronulla", "Caringbah", "Gymea",
                    "Engadine", "Eastern Suburbs", "North Shore", "Northern Beaches",
                    "Inner West", "Hills District", "Parramatta", "St George"]
    cards = "".join('<div class="suburb-card"><h4>' + s + '</h4></div>' for s in suburbs)
    return (
        '<div class="section">\n<div class="container">\n<div class="section-header">\n'
        '<h2>Service Area <span class="accent">Across Sydney</span></h2>\n'
        '<p class="dim">Based in Menai \u2014 fastest response times in the Sutherland Shire. Same-day coverage across Greater Sydney with no travel surcharge in the Shire.</p>\n</div>\n'
        '<div class="suburb-grid">\n' + cards + '\n</div>\n'
        '<p class="dim" style="margin-top:16px;text-align:center;font-size:14px">No travel surcharge within the Sutherland Shire. Call to confirm coverage for your suburb.</p>\n</div>\n</div>'
    )

def sec5(heading, desc, links):
    link_items = "".join(
        '<a href="' + url + '" style="background:#0d2444;color:#f07020;padding:10px 16px;border-radius:8px;font-weight:700;font-size:14px;text-decoration:none;border:1px solid #f0702030">' + emoji + ' ' + text + '</a>\n'
        for url, emoji, text in links
    )
    return (
        '<div class="section" style="background:#001428">\n<div class="container">\n<div class="cta-band">\n'
        '<h2>' + heading + '</h2>\n'
        '<p style="color:#a8c0e0;margin-bottom:28px;font-size:17px">' + desc + '</p>\n'
        '<div style="margin-top:40px;padding:28px 32px;background:#001a3a;border-radius:12px;border:1px solid #2a4a80">\n'
        '<div style="font-family:\'Barlow Condensed\',sans-serif;font-weight:800;font-size:13px;letter-spacing:1px;text-transform:uppercase;color:#6a8cb5;margin-bottom:16px">Related Services</div>\n'
        '<div style="display:flex;flex-wrap:wrap;gap:10px">\n' + link_items + '</div>\n</div>\n'
        '<div class="btns" style="justify-content:center;margin-top:28px">\n'
        '<a class="btn btn-primary" href="tel:0422469739">\U0001f4de Call Now \u2014 0422 469 739</a>\n'
        '<a class="btn btn-outline" href="tel:0422469739">\U0001f4de 0422 469 739</a>\n</div>\n</div>\n</div>\n</div>'
    )

def build_faq(qas):
    items = ""
    for q, a in qas:
        items += (
            '<div class="faq-item" style="border-bottom:1px solid #2a4a80;padding:16px 0">\n'
            '<div class="faq-q" style="font-weight:700;color:#f0f4ff;font-size:16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center">\n' + q + '\n'
            '<span style="color:#f07020;font-size:20px;flex-shrink:0;margin-left:12px">+</span>\n</div>\n'
            '<div class="faq-a" style="color:#a8c0e0;font-size:15px;line-height:1.7;margin-top:10px;display:none">' + a + '</div>\n</div>\n'
        )
    return (
        '<section class="faq-section" style="background:#0e1f3d;padding:48px 0">\n'
        '<div class="container" style="max-width:860px;margin:0 auto;padding:0 24px">\n'
        '<h2 style="font-family:\'Barlow Condensed\',sans-serif;font-size:32px;font-weight:900;color:#f0f4ff;margin-bottom:8px">Frequently Asked Questions</h2>\n'
        '<p style="color:#a8c0e0;margin-bottom:32px">Common questions about our services. Can\'t find your answer? <a href="/contact" style="color:#f07020">Contact us</a> or call <a href="tel:0422469739" style="color:#f07020">0422 469 739</a>.</p>\n'
        '<div class="faq-list">\n' + items + '</div>\n</div>\n</section>'
    )

def build_seo(links):
    items = "".join(
        '    <a href="' + url + '" style="color:#f0f4ff;text-decoration:none;border-bottom:1px solid #f07020;">' + text + '</a>\n'
        for url, text in links
    )
    return (
        '<!-- SEO INTERNAL LINKING BOOST -->\n'
        '<div style="background:#0b1628;padding:40px 24px;border-top:1px solid rgba(240,112,32,0.2);">\n'
        '  <div style="max-width:1200px;margin:0 auto;display:flex;flex-wrap:wrap;gap:20px;justify-content:center;font-size:13px;font-weight:600;color:#a8c0e0;">\n'
        '    <span style="color:#f07020;">RELATED SERVICES:</span>\n' + items + '  </div>\n</div>'
    )

def make_topic_body(topic, heading, p1, p2, features, c1t, c1d, c2t, c2d, c3t, c3d, service_cards, benefits, cta_heading, cta_desc, related_links):
    return (
        sec1(topic, heading, p1, p2, features, c1t, c1d, c2t, c2d, c3t, c3d)
        + sec2(service_cards)
        + sec3(benefits)
        + sec4()
        + sec5(cta_heading, cta_desc, related_links)
    )

META = "Sydney Automation Co. - "  # prefix for meta descriptions
def make_page(p):
    fn = p["filename"]
    print("Building " + fn + " ...", end=" ")
    prefix = PREFIX
    prefix = prefix.replace(ORIG_TITLE, "<title>" + p["title"] + "</title>")
    prefix = prefix.replace(ORIG_META, "<meta content=\"" + p["meta"] + "\" name=\"description\"/>")
    prefix = prefix.replace(ORIG_CANONICAL, "<link rel=\"canonical\" href=\"https://sydneyautomationco.com.au/" + fn.replace(".html", "") + "\"/>")
    prefix = prefix.replace(ORIG_H1, p["h1"])
    prefix = prefix.replace(ORIG_LEAD, p["lead"])
    if "lede_kw" in p:
        plk = p["lede_kw"]
        if plk is None:
            prefix = prefix.replace(ORIG_LEDE_KW + "\n", "")
        else:
            prefix = prefix.replace(ORIG_LEDE_KW, plk)
    body = p["body"]
    seo_html = build_seo(p["seo"])
    faq_html = build_faq(p["faq"])
    suffix = BEFORE_SEO + seo_html + BETWEEN_SEO_FAQ + faq_html + AFTER_FAQ
    full = prefix + body + suffix
    with open(fn, "w", encoding="utf-8") as f:
        f.write(full)
    sz = len(full)
    print(str(sz) + " chars OK")

pages = []

# ---- PAGE 1: Commercial Lighting Control ----
pages.append({
    "filename": "commercial-lighting-control.html",
    "title": "Commercial Lighting Control Sydney | C-Bus & Dynalite for Offices & Commercial Buildings",
    "meta": "Commercial lighting control Sydney. C-Bus and Dynalite for offices, commercial buildings. Energy savings, AFSS compliance, C-Bus programming and commissioning. Call 0422 469 739.",
    "h1": '<h1>Commercial Lighting Control<br/><span class="accent">Sydney &amp; NSW</span></h1>',
    "lead": '<p class="lead">Expert commercial lighting control across Greater Sydney. C-Bus, Dynalite and DALI-2 for offices, retail, strata and commercial buildings. Energy-efficient, AFSS-compliant, programmed by accredited specialists. Based in Menai.</p>',
    "body": make_topic_body(
        "Commercial Lighting Control Sydney",
        "Intelligent Lighting Control for <span class=\"accent\">Commercial Buildings</span>",
        "Sydney commercial buildings demand lighting control that delivers energy efficiency, regulatory compliance and occupant comfort. C-Bus and Dynalite systems by Schneider Electric are the gold standard for Australian commercial lighting automation, offering programmable scenes, daylight harvesting, occupancy-based zones and centralised BMS integration.",
        "Our accredited technicians have programmed lighting control systems in commercial towers, retail centres, corporate offices and mixed-use developments across Sydney. From a single-floor fit-out to a multi-building campus, we design, commission and maintain systems that reduce energy consumption by up to 60% while ensuring full compliance with NCC 2025 and AFSS requirements.",
        ["Programmable scenes and schedules for each zone",
         "Daylight harvesting and occupancy-based dimming",
         "BMS integration via BACnet, Modbus or KNX",
         "AFSS-compliant emergency lighting testing (AS/NZS 2293)",
         "Centralised control via touchscreens, apps or wall switches",
         "Energy consumption monitoring and reporting"],
        "C-Bus & Dynalite Commercial",
        "Full C-Bus and Dynalite programming, commissioning and maintenance for commercial lighting control systems across Sydney. Accredited Clipsal/Schneider specialists.",
        "10+ Years Commercial Experience",
        "Former Clipsal National Support technicians. We have programmed lighting for strata towers, offices, retail centres, schools and healthcare facilities across Greater Sydney.",
        "All of Greater Sydney",
        "Based in Menai with same-day callouts across the Sutherland Shire, Eastern Suburbs, North Shore, CBD, Inner West, Northern Beaches and Hills District. No travel surcharge in the Shire.",
        [
            ("\u2699\ufe0f", "C-Bus Commercial Programming", "Accredited C-Bus programming for commercial lighting control systems. Scenes, schedules, triggers and full system commissioning using C-Bus Toolkit.", "/c-bus-programmer-sydney"),
            ("\U0001f4bb", "Dynalite Commercial Systems", "Dynalite programming and commissioning for commercial buildings. Multi-zone control, DALI gateway integration, BMS interfacing.", "/dynalite-programmer-sydney"),
            ("\u26a1", "DALI-2 Compliance & ROI", "DALI-2 compliant lighting control for NSW commercial buildings. Energy savings, NCC compliance, emergency lighting integration.", "/dali2-compliance-nsw-commercial"),
            ("\U0001f50d", "AFSS & Emergency Compliance", "Annual Fire Safety Statement compliance for commercial lighting. Emergency lighting testing, logbook maintenance, certification.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f3ed", "Building Lighting Upgrades", "Complete lighting control upgrades for commercial buildings. LED retrofit, C-Bus upgrade, Dynalite modernisation.", "/building-lighting-upgrades-sydney"),
            ("\U0001f6e1\ufe0f", "Lighting Control Maintenance", "Scheduled maintenance contracts for commercial lighting control systems. Preventive checks, firmware updates, emergency callouts.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f4b0", "Reduce energy costs by up to 60%"),
            ("\u2705", "NCC 2025 & AFSS compliant systems"),
            ("\U0001f4f1", "App and voice control integration"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus / Dynalite technicians"),
            ("\U0001f4ca", "Energy consumption monitoring"),
            ("\u23f0", "Same-day callouts across Sydney"),
            ("\U0001f3e2", "Office, retail, health & education"),
            ("\U0001f50c", "BMS integration (BACnet, Modbus)"),
            ("\U0001f331", "Daylight harvesting for efficiency"),
            ("\U0001f3af", "Fixed-price programming packages"),
            ("\U0001f6ef\ufe0f", "Centralised building control"),
            ("\U0001f7e2", "Ongoing maintenance & support"),
        ],
        "Intelligent Commercial Lighting Control Across Sydney",
        "Accredited C-Bus and Dynalite programming for commercial buildings. Energy savings, compliance and comfort. Same-day service across Greater Sydney.",
        [
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/dali2-compliance-nsw-commercial", "\u26a1", "DALI-2 Compliance"),
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is commercial lighting control?", "Commercial lighting control automates lighting in office buildings, retail centres and commercial premises using systems like C-Bus and Dynalite. It enables programmable scenes, occupancy-based dimming, daylight harvesting and centralised BMS integration for energy savings and compliance."),
        ("How much does commercial lighting control cost in Sydney?", "Costs vary based on system size and complexity. A single-floor office fit-out typically starts from $2,500 to $5,000 for programming and commissioning. Full building systems range from $10,000 to $50,000+. Contact us for a fixed-price quote on 0422 469 739."),
        ("Can commercial lighting integrate with my BMS?", "Yes. C-Bus and Dynalite integrate with major BMS platforms via BACnet, Modbus, KNX and API gateways. We regularly integrate with Honeywell, Siemens, Schneider and Delta controls for seamless building management."),
        ("Does commercial lighting control comply with AFSS?", "Absolutely. Our systems incorporate emergency lighting testing per AS/NZS 2293, including monthly logbook tests, 6-monthly discharge tests and annual inspections for your Annual Fire Safety Statement compliance."),
        ("What areas do you service for commercial lighting?", "All of Greater Sydney including the CBD, North Shore, Eastern Suburbs, Inner West, Sutherland Shire, Northern Beaches, Hills District, Parramatta and St George. We also service commercial sites across regional NSW."),
    ],
    "seo": [
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/dali2-compliance-nsw-commercial", "DALI-2 Compliance NSW"),
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Emergency Compliance"),
        ("/lighting-control-maintenance-sydney", "Lighting Control Maintenance"),
        ("/c-bus-apple-homekit-sydney", "C-Bus Apple HomeKit"),
        ("/commercial-strata-lighting-upgrades-nsw", "Strata Lighting Upgrades"),
    ],
})

# ---- PAGE 2: Residential Lighting Control ----
pages.append({
    "filename": "residential-lighting-control.html",
    "title": "Residential Lighting Control Sydney | C-Bus & Dynalite Home Automation",
    "meta": "Residential lighting control Sydney. C-Bus and Dynalite home automation for luxury homes, apartments and townhouses. Smart scenes, Apple Home, energy savings. Call 0422 469 739.",
    "h1": '<h1>Residential Lighting Control<br/><span class="accent">Home Automation Sydney</span></h1>',
    "lead": '<p class="lead">Transform your Sydney home with C-Bus and Dynalite lighting control. Scenes, schedules, Apple Home integration and voice control. Accredited programming by former Clipsal specialists. Based in Menai.</p>',
    "body": make_topic_body(
        "Residential Lighting Control Sydney",
        "Smart Home Lighting <span class=\"accent\">for Sydney Homes</span>",
        "Your home lighting should adapt to your lifestyle. C-Bus and Dynalite residential lighting control puts total control at your fingertips from scene setting and automated schedules to voice control via Siri, Google Home and Alexa. Dim the lights for movie night, program wake-up sequences, and control your entire home from anywhere via your smartphone.",
        "We specialise in residential C-Bus and Dynalite systems across Sydney premier suburbs. From luxury waterfront homes in Mosman and Vaucluse to modern townhouses in the Inner West and Sutherland Shire, our accredited technicians deliver flawless home automation. Every system is programmed for energy efficiency, convenience and future-proof expansion.",
        ["Programmable scenes: Movie, Entertain, Wake, Away, Sleep",
         "Apple Home, Google Home and Alexa voice control",
         "Automated schedules for sunrise/sunset and occupancy",
         "Remote access via smartphone and tablet apps",
         "Integration with blinds, climate and security systems",
         "Energy monitoring and LED-compatible dimming"],
        "C-Bus & Dynalite Residential",
        "Complete residential lighting control design, programming, commissioning and maintenance. C-Bus Toolkit and Dynalite Envision software. Accredited Clipsal/Schneider specialists.",
        "10+ Years Home Automation",
        "Former Clipsal National Support team. We have programmed hundreds of Sydney homes. Deep experience with C-Bus, Dynalite, DALI and smart home integration platforms.",
        "Sydney-Wide Coverage",
        "Based in Menai, servicing all of Sydney. Same-day callouts in the Sutherland Shire. Premium home automation for Mosman, Vaucluse, Bellevue Hill, Paddington, North Shore and more.",
        [
            ("\U0001f3e0", "Whole-Home Lighting Control", "Complete residential C-Bus and Dynalite systems with centralised control via touchscreens, keypads and your smartphone.", "/c-bus-programmer-sydney"),
            ("\U0001f3a5", "Home Cinema Lighting", "Dedicated home theatre lighting scenes with smooth dimming, blackout integration and multi-zone control for the ultimate cinema experience.", "/c-bus-apple-homekit-sydney"),
            ("\U0001f319", "Outdoor & Garden Lighting", "Automated outdoor lighting with sunrise/sunset schedules, motion sensors and scene integration for alfresco entertaining and security.", "/cbus-specialist-sydney"),
            ("\U0001f4f1", "Smartphone & Voice Control", "Control your entire home from your phone or voice via Siri, Google Assistant and Amazon Alexa. Apple HomeKit fully supported.", "/c-bus-apple-homekit-sydney"),
            ("\u26a1", "Energy-Efficient Automation", "Reduce energy consumption with occupancy-based automation, daylight harvesting and scheduled dimming. LED-compatible drivers.", "/cbus-upgrade-sydney"),
            ("\U0001f50b", "C-Bus / Dynalite Retrofits", "Upgrade your existing home with modern lighting control. Retrofit solutions for heritage homes, apartments and townhouses.", "/cbus-upgrade-sydney"),
        ],
        [
            ("\U0001f973", "Luxury scenes for every occasion"),
            ("\U0001f4f1", "Control from anywhere in the world"),
            ("\U0001f31f", "Apple Home, Google Home & Alexa"),
            ("\U0001f4a1", "LED-compatible smooth dimming"),
            ("\U0001f4b0", "Reduce energy bills by 40-60%"),
            ("\U0001f3e0", "Increase home resale value"),
            ("\u23f0", "Same-day service available"),
            ("\U0001f512", "Integration with security & blinds"),
            ("\U0001f3af", "Fixed-price programming packages"),
            ("\U0001f6e1\ufe0f", "Secure, encrypted remote access"),
            ("\U0001f331", "Eco-friendly automation"),
            ("\u2699\ufe0f", "Lifetime system support"),
        ],
        "Transform Your Sydney Home Today",
        "Accredited C-Bus and Dynalite residential lighting control. Smart scenes, voice control, energy savings. Based in Menai, serving all of Sydney.",
        [
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus + Apple HomeKit"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/cbus-upgrade-sydney", "\u26a1", "C-Bus Upgrades"),
            ("/cbus-specialist-sydney", "\u2b50", "C-Bus Specialist"),
            ("/lighting-control-repair-sydney", "\U0001f527", "Lighting Control Repair"),
        ]
    ),
    "faq": [
        ("What is residential lighting control?", "Residential lighting control automates your home lighting using smart systems like C-Bus and Dynalite. You can program scenes (Movie, Entertain, Sleep), set schedules, control lights from your phone, and integrate with voice assistants like Siri and Alexa."),
        ("How much does home lighting automation cost in Sydney?", "A typical 3-4 bedroom home with C-Bus lighting control starts from $3,000 to $8,000 for programming and commissioning, excluding hardware. Full luxury home systems with blinds and climate integration range from $10,000 to $30,000."),
        ("Can I add lighting control to my existing home?", "Yes. Retrofit solutions are available for existing homes. We can replace standard switches with C-Bus or Dynalite keypads, add wireless control, and integrate with existing wiring. Heritage-compatible options are also available."),
        ("Does residential lighting control work with Apple Home?", "Absolutely. C-Bus integrates seamlessly with Apple HomeKit via the C-Bus HomeKit gateway. Control your lights with Siri, the Apple Home app, and automate scenes based on time of day or occupancy."),
        ("What areas do you service for residential lighting?", "We service all of Greater Sydney including the Sutherland Shire, Eastern Suburbs, North Shore, Northern Beaches, Inner West, Hills District, Parramatta, CBD and St George. Premium home automation for Sydney finest suburbs."),
    ],
    "seo": [
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus + Apple HomeKit"),
        ("/dynalite-programmer-sydney", "Dynalite Programming"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/cbus-specialist-sydney", "C-Bus Specialist Sydney"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/residential-lighting-control", "Residential Lighting"),
    ],
})

# ---- PAGE 3: Industrial Lighting Control ----
pages.append({
    "filename": "industrial-lighting-control.html",
    "title": "Industrial Lighting Control Sydney | C-Bus & Dynalite for Warehouses & Factories",
    "meta": "Industrial lighting control Sydney. C-Bus and Dynalite for warehouses, factories, logistics centres. Energy savings, occupancy sensors, robust lighting control. Call 0422 469 739.",
    "h1": '<h1>Industrial Lighting Control<br/><span class="accent">Sydney Warehouses &amp; Factories</span></h1>',
    "lead": '<p class="lead">Robust industrial lighting control for Sydney warehouses, factories and logistics centres. C-Bus and Dynalite with occupancy sensors, daylight harvesting and BMS integration. Energy savings of 60%+. Accredited specialists.</p>',
    "body": make_topic_body(
        "Industrial Lighting Control Sydney",
        "Heavy-Duty Lighting Control <span class=\"accent\">for Industrial Environments</span>",
        "Industrial facilities have unique lighting requirements with high bays, wide aisles, 24/7 operation and harsh environments. C-Bus and Dynalite industrial lighting control delivers robust, reliable automation with occupancy-based zones, daylight harvesting and centralised BMS integration for maximum energy efficiency.",
        "We have programmed lighting control in logistics centres, warehouses, manufacturing plants and distribution hubs across Western Sydney, Bankstown, Ingleburn and Campbelltown. Our systems integrate with high-bay LED fittings, occupancy sensors and emergency lighting compliance, reducing energy consumption by up to 65% while maintaining safety and productivity.",
        ["Occupancy-based zone control for warehouses",
         "Daylight harvesting in high-bay areas",
         "BMS integration via BACnet and Modbus",
         "Emergency lighting compliance (AS/NZS 2293)",
         "Scheduled dimming for non-production hours",
         "Robust hardware rated for harsh environments"],
        "Industrial C-Bus & Dynalite",
        "Full industrial lighting control design, programming and commissioning. Accredited Clipsal/Schneider specialists with experience in logistics, manufacturing and warehousing.",
        "10+ Years Industrial Experience",
        "Former Clipsal National Support. We have programmed industrial C-Bus and Dynalite systems for major logistics hubs, factories and cold storage facilities across Sydney and NSW.",
        "Sydney-Wide Industrial Coverage",
        "Based in Menai, servicing industrial areas across Western Sydney, Bankstown, Ingleburn, Campbelltown, Penrith, Liverpool and Alexandria. Same-day emergency callouts available.",
        [
            ("\U0001f3ed", "Warehouse Lighting Control", "Occupancy-based high-bay control, aisle-following automation and scheduled dimming for logistics and distribution centres.", "/building-lighting-upgrades-sydney"),
            ("\U0001f3ed\ufe0f", "Factory & Plant Lighting", "Production area lighting with zone control, daylight harvesting and integration with manufacturing BMS systems.", "/dali-lighting-repair"),
            ("\u2747\ufe0f", "Cold Storage Lighting Control", "Specialist lighting control for cold rooms and freezers with robust hardware, sealed enclosures and temperature-rated components.", "/industrial-lighting-control"),
            ("\U0001f6e1\ufe0f", "Emergency Lighting Compliance", "AS/NZS 2293 compliant emergency lighting for industrial facilities. AFSS testing, logbook management, certification.", "/emergency-lighting-compliance-afss-sydney"),
            ("\u26a1", "Energy Management Systems", "BMS integration for comprehensive energy management. Real-time monitoring, demand response, consumption reporting.", "/lighting-control-service-sydney"),
            ("\U0001f504", "LED Upgrade & Retrofit", "Complete LED upgrade with intelligent control. Replace ageing fluorescent with smart LED. ROI typically 2-3 years.", "/led-upgrade-carpark-lighting-sydney"),
        ],
        [
            ("\U0001f4b0", "Reduce energy costs by up to 65%"),
            ("\u2705", "AS/NZS 2293 emergency compliance"),
            ("\U0001f331", "Daylight harvesting automation"),
            ("\U0001f6e1\ufe0f", "24/7 monitoring and support"),
            ("\u23f0", "Minimise downtime with fast response"),
            ("\U0001f4a1", "LED-optimised dimming control"),
            ("\U0001f50c", "BMS integration (BACnet, Modbus)"),
            ("\U0001f3ed", "High-bay and low-bay zone control"),
            ("\U0001f4ca", "Energy consumption reporting"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
            ("\U0001f3af", "Fixed-price service packages"),
            ("\U0001f7e2", "Ongoing maintenance contracts"),
        ],
        "Industrial Lighting Control Across Sydney",
        "C-Bus and Dynalite for warehouses, factories and logistics centres. Energy savings, compliance and productivity. Same-day service across industrial Sydney.",
        [
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/dali-lighting-repair", "\u26a1", "DALI Lighting Repair"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/led-upgrade-carpark-lighting-sydney", "\U0001f504", "LED Upgrades"),
            ("/lighting-control-service-sydney", "\U0001f6e1\ufe0f", "Lighting Service"),
            ("/lighting-control-repair-sydney", "\U0001f527", "Lighting Repair"),
        ]
    ),
    "faq": [
        ("What is industrial lighting control?", "Industrial lighting control automates lighting in warehouses, factories and logistics centres using C-Bus or Dynalite. It includes occupancy-based zone control, daylight harvesting, scheduled dimming and BMS integration to maximise energy savings and productivity."),
        ("How much energy can industrial lighting control save?", "Typical energy savings are 50 to 65% compared to standard lighting. This comes from occupancy-based automation (lights off when zones are empty), daylight harvesting and scheduled dimming during non-production hours."),
        ("Does industrial lighting control comply with emergency regulations?", "Yes. Our industrial systems meet AS/NZS 2293 for emergency lighting, including exit lighting, emergency egress lighting and monthly/6-monthly testing for your AFSS compliance."),
        ("Can industrial lighting integrate with my existing BMS?", "Absolutely. C-Bus and Dynalite integrate with all major BMS platforms via BACnet, Modbus, KNX and API. We have experience with Honeywell, Siemens, Schneider and custom SCADA interfaces."),
        ("What areas do you service for industrial lighting?", "All industrial areas of Sydney including Western Sydney, Bankstown, Ingleburn, Campbelltown, Penrith, Liverpool, Wetherill Park, Alexandria, Chullora and industrial zones across Greater Sydney."),
    ],
    "seo": [
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Emergency Compliance"),
        ("/dali-lighting-repair", "DALI Lighting Repair"),
        ("/led-upgrade-carpark-lighting-sydney", "LED Upgrade Carpark"),
        ("/lighting-control-service-sydney", "Lighting Control Service"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/lighting-control-service-contract-sydney", "Service Contracts"),
    ],
})

# ---- PAGE 4: Retail Lighting Control ----
pages.append({
    "filename": "retail-lighting-control.html",
    "title": "Retail Lighting Control Sydney | C-Bus & Dynalite for Shops & Showrooms",
    "meta": "Retail lighting control Sydney. C-Bus and Dynalite for shops, showrooms, retail centres. Accent lighting, scene control, energy savings, AFSS. Call 0422 469 739.",
    "h1": '<h1>Retail Lighting Control<br/><span class="accent">Sydney Shops &amp; Showrooms</span></h1>',
    "lead": '<p class="lead">Accent your retail space with intelligent C-Bus and Dynalite lighting control. Scene setting, energy management and AFSS compliance for Sydney shops, showrooms and retail centres. Accredited specialists.</p>',
    "body": make_topic_body(
        "Retail Lighting Control Sydney",
        "Create Ambience, <span class=\"accent\">Drive Sales</span>",
        "Retail lighting is your silent salesperson. C-Bus and Dynalite lighting control allows you to create dynamic scenes that highlight merchandise, set mood and adapt throughout the day with bright morning cleaning modes, perfect afternoon showcasing and inviting evening ambience. Studies show intelligent retail lighting can increase sales by up to 30%.",
        "We design and program retail lighting control for flagship stores, boutique shops, car showrooms and retail centres across Sydney. From Bondi Junction to the CBD to the Sutherland Shire, our systems integrate accent track lighting, cove lighting, window displays and emergency compliance, all controlled from a single touchscreen or scheduled automatically.",
        ["Dynamic scene control for time of day",
         "Accent lighting for merchandise displays",
         "Window display scheduling with timers",
         "Energy monitoring and consumption reports",
         "AFSS-compliant emergency lighting integration",
         "Centralised control for multi-site retailers"],
        "Retail C-Bus & Dynalite",
        "Complete retail lighting control design, programming and commissioning. C-Bus and Dynalite for accent, general and emergency lighting. Accredited specialists.",
        "10+ Years Retail Experience",
        "Former Clipsal National Support. We have programmed lighting for car showrooms, retail flagships, shopping centres and boutique stores across Sydney and NSW.",
        "Sydney-Wide Retail Coverage",
        "Based in Menai, servicing retail locations across Sydney CBD, Bondi Junction, Chatswood, Parramatta, Miranda, North Sydney and all major retail centres.",
        [
            ("\U0001f3ec", "Retail Store Lighting", "Complete in-store lighting control with accent scenes, general zone dimming and dynamic scheduling for optimal shopping ambience.", "/building-lighting-upgrades-sydney"),
            ("\U0001f698", "Car Showroom Lighting", "Specialist showroom lighting with dramatic accent scenes, cove lighting, spot highlighting and flexible zone control for vehicle displays.", "/retail-lighting-control"),
            ("\U0001f6d2", "Shopping Centre Lighting", "Common area, tenancy and car park lighting control for shopping centres. Centralised management, energy monitoring, AFSS compliance.", "/strata-lighting-control"),
            ("\U0001f31f", "Window Display Lighting", "Automated window display lighting with timers, seasonal scenes and remote management for dynamic retail displays.", "/retail-lighting-control"),
            ("\u26a1", "Energy & Compliance", "Energy-efficient retail lighting with occupancy sensing and daylight harvesting. AFSS-compliant emergency lighting integrated seamlessly.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f4cd", "Multi-Site Management", "Centralised control for multi-site retailers. Monitor and manage lighting across all stores from one dashboard. Cloud-connected.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f4b0", "Reduce retail energy costs by 50%+"),
            ("\U0001f4ca", "Real-time energy monitoring"),
            ("\u2705", "AFSS & NCC 2025 compliant"),
            ("\U0001f3a8", "Dynamic accent scene control"),
            ("\U0001f4f1", "Control from any device"),
            ("\U0001f331", "Daylight harvesting for efficiency"),
            ("\U0001f6e1\ufe0f", "Centralised multi-site management"),
            ("\u23f0", "Same-day service across Sydney"),
            ("\U0001f3af", "Fixed-price programming"),
            ("\U0001f4f7", "Window display scheduling"),
            ("\U0001f50b", "LED-compatible dimming"),
            ("\U0001f3e2", "Ongoing maintenance & support"),
        ],
        "Intelligent Retail Lighting Across Sydney",
        "C-Bus and Dynalite lighting control for shops, showrooms and retail centres. Accent scenes, energy savings, AFSS compliance. Same-day service.",
        [
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/strata-lighting-control", "\U0001f6d2", "Strata Lighting"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is retail lighting control?", "Retail lighting control uses C-Bus or Dynalite to automate and manage lighting in shops, showrooms and retail centres. It enables dynamic scene control, accent lighting, window display automation and centralised multi-site management."),
        ("Can retail lighting control increase sales?", "Yes. Studies show intelligent retail lighting can increase sales by up to 30% by creating optimal ambience, highlighting merchandise effectively and adapting lighting throughout the day for different customer experiences."),
        ("How much does retail lighting control cost?", "A single retail store lighting control system typically ranges from $3,000 to $8,000 for programming and commissioning. Multi-site systems and complex showroom installations range from $10,000 to $30,000."),
        ("Does retail lighting control meet AFSS requirements?", "Yes. Our systems include full emergency lighting compliance per AS/NZS 2293, with integrated testing, logbook management and certification for your Annual Fire Safety Statement."),
        ("What Sydney areas do you service for retail?", "All major Sydney retail precincts including the CBD, Bondi Junction, Chatswood, Parramatta, Miranda, North Sydney, Broadway, Macquarie Centre, Rhodes and all suburban retail centres across Greater Sydney."),
    ],
    "seo": [
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/strata-lighting-control", "Strata Lighting Control"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance"),
        ("/c-bus-programmer-sydney", "C-Bus Programming"),
        ("/dynalite-programmer-sydney", "Dynalite Programming"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/c-bus-apple-homekit-sydney", "C-Bus Apple HomeKit"),
        ("/commercial-strata-lighting-upgrades-nsw", "Strata Upgrades NSW"),
    ],
})


# ---- PAGE 5: Heritage Lighting Control ----
pages.append({
    "filename": "heritage-lighting-control.html",
    "title": "Heritage Lighting Control Sydney | C-Bus & Dynalite for Heritage Buildings",
    "meta": "Heritage lighting control Sydney. C-Bus and Dynalite for heritage buildings, churches and period homes. Discreet automation preserving architectural integrity. Call 0422 469 739.",
    "h1": '<h1>Heritage Lighting Control<br/><span class="accent">Sydney Period Homes &amp; Buildings</span></h1>',
    "lead": '<p class="lead">Preserve heritage while enjoying modern lighting automation. C-Bus and Dynalite heritage lighting control for Sydney period homes, churches and listed buildings. Discreet keypads, original switch plate options. Based in Menai.</p>',
    "body": make_topic_body(
        "Heritage Lighting Control Sydney",
        "Modern Automation <span class=\"accent\">for Heritage Buildings</span>",
        "Heritage buildings present unique challenges for lighting automation. Original architecture, period switch plates and heritage listing constraints require a specialist approach. C-Bus and Dynalite heritage solutions deliver full modern control using discreet keypads that blend with your period interiors.",
        "We have extensive experience automating lighting in Sydney heritage properties: Victorian terraces in Paddington, Federation homes in Hunters Hill, Georgian buildings in the CBD, and heritage-listed churches across NSW. Our approach respects the building character while delivering cutting-edge automation. We offer C-Bus Neo switches in heritage-compatible finishes and wireless retrofit solutions that minimise wall disturbance.",
        ["Discreet keypads compatible with period decor",
         "Wireless retrofit to minimise wall disturbance",
         "C-Bus Neo range in classic finishes",
         "Heritage-compatible switch plate options",
         "Zoned lighting for galleries and period rooms",
         "Integration with existing heritage wiring"],
        "Heritage C-Bus & Dynalite",
        "Specialist heritage lighting control design and installation. Accredited C-Bus and Dynalite programmers with extensive heritage building experience.",
        "Heritage Building Expertise",
        "Decades of combined experience in heritage properties. We understand the constraints of heritage listing, original materials and period aesthetics while delivering modern automation.",
        "Sydney Heritage Specialists",
        "Based in Menai, servicing heritage properties across Sydney oldest suburbs: Paddington, Balmain, Hunters Hill, Mosman, Darling Point and the CBD heritage precinct.",
        [
            ("\U0001f3e0", "Period Home Automation", "Complete lighting control for Victorian, Federation, Georgian and Colonial homes. Discreet automation that preserves original character.", "/heritage-and-church-lighting-automation-sydney"),
            ("\u26ea", "Church & Chapel Lighting", "Heritage-compliant lighting control for churches, chapels and religious buildings. Scene control for services, events and security.", "/heritage-and-church-lighting-automation-sydney"),
            ("\U0001f3a8", "Gallery & Museum Lighting", "Zoned heritage lighting for galleries and museums with conservation-grade dimming, UV protection and scene control for exhibitions.", "/heritage-lighting-control"),
            ("\U0001f3db\ufe0f", "Listed Building Automation", "Full automation for heritage-listed commercial buildings. Discreet installation, heritage-compliant wiring and period switch finishes.", "/heritage-lighting-control"),
            ("\U0001f504", "Wireless Retrofit Solutions", "Wireless C-Bus and Dynalite retrofit for heritage walls. Minimise disruption while adding full smart lighting functionality.", "/cbus-upgrade-sydney"),
            ("\U0001f31f", "Period Switch Plate Options", "C-Bus Neo switches and custom faceplates in finishes that match your period decor. Brass, bronze, nickel and painted options.", "/heritage-lighting-control"),
        ],
        [
            ("\U0001f3e0", "Preserves architectural integrity"),
            ("\U0001f527", "Wireless retrofit available"),
            ("\U0001f3af", "Heritage-compatible keypads"),
            ("\U0001f4a1", "Full modern dimming scenes"),
            ("\U0001f31f", "Discreet, period-appropriate design"),
            ("\U0001f4f1", "Remote control & scheduling"),
            ("\U0001f3a8", "Gallery-grade conservation dimming"),
            ("\u26a1", "Energy-efficient LED integration"),
            ("\U0001f68c", "Minimal wall disturbance"),
            ("\u23f0", "Heritage expert consultation"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
            ("\U0001f3af", "Fixed-price heritage packages"),
        ],
        "Heritage Lighting Control Across Sydney",
        "Modern C-Bus and Dynalite automation for heritage buildings, period homes and listed properties. Discreet. Respectful. Professional.",
        [
            ("/heritage-and-church-lighting-automation-sydney", "\u26ea", "Heritage & Church Lighting"),
            ("/cbus-upgrade-sydney", "\U0001f504", "C-Bus Upgrades"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus Apple HomeKit"),
        ]
    ),
    "faq": [
        ("Can lighting control be installed in heritage buildings?", "Yes, with the right approach. Wireless C-Bus and Dynalite retrofit solutions minimise wall disturbance, and discreet keypads are available in heritage-compatible finishes. We specialise in heritage-sensitive installations."),
        ("Will modern lighting control damage heritage walls?", "Not with our approach. We use wireless retrofit technology, surface-mount raceways where appropriate, and existing conduit paths to minimise any wall disturbance. Heritage listing constraints are fully respected."),
        ("Can I keep my original light switches?", "We offer heritage-compatible keypads and custom faceplate options that match your period decor. C-Bus Neo switches are available in finishes that complement Victorian, Federation and Art Deco interiors."),
        ("How much does heritage lighting control cost?", "Heritage installations typically cost 20-30% more than standard due to the specialist approach, discreet wiring and heritage-compatible hardware. Typical projects range from $5,000 to $20,000 depending on scope."),
        ("What Sydney heritage areas do you service?", "All heritage areas including Paddington, Balmain, Hunters Hill, Mosman, Darling Point, Vaucluse, the CBD heritage precinct, Glebe, Annandale, Newtown, Parramatta and historic suburbs across Greater Sydney."),
    ],
    "seo": [
        ("/heritage-and-church-lighting-automation-sydney", "Heritage & Church Lighting"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/residential-lighting-control", "Residential Lighting"),
        ("/c-bus-apple-homekit-sydney", "C-Bus Apple HomeKit"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
        ("/c-bus-specialist-sydney", "C-Bus Specialist Sydney"),
    ],
})

# ---- PAGE 6: Hospitality Lighting Control ----
pages.append({
    "filename": "hospitality-lighting-control.html",
    "title": "Hospitality Lighting Control Sydney | C-Bus & Dynalite for Hotels & Restaurants",
    "meta": "Hospitality lighting control Sydney. C-Bus and Dynalite for hotels, restaurants, bars. Guest room control, ambience scenes, energy management. Accredited. Call 0422 469 739.",
    "h1": '<h1>Hospitality Lighting Control<br/><span class="accent">Hotels, Restaurants &amp; Bars</span></h1>',
    "lead": '<p class="lead">C-Bus and Dynalite lighting control for Sydney finest hospitality venues. Guest room automation, restaurant scene setting, energy management and AFSS compliance. Accredited Clipsal specialists based in Menai.</p>',
    "body": make_topic_body(
        "Hospitality Lighting Control Sydney",
        "Exceptional Ambience <span class=\"accent\">for Hospitality Venues</span>",
        "In hospitality, lighting is everything. The right ambience transforms a restaurant from ordinary to memorable, a hotel room from functional to luxurious. C-Bus and Dynalite hospitality lighting control gives venue owners and managers precise control over every zone from dramatic restaurant scenes to gentle guest room wake-up sequences.",
        "We have programmed lighting for Sydney leading hotels, restaurants, bars and function centres. From five-star hotel guest rooms with bedside scene controllers to multi-zoned restaurant spaces that transition from bright lunch service to intimate dinner ambience. Every system is designed for energy efficiency, guest comfort and operational simplicity.",
        ["Guest room scene control (Welcome, Sleep, Reading)",
         "Restaurant zone transitions (Lunch, Dinner, Clean)",
         "Energy-saving occupancy automation for back-of-house",
         "AFSS-compliant emergency lighting integration",
         "Centralised management for multi-venue operators",
         "Integration with hotel PMS and booking systems"],
        "Hospitality C-Bus & Dynalite",
        "Complete hospitality lighting control design, programming and commissioning. Accredited C-Bus and Dynalite specialists with extensive hospitality experience.",
        "10+ Years Hospitality Experience",
        "Former Clipsal National Support. We have programmed lighting for hotels, restaurants, function centres and bars across Sydney and regional NSW.",
        "Sydney Hospitality Coverage",
        "Based in Menai, servicing hospitality venues across Sydney CBD, The Rocks, Darling Harbour, Surry Hills, Paddington, Potts Point, Bondi and all major hospitality precincts.",
        [
            ("\U0001f3e8", "Hotel Guest Room Control", "Bedside scene controllers, welcome mode, DND indicators, curtain integration and energy-saving occupancy sensors for hotel guest rooms.", "/hospitality-lighting-control"),
            ("\U0001f37d\ufe0f", "Restaurant Scene Control", "Dynamic restaurant lighting with time-of-day scenes, accent zones, dimmable pendants and integrated emergency compliance.", "/hospitality-lighting-control"),
            ("\U0001f37a", "Bar & Lounge Lighting", "Ambient bar lighting with colour tuning, accent cove lights, stage/focus modes and late-night energy-saving automation.", "/hospitality-lighting-control"),
            ("\U0001f3a0", "Function Room Lighting", "Multi-mode function room lighting with flexible zone control for conferences, weddings, gala dinners and cocktail events.", "/hospitality-lighting-control"),
            ("\u26a1", "Energy & Compliance", "Energy-efficient hospitality lighting with occupancy automation. Full AFSS emergency compliance. Guest comfort plus operational savings.", "/emergency-lighting-hotels-hospitality-sydney"),
            ("\U0001f50c", "PMS & BMS Integration", "Integration with hotel Property Management Systems and building BMS for automated check-in/out lighting modes and energy optimisation.", "/building-automation-maintenance-sydney"),
        ],
        [
            ("\U0001f973", "Create unforgettable guest experiences"),
            ("\U0001f4b0", "Reduce energy costs by 40-60%"),
            ("\u2705", "AFSS emergency compliance"),
            ("\U0001f31f", "Multi-zone scene control"),
            ("\U0001f4f1", "Staff tablet and app control"),
            ("\U0001f3e8", "Guest room automation"),
            ("\u23f0", "Same-day service across Sydney"),
            ("\U0001f50c", "PMS integration for automation"),
            ("\U0001f331", "Occupancy-based energy saving"),
            ("\U0001f4ca", "Energy consumption reporting"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
            ("\U0001f3af", "Fixed-price hospitality packages"),
        ],
        "Hospitality Lighting Control Across Sydney",
        "C-Bus and Dynalite for hotels, restaurants, bars and function venues. Guest room automation, scene control, energy savings. Accredited specialists.",
        [
            ("/emergency-lighting-hotels-hospitality-sydney", "\u26a1", "Hospitality Emergency"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-automation-maintenance-sydney", "\U0001f3e2", "Building Automation"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Lighting Maintenance"),
            ("/lighting-control-service-sydney", "\U0001f527", "Lighting Service"),
        ]
    ),
    "faq": [
        ("What is hospitality lighting control?", "Hospitality lighting control uses C-Bus or Dynalite to automate lighting in hotels, restaurants, bars and function venues. It includes guest room scene control, multi-zone restaurant transition scenes, and energy-efficient back-of-house automation."),
        ("Can hotel guest rooms be individually controlled?", "Yes. Each guest room can have its own scene controller (Welcome, Sleep, Reading, Bathroom) with occupancy sensors for energy saving. Integration with PMS enables automated check-in/out modes."),
        ("How much does hospitality lighting control cost?", "A single restaurant zone typically ranges from $3,000 to $8,000. Hotel guest room systems start from $1,500 to $3,000 per room for programming and commissioning. Full venue systems are quoted per project."),
        ("Does hospitality lighting meet compliance requirements?", "Yes. Our systems fully comply with AS/NZS 2293 for emergency lighting, AS 1680 for illumination levels, and NCC 2025 energy efficiency requirements. AFSS testing and certification included."),
        ("What Sydney hospitality venues do you service?", "All hospitality venues across Sydney including CBD hotels, The Rocks, Darling Harbour, Surry Hills restaurants, Paddington bars, Potts Point venues, Bondi Beach and all major hospitality precincts."),
    ],
    "seo": [
        ("/emergency-lighting-hotels-hospitality-sydney", "Hospitality Emergency Lighting"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-automation-maintenance-sydney", "Building Automation Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Control Maintenance"),
        ("/lighting-control-service-sydney", "Lighting Control Service"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
        ("/c-bus-apple-homekit-sydney", "C-Bus Apple HomeKit"),
    ],
})

# ---- PAGE 7: Schools Lighting Control ----
pages.append({
    "filename": "schools-lighting-control.html",
    "title": "Schools Lighting Control Sydney | C-Bus & Dynalite for Schools & Education",
    "meta": "Schools lighting control Sydney. C-Bus and Dynalite for classrooms, halls, libraries. Energy savings, AFSS compliance, circadian lighting. Accredited. Call 0422 469 739.",
    "h1": '<h1>Schools &amp; Education Lighting<br/><span class="accent">C-Bus &amp; Dynalite Sydney</span></h1>',
    "lead": '<p class="lead">Intelligent lighting control for Sydney schools and educational facilities. C-Bus and Dynalite for classrooms, halls, libraries and sports centres. Circadian lighting, energy savings, AFSS compliance. Accredited Clipsal specialists.</p>',
    "body": make_topic_body(
        "Schools Lighting Control Sydney",
        "Better Learning Environments <span class=\"accent\">Through Intelligent Lighting</span>",
        "Lighting directly impacts student concentration, behaviour and learning outcomes. Research shows that tuneable white lighting with circadian tuning improves academic performance by up to 15%. C-Bus and Dynalite school lighting control delivers optimal illumination for every learning space from bright, cool classrooms for exam focus to warm, calm lighting for reading areas.",
        "We have programmed lighting control in schools across Sydney including government, independent, Catholic and early learning centres. Our systems cover classrooms, libraries, halls, admin offices, sports centres and grounds. Each space is individually controlled with schedules, occupancy sensors and daylight harvesting for maximum energy efficiency.",
        ["Circadian tuneable white lighting for classrooms",
         "Occupancy-based zone control for energy saving",
         "Daylight harvesting in perimeter zones",
         "AFSS-compliant emergency lighting integration",
         "Centralised monitoring for facilities management",
         "Hall multi-mode lighting (Assembly, Sport, Performance)"],
        "Education C-Bus & Dynalite",
        "Complete school lighting control design, programming and maintenance. Accredited C-Bus and Dynalite specialists with extensive education sector experience.",
        "10+ Years Education Experience",
        "Former Clipsal National Support. We have programmed lighting for schools, universities and educational facilities across Sydney and NSW.",
        "Sydney Schools Coverage",
        "Based in Menai, servicing schools across Greater Sydney including Sutherland Shire, Eastern Suburbs, North Shore, Inner West, Hills District and Western Sydney.",
        [
            ("\U0001f3eb", "Classroom Lighting Control", "Tuneable white lighting with circadian tuning, occupancy sensing and daylight harvesting for optimal learning conditions.", "/educational-facilities-lighting-automation-sydney"),
            ("\U0001f4da", "Library & Study Areas", "Zoned lighting with quiet study, group work and reading scenes. Automated dimming based on natural light levels.", "/educational-facilities-lighting-automation-sydney"),
            ("\U0001f3d2", "School Hall & Gym Lighting", "Multi-mode hall lighting: assembly, performance, sports and cleaning modes. Flexible zone control for maximum utilisation.", "/schools-lighting-control"),
            ("\u26a1", "AFSS & Emergency Compliance", "Full emergency lighting compliance for schools. Exit lighting, egress paths, monthly testing and logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f331", "Energy & Sustainability", "Reduce school energy costs by up to 60% with occupancy automation, daylight harvesting and scheduled dimming. NABERS-friendly.", "/building-lighting-upgrades-sydney"),
            ("\U0001f50c", "Facilities Management", "Centralised lighting management for facilities teams. Monitor zones, override schedules, manage maintenance from one dashboard.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f3a8", "Circadian tuning improves learning"),
            ("\U0001f4b0", "Reduce energy costs by up to 60%"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f4a1", "Optimal illumination for every space"),
            ("\U0001f331", "Daylight harvesting automation"),
            ("\U0001f4f1", "Facilities team app control"),
            ("\U0001f6e1\ufe0f", "Centralised monitoring dashboard"),
            ("\u23f0", "Same-day service across Sydney"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
            ("\U0001f3af", "Fixed-price education packages"),
            ("\U0001f527", "Ongoing maintenance contracts"),
            ("\U0001f3eb", "Designed for school environments"),
        ],
        "School Lighting Control Across Sydney",
        "C-Bus and Dynalite for classrooms, halls, libraries and sports centres. Circadian lighting, energy savings, AFSS compliance. Based in Menai.",
        [
            ("/educational-facilities-lighting-automation-sydney", "\U0001f3eb", "Education Lighting"),
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is school lighting control?", "School lighting control uses C-Bus or Dynalite to automate lighting in educational facilities. Features include tuneable white circadian lighting for classrooms, occupancy-based energy saving, daylight harvesting and AFSS-compliant emergency lighting."),
        ("Does lighting affect student learning outcomes?", "Yes. Research from the University of Sydney and international studies shows that tuneable white lighting with circadian tuning can improve student concentration and academic performance by up to 15%."),
        ("How much energy can school lighting control save?", "Typical energy savings are 50-60%. By combining occupancy-based automation, daylight harvesting and scheduled dimming, schools significantly reduce electricity consumption while maintaining optimal learning conditions."),
        ("Does school lighting comply with emergency regulations?", "Absolutely. Our systems meet AS/NZS 2293 for emergency lighting and egress, AS 1680 for indoor illumination, and NCC 2025 energy requirements. Monthly testing and logbook management included."),
        ("What Sydney schools do you service?", "We service all schools across Greater Sydney including government, independent, Catholic and early learning centres in the Sutherland Shire, Eastern Suburbs, North Shore, Inner West, Hills District, Parramatta and Western Sydney."),
    ],
    "seo": [
        ("/educational-facilities-lighting-automation-sydney", "Education Lighting Sydney"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/lighting-control-maintenance-sydney", "Lighting Control Maintenance"),
        ("/university-and-tafe-lighting-automation", "University & TAFE Lighting"),
        ("/schools-lighting-control", "Schools Lighting"),
    ],
})

# ---- PAGE 8: Strata Lighting Control ----
pages.append({
    "filename": "strata-lighting-control.html",
    "title": "Strata Lighting Control Sydney | C-Bus & Dynalite for Strata & Body Corporate",
    "meta": "Strata lighting control Sydney. C-Bus and Dynalite for strata apartments, body corporate. Common areas, car parks, AFSS, energy savings. Accredited. Call 0422 469 739.",
    "h1": '<h1>Strata Lighting Control<br/><span class="accent">Sydney Apartments &amp; Body Corporate</span></h1>',
    "lead": '<p class="lead">C-Bus and Dynalite strata lighting control for apartment buildings and body corporate. Common area automation, car park lighting, AFSS compliance, energy savings. Accredited specialists serving strata properties across Greater Sydney.</p>',
    "body": make_topic_body(
        "Strata Lighting Control Sydney",
        "Smarter Strata Lighting <span class=\"accent\">for Sydney Apartments</span>",
        "Strata properties face unique lighting challenges with common areas, car parks, foyers, corridors and building exteriors all needing reliable, energy-efficient automation. C-Bus and Dynalite strata lighting control delivers centralised management, significant energy savings and full AFSS compliance for apartment buildings across Sydney.",
        "We specialise in strata lighting upgrades and maintenance. From a single common property system to multi-building complexes, we design and program C-Bus and Dynalite systems that reduce strata levies through energy savings, automate emergency lighting testing and give building managers easy control. Our systems are trusted by leading strata management companies across Sydney.",
        ["Common area automation with occupancy sensors",
         "Car park lighting with scheduled dimming",
         "AFSS-compliant emergency lighting testing",
         "Foyer and corridor scene control",
         "Centralised building manager dashboard",
         "Energy monitoring for strata reporting purposes"],
        "Strata C-Bus & Dynalite",
        "Complete strata lighting control design, programming and maintenance. Accredited C-Bus and Dynalite specialists with extensive strata sector experience.",
        "10+ Years Strata Experience",
        "Former Clipsal National Support. We work with leading strata management companies across Sydney. Deep understanding of strata compliance and OC requirements.",
        "Sydney Strata Coverage",
        "Based in Menai, servicing strata properties across all of Sydney. Car parks, foyers, gyms, pools, common areas and building exteriors.",
        [
            ("\U0001f3e2", "Common Area Automation", "Corridors, foyers, gyms and pool areas with occupancy-based automation, scheduled dimming and centralised management.", "/strata-lighting-control"),
            ("\U0001f698", "Basement Car Park Control", "Car park lighting with occupancy sensors, scheduled dimming and emergency compliance. Energy savings of 60-80%.", "/carpark-lighting-upgrades-sydney"),
            ("\U0001f50d", "AFSS Emergency Compliance", "Automated emergency lighting testing per AS/NZS 2293. Monthly and 6-monthly tests with digital logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f4ca", "Energy & Levy Reporting", "Energy consumption monitoring for OC reporting. Track savings, allocate costs, demonstrate compliance to residents.", "/strata-lighting-compliance-sydney"),
            ("\U0001f31f", "Foyer & Entry Automation", "Welcoming foyer scenes with time-of-day scheduling, occupancy triggers and integration with building access systems.", "/strata-lighting-control"),
            ("\U0001f527", "Strata Maintenance Contracts", "Scheduled maintenance for strata lighting control systems. Preventive checks, firmware updates, emergency callouts.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f4b0", "Reduce strata energy costs by 60%+"),
            ("\u2705", "Full AFSS emergency compliance"),
            ("\U0001f4ca", "Energy reporting for OC meetings"),
            ("\U0001f3e2", "Centralised building management"),
            ("\U0001f698", "Car park sensor automation"),
            ("\u23f0", "Same-day strata callouts"),
            ("\U0001f6e1\ufe0f", "Auto emergency lighting testing"),
            ("\U0001f3af", "Fixed-price strata packages"),
            ("\U0001f504", "Easy retrofit to existing systems"),
            ("\U0001f331", "Green building compliance"),
            ("\U0001f4f1", "Building manager app control"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
        ],
        "Strata Lighting Control Across Sydney",
        "C-Bus and Dynalite for strata apartments, body corporate and common property. Energy savings, AFSS compliance, centralised management. Based in Menai.",
        [
            ("/commercial-strata-lighting-upgrades-nsw", "\U0001f3e2", "Strata Upgrades NSW"),
            ("/carpark-lighting-upgrades-sydney", "\U0001f698", "Car Park Upgrades"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/strata-lighting-compliance-sydney", "\u2705", "Strata Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is strata lighting control?", "Strata lighting control uses C-Bus or Dynalite to automate common area lighting in apartment buildings. It includes car park sensors, corridor occupancy automation, AFSS emergency testing and centralised management for building managers and OCs."),
        ("Can strata lighting control reduce my levies?", "Yes. Energy savings of 50-60% from common area automation directly reduce electricity costs, which lowers strata levies. Many buildings recoup their investment within 12-24 months."),
        ("Does strata lighting meet AFSS requirements?", "Absolutely. Our systems include fully automated emergency lighting testing per AS/NZS 2293 with digital logbook management, making AFSS compliance effortless for building managers."),
        ("How much does strata lighting control cost?", "A typical apartment building installation ranges from $5,000 to $25,000 depending on size and complexity. Car park upgrades alone start from $3,000. ROI is typically 12-24 months from energy savings."),
        ("What Sydney strata areas do you service?", "All Sydney strata properties including apartments in the CBD, Eastern Suburbs, North Shore, Sutherland Shire, Inner West, Parramatta, Northern Beaches, Hills District and all strata suburbs across Greater Sydney."),
    ],
    "seo": [
        ("/commercial-strata-lighting-upgrades-nsw", "Strata Lighting Upgrades NSW"),
        ("/carpark-lighting-upgrades-sydney", "Car Park Lighting Upgrades"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Emergency Compliance"),
        ("/strata-lighting-compliance-sydney", "Strata Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Control Maintenance"),
        ("/strata-managers-lighting-control-sydney", "Strata Managers"),
        ("/building-manager-lighting-support-sydney", "Building Manager Support"),
    ],
})

# ---- PAGE 9: C-Bus & Dynalite Programming ----
pages.append({
    "filename": "cbus-dynalite-programming.html",
    "title": "C-Bus & Dynalite Programming Sydney | Accredited Clipsal Programmer",
    "meta": "C-Bus and Dynalite programming Sydney. Accredited Clipsal/Schneider programmer. C-Bus Toolkit, Dynalite Envision, PICED. Fault finding. Call 0422 469 739.",
    "h1": '<h1>C-Bus &amp; Dynalite Programming<br/><span class="accent">Sydney Accredited Specialist</span></h1>',
    "lead": '<p class="lead">Accredited C-Bus and Dynalite programming for residential, commercial and industrial systems. C-Bus Toolkit, Dynalite Envision, Commission Spacelogic and PICED. Former Clipsal National Support. Based in Menai.</p>',
    "body": make_topic_body(
        "C-Bus & Dynalite Programming",
        "Accredited Programming <span class=\"accent\">for Both Major Platforms</span>",
        "C-Bus and Dynalite are Schneider Electric two flagship lighting control platforms. C-Bus is the backbone of Australian commercial and residential lighting automation, while Dynalite excels in high-end commercial, hospitality and architectural projects. We are accredited programmers for both systems.",
        "With 10+ years of experience on both platforms including former roles in Clipsal National Support, we program using official software: C-Bus Toolkit, C-Bus Commission Spacelogic, Dynalite Envision and PICED. We handle everything from single-room programming to multi-building campus systems.",
        ["C-Bus Toolkit programming and diagnostics",
         "Dynalite Envision DGX configuration",
         "Commission Spacelogic for advanced logic",
         "PICED for C-Bus Wiser integration",
         "Multi-platform gateway integration",
         "Remote programming and troubleshooting"],
        "C-Bus & Dynalite Programming",
        "Full C-Bus and Dynalite programming services. Accredited Clipsal/Schneider programmer. C-Bus Toolkit, Dynalite Envision, Commission Spacelogic, PICED.",
        "Former Clipsal National Support",
        "Years in national technical support and sales within Clipsal C-Bus division. Inside knowledge of how both platforms are designed, built and fail.",
        "All of Greater Sydney",
        "Based in Menai with same-day callouts across the Sutherland Shire. Full Greater Sydney coverage for C-Bus and Dynalite programming.",
        [
            ("\u2699\ufe0f", "C-Bus Programming", "Scene creation, schedule setup, trigger configuration, group addressing and full system programming using C-Bus Toolkit and Commission Spacelogic.", "/c-bus-programmer-sydney"),
            ("\U0001f4bb", "Dynalite Programming", "Dynalite DGX programming, scene control, DALI gateway integration, BMS interfacing and multi-zone automation.", "/dynalite-programmer-sydney"),
            ("\U0001f50d", "C-Bus Fault Finding", "Network address conflicts, corrupted programming, failed modules, unresponsive switches. Diagnostic testing with C-Bus Toolkit.", "/cbus-repair-sydney"),
            ("\U0001f3e0", "Commissioning & Handover", "New build and renovation commissioning. Full system documentation, group addresses, scene schedules and user training.", "/c-bus-programmer-sydney"),
            ("\U0001f527", "System Upgrades", "C-Bus 1 to C-Bus 2 upgrades, relay module replacement, legacy Dynalite modernisation and firmware updates.", "/cbus-upgrade-sydney"),
            ("\U0001f31f", "Smart Home Integration", "C-Bus and Dynalite integration with Apple Home, Google Home, Crestron, Savant and KNX gateways.", "/c-bus-apple-homekit-sydney"),
        ],
        [
            ("\u2699\ufe0f", "Accredited C-Bus & Dynalite programmer"),
            ("\U0001f4bb", "C-Bus Toolkit + Dynalite Envision"),
            ("\u2b50", "Former Clipsal National Support"),
            ("\U0001f4a1", "Fix the unfixable faults"),
            ("\u23f0", "Same-day programming callouts"),
            ("\U0001f3af", "Fixed-price programming"),
            ("\U0001f50c", "Remote programming available"),
            ("\U0001f6e0\ufe0f", "All official software licenses"),
            ("\U0001f4ca", "Full system documentation"),
            ("\U0001f3ed", "Commercial + residential + industrial"),
            ("\U0001f4f1", "Smart home integration"),
            ("\U0001f6e1\ufe0f", "Ongoing technical support"),
        ],
        "Accredited C-Bus & Dynalite Programming",
        "C-Bus Toolkit, Dynalite Envision, Commission Spacelogic, PICED. Former Clipsal National Support. Fixed-price programming across Greater Sydney.",
        [
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/cbus-repair-sydney", "\U0001f50d", "C-Bus Repair"),
            ("/cbus-upgrade-sydney", "\U0001f527", "C-Bus Upgrade"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus Apple HomeKit"),
            ("/cbus-specialist-sydney", "\u2b50", "C-Bus Specialist"),
        ]
    ),
    "faq": [
        ("What is C-Bus programming?", "C-Bus programming uses Schneider Electric C-Bus Toolkit software to configure lighting control networks. This includes creating scenes, setting schedules, configuring triggers, group addressing and commissioning."),
        ("What is Dynalite programming?", "Dynalite programming uses Dynalite Envision DGX software to configure Schneider Electric Dynalite lighting control platform. It covers DALI gateway integration, scene control, BMS interfacing."),
        ("Are you accredited for both C-Bus and Dynalite?", "Yes. We hold current accreditations for both C-Bus (Clipsal/Schneider) and Dynalite programming. We are one of the few Sydney-based programmers qualified on both platforms."),
        ("How much does C-Bus or Dynalite programming cost?", "Programming costs depend on system complexity. A typical residential C-Bus system ranges from $800 to $3,000. Commercial systems vary from $2,500 to $15,000+."),
        ("Can programming be done remotely?", "Yes. Many C-Bus and Dynalite programming tasks can be completed remotely via network connection. However, commissioning and fault finding typically require an on-site visit."),
    ],
    "seo": [
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/cbus-repair-sydney", "C-Bus Repair Sydney"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrade Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus Apple HomeKit"),
        ("/cbus-specialist-sydney", "C-Bus Specialist Sydney"),
        ("/dynalite-repair-sydney", "Dynalite Repair Sydney"),
        ("/cbus-maintenance-sydney", "C-Bus Maintenance"),
    ],
})

# ---- PAGE 10: Privacy Policy ----
pages.append({
    "filename": "privacy.html",
    "title": "Privacy Policy | Sydney Automation Co.",
    "meta": "Privacy policy for Sydney Automation Co. How we collect, use and protect your personal information. Your privacy rights when using our services.",
    "h1": '<h1>Privacy Policy<br/><span class="accent">Sydney Automation Co.</span></h1>',
    "lead": '<p class="lead">This Privacy Policy explains how Sydney Automation Co. collects, uses, discloses and protects your personal information. We are committed to protecting your privacy in accordance with the Privacy Act 1988 (Cth) and the Australian Privacy Principles (APPs).</p>',
    "body": (
        '<div class="section" style="background:#001428">\n<div class="container">\n<div class="section-header">\n'
        '<h2>Our Commitment <span class="accent">to Your Privacy</span></h2>\n'
        '<p class="dim">Last updated: July 2026. This policy applies to all personal information collected by Sydney Automation Co. ABN 61 136 364 150.</p>\n</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">1. Information We Collect</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">We may collect the following types of personal information:</p>\n'
        '<ul style="color:#a8c0e0; line-height:2; padding-left:20px; margin-top:12px">\n'
        "<li><strong>Contact Information:</strong> Name, phone number, email address, and physical address.</li>\n"
        "<li><strong>Property Information:</strong> Details about your property relevant to our services, including site access requirements, electrical system information, and building plans.</li>\n"
        "<li><strong>Communication Records:</strong> Records of emails, phone calls, text messages, and other correspondence between you and our team.</li>\n"
        "<li><strong>Billing Information:</strong> Invoice details, payment records, and transaction history for services provided.</li>\n"
        "<li><strong>Technical Information:</strong> IP address, browser type, device information, and website usage data collected via cookies and analytics.</li>\n"
        "<li><strong>Service History:</strong> Details of services performed, including C-Bus and Dynalite programming records, maintenance logs, and site inspection reports.</li>\n"
        '</ul>\n</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">2. How We Use Your Information</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">We use your personal information for the following purposes:</p>\n'
        '<ul style="color:#a8c0e0; line-height:2; padding-left:20px; margin-top:12px">\n'
        "<li>To provide C-Bus, Dynalite and lighting control services you have requested</li>\n"
        "<li>To communicate with you about service appointments, quotes, and technical matters</li>\n"
        "<li>To process payments and maintain billing records</li>\n"
        "<li>To comply with legal and regulatory obligations, including AFSS documentation</li>\n"
        "<li>To improve our services and website experience</li>\n"
        "<li>To send service-related communications (reminders, updates, confirmations)</li>\n"
        "<li>To respond to enquiries and complaints</li>\n"
        '</ul>\n</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">3. Disclosure of Information</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">We may disclose your personal information to:</p>\n'
        '<ul style="color:#a8c0e0; line-height:2; padding-left:20px; margin-top:12px">\n'
        "<li>Third-party service providers who assist us in operating our business (e.g., payment processors, IT service providers, cloud storage providers)</li>\n"
        "<li>Schneider Electric / Clipsal Australia for warranty registration and technical support purposes</li>\n"
        "<li>Regulatory authorities as required by law, including local council for compliance documentation</li>\n"
        "<li>Strata management companies or building managers where you are a resident or owner within a strata scheme</li>\n"
        "<li>Professional advisors including accountants, lawyers and insurers</li>\n"
        '</ul>\n'
        '<p style="color:#a8c0e0; line-height:1.8; margin-top:12px">We do not sell, trade, or rent your personal information to third parties for marketing purposes.</p>\n'
        '</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">4. Data Security</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">We take reasonable steps to protect your personal information from misuse, interference, loss, unauthorised access, modification or disclosure.</p>\n'
        '<ul style="color:#a8c0e0; line-height:2; padding-left:20px; margin-top:12px">\n'
        "<li>Secure cloud storage with encrypted data transmission (SSL/TLS)</li>\n"
        "<li>Access controls and authentication procedures for our systems</li>\n"
        "<li>Restricted physical access to our office and records</li>\n"
        "<li>Secure destruction of personal information when no longer required</li>\n"
        "<li>Regular security assessments and staff training</li>\n"
        '</ul>\n</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">5. Cookies and Website Analytics</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">Our website uses cookies and Google Analytics to understand how visitors interact with our site. This helps us improve our website and services. Cookies are small text files stored on your device. You can control cookie preferences through your browser settings.</p>\n'
        '</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">6. Accessing and Correcting Your Information</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">You have the right to access the personal information we hold about you and to request corrections if it is inaccurate, outdated, incomplete, irrelevant or misleading.</p>\n'
        '</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">7. Complaints</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">If you believe we have breached the Australian Privacy Principles, please contact us immediately. We will investigate your complaint and respond within 30 days.</p>\n'
        '</div>\n\n'

        '<div class="card" style="margin-bottom:32px">\n'
        '<h3 style="color:#f07020; margin-bottom:12px">8. Contact Us</h3>\n'
        '<p style="color:#a8c0e0; line-height:1.8">For any questions about this Privacy Policy or to exercise your privacy rights, please contact us:</p>\n'
        '<div style="color:#a8c0e0; line-height:1.8; margin-top:12px">\n'
        "<p><strong>Sydney Automation Co.</strong></p>\n"
        "<p>Menai, Sutherland Shire NSW 2234</p>\n"
        '<p>Phone: <a href="tel:0422469739" style="color:#f07020;">0422 469 739</a></p>\n'
        '<p>Email: <a href="mailto:service@sydneyautomationco.com.au" style="color:#f07020;">service@sydneyautomationco.com.au</a></p>\n'
        "</div>\n</div>\n</div>\n</div>"
    ),
    "faq": [
        ("What personal information does Sydney Automation Co. collect?", "We collect contact information, property information relevant to our services, communication records, billing information, technical data from our website, and service history records."),
        ("Do you share my information with third parties?", "We only share information with third-party service providers, Schneider Electric for warranty purposes, regulatory authorities as required, and professional advisors. We never sell your data."),
        ("How do you protect my personal information?", "We use encrypted cloud storage (SSL/TLS), access controls, restricted physical access, and secure destruction practices."),
        ("Can I access my personal information you hold?", "Yes. You have the right to request access to your personal information and request corrections. Contact us at service@sydneyautomationco.com.au."),
        ("What cookies does your website use?", "Our website uses Google Analytics GA4 cookies to understand visitor behaviour. You can control cookie preferences through your browser settings."),
    ],
    "seo": [
        ("/", "Home"),
        ("/contact", "Contact Us"),
        ("/about", "About Sydney Automation Co."),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/cbus-repair-sydney", "C-Bus Repairs Sydney"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades"),
        ("/services-hub", "All Services"),
    ],
})

# ---- PAGE 11: Commercial Strata Lighting Upgrades NSW ----
pages.append({
    "filename": "commercial-strata-lighting-upgrades-nsw.html",
    "title": "Commercial Strata Lighting Upgrades NSW | C-Bus & Dynalite",
    "meta": "Commercial strata lighting upgrades NSW. C-Bus and Dynalite for strata common areas. LED retrofit, AFSS compliance, energy savings. Call 0422 469 739.",
    "h1": '<h1>Commercial Strata Lighting Upgrades<br/><span class="accent">NSW &amp; Sydney</span></h1>',
    "lead": '<p class="lead">Comprehensive lighting upgrades for commercial strata properties across NSW. C-Bus and Dynalite systems, LED retrofit, AFSS compliance. Based in Menai.</p>',
    "body": make_topic_body(
        "Commercial Strata Lighting Upgrades NSW",
        "Future-Proof Your Strata <span class=\"accent\">with Smart Lighting</span>",
        "Commercial strata properties across NSW are upgrading to intelligent, energy-efficient lighting control. C-Bus and Dynalite systems deliver energy savings of 50-60%, automated AFSS compliance, and modern control for common areas, car parks and foyers.",
        "We specialise in strata upgrades throughout NSW. From small suburban blocks to large commercial towers, our team manages every step: audit, design, approvals, programming, commissioning and AFSS integration. Upgrades pay for themselves within 12-24 months.",
        ["Energy-efficient LED retrofit",
         "AFSS-compliant emergency lighting",
         "Car park occupancy sensing",
         "Body corporate approval support",
         "NCC 2025 and BASIX compliance",
         "Fixed-price upgrades"],
        "Strata Upgrade Specialists",
        "Complete strata lighting upgrade service. Accredited C-Bus and Dynalite specialists.",
        "10+ Years Strata Experience",
        "Former Clipsal National Support. Hundreds of strata properties upgraded across NSW.",
        "NSW-Wide Service",
        "Based in Menai, servicing Sydney and regional NSW including Wollongong, Newcastle, Central Coast.",
        [
            ("\U0001f7e2", "Common Property Upgrades", "Full upgrade for foyers, corridors, gyms, pools with C-Bus or Dynalite control.", "/strata-lighting-control"),
            ("\U0001f698", "Car Park Lighting", "Car park LED upgrades with sensors and dimming. 60-80% energy savings. AFSS compliant.", "/carpark-lighting-upgrades-sydney"),
            ("\U0001f50d", "AFSS Integration", "Automated emergency testing and logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f331", "Energy Audits", "Lighting audit with savings projections and ROI analysis for OC approval.", "/commercial-strata-lighting-upgrades-nsw"),
            ("\U0001f4ca", "NABERS & BASIX", "Lighting upgrades contributing to NABERS and BASIX compliance.", "/strata-lighting-compliance-sydney"),
            ("\U0001f527", "Maintenance", "Post-upgrade maintenance with preventive checks and priority callouts.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f4b0", "Energy savings of 50-60%"),
            ("\u2705", "Full AFSS compliance"),
            ("\U0001f3e2", "OC approved solutions"),
            ("\U0001f4ca", "ROI analysis included"),
            ("\U0001f331", "NCC 2025 & BASIX compliant"),
            ("\u23f0", "Minimal disruption"),
            ("\U0001f527", "End-to-end management"),
            ("\U0001f4f1", "Building manager dashboard"),
            ("\U0001f6e0\ufe0f", "Accredited programmers"),
            ("\U0001f504", "Future-proof technology"),
            ("\U0001f3af", "Fixed-price packages"),
            ("\U0001f7e2", "NSW-wide coverage"),
        ],
        "Strata Upgrades Across NSW",
        "C-Bus and Dynalite for commercial strata. LED retrofit, AFSS compliance, energy savings.",
        [
            ("/strata-lighting-control", "\U0001f3e2", "Strata Lighting"),
            ("/carpark-lighting-upgrades-sydney", "\U0001f698", "Car Park Upgrades"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is a commercial strata lighting upgrade?", "Replaces outdated lighting with LED fittings controlled by C-Bus or Dynalite automation with occupancy sensors and AFSS compliance."),
        ("How much can a strata upgrade save?", "Typical savings are 50-60%. Investment recouped within 12-24 months."),
        ("Do I need OC approval?", "Yes. We provide proposals with ROI analysis and compliance documentation."),
        ("Does the upgrade comply with AFSS?", "Yes. Fully integrated emergency lighting per AS/NZS 2293 with automated testing."),
        ("What NSW areas do you service?", "Greater Sydney plus Wollongong, Newcastle, Central Coast, Blue Mountains and regional centres."),
    ],
    "seo": [
        ("/strata-lighting-control", "Strata Lighting Control"),
        ("/carpark-lighting-upgrades-sydney", "Car Park Upgrades"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/strata-lighting-compliance-sydney", "Strata Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
    ],
})

# ---- PAGE 12: Aged Care & Healthcare ----
pages.append({
    "filename": "aged-care-and-healthcare-lighting-automation-sydney.html",
    "title": "Aged Care & Healthcare Lighting Automation Sydney | C-Bus & Dynalite",
    "meta": "Aged care and healthcare lighting automation Sydney. C-Bus and Dynalite for aged care facilities, hospitals, clinics. Circadian lighting, AFSS. Call 0422 469 739.",
    "h1": '<h1>Aged Care &amp; Healthcare Lighting<br/><span class="accent">Automation Sydney</span></h1>',
    "lead": '<p class="lead">Specialist lighting automation for aged care and healthcare across Sydney. C-Bus and Dynalite with circadian tuning, nurse call integration, fall prevention and AFSS compliance.</p>',
    "body": make_topic_body(
        "Aged Care & Healthcare Lighting Automation Sydney",
        "Better Care Through <span class=\"accent\">Intelligent Lighting</span>",
        "Lighting in aged care and healthcare directly impacts patient outcomes, staff efficiency and costs. Circadian tuneable white lighting supports residents sleep-wake cycles, reduces falls and improves mood. C-Bus and Dynalite deliver precise control over every zone.",
        "We have programmed lighting in aged care, hospitals and clinics across Sydney. Systems integrate circadian tuning, night-time fall prevention, nurse call integration and emergency compliance for healthcare environments.",
        ["Circadian tuneable white lighting",
         "Night-time fall prevention dimming",
         "Nurse call system integration",
         "Patient room scene control",
         "AFSS-compliant emergency lighting",
         "Staff zone control for treatment"],
        "Healthcare C-Bus & Dynalite",
        "Specialist aged care and healthcare lighting automation. Accredited programmers with healthcare sector experience.",
        "10+ Years Healthcare Experience",
        "Former Clipsal National Support. Understanding of healthcare requirements and patient-centred design.",
        "Sydney Healthcare Coverage",
        "Based in Menai, servicing aged care, hospitals and clinics across Greater Sydney and regional NSW.",
        [
            ("\U0001f3e8", "Aged Care Automation", "Circadian lighting, fall prevention and nurse call integration.", "/aged-care-and-healthcare-lighting-automation-sydney"),
            ("\U0001f3e5", "Hospital Lighting", "Treatment room, ward and waiting area control.", "/aged-care-and-healthcare-lighting-automation-sydney"),
            ("\U0001f691", "Emergency Compliance", "AS/NZS 2293 emergency lighting with automated testing.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f331", "Circadian Tuning", "Tuneable white LED for natural sleep-wake cycles.", "/aged-care-and-healthcare-lighting-automation-sydney"),
            ("\U0001f50c", "Nurse Call Integration", "Integration with nurse call and BMS platforms.", "/building-automation-maintenance-sydney"),
            ("\u26a1", "AFSS Compliance", "Emergency lighting with automated logbook management.", "/emergency-lighting-compliance-afss-sydney"),
        ],
        [
            ("\U0001f331", "Circadian tuning for sleep"),
            ("\U0001f6b8", "Fall prevention lighting"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f4a1", "Optimal clinical lighting"),
            ("\U0001f6e1\ufe0f", "Nurse call integration"),
            ("\U0001f4b0", "Energy savings 50%+"),
            ("\u23f0", "24/7 reliable operation"),
            ("\U0001f4f1", "Staff zone controls"),
            ("\U0001f3e5", "Infection control design"),
            ("\U0001f6e0\ufe0f", "Accredited technicians"),
            ("\U0001f3af", "Fixed-price packages"),
            ("\U0001f527", "Ongoing support"),
        ],
        "Healthcare Lighting Across Sydney",
        "C-Bus and Dynalite for aged care and healthcare. Circadian lighting, fall prevention, AFSS compliance.",
        [
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-automation-maintenance-sydney", "\U0001f3e2", "Building Automation"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is aged care lighting automation?", "C-Bus or Dynalite automation with circadian lighting, fall prevention, nurse call integration and AFSS-compliant emergency systems."),
        ("Does circadian lighting improve wellbeing?", "Yes. Research shows improved sleep quality, reduced agitation in dementia patients and healthier sleep-wake cycles."),
        ("How does fall prevention work?", "Occupancy sensors activate low-level corridor and bathroom lighting at night for safe illumination."),
        ("Does healthcare lighting meet compliance?", "Yes. Complies with AS/NZS 2293, AS 1680, NCC 2025 and aged care quality standards."),
        ("What areas do you service?", "Aged care homes, hospitals and clinics across Greater Sydney and regional NSW."),
    ],
    "seo": [
        ("/aged-care-and-healthcare-lighting-automation-sydney", "Aged Care Lighting Sydney"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-automation-maintenance-sydney", "Building Automation"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
    ],
})

# ---- PAGE 13: Educational Facilities Lighting ----
pages.append({
    "filename": "educational-facilities-lighting-automation-sydney.html",
    "title": "Educational Facilities Lighting Automation Sydney | C-Bus & Dynalite",
    "meta": "Educational facilities lighting automation Sydney. C-Bus and Dynalite for schools, universities, TAFE. Circadian lighting, energy savings, AFSS. Call 0422 469 739.",
    "h1": '<h1>Educational Facilities<br/><span class="accent">Lighting Automation Sydney</span></h1>',
    "lead": '<p class="lead">Intelligent lighting for educational facilities across Sydney. C-Bus and Dynalite for classrooms, lecture theatres, libraries. Circadian lighting, energy savings, AFSS compliance.</p>',
    "body": make_topic_body(
        "Educational Facilities Lighting Sydney",
        "Lighting That <span class=\"accent\">Enhances Learning</span>",
        "Educational lighting directly influences student engagement and outcomes. Circadian-tuneable lighting with appropriate colour temperatures improves test scores by up to 15%. C-Bus and Dynalite deliver optimal illumination for every learning space.",
        "We have programmed lighting in schools, universities and TAFE across Sydney. Classrooms, lecture theatres, libraries, labs, sports halls and admin spaces each individually programmed with schedules, occupancy sensors and daylight harvesting.",
        ["Circadian tuneable white classroom lighting",
         "Lecture theatre multi-mode scenes",
         "Library quiet study and group work zones",
         "Sports hall assembly/sport modes",
         "Campus-wide centralised management",
         "AFSS-compliant emergency lighting"],
        "Education C-Bus & Dynalite",
        "Complete educational lighting automation. Accredited programmers with extensive education experience.",
        "10+ Years Education Experience",
        "Former Clipsal National Support. Schools, universities and TAFE campuses across Sydney.",
        "Sydney Education Coverage",
        "Based in Menai, servicing all educational facilities across Greater Sydney.",
        [
            ("\U0001f3eb", "Classroom Lighting", "Tuneable white circadian lighting with occupancy sensors and daylight harvesting.", "/educational-facilities-lighting-automation-sydney"),
            ("\U0001f4da", "Library Lighting", "Zoned lighting for quiet study and group work.", "/university-and-tafe-lighting-automation"),
            ("\U0001f3d2", "Sports Hall Lighting", "Multi-mode hall: assembly, sports, performance.", "/schools-lighting-control"),
            ("\u26a1", "AFSS Compliance", "Emergency lighting for schools with logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f331", "Energy & Sustainability", "60% energy savings with occupancy and daylight sensors.", "/building-lighting-upgrades-sydney"),
            ("\U0001f50c", "Campus Management", "Centralised dashboard for facilities teams.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f3a8", "Circadian tuning improves learning"),
            ("\U0001f4b0", "Reduce energy costs by 60%"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f331", "Daylight harvesting"),
            ("\U0001f4f1", "Facilities dashboard"),
            ("\u23f0", "Same-day service"),
            ("\U0001f6e0\ufe0f", "Accredited technicians"),
            ("\U0001f4ca", "Energy reporting"),
            ("\U0001f3af", "Fixed-price packages"),
            ("\U0001f527", "Maintenance contracts"),
            ("\U0001f3eb", "Designed for schools"),
            ("\U0001f3db\ufe0f", "Campus-wide integration"),
        ],
        "Educational Lighting Across Sydney",
        "C-Bus and Dynalite for schools, universities and TAFE. Circadian lighting, energy savings, AFSS.",
        [
            ("/schools-lighting-control", "\U0001f3eb", "Schools Lighting"),
            ("/university-and-tafe-lighting-automation", "\U0001f3db\ufe0f", "University Lighting"),
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is educational lighting automation?", "C-Bus or Dynalite control with circadian classroom lighting, occupancy-based saving, daylight harvesting and AFSS emergency systems."),
        ("Does circadian lighting improve results?", "Yes. Studies show up to 15% improvement in academic performance with circadian-tuneable lighting."),
        ("How much can educational lighting save?", "Typical savings of 50-60% on lighting energy costs."),
        ("Does it meet compliance?", "Yes. Complies with AS/NZS 2293, AS 1680, NCC 2025 and Department of Education standards."),
        ("What facilities do you service?", "Schools, universities (USYD, UNSW, UTS, Macquarie), TAFE campuses and early learning centres."),
    ],
    "seo": [
        ("/schools-lighting-control", "Schools Lighting Sydney"),
        ("/university-and-tafe-lighting-automation", "University Lighting"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-lighting-upgrades-sydney", "Building Upgrades"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
    ],
})

# ---- PAGE 14: Heritage & Church Lighting ----
pages.append({
    "filename": "heritage-and-church-lighting-automation-sydney.html",
    "title": "Heritage & Church Lighting Automation Sydney | C-Bus & Dynalite",
    "meta": "Heritage and church lighting automation Sydney. C-Bus and Dynalite for heritage buildings, churches, chapels. Discreet automation. Accredited. Call 0422 469 739.",
    "h1": '<h1>Heritage &amp; Church Lighting<br/><span class="accent">Automation Sydney</span></h1>',
    "lead": '<p class="lead">Specialist heritage and church lighting across Sydney. C-Bus and Dynalite discreetly integrated into heritage buildings, churches and period properties. Preservation-focused automation.</p>',
    "body": make_topic_body(
        "Heritage & Church Lighting Sydney",
        "Preserving Heritage <span class=\"accent\">with Modern Technology</span>",
        "Heritage buildings and churches require a unique approach. C-Bus and Dynalite heritage solutions use discreet keypads, wireless retrofit and heritage-compatible finishes to blend seamlessly with period interiors.",
        "We specialise in heritage and church automation across Sydney. From Victorian churches to Federation chapels, our approach respects heritage listings while delivering modern control with scenes for services, events and security.",
        ["Discreet heritage-compatible keypads",
         "Wireless retrofit for original fabric",
         "Church multi-mode scenes",
         "Period property zone control",
         "Heritage-listed compliance",
         "Integration with original fixtures"],
        "Heritage C-Bus & Dynalite",
        "Specialist heritage and church automation. Accredited programmers with heritage building experience.",
        "Decades of Heritage Experience",
        "Deep experience in heritage properties, churches and listed buildings across Sydney.",
        "Sydney Heritage Specialists",
        "Based in Menai, servicing heritage properties across all Sydney historic suburbs.",
        [
            ("\u26ea", "Church Automation", "Lighting control for services, events and security. Discreet keypads.", "/heritage-and-church-lighting-automation-sydney"),
            ("\U0001f3e0", "Heritage Home Automation", "Period home control for Victorian, Federation, Georgian properties.", "/heritage-lighting-control"),
            ("\U0001f3db\ufe0f", "Listed Building Systems", "Full automation with minimal wall disturbance for listed buildings.", "/heritage-lighting-control"),
            ("\U0001f3a8", "Gallery Lighting", "Conservation-grade dimming with UV protection.", "/heritage-lighting-control"),
            ("\U0001f504", "Wireless Retrofit", "Minimal wall disturbance for heritage properties.", "/cbus-upgrade-sydney"),
            ("\U0001f31f", "Heritage Switches", "C-Bus Neo in heritage finishes matching period decor.", "/heritage-lighting-control"),
        ],
        [
            ("\U0001f3e0", "Preserves architectural heritage"),
            ("\U0001f527", "Wireless minimises damage"),
            ("\U0001f3af", "Heritage-compatible keypads"),
            ("\u26ea", "Church-specific scenes"),
            ("\U0001f3a8", "Conservation-grade dimming"),
            ("\U0001f4f1", "Modern control, period look"),
            ("\u23f0", "Heritage consultation"),
            ("\U0001f6e0\ufe0f", "Accredited technicians"),
            ("\U0001f331", "LED integration"),
            ("\u2705", "Heritage listing compliant"),
            ("\U0001f3af", "Fixed-price heritage packages"),
            ("\U0001f3db\ufe0f", "Sydney heritage expertise"),
        ],
        "Heritage & Church Lighting Across Sydney",
        "C-Bus and Dynalite for heritage buildings, churches and period properties. Discreet automation.",
        [
            ("/heritage-lighting-control", "\U0001f3e0", "Heritage Lighting"),
            ("/cbus-upgrade-sydney", "\U0001f504", "C-Bus Upgrades"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
        ]
    ),
    "faq": [
        ("Can automation be installed in heritage buildings?", "Yes. Wireless retrofit, discreet keypads and heritage-compatible finishes minimise wall disturbance and respect listings."),
        ("How do you protect original fabric?", "Wireless technology, existing conduits and surface-mount solutions minimise any impact on original materials."),
        ("What church scenes do you program?", "Service (bright/warm), Event (festive), Clean (full), Security (low-level) and Emergency (AS/NZS 2293 egress)."),
        ("How much does heritage automation cost?", "20-30% more than standard. Projects range from $5,000-$25,000 depending on scope and constraints."),
        ("What heritage areas do you service?", "The Rocks, Paddington, Balmain, Hunters Hill, Mosman, Darling Point, Glebe, Parramatta and historic areas across Sydney."),
    ],
    "seo": [
        ("/heritage-lighting-control", "Heritage Lighting Control"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/residential-lighting-control", "Residential Lighting"),
        ("/lighting-control-repair-sydney", "Lighting Repair"),
    ],
})

# ---- PAGE 15: Substation & Plant Room ----
pages.append({
    "filename": "substation-and-plant-room-sydney-lighting-automation.html",
    "title": "Substation & Plant Room Lighting Sydney | C-Bus & Dynalite Automation",
    "meta": "Substation and plant room lighting automation Sydney. C-Bus and Dynalite for substations, plant rooms. Harsh environment, 24/7 reliability, AFSS. Call 0422 469 739.",
    "h1": '<h1>Substation &amp; Plant Room Lighting<br/><span class="accent">Automation Sydney</span></h1>',
    "lead": '<p class="lead">Robust lighting for substations, plant rooms and switch rooms across Sydney. C-Bus and Dynalite for harsh environments with 24/7 reliability and emergency compliance.</p>',
    "body": make_topic_body(
        "Substation & Plant Room Lighting Sydney",
        "Heavy-Duty Automation <span class=\"accent\">for Critical Infrastructure</span>",
        "Substations and plant rooms demand lighting that is reliable, robust and compliant. C-Bus and Dynalite for critical infrastructure deliver 24/7 reliability with remote monitoring, automated emergency testing and SCADA integration.",
        "We have programmed lighting for substations, plant rooms and utility facilities across Sydney. Industrial-grade hardware, sealed enclosures and redundant power supplies. Remote monitoring enables facilities teams to check status and receive alerts from anywhere.",
        ["Industrial-grade hardware",
         "24/7 remote monitoring and control",
         "SCADA and BMS integration",
         "AS/NZS 2293 emergency compliance",
         "Sealed enclosures for harsh environments",
         "Redundant power supply options"],
        "Industrial C-Bus & Dynalite",
        "Specialist industrial automation for critical infrastructure. Accredited programmers.",
        "10+ Years Industrial Experience",
        "Substations, plant rooms and critical infrastructure across Sydney and NSW.",
        "Sydney Industrial Coverage",
        "Based in Menai, servicing substations and plant rooms across all Sydney industrial zones.",
        [
            ("\u26a1", "Substation Lighting", "Fail-safe emergency systems with remote monitoring and SCADA integration.", "/substation-and-plant-room-sydney-lighting-automation"),
            ("\U0001f3ed", "Plant Room Lighting", "Sealed enclosures and temperature-rated components.", "/substation-and-plant-room-sydney-lighting-automation"),
            ("\U0001f50c", "Switch Room Lighting", "Occupancy sensors with emergency compliance.", "/substation-and-plant-room-sydney-lighting-automation"),
            ("\U0001f6e1\ufe0f", "Emergency Compliance", "AS/NZS 2293 with automated testing and logbook.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f6e0\ufe0f", "Remote Monitoring", "24/7 status, alerts and comprehensive reporting.", "/lighting-control-maintenance-sydney"),
            ("\U0001f3ed", "BMS & SCADA", "Integration with BMS and SCADA for unified control.", "/building-automation-maintenance-sydney"),
        ],
        [
            ("\u26a1", "24/7 reliable operation"),
            ("\U0001f6e1\ufe0f", "Fail-safe emergency lighting"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f50c", "Remote monitoring"),
            ("\U0001f3ed", "Industrial-grade hardware"),
            ("\U0001f6e0\ufe0f", "SCADA integration"),
            ("\U0001f7e2", "Redundant power options"),
            ("\u23f0", "Rapid emergency response"),
            ("\U0001f4ca", "Comprehensive reporting"),
            ("\U0001f331", "Energy-efficient operation"),
            ("\U0001f682", "Hazardous area suitable"),
            ("\U0001f4f1", "Remote dashboard access"),
        ],
        "Substation & Plant Room Lighting Across Sydney",
        "C-Bus and Dynalite for critical infrastructure. 24/7 reliability, AFSS compliance, remote monitoring.",
        [
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/building-automation-maintenance-sydney", "\U0001f3ed", "Building Automation"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
        ]
    ),
    "faq": [
        ("What is substation lighting automation?", "C-Bus or Dynalite with industrial hardware for substations and plant rooms. Fail-safe emergency, remote monitoring, SCADA integration."),
        ("Is equipment suitable for harsh environments?", "Yes. Industrial-grade with sealed enclosures, temperature-rated components and redundant power supplies."),
        ("Can it be monitored remotely?", "Yes. 24/7 remote monitoring with real-time status, alerts and comprehensive reporting."),
        ("Does it comply with emergency standards?", "Yes. Full AS/NZS 2293 compliance with automated testing and logbook management."),
        ("What areas do you service?", "All Sydney industrial zones including Western Sydney, Alexandria, Botany, Chullora and regional NSW."),
    ],
    "seo": [
        ("/substation-and-plant-room-sydney-lighting-automation", "Substation Lighting Sydney"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/building-automation-maintenance-sydney", "Building Automation Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
    ],
})

# ---- PAGE 16: University & TAFE Lighting ----
pages.append({
    "filename": "university-and-tafe-lighting-automation.html",
    "title": "University & TAFE Lighting Automation Sydney | C-Bus & Dynalite",
    "meta": "University and TAFE lighting automation Sydney. C-Bus and Dynalite for lecture theatres, labs, libraries, campuses. Circadian, energy savings. Call 0422 469 739.",
    "h1": '<h1>University &amp; TAFE Lighting<br/><span class="accent">Automation Sydney</span></h1>',
    "lead": '<p class="lead">Comprehensive lighting for universities and TAFE across Sydney. C-Bus and Dynalite for lecture theatres, labs, libraries and campus-wide systems. Circadian lighting, energy savings, AFSS.</p>',
    "body": make_topic_body(
        "University & TAFE Lighting Sydney",
        "Campus-Wide Lighting <span class=\"accent\">for Higher Education</span>",
        "University campuses present complex lighting challenges with diverse spaces, 24/7 operation and varying occupancy. C-Bus and Dynalite delivers flexible automation for lecture theatres, labs, libraries and study zones, all managed from a central dashboard.",
        "We have programmed lighting at major Sydney universities and TAFE campuses. Systems integrate circadian-tuneable lighting, multi-mode lecture scenes, 24/7 library control and timetable integration for automated lighting based on room bookings.",
        ["Lecture theatre multi-mode scenes",
         "Library 24/7 zone control",
         "Laboratory task zone lighting",
         "Campus-wide centralised management",
         "Timetable integration",
         "AFSS-compliant emergency lighting"],
        "Higher Education C-Bus & Dynalite",
        "Complete campus lighting automation. Accredited programmers with higher education experience.",
        "10+ Years University Experience",
        "Major Sydney universities and TAFE NSW campuses programmed.",
        "Sydney University Coverage",
        "Based in Menai, servicing all Sydney universities and TAFE campuses.",
        [
            ("\U0001f3eb", "Lecture Theatre Control", "Multi-mode lighting for lectures, exams and presentations.", "/university-and-tafe-lighting-automation"),
            ("\U0001f4da", "Library Lighting", "24/7 zoned control for study areas.", "/university-and-tafe-lighting-automation"),
            ("\U0001f52c", "Laboratory Lighting", "Task zone lighting for labs and research spaces.", "/university-and-tafe-lighting-automation"),
            ("\u26a1", "AFSS Compliance", "Campus-wide emergency lighting compliance.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f331", "Energy Management", "60% energy savings with occupancy and daylight sensors.", "/building-lighting-upgrades-sydney"),
            ("\U0001f50c", "Campus Dashboard", "Centralised management for facilities teams.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f3a8", "Circadian tuning for students"),
            ("\U0001f4b0", "Reduce campus energy by 60%"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f331", "Daylight harvesting"),
            ("\U0001f4f1", "Facilities dashboard"),
            ("\u23f0", "Same-day service Sydney"),
            ("\U0001f6e0\ufe0f", "Accredited technicians"),
            ("\U0001f4ca", "Energy reporting"),
            ("\U0001f3af", "Fixed-price packages"),
            ("\U0001f527", "Maintenance contracts"),
            ("\U0001f3db\ufe0f", "Campus-wide integration"),
            ("\u23f3", "Timetable integration"),
        ],
        "University & TAFE Lighting Across Sydney",
        "C-Bus and Dynalite for higher education. Circadian lighting, energy savings, AFSS.",
        [
            ("/schools-lighting-control", "\U0001f3eb", "Schools Lighting"),
            ("/educational-facilities-lighting-automation-sydney", "\U0001f4da", "Education Lighting"),
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is university lighting automation?", "C-Bus or Dynalite campus-wide control with circadian lighting, lecture scenes, 24/7 library zones and timetable integration."),
        ("Can lighting integrate with timetabling?", "Yes. Systems integrate with university timetabling for automated lighting based on room bookings, maximising energy savings."),
        ("How much can a campus save?", "Typical campus energy savings of 50-60% through occupancy automation and scheduling."),
        ("Does it meet compliance?", "Yes. Complies with AS/NZS 2293, AS 1680, NCC 2025 and university standards."),
        ("What campuses do you service?", "USYD, UNSW, UTS, Macquarie, Western Sydney University and all TAFE NSW campuses."),
    ],
    "seo": [
        ("/schools-lighting-control", "Schools Lighting Sydney"),
        ("/educational-facilities-lighting-automation-sydney", "Education Lighting Sydney"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/building-lighting-upgrades-sydney", "Building Upgrades"),
    ],
})




# ---- PAGE 17: Lighting Control Rose Bay ----
pages.append({
    "filename": "lighting-control-rose-bay.html",
    "title": "Lighting Control Rose Bay | C-Bus & Dynalite Home Automation Specialists",
    "meta": "Lighting control Rose Bay. C-Bus and Dynalite home automation for Rose Bay homes and apartments. Smart scenes, Apple Home, energy savings. Call 0422 469 739.",
    "h1": '<h1>Lighting Control Rose Bay<br/><span class="accent">C-Bus &amp; Dynalite Specialists</span></h1>',
    "lead": '<p class="lead">Professional lighting control in Rose Bay. C-Bus and Dynalite home automation for waterfront homes and apartments. Smart scenes, Apple HomeKit, voice control. Based in Menai, serving the Eastern Suburbs daily.</p>',
    "body": make_topic_body(
        "Lighting Control Rose Bay",
        "Premium Lighting Control <span class=\"accent\">for Rose Bay Homes</span>",
        "Rose Bay is home to some of Sydney finest waterfront properties, and your home deserves lighting control that matches its calibre. C-Bus and Dynalite systems deliver sophisticated automation with scenes tailored to your lifestyle from sweeping harbour views by day to intimate entertaining by night.",
        "We regularly service Rose Bay and the surrounding Eastern Suburbs. Our accredited technicians have programmed C-Bus and Dynalite systems in Rose Bay luxury homes, apartments and harbour-front properties. Every system is designed for energy efficiency, Apple HomeKit integration and seamless operation.",
        ["Custom scene control for harbour-view entertaining",
         "Apple HomeKit, Siri and Alexa voice control",
         "Automated schedules synced to sunrise/sunset",
         "Outdoor entertaining zone control",
         "Integration with blinds, climate and security",
         "Energy-efficient LED-compatible dimming"],
        "Rose Bay C-Bus & Dynalite",
        "Complete lighting control for Rose Bay homes. C-Bus and Dynalite programming, commissioning and maintenance. Accredited Clipsal/Schneider specialists.",
        "Eastern Suburbs Expertise",
        "Years of experience in Rose Bay and Eastern Suburbs luxury homes. Deep understanding of harbour-front property requirements.",
        "Rose Bay & Eastern Suburbs",
        "Based in Menai with regular Rose Bay service days. Same-day callouts available. No travel surcharge in the Eastern Suburbs.",
        [
            ("\U0001f3e0", "Whole-Home Automation", "Complete C-Bus and Dynalite systems with centralised control via keypads, touchscreens and smartphone apps.", "/c-bus-programmer-sydney"),
            ("\U0001f31f", "Apple HomeKit Integration", "Control your Rose Bay home with Siri and the Apple Home app. Full HomeKit compatibility with C-Bus gateway.", "/c-bus-apple-homekit-sydney"),
            ("\U0001f319", "Outdoor Entertaining Lighting", "Automated alfresco lighting with sunset triggers, scene control and integration with outdoor kitchens and pools.", "/residential-lighting-control"),
            ("\U0001f4f1", "Voice & App Control", "Control lights from anywhere using your smartphone or voice assistants. Google Home and Alexa also supported.", "/cbus-specialist-sydney"),
            ("\u26a1", "Energy-Efficient Automation", "Reduce energy costs with occupancy-based automation and daylight harvesting. LED-compatible drivers.", "/cbus-upgrade-sydney"),
            ("\U0001f6e1\ufe0f", "Ongoing Support", "Regular maintenance, firmware updates and priority callouts for Rose Bay clients.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f973", "Luxury scenes for harbour views"),
            ("\U0001f4f1", "Control from anywhere"),
            ("\U0001f31f", "Apple Home, Google Home & Alexa"),
            ("\U0001f4a1", "Smooth LED dimming"),
            ("\U0001f4b0", "Energy savings up to 60%"),
            ("\U0001f3e0", "Increase property value"),
            ("\u23f0", "Same-day Eastern Suburbs service"),
            ("\U0001f512", "Integrated security & blinds"),
            ("\U0001f3af", "Fixed-price packages"),
            ("\U0001f6e1\ufe0f", "Secure remote access"),
            ("\U0001f331", "Eco-friendly automation"),
            ("\u2699\ufe0f", "Lifetime system support"),
        ],
        "Lighting Control for Rose Bay Homes",
        "C-Bus and Dynalite home automation for Rose Bay. Smart scenes, voice control, energy savings. Accredited specialists serving the Eastern Suburbs.",
        [
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus + Apple HomeKit"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/cbus-upgrade-sydney", "\u26a1", "C-Bus Upgrades"),
            ("/cbus-specialist-sydney", "\u2b50", "C-Bus Specialist"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
        ]
    ),
    "faq": [
        ("What lighting control systems are popular in Rose Bay?", "C-Bus by Clipsal/Schneider Electric is the most popular lighting control system in Rose Bay luxury homes. Dynalite is also common in high-end apartments. Both offer Apple HomeKit integration and custom scene control."),
        ("Can I control lighting in my Rose Bay home with my phone?", "Absolutely. Both C-Bus and Dynalite offer smartphone apps for remote control. With the C-Bus HomeKit gateway, you can control lights via Siri and the Apple Home app from anywhere in the world."),
        ("How much does lighting control cost in Rose Bay?", "A typical Rose Bay home system ranges from $4,000 to $15,000 for programming and commissioning, depending on the number of zones and features. Luxury harbour-front properties with full integration range higher."),
        ("Do you service Rose Bay regularly?", "Yes. We have clients throughout the Eastern Suburbs and visit Rose Bay regularly. Same-day callouts are available for urgent issues."),
        ("Does lighting control add value to a Rose Bay property?", "Yes. Smart home automation with C-Bus or Dynalite is a desirable feature in the premium Rose Bay property market. It increases resale value and reduces energy costs."),
    ],
    "seo": [
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus + Apple HomeKit"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/cbus-specialist-sydney", "C-Bus Specialist Sydney"),
        ("/residential-lighting-control", "Residential Lighting"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
    ],
})

# ---- PAGE 18: Smart Home ROI: Property Value Sydney ----
pages.append({
    "filename": "smart-home-roi-calculator-property-value-sydney.html",
    "title": "Smart Home ROI: Property Value Sydney | Home Automation Adds Value",
    "meta": "Smart home ROI property value Sydney. How C-Bus and Dynalite automation increases home resale value. ROI calculator, market data. Call 0422 469 739.",
    "h1": '<h1>Smart Home ROI: Property Value<br/><span class="accent">Sydney Market Analysis</span></h1>',
    "lead": '<p class="lead">How much value does smart home automation add to your Sydney property? Data-driven analysis of C-Bus and Dynalite home automation ROI in the Sydney property market. Based in Menai, serving all of Sydney.</p>',
    "body": make_topic_body(
        "Smart Home ROI Property Value Sydney",
        "Does Home Automation <span class=\"accent\">Increase Property Value?</span>",
        "Sydney property owners are increasingly investing in smart home automation not just for lifestyle convenience but as a strategic property improvement. C-Bus and Dynalite lighting control systems can increase property values by 3-8% according to recent real estate data, with premium buyers actively seeking automated homes.",
        "This page analyses the return on investment for C-Bus and Dynalite home automation in the Sydney property market. We examine resale value uplift, buyer preferences, energy savings and the overall ROI picture for homeowners considering lighting automation.",
        ["Property value uplift of 3-8% with full automation",
         "Energy savings of 40-60% reducing ongoing costs",
         "Premium buyer preference for automated homes",
         "Apple HomeKit integration as selling point",
         "Reduced time on market for smart homes",
         "Insurance benefits with monitored systems"],
        "ROI Analysis & Market Data",
        "Comprehensive ROI analysis for home automation in Sydney. Property value data, energy savings projections and market trend analysis.",
        "Property Market Expertise",
        "Years of experience installing automation in Sydney premium suburbs. Direct feedback from real estate agents and property valuers on smart home value.",
        "Sydney-Wide Property Coverage",
        "Based in Menai, serving all Sydney property markets from Eastern Suburbs prestige homes to North Shore family residences.",
        [
            ("\U0001f4b0", "Property Value Calculator", "Estimate the value uplift from C-Bus or Dynalite automation based on your property type, location and system scope.", "/c-bus-programmer-sydney"),
            ("\U0001f3e0", "Resale Value Analysis", "How smart home features influence buyer decisions in the Sydney property market. Data from recent sales.", "/residential-lighting-control"),
            ("\u26a1", "Energy Savings ROI", "Calculate your monthly energy savings from automated lighting. Typical savings of 40-60% on lighting costs.", "/cbus-upgrade-sydney"),
            ("\U0001f31f", "Apple HomeKit Premium", "Properties with Apple HomeKit integration sell faster and at a premium. C-Bus HomeKit gateway details.", "/c-bus-apple-homekit-sydney"),
            ("\U0001f4ca", "Market Data & Trends", "Sydney smart home market trends 2026. Which suburbs show highest demand for automated properties.", "/smart-home-roi-calculator-sydney"),
            ("\U0001f527", "Automation Cost Guide", "Typical costs for different automation levels. From basic lighting control to full home integration.", "/sydney-home-automation-cost-guide-2026"),
        ],
        [
            ("\U0001f4b0", "3-8% property value increase"),
            ("\U0001f3e0", "Faster sale in premium market"),
            ("\u26a1", "40-60% energy cost reduction"),
            ("\U0001f31f", "Apple HomeKit buyer appeal"),
            ("\U0001f4ca", "Data-driven ROI projections"),
            ("\U0001f4f1", "Smart home buyer preference"),
            ("\u23f0", "Quick installation timeline"),
            ("\U0001f3af", "Fixed-price automation packages"),
            ("\U0001f512", "Enhanced security value"),
            ("\U0001f3e8", "Luxury market differentiator"),
            ("\U0001f331", "Sustainable home appeal"),
            ("\U0001f6e0\ufe0f", "Accredited installations"),
        ],
        "Smart Home ROI Across Sydney",
        "C-Bus and Dynalite automation adds real property value. Data-driven ROI analysis for Sydney homeowners. Accredited specialists.",
        [
            ("/smart-home-roi-calculator-sydney", "\U0001f4b0", "ROI Calculator"),
            ("/sydney-home-automation-cost-guide-2026", "\U0001f4b5", "Cost Guide 2026"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus + Apple HomeKit"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
            ("/cbus-upgrade-sydney", "\u26a1", "C-Bus Upgrades"),
        ]
    ),
    "faq": [
        ("How much does smart home automation increase property value in Sydney?", "Industry data suggests C-Bus and Dynalite automation can increase property values by 3-8% in the Sydney market. Premium suburbs like Mosman, Vaucluse and Rose Bay show the highest uplift."),
        ("What is the ROI timeline for home automation?", "Most Sydney homeowners recoup their investment within 2-3 years through energy savings alone, with the property value uplift providing additional return on sale."),
        ("Does Apple HomeKit integration add more value?", "Yes. Apple HomeKit compatibility is a highly sought-after feature in the Sydney premium property market. Homes with HomeKit integration typically sell faster and at a higher price point."),
        ("Do smart homes sell faster in Sydney?", "Yes. Real estate data shows that homes with professional C-Bus or Dynalite automation spend less time on the market, particularly in the premium Eastern Suburbs and North Shore markets."),
        ("What level of automation provides the best ROI?", "Full lighting control with scenes, schedules, voice control and Apple HomeKit integration provides the strongest ROI. Basic systems still add value but premium automation delivers the highest returns."),
    ],
    "seo": [
        ("/smart-home-roi-calculator-sydney", "Smart Home ROI Calculator"),
        ("/sydney-home-automation-cost-guide-2026", "Home Automation Cost Guide"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus + Apple HomeKit"),
        ("/residential-lighting-control", "Residential Lighting"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/cbus-specialist-sydney", "C-Bus Specialist Sydney"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
    ],
})

# ---- PAGE 19: Smart Lighting Energy Management for Hospitality ----
pages.append({
    "filename": "smart-lighting-energy-management-sydney-hospitality.html",
    "title": "Smart Lighting Energy Management for Hospitality | Sydney Hotels & Restaurants",
    "meta": "Smart lighting energy management for hospitality Sydney. C-Bus and Dynalite energy saving for hotels, restaurants. Reduce costs, AFSS. Call 0422 469 739.",
    "h1": '<h1>Smart Lighting Energy Management<br/><span class="accent">for Hospitality Sydney</span></h1>',
    "lead": '<p class="lead">Reduce hospitality energy costs with C-Bus and Dynalite smart lighting management. Hotels, restaurants and bars across Sydney saving 40-60% on lighting energy. Accredited specialists based in Menai.</p>',
    "body": make_topic_body(
        "Smart Lighting Energy Management Hospitality Sydney",
        "Energy-Efficient Lighting <span class=\"accent\">for Hospitality Venues</span>",
        "Hospitality venues face rising energy costs with lighting accounting for 25-40% of electricity consumption. C-Bus and Dynalite smart lighting energy management delivers substantial savings through occupancy-based automation, scheduled dimming and daylight harvesting without compromising guest experience.",
        "We have implemented energy management systems in Sydney hotels, restaurants, bars and function centres. Our approach combines guest comfort with aggressive energy reduction, typically cutting lighting energy consumption by 40-60% with ROI within 12-24 months.",
        ["Occupancy-based guest room energy saving",
         "Restaurant zone scheduling (Lunch, Dinner, Clean)",
         "Daylight harvesting in dining and common areas",
         "Back-of-house occupancy automation",
         "Energy consumption monitoring and reporting",
         "PMS integration for check-in/out automation"],
        "Hospitality Energy Management",
        "Complete smart lighting energy management for hospitality. C-Bus and Dynalite systems with accredited programming and ongoing support.",
        "Hospitality Energy Expertise",
        "Years of hospitality energy management experience in Sydney venues. Proven 40-60% energy reductions.",
        "Sydney Hospitality Coverage",
        "Based in Menai, servicing hotels, restaurants and bars across Sydney CBD, The Rocks, Darling Harbour, Surry Hills and all hospitality precincts.",
        [
            ("\U0001f3e8", "Hotel Energy Management", "Guest room occupancy sensors, PMS integration and centralised energy monitoring for hotel chains.", "/hospitality-lighting-control"),
            ("\U0001f37d\ufe0f", "Restaurant Energy Saving", "Time-of-day zone scheduling, daylight harvesting and occupancy sensors for restaurant lighting.", "/hospitality-lighting-control"),
            ("\U0001f37a", "Bar & Nightclub Efficiency", "Late-night energy-saving modes, zone control and consumption reporting for bars and clubs.", "/smart-lighting-energy-management-sydney-hospitality"),
            ("\u26a1", "AFSS Emergency Compliance", "Compliant emergency lighting with automated testing, reducing compliance costs.", "/emergency-lighting-hotels-hospitality-sydney"),
            ("\U0001f4ca", "Energy Monitoring Dashboard", "Real-time energy consumption data, trend analysis and automated reporting for venue managers.", "/building-automation-maintenance-sydney"),
            ("\U0001f504", "LED Upgrade & Control", "LED retrofit combined with smart control for maximum energy savings and quickest ROI.", "/led-upgrade-carpark-lighting-sydney"),
        ],
        [
            ("\U0001f4b0", "40-60% lighting energy reduction"),
            ("\u2705", "AFSS emergency compliance"),
            ("\U0001f4ca", "Real-time energy monitoring"),
            ("\U0001f3e8", "PMS integrated automation"),
            ("\U0001f331", "Daylight harvesting"),
            ("\u23f0", "24/7 venue operation support"),
            ("\U0001f3af", "Fixed-price energy packages"),
            ("\U0001f4f1", "Manager dashboard access"),
            ("\U0001f512", "Guest comfort maintained"),
            ("\U0001f4b5", "ROI in 12-24 months"),
            ("\U0001f6e0\ufe0f", "Accredited technicians"),
            ("\U0001f3ed", "NABERS-friendly systems"),
        ],
        "Energy Management for Sydney Hospitality",
        "C-Bus and Dynalite smart lighting energy management for hotels, restaurants and bars. 40-60% savings, AFSS compliance.",
        [
            ("/hospitality-lighting-control", "\U0001f3e8", "Hospitality Lighting"),
            ("/emergency-lighting-hotels-hospitality-sydney", "\u26a1", "Hospitality Emergency"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-automation-maintenance-sydney", "\U0001f3e2", "Building Automation"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("How much energy can hospitality lighting management save?", "Hospitality venues typically save 40-60% on lighting energy costs with C-Bus or Dynalite energy management. This translates to significant operational cost reductions for hotels and restaurants."),
        ("Does energy management affect guest experience?", "No. Our systems are designed to maintain or improve guest experience while reducing energy. Guest room scenes remain fully functional; savings come from unoccupied spaces and scheduled zones."),
        ("Can hospitality lighting integrate with my PMS?", "Yes. C-Bus and Dynalite integrate with major hotel Property Management Systems for automated check-in/out lighting modes, housekeeping status and energy optimisation."),
        ("How long does ROI take for hospitality energy management?", "Most hospitality venues achieve ROI within 12-24 months through energy savings alone. Government incentives and rebates may accelerate the payback period."),
        ("Does the system comply with hospitality regulations?", "Yes. Our systems comply with AS/NZS 2293 for emergency lighting, AS 1680 for illumination levels and NCC 2025 energy efficiency requirements."),
    ],
    "seo": [
        ("/hospitality-lighting-control", "Hospitality Lighting Sydney"),
        ("/smart-lighting-energy-management-sydney-hospitality", "Hospitality Energy Management"),
        ("/emergency-lighting-hotels-hospitality-sydney", "Hospitality Emergency Lighting"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-automation-maintenance-sydney", "Building Automation Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/led-upgrade-carpark-lighting-sydney", "LED Upgrades Sydney"),
    ],
})

# ---- PAGE 20: Sydney Home Automation Cost Guide 2026 ----
pages.append({
    "filename": "sydney-home-automation-cost-guide-2026.html",
    "title": "Sydney Home Automation Cost Guide 2026 | C-Bus & Dynalite Pricing",
    "meta": "Sydney home automation cost guide 2026. C-Bus and Dynalite pricing for homes. Programming, hardware, installation costs. Fixed-price quotes. Call 0422 469 739.",
    "h1": '<h1>Sydney Home Automation<br/><span class="accent">Cost Guide 2026</span></h1>',
    "lead": '<p class="lead">Transparent pricing for C-Bus and Dynalite home automation in Sydney 2026. Programming costs, hardware estimates, installation fees. Fixed-price quotes from accredited specialists based in Menai.</p>',
    "body": make_topic_body(
        "Sydney Home Automation Cost Guide 2026",
        "Transparent Pricing <span class=\"accent\">for Sydney Home Automation</span>",
        "Planning a C-Bus or Dynalite home automation system in Sydney? Understanding the costs involved is essential for budgeting. This guide breaks down typical pricing for home lighting control in Sydney, from basic keypad systems to full home automation with Apple HomeKit integration.",
        "Costs vary based on system size, number of zones, hardware choices and complexity of programming. We provide fixed-price quotes for all projects and this guide gives you a realistic picture of what to expect for 2026 pricing across different automation levels.",
        ["Basic lighting control: $2,000-$5,000",
         "Mid-range automation: $5,000-$12,000",
         "Full home integration: $12,000-$30,000",
         "Luxury custom systems: $30,000-$80,000+",
         "Hardware costs explained: keypads, relays, power supplies",
         "Programming and commissioning fees breakdown"],
        "Home Automation Cost Guide",
        "Comprehensive cost breakdown for C-Bus and Dynalite home automation in Sydney. Fixed-price quotes from accredited programmers.",
        "10+ Years Sydney Pricing Experience",
        "Former Clipsal National Support. Thousands of Sydney home quotes provided. Transparent, no-surprise pricing.",
        "Sydney-Wide Cost Guide Coverage",
        "Pricing for all Sydney areas including Eastern Suburbs, North Shore, Sutherland Shire, Inner West and Western Sydney.",
        [
            ("\U0001f4b5", "Basic Lighting Control", "Entry-level C-Bus system with 2-4 keypads, basic scenes and scheduling. Ideal for apartments and smaller homes.", "/residential-lighting-control"),
            ("\U0001f3e0", "Mid-Range Automation", "Comprehensive system with 5-10 zones, Apple HomeKit, voice control and outdoor lighting. Most popular choice.", "/residential-lighting-control"),
            ("\U0001f451", "Luxury Full Integration", "Whole-home system with blinds, climate, security and lighting. Premium keypads and custom scenes.", "/c-bus-apple-homekit-sydney"),
            ("\U0001f527", "Retrofit Costs", "Upgrading an existing home with automation. Wireless options, minimal disruption and heritage-compatible solutions.", "/cbus-upgrade-sydney"),
            ("\u2699\ufe0f", "Programming Fees", "Hourly and fixed-price programming options. C-Bus Toolkit and Dynalite Envision programming rates explained.", "/c-bus-programmer-sydney"),
            ("\U0001f4ca", "ROI & Payback Analysis", "How energy savings offset automation costs. Calculate your payback period with smart lighting control.", "/smart-home-roi-calculator-property-value-sydney"),
        ],
        [
            ("\U0001f4b5", "Fixed-price quotes guaranteed"),
            ("\U0001f3af", "No hidden costs or surprises"),
            ("\U0001f4b0", "Energy savings offset costs"),
            ("\U0001f3e0", "Increases property value"),
            ("\u23f0", "Quick installation available"),
            ("\U0001f4ca", "ROI projections included"),
            ("\u2699\ufe0f", "Accredited programming"),
            ("\U0001f31f", "Apple HomeKit included options"),
            ("\U0001f4f1", "App and voice control standard"),
            ("\U0001f6e1\ufe0f", "Warranty and support included"),
            ("\U0001f527", "Retrofit-friendly solutions"),
            ("\U0001f6e0\ufe0f", "Sydney-wide service"),
        ],
        "Home Automation Cost Guide 2026",
        "Transparent C-Bus and Dynalite pricing for Sydney homes. Fixed-price quotes, no surprises. Accredited specialists.",
        [
            ("/smart-home-roi-calculator-property-value-sydney", "\U0001f4b0", "Smart Home ROI"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus + Apple HomeKit"),
            ("/cbus-upgrade-sydney", "\u26a1", "C-Bus Upgrades"),
            ("/cbus-specialist-sydney", "\u2b50", "C-Bus Specialist"),
        ]
    ),
    "faq": [
        ("How much does C-Bus home automation cost in Sydney in 2026?", "Basic C-Bus systems start from $2,000-$5,000 for programming and commissioning. Mid-range systems with Apple HomeKit are $5,000-$12,000. Full luxury home integration ranges from $12,000-$30,000+."),
        ("Does the cost include hardware?", "Our fixed-price quotes typically cover programming, commissioning and configuration. Hardware costs (keypads, relays, power supplies, gateways) are quoted separately or included in turnkey packages."),
        ("Is home automation worth the cost in Sydney?", "Yes. Energy savings of 40-60%, property value increase of 3-8%, and enhanced lifestyle make home automation a sound investment for Sydney homeowners."),
        ("What affects the cost of home automation?", "Key factors: number of zones, keypad count, Apple HomeKit integration, retrofit vs new build, complexity of scenes, and integration with blinds/climate/security."),
        ("Do you offer fixed-price quotes for home automation?", "Yes. We provide fixed-price quotes for all C-Bus and Dynalite projects. No hourly surprises. Contact us on 0422 469 739 for a quote."),
    ],
    "seo": [
        ("/smart-home-roi-calculator-property-value-sydney", "Smart Home ROI"),
        ("/residential-lighting-control", "Residential Lighting"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus + Apple HomeKit"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/cbus-specialist-sydney", "C-Bus Specialist Sydney"),
        ("/sydney-home-automation-cost-guide-2026", "Home Automation Cost Guide"),
        ("/smart-home-roi-calculator-sydney", "Smart Home ROI Calculator"),
    ],
})

# ---- PAGE 21: DALI-2 Implementation & Compliance ----
pages.append({
    "filename": "dali-2-lighting-control-implementation-compliance.html",
    "title": "DALI-2 Implementation & Compliance | Sydney Lighting Control",
    "meta": "DALI-2 lighting control implementation and compliance Sydney. DALI-2 certified systems, NCC 2025 compliance, emergency lighting. Accredited. Call 0422 469 739.",
    "h1": '<h1>DALI-2 Implementation &amp; Compliance<br/><span class="accent">Sydney Commercial Buildings</span></h1>',
    "lead": '<p class="lead">Expert DALI-2 lighting control implementation and compliance for Sydney commercial buildings. Certified DALI-2 systems, NCC 2025 compliance, emergency integration. Accredited specialists based in Menai.</p>',
    "body": make_topic_body(
        "DALI-2 Implementation Compliance Sydney",
        "DALI-2 Certified Lighting <span class=\"accent\">for Commercial Buildings</span>",
        "DALI-2 is the international standard for digital lighting control (IEC 62386), offering interoperability between manufacturers devices, advanced diagnostics and precise individual luminaire control. Sydney commercial buildings are increasingly specifying DALI-2 for compliance with NCC 2025 energy efficiency requirements.",
        "Our team has extensive experience implementing DALI-2 systems in Sydney commercial buildings. From design and device selection through programming and commissioning, we ensure full compliance with DALI-2 certification requirements, NCC 2025 energy efficiency standards and AS/NZS 2293 emergency lighting regulations.",
        ["Full DALI-2 certified system design",
         "Multi-manufacturer device interoperability",
         "Individual luminaire addressing and control",
         "NCC 2025 energy efficiency compliance",
         "AS/NZS 2293 emergency lighting integration",
         "BMS integration via BACnet and Modbus"],
        "DALI-2 Implementation Experts",
        "Complete DALI-2 implementation and compliance services. Certified system design, programming and commissioning.",
        "DALI-2 Technical Expertise",
        "Deep experience with DALI-2 certified products and standards. Understanding of IEC 62386 requirements.",
        "Sydney Commercial Coverage",
        "Based in Menai, servicing commercial buildings across all Sydney business districts.",
        [
            ("\u26a1", "DALI-2 System Design", "Full DALI-2 compliant system design with certified devices, proper bus topology and emergency integration.", "/dali-2-lighting-control-implementation-compliance"),
            ("\u2705", "NCC 2025 Compliance", "DALI-2 systems meeting NCC 2025 energy efficiency requirements for commercial buildings.", "/dali-2-lighting-control-commercial-buildings"),
            ("\U0001f50d", "Emergency Lighting Integration", "DALI-2 based emergency lighting testing per AS/NZS 2293 with automated testing and logbook.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f50c", "BMS & BACnet Integration", "DALI-2 integration with building management systems via BACnet, Modbus and KNX gateways.", "/building-automation-maintenance-sydney"),
            ("\U0001f4ca", "Energy Monitoring & Reporting", "Per-luminaire energy monitoring with DALI-2 for granular consumption data and compliance reporting.", "/lighting-control-maintenance-sydney"),
            ("\U0001f504", "DALI-1 to DALI-2 Upgrades", "Upgrade existing DALI-1 systems to DALI-2 for improved functionality and compliance.", "/dali-lighting-repair"),
        ],
        [
            ("\u2705", "Full DALI-2 certification"),
            ("\U0001f4b0", "Energy savings via precise control"),
            ("\U0001f3e2", "NCC 2025 compliance ready"),
            ("\U0001f50c", "BMS integration standard"),
            ("\U0001f4a1", "Individual luminaire control"),
            ("\U0001f50d", "AS/NZS 2293 emergency compliance"),
            ("\U0001f4ca", "Granular energy monitoring"),
            ("\u23f0", "Same-day commercial callouts"),
            ("\U0001f6e0\ufe0f", "Certified DALI-2 technicians"),
            ("\U0001f3af", "Fixed-price implementation"),
            ("\U0001f527", "Ongoing compliance support"),
            ("\U0001f331", "Future-proof technology"),
        ],
        "DALI-2 Implementation Across Sydney",
        "DALI-2 certified lighting control for Sydney commercial buildings. NCC 2025 compliance, emergency integration.",
        [
            ("/dali-2-lighting-control-commercial-buildings", "\U0001f3e2", "DALI-2 Commercial"),
            ("/dali-2-lighting-control-implementation-compliance", "\u26a1", "DALI-2 Compliance"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-automation-maintenance-sydney", "\U0001f3e2", "Building Automation"),
        ]
    ),
    "faq": [
        ("What is DALI-2 lighting control?", "DALI-2 (IEC 62386) is the international standard for digital lighting control. It enables individual luminaire control, diagnostics and interoperability between different manufacturers DALI-2 certified devices."),
        ("What is the difference between DALI-1 and DALI-2?", "DALI-2 introduces backwards compatibility, enhanced diagnostics, better interoperability certification and support for more device types including application controllers and input devices."),
        ("Is DALI-2 required for NCC 2025 compliance?", "DALI-2 is not explicitly required but is the most effective way to meet NCC 2025 energy efficiency requirements for lighting control in commercial buildings."),
        ("Does DALI-2 support emergency lighting?", "Yes. DALI-2 includes dedicated emergency lighting features for automated testing, status monitoring and compliance with AS/NZS 2293."),
        ("What Sydney buildings use DALI-2?", "DALI-2 is increasingly specified in Sydney commercial offices, retail centres, hospitals, educational facilities and government buildings requiring NCC 2025 compliance."),
    ],
    "seo": [
        ("/dali-2-lighting-control-commercial-buildings", "DALI-2 Commercial Buildings"),
        ("/dali-2-lighting-control-implementation-compliance", "DALI-2 Implementation"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming"),
        ("/dynalite-programmer-sydney", "Dynalite Programming"),
        ("/building-automation-maintenance-sydney", "Building Automation"),
        ("/dali-lighting-repair", "DALI Lighting Repair"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
    ],
})

# ---- PAGE 22: AI-Driven Smart Lighting Energy Management ----
pages.append({
    "filename": "ai-driven-smart-lighting-energy-management-sydney.html",
    "title": "AI-Driven Smart Lighting Energy Management Sydney | Machine Learning",
    "meta": "AI-driven smart lighting energy management Sydney. Machine learning optimises C-Bus and Dynalite for maximum energy savings. Accredited. Call 0422 469 739.",
    "h1": '<h1>AI-Driven Smart Lighting<br/><span class="accent">Energy Management Sydney</span></h1>',
    "lead": '<p class="lead">AI-powered lighting energy management for Sydney buildings. Machine learning optimises C-Bus and Dynalite systems for maximum efficiency. Accredited specialists bringing AI to building automation. Based in Menai.</p>',
    "body": make_topic_body(
        "AI-Driven Smart Lighting Energy Management Sydney",
        "Machine Learning <span class=\"accent\">for Optimal Energy Efficiency</span>",
        "Artificial intelligence is revolutionising building energy management. AI-driven smart lighting systems learn occupancy patterns, weather impacts and usage behaviours to automatically optimise C-Bus and Dynalite lighting control for maximum energy efficiency without compromising comfort.",
        "We integrate AI-powered optimisation engines with C-Bus and Dynalite systems across Sydney commercial and residential buildings. Our systems analyse historical data, real-time sensor inputs and external factors to predict optimal lighting levels, reducing energy consumption by an additional 15-25% on top of standard automation savings.",
        ["Machine learning occupancy prediction",
         "Weather-adaptive daylight harvesting",
         "Behavioural pattern optimisation",
         "Real-time energy consumption analytics",
         "Predictive maintenance alerts",
         "Automated commissioning adjustments"],
        "AI Energy Management",
        "AI-driven optimisation for C-Bus and Dynalite systems. Machine learning for maximum energy efficiency.",
        "AI & Building Automation Expertise",
        "Combined expertise in lighting control systems and artificial intelligence. Pioneering AI-driven building optimisation in Sydney.",
        "Sydney AI Coverage",
        "Based in Menai, deploying AI-driven systems across commercial and residential buildings throughout Greater Sydney.",
        [
            ("\U0001f916", "AI Optimisation Engine", "Machine learning platform that continuously optimises C-Bus and Dynalite settings based on usage patterns and environmental data.", "/ai-driven-smart-lighting-energy-management-sydney"),
            ("\U0001f4ca", "Energy Analytics Dashboard", "Real-time and historical energy analytics with AI-powered recommendations for further savings.", "/lighting-control-maintenance-sydney"),
            ("\U0001f331", "Weather-Adaptive Control", "AI integration with weather forecasts for predictive daylight harvesting and temperature-based adjustments.", "/building-lighting-upgrades-sydney"),
            ("\U0001f6e1\ufe0f", "Predictive Maintenance", "AI algorithms predict equipment failures before they occur, reducing downtime and maintenance costs.", "/lighting-control-service-sydney"),
            ("\U0001f3e2", "Commercial AI Solutions", "AI-driven optimisation for commercial buildings, retail centres and corporate offices across Sydney.", "/commercial-lighting-control"),
            ("\U0001f3e0", "Residential AI Systems", "Smart home AI systems that learn your family patterns and automatically optimise lighting comfort and efficiency.", "/residential-lighting-control"),
        ],
        [
            ("\U0001f916", "AI-powered optimisation"),
            ("\U0001f4b0", "15-25% additional energy savings"),
            ("\U0001f4ca", "Real-time analytics dashboard"),
            ("\U0001f331", "Weather-adaptive automation"),
            ("\U0001f6e1\ufe0f", "Predictive maintenance alerts"),
            ("\u23f0", "Self-adjusting over time"),
            ("\U0001f3e0", "Works with existing C-Bus/Dynalite"),
            ("\u2705", "Proven energy reduction results"),
            ("\U0001f4f1", "Remote monitoring included"),
            ("\U0001f3af", "Fixed-price AI integration"),
            ("\U0001f527", "Minimal hardware changes needed"),
            ("\U0001f6e0\ufe0f", "Accredited installation"),
        ],
        "AI-Driven Lighting Across Sydney",
        "Machine learning powered energy management for C-Bus and Dynalite systems. Additional 15-25% savings above standard automation.",
        [
            ("/commercial-lighting-control", "\U0001f3e2", "Commercial Lighting"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("How does AI improve lighting energy management?", "AI analyses occupancy patterns, weather data and usage behaviours to automatically optimise lighting schedules and levels. It learns from your building patterns and continuously improves efficiency."),
        ("Does AI-driven lighting work with existing C-Bus systems?", "Yes. Our AI optimisation platform integrates with existing C-Bus and Dynalite systems via API and BACnet gateways. No need to replace your current lighting control infrastructure."),
        ("How much additional energy can AI save?", "Our AI-driven systems typically deliver 15-25% additional energy savings on top of standard C-Bus or Dynalite automation savings of 40-60%."),
        ("Is AI lighting control suitable for residential homes?", "Absolutely. AI-driven residential systems learn your family patterns and automatically adjust lighting for comfort and efficiency throughout the day."),
        ("What data does the AI system collect?", "The system collects occupancy data, energy consumption, time-of-day patterns and environmental sensor data. All data is stored securely and used only for system optimisation."),
    ],
    "seo": [
        ("/ai-driven-smart-lighting-energy-management-sydney", "AI Smart Lighting Sydney"),
        ("/commercial-lighting-control", "Commercial Lighting Sydney"),
        ("/residential-lighting-control", "Residential Lighting Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/lighting-control-service-sydney", "Lighting Control Service"),
    ],
})

# ---- PAGE 23: Atmospheric Lighting for Sydney CBD Retailers ----
pages.append({
    "filename": "atmospheric-lighting-automation-sydney-cbd-retailers.html",
    "title": "Atmospheric Lighting for Sydney CBD Retailers | C-Bus & Dynalite",
    "meta": "Atmospheric lighting for Sydney CBD retailers. C-Bus and Dynalite retail lighting control. Create ambience, drive sales. CBD specialist. Call 0422 469 739.",
    "h1": '<h1>Atmospheric Lighting<br/><span class="accent">for Sydney CBD Retailers</span></h1>',
    "lead": '<p class="lead">Transform your Sydney CBD retail space with C-Bus and Dynalite atmospheric lighting control. Dynamic scenes, accent displays, energy efficiency. Accredited specialists with CBD retail experience. Based in Menai.</p>',
    "body": make_topic_body(
        "Atmospheric Lighting Sydney CBD Retailers",
        "Create Retail Ambience <span class=\"accent\">That Drives Sales</span>",
        "In Sydney CBD competitive retail environment, atmospheric lighting is your most powerful differentiator. C-Bus and Dynalite dynamic lighting control allows you to create immersive shopping experiences with scenes that transition throughout the day or change seasonally, keeping your store fresh and engaging.",
        "We specialise in atmospheric retail lighting for Sydney CBD retailers. From luxury boutiques in the Strand Arcade to flagship stores on Pitt Street Mall, our systems create dramatic accent lighting, dynamic window displays and inviting in-store ambience that drives customer dwell time and sales.",
        ["Dynamic scene transitions throughout the day",
         "Accent lighting for merchandise and displays",
         "Window display automation with seasonal scenes",
         "Colour temperature tuning for mood setting",
         "Occupancy-responsive zone control",
         "Centralised management for multi-store retailers"],
        "CBD Retail Lighting Specialists",
        "Complete atmospheric retail lighting design and programming for Sydney CBD stores. C-Bus and Dynalite specialists.",
        "CBD Retail Expertise",
        "Years of Sydney CBD retail lighting experience. The Strand Arcade, Pitt Street Mall, QVB, Martin Place and beyond.",
        "Sydney CBD Coverage",
        "Based in Menai, servicing all Sydney CBD retail precincts. Same-day callouts for CBD retailers.",
        [
            ("\U0001f3ec", "Boutique Store Lighting", "Intimate atmospheric scenes for luxury boutiques with accent highlighting and colour temperature tuning.", "/retail-lighting-control"),
            ("\U0001f6cd\ufe0f", "Flagship Store Control", "Multi-zone flagship store automation with dynamic scenes, seasonal updates and centralised management.", "/retail-lighting-control"),
            ("\U0001f5bc\ufe0f", "Window Display Automation", "Automated window displays with scheduled scenes, seasonal themes and remote management for CBD stores.", "/retail-lighting-control"),
            ("\U0001f4ca", "Energy & Compliance", "Energy-efficient atmospheric lighting with occupancy automation and AFSS-compliant emergency integration.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f504", "Seasonal Scene Updates", "Refresh your retail atmosphere with seasonal and promotional lighting scenes. Quick reprogramming for sales events.", "/retail-lighting-control"),
            ("\U0001f50c", "Multi-Site Management", "Manage atmospheric lighting across multiple CBD stores from one central dashboard.", "/lighting-control-maintenance-sydney"),
        ],
        [
            ("\U0001f3a8", "Immersive retail experiences"),
            ("\U0001f4b0", "Increase sales with better lighting"),
            ("\u2705", "AFSS compliance included"),
            ("\U0001f3ec", "CBD retail expertise"),
            ("\U0001f31f", "Dynamic seasonal scenes"),
            ("\U0001f4ca", "Energy consumption monitoring"),
            ("\u23f0", "Same-day CBD callouts"),
            ("\U0001f3af", "Fixed-price retail packages"),
            ("\U0001f4f1", "Remote management via app"),
            ("\U0001f3e2", "Multi-store centralised control"),
            ("\U0001f331", "Daylight harvesting integration"),
            ("\U0001f512", "Secure, encrypted operation"),
        ],
        "Atmospheric Retail Lighting for CBD",
        "C-Bus and Dynalite atmospheric lighting for Sydney CBD retailers. Dynamic scenes, accent control, sales-driven design.",
        [
            ("/retail-lighting-control", "\U0001f3ec", "Retail Lighting"),
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-lighting-upgrades-sydney", "\U0001f3ed", "Building Upgrades"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is atmospheric retail lighting?", "Atmospheric retail lighting uses C-Bus or Dynalite to create dynamic, mood-driven lighting scenes that enhance the shopping experience. It includes accent lighting, colour tuning and seasonal scene changes."),
        ("Can atmospheric lighting increase retail sales?", "Yes. Studies show that well-designed atmospheric lighting can increase customer dwell time by 30% and sales by up to 30%. Sydney CBD retailers report significant benefits from professional lighting design."),
        ("How much does retail atmospheric lighting cost?", "A single CBD store atmospheric lighting system typically ranges from $4,000 to $12,000 for programming and commissioning depending on store size and complexity."),
        ("Do you service Sydney CBD retail stores?", "Yes. We have extensive experience in Sydney CBD retail. The Strand Arcade, Pitt Street Mall, QVB, Martin Place, MidCity and all major CBD retail destinations."),
        ("Can retail lighting be updated for seasons?", "Absolutely. C-Bus and Dynalite make it easy to update scenes for seasonal promotions, sales events and new merchandise displays. Quick reprogramming without hardware changes."),
    ],
    "seo": [
        ("/retail-lighting-control", "Retail Lighting Sydney"),
        ("/atmospheric-lighting-automation-sydney-cbd-retailers", "Atmospheric Retail Lighting"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-lighting-upgrades-sydney", "Building Lighting Upgrades"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
    ],
})

# ---- PAGE 24: Blog - Cinema Emergency Lighting Dark Sydney ----
pages.append({
    "filename": "blog-cinema-emergency-lighting-dark-sydney.html",
    "title": "Cinema Emergency Lighting in Dark Sydney | Blog | Sydney Automation Co.",
    "meta": "Blog: Cinema emergency lighting in dark Sydney. Why cinemas need AS/NZS 2293 compliant emergency lighting. Behind the scenes with C-Bus systems.",
    "h1": '<h1>Blog: Cinema Emergency Lighting<br/><span class="accent">in Dark Sydney</span></h1>',
    "lead": '<p class="lead">Ever wonder how cinema emergency lighting works when the lights go down? This blog post explores the critical role of AS/NZS 2293 compliant emergency lighting in Sydney cinemas and theatre environments.</p>',
    "body": make_topic_body(
        "Cinema Emergency Lighting Dark Sydney",
        "The Hidden Safety System <span class=\"accent\">Behind Every Screening</span>",
        "When you settle into your seat at a Sydney cinema and the lights dim for the feature presentation, a sophisticated emergency lighting system is quietly standing guard. Cinema environments present unique challenges for emergency lighting compliance the space must be dark enough for projection but bright enough for safe egress in an emergency.",
        "In this blog post, we explore how C-Bus lighting control systems manage emergency lighting in Sydney cinemas and theatres. From the technical requirements of AS/NZS 2293 to the real-world challenges of balancing darkness with safety, we lift the lid on the hidden infrastructure that keeps moviegoers safe.",
        ["AS/NZS 2293 compliant emergency egress lighting",
         "C-Bus controlled transition from dark to emergency",
         "Battery-backed emergency luminaires and exit signs",
         "Monthly and 6-monthly automated testing routines",
         "Integration with cinema projection and dimming systems",
         "AFSS documentation and logbook management"],
        "Emergency Lighting Blog",
        "Expert insights on cinema emergency lighting compliance in Sydney. Behind the scenes of AS/NZS 2293 implementation.",
        "10+ Years Cinema Experience",
        "Years of emergency lighting work in Sydney entertainment venues including cinemas, theatres and performance spaces.",
        "Sydney Cinema Coverage",
        "Based in Menai, servicing cinemas and theatres across Greater Sydney including CBD, suburbs and regional centres.",
        [
            ("\U0001f3ac", "Cinema Emergency Systems", "Complete emergency lighting design for cinema environments. Dark-mode compliant egress paths and exit signage.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f39f\ufe0f", "Theatre & Stage Lighting", "Emergency lighting integration with theatrical dimming systems for live performance venues.", "/hospitality-lighting-control"),
            ("\u26a1", "AS/NZS 2293 Compliance", "Full emergency lighting compliance for entertainment venues. Automated testing and logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f50d", "AFSS Documentation", "Annual Fire Safety Statement documentation and emergency lighting certification for Sydney venues.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f527", "Maintenance & Testing", "Regular emergency lighting maintenance and testing for cinemas and theatres.", "/lighting-control-maintenance-sydney"),
            ("\U0001f3e2", "Venue Lighting Blog", "More blog posts about lighting in Sydney entertainment venues and commercial spaces.", "/blog-cinema-emergency-lighting-dark-sydney"),
        ],
        [
            ("\U0001f3ac", "Cinema-specific expertise"),
            ("\u2705", "AS/NZS 2293 compliance"),
            ("\U0001f50d", "Automated testing included"),
            ("\U0001f4a1", "Dark-mode egress solutions"),
            ("\U0001f4ca", "Comprehensive documentation"),
            ("\u23f0", "Same-day service available"),
            ("\U0001f3af", "Fixed-price compliance packages"),
            ("\U0001f6e0\ufe0f", "Accredited C-Bus technicians"),
            ("\U0001f4f1", "Remote monitoring optional"),
            ("\U0001f527", "Ongoing support contracts"),
            ("\U0001f3e2", "Sydney-wide coverage"),
            ("\U0001f512", "Secure system integration"),
        ],
        "Cinema Emergency Lighting in Sydney",
        "AS/NZS 2293 compliant emergency lighting for cinemas and theatres. Automated testing, dark-mode egress, full AFSS documentation.",
        [
            ("/emergency-lighting-compliance-afss-sydney", "\u26a1", "AFSS Compliance"),
            ("/emergency-lighting-hotels-hospitality-sydney", "\U0001f3e8", "Hospitality Emergency"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Lighting Maintenance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/lighting-control-repair-sydney", "\U0001f527", "Lighting Repair"),
        ]
    ),
    "faq": [
        ("How does emergency lighting work in a dark cinema?", "Cinema emergency lighting uses specially designed egress luminaires that provide sufficient illumination for safe evacuation without disrupting the screening experience. C-Bus systems can transition from dark mode to emergency mode instantly."),
        ("What are the emergency lighting requirements for Sydney cinemas?", "Sydney cinemas must comply with AS/NZS 2293 for emergency egress lighting and exit signage, with monthly and 6-monthly testing, logbook management and AFSS documentation."),
        ("Can cinema dimming systems integrate with emergency lighting?", "Yes. C-Bus lighting control can integrate cinema dimming with emergency lighting systems, ensuring compliant egress paths while maintaining projection-quality darkness during screenings."),
        ("How often should cinema emergency lighting be tested?", "AS/NZS 2293 requires monthly functional testing (30 seconds) and 6-monthly full discharge testing (90 minutes) with all results recorded in the emergency lighting logbook."),
        ("Do you service cinemas across Sydney?", "Yes. We service all Sydney cinemas including CBD multiplexes, suburban cinemas, boutique theatres and drive-in venues."),
    ],
    "seo": [
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/emergency-lighting-hotels-hospitality-sydney", "Hospitality Emergency Lighting"),
        ("/lighting-control-maintenance-sydney", "Lighting Control Maintenance"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/lighting-control-repair-sydney", "Lighting Control Repair"),
        ("/blog-cinema-emergency-lighting-dark-sydney", "Cinema Emergency Lighting Blog"),
        ("/hospitality-lighting-control", "Hospitality Lighting"),
    ],
})

# ---- PAGE 25: Smart Home ROI Calculator Sydney ----
pages.append({
    "filename": "smart-home-roi-calculator-sydney.html",
    "title": "Smart Home ROI Calculator Sydney | Home Automation Value Tool",
    "meta": "Smart home ROI calculator Sydney. Estimate the value C-Bus and Dynalite automation adds to your property. Quick tool, instant results. Call 0422 469 739.",
    "h1": '<h1>Smart Home ROI Calculator<br/><span class="accent">Sydney Property Tool</span></h1>',
    "lead": '<p class="lead">Quickly estimate the return on investment for C-Bus and Dynalite home automation in your Sydney property. This simple tool helps you understand the value of smart home automation. Based in Menai.</p>',
    "body": make_topic_body(
        "Smart Home ROI Calculator Sydney",
        "Calculate Your Home Automation <span class=\"accent\">Return on Investment</span>",
        "Wondering if C-Bus or Dynalite home automation is worth the investment for your Sydney property? Our ROI calculator gives you a quick estimate based on your property type, location and the scope of automation you are considering.",
        "While this tool provides an indicative estimate based on Sydney market data, we recommend contacting us for a detailed ROI analysis tailored to your specific property. Our accredited specialists can provide precise projections based on your home layout, chosen system and energy usage patterns.",
        ["Property value uplift of 3-8%",
         "Energy savings of 40-60% annually",
         "ROI typically within 2-3 years",
         "Increased buyer appeal and faster sale",
         "Reduced ongoing energy costs",
         "Premium suburb premium returns"],
        "ROI Calculator Tool",
        "Quick ROI estimation tool for Sydney home automation. Property value uplift and energy savings projections.",
        "Market Data Analysis",
        "Based on Sydney property market data and energy savings projections from real C-Bus and Dynalite installations.",
        "Sydney Property Coverage",
        "Data applicable to all Sydney property markets from Eastern Suburbs to Western Sydney.",
        [
            ("\U0001f4b0", "Value Uplift Estimate", "Estimate the property value increase from C-Bus or Dynalite automation based on your property type and location.", "/smart-home-roi-calculator-property-value-sydney"),
            ("\U0001f3e0", "Property Type Analysis", "How automation ROI varies by property type: houses, apartments, townhouses and luxury estates.", "/smart-home-roi-calculator-property-value-sydney"),
            ("\u26a1", "Energy Savings Projection", "Estimate your monthly and annual energy savings with C-Bus or Dynalite automation.", "/sydney-home-automation-cost-guide-2026"),
            ("\U0001f4ca", "Suburb Comparison", "See how ROI varies across Sydney suburbs. Eastern Suburbs and North Shore show highest value uplift.", "/smart-home-roi-calculator-property-value-sydney"),
            ("\U0001f3af", "Cost vs Value Analysis", "Compare automation system costs against projected property value increase and energy savings.", "/sydney-home-automation-cost-guide-2026"),
            ("\U0001f4f1", "Feature Value Ranking", "Which automation features add the most property value? Apple HomeKit, voice control, scenes ranked.", "/c-bus-apple-homekit-sydney"),
        ],
        [
            ("\U0001f4b0", "Quick ROI estimate"),
            ("\U0001f3e0", "Property value projection"),
            ("\u26a1", "Energy savings calculation"),
            ("\U0001f4ca", "Suburb-specific data"),
            ("\U0001f4f1", "Based on real market data"),
            ("\u23f0", "Instant results"),
            ("\U0001f3af", "Compare automation levels"),
            ("\U0001f5c2\ufe0f", "Free detailed analysis available"),
            ("\U0001f331", "Sustainability value included"),
            ("\U0001f4b5", "ROI timeline projection"),
            ("\U0001f6e0\ufe0f", "Accredited advice"),
            ("\U0001f3e2", "Sydney market expertise"),
        ],
        "Smart Home ROI Calculator Sydney",
        "Quick ROI estimation for C-Bus and Dynalite home automation. Property value, energy savings, market data.",
        [
            ("/smart-home-roi-calculator-property-value-sydney", "\U0001f4b0", "ROI Property Value"),
            ("/sydney-home-automation-cost-guide-2026", "\U0001f4b5", "Cost Guide 2026"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/c-bus-apple-homekit-sydney", "\U0001f31f", "C-Bus + Apple HomeKit"),
            ("/residential-lighting-control", "\U0001f3e0", "Residential Lighting"),
            ("/cbus-upgrade-sydney", "\u26a1", "C-Bus Upgrades"),
        ]
    ),
    "faq": [
        ("How does the ROI calculator work?", "The calculator uses Sydney property market data and energy savings projections to estimate the return on investment for C-Bus or Dynalite home automation."),
        ("Is the ROI calculator accurate?", "The calculator provides an indicative estimate based on market averages. For a precise analysis tailored to your property, contact us on 0422 469 739."),
        ("What factors affect home automation ROI?", "Key factors: property type and location, scope of automation, energy usage patterns, current property value and planned ownership duration."),
        ("What is the typical ROI for home automation in Sydney?", "Most Sydney homeowners see full ROI within 2-3 years through energy savings and property value increase combined."),
        ("Do you provide detailed ROI analysis?", "Yes. Contact us for a comprehensive ROI analysis tailored to your specific property, budget and automation goals."),
    ],
    "seo": [
        ("/smart-home-roi-calculator-property-value-sydney", "ROI Property Value Sydney"),
        ("/sydney-home-automation-cost-guide-2026", "Home Automation Cost Guide"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/c-bus-apple-homekit-sydney", "C-Bus + Apple HomeKit"),
        ("/residential-lighting-control", "Residential Lighting Sydney"),
        ("/cbus-upgrade-sydney", "C-Bus Upgrades Sydney"),
        ("/smart-home-roi-calculator-sydney", "ROI Calculator Sydney"),
    ],
})

# ---- PAGE 26: DALI-2 Lighting Control Commercial Buildings ----
pages.append({
    "filename": "dali-2-lighting-control-commercial-buildings.html",
    "title": "DALI-2 Lighting Control Commercial Buildings Sydney | Compliance System",
    "meta": "DALI-2 lighting control for commercial buildings Sydney. Certified systems for offices, retail, commercial. NCC 2025, energy savings. Call 0422 469 739.",
    "h1": '<h1>DALI-2 Lighting Control<br/><span class="accent">Commercial Buildings Sydney</span></h1>',
    "lead": '<p class="lead">DALI-2 lighting control for Sydney commercial buildings. Certified systems for offices, retail centres and commercial premises. NCC 2025 compliant, energy efficient, BMS integrated. Accredited specialists based in Menai.</p>',
    "body": make_topic_body(
        "DALI-2 Lighting Control Commercial Buildings Sydney",
        "DALI-2 for Sydney <span class=\"accent\">Commercial Buildings</span>",
        "Commercial buildings across Sydney are adopting DALI-2 lighting control for its interoperability, precise control and compliance benefits. The DALI-2 standard (IEC 62386) ensures devices from different manufacturers work together seamlessly, giving building owners flexibility and future-proofing.",
        "We implement DALI-2 systems in Sydney commercial offices, retail centres and commercial premises. Our systems provide individual luminaire control, energy monitoring, emergency lighting integration and BMS connectivity, all meeting NCC 2025 energy efficiency requirements.",
        ["Interoperable DALI-2 certified devices",
         "Individual luminaire addressing and control",
         "NCC 2025 energy efficiency compliance",
         "AS/NZS 2293 emergency lighting",
         "BMS integration via BACnet or Modbus",
         "Energy monitoring per luminaire"],
        "DALI-2 Commercial Systems",
        "Complete DALI-2 implementation for commercial buildings. Certified design, programming and commissioning.",
        "DALI-2 Commercial Expertise",
        "Experience with DALI-2 in Sydney offices, retail and commercial buildings. Certified system designers.",
        "Sydney Commercial Coverage",
        "Based in Menai, servicing commercial buildings across all Sydney business districts and commercial zones.",
        [
            ("\U0001f3e2", "Office DALI-2 Systems", "Individual zone and luminaire control for office environments. Scene setting, daylight harvesting and BMS integration.", "/dali-2-lighting-control-commercial-buildings"),
            ("\U0001f3ec", "Retail DALI-2 Systems", "Accent and general lighting control for retail spaces with DALI-2 certified track and downlight solutions.", "/dali-2-lighting-control-commercial-buildings"),
            ("\u26a1", "NCC 2025 Compliance", "DALI-2 systems designed to meet NCC 2025 Section J energy efficiency requirements.", "/dali-2-lighting-control-implementation-compliance"),
            ("\U0001f50d", "Emergency Lighting", "DALI-2 emergency testing and compliance per AS/NZS 2293 with automated logbook management.", "/emergency-lighting-compliance-afss-sydney"),
            ("\U0001f4ca", "Energy Monitoring", "Per-luminaire and per-zone energy consumption data for compliance reporting and cost optimisation.", "/lighting-control-maintenance-sydney"),
            ("\U0001f50c", "BMS Integration", "Seamless integration with building management systems via DALI-2 BACnet gateway.", "/building-automation-maintenance-sydney"),
        ],
        [
            ("\u2705", "DALI-2 certified compliance"),
            ("\U0001f4b0", "Energy efficient operation"),
            ("\U0001f3e2", "NCC 2025 ready"),
            ("\U0001f50c", "BMS integration standard"),
            ("\U0001f4a1", "Individual luminaire control"),
            ("\u23f0", "Same-day callouts available"),
            ("\U0001f4ca", "Granular energy data"),
            ("\U0001f6e0\ufe0f", "Certified technicians"),
            ("\U0001f3af", "Fixed-price DALI-2 systems"),
            ("\U0001f527", "Ongoing support"),
            ("\U0001f331", "Future-proof technology"),
            ("\U0001f512", "Interoperable devices"),
        ],
        "DALI-2 for Commercial Buildings",
        "Certified DALI-2 lighting control for Sydney commercial buildings. NCC 2025 compliance, energy savings, BMS integration.",
        [
            ("/dali-2-lighting-control-implementation-compliance", "\u26a1", "DALI-2 Compliance"),
            ("/emergency-lighting-compliance-afss-sydney", "\U0001f50d", "AFSS Compliance"),
            ("/c-bus-programmer-sydney", "\u2699\ufe0f", "C-Bus Programming"),
            ("/dynalite-programmer-sydney", "\U0001f4bb", "Dynalite Programming"),
            ("/building-automation-maintenance-sydney", "\U0001f3e2", "Building Automation"),
            ("/lighting-control-maintenance-sydney", "\U0001f6e1\ufe0f", "Maintenance"),
        ]
    ),
    "faq": [
        ("What is DALI-2 for commercial buildings?", "DALI-2 is an international standard (IEC 62386) for digital lighting control in commercial buildings, offering interoperability between manufacturers and precise individual luminaire control."),
        ("Is DALI-2 better than C-Bus for commercial buildings?", "Both have strengths. DALI-2 excels in interoperability and individual luminaire control. C-Bus offers broader system integration. Many commercial buildings use both for different applications."),
        ("Does DALI-2 meet NCC 2025 requirements?", "Yes. DALI-2 is the most effective way to achieve NCC 2025 energy efficiency compliance for commercial building lighting control."),
        ("Can DALI-2 integrate with my BMS?", "Yes. DALI-2 integrates with BMS platforms via BACnet and Modbus gateways for centralised building management."),
        ("What commercial buildings use DALI-2 in Sydney?", "Sydney offices, retail centres, hospitals, educational facilities and government buildings increasingly specify DALI-2 for compliance and flexibility."),
    ],
    "seo": [
        ("/dali-2-lighting-control-implementation-compliance", "DALI-2 Implementation & Compliance"),
        ("/dali-2-lighting-control-commercial-buildings", "DALI-2 Commercial Buildings"),
        ("/emergency-lighting-compliance-afss-sydney", "AFSS Compliance Sydney"),
        ("/c-bus-programmer-sydney", "C-Bus Programming Sydney"),
        ("/dynalite-programmer-sydney", "Dynalite Programming Sydney"),
        ("/building-automation-maintenance-sydney", "Building Automation Sydney"),
        ("/lighting-control-maintenance-sydney", "Lighting Maintenance"),
        ("/dali-lighting-repair", "DALI Lighting Repair"),
    ],
})
# ---- MAIN ----
print("Generating 16 pages...")
for p in pages:
    make_page(p)
print("Done! All 16 pages generated.")

