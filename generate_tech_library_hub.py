import os
import re

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"
TECH_LIB_DIR = os.path.join(DIR, "tech-library")

if not os.path.exists(TECH_LIB_DIR):
    print("tech-library directory not found.")
    exit(1)

files = [f for f in os.listdir(TECH_LIB_DIR) if f.endswith('.html')]

# Group files by system and part
grouped = {}
for f in files:
    # filename format: system-part-symptom-region.html
    # e.g. clipsal-c-bus-5508rvf-blinking-led-codes-north-shore.html
    # dynalite-ddbc1200-frozen-unresponsive-interfaces-eastern-suburbs.html
    
    parts = f.split('-')
    if f.startswith('clipsal-c-bus'):
        system = 'Clipsal C-Bus'
        part_no = parts[3].upper()
        name = f.replace('.html', '').replace('-', ' ').title()
    elif f.startswith('dynalite'):
        system = 'Dynalite'
        part_no = parts[1].upper()
        # Edge case: DMDR12-320
        if part_no == 'DMDR12':
            part_no = 'DMDR12-320'
        name = f.replace('.html', '').replace('-', ' ').title()
    else:
        continue
        
    key = f"{system} {part_no}"
    if key not in grouped:
        grouped[key] = []
    
    grouped[key].append({"filename": f, "title": name})

base_template_path = os.path.join(DIR, "index.html")
with open(base_template_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Replace Title and Meta
content = re.sub(r'<title>.*?</title>', '<title>Technical Troubleshooting Library | Sydney Automation Co.</title>', base_html)
content = re.sub(r'name="description" content=".*?"', 'name="description" content="Access our comprehensive technical library of 480+ troubleshooting guides for Clipsal C-Bus and Signify Dynalite hardware components."', content)

# Remove FAQ Schema
content = re.sub(r'<script type="application/ld\+json">.*?FAQPage.*?</script>', '', content, flags=re.DOTALL)

# Build body
html_body = []
html_body.append('''
<div class="hero" style="padding-top:120px; padding-bottom:60px;">
    <div class="container text-center">
        <div class="tag">Knowledge Base</div>
        <h1>Technical Troubleshooting Library</h1>
        <p class="subtitle" style="max-width:800px; margin:0 auto;">Browse our 480+ technical guides for Clipsal C-Bus and Signify Dynalite hardware faults across Sydney regions.</p>
    </div>
</div>
<div class="section">
    <div class="container">
''')

for key, links in sorted(grouped.items()):
    html_body.append(f'<div style="background:#132647; padding:30px; border-radius:12px; border:1px solid #2a4a80; margin-bottom:30px;">')
    html_body.append(f'<h2 style="margin-bottom:20px;">{key} Troubleshooting Guides</h2>')
    html_body.append('<div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px;">')
    for link in links:
        # Strip .html extension for clean URL
        clean_url = link["filename"].replace(".html", "")
        html_body.append(f'<a href="/tech-library/{clean_url}" style="display:block; padding:10px; background:rgba(255,255,255,0.05); border-radius:6px; font-size:14px; text-decoration:none; color:#a8c0e0;">{link["title"]}</a>')
    html_body.append('</div></div>')

html_body.append('</div></div>')

body_content = "\n".join(html_body)

if '</nav>' in content and '<footer' in content:
    head_nav = content.split('</nav>')[0] + '</nav>'
    footer_end = '<footer' + content.split('<footer')[1]
    content = head_nav + body_content + footer_end

with open(os.path.join(DIR, "tech-library.html"), 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated tech-library.html hub page.")
