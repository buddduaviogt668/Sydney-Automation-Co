import os
import re
import json

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"
TECH_LIB_DIR = os.path.join(DIR, "tech-library")

if not os.path.exists(TECH_LIB_DIR):
    os.makedirs(TECH_LIB_DIR)

cbus_parts = ['5508RVF', 'L5512RVF', '5504AMP', '5500PC', '5500CN', 'L5508D1A', 'L5508D2A', '5084TXP', '5200WHC2', '5502DAL']
dynalite_parts = ['DDBC1200', 'DMDR12-320', 'DDRC1220', 'DDRC1210', 'DDMC802', 'PDEG', 'DDNG232', 'DDNG485', 'DUS360CS', 'Antumbra']
parts = cbus_parts + dynalite_parts

symptoms = [
    {
        "name": "Blinking LED Codes",
        "desc": "Lost network clock / communications timeout",
        "answer": "A blinking LED indicates a lost network clock or power supply voltage drop. Verify network voltage is above 22V and use toolkit software to re-assign a network clock driver.",
        "steps": [
            "Check the system power supply voltage with a multimeter.",
            "If voltage is below 22V, the power supply module may need replacement.",
            "Connect using the manufacturer toolkit software.",
            "Verify that a network clock is enabled on at least one device.",
            "Re-program if necessary and monitor LED status."
        ]
    },
    {
        "name": "Buzzing or Clicking Noises",
        "desc": "Relay contact degradation / power supply failure",
        "answer": "A buzzing or clicking noise indicates relay contact degradation or an internal power supply failure. This is a hardware fault requiring replacement of the affected module to prevent fire hazards.",
        "steps": [
            "Identify the exact module making the buzzing noise.",
            "Isolate power to the affected lighting circuits immediately.",
            "Check for signs of thermal damage or burning smells.",
            "Do not attempt to repair the internal relay contacts.",
            "Contact a certified specialist to replace the module."
        ]
    },
    {
        "name": "Stuck-On Channels",
        "desc": "Fused load contactors causing lights to stay on 24/7",
        "answer": "Stuck-on channels are typically caused by fused load contactors inside the relay. When inrush currents exceed the relay rating, the contacts weld together, keeping the lights permanently on.",
        "steps": [
            "Attempt to manually toggle the channel override button on the unit.",
            "If the button is physically stuck or does not change the light state, the relay is fused.",
            "Turn off the circuit breaker for the affected lights to save energy.",
            "The internal relays cannot be safely un-welded.",
            "A hardware replacement of the dimmer or relay module is required."
        ]
    },
    {
        "name": "Frozen / Unresponsive Interfaces",
        "desc": "Keypads or touchscreens locked up",
        "answer": "Frozen or unresponsive keypads and touchscreens usually point to a software lockup or a network communication drop. A hard reset of the network or the specific touchscreen is the first step.",
        "steps": [
            "Locate the main lighting control switchboard.",
            "Cycle power to the specific network branch or touchscreen.",
            "Wait 60 seconds for the system to reboot and re-establish network clocks.",
            "If the touchscreen remains frozen, its internal operating system may be corrupt.",
            "A firmware flash or hardware upgrade to a modern interface may be necessary."
        ]
    },
    {
        "name": "Lost Schedules & Clock Drift",
        "desc": "Internal battery backup failure",
        "answer": "If schedules are failing or the time is drifting, the internal RTC (Real Time Clock) battery backup has likely failed. Older modules lose their timekeeping ability when power fluctuates.",
        "steps": [
            "Connect to the system using the programming toolkit.",
            "Check the current system time and date against actual time.",
            "If the time resets to a default (e.g., 01/01/2000) after a power cycle, the battery is dead.",
            "Some batteries are soldered onto the PCB and cannot be easily replaced.",
            "Consider upgrading to an Ethernet gateway that syncs via NTP (Network Time Protocol)."
        ]
    },
    {
        "name": "Surge / Storm Damage",
        "desc": "Blown communication transceivers after lightning strike",
        "answer": "Surge or storm damage often blows the delicate RS485 communication transceivers on the network. This causes the entire lighting network to drop offline and become unresponsive.",
        "steps": [
            "Check the network burden and clock LED indicators.",
            "If no LEDs are illuminated across multiple devices, the network power is dead.",
            "Use a multimeter to check the network voltage; if it's 0V, the power supply or transceivers are fried.",
            "Disconnect modules one by one to find the shorted device bringing the network down.",
            "Replace damaged components and install surge protection devices."
        ]
    }
]

regions = [
    "North Shore",
    "Eastern Suburbs",
    "Sutherland Shire",
    "Sydney CBD"
]

# Read the base template
base_template_path = os.path.join(DIR, "index.html")
with open(base_template_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

# We need to strip out existing main content, title, description, schema, etc.
# Actually, since index.html is complex, let's find the header/footer bounds or replace known segments.

generated_urls = []

for part in parts:
    system = "Clipsal C-Bus" if part in cbus_parts else "Dynalite"
    
    for sym in symptoms:
        for region in regions:
            slug = f"{system.lower().replace(' ', '-')}-{part.lower()}-{sym['name'].lower().replace(' / ', '-').replace(' ', '-')}-{region.lower().replace(' ', '-')}"
            filename = f"{slug}.html"
            filepath = os.path.join(TECH_LIB_DIR, filename)
            
            title = f"Fix {part} {sym['name']} | {system} Repairs {region}"
            desc = f"How to fix {sym['name'].lower()} on a {system} {part} module. Expert troubleshooting and repair services in {region}."
            
            # Create schema
            schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": {
                    "@type": "Question",
                    "name": f"How do I fix a {sym['name'].lower()} on {system} {part}?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": sym['answer']
                    }
                }
            }
            schema_json = json.dumps(schema, indent=2)
            
            # We'll use a simplified HTML structure injected into the base template's head/body
            # 1. Title
            content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', base_html)
            # 2. Meta description
            content = re.sub(r'name="description" content=".*?"', f'name="description" content="{desc}"', content)
            
            # 3. Inject FAQ Schema before </head>
            content = content.replace('</head>', f'<script type="application/ld+json">\n{schema_json}\n</script>\n</head>')
            
            # 4. Replace Hero Section
            hero_html = f'''
            <div class="hero" style="padding-top:120px; padding-bottom:60px;">
                <div class="container text-center">
                    <div class="tag">{system} Troubleshooting</div>
                    <h1>How to fix {sym['name']} on {system} {part}</h1>
                    <p class="subtitle" style="max-width:800px; margin:0 auto;">Expert diagnostic guide and repair services in the {region}.</p>
                </div>
            </div>
            '''
            content = re.sub(r'<div class="hero">.*?</div>\s*</div>\s*</div>', hero_html, content, flags=re.DOTALL)
            # To be safer with regex, let's do a more robust body replacement.
            # Find everything between </nav> and <footer...
            
            body_content = f'''
            {hero_html}
            <div class="section">
                <div class="container-sm">
                    <div style="background:#132647; padding:40px; border-radius:12px; border:1px solid #2a4a80;">
                        <h2>Direct Answer: {part} {sym['name']}</h2>
                        <p style="font-size:18px; line-height:1.6;"><strong>{sym['answer']}</strong></p>
                        
                        <h3 style="margin-top:40px;">Step-by-Step Diagnostic Steps</h3>
                        <ol style="margin-left:20px; line-height:1.8; font-size:16px;">
                            {''.join([f"<li>{step}</li>" for step in sym['steps']])}
                        </ol>
                        
                        <div style="margin-top:50px; text-align:center; padding:30px; background:rgba(240, 112, 32, 0.1); border-radius:8px;">
                            <h3>Need professional help in the {region}?</h3>
                            <p>If you're unable to resolve the {sym['desc'].lower()} issue on your {part}, our certified technicians can help. We provide modern upgrade recommendations and emergency repairs.</p>
                            <a href="/contact.html" class="nav-cta" style="display:inline-block; margin-top:20px; padding:15px 30px!important; font-size:16px;">Book a Service Call</a>
                        </div>
                    </div>
                </div>
            </div>
            '''
            
            # Replace main content. We can split at </nav> and <footer class="footer">
            if '</nav>' in content and '<footer' in content:
                head_nav = content.split('</nav>')[0] + '</nav>'
                footer_end = '<footer' + content.split('<footer')[1]
                content = head_nav + body_content + footer_end
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            generated_urls.append(f"tech-library/{filename}")

print(f"Generated {len(generated_urls)} technical articles in /tech-library/")

# Update Sitemaps
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    for url in generated_urls:
        if url not in xml:
            url_block = f"\n  <url>\n    <loc>https://sydneyautomationco.com.au/{url}</loc>\n    <lastmod>2026-06-20</lastmod>\n    <priority>0.60</priority>\n  </url>"
            xml = xml.replace("</urlset>", f"{url_block}\n</urlset>")
            
    with open(sitemap_xml, 'w', encoding='utf-8') as f:
        f.write(xml)

sitemap_html = os.path.join(DIR, "sitemap.html")
if os.path.exists(sitemap_html):
    with open(sitemap_html, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for url in generated_urls:
        if url not in html:
            title = url.replace("tech-library/", "").replace("-", " ").replace(".html", "").title()
            link_html = f'\n<li><a href="/{url}">{title}</a></li>'
            if "</ul>" in html:
                html = html.replace("</ul>", f"{link_html}\n</ul>", 1)
            else:
                html += f"\n<ul>{link_html}</ul>"
            
    with open(sitemap_html, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated sitemaps.")
