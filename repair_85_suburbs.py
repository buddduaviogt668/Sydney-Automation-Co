import os
import re

# Master templates
CBUS_MASTER = 'c-bus-programmer-sydney.html'
DYN_MASTER = 'dynalite-programmer-sydney.html'

with open(CBUS_MASTER, 'r', encoding='utf-8') as f:
    cbus_content = f.read()

with open(DYN_MASTER, 'r', encoding='utf-8') as f:
    dyn_content = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
corrupted_files = []

for f in html_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        if 'automationco.com.au' in content and 'sydneyautomationco.com.au' not in content:
            corrupted_files.append(f)
        elif 'Automation Co.' in content and 'Sydney Automation Co.' not in content:
            if f not in corrupted_files:
                corrupted_files.append(f)

print(f"Found {len(corrupted_files)} corrupted files to repair and normalize.")

def repair_file(filename, is_cbus, sub_slug, sub_title):
    master = cbus_content if is_cbus else dyn_content
    
    # 1. Title
    if is_cbus:
        new_title = f"<title>C-Bus Programmer {sub_title} | Accredited Clipsal Specialist</title>"
        master = re.sub(r'<title>.*?</title>', new_title, master)
    else:
        new_title = f"<title>Accredited Signify Dynalite Programmer {sub_title} | System Design &amp; Repairs</title>"
        master = re.sub(r'<title>.*?</title>', new_title, master)
        
    # 2. Meta description
    if is_cbus:
        new_desc = f'<meta content="C-Bus Programmer {sub_title}. Accredited C-Bus Programmer based in Menai, Sutherland Shire. C-Bus fault finding, programming, commissioning and system design across {sub_title}. Call 0422 469 739." name="description"/>'
        master = re.sub(r'<meta content="[^"]+" name="description"/>', new_desc, master)
    else:
        new_desc = f'<meta content="Signify Dynalite Programmer {sub_title}. Accredited Signify Dynalite System Designer based in Menai, Sutherland Shire. Specialist fault finding, repairs and programming across {sub_title}. Call 0422 469 739." name="description"/>'
        master = re.sub(r'<meta content="[^"]+" name="description"/>', new_desc, master)

    # 3. Canonical
    new_canonical = f'<link rel="canonical" href="https://sydneyautomationco.com.au/{filename.replace(".html", "")}"/>'
    master = re.sub(r'<link rel="canonical" href="[^"]+"/>', new_canonical, master)

    # 4. OG tags
    new_og_url = f'<meta content="https://sydneyautomationco.com.au/{filename.replace(".html", "")}" property="og:url"/>'
    master = re.sub(r'<meta content="[^"]+" property="og:url"/>', new_og_url, master)
    
    clean_title = new_title.replace("<title>", "").replace("</title>", "")
    new_og_title = f'<meta content="{clean_title}" property="og:title"/>'
    master = re.sub(r'<meta content="[^"]+" property="og:title"/>', new_og_title, master)
    
    clean_desc = re.search(r'content="([^"]+)"', new_desc).group(1)
    new_og_desc = f'<meta content="{clean_desc}" property="og:description"/>'
    master = re.sub(r'<meta content="[^"]+" property="og:description"/>', new_og_desc, master)

    # 5. Geo placename
    new_geo = f'<meta content="Menai, Sutherland Shire, {sub_title}" name="geo.placename"/>'
    master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', new_geo, master)

    # 6. Schema LocalBusiness
    # Replace url and areaServed in LocalBusiness
    # We know LocalBusiness is the first schema script or has "@type": "LocalBusiness"
    master = re.sub(r'"url": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"url": "https://sydneyautomationco.com.au/{filename.replace(".html", "")}"', master)
    master = re.sub(r'"url": "https://sydneyautomationco.com.au/dynalite-programmer-sydney"', f'"url": "https://sydneyautomationco.com.au/{filename.replace(".html", "")}"', master)
    master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{sub_title}"', master)

    # 7. Schema BreadcrumbList
    # Replace name and item for position 2
    if is_cbus:
        master = re.sub(r'"name": "C-Bus Programmer Sydney"', f'"name": "C-Bus Programmer {sub_title}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"item": "https://sydneyautomationco.com.au/{filename.replace(".html", "")}"', master)
    else:
        master = re.sub(r'"name": "Signify Dynalite Programmer Sydney"', f'"name": "Signify Dynalite Programmer {sub_title}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/dynalite-programmer-sydney"', f'"item": "https://sydneyautomationco.com.au/{filename.replace(".html", "")}"', master)

    # 8. H1 and Lead
    if is_cbus:
        new_h1 = f'<h1>C-Bus Programmer<br/><span class="accent">{sub_title}</span></h1>'
        master = re.sub(r'<h1>C-Bus Programming<br/><span class="accent">&amp; Commissioning</span></h1>', new_h1, master)
        new_lead = f'<p class="lead">Accredited C-Bus Programmers. Same-day fault finding. Fixed-price programming. Based in Menai — covering all of <span style="color:#fff; font-weight:700;">{sub_title}</span>.</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)
    else:
        new_h1 = f'<h1>Signify Dynalite Programmer<br/><span class="accent">{sub_title}</span></h1>'
        master = re.sub(r'<h1>Signify Dynalite Programming<br/><span class="accent">.*?Sydney</span></h1>', new_h1, master, flags=re.DOTALL)
        new_lead = f'<p class="lead">Accredited Signify Dynalite System Designers. Most Automation Specialists can\'t touch Signify Dynalite faults without the software. Based in Menai, we provide direct specialist same-day service across <span style="color:#fff; font-weight:700;">{sub_title}</span>.</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)

    # 9. Main content body localization (specific headings/paragraphs)
    master = master.replace('<h3>Based in Menai — All of Sydney</h3>', f'<h3>Based in Menai — All of {sub_title}</h3>')
    master = master.replace('<strong>Priority Same-Day Service</strong> across Sydney', f'<strong>Priority Same-Day Service</strong> across {sub_title}')
    master = master.replace('same-day coverage across Greater Sydney', f'same-day coverage across {sub_title}')
    master = master.replace('Full Greater Sydney coverage.', f'Full {sub_title} coverage.')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(master)

repaired_count = 0
for cf in corrupted_files:
    parts = cf.replace('.html', '').split('-programmer-')
    if len(parts) == 2:
        is_cbus = cf.startswith('c-bus-')
        sub_slug = parts[1]
        sub_title = sub_slug.replace('-', ' ').title()
        repair_file(cf, is_cbus, sub_slug, sub_title)
        repaired_count += 1
    else:
        print(f"Skipping unknown structure: {cf}")

print(f"SUCCESS: Repaired and normalized {repaired_count} files.")
