import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))

BLUF_PARAGRAPHS = {
    "cbus-specialist-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To repair a Clipsal C-Bus lighting network that is dropping packets, failing to activate zones, or showing erratic channel behaviour, you must perform an RS-485 bus voltage analysis (normal range: 5–11.5V), verify correct network burden placement at each bus segment end, clear any colliding Pascal logic scripts in C-Bus Toolkit, and confirm the 5500PS power supply is delivering stable voltage to the bus.</strong></div>',
    
    "cbus-repair-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To repair a Clipsal C-Bus system that is not responding, channels are flashing, or scenes are failing to trigger, a specialist must diagnose the RS-485 bus with a network analyser, verify the 5500PC interface connectivity, check individual module status via C-Bus Toolkit, and test each relay or dimmer output for correct operation.</strong></div>',
    
    "cbus-fault-finding-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To diagnose C-Bus faults in Sydney, start by measuring bus voltage at the 5500PS power supply (should read 5–11.5V DC), check the 5500PC network interface LED status, use C-Bus Toolkit to scan for address conflicts or offline modules, and verify network burden placement at each segment end.</strong></div>',
    
    "dynalite-fault-finding-sydney-common-faults.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To diagnose Dynalite system faults, you must verify DyNet bus communication voltage (9.6–42V DC), check for address conflicts using Dynalite EnvisionProject software, confirm the DDBC1200 processor is not in fault mode, and inspect all DyNet wiring for loose or corroded connections.</strong></div>',
    
    "dynalite-repair-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To repair a Philips Dynalite system that is unresponsive or experiencing communication errors, a specialist must connect via Dynalite EnvisionProject software, verify DyNet bus voltage and termination, check processor health on the DDBC1200, and re-address any conflicting devices on the network.</strong></div>',
    
    "dynalite-not-working-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">If your Dynalite system is completely non-responsive, first check that the DDBC1200 processor has power and is not in fault mode, verify DyNet bus voltage at any keypad (9.6–42V DC), power-cycle the processor for 30 seconds, and if keypads remain dead, test the DyNet bus cable for continuity between the processor and the furthest device.</strong></div>',
    
    "emergency-repair-sydney.html": '<div style="background:#3d1515;border-left:4px solid #ff4444;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">For a total lighting control system failure — C-Bus, Dynalite, DALI, or RAPIX — the emergency diagnostic protocol is: verify mains power to the control equipment, check power supply output voltages, test bus communication with a specialist analyser, and if the processor is unresponsive, power-cycle for 30 seconds. Same-day emergency service available on 0422 469 739.</strong></div>',
    
    "dali-lighting-control-system-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To commission or repair a DALI lighting control system, you must verify the DALI bus voltage (16V DC nominal), assign short addresses to each DALI ballast using a DALI configurator, test emergency lighting AFSS compliance circuits, and confirm BMS integration communication if applicable.</strong></div>',
    
    "afss-emergency-lighting-services.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To complete AFSS emergency lighting compliance testing in NSW, you must perform a 90-minute discharge test on all emergency luminaires, verify battery backup capacity meets AS 2293 standards, test DALI emergency lighting self-test functionality, and produce a compliant fire safety statement for your building.</strong></div>',
    
    "cbus-upgrade-sydney.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">To upgrade a Clipsal C-Bus system, you must assess the existing hardware generation (C-Bus Classic vs C-Bus 2), migrate legacy 5000-series modules to current L55-series hardware, reprogram scenes and schedules in C-Bus Toolkit, and optionally integrate mobile app control via the C-Bus Home Control interface.</strong></div>',
    
    "services.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">Sydney Automation Co. provides specialist lighting control services for Clipsal C-Bus, Signify Dynalite, DALI/DALI-2, and RAPIX emergency lighting systems. Every engagement includes RS-485 bus diagnostics, system programming from C-Bus Toolkit or Dynalite EnvisionProject software, and a full database backup handover.</strong></div>',
    
    "services-hub.html": '<div style="background:#132647;border-left:4px solid #f07020;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px"><strong style="color:#f0c040;font-size:1.05rem">Browse our complete service catalogue covering C-Bus programming and fault finding, Dynalite system design and repair, DALI-2 emergency lighting compliance, RAPIX programming, lighting control maintenance contracts, and emergency same-day repair across Greater Sydney.</strong></div>',
}

def inject_bluf(filepath, bluf_html):
    """Inject BLUF paragraph before <div class="page"> in the file."""
    for enc in ('utf-8', 'latin1', 'cp1252'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    # Check if BLUF already exists
    if 'border-left:4px solid #f07020' in content and 'To repair' in content:
        print(f"  SKIP (BLUF already exists): {os.path.basename(filepath)}")
        return False
    
    if 'border-left:4px solid #f07020' in content and 'To diagnose' in content:
        print(f"  SKIP (BLUF already exists): {os.path.basename(filepath)}")
        return False
    
    if 'border-left:4px solid #ff4444' in content and 'total lighting control system failure' in content:
        print(f"  SKIP (BLUF already exists): {os.path.basename(filepath)}")
        return False
    
    if 'border-left:4px solid #f07020' in content and 'Sydney Automation Co. provides specialist' in content:
        print(f"  SKIP (BLUF already exists): {os.path.basename(filepath)}")
        return False
    
    if 'border-left:4px solid #f07020' in content and 'Browse our complete service' in content:
        print(f"  SKIP (BLUF already exists): {os.path.basename(filepath)}")
        return False
    
    # Strategy 1: Insert before <div class="page"> (most common pattern)
    if '<div class="page">' in content:
        content = content.replace(
            '<div class="page">',
            bluf_html + '\n<div class="page">',
            1  # Only first occurrence
        )
        with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
            f.write(content)
        print(f"  OK (before div.page): {os.path.basename(filepath)}")
        return True
    
    # Strategy 2: Insert before <div class="hero" (pages where hero is outside div.page)
    hero_match = re.search(r'(<div class="hero"[^>]*>)', content)
    if hero_match:
        content = content.replace(
            hero_match.group(1),
            bluf_html + '\n' + hero_match.group(1),
            1
        )
        with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
            f.write(content)
        print(f"  OK (before hero div): {os.path.basename(filepath)}")
        return True
    
    # Strategy 3: Insert before <section class="hero">
    hero_match = re.search(r'(<section class="hero"[^>]*>)', content)
    if hero_match:
        content = content.replace(
            hero_match.group(1),
            bluf_html + '\n' + hero_match.group(1),
            1
        )
        with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
            f.write(content)
        print(f"  OK (before hero section): {os.path.basename(filepath)}")
        return True
    
    print(f"  FAIL (no insertion point found): {os.path.basename(filepath)}")
    return False


def read_file(filepath):
    for enc in ('utf-8', 'latin1', 'cp1252'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    return None


print("=== BLUF Injection Script ===\n")

success = 0
failed = 0

for filename, bluf in BLUF_PARAGRAPHS.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print(f"  FILE NOT FOUND: {filename}")
        failed += 1
        continue
    
    if inject_bluf(filepath, bluf):
        success += 1
    else:
        failed += 1

print(f"\nDone: {success} injected, {failed} failed/skipped")
