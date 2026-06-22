"""
generate_phase3_pages.py
Generates ~350+ new pages targeting:
  - Gyms & Fitness Centres
  - Aged Care & Healthcare Facilities
  - Universities & TAFEs
  - Hotels & Serviced Apartments
  - Childcare Centres
  - Government Buildings & Councils
  - Data Centres & IT Facilities
  - Industrial & Warehouse
  - Car Dealerships
  - Sporting Venues & Stadiums

Cross-multiplied against 15 key Sydney hubs x 3 systems x 4 faults
= ~1,800 new pages

Plus hub landing pages for each vertical = 10 pages
Total: ~1,810 pages
"""

import os

BASE_DIR = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'

VERTICALS = [
    ("gyms-and-fitness-centres", "Gyms and Fitness Centres", "gym", [
        "Members depend on reliable lighting 24/7. A C-Bus fault at 5am means shutting the gym floor — costing you memberships.",
        "Fitness centres require precise lighting zones — spin studios, weight floors, reception, and changerooms each need independent control.",
        "We've repaired C-Bus and Dynalite faults in fitness facilities across Sydney, restoring full zonal control with minimal disruption.",
        "Our SLA-backed response means your gym reopens fast. We carry common replacement modules on every service van."
    ]),
    ("aged-care-and-healthcare-facilities", "Aged Care and Healthcare Facilities", "aged care", [
        "Aged care facilities face strict fire and emergency lighting compliance under AS 2293. Faults cannot wait.",
        "Residents' safety depends on reliable lighting automation — night lighting, emergency paths, and nurse call integration must all function perfectly.",
        "We hold all required accreditations to service healthcare environments and provide full compliance documentation after every visit.",
        "Our technicians understand the sensitivity of aged care environments — we work quietly, safely, and respect residents at all times."
    ]),
    ("universities-and-tafes", "Universities and TAFEs", "university", [
        "Lecture theatres, labs, libraries, and open learning spaces all require independent lighting zones — a C-Bus fault disrupts hundreds of students.",
        "TAFE and university campuses span multiple buildings, often on ageing C-Bus infrastructure that needs specialist knowledge to diagnose remotely.",
        "We provide SLA-backed automation support for educational institutions, with after-hours scheduling to avoid disrupting classes.",
        "From lecture theatre scene programming to emergency lighting compliance, we handle the full scope of university automation needs."
    ]),
    ("hotels-and-serviced-apartments", "Hotels and Serviced Apartments", "hotel", [
        "Guest experience depends on perfect lighting automation — room scenes, corridors, lobbies, and conference rooms must all work flawlessly.",
        "A C-Bus or Dynalite fault in a hotel costs more than repair time — it costs you TripAdvisor reviews and repeat bookings.",
        "We provide discreet, after-hours repair services for hotels, ensuring zero guest disturbance while restoring full system functionality.",
        "Our team handles everything from guestroom lighting scenes to ballroom DALI systems and AFSS emergency compliance."
    ]),
    ("childcare-centres", "Childcare Centres", "childcare", [
        "Childcare facilities require safe, reliable lighting — emergency path lighting, sleep room dimming, and outdoor area control are all critical.",
        "Under AS 2293, childcare emergency lighting must pass annual AFSS testing. Non-compliance risks your licence.",
        "We provide fast, safe service in childcare environments — fully insured, working respectfully around children and staff.",
        "Our repairs cover C-Bus sleep room scene programming, outdoor sensor integration, and emergency lighting compliance documentation."
    ]),
    ("government-buildings-and-councils", "Government Buildings and Councils", "council", [
        "Government facilities require strict compliance documentation, certified technicians, and procurement-friendly invoicing — we deliver all three.",
        "Council chambers, libraries, depots, and community centres all depend on reliable lighting control. We service the full scope.",
        "We hold active accreditations and public liability insurance required to work in government-managed buildings across Greater Sydney.",
        "Our reporting documentation satisfies council procurement and compliance requirements, making audits simple."
    ]),
    ("data-centres-and-it-facilities", "Data Centres and IT Facilities", "data centre", [
        "Data centres require precise environmental control — lighting faults can trigger safety shutdowns that cost thousands per minute in downtime.",
        "We have experience working in live data centre environments, following strict change management and safety protocols.",
        "C-Bus and Dynalite faults in data halls, comms rooms, and UPS bays require specialist diagnosis — not a generic sparky.",
        "Our technicians are inducted and familiar with data centre access procedures, ensuring compliance with your security requirements."
    ]),
    ("industrial-and-warehouse-facilities", "Industrial and Warehouse Facilities", "industrial", [
        "Warehouses and factories rely on motion-sensor-driven lighting to cut energy costs. A sensor or C-Bus fault kills those savings immediately.",
        "Industrial lighting automation — from high-bay PIR integration to emergency egress lighting — is our speciality.",
        "We service C-Bus and DALI systems in industrial environments, including high-voltage switchboard areas and dust-heavy spaces.",
        "Our emergency lighting compliance services cover AS 2293 annual testing for warehouses, factories, and logistics facilities."
    ]),
    ("car-dealerships", "Car Dealerships", "dealership", [
        "Showroom lighting is your silent salesperson — flicker, wrong colour temperature, or a failed scene ruins the premium feel and costs you sales.",
        "Car dealerships require precise C-Bus scene control across showrooms, service bays, offices, and forecourts. We programme and repair all of it.",
        "Dealership service bays must comply with emergency lighting standards — we provide full AFSS compliance documentation.",
        "We've worked with major Sydney car dealerships to optimise C-Bus and Dynalite systems for maximum ambience and energy efficiency."
    ]),
    ("sporting-venues-and-stadiums", "Sporting Venues and Stadiums", "sports venue", [
        "Sporting venues require broadcast-quality lighting control, emergency evacuation systems, and crowd-safe scene management — all automated.",
        "A lighting fault during an event is a liability. We offer priority response SLAs for sporting venues and community facilities.",
        "We service C-Bus, DALI, and Dynalite systems in sporting venues — from community rugby clubs to multi-court indoor arenas.",
        "Emergency egress lighting in grandstands and indoor venues must comply with AS 2293. We provide full testing and AFSS certification."
    ]),
]

SUBURBS = [
    "Parramatta", "Chatswood", "North Sydney", "Bondi Junction", "Liverpool",
    "Penrith", "Blacktown", "Hurstville", "Manly", "Newtown",
    "Mascot", "Macquarie Park", "Castle Hill", "Campbelltown", "Hornsby",
    "Epping", "Strathfield", "Rhodes", "Olympic Park", "Norwest"
]

SYSTEMS = [
    ("c-bus", "C-Bus"),
    ("dynalite", "Dynalite"),
    ("dali-2", "DALI-2"),
]

FAULTS = [
    ("afss-emergency-lighting-compliance", "AFSS Emergency Lighting Non-Compliance"),
    ("automated-schedule-and-timeclock-drift", "Automated Schedule and Timeclock Drift"),
    ("daylight-harvesting-and-sensor-failure", "Daylight Harvesting and Sensor Failure"),
    ("network-communication-and-bus-crashes", "Network Communication and Bus Crashes"),
]

NAV_HTML = '''
<nav style="background:#001226;padding:10px 0;text-align:center;border-bottom:1px solid rgba(255,255,255,0.08);position:sticky;top:44px;z-index:9000;">
  <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:center;gap:24px;flex-wrap:wrap;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:14px;">
    <a href="/" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">🏠 Home</a>
    <a href="/automation-sydney" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">⚡ Automation</a>
    <a href="/afss-emergency-lighting-services" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">🚨 Emergency Lighting</a>
    <a href="/blog" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">📝 Blog</a>
    <a href="/about" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">👤 About</a>
    <a href="/book-service" style="background:#f07020;color:#fff;text-decoration:none;padding:6px 16px;border-radius:4px;font-weight:700;" onmouseover="this.style.background='#d06010'" onmouseout="this.style.background='#f07020'">📅 Book Service</a>
    <a href="tel:0422469739" style="color:#4da6ff;text-decoration:none;padding:6px 10px;border-radius:4px;font-weight:600;">📞 0422 469 739</a>
  </div>
</nav>
'''

SITEMAP_ENTRIES = []

def make_slug(*parts):
    return '-'.join(p.lower().replace(' ', '-').replace('&', 'and').replace(',', '').replace("'", '') for p in parts)

def build_page(vertical_slug, vertical_name, vertical_desc, suburb, system_slug, system_name, fault_slug, fault_name, facts):
    slug = f"{vertical_slug}-{make_slug(suburb)}-{system_slug}-{fault_slug}"
    filename = slug + ".html"
    canonical = f"https://sydneyautomationco.com.au/{slug}"
    
    title = f"{system_name} {fault_name} Repair for {vertical_name} in {suburb} | Sydney Automation Co."
    meta_desc = (
        f"Expert {system_name} fault diagnosis and repair for {vertical_name} experiencing {fault_name} in {suburb}. "
        f"SLA-backed commercial automation services. Call 0422 469 739."
    )

    facts_html = ''.join(f'<li style="margin-bottom:12px;color:#a8c0e0;">{f}</li>' for f in facts)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical}">
    <link rel="stylesheet" href="/style.css">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Sydney Automation Co.",
      "description": "{meta_desc}",
      "url": "{canonical}",
      "telephone": "+61422469739",
      "areaServed": {{
        "@type": "Place",
        "name": "{suburb}",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{suburb}",
          "addressRegion": "NSW",
          "addressCountry": "AU"
        }}
      }},
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "Commercial Automation Services for {vertical_name}",
        "itemListElement": [
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "{system_name} {fault_name} for {vertical_name} in {suburb}"}}}}
        ]
      }}
    }}
    </script>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "How quickly can you fix {fault_name} for {vertical_name} in {suburb}?",
          "acceptedAnswer": {{"@type": "Answer", "text": "We offer priority SLA-backed response for commercial facilities in {suburb}. Our technicians arrive fully equipped to diagnose and resolve {system_name} faults on the first visit wherever possible."}}
        }},
        {{
          "@type": "Question",
          "name": "Are your {system_name} services compliant for {vertical_name}?",
          "acceptedAnswer": {{"@type": "Answer", "text": "Yes. We hold all required accreditations and insurances for servicing {vertical_name}, providing complete compliance documentation and tax invoices after every job."}}
        }},
        {{
          "@type": "Question",
          "name": "Do you work after-hours for {vertical_name} in {suburb}?",
          "acceptedAnswer": {{"@type": "Answer", "text": "Yes. We understand that {vertical_name} often cannot afford downtime during operating hours. We offer flexible scheduling including early mornings, evenings, and weekends in {suburb}."}}
        }}
      ]
    }}
    </script>

    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #0a1628; color: #a8c0e0; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        header {{ background-color: #001f3d; color: #fff; padding: 1rem 0; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2.5em; }}
        .hero {{ background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url('/images/hero-bg.jpg') no-repeat center center/cover; color: #fff; padding: 100px 0; text-align: center; }}
        .hero h2 {{ font-size: 2.4em; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.15em; margin-bottom: 30px; max-width: 800px; margin-left: auto; margin-right: auto; }}
        .cta-button {{ background-color: #f07020; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }}
        .section {{ padding: 60px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        .section h3 {{ color: #fff; font-size: 1.8em; margin-bottom: 20px; }}
        .section p {{ font-size: 1.05em; margin-bottom: 16px; }}
        .faq-item {{ background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); padding: 24px; margin-bottom: 16px; border-radius: 8px; }}
        .faq-item h4 {{ color: #fff; margin-top: 0; font-size: 1.1em; }}
        .faq-item p {{ margin: 0; }}
        .alert-bar {{ background: rgba(240,112,32,0.15); border-left: 4px solid #f07020; padding: 20px; margin: 30px 0; border-radius: 4px; }}
        .cta-block {{ background: linear-gradient(135deg, rgba(240,112,32,0.1) 0%, rgba(77,166,255,0.05) 100%); border: 2px solid #f07020; border-radius: 12px; padding: 30px; margin: 40px 0; text-align: center; }}
        .cta-block h3 {{ color: #fff; margin-top: 0; }}
        .cta-block .cta-button {{ display: inline-block; font-size: 16px; padding: 15px 40px; border-radius: 8px; }}
        .trust-points {{ color: #4da6ff; font-size: 13px; margin-top: 15px; }}
        .facts-list {{ padding-left: 20px; }}
        footer {{ background-color: #001f3d; color: #a8c0e0; text-align: center; padding: 20px 0; margin-top: 40px; }}
    </style>
</head>
<body>
  <div id="sticky-cta-bar" style="position:fixed;top:0;left:0;right:0;z-index:99999;background:linear-gradient(90deg,#0a2240 0%,#1a3a6e 100%);display:flex;align-items:center;justify-content:center;gap:16px;padding:10px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.4);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
    <span style="color:#f0c040;font-size:13px;font-weight:600;white-space:nowrap;">⚡ Enterprise-Grade Automation Support — Available Today</span>
    <a href="tel:0422469739" style="background:#e8330a;color:#fff;text-decoration:none;padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;white-space:nowrap;" onclick="gtag&&gtag('event','click',{{event_category:'CTA',event_label:'sticky-call'}})">📞 Call George</a>
    <a href="/book-service" style="background:#fff;color:#0a2240;text-decoration:none;padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;white-space:nowrap;border:2px solid #fff;">Book Online →</a>
    <button onclick="document.getElementById('sticky-cta-bar').style.display='none'" style="background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;font-size:18px;line-height:1;margin-left:8px;padding:0;" aria-label="Close">×</button>
  </div>
  <style>body {{ padding-top: 44px !important; }}</style>

    <header>
        <div class="container">
            <h1>Sydney Automation Co.</h1>
            <p>Certified B2B Automation &amp; Lighting Control Specialists</p>
        </div>
    </header>

    {NAV_HTML}

    <main>
        <section class="hero">
            <div class="container">
                <h2>{system_name} {fault_name} for {vertical_name} in {suburb}</h2>
                <p>Specialist B2B automation support for {vertical_name} across {suburb}. We rapidly diagnose and fix {fault_name} so your facility stays compliant, safe, and fully operational.</p>
                <a href="/book-service" class="cta-button">Book Priority Call-Out &#8594;</a>
            </div>
        </section>

        <div class="container">
            <div class="alert-bar">
                <p style="color:#fff;font-weight:700;font-size:16px;">&#9888;&#65039; {system_name} Emergency in {suburb}? Call Now: <span style="color:#f07020;font-size:18px;">0422 469 739</span></p>
                <p style="color:#a8c0e0;margin-top:8px;font-size:14px;">Certified automation technicians. Fast SLA-backed response for {vertical_name} in {suburb}.</p>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <h3>Why {vertical_name} in {suburb} Need Specialist {system_name} Support</h3>
                <p>{vertical_name} in {suburb} face unique challenges when {system_name} systems develop faults like {fault_name}. Generic electricians lack the manufacturer-level diagnostic tools and software access required to restore full network functionality without business disruption.</p>
                <p>Sydney Automation Co. is a certified {system_name} specialist with direct experience servicing {vertical_desc} facilities. We understand the compliance pressures, operational constraints, and SLA expectations that come with your sector.</p>
                <ul class="facts-list">
                    {facts_html}
                </ul>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>What Causes {fault_name} in {system_name} Systems?</h3>
                <p>In {vertical_name} environments, {fault_name} can be triggered by a range of factors — from hardware ageing and firmware conflicts to incorrect programming after a partial renovation. Our diagnostic process covers the full network topology to find root causes fast.</p>
                <p>We use manufacturer-authorised diagnostic software to isolate faults at the unit, zone, and network level — giving you a clear fault report and a repair plan before any work proceeds.</p>

                <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:24px;">
                    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,112,32,0.2);border-radius:8px;padding:20px;">
                        <h4 style="color:#f07020;margin-top:0;">🔍 Fault Diagnosis</h4>
                        <p style="font-size:14px;">Full {system_name} network scan using manufacturer toolkits. Root cause identified before any parts are ordered.</p>
                    </div>
                    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,112,32,0.2);border-radius:8px;padding:20px;">
                        <h4 style="color:#f07020;margin-top:0;">🔧 Repair &amp; Restoration</h4>
                        <p style="font-size:14px;">Module replacement, re-addressing, scene reprogramming — restored to full spec with no data loss.</p>
                    </div>
                    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,112,32,0.2);border-radius:8px;padding:20px;">
                        <h4 style="color:#f07020;margin-top:0;">📋 Compliance Docs</h4>
                        <p style="font-size:14px;">Full compliance report and tax invoice provided. Ready for your facility management records.</p>
                    </div>
                    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(240,112,32,0.2);border-radius:8px;padding:20px;">
                        <h4 style="color:#f07020;margin-top:0;">🕐 Flexible Scheduling</h4>
                        <p style="font-size:14px;">Early morning, evening, and weekend appointments to minimise disruption to {vertical_name} operations in {suburb}.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>Frequently Asked Questions — {vertical_name} in {suburb}</h3>
                <div class="faq-item"><h4>How quickly can you fix {fault_name} for {vertical_name} in {suburb}?</h4><p>We offer priority SLA-backed response for commercial facilities in {suburb}. Our technicians arrive fully equipped to diagnose and resolve {system_name} faults on the first visit wherever possible.</p></div>
                <div class="faq-item"><h4>Are your {system_name} services compliant for {vertical_name}?</h4><p>Yes. We hold all required accreditations and insurances for servicing {vertical_name}, providing complete compliance documentation and tax invoices after every job.</p></div>
                <div class="faq-item"><h4>Do you work after-hours for {vertical_name} in {suburb}?</h4><p>Yes. We understand that {vertical_name} often cannot afford downtime during operating hours. We offer flexible scheduling including early mornings, evenings, and weekends in {suburb}.</p></div>
                <div class="faq-item"><h4>Can you integrate {system_name} with BMS or access control at our {suburb} facility?</h4><p>Absolutely. We have experience integrating {system_name} with building management systems, access control, HVAC, and AV equipment in {vertical_name} environments across {suburb} and Greater Sydney.</p></div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>Transparent Pricing for {vertical_name}</h3>
                <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:20px;">
                    <div style="background:#0e1f3d;padding:24px;border-radius:8px;">
                        <h3 style="margin-bottom:16px;color:#fff;">Commercial Rate Card</h3>
                        <ul style="list-style:none;padding:0;">
                            <li style="margin-bottom:8px;">&#10003; <strong style="color:#f0f4ff;">Consultation &amp; Diagnosis:</strong> $150/hr</li>
                            <li style="margin-bottom:8px;">&#10003; <strong style="color:#f0f4ff;">Programming &amp; Integration:</strong> $150/hr</li>
                            <li style="margin-bottom:8px;">&#10003; <strong style="color:#f0f4ff;">Emergency / AFSS Compliance:</strong> $150/hr + 15% premium</li>
                            <li style="margin-bottom:8px;">&#10003; <strong style="color:#f0f4ff;">Minimum Call-Out:</strong> 3 hours ($450)</li>
                        </ul>
                    </div>
                    <div style="background:#0e1f3d;padding:24px;border-radius:8px;">
                        <h3 style="margin-bottom:16px;color:#fff;">Our Commercial Guarantee</h3>
                        <p style="font-size:15px;line-height:1.7;margin-bottom:16px;color:#a8c0e0;">We arrive with manufacturer diagnostic toolkits and common replacement modules. No work proceeds without site management approval.</p>
                        <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:16px;">
                            <a href="/book-service" class="cta-button" style="padding:10px 20px;">Book $450 Diagnostic Call</a>
                            <a href="tel:0422469739" class="cta-button" style="background:transparent;border:2px solid #f07020;padding:8px 18px;">Call 0422 469 739</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <div class="container">
            <div class="cta-block">
                <h3>Ready to Fix {fault_name} at Your {suburb} {vertical_desc.title()} Facility?</h3>
                <p style="color:#a8c0e0;font-size:16px;margin-bottom:20px;">Don't let {fault_name} disrupt operations or void your compliance certificates.</p>
                <a href="/book-service" class="cta-button">Book B2B Service &amp; Pay Deposit &#8594;</a>
                <p class="trust-points">&#10003; Priority commercial response &nbsp;|&nbsp; &#10003; Certified technicians &nbsp;|&nbsp; &#10003; Tax invoices provided</p>
            </div>
        </div>
    </main>

<footer>
        <div class="container">
            <p>&copy; 2026 Sydney Automation Co. ABN 61 136 364 150. All rights reserved. Servicing {vertical_name} in {suburb}, NSW.</p>
            <p><a href="tel:+61422469739" style="color:#f07020;">0422 469 739</a> &nbsp;|&nbsp; <a href="mailto:george@sydneyautomationco.com.au" style="color:#4da6ff;">george@sydneyautomationco.com.au</a></p>
            <p style="font-size:12px;margin-top:12px;">
                <a href="/" style="color:#a8c0e0;margin-right:12px;">Home</a>
                <a href="/automation-sydney" style="color:#a8c0e0;margin-right:12px;">Automation</a>
                <a href="/afss-emergency-lighting-services" style="color:#a8c0e0;margin-right:12px;">Emergency Lighting</a>
                <a href="/blog" style="color:#a8c0e0;margin-right:12px;">Blog</a>
                <a href="/book-service" style="color:#a8c0e0;">Book Service</a>
            </p>
        </div>
    </footer>
</body>
</html>"""
    return filename, html, canonical


def build_hub_page(vertical_slug, vertical_name, vertical_desc, facts, suburbs, systems):
    """Create a hub landing page for each vertical"""
    filename = f"{vertical_slug}-lighting-automation-sydney.html"
    canonical = f"https://sydneyautomationco.com.au/{vertical_slug}-lighting-automation-sydney"
    title = f"{vertical_name} Lighting Automation & C-Bus Repair Sydney | Sydney Automation Co."
    meta_desc = (
        f"Specialist lighting automation, C-Bus, Dynalite, and DALI-2 repair for {vertical_name} across Sydney. "
        f"SLA-backed B2B service. Call 0422 469 739."
    )

    suburb_links = ' | '.join(
        f'<a href="/{vertical_slug}-{s.lower().replace(" ","-")}-c-bus-afss-emergency-lighting-compliance" style="color:#4da6ff;text-decoration:none;">{s}</a>'
        for s in suburbs[:10]
    )
    system_links = ' | '.join(
        f'<a href="/{vertical_slug}-{suburbs[0].lower().replace(" ","-")}-{sslug}-afss-emergency-lighting-compliance" style="color:#4da6ff;text-decoration:none;">{sname}</a>'
        for sslug, sname in systems
    )
    facts_html = ''.join(f'<li style="margin-bottom:14px;color:#a8c0e0;font-size:1.05em;">{f}</li>' for f in facts)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical}">
    <link rel="stylesheet" href="/style.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Sydney Automation Co.",
      "description": "{meta_desc}",
      "url": "{canonical}",
      "telephone": "+61422469739",
      "areaServed": {{"@type": "Place", "name": "Sydney", "addressRegion": "NSW", "addressCountry": "AU"}}
    }}
    </script>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #0a1628; color: #a8c0e0; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        header {{ background-color: #001f3d; color: #fff; padding: 1rem 0; text-align: center; }}
        .hero {{ background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url('/images/hero-bg.jpg') no-repeat center center/cover; color: #fff; padding: 80px 0; text-align: center; }}
        .hero h2 {{ font-size: 2.4em; margin-bottom: 20px; }}
        .cta-button {{ background-color: #f07020; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }}
        .section {{ padding: 50px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }}
        .section h3 {{ color: #fff; font-size: 1.8em; margin-bottom: 18px; }}
        footer {{ background-color: #001f3d; color: #a8c0e0; text-align: center; padding: 20px 0; margin-top: 40px; }}
    </style>
</head>
<body>
  <div id="sticky-cta-bar" style="position:fixed;top:0;left:0;right:0;z-index:99999;background:linear-gradient(90deg,#0a2240 0%,#1a3a6e 100%);display:flex;align-items:center;justify-content:center;gap:16px;padding:10px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.4);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
    <span style="color:#f0c040;font-size:13px;font-weight:600;white-space:nowrap;">⚡ {vertical_name} Automation Specialists — Sydney-Wide</span>
    <a href="tel:0422469739" style="background:#e8330a;color:#fff;text-decoration:none;padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;">📞 Call George</a>
    <a href="/book-service" style="background:#fff;color:#0a2240;text-decoration:none;padding:7px 18px;border-radius:4px;font-size:13px;font-weight:700;border:2px solid #fff;">Book Online →</a>
    <button onclick="document.getElementById('sticky-cta-bar').style.display='none'" style="background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;font-size:18px;line-height:1;margin-left:8px;padding:0;" aria-label="Close">×</button>
  </div>
  <style>body {{ padding-top: 44px !important; }}</style>
    <header>
        <div class="container">
            <h1>Sydney Automation Co.</h1>
            <p>Certified {vertical_name} Automation Specialists</p>
        </div>
    </header>
    {NAV_HTML}
    <main>
        <section class="hero">
            <div class="container">
                <h2>{vertical_name} Lighting Automation &amp; C-Bus Repair — Sydney</h2>
                <p>Sydney's specialist for {vertical_name} lighting control, C-Bus, Dynalite, and DALI-2 repair. SLA-backed B2B response across all Sydney suburbs.</p>
                <a href="/book-service" class="cta-button">Book a Priority Call-Out &#8594;</a>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h3>Why {vertical_name} Choose Sydney Automation Co.</h3>
                <ul style="padding-left:20px;">{facts_html}</ul>
                <p style="margin-top:24px;">We service all major {system_links} systems and cover {suburb_links} and beyond.</p>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h3>Locations We Service</h3>
                <p style="line-height:2;">{suburb_links}</p>
            </div>
        </section>
        <section class="section">
            <div class="container" style="text-align:center;">
                <h3>Ready to Book?</h3>
                <p style="max-width:600px;margin:0 auto 24px;">Contact us today for a priority diagnostic call-out. Minimum 3-hour call-out ($450). Tax invoices provided.</p>
                <a href="/book-service" class="cta-button" style="margin-right:16px;">Book Online</a>
                <a href="tel:0422469739" class="cta-button" style="background:transparent;border:2px solid #f07020;">Call 0422 469 739</a>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 Sydney Automation Co. ABN 61 136 364 150. All rights reserved.</p>
            <p><a href="/" style="color:#a8c0e0;margin-right:12px;">Home</a>
               <a href="/blog" style="color:#a8c0e0;margin-right:12px;">Blog</a>
               <a href="/book-service" style="color:#a8c0e0;">Book Service</a></p>
        </div>
    </footer>
</body>
</html>"""
    return filename, html, canonical


# ── GENERATE ──────────────────────────────────────────────────────────────────
generated = 0
sitemap_additions = []

for v_slug, v_name, v_desc, v_facts in VERTICALS:
    # Hub page
    hub_filename, hub_html, hub_canonical = build_hub_page(
        v_slug, v_name, v_desc, v_facts, SUBURBS, SYSTEMS
    )
    hub_path = os.path.join(BASE_DIR, hub_filename)
    if not os.path.exists(hub_path):
        with open(hub_path, 'w', encoding='utf-8') as f:
            f.write(hub_html)
        sitemap_additions.append(hub_canonical)
        generated += 1
        print(f"[HUB] {hub_filename}")

    # Detailed pages
    for suburb in SUBURBS:
        for sys_slug, sys_name in SYSTEMS:
            for fault_slug, fault_name in FAULTS:
                filename, html, canonical = build_page(
                    v_slug, v_name, v_desc, suburb,
                    sys_slug, sys_name,
                    fault_slug, fault_name,
                    v_facts
                )
                filepath = os.path.join(BASE_DIR, filename)
                if not os.path.exists(filepath):
                    with open(filepath, 'w', encoding='utf-8') as fh:
                        fh.write(html)
                    sitemap_additions.append(canonical)
                    generated += 1

print(f"\n✅ Generated {generated} new pages")

# Append to sitemap.xml
sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
if os.path.exists(sitemap_path) and sitemap_additions:
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sm = f.read()
    
    new_entries = '\n'.join(
        f'  <url><loc>{c}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>'
        for c in sitemap_additions
    )
    sm = sm.replace('</urlset>', f'\n{new_entries}\n</urlset>')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sm)
    print(f"✅ Added {len(sitemap_additions)} URLs to sitemap.xml")

print(f"\n📊 FINAL STATS:")
import glob as gb
total = len(gb.glob(os.path.join(BASE_DIR, '*.html')))
print(f"   Total HTML pages now: {total}")
