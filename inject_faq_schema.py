import os
import json
import re

# ============================================================
# SCRIPT 1: inject_faq_schema.py
# Injects FAQPage JSON-LD into top 20 high-priority service pages
# ============================================================

# FAQ data per page type
faq_sets = {
    'c-bus-programmer-sydney.html': [
        {"q": "What is Clipsal C-Bus and why do I need an accredited programmer?", "a": "Clipsal C-Bus is Australia's leading wired lighting automation system, using Cat5e bus communication to control lights, fans, and scenes. Accredited programmers have direct access to C-Bus Toolkit software and genuine Schneider Electric hardware, ensuring correct commissioning, DALI integration, and database backups that general electricians cannot provide."},
        {"q": "How quickly can Sydney Automation Co. respond to a C-Bus emergency?", "a": "We offer 2-hour emergency dispatch across Greater Sydney for critical system failures. For same-day urgent faults and scheduled maintenance, we typically respond within 4 business hours of your call."},
        {"q": "Can you repair a C-Bus system installed by another company?", "a": "Yes. We specialize in orphaned system takeovers, database recovery, and password lockout bypasses for all C-Bus systems regardless of the original installer. We also provide free second opinion audits on existing contractor quotes."},
        {"q": "What is the cost of C-Bus programming in Sydney?", "a": "A $200 diagnostic fee applies to all callouts — this covers travel, on-site fault diagnosis with C-Bus Toolkit, and a written report. It is not credited toward further work. Subsequent repair or programming is charged at $150/hr with a 3-hour minimum. Use our interactive cost calculator on our website for an instant estimate."},
    ],
    'dynalite-programmer-sydney.html': [
        {"q": "What is Signify Dynalite and how does it differ from C-Bus?", "a": "Signify Dynalite (formerly Philips Dynalite) is a premium architectural lighting control system using RS-485 DyNet serial communication. It excels in hospitality, luxury hotels, and commercial towers requiring sophisticated multi-scene dimming and elegant Antumbra keypad aesthetics. C-Bus uses a Cat5e wired bus and is the dominant system in Australian residential and commercial buildings."},
        {"q": "My Dynalite keypad is unresponsive — what should I check first?", "a": "An unresponsive Dynalite Antumbra or DLight keypad typically indicates a DyNet bus power supply failure, a severed RS-485 cable, or a corrupt controller firmware. Check that the 'DyNet' LED on your primary DDBC or DDRC controller is pulsing green. If not, call our emergency line or visit cbusnotworking.com.au for immediate guidance."},
        {"q": "Can you recover a Dynalite database if the original programmer is unavailable?", "a": "Yes. We utilize advanced diagnostic tools to extract Dynalite programming directly from controller firmware, bypassing lost password barriers. We then provide you with a clean, unencrypted EnvisionProject database backup."},
        {"q": "Do you service Dynalite systems outside of Sydney?", "a": "Yes. We provide accredited Dynalite programming across Regional NSW including the Southern Highlands (Bowral, Mittagong), Illawarra (Wollongong, Kiama), and Central Coast (Terrigal, Avoca Beach)."},
    ],
    'c-bus-repairs-sydney.html': [
        {"q": "What are the most common C-Bus repair faults you fix in Sydney?", "a": "The most common faults we repair include: fused relay contactors in DIN-rail enclosures causing lights to stick on, flashing red PCI interface indicator LEDs indicating network clock failures, buzzing relay modules with overheated contactors, and C-Bus Toolkit software connection failures due to COM port driver conflicts."},
        {"q": "How do I know if my C-Bus relay needs replacing?", "a": "Key symptoms of a failing C-Bus relay include: a loud buzzing or chattering noise from the switchboard enclosure, a specific lighting circuit that cannot be turned off or on via keypads, an orange channel status LED that flickers erratically, or a burning plastic smell from the DIN-rail enclosure."},
        {"q": "Can you replace obsolete C-Bus 5000 series relays?", "a": "Yes. We specialize in drop-in replacements for discontinued Clipsal C-Bus 5000 series relay units. We install the latest Schneider Electric C-Bus SpaceLogic series controllers and transfer your existing database programming with zero operational downtime."},
        {"q": "Do you provide emergency C-Bus repairs on weekends?", "a": "Yes. We offer 2-hour emergency dispatch across Greater Sydney for critical C-Bus failures. For after-hours emergency guidance, visit our dedicated portal at cbusnotworking.com.au for immediate technical support."},
    ],
    'afss-testing-sydney.html': [
        {"q": "What is an AFSS annual fire safety statement for lighting?", "a": "An Annual Fire Safety Statement (AFSS) is a mandatory annual certification required by NSW councils confirming that all essential fire safety measures in a building — including emergency and exit lighting — have been inspected, tested, and are operating correctly to relevant Australian Standards (AS/NZS 2293)."},
        {"q": "What happens if my DALI emergency lighting fails an AFSS test?", "a": "If your DALI emergency lighting fails an AFSS inspection, your building will receive a non-compliance notice requiring immediate rectification. Common failures include DALI line address conflicts, failed emergency ballasts not responding to battery discharge tests, and broken communication loops between the DALI controller and individual fittings."},
        {"q": "Can you fix DALI emergency lighting faults before an AFSS inspection?", "a": "Yes. We provide direct, accredited DALI-2 commissioning and emergency ballast address resolution ahead of AFSS inspections for commercial buildings, strata complexes, and warehouses across Greater Sydney. We also provide a written DALI discharge test compliance report."},
        {"q": "How quickly can you resolve an AFSS emergency lighting failure?", "a": "For urgent AFSS compliance rectification, we typically provide same-day or next-day emergency dispatch across Sydney. Contact us on 0422 469 739 or visit cbusnotworking.com.au for immediate emergency support."},
    ],
    'cbus-dynalite-fault-codes-sydney.html': [
        {"q": "What does a flashing red LED on my C-Bus PCI interface mean?", "a": "A flashing red LED on a Clipsal C-Bus PC Interface (5500PC / 5500PCI) indicates a critical network clock collapse or network burden failure. Without a stable system clock, all smart keypads and touchscreens across the building become unresponsive. This requires immediate accredited diagnosis and rectification."},
        {"q": "Why is my C-Bus relay making a buzzing noise?", "a": "A buzzing or chattering noise from a C-Bus relay enclosure indicates severe internal contactor arcing and carbon buildup. This creates extreme electrical resistance, excessive heat generation, and represents a serious thermal fire risk within your switchboard. The relay module requires urgent drop-in replacement."},
        {"q": "My C-Bus Toolkit software cannot connect — how do I fix this?", "a": "Common causes of C-Bus Toolkit connection failures include: the C-Gate Server background service has crashed (check Windows Services), the USB-to-Serial adapter COM port number does not match the Toolkit settings, or the physical PC Interface is not receiving 22V DC bus power. Visit cbusnotworking.com.au for step-by-step troubleshooting."},
        {"q": "What causes a Dynalite keypad to go completely unresponsive?", "a": "An unresponsive Signify Dynalite keypad is typically caused by: a failed 15V DC power supply within the central DDBC or DDRC controller, a broken Cat5e DyNet RS-485 bus cable, or a firmware lockup caused by an electrical storm surge. Check that the DyNet indicator LED on your controller is pulsing steadily."},
    ],
    'strata-lighting-maintenance-nsw.html': [
        {"q": "What C-Bus and Dynalite maintenance services do you provide for strata buildings?", "a": "We provide comprehensive strata lighting maintenance including: common area C-Bus relay and dimmer inspections, basement carpark DALI sensor audits, external sensor corrosion treatments, timer schedule optimization to reduce electricity levies, and fixed-price preventative maintenance agreements for body corporates and strata managers across NSW."},
        {"q": "How can strata buildings reduce electricity costs with smart lighting automation?", "a": "By optimizing C-Bus and Dynalite timer schedules and motion sensor sensitivity thresholds, we can reduce strata common area electricity consumption by 30-60%. Empty corridors, stairwells, and carparks dim automatically during low-traffic hours while maintaining safety compliance."},
        {"q": "Do you provide fixed-price maintenance contracts for strata managers?", "a": "Yes. We offer tailored, fixed-price preventative maintenance agreements specifically designed for strata management firms operating across NSW. These include scheduled system audits, written health reports, and priority emergency dispatch for body corporates."},
        {"q": "Our carpark lighting is stuck on all night — what is causing this?", "a": "Carpark lighting stuck permanently on is typically caused by a failed C-Bus relay contactor welded in the 'closed' position, or a DALI motion sensor that has lost communication with the head-end controller. We can resolve this fault with a same-day fixed-price repair."},
    ],
    'warehouse-lighting-automation-sydney.html': [
        {"q": "What lighting control systems do you use for warehouses in Western Sydney?", "a": "We install and repair Clipsal C-Bus relay controllers, Signify Dynalite DALI-2 lighting networks, and motion sensor automation systems for high-bay warehouse environments across Western Sydney including Wetherill Park, Erskine Park, Eastern Creek, and Arndell Park logistics corridors."},
        {"q": "How can warehouse lighting automation reduce energy costs?", "a": "By programming C-Bus and DALI motion sensor networks to dim empty warehouse aisles automatically, we typically reduce warehouse lighting energy consumption by 40-70%. The return on investment for automation upgrades is frequently achieved within 12-18 months through electricity savings alone."},
        {"q": "What causes warehouse high-bay lighting contactors to burn out?", "a": "High-bay lighting circuits carry substantial inductive loads from hundreds of LED and metal halide fixtures. Over years of continuous cycling, standard C-Bus relay contactors experience severe arcing and carbon buildup, eventually burning out or welding shut. Heavy-duty industrial-grade contactor replacements and surge protection are the definitive solution."},
        {"q": "Do you service DALI emergency lighting systems in warehouses?", "a": "Yes. We provide full DALI-2 emergency lighting commissioning, ballast conflict resolution, and AFSS compliance audit support for warehouse and logistics facilities across Western Sydney. We eliminate line faults and ensure 100% annual discharge test compliance."},
    ],
    'building-managers-lighting-control-nsw.html': [
        {"q": "What accredited lighting control services do you provide for building managers?", "a": "We provide commercial building managers with direct accredited C-Bus and Signify Dynalite head-end software programming, DALI emergency lighting compliance management, after-hours schedule optimization, relay and hardware replacements, and comprehensive database backup and documentation services across NSW."},
        {"q": "Can you help improve our building's NABERS energy rating?", "a": "Yes. By implementing precise after-hours sensor timeout profiles, automated daylight harvesting via DALI photosensors, and eliminating conflicting lighting schedules that leave office floors illuminated overnight, we directly reduce baseline energy consumption and improve your building's NABERS energy efficiency rating."},
        {"q": "Our head-end C-Bus software is locked — can you recover access?", "a": "Yes. We specialize in C-Bus and Dynalite database recovery and password lockout bypasses for building management teams. We extract the active programming database directly from hardware controllers, completely bypassing lost software credentials without wiping your building's settings."},
        {"q": "Do you provide 24/7 emergency support for commercial buildings?", "a": "We offer 2-hour emergency dispatch for critical C-Bus and Dynalite system failures in commercial buildings across Greater Sydney. For after-hours technical guidance, facility teams can access immediate support through our dedicated emergency portal at cbusnotworking.com.au."},
    ],
    'electrician-partner-cbus-dynalite-programming.html': [
        {"q": "How does your white-label electrician partner program work?", "a": "Our partner program is simple: you install the C-Bus or Dynalite hardware and pull the bus cabling, and we provide accredited head-end software programming on your behalf. We arrive on site and commission the system, you deliver a flawless project to your client and retain 100% of the client relationship. We can work under your company brand if preferred."},
        {"q": "What types of electrical jobs can benefit from your programming partnership?", "a": "Any residential, commercial, strata, or warehouse electrical project involving Clipsal C-Bus, Signify Dynalite, or DALI-2 systems can benefit from our partnership. This includes new home builds, commercial tenancy fit-outs, strata common area upgrades, and warehouse lighting control installations."},
        {"q": "Do you offer a referral fee to electrical contractors?", "a": "Yes. We offer competitive referral arrangements for licensed electrical contractors who introduce new programming clients. Contact us on 0422 469 739 to discuss our current partner program terms and referral fee schedule."},
        {"q": "Can you provide accredited C-Bus programming on short notice?", "a": "Yes. We provide same-day and next-day accredited programming dispatch for electrical contractors under time pressure to achieve practical completion on commercial and residential projects. Call 0422 469 739 for urgent partner dispatch scheduling."},
    ],
    'lighting-automation-cost-calculator-sydney.html': [
        {"q": "How much does C-Bus programming cost in Sydney?", "a": "A $200 diagnostic fee applies to all callouts — this covers travel, on-site fault finding, and a written report. It is not credited toward further work. Subsequent repair or programming is charged at $150/hr with a 3-hour minimum ($450). All pricing is transparent and scope-defined before works commence. Use our interactive calculator on this page for an instant estimate."},
        {"q": "How much does a Dynalite system repair cost in Sydney?", "a": "A $200 diagnostic fee applies to all Dynalite callouts. This covers travel, on-site fault diagnosis, and a written report. It is not credited toward further work. Subsequent repair work is $150/hr with a 3-hour minimum. DyNet bus power supply replacements, controller firmware recovery, and database restoration are scoped after the diagnostic assessment."},
        {"q": "Do you provide fixed-price quotes for lighting automation works?", "a": "Yes. All Sydney Automation Co. works are provided on a fixed-price, transparent basis. We do not charge open-ended hourly billing rates. After an initial on-site diagnostic assessment, we provide a written fixed-price scope before commencing any programming or hardware replacement works."},
        {"q": "Is emergency after-hours C-Bus repair available, and at what cost?", "a": "Yes. We offer 2-hour emergency dispatch across Greater Sydney for critical lighting system failures. Emergency dispatch works carry a priority surcharge above standard rates. For immediate emergency cost guidance and dispatch booking, call 0422 469 739 or visit cbusnotworking.com.au."},
    ],
}

# Priority pages for FAQ injection (also include the top suburb pages)
priority_pages = list(faq_sets.keys()) + [
    'architects-consultants-lighting-specification-sydney.html',
    'orphaned-cbus-dynalite-system-takeover-sydney.html',
    'cbus-dynalite-second-opinion-quote-match-sydney.html',
    'sydney-lighting-automation-contractor-comparison.html',
    'cbus-pci-interface-blinking-red-sydney.html',
    'cbus-relay-making-buzzing-noise-sydney.html',
    'dynalite-dlight-keypad-unresponsive-sydney.html',
    'cbus-5500pc-network-bridge-failure-sydney.html',
    'cbus-toolkit-software-cannot-connect-sydney.html',
]

# Generic FAQ for pages without specific FAQ sets
generic_faq = [
    {"q": "What accredited C-Bus and Dynalite services do you provide in this area?", "a": "Sydney Automation Co. provides comprehensive accredited Clipsal C-Bus and Signify Dynalite services including head-end software programming, relay and dimmer replacements, DALI-2 emergency lighting commissioning, keypad upgrades, database recovery, and fixed-price preventative maintenance contracts across Greater Sydney and Regional NSW."},
    {"q": "How quickly can you respond to an emergency lighting fault?", "a": "We offer 2-hour emergency dispatch across Greater Sydney for critical C-Bus and Dynalite system failures. For immediate after-hours technical guidance, visit our dedicated emergency portal at cbusnotworking.com.au."},
    {"q": "Do you provide fixed-price programming and repairs?", "a": "Yes. All works are provided on a transparent, fixed-price basis. We do not charge open-ended hourly billing. After an on-site diagnostic assessment, we provide a written fixed-price scope before commencing any works."},
    {"q": "Can you recover a C-Bus or Dynalite system if the original programmer is unavailable?", "a": "Yes. We specialize in orphaned system takeovers, extracting programming databases directly from hardware controllers and providing you with a clean, unencrypted backup — completely bypassing lost password barriers without wiping your settings."},
]

injected = 0
skipped = 0

for page in priority_pages:
    if not os.path.exists(page):
        skipped += 1
        continue
        
    faqs = faq_sets.get(page, generic_faq)
    
    # Build FAQPage JSON-LD
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq["a"]
                }
            }
            for faq in faqs
        ]
    }
    
    faq_json = json.dumps(faq_schema, indent=2, ensure_ascii=False)
    faq_script = f'\n<script type="application/ld+json">\n{faq_json}\n</script>\n'
    
    with open(page, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if FAQ schema already injected
    if '"FAQPage"' in content:
        skipped += 1
        continue
    
    # Inject before </head>
    if '</head>' in content:
        content = content.replace('</head>', faq_script + '</head>', 1)
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        injected += 1
        print(f"FAQ injected: {page}")
    else:
        skipped += 1

print(f"\nSUCCESS: FAQ Schema injected into {injected} pages. Skipped: {skipped}.")
