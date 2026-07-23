import os
import re

# Read pristine masters
with open('automation-sydney.html', 'r', encoding='utf-8') as f:
    comm_master = f.read()

with open('c-bus-programmer-sydney.html', 'r', encoding='utf-8') as f:
    cbus_master = f.read()

with open('dynalite-programmer-sydney.html', 'r', encoding='utf-8') as f:
    dyn_master = f.read()

# Define the 19 new monster pages with WAREHOUSE LIGHTING CONTROL focus (No PLC/SCADA Industrial Automation)
monster_pages = [
    # Category 1: Western Sydney Warehousing & Logistics Lighting Control
    {
        "filename": "warehouse-lighting-automation-sydney.html",
        "type": "comm",
        "sub_title": "Sydney Warehousing &amp; Logistics Lighting",
        "title": "Warehouse Lighting Automation Sydney | C-Bus &amp; Dynalite Relays",
        "desc": "Specialist warehouse lighting control across Greater Sydney. Expert C-Bus/Signify Dynalite relay repairs, high-bay lighting contactors, and DALI automation. Call 0422 469 739.",
        "lead": "Accredited Warehouse Lighting Specialists. Providing rapid C-Bus/Signify Dynalite relay repairs, high-bay lighting contactor maintenance, and automated motion sensors for major warehouses and logistics centers across Greater Sydney.",
        "landmarks": "<p>We service major distribution centers, fulfillment warehouses, and logistics hubs across Greater Sydney, delivering robust warehouse lighting control from the Western Sydney logistics corridors to southern warehousing precincts.</p>",
        "links": '<li><a href="/warehouse-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/warehouse-energy-optimization-cbus-dynalite" style="color:#f07020;text-decoration:underline;">Warehouse Energy Optimization</a></li><li><a href="/cbus-dynalite-repairs-erskine-park-logistics" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Repairs Erskine Park</a></li>'
    },
    {
        "filename": "industrial-lighting-control-western-sydney.html", # Keeping URL for sitemap consistency but changing title/content to warehouse lighting
        "type": "comm",
        "sub_title": "Western Sydney Warehousing Corridors",
        "title": "Warehouse Lighting Control Western Sydney | C-Bus &amp; Dynalite",
        "desc": "Expert warehouse lighting control across Western Sydney. Servicing logistics corridors in Wetherill Park, Erskine Park, Eastern Creek, and Smithfield. Call 0422 469 739.",
        "lead": "Accredited Warehouse Lighting Specialists. Servicing high-bay lighting relays, automated contactors, and DALI emergency lighting networks across warehousing corridors in Wetherill Park, Erskine Park, Eastern Creek, Arndell Park, and Smithfield.",
        "landmarks": "<p>We provide specialized C-Bus, Signify Dynalite, and DALI lighting support for major warehousing facilities across Western Sydney, covering key logistics and distribution corridors along the M4, M7, and Great Western Highway.</p>",
        "links": '<li><a href="/warehouse-lighting-control-eastern-creek" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Eastern Creek</a></li><li><a href="/warehouse-lighting-smithfield" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Smithfield</a></li><li><a href="/cbus-lighting-repairs-arndell-park-warehousing" style="color:#f07020;text-decoration:underline;">C-Bus Repairs Arndell Park Warehousing</a></li>'
    },
    {
        "filename": "cbus-dynalite-repairs-erskine-park-logistics.html",
        "type": "comm",
        "sub_title": "Erskine Park Logistics Lighting",
        "title": "C-Bus &amp; Dynalite Repairs Erskine Park | Logistics Lighting Control",
        "desc": "Specialist C-Bus and Signify Dynalite repairs for logistics centers, distribution warehouses, and fulfillment facilities in Erskine Park. Call 0422 469 739.",
        "lead": "Accredited Warehouse Lighting Specialists. Providing rapid C-Bus and Signify Dynalite relay repairs, high-bay contactor replacements, and DALI emergency lighting maintenance for major logistics centers across Erskine Park.",
        "landmarks": "<p>We support major distribution facilities and warehousing parks across Erskine Park, delivering heavy-duty lighting automation solutions along Lenore Drive, Erskine Park Road, and the central logistics estate corridors.</p>",
        "links": '<li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/warehouse-lighting-control-eastern-creek" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Eastern Creek</a></li><li><a href="/cbus-repair-wetherill-park-industrial" style="color:#f07020;text-decoration:underline;">C-Bus Repair Wetherill Park Warehousing</a></li>'
    },
    {
        "filename": "warehouse-lighting-control-eastern-creek.html",
        "type": "comm",
        "sub_title": "Eastern Creek Warehousing Lighting",
        "title": "Warehouse Lighting Control Eastern Creek | Fulfillment Lighting",
        "desc": "Expert warehouse lighting control for fulfillment centers, distribution hubs, and logistics facilities in Eastern Creek. Call 0422 469 739.",
        "lead": "Accredited Warehouse Lighting Specialists. Providing expert high-bay lighting maintenance, automated sensor networks, and rapid C-Bus/Dynalite fault finding for major fulfillment centers and distribution hubs across Eastern Creek.",
        "landmarks": "<p>We service massive warehousing facilities and logistics centers across Eastern Creek, delivering expert lighting automation support along Old Wallgrove Road, Wonderland Drive, and the M7 business park corridors.</p>",
        "links": '<li><a href="/cbus-dynalite-repairs-erskine-park-logistics" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Repairs Erskine Park</a></li><li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/cbus-lighting-repairs-arndell-park-warehousing" style="color:#f07020;text-decoration:underline;">C-Bus Repairs Arndell Park Warehousing</a></li>'
    },
    {
        "filename": "industrial-automation-lighting-smithfield.html", # Keeping URL for sitemap consistency
        "type": "comm",
        "sub_title": "Smithfield Warehousing Lighting",
        "title": "Warehouse Lighting Smithfield | C-Bus &amp; Dynalite Relay Repairs",
        "desc": "Specialist warehouse lighting control repairs for distribution centers, logistics hubs, and commercial warehousing facilities in Smithfield. Call 0422 469 739.",
        "lead": "Accredited Warehouse Lighting Specialists. Providing heavy-duty C-Bus/Signify Dynalite relay upgrades, automated high-bay contactor repairs, and DALI lighting maintenance for warehousing facilities across Smithfield.",
        "landmarks": "<p>We support established commercial distribution facilities and warehousing corridors across Smithfield, delivering expert lighting automation solutions along Cumberland Highway, Warren Road, and Woodpark Road.</p>",
        "links": '<li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/cbus-repair-wetherill-park-industrial" style="color:#f07020;text-decoration:underline;">C-Bus Repair Wetherill Park Warehousing</a></li><li><a href="/dynalite-repair-silverwater" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Silverwater Warehousing</a></li>'
    },
    {
        "filename": "cbus-lighting-repairs-arndell-park-warehousing.html",
        "type": "cbus",
        "sub_title": "Arndell Park Warehousing Lighting",
        "title": "C-Bus Repairs Arndell Park | Logistics &amp; Warehouse Lighting",
        "desc": "Expert C-Bus repairs for logistics facilities, commercial business parks, and distribution warehousing in Arndell Park. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Providing expert C-Bus relay repairs, automated high-bay lighting contactor maintenance, and rapid fault finding for logistics facilities and commercial warehousing across Arndell Park.",
        "landmarks": "<p>We service major warehousing facilities and distribution centers across Arndell Park, providing heavy-duty C-Bus lighting automation support along Holbeche Road, Doonside Road, and the Great Western Highway warehousing fringe.</p>",
        "links": '<li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/warehouse-lighting-control-eastern-creek" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Eastern Creek</a></li><li><a href="/cbus-dynalite-repairs-erskine-park-logistics" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Repairs Erskine Park</a></li>'
    },
    {
        "filename": "warehouse-energy-optimization-cbus-dynalite.html",
        "type": "comm",
        "sub_title": "Warehouse Lighting Energy Optimization",
        "title": "Warehouse Lighting Energy Optimization | C-Bus &amp; Dynalite Sensors",
        "desc": "Slash warehouse lighting bills with C-Bus and Signify Dynalite automated sensors, DALI relay scheduling, and high-bay lighting optimization. Call 0422 469 739.",
        "lead": "Accredited Warehouse Energy Optimization Specialists. Helping warehouse facility managers slash electricity waste by upgrading obsolete manual lighting to automated C-Bus/Dynalite motion sensors and DALI relay scheduling.",
        "landmarks": "<p>We provide warehouse energy optimization and automated lighting control upgrades for major logistics facilities and distribution centers across Greater Sydney, helping facility directors achieve significant operational cost reductions.</p>",
        "links": '<li><a href="/warehouse-lighting-automation-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Automation Sydney</a></li><li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li><li><a href="/carpark-lighting-upgrades-sydney" style="color:#f07020;text-decoration:underline;">Carpark Lighting Upgrades Sydney</a></li>'
    },

    # Category 2: Strata Managers Across NSW
    {
        "filename": "strata-lighting-maintenance-nsw.html",
        "type": "comm",
        "sub_title": "NSW Strata Maintenance",
        "title": "Strata Lighting Maintenance NSW | C-Bus, Dynalite &amp; DALI Support",
        "desc": "NSW-wide strata lighting maintenance contracts. Direct specialist support for Strata Managers covering C-Bus, Dynalite, DALI, and emergency lighting. Call 0422 469 739.",
        "lead": "Accredited Strata Lighting Specialists. Providing comprehensive maintenance contracts, rapid fault finding, and direct accredited software support for Strata Managers across Greater Sydney and Regional NSW.",
        "landmarks": "<p>We partner with leading strata management firms across NSW, providing dedicated automation support for residential towers, strata complexes, and waterfront properties from Sydney CBD to coastal and regional centers.</p>",
        "links": '<li><a href="/strata-managers-dynalite-cbus-repairs-sydney" style="color:#f07020;text-decoration:underline;">Strata Managers C-Bus &amp; Dynalite Repairs</a></li><li><a href="/high-rise-strata-lighting-automation-sydney" style="color:#f07020;text-decoration:underline;">High-Rise Strata Lighting Automation</a></li><li><a href="/strata-carpark-lighting-upgrades-nsw" style="color:#f07020;text-decoration:underline;">Strata Carpark Lighting Upgrades</a></li>'
    },
    {
        "filename": "strata-managers-dynalite-cbus-repairs-sydney.html",
        "type": "comm",
        "sub_title": "Strata Managers Rapid Response",
        "title": "Strata Managers C-Bus &amp; Dynalite Repairs | Direct Sydney Support",
        "desc": "Dedicated rapid response for Strata Managers dealing with C-Bus and Signify Dynalite lighting faults. Fixed-price programming, same-day service. Call 0422 469 739.",
        "lead": "Accredited Automation Specialists for Strata Managers. Stop relying on slow electrical contractors who outsource programming. We provide direct, same-day accredited software support for C-Bus and Dynalite common area faults.",
        "landmarks": "<p>We provide priority response for strata management portfolios across Greater Sydney, delivering rapid fault finding for residential towers, basement carparks, and common area lighting networks.</p>",
        "links": '<li><a href="/strata-lighting-maintenance-nsw" style="color:#f07020;text-decoration:underline;">Strata Lighting Maintenance NSW</a></li><li><a href="/strata-carpark-lighting-upgrades-nsw" style="color:#f07020;text-decoration:underline;">Strata Carpark Lighting Upgrades</a></li><li><a href="/strata" style="color:#f07020;text-decoration:underline;">Strata Services Hub</a></li>'
    },
    {
        "filename": "high-rise-strata-lighting-automation-sydney.html",
        "type": "comm",
        "sub_title": "High-Rise Strata Automation",
        "title": "High-Rise Strata Lighting Automation | Residential Tower Control",
        "desc": "Expert lighting automation for high-rise residential towers in Sydney. C-Bus/Dynalite common area repairs, DALI emergency lighting, and relay maintenance. Call 0422 469 739.",
        "lead": "Accredited High-Rise Strata Specialists. Providing expert lighting automation, common area relay maintenance, and DALI emergency lighting compliance for residential towers and multi-level strata complexes across Sydney.",
        "landmarks": "<p>We service premium high-rise residential towers across Sydney CBD, North Sydney, Chatswood, Parramatta, and the Eastern Suburbs, ensuring seamless common area lighting and automated relay control.</p>",
        "links": '<li><a href="/strata-lighting-maintenance-nsw" style="color:#f07020;text-decoration:underline;">Strata Lighting Maintenance NSW</a></li><li><a href="/strata-managers-dynalite-cbus-repairs-sydney" style="color:#f07020;text-decoration:underline;">Strata Managers C-Bus &amp; Dynalite Repairs</a></li><li><a href="/luxury-strata-automation-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Luxury Strata Eastern Suburbs</a></li>'
    },
    {
        "filename": "strata-carpark-lighting-upgrades-nsw.html",
        "type": "comm",
        "sub_title": "Strata Carpark Lighting Upgrades",
        "title": "Strata Carpark Lighting Upgrades NSW | DALI &amp; LED Sensor Networks",
        "desc": "Upgrade strata basement carparks with automated DALI and LED sensor networks. Slash energy waste, improve resident safety, and ensure AFSS compliance. Call 0422 469 739.",
        "lead": "Accredited Strata Energy &amp; Safety Specialists. Upgrading obsolete, energy-wasting strata basement carparks to intelligent, automated DALI and LED motion sensor networks across Greater Sydney and NSW.",
        "landmarks": "<p>We provide specialized basement carpark lighting upgrades for residential strata complexes across NSW, helping body corporates slash common area electricity bills while significantly improving security and compliance.</p>",
        "links": '<li><a href="/carpark-lighting-upgrades-sydney" style="color:#f07020;text-decoration:underline;">Carpark Lighting Upgrades Sydney</a></li><li><a href="/strata-lighting-maintenance-nsw" style="color:#f07020;text-decoration:underline;">Strata Lighting Maintenance NSW</a></li><li><a href="/led-upgrade-carpark-lighting-sydney" style="color:#f07020;text-decoration:underline;">LED Carpark Lighting Sydney</a></li>'
    },
    {
        "filename": "luxury-strata-automation-eastern-suburbs.html",
        "type": "comm",
        "sub_title": "Eastern Suburbs Luxury Strata",
        "title": "Luxury Strata Automation Eastern Suburbs | Prestige Tower Lighting",
        "desc": "Prestige strata automation across the Eastern Suburbs. Expert C-Bus, Signify Dynalite, and DALI lighting maintenance for luxury apartment complexes. Call 0422 469 739.",
        "lead": "Accredited Luxury Strata Specialists. Providing dedicated C-Bus, Signify Dynalite, and DALI lighting control maintenance for prestige residential towers and luxury apartment complexes across the Eastern Suburbs.",
        "landmarks": "<p>We support prestige strata complexes and luxury apartments across Bellevue Hill, Point Piper, Darling Point, Double Bay, Bondi, and Edgecliff, delivering discrete, high-end common area automation support.</p>",
        "links": '<li><a href="/high-rise-strata-lighting-automation-sydney" style="color:#f07020;text-decoration:underline;">High-Rise Strata Lighting Automation</a></li><li><a href="/strata-lighting-maintenance-nsw" style="color:#f07020;text-decoration:underline;">Strata Lighting Maintenance NSW</a></li><li><a href="/waterfront-strata-lighting-lower-north-shore" style="color:#f07020;text-decoration:underline;">Waterfront Strata Lower North Shore</a></li>'
    },
    {
        "filename": "waterfront-strata-lighting-lower-north-shore.html",
        "type": "comm",
        "sub_title": "Lower North Shore Waterfront Strata",
        "title": "Waterfront Strata Automation Lower North Shore | Prestige Lighting",
        "desc": "Specialist strata automation for waterfront apartment complexes across the Lower North Shore. C-Bus and Dynalite common area maintenance. Call 0422 469 739.",
        "lead": "Accredited Waterfront Strata Specialists. Providing specialist C-Bus, Signify Dynalite, and DALI common area lighting maintenance for luxury waterfront apartment complexes across the Lower North Shore.",
        "landmarks": "<p>We service premium waterfront strata complexes across Kirribilli, Kurraba Point, Cremorne Point, Neutral Bay, Mosman, and McMahons Point, ensuring flawless common area lighting and automated security relay control.</p>",
        "links": '<li><a href="/luxury-strata-automation-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Luxury Strata Eastern Suburbs</a></li><li><a href="/strata-lighting-maintenance-nsw" style="color:#f07020;text-decoration:underline;">Strata Lighting Maintenance NSW</a></li><li><a href="/high-rise-strata-lighting-automation-sydney" style="color:#f07020;text-decoration:underline;">High-Rise Strata Lighting Automation</a></li>'
    },

    # Category 3: Facility & Building Managers Across NSW
    {
        "filename": "building-managers-lighting-control-nsw.html",
        "type": "comm",
        "sub_title": "NSW Building Managers Hub",
        "title": "Building Managers Lighting Control NSW | Commercial Automation",
        "desc": "NSW-wide commercial building manager lighting support hub. Direct accredited software support for C-Bus, Signify Dynalite, DALI, and emergency lighting. Call 0422 469 739.",
        "lead": "Accredited Commercial Building Automation Specialists. Providing direct accredited software support, priority fault finding, and scheduled maintenance contracts for Commercial Building Managers across Greater Sydney and NSW.",
        "landmarks": "<p>We partner with commercial property management teams and facility directors across NSW, providing dedicated lighting control support for A-grade office towers, corporate parks, and institutional facilities.</p>",
        "links": '<li><a href="/facility-managers-dynalite-c(bus-support-sydney" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Support</a></li><li><a href="/commercial-tower-lighting-automation-sydney-cbd" style="color:#f07020;text-decoration:underline;">Commercial Tower Lighting Sydney CBD</a></li><li><a href="/building-manager-lighting-support-sydney" style="color:#f07020;text-decoration:underline;">Building Manager Lighting Support</a></li>'
    },
    {
        "filename": "facility-managers-dynalite-cbus-support-sydney.html",
        "type": "comm",
        "sub_title": "Facility Managers Direct Support",
        "title": "Facility Managers C-Bus &amp; Dynalite Support | Accredited Programmers",
        "desc": "Dedicated direct-access support for Facility Managers needing accredited C-Bus and Signify Dynalite software programmers. Bypass distributor delays. Call 0422 469 739.",
        "lead": "Accredited Software Programmers for Facility Managers. Bypass distributor delays and third-party contractor markups. We provide direct, accredited head-end software programming and rapid fault finding for commercial facilities.",
        "landmarks": "<p>We provide priority head-end software support for facility management portfolios across Greater Sydney, delivering rapid fault finding for complex commercial lighting, DALI networks, and automated relay controllers.</p>",
        "links": '<li><a href="/building-managers-lighting-control-nsw" style="color:#f07020;text-decoration:underline;">Building Managers Lighting Control NSW</a></li><li><a href="/facility-managers-cbus-dynalite-dali-guide" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Guide</a></li><li><a href="/commercial-tower-lighting-automation-sydney-cbd" style="color:#f07020;text-decoration:underline;">Commercial Tower Lighting Sydney CBD</a></li>'
    },
    {
        "filename": "commercial-tower-lighting-automation-sydney-cbd.html",
        "type": "comm",
        "sub_title": "Sydney CBD Commercial Towers",
        "title": "Commercial Tower Lighting Sydney CBD | Office Automation &amp; Relays",
        "desc": "Premium office tower lighting and relay maintenance in Sydney CBD. Expert C-Bus, Signify Dynalite, DALI, and emergency lighting automation. Call 0422 469 739.",
        "lead": "Accredited Commercial Tower Specialists. Providing premium office tower lighting automation, head-end software programming, and automated relay maintenance for A-grade commercial buildings across the Sydney CBD.",
        "landmarks": "<p>We service high-rise commercial office towers and corporate headquarters across the Sydney CBD, delivering expert lighting control support along Martin Place, George Street, Pitt Street, and Barangaroo.</p>",
        "links": '<li><a href="/building-managers-lighting-control-nsw" style="color:#f07020;text-decoration:underline;">Building Managers Lighting Control NSW</a></li><li><a href="/facility-managers-dynalite-cbus-support-sydney" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Support</a></li><li><a href="/boardroom-executive-office-automation-sydney" style="color:#f07020;text-decoration:underline;">Boardroom Executive Office Automation</a></li>'
    },
    {
        "filename": "hospitality-facility-management-lighting-sydney.html",
        "type": "comm",
        "sub_title": "Hospitality Facility Management",
        "title": "Hospitality Facility Management Lighting | Hotel &amp; Venue Automation",
        "desc": "Specialist lighting control and mood scene programming for hotels, pubs, restaurants, and hospitality venues across Greater Sydney. Call 0422 469 739.",
        "lead": "Accredited Hospitality Automation Specialists. Providing specialist architectural lighting control, mood scene programming, and rapid C-Bus/Dynalite fault finding for hotels, pubs, restaurants, and entertainment venues across Sydney.",
        "landmarks": "<p>We support major hospitality groups, boutique hotels, and entertainment venues across Greater Sydney, delivering expert lighting automation support from Sydney CBD and Darling Harbour to coastal and regional hospitality hubs.</p>",
        "links": '<li><a href="/hospitality-automation-sydney" style="color:#f07020;text-decoration:underline;">Hospitality Automation Sydney</a></li><li><a href="/commercial-tower-lighting-automation-sydney-cbd" style="color:#f07020;text-decoration:underline;">Commercial Tower Lighting Sydney CBD</a></li><li><a href="/facility-managers-dynalite-cbus-support-sydney" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Support</a></li>'
    },
    {
        "filename": "institutional-lighting-control-parramatta-western-sydney.html",
        "type": "comm",
        "sub_title": "Western Sydney Institutional",
        "title": "Institutional Lighting Control Parramatta | Healthcare &amp; Education",
        "desc": "Expert institutional, university, and healthcare facility lighting management across Parramatta and Western Sydney. C-Bus, Dynalite, and DALI support. Call 0422 469 739.",
        "lead": "Accredited Institutional Lighting Specialists. Providing expert C-Bus, Signify Dynalite, and DALI lighting management for universities, healthcare facilities, schools, and institutional campuses across Parramatta and Western Sydney.",
        "landmarks": "<p>We service major institutional facilities, university campuses, and healthcare centers across Parramatta, Westmead, Penrith, and the Western Sydney growth corridor, ensuring rigorous lighting compliance and automated control.</p>",
        "links": '<li><a href="/building-managers-lighting-control-nsw" style="color:#f07020;text-decoration:underline;">Building Managers Lighting Control NSW</a></li><li><a href="/facility-managers-dynalite-cbus-support-sydney" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Support</a></li><li><a href="/industrial-lighting-control-western-sydney" style="color:#f07020;text-decoration:underline;">Warehouse Lighting Control Western Sydney</a></li>'
    },
    {
        "filename": "boardroom-executive-office-automation-sydney.html",
        "type": "comm",
        "sub_title": "Executive Boardroom Automation",
        "title": "Boardroom &amp; Executive Office Automation Sydney | C-Bus &amp; Dynalite",
        "desc": "Corporate boardroom lighting, motorized shading, and AV relay integration across Sydney. Expert C-Bus and Signify Dynalite programming. Call 0422 469 739.",
        "lead": "Accredited Corporate Automation Specialists. Providing seamless C-Bus and Signify Dynalite programming for corporate boardrooms, executive suites, motorized shading, and AV relay integration across Greater Sydney.",
        "landmarks": "<p>We service premium corporate boardrooms and executive office suites across Sydney CBD, North Sydney, Barangaroo, and Parramatta, delivering flawless architectural lighting and automated AV scene control.</p>",
        "links": '<li><a href="/commercial-tower-lighting-automation-sydney-cbd" style="color:#f07020;text-decoration:underline;">Commercial Tower Lighting Sydney CBD</a></li><li><a href="/building-managers-lighting-control-nsw" style="color:#f07020;text-decoration:underline;">Building Managers Lighting Control NSW</a></li><li><a href="/facility-managers-dynalite-cbus-support-sydney" style="color:#f07020;text-decoration:underline;">Facility Managers C-Bus &amp; Dynalite Support</a></li>'
    }
]

print(f"Generating {len(monster_pages)} monster commercial, strata, warehouse, and facility management pages...")

generated = 0
for d in monster_pages:
    t = d["type"]
    fn = d["filename"]
    st = d["sub_title"]
    title = d["title"]
    desc = d["desc"]
    lead = d["lead"]
    landmarks = d["landmarks"]
    links = d["links"]
    
    if t == "comm":
        master = comm_master
        master = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", master)
        master = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', master)
        master = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', master)
        master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', f'<meta content="Menai, Sutherland Shire, {st}" name="geo.placename"/>', master)
        
        master = re.sub(r'"url": "https://sydneyautomationco.com.au/automation-sydney"', f'"url": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{st}"', master)
        master = re.sub(r'"name": "Premium Home & Commercial Automation Sydney"', f'"name": "{title.split("|")[0].strip()}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/automation-sydney"', f'"item": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        
        new_h1 = f'<h1>Lighting &amp; Automation<br/><span class="accent">{st}</span></h1>'
        master = re.sub(r'<h1>Premium Home & Commercial<br/><span class="accent">Automation Sydney</span></h1>', new_h1, master)
        new_lead = f'<p class="lead">{lead}</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)
        
    elif t == "cbus":
        master = cbus_master
        master = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", master)
        master = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', master)
        master = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', master)
        master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', f'<meta content="Menai, Sutherland Shire, {st}" name="geo.placename"/>', master)
        
        master = re.sub(r'"url": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"url": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{st}"', master)
        master = re.sub(r'"name": "C-Bus Programmer Sydney"', f'"name": "{title.split("|")[0].strip()}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"item": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        
        new_h1 = f'<h1>C-Bus Programmer<br/><span class="accent">{st}</span></h1>'
        master = re.sub(r'<h1>C-Bus Programming<br/><span class="accent">&amp; Commissioning</span></h1>', new_h1, master)
        new_lead = f'<p class="lead">{lead}</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)

    # Inject local geography and links
    match = re.search(r'(<h2.*?>.*?</h2>)', master)
    if match and "<!-- LOCAL CONTEXT INJECTED -->" not in master:
        injection = f"""
      <h3>Specialist Scope & Facilities</h3>
      {landmarks}
      
      <h3>Related Commercial Services</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        {links}
      </ul>
      <!-- LOCAL CONTEXT INJECTED -->
      
"""
        master = master[:match.start()] + injection + master[match.start():]
        
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(master)
        generated += 1
        print(f"Created: {fn}")

print(f"SUCCESS: Generated {generated} monster commercial pages.")

# Update the 12 blogs to speak to all stakeholders
html_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])
blogs = [f for f in html_files if f.startswith('blog-') or f.startswith('guide-') or f.startswith('how-to-') or f in ['cbus-vs-dynalite.html', 'dynalite-vs-cbus-sydney.html', 'cbus-dynalite-upgrade-guide.html', '4-years-building-facilities-management-jll-pbmg.html']]

callout_box = """
      <!-- MULTI-STAKEHOLDER CALLOUT -->
      <div style="background:#1a1a1a; border-left:4px solid #f07020; padding:28px; margin:36px 0; border-radius:6px; box-shadow:0 4px 20px rgba(0,0,0,0.3);">
        <h3 style="color:#f07020; margin-top:0; font-size:24px; font-weight:800; letter-spacing:0.5px;">Tailored Expertise for Every Stakeholder</h3>
        <p style="font-size:16px; line-height:1.7; color:#e0e0e0; margin-bottom:0;">Whether you are a <strong>Strata Manager</strong> resolving common area lighting faults across NSW, a <strong>Facility Manager</strong> needing direct accredited software access without distributor delays, an <strong>Operations Director</strong> slashing warehouse energy waste in Western Sydney, or an <strong>Electrical Contractor</strong> partnering with an accredited programmer, Sydney Automation Co. provides direct, fixed-price, same-day specialist support across Greater Sydney and Regional NSW.</p>
      </div>
      <!-- MULTI-STAKEHOLDER CALLOUT -->
"""

blogs_updated = 0
for b in blogs:
    with open(b, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    if "<!-- MULTI-STAKEHOLDER CALLOUT -->" not in content:
        # Find a suitable place to inject, e.g. after the first <p> or before the first <h2> / <h3>
        match = re.search(r'(<h2.*?>.*?</h2>|<h3.*?>.*?</h3>)', content)
        if match:
            content = content[:match.start()] + callout_box + content[match.start():]
            with open(b, 'w', encoding='utf-8') as f:
                f.write(content)
            blogs_updated += 1
            print(f"Updated blog with multi-stakeholder callout: {b}")
        else:
            # Try finding first <p> or similar
            match_p = re.search(r'(<p.*?>.*?</p>)', content)
            if match_p:
                content = content[:match_p.end()] + callout_box + content[match_p.end():]
                with open(b, 'w', encoding='utf-8') as f:
                    f.write(content)
                blogs_updated += 1
                print(f"Updated blog with multi-stakeholder callout: {b}")

print(f"SUCCESS: Updated {blogs_updated} blogs/guides.")
