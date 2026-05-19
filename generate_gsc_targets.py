import os
import re

with open('blog-strata-lighting-energy-savings-sydney.html', 'r', encoding='utf-8', errors='ignore') as f:
    master = f.read()

def make_page(fn, tag, title, desc, h1, lead, body):
    content = master
    content = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", content)
    content = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', content)
    content = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', content)
    content = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', content)
    content = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', content)
    content = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', content)
    content = re.sub(r'<span style="background:rgba\(240,112,32,0\.12\).*?</span>', f'<span style="background:rgba(240,112,32,0.12);color:#f07020;border:1px solid #f0702040;border-radius:50px;padding:4px 12px;font-size:12px;font-weight:700">{tag}</span>', content)
    content = re.sub(r'<h1.*?>.*?</h1>', f'<h1 style="font-family:\'Barlow Condensed\',sans-serif;font-size:clamp(32px,5vw,56px);font-weight:900;line-height:1.05;margin-bottom:20px">{h1}</h1>', content, flags=re.DOTALL)
    content = re.sub(r'<p style="font-size:18px;color:#a8c0e0;line-height:1\.8;margin-bottom:40px;max-width:640px">.*?</p>', f'<p style="font-size:18px;color:#a8c0e0;line-height:1.8;margin-bottom:40px;max-width:640px">{lead}</p>', content, flags=re.DOTALL)
    img_html = '<div style="margin:8px 0 40px;border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.4);"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=1200&q=80" alt="'+title.split("|")[0].strip()+'" style="width:100%;height:420px;object-fit:cover;display:block;"/></div>'
    full_body = img_html + body
    match = re.search(r'<div class="article-body">.*?</div\s*>\s*<div style="background:#132647', content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + f'<div class="article-body">\n{full_body}\n</div>\n<div style="background:#132647' + content[match.end():]
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {fn}")

EMERGENCY_BOX = '''<div style="background:#1a1a1a;border-left:4px solid #f07020;padding:24px;margin:32px 0;border-radius:6px;">
  <h3 style="color:#f07020;margin-top:0;">Emergency Breakdown?</h3>
  <p style="color:#e0e0e0;margin-bottom:0;">For immediate C-Bus or Dynalite emergency support visit <a href="https://cbusnotworking.com.au" target="_blank" style="color:#f07020;font-weight:bold;">cbusnotworking.com.au</a> or call <strong>0422 469 739</strong>.</p>
</div>'''

pages = [
    # ── STRATEGY: "automation companies sydney" generic landing ──
    ("smart-home-automation-companies-sydney.html", "Smart Home Automation",
     "Smart Home Automation Companies Sydney | C-Bus &amp; Dynalite Specialists",
     "Searching for smart home automation companies in Sydney? Sydney Automation Co. — accredited C-Bus and Dynalite specialists. Fixed-price. 2-hr emergency dispatch. Call 0422 469 739.",
     'Smart Home Automation Companies Sydney<br/><span style="color:#f07020">Accredited C-Bus &amp; Dynalite Specialists</span>',
     "The accredited difference: why Sydney Automation Co. outperforms generic automation companies in Sydney for C-Bus programming, Dynalite commissioning, and emergency fault resolution.",
     f"""
<h2>Why 'Automation Company' Matters More Than You Think</h2>
<p>When searching for smart home automation companies in Sydney, the difference between a generalist AV integrator and an officially accredited C-Bus and Signify Dynalite specialist is enormous. Only accredited specialists hold manufacturer-issued software licences allowing them to connect directly to your system's head-end, diagnose faults with precision tools, and deliver a complete database backup upon handover.</p>
<h2>What Sets Sydney Automation Co. Apart</h2>
<ul style="line-height:1.9;margin:20px 0 28px;padding-left:20px;color:#e0e0e0;">
<li><strong>Accredited C-Bus System Integrator</strong> — Schneider Electric certified, full Toolkit access</li>
<li><strong>Accredited Signify Dynalite Specialist</strong> — DyNet RS-485, EnvisionProject licensed</li>
<li><strong>DALI-2 Certified</strong> — Emergency lighting AFSS compliance expertise</li>
<li><strong>Fixed-price transparent quotes</strong> — No open-ended hourly billing</li>
<li><strong>2-hour emergency dispatch</strong> across Greater Sydney, 7 days a week</li>
<li><strong>100% database handover</strong> — You own your automation data, forever</li>
</ul>
{EMERGENCY_BOX}
<h2>Services Across All Property Types</h2>
<p>We serve <a href="/c-bus-programmer-sydney">luxury smart homes</a>, <a href="/commercial-tower-lighting-automation-sydney-cbd">commercial office towers</a>, <a href="/strata-lighting-maintenance-nsw">strata complexes</a>, and <a href="/warehouse-lighting-automation-sydney">industrial warehouses</a> across Greater Sydney and Regional NSW. Use our <a href="/lighting-automation-cost-calculator-sydney">interactive cost calculator</a> for an instant estimate, or call <strong>0422 469 739</strong> now.</p>
"""),

    # ── STRATEGY: car park lighting hub ──
    ("car-park-lighting-repairs-sydney.html", "Carpark Lighting",
     "Car Park Lighting Repairs Sydney | C-Bus &amp; DALI Maintenance",
     "Expert car park lighting repairs in Sydney. C-Bus relay faults, DALI sensor failures, emergency lighting compliance. Strata and commercial carparks. Call 0422 469 739.",
     'Car Park Lighting Repairs Sydney<br/><span style="color:#f07020">C-Bus Relay &amp; DALI Sensor Specialists</span>',
     "Resolving stuck-on carpark lights, failed DALI motion sensors, and C-Bus relay faults in strata and commercial basement carparks across Greater Sydney.",
     f"""
<h2>The Critical Role of Carpark Lighting Automation</h2>
<p>Basement carparks across strata complexes, commercial towers, and mixed-use developments across <a href="/strata-lighting-maintenance-nsw">Sydney's strata buildings</a> and <a href="/building-managers-lighting-control-nsw">commercial facilities</a> rely on integrated C-Bus relay controllers and DALI motion sensor networks to deliver safe, energy-efficient lighting. When these systems fail, carpark lights either go completely dark — creating serious safety and liability risks — or remain permanently on 24/7, causing strata electricity bills to skyrocket.</p>
<h2>Common Car Park Lighting Faults We Fix</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:24px 0 32px;">
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">Stuck-On C-Bus Relays</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">Fused contactor channels leaving carpark lights permanently illuminated. Drop-in relay replacement from $450 fixed.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">DALI Sensor Failures</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">Dead motion sensors leaving bays in darkness or preventing automatic dimming. IP65 replacement and DALI re-addressing.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">Emergency Lighting Failures</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">DALI emergency luminaire AFSS non-compliance. Pre-inspection rectification and discharge test reporting.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">LED Upgrade & Dimming</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">LED high-bay replacement with DALI dimming integration for 40-60% energy cost reduction in strata carparks.</p></div>
</div>
{EMERGENCY_BOX}
<h2>Carpark Lighting Across Sydney</h2>
<p>We service strata carparks across the <a href="/strata-carpark-lighting-upgrades-nsw">Eastern Suburbs, North Shore, and inner city</a>, commercial basement carparks in the <a href="/commercial-tower-lighting-automation-sydney-cbd">Sydney CBD and Parramatta</a>, and warehouse dispatch bays across <a href="/warehouse-lighting-automation-sydney">Western Sydney</a>. Call <strong>0422 469 739</strong> or visit <a href="https://cbusnotworking.com.au" target="_blank" style="color:#f07020;">cbusnotworking.com.au</a> for emergency support.</p>
"""),

    # ── STRATEGY: brownfield lighting upgrade ──
    ("brownfield-lighting-upgrade-cbus-dynalite-sydney.html", "Upgrade Specialist",
     "Brownfield Lighting Upgrade | C-Bus &amp; Dynalite Retrofit Sydney",
     "Accredited brownfield lighting control upgrades across Sydney. Replacing legacy relay panels with C-Bus and Dynalite without full rewires. Call 0422 469 739.",
     'Brownfield Lighting Upgrade<br/><span style="color:#f07020">C-Bus &amp; Dynalite Retrofit Without Full Rewires</span>',
     "How commercial building managers and facility engineers can upgrade obsolete manual relay panels and legacy dimming systems to modern C-Bus and Dynalite automation without costly full rewires.",
     f"""
<h2>What Is a Brownfield Lighting Upgrade?</h2>
<p>A brownfield lighting upgrade refers to retrofitting modern automation into an existing, occupied building — as opposed to a greenfield new build where automation is designed in from scratch. This scenario is extremely common across commercial towers, strata complexes, warehouses, and institutional facilities built in the 1990s and 2000s across Greater Sydney, where lighting was originally controlled via simple manual switchboards, timer relays, or basic photocell sensors.</p>
<h2>The Core Challenge: Existing Infrastructure</h2>
<p>Brownfield sites present unique engineering constraints. Existing conduit runs, circuit wiring, and switchboard configurations cannot simply be ripped out without massive disruption to occupied tenants and facilities. The solution requires a staged, intelligent retrofit strategy that layers modern C-Bus or Dynalite automation intelligence over the existing 240V wiring infrastructure with minimal disturbance.</p>
<h2>Our Staged Brownfield Retrofit Approach</h2>
<ol style="line-height:1.9;margin:20px 0 28px;padding-left:20px;color:#e0e0e0;">
<li><strong>Circuit Audit:</strong> We map existing lighting circuits, identify load types (LED, fluorescent, HID), and determine optimal relay and dimmer sizing for the new C-Bus or Dynalite enclosures.</li>
<li><strong>DIN-Rail Enclosure Integration:</strong> New C-Bus SpaceLogic relay and dimmer modules are installed within existing switchboard enclosures, utilizing existing wiring where possible to minimize rewiring costs.</li>
<li><strong>DALI-2 Sensor Overlay:</strong> Modern DALI-2 motion and daylight sensors are installed in occupied spaces without requiring new conduit — connecting via existing Cat5e or dedicated DALI bus cable run overhead.</li>
<li><strong>Head-End Commissioning:</strong> Full C-Bus Toolkit or Dynalite EnvisionProject database programming, schedule automation, and DALI emergency lighting integration is executed by our accredited specialists.</li>
</ol>
{EMERGENCY_BOX}
<h2>Upgrade Your Building Without the Disruption</h2>
<p>We have executed successful brownfield upgrades across commercial towers in the <a href="/commercial-tower-lighting-automation-sydney-cbd">Sydney CBD</a>, strata complexes across the <a href="/strata-lighting-maintenance-nsw">Eastern Suburbs</a>, and logistics warehouses across <a href="/warehouse-lighting-automation-sydney">Western Sydney</a>. Explore our <a href="/obsolete-cbus-5000-series-relay-replacement-sydney">obsolete relay replacement guide</a> and <a href="/lighting-automation-cost-calculator-sydney">cost calculator</a> to scope your upgrade.</p>
"""),

    # ── STRATEGY: strata energy consumption reduction ──
    ("strata-energy-consumption-reduction-lighting-nsw.html", "Energy Savings",
     "Strata Energy Consumption Reduction | Lighting Automation NSW",
     "Reduce strata building energy consumption by 30-60% through C-Bus and DALI lighting schedule optimization across NSW. Fixed-price audits. Call 0422 469 739.",
     'Strata Energy Consumption Reduction<br/><span style="color:#f07020">C-Bus &amp; DALI Lighting Optimization NSW</span>',
     "How strata managers and owners corporations across NSW can reduce common area electricity consumption by 30-60% through targeted C-Bus relay scheduling and DALI motion sensor optimization.",
     f"""
<h2>The Electricity Cost Crisis in NSW Strata Buildings</h2>
<p>Electricity costs represent the single largest controllable expense in most NSW strata building budgets. Common area lighting — spanning lobby areas, basement carparks, stairwells, lift lobbies, and external perimeter lighting — frequently accounts for 40-70% of a strata building's total electricity consumption. In most strata complexes, this lighting runs at full brightness 24 hours a day because the original C-Bus or DALI automation schedules were never properly configured or have drifted significantly from their optimal programming over the years.</p>
<h2>How We Reduce Your Strata Electricity Bill</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:24px 0 32px;">
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">Schedule Audit &amp; Optimization</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">We eliminate conflicting and duplicate C-Bus timer schedules that leave lights running unnecessarily during low-occupancy hours.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">DALI Motion Sensor Tuning</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">Recalibrating occupancy sensor sensitivity and timeout thresholds to ensure corridors and stairwells dim within 3 minutes of vacancy.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">Daylight Harvesting</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">Programming DALI photosensors to automatically dim common area lighting proportionally to available natural light throughout the day.</p></div>
  <div style="background:#132647;border:1px solid #2a4a80;padding:20px;border-radius:8px;"><h3 style="color:#f07020;font-size:17px;margin:0 0 8px;">Carpark Dimming Profiles</h3><p style="color:#a8c0e0;font-size:14px;margin:0;">Programming basement carpark C-Bus and DALI networks to dim to 20% ambient light during off-peak hours with instant full-brightness motion response.</p></div>
</div>
{EMERGENCY_BOX}
<h2>Fixed-Price Energy Audits for Strata Portfolios</h2>
<p>We provide transparent, fixed-price lighting energy audits with written before-and-after consumption reports for strata management firms managing portfolios across NSW. Explore our <a href="/strata-lighting-maintenance-nsw">Strata Lighting Maintenance NSW</a> capabilities and <a href="/strata-carpark-lighting-upgrades-nsw">Strata Carpark Lighting Upgrades</a> to start reducing your strata levies today.</p>
"""),

    # ── STRATEGY: emergency exit lighting maintenance ──
    ("emergency-exit-lighting-maintenance-sydney.html", "Emergency Lighting",
     "Emergency &amp; Exit Lighting Maintenance Sydney | AFSS Compliance",
     "Specialist emergency and exit lighting maintenance in Sydney. DALI testing, AFSS compliance, and urgent fault rectification for commercial and strata buildings. Call 0422 469 739.",
     'Emergency &amp; Exit Lighting Maintenance Sydney<br/><span style="color:#f07020">DALI Testing &amp; AFSS Compliance Experts</span>',
     "Specialist DALI emergency lighting maintenance, exit light testing, and Annual Fire Safety Statement compliance for commercial buildings, strata complexes, and warehouses across Sydney.",
     f"""
<h2>Your Legal Obligation: AFSS Emergency Lighting Compliance</h2>
<p>Under NSW Building legislation and Australian Standard AS/NZS 2293, all commercial buildings, strata complexes, and multi-tenancy facilities must maintain fully functional emergency and exit lighting systems. An Annual Fire Safety Statement (AFSS) must be lodged with your local council each year, confirming that all essential fire safety measures — including emergency luminaires and exit signs — have been professionally inspected and tested to the required standard.</p>
<h2>Common Emergency Lighting Failures We Rectify</h2>
<ul style="line-height:1.9;margin:20px 0 28px;padding-left:20px;color:#e0e0e0;">
<li><strong>DALI line address conflicts</strong> — Duplicate ballast addresses causing entire emergency zones to fail discharge tests</li>
<li><strong>Failed DALI emergency drivers</strong> — Luminaires not switching to battery mode during mains power failure simulation</li>
<li><strong>Broken DALI communication loops</strong> — Cable breaks preventing the monitoring controller from polling emergency luminaire status</li>
<li><strong>Depleted battery packs</strong> — Emergency fittings failing the mandatory 90-minute discharge duration test</li>
<li><strong>Exit sign lamp failures</strong> — LED exit signs with failed drivers or broken illumination circuits</li>
</ul>
{EMERGENCY_BOX}
<h2>Pre-AFSS Inspection Rectification</h2>
<p>Do not wait until your AFSS inspection to discover emergency lighting failures. Sydney Automation Co. provides comprehensive pre-inspection DALI line audits, fault rectification, and written discharge test compliance reports for commercial and strata buildings across Greater Sydney. Explore our dedicated <a href="/afss-testing-sydney">AFSS Testing Sydney</a> service page and <a href="/cbus-dynalite-fault-codes-sydney">Emergency Fault Code Hub</a> for immediate support.</p>
"""),

    # ── STRATEGY: LED lighting upgrade service ──
    ("led-lighting-upgrade-cbus-dali-sydney.html", "LED Upgrades",
     "LED Lighting Upgrade Service Sydney | C-Bus &amp; DALI Integration",
     "Specialist LED lighting upgrade and C-Bus/DALI integration service across Sydney. Eliminate flickering, improve dimming, and slash energy costs. Call 0422 469 739.",
     'LED Lighting Upgrade Service Sydney<br/><span style="color:#f07020">C-Bus &amp; DALI-2 Integration Specialists</span>',
     "Eliminating LED dimming flicker, integrating new LED arrays into existing C-Bus and Signify Dynalite networks, and deploying DALI-2 addressable drivers for luxury homes and commercial buildings.",
     f"""
<h2>The Hidden Complexity of LED Upgrades in Automated Buildings</h2>
<p>Upgrading halogen or fluorescent luminaires to modern LED technology in a C-Bus or Signify Dynalite automated building is not as simple as swapping globes. Legacy C-Bus leading-edge phase-cut dimmers were designed for resistive halogen loads and are fundamentally incompatible with the capacitive switching power supplies inside modern LED drivers, causing severe flickering, buzz, and premature LED driver failure.</p>
<h2>How We Resolve LED Dimming Compatibility</h2>
<ol style="line-height:1.9;margin:20px 0 28px;padding-left:20px;color:#e0e0e0;">
<li><strong>Dimmer Compatibility Audit:</strong> We test your existing C-Bus or Dynalite dimmer channels against your new LED specifications to identify incompatible load mismatches before any fittings are purchased.</li>
<li><strong>Universal Dimmer Upgrades:</strong> We upgrade legacy C-Bus leading-edge dimmers to advanced universal trailing-edge or 0-10V/DALI-2 dimmer controllers providing 100% smooth, flicker-free LED dimming.</li>
<li><strong>DALI-2 Driver Integration:</strong> For premium installations, we integrate addressable DALI-2 LED drivers into your C-Bus or Dynalite network, enabling individual luminaire-level dimming control, colour tuning, and automated fault reporting.</li>
<li><strong>Scene Reprogramming:</strong> We remap all existing lighting scenes and presets to the new LED load profiles, ensuring every button press delivers the precise, elegant ambience your space demands.</li>
</ol>
{EMERGENCY_BOX}
<h2>LED Upgrades Across Sydney</h2>
<p>We execute LED upgrade integrations for luxury smart homes across the <a href="/c-bus-programmer-eastern-suburbs">Eastern Suburbs</a> and <a href="/c-bus-programmer-north-shore">North Shore</a>, commercial office floors across the <a href="/commercial-tower-lighting-automation-sydney-cbd">Sydney CBD</a>, and LED high-bay retrofits in <a href="/warehouse-lighting-automation-sydney">Western Sydney warehouses</a>. Use our <a href="/lighting-automation-cost-calculator-sydney">interactive cost calculator</a> for an instant upgrade estimate.</p>
"""),
]

# Smart home automation suburb pages — targeting the exact GSC queries
smart_home_suburbs = [
    ("pymble", "Smart Home Automation Pymble | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Pymble. Expert keypad upgrades, relay repairs and scene programming. Call 0422 469 739."),
    ("st-ives", "Smart Home Automation St Ives | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in St Ives. Expert relay repairs, scene programming and LED dimming. Call 0422 469 739."),
    ("lindfield", "Smart Home Automation Lindfield | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Lindfield. Keypad upgrades, dimmer repairs and database recovery. Call 0422 469 739."),
    ("neutral-bay", "Smart Home Automation Neutral Bay | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Neutral Bay. Relay replacements, touchscreen upgrades and fault finding. Call 0422 469 739."),
    ("turramurra", "Smart Home Automation Turramurra | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Turramurra. Expert relay repairs, LED dimmer upgrades and programming. Call 0422 469 739."),
    ("killara", "Smart Home Automation Killara | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Killara. Scene programming, relay replacements and emergency dispatch. Call 0422 469 739."),
    ("mosman", "Smart Home Automation Mosman | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Mosman. Waterfront home relay repairs, dimmer upgrades and programming. Call 0422 469 739."),
    ("double-bay", "Smart Home Automation Double Bay | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Double Bay. Luxury apartment lighting repairs and keypad upgrades. Call 0422 469 739."),
    ("cremorne", "Smart Home Automation Cremorne | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Cremorne. Expert relay repairs, touchscreen upgrades and fault finding. Call 0422 469 739."),
    ("lane-cove", "Smart Home Automation Lane Cove | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Lane Cove. Relay replacements, dimmer upgrades and emergency dispatch. Call 0422 469 739."),
    ("miranda", "Smart Home Automation Miranda | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Miranda. Expert relay repairs, LED upgrades and scene programming. Call 0422 469 739."),
    ("vaucluse", "Smart Home Automation Vaucluse | C-Bus &amp; Dynalite Specialists", "Accredited C-Bus and Dynalite smart home automation in Vaucluse. Waterfront home relay repairs and keypad upgrades. Call 0422 469 739."),
]

for suburb, title, desc in smart_home_suburbs:
    suburb_label = suburb.replace('-', ' ').title()
    fn = f"smart-home-automation-{suburb}.html"
    h1 = f'Smart Home Automation {suburb_label}<br/><span style="color:#f07020">Accredited C-Bus &amp; Dynalite Specialists</span>'
    lead = f"Accredited Clipsal C-Bus and Signify Dynalite smart home automation specialists serving {suburb_label} and surrounding suburbs. Fixed-price repairs, keypad upgrades, and 2-hour emergency dispatch."
    body = f"""
<h2>Expert Smart Home Automation in {suburb_label}</h2>
<p>Prestige homes and luxury apartments throughout {suburb_label} rely on sophisticated Clipsal C-Bus and Signify Dynalite automation networks to manage architectural lighting scenes, motorized blinds, climate control integration, and secure access systems. When these systems malfunction, only an accredited specialist with genuine manufacturer software tools can restore them correctly.</p>
<h2>Common Smart Home Faults We Fix in {suburb_label}</h2>
<ul style="line-height:1.9;margin:20px 0 28px;padding-left:20px;color:#e0e0e0;">
<li>C-Bus relay contactors welded shut leaving lights permanently on</li>
<li>LED dimming flicker from incompatible leading-edge C-Bus dimmers</li>
<li>Dynalite keypad unresponsive due to DyNet bus power supply failure</li>
<li>Touchscreen interface frozen or displaying network error messages</li>
<li>C-Bus Toolkit software locked out after installer discontinued service</li>
<li>Smart lighting scenes not triggering correctly after power outage</li>
</ul>
{EMERGENCY_BOX}
<h2>Your Accredited Local Specialists</h2>
<p>Sydney Automation Co. provides direct, fixed-price smart home automation services in {suburb_label} and across the <a href="/c-bus-programmer-north-shore">North Shore</a>, <a href="/c-bus-programmer-eastern-suburbs">Eastern Suburbs</a>, and <a href="/c-bus-programmer-sydney">Greater Sydney</a>. Explore our <a href="/control4-lighting-repairs-cbus-replacement-sydney">smart home upgrade options</a> and <a href="/lighting-automation-cost-calculator-sydney">instant cost calculator</a> to scope your project.</p>
"""
    pages.append((fn, "Smart Home Automation", title, desc, h1, lead, body))

print(f"Generating {len(pages)} GSC-targeted pages...")
for p in pages:
    make_page(*p)

print(f"\nSUCCESS: Generated {len(pages)} pages targeting real GSC search queries.")
