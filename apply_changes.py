import os
import json
import re

suburb_data_path = r'C:\Users\gaska\.gemini\antigravity\brain\6569efe0-ccea-4491-ab7a-fd9f96a92864\scratch\suburb_data.json'
with open(suburb_data_path, 'r', encoding='utf-8') as f:
    suburb_data = json.load(f)

project_mapping = {
    "Parramatta": {
        "cta": "We have completed automation works at prestigious locations across Parramatta, including high-rise blind control and lighting commissioning at 1 Parramatta Square (WSU).",
        "img": "wsu-01-studio-1-3-39-level-3.jpg",
        "alt": "C-Bus Automation at 1 Parramatta Square WSU"
    },
    "North Sydney": {
        "cta": "Our North Shore team recently completed a major C-Bus relay upgrade for Winten Property Group, ensuring their commercial space remains at the cutting edge of automation.",
        "img": "winten-11-winten-reception.jpg",
        "alt": "C-Bus Relay Upgrade in North Sydney"
    },
    "Ingleburn": {
        "cta": "We recently upgraded the automation system for Kebia Importex in Ingleburn, replacing aging relay modules to restore full reliability to their warehouse operations.",
        "img": "kebia-industrial-cbus.jpg",
        "alt": "Ingleburn Local Landmark"
    },
    "Kingswood": {
        "cta": "Closely tied to our work at WSU Parramatta, our team provides specialist C-Bus and Dynalite support for educational and residential facilities across Kingswood.",
        "img": "wsu-04-teaching-studio-blockouts-down.jpg",
        "alt": "Educational Automation Specialist"
    }
}

template = """
<!-- LOCAL HIGHLIGHT SECTION -->
<div class="section" style="background:linear-gradient(135deg,#0e1f3d 0%,#132647 100%);border-top:1px solid #2a4a80;border-bottom:1px solid #2a4a80">
  <div class="container">
    <div class="grid-2" style="align-items:center;gap:64px">
      <div>
        <div class="tag">&#x1F4CD; Local Authority</div>
        <h2 style="margin-bottom:20px">{suburb_name} <span class="accent">Landmarks &amp; History</span></h2>
        <p style="color:#a8c0e0;line-height:1.8;font-size:16px;margin-bottom:24px">
          {suburb_history} Notable landmarks include {suburb_landmarks}.
        </p>
        <p style="color:#f0f4ff;font-weight:600;font-size:15px;margin-bottom:24px">
          {project_cta}
        </p>
        <a class="btn btn-outline" href="/contact">Get a Local Quote</a>
      </div>
      <div>
        <div style="position:relative;border-radius:20px;overflow:hidden;border:1px solid #2a4a80;box-shadow:0 20px 40px rgba(0,0,0,0.4)">
          <img src="{image_src}" alt="{image_alt}" style="width:100%;display:block">
          {placeholder_overlay}
        </div>
      </div>
    </div>
  </div>
</div>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()

    changed = False

    # 1. Update brand marquee and text transition to Signify Dynalite (what 63fd90a did)
    if 'Dynalite' in html and 'Signify Dynalite' not in html:
        # Simple text replacement for heading/body, being careful not to break URLs
        html = re.sub(r'(?<![-/a-zA-Z0-9])Dynalite(?![a-zA-Z0-9.-])', 'Signify Dynalite', html)
        changed = True
        
    # 2. Update the Brand Marquee with professional logos (what b0f4eca did, but we are already on b0f4eca. However, let's make sure it's clean)
    
    # 3. Add products.html to nav
    if '<a href="/services">All Services \u2192</a>' in html:
        html = html.replace('<a href="/services">All Services \u2192</a>', '<a href="/products.html">Hardware Directory</a>\n            <a href="/services">All Services \u2192</a>')
        changed = True
    elif '<a href="/services">All Services &rarr;</a>' in html:
        html = html.replace('<a href="/services">All Services &rarr;</a>', '<a href="/products.html">Hardware Directory</a>\n            <a href="/services">All Services &rarr;</a>')
        changed = True
    elif 'Hardware Directory' not in html and '<a href="/services">All Services' in html:
        html = html.replace('<a href="/services">All Services', '<a href="/products.html">Hardware Directory</a>\n            <a href="/services">All Services')
        changed = True

    # 4. Add EEAT Suburb Content
    filename = os.path.basename(filepath).lower()
    suburb_name = ""
    for s in suburb_data:
        if "cbd" in filename and s == "Sydney CBD":
            suburb_name = s
            break
        if s.lower().replace(" ", "-") in filename or s.lower() in filename.replace("-", " "):
            suburb_name = s
            break

    if suburb_name and suburb_name in suburb_data and 'Local Authority' not in html and 'Landmarks &amp; History' not in html:
        data = suburb_data[suburb_name]
        proj = project_mapping.get(suburb_name, {
            "cta": f"Your {suburb_name} project could be featured here. We specialize in local C-Bus & Dynalite automation for prestige homes and commercial sites.",
            "img": "og-image.jpg",
            "alt": f"Iconic view of {suburb_name}"
        })
        img_path = proj['img']
        overlay = '<div style="position:absolute;bottom:20px;left:20px;right:20px;background:rgba(240,112,32,0.9);color:#fff;padding:12px;border-radius:10px;text-align:center;font-weight:700;font-size:14px">YOUR PROJECT COULD BE HERE</div>' if img_path == "og-image.jpg" else ""

        content = template.format(
            suburb_name=suburb_name,
            suburb_history=data['history'],
            suburb_landmarks=", ".join(data['landmarks']),
            project_cta=proj['cta'],
            image_src=f"/{img_path}" if not img_path.startswith("/") else img_path,
            image_alt=proj['alt'],
            placeholder_overlay=overlay
        )

        pattern = re.compile(r'(<div class="section">[\s\S]*?<div class="section-header">)')
        match = pattern.search(html)
        if match:
            insertion_point = match.start()
            html = html[:insertion_point] + content + "\n" + html[insertion_point:]
            changed = True
        else:
            footer_point = html.find('<footer>')
            if footer_point != -1:
                html = html[:footer_point] + content + "\n" + html[footer_point:]
                changed = True
            else:
                html = html.replace('</body>', content + '</body>')
                changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

base_path = r'c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co'
files = [f for f in os.listdir(base_path) if f.endswith('.html')]

exclude = ['products.html', 'index.html', 'about.html', 'contact.html', 'services.html', 'projects.html', 'privacy-policy.html', 'locations.html', '404.html', 'strata.html', 'shire.html']

count = 0
for f in files:
    if f in exclude or f.startswith('blog-'):
        continue
    filepath = os.path.join(base_path, f)
    if process_file(filepath):
        count += 1

# Also process index for nav specifically
if process_file(os.path.join(base_path, 'index.html')):
    count += 1
if process_file(os.path.join(base_path, 'services.html')):
    count += 1

print(f"Updated {count} files.")
