import os, re, json

BASE = r'C:\Users\gaska\Sydney-Automation-Co'

def read_file(fp):
    for enc in ('utf-8','latin1','cp1252'):
        try:
            with open(fp,'r',encoding=enc) as f: return f.read()
        except: continue
    return None

def write_file(fp, c):
    with open(fp,'w',encoding='utf-8',errors='replace') as f: f.write(c)

# ============================================================
# 1. HOWTO SCHEMA for fault-finding pages
# ============================================================
print("=== 1. HowTo Schema for Troubleshooting Pages ===")

howto_cbus = {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "How to Diagnose C-Bus Lighting Control Faults",
    "description": "Step-by-step diagnostic procedure for Clipsal C-Bus lighting control system faults including bus voltage checks, module diagnostics, and programming verification.",
    "totalTime": "PT30M",
    "step": [
        {"@type": "HowToStep", "name": "Measure C-Bus Network Voltage", "text": "Using a multimeter, measure the voltage across the C-Bus network terminals at the 5500PS power supply. Normal range is 5 to 11.5V DC. Below 5V indicates a power supply fault or short circuit.", "position": 1},
        {"@type": "HowToStep", "name": "Check 5500PC Network Interface LEDs", "text": "Observe the LED indicators on the 5500PC network interface. A steady light indicates normal communication. Rapid flashing indicates a network fault. No light indicates power or hardware failure.", "position": 2},
        {"@type": "HowToStep", "name": "Scan with C-Bus Toolkit Software", "text": "Connect a laptop running C-Bus Toolkit to the 5500PC via USB or Ethernet. Run a network scan to identify all online modules, check for address conflicts, and verify programming integrity.", "position": 3},
        {"@type": "HowToStep", "name": "Verify Network Burden Placement", "text": "C-Bus networks require a network burden at each end of the bus segment. Check that burdens are correctly placed and that no segment has multiple or missing burdens.", "position": 4},
        {"@type": "HowToStep", "name": "Test Individual Module Outputs", "text": "Using C-Bus Toolkit, manually activate each dimmer or relay channel to verify output. A non-responsive module may need power cycling or replacement.", "position": 5}
    ]
}

howto_dynalite = {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "How to Diagnose Dynalite Lighting Control Faults",
    "description": "Step-by-step diagnostic procedure for Signify Dynalite lighting control system faults including DyNet bus checks, processor verification, and address conflict resolution.",
    "totalTime": "PT30M",
    "step": [
        {"@type": "HowToStep", "name": "Check DyNet Bus Voltage", "text": "Measure the voltage between DyNet+ and DyNet- terminals at any keypad or device. Normal operating range is 9.6 to 42V DC. Below 9.6V indicates a bus power fault.", "position": 1},
        {"@type": "HowToStep", "name": "Inspect Processor Status LEDs", "text": "Check the DDBC1200 or main processor LED indicators. Normal operation shows specific LED patterns. Error LEDs indicate processor fault or communication loss.", "position": 2},
        {"@type": "HowToStep", "name": "Scan with Dynalite EnvisionProject", "text": "Connect to the processor via Dynalite EnvisionProject software. Scan the DyNet bus to identify all online devices, check for address conflicts, and verify device configuration.", "position": 3},
        {"@type": "HowToStep", "name": "Power Cycle the Processor", "text": "Disconnect power from the Dynalite processor for 30 seconds. Reconnect and wait 2 minutes for the DyNet bus to re-initialise. Check keypad response after reboot.", "position": 4},
        {"@type": "HowToStep", "name": "Verify Keypad Communication", "text": "Test each keypad by pressing buttons and observing LED response. Non-responsive keypads may have wiring faults, address conflicts, or hardware failure.", "position": 5}
    ]
}

# Add HowTo to cbus-fault-finding-sydney.html (if not already there)
fp = os.path.join(BASE, 'cbus-fault-finding-sydney.html')
c = read_file(fp)
if c and 'HowTo' not in c:
    howto_json = json.dumps(howto_cbus, indent=2)
    schema_tag = f'<script type="application/ld+json">\n{howto_json}\n</script>'
    # Insert before </head>
    if '</head>' in c:
        c = c.replace('</head>', schema_tag + '\n</head>', 1)
        write_file(fp, c)
        print("  OK: cbus-fault-finding-sydney.html")
    else:
        print("  FAIL: cbus-fault-finding-sydney.html")
elif c:
    print("  SKIP (already has HowTo): cbus-fault-finding-sydney.html")

# Add HowTo to dynalite-fault-finding-sydney-common-faults.html
fp = os.path.join(BASE, 'dynalite-fault-finding-sydney-common-faults.html')
c = read_file(fp)
if c and 'HowTo' not in c:
    howto_json = json.dumps(howto_dynalite, indent=2)
    schema_tag = f'<script type="application/ld+json">\n{howto_json}\n</script>'
    if '</head>' in c:
        c = c.replace('</head>', schema_tag + '\n</head>', 1)
        write_file(fp, c)
        print("  OK: dynalite-fault-finding-sydney-common-faults.html")
    else:
        print("  FAIL: dynalite-fault-finding-sydney-common-faults.html")
elif c:
    print("  SKIP (already has HowTo): dynalite-fault-finding-sydney-common-faults.html")


# ============================================================
# 2. SERVICE SCHEMA for pages that lack it
# ============================================================
print("\n=== 2. Service Schema for Service Pages ===")

SERVICE_PAGES = {
    'cbus-specialist-sydney.html': {
        'name': 'C-Bus Specialist Sydney — Programming, Fault Finding & Commissioning',
        'description': 'Accredited C-Bus specialist services in Sydney including C-Bus programming with C-Bus Toolkit, system commissioning, fault finding, and module replacement by a certified Clipsal programmer.',
        'serviceType': 'C-Bus Programming and Fault Finding'
    },
    'cbus-upgrade-sydney.html': {
        'name': 'C-Bus System Upgrade Sydney — Modernisation & Expansion',
        'description': 'Upgrade your Clipsal C-Bus system with current-generation hardware, mobile app control, touchscreens, and energy-efficient sensors. System migration from C-Bus Classic to C-Bus 2.',
        'serviceType': 'C-Bus System Upgrade'
    },
    'dynalite-programmer-sydney.html': {
        'name': 'Dynalite Programmer Sydney — System Design & Programming',
        'description': 'Accredited Dynalite system designer offering programming and commissioning services using Dynalite EnvisionProject software for commercial and residential buildings.',
        'serviceType': 'Dynalite System Design and Programming'
    },
    'dynalite-repair-sydney.html': {
        'name': 'Dynalite Repair Sydney — Fault Finding & System Restoration',
        'description': 'Specialist Philips Dynalite repairs including DyNet bus diagnostics, processor replacement, keypad troubleshooting, and system restoration for commercial and strata buildings.',
        'serviceType': 'Dynalite Repair and Fault Finding'
    },
    'dynalite-not-working-sydney.html': {
        'name': 'Dynalite System Not Working — Emergency Diagnosis Sydney',
        'description': 'Emergency diagnostics for Dynalite systems that are completely non-responsive. Same-day DyNet bus analysis, processor checks, and hardware replacement.',
        'serviceType': 'Emergency Dynalite Diagnosis'
    },
    'dali-lighting-control-system-sydney.html': {
        'name': 'DALI Lighting Control System Sydney — Commissioning & Repair',
        'description': 'DALI and DALI-2 lighting control system commissioning, bus diagnostics, emergency lighting AFSS compliance testing, and BMS integration across Sydney.',
        'serviceType': 'DALI Lighting Control'
    },
    'afss-emergency-lighting-services.html': {
        'name': 'AFSS Emergency Lighting Compliance Testing Sydney',
        'description': 'Annual fire safety statement emergency lighting testing, 90-minute discharge tests, battery verification, and compliance documentation for NSW buildings.',
        'serviceType': 'AFSS Emergency Lighting Compliance'
    },
    'emergency-repair-sydney.html': {
        'name': 'Emergency Lighting Control Repair Sydney — Same Day Response',
        'description': 'Rapid emergency response for total C-Bus, Dynalite, DALI, and RAPIX lighting control system failures. Same-day service across Greater Sydney.',
        'serviceType': 'Emergency Lighting Control Repair'
    },
}

service_schema_template = {
    "@context": "https://schema.org",
    "@type": "Service",
    "provider": {
        "@type": "LocalBusiness",
        "name": "Sydney Automation Co.",
        "telephone": "+61422469739",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Menai",
            "addressRegion": "NSW",
            "postalCode": "2234",
            "addressCountry": "AU"
        }
    },
    "areaServed": {
        "@type": "City",
        "name": "Sydney",
        "containedInPlace": {"@type": "State", "name": "New South Wales"}
    }
}

for filename, svc_data in SERVICE_PAGES.items():
    fp = os.path.join(BASE, filename)
    c = read_file(fp)
    if not c:
        print(f"  SKIP (not found): {filename}")
        continue
    
    # Check if Service schema already exists
    if '"@type": "Service"' in c or '"@type":"Service"' in c:
        print(f"  SKIP (has Service): {filename}")
        continue
    
    schema = service_schema_template.copy()
    schema['name'] = svc_data['name']
    schema['description'] = svc_data['description']
    schema['serviceType'] = svc_data['serviceType']
    
    schema_json = json.dumps(schema, indent=2)
    schema_tag = f'<script type="application/ld+json">\n{schema_json}\n</script>'
    
    # Insert before </head>
    if '</head>' in c:
        c = c.replace('</head>', schema_tag + '\n</head>', 1)
        write_file(fp, c)
        print(f"  OK: {filename}")
    else:
        print(f"  FAIL: {filename}")


# ============================================================
# 3. PRODUCT SCHEMA (ItemList) for products.html
# ============================================================
print("\n=== 3. Product Schema (products.html) ===")

fp = os.path.join(BASE, 'products.html')
c = read_file(fp)
if c and 'ItemList' not in c:
    product_schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "C-Bus, Dynalite & RAPIX Product Catalogue",
        "description": "Complete range of Clipsal C-Bus, Signify Dynalite, and RAPIX lighting control products available through Sydney Automation Co.",
        "numberOfItems": "266",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Clipsal C-Bus 5500PC Network Interface", "description": "C-Bus network interface for Ethernet/USB connection to C-Bus Toolkit software"},
            {"@type": "ListItem", "position": 2, "name": "Clipsal C-Bus 5500PS Power Supply", "description": "C-Bus 2 power supply providing 5-11.5V DC to the C-Bus network"},
            {"@type": "ListItem", "position": 3, "name": "Clipsal C-Bus 5000C/T Dimmer Module", "description": "C-Bus dimmer module for incandescent and leading-edge LED loads"},
            {"@type": "ListItem", "position": 4, "name": "Clipsal C-Bus L5508D1A Dimmer Module", "description": "Next-generation 8-channel C-Bus dimmer for LED and resistive loads"},
            {"@type": "ListItem", "position": 5, "name": "Clipsal C-Bus Saturn KeyPad", "description": "Wall-mounted C-Bus keypad with programmable buttons and LED indicators"},
            {"@type": "ListItem", "position": 6, "name": "Dynalite DDBC1200 Processor", "description": "Main Dynalite system processor managing DyNet bus communication"},
            {"@type": "ListItem", "position": 7, "name": "Dynalite DDMC802 Dimmer Controller", "description": "8-channel dimmer controller for Dynalite lighting systems"},
            {"@type": "ListItem", "position": 8, "name": "Dynalite DDNG232 Network Gateway", "description": "DyNet network gateway for IP-based Dynalite system communication"},
            {"@type": "ListItem", "position": 9, "name": "Dynalite Antumbra Keypad", "description": "Premium wall-mounted touchscreen keypad for Dynalite systems"},
            {"@type": "ListItem", "position": 10, "name": "RAPIX Emergency Lighting Module", "description": "Emergency lighting control module for mandatory fire safety circuits"}
        ]
    }
    schema_json = json.dumps(product_schema, indent=2)
    schema_tag = f'<script type="application/ld+json">\n{schema_json}\n</script>'
    if '</head>' in c:
        c = c.replace('</head>', schema_tag + '\n</head>', 1)
        write_file(fp, c)
        print("  OK: Added ItemList/Product schema to products.html")
    else:
        print("  FAIL: products.html")
elif c:
    print("  SKIP: Product schema already exists")


print("\n=== All HowTo/Service/Product schema tasks complete ===")
