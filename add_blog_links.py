import re
import os

BASE = "C:\\Users\\gaska\\OneDrive\\Documents\\Sydney-Automation-Co"

PAGES = {
    "cbus-repair-sydney.html": {
        "heading": "C-Bus Technical Guides &amp; Troubleshooting",
        "links": [
            ("blog-cbus-not-working-repair-guide.html", "C-Bus Not Working? A Practical Troubleshooting Guide for Sydney Homes", "Step-by-step C-Bus fault diagnosis guide covering power supply checks, network errors, and common configuration issues."),
            ("blog-cbus-5500pc-software-crash-sydney.html", "C-Bus 5500PC Software Crash Recovery", "How to recover a C-Bus 5500PC after a software crash, including firmware reflash and project restore procedures."),
            ("blog-cbus-dimmer-module-failure-sydney.html", "C-Bus Dimmer Module Failure: Signs &amp; Solutions", "Common C-Bus dimmer failure symptoms, error codes, and repair options for L5504DIM and 5508RVF modules."),
            ("blog-cbus-network-noise-interference-sydney.html", "C-Bus Network Noise &amp; Interference Fixes", "Diagnosing C-Bus network burden issues, electrical noise interference, and bus communication crashes."),
            ("blog-cbus-5508rvf-blinking-red-led-sydney.html", "C-Bus 5508RVF Blinking Red LED Codes", "Decode 5508RVF blinking LED patterns to quickly identify C-Bus hardware faults and module failures."),
            ("blog-cbus-ethernet-interface-offline-sydney.html", "C-Bus Ethernet Interface Offline: Fix", "Troubleshoot C-Bus Ethernet interface (5500CN) going offline, including IP configuration and network diagnosis."),
            ("blog-cbus-power-supply-overheating-sydney.html", "C-Bus Power Supply Overheating: Causes &amp; Fix", "Identify and fix C-Bus 5500PS and 5100PS power supply overheating, humming, and voltage drop issues."),
            ("blog-cbus-schedule-timeclock-drift-sydney.html", "C-Bus Schedule &amp; Timeclock Drift Fix", "Fix C-Bus schedule drift and clock sync problems that cause lights to turn on/off at wrong times."),
        ]
    },
    "dynalite-repair-sydney.html": {
        "heading": "Dynalite Technical Guides &amp; Troubleshooting",
        "links": [
            ("blog-dynalite-repairs-electrician-sydney.html", "Dynalite Repairs: Why You Need a Specialist Programmer, Not Just an Electrician", "Understand why Dynalite system repair requires accredited specialist knowledge beyond standard electrical work."),
            ("blog-dynalite-ddng232-config-loss-sydney.html", "Dynalite DDNG232 Configuration Lost? Recovery", "Step-by-step recovery guide for Dynalite DDNG232 units that have lost their configuration or programming."),
            ("blog-dynalite-ddbc1200-error-codes-sydney.html", "Dynalite DDBC1200 Error Codes Explained", "Comprehensive guide to Dynalite DDBC1200 error codes — what they mean and how to resolve each fault."),
            ("blog-dynalite-dtk-connection-sydney.html", "Dynalite DTK Connection Issues: Troubleshoot", "Troubleshoot Dynalite DTK (Designer Toolkit) connection problems, USB driver issues, and network detection failures."),
            ("blog-dynalite-network-termination-sydney.html", "Dynalite Network Burden Termination Guide", "Proper DyNet network burden termination to prevent communication crashes and intermittent faults."),
            ("blog-dynalite-4-channel-dimmer-repair-sydney.html", "Dynalite 4-Channel Dimmer Module Repair", "Diagnose and repair Dynalite 4-channel dimmer modules including DDBC1200 and DDM series hardware faults."),
            ("blog-dynalite-power-failure-recovery-sydney.html", "Dynalite Power Failure Recovery Procedures", "Steps to recover a Dynalite system after a power outage, including sequencer restart and schedule restoration."),
            ("blog-dynalite-dimmer-repair-vs-replace-sydney.html", "Dynalite Dimmer Module: Repair or Replace?", "Compare repair vs replacement costs for faulty Dynalite dimmer modules and series B hardware upgrades."),
        ]
    },
    "emergency-lighting-compliance-afss-sydney.html": {
        "heading": "AFSS, DALI-2 &amp; Emergency Lighting Guides",
        "links": [
            ("blog-afss-inspection-checklist-sydney.html", "AFSS Emergency Lighting Inspection Checklist", "Complete AFSS emergency lighting inspection checklist covering exit signs, spitfires, battens, and log book requirements."),
            ("blog-afss-emergency-log-book-app-sydney.html", "AFSS Emergency Lighting Log Book App", "Digital log book solutions for AFSS emergency lighting compliance and annual inspection records."),
            ("blog-dali-2-compliance-guide-sydney-building-managers.html", "DALI-2 Compliance Guide for Sydney Building Managers", "Essential DALI-2 compliance guide for building managers covering NCC 2022, AS/NZS 2293, and emergency testing requirements."),
            ("blog-ncc-2022-compliance-lighting-sydney.html", "Navigating NCC 2022 Compliance for Lighting", "How NCC 2022 changes affect emergency lighting compliance, AFSS requirements, and building certification in NSW."),
            ("blog-dali2-emergency-test-procedures-sydney.html", "DALI-2 Emergency Lighting Test Procedures", "Step-by-step DALI-2 emergency lighting test procedures including self-test, central test, and compliance reporting."),
            ("blog-dali2-diagnostics-fault-finding-sydney.html", "DALI-2 Diagnostics &amp; Fault Finding Guide", "Diagnose DALI-2 bus faults, address conflicts, and driver communication errors using commissioning tools."),
            ("blog-emergency-lighting-log-book-sydney.html", "Emergency Lighting Log Book Requirements", "What NSW building managers need to know about emergency lighting log books, monthly tests, and AFSS documentation."),
            ("blog-dali2-central-vs-distributed-emergency-sydney.html", "DALI-2 Central vs Distributed Emergency Lighting", "Compare central vs distributed DALI-2 emergency lighting architectures for compliance, cost, and maintenance."),
        ]
    }
}

def section_html(heading, links):
    items = ""
    for filename, title, desc in links:
        items += f"""
<div style="background:#13274a;border-radius:12px;padding:24px;border:1px solid rgba(240,112,32,0.15);transition:transform 0.2s,border-color 0.2s;" onmouseover="this.style.transform='translateY(-2px)';this.style.borderColor='#f07020'" onmouseout="this.style.transform='';this.style.borderColor='rgba(240,112,32,0.15)'">
<h3 style="margin:0 0 8px 0;font-family:'Barlow Condensed',sans-serif;font-size:20px;font-weight:700;line-height:1.3;"><a href="/{filename}" style="color:#f07020;text-decoration:none;">{title}</a></h3>
<p style="color:#a8c0e0;font-size:14px;margin:0;line-height:1.6;">{desc}</p>
</div>"""
    return f"""
<!-- ===== RELATED BLOG ARTICLES ===== -->
<section style="background:#0e1f3d;padding:80px 0;border-top:1px solid rgba(240,112,32,0.1);">
<div class="container" style="max-width:1200px;margin:0 auto;padding:0 24px;">
<div style="text-align:center;margin-bottom:48px;">
<span style="color:#f07020;font-weight:700;letter-spacing:3px;text-transform:uppercase;font-size:12px;display:block;margin-bottom:12px;">RELATED GUIDES</span>
<h2 style="color:#fff;font-size:clamp(32px,5vw,46px);margin:0;font-family:'Barlow Condensed',sans-serif;font-weight:900;line-height:1.1;">{heading}</h2>
<div style="width:60px;height:4px;background:#f07020;margin:24px auto;"></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;">{items}
</div>
</div>
</section>
<!-- ===== END RELATED BLOG ARTICLES ===== -->
"""

MARKER = "<!-- ===== PREMIUM TESTIMONIALS CAROUSEL ===== -->"

results = {}
for page, cfg in PAGES.items():
    path = os.path.join(BASE, page)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    insert_html = section_html(cfg["heading"], cfg["links"])
    new_content = content.replace(MARKER, insert_html + "\n" + MARKER, 1)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    results[page] = len(cfg["links"])

for page, count in results.items():
    print(f"[OK] {page}: {count} blog links added")
print(f"\nTotal: {sum(results.values())} blog links across {len(results)} pages")
