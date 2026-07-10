import re
import os

def update_file(filepath, updates):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for pattern, replacement in updates:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

cbus_updates = [
    (r'<title>.*?</title>', '<title>C-Bus Lights Stuck On? Same-Day Repairs Sydney | 0422 469 739</title>'),
    (r'<meta content="C-Bus Repair Sydney\. C-Bus system not working\? Accredited Clipsal C-Bus repair specialists in Sydney\. Call 0422 469 739\." name="description"/>', 
     '<meta content="C-Bus system stuck on or not responding? We are Accredited Clipsal C-Bus repair specialists in Sydney. Same-day emergency response. Call 0422 469 739." name="description"/>'),
    (r'<meta content="C-Bus Repair Sydney \| Same-Day Fault Finding &amp; Repair" name="twitter:title"/>',
     '<meta content="C-Bus Lights Stuck On? Same-Day Repairs Sydney | 0422 469 739" name="twitter:title"/>'),
    (r'<meta content="C-Bus Repair Sydney \| Clipsal Fault Finding Specialists" property="og:title"/>',
     '<meta content="C-Bus Lights Stuck On? Same-Day Repairs Sydney | 0422 469 739" property="og:title"/>')
]

dynalite_updates = [
    (r'<title>.*?</title>', '<title>Dynalite Keypad Not Working? Same-Day Repairs Sydney | 0422 469 739</title>'),
    (r'<meta content="Dynalite Repair Sydney\. Dynalite system not working\? Accredited Signify Dynalite repair specialists in Sydney\. Call 0422 469 739\." name="description"/>',
     '<meta content="Dynalite system stuck on or keypad not responding? We are Accredited Signify Dynalite repair specialists in Sydney. Same-day emergency response. Call 0422 469 739." name="description"/>'),
    (r'<meta content="Dynalite Repair Sydney \| Same-Day Fault Finding &amp; Repair" name="twitter:title"/>',
     '<meta content="Dynalite Keypad Not Working? Same-Day Repairs Sydney | 0422 469 739" name="twitter:title"/>'),
    (r'<meta content="Dynalite Repair Sydney \| Signify Fault Finding Specialists" property="og:title"/>',
     '<meta content="Dynalite Keypad Not Working? Same-Day Repairs Sydney | 0422 469 739" property="og:title"/>')
]

cbus_prog_updates = [
    (r'<title>.*?</title>', '<title>C-Bus Programmer Sydney | Clipsal Accredited Specialist | 0422 469 739</title>'),
    (r'<meta content="C-Bus Programmer Sydney\. Expert C-Bus programming for residential and commercial\. Clipsal Accredited C-Bus Programmer\. Call 0422 469 739\." name="description"/>',
     '<meta content="Need an Accredited C-Bus Programmer in Sydney? We specialize in complex C-Bus programming, fault finding and system upgrades. Same-day response. Call 0422 469 739." name="description"/>')
]

dynalite_prog_updates = [
    (r'<title>.*?</title>', '<title>Dynalite Programmer Sydney | Signify Accredited Specialist | 0422 469 739</title>'),
    (r'<meta content="Dynalite Programmer Sydney\. Expert Dynalite programming for commercial and residential\. Accredited Signify Dynalite Programmer\. Call 0422 469 739\." name="description"/>',
     '<meta content="Need an Accredited Dynalite Programmer in Sydney? We specialize in complex Dynalite programming, fault finding and system upgrades. Same-day response. Call 0422 469 739." name="description"/>')
]

products_updates = [
    (r'<title>.*?</title>', '<title>Buy C-Bus, Dynalite & RAPIX Parts Sydney | Sydney Automation Co</title>'),
    (r'<meta content="Purchase replacement C-Bus, Dynalite, and RAPIX lighting control parts in Sydney\. Fast dispatch, expert advice\." name="description"/>',
     '<meta content="Looking for replacement C-Bus, Dynalite, or RAPIX parts in Sydney? We supply hardware for all major lighting control systems. Fast dispatch & expert advice. Call 0422 469 739." name="description"/>')
]

update_file('cbus-repair-sydney.html', cbus_updates)
update_file('dynalite-repair-sydney.html', dynalite_updates)
update_file('c-bus-programmer-sydney.html', cbus_prog_updates)
update_file('dynalite-programmer-sydney.html', dynalite_prog_updates)
update_file('products.html', products_updates)

print("Title/Meta tags updated successfully.")
