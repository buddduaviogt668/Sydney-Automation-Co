import os

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"
source_file = os.path.join(DIR, "smart-home-automation-companies-sydney.html")
target_file = os.path.join(DIR, "automation-companies-sydney.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles and meta
content = content.replace(
    '<title>Smart Home Automation Companies Sydney | Sydney Automation Co</title>',
    '<title>Commercial Automation Companies Sydney | Lighting Control Specialists</title>'
)
content = content.replace(
    'Top-rated smart home automation companies in Sydney. Expert C-Bus and Dynalite installation, programming, and repair for residential properties.',
    'Leading commercial lighting automation company in Sydney. We specialize strictly in C-Bus, Dynalite, DALI, and RAPIX. We do not do BMS or Industrial automation.'
)
content = content.replace(
    'href="https://sydneyautomationco.com.au/smart-home-automation-companies-sydney"',
    'href="https://sydneyautomationco.com.au/automation-companies-sydney"'
)

# Replace Hero
content = content.replace('Smart Home Automation Companies Sydney', 'Commercial Lighting Automation Companies Sydney')
content = content.replace('Looking for the best smart home automation companies in Sydney?', 'Looking for a specialist commercial automation company in Sydney?')
content = content.replace('We deliver premium C-Bus and Dynalite solutions for luxury residential properties.', 'We deliver premium C-Bus, Dynalite, DALI, and RAPIX solutions for commercial and strata properties. Note: We strictly specialize in lighting control. We do not service BMS (Building Management Systems) or Industrial/SCADA automation.')
content = content.replace('Top Smart Home Companies', 'Specialist Automation Companies')

# Replace body text
content = content.replace('smart home automation companies', 'commercial automation companies')
content = content.replace('Smart Home Automation Companies', 'Commercial Automation Companies')
content = content.replace('smart home automation', 'commercial lighting automation')
content = content.replace('Smart home automation', 'Commercial lighting automation')
content = content.replace('luxury homes', 'commercial towers and strata buildings')
content = content.replace('luxury residential', 'commercial and strata')
content = content.replace('residential properties', 'commercial properties')
content = content.replace('home automation', 'commercial automation')
content = content.replace('Home Automation', 'Commercial Automation')
content = content.replace('residential automation', 'commercial automation')

# Add specific exclusion disclaimer block
exclusion_block = '''
      <div style="background:rgba(240,112,32,0.1); border:1px solid #f07020; border-radius:12px; padding:24px; margin-bottom:48px;">
        <h3 style="color:#f07020; margin-bottom:12px; font-family:'Barlow Condensed', sans-serif;">Our Specialization: What We Do & Don't Do</h3>
        <p style="color:#a8c0e0; font-size:15px; margin-bottom:12px;">We believe in deep specialization rather than being "jacks of all trades." Therefore, we are strictly commercial lighting control programmers.</p>
        <ul style="color:#a8c0e0; padding-left:20px; font-size:15px; line-height:1.6; margin-bottom:16px;">
            <li><strong style="color:#fff;">WHAT WE DO:</strong> C-Bus, Philips Dynalite, DALI-2, and RAPIX. (Commercial towers, strata common areas, carparks, hotels, and high-end architectural residential).</li>
            <li><strong style="color:#e8330a;">WHAT WE DO NOT DO:</strong> We do NOT install or program BMS (Building Management Systems) such as Johnson Controls, Siemens, or Tridium Niagra. We do NOT do Industrial Automation or PLC programming for factory floors, manufacturing, or SCADA.</li>
        </ul>
      </div>
'''

# Inject after hero closing
content = content.replace('</section>\n\n  <section style="padding:64px 24px">', '</section>\n\n  <section style="padding:64px 24px">\n    <div style="max-width:960px;margin:0 auto">\n' + exclusion_block + '\n    </div>\n')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Update sitemap
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    if "automation-companies-sydney" not in xml:
        url_block = f"\n  <url>\n    <loc>https://sydneyautomationco.com.au/automation-companies-sydney</loc>\n    <lastmod>2026-06-21</lastmod>\n    <priority>0.70</priority>\n  </url>"
        xml = xml.replace("</urlset>", f"{url_block}\n</urlset>")
        
        with open(sitemap_xml, 'w', encoding='utf-8') as f:
            f.write(xml)

print("Created automation-companies-sydney.html and updated sitemap.")
