import os

directory = '.'

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            orig_content = content

            content = content.replace("for over 15 years.", "since our establishment in 2025.")
            content = content.replace("with over 15 years of experience", "with extensive accredited experience")
            content = content.replace("over 15 years of hands-on experience", "extensive hands-on experience")
            content = content.replace("over 15 years of technical authority", "extensive technical authority")
            content = content.replace("over 15 years old", "older")
            content = content.replace("15+ Years of Accredited Experience", "Founded in 2025")
            content = content.replace('15+</div><div class="stat-label">Years of Accredited Experience', '2025</div><div class="stat-label">Year Established')
            
            content = content.replace("✅ Licensed Electrical Contractor NSW", "✅ Partnering with Licensed Electricians")
            content = content.replace("Licensed Electrical Contractor NSW", "Partnering with Licensed Electrical Contractors")
            content = content.replace("Fully licensed electrical contractor registered with NSW Fair Trading, providing compliant 240V electrical works alongside specialist automation programming under a single, accountable service provider.", "We partner with fully licensed electrical contractors registered with NSW Fair Trading to ensure compliant 240V electrical works alongside our specialist automation programming.")
            
            content = content.replace("✅ Schneider Electric Certified", "✅ Schneider Electric Trained")
            content = content.replace("Schneider Electric Channel Partner", "Genuine Schneider Electric Hardware")
            content = content.replace("Direct Schneider Electric channel partner with priority access", "We utilize genuine Schneider Electric C-Bus SpaceLogic hardware with access")
            
            # Additional replace for the "Our Journey" section
            content = content.replace(
                '<div class="timeline-year">Early 2000s</div>',
                '<div class="timeline-year">2025</div>'
            )
            content = content.replace(
                '<div class="timeline-title">The First Commission</div>',
                '<div class="timeline-title">Company Founded</div>'
            )
            content = content.replace(
                'Completed our first residential C-Bus commissioning project in the Sutherland Shire, discovering a clear gap in the Sydney market for genuine, accredited specialist programming — distinct from general electrical or AV companies.',
                'Founded Sydney Automation Co. to fill a clear gap in the Sydney market for genuine, accredited specialist programming — distinct from general electrical or AV companies.'
            )
            
            # Remove the 2010s / 2015 / 2020 items from about-sydney-automation-co.html and about.html
            content = content.replace(
                '''<div class="timeline-item">
      <div class="timeline-year">2010s</div>
      <div class="timeline-title">Commercial & Strata Expansion</div>
      <div class="timeline-body">Expanded our capabilities into commercial office towers across the Sydney CBD, strata common area automation across the Eastern Suburbs and North Shore, and warehouse lighting control across Western Sydney's industrial corridors.</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-year">2015</div>
      <div class="timeline-title">Dynalite Accreditation</div>
      <div class="timeline-body">Achieved official Dynalite accreditation, enabling us to service premium hospitality venues, luxury hotels, and architectural residential estates requiring world-class DyNet lighting control and Antumbra keypad aesthetics.</div>
    </div>
    <div class="timeline-item">
      <div class="timeline-year">2020</div>
      <div class="timeline-title">cbusnotworking.com.au Launch</div>
      <div class="timeline-body">Launched our dedicated emergency breakdown portal — cbusnotworking.com.au — providing 24/7 technical guidance, error code diagnostics, and emergency dispatch booking for critical C-Bus and Dynalite system failures across NSW.</div>
    </div>''',
                ''
            )

            # And same for the about.html which has slightly different spacing
            content = content.replace(
                '''<div class="timeline-item">
<div class="timeline-year">2010s</div>
<div class="timeline-title">Commercial & Strata Expansion</div>
<div class="timeline-body">Expanded our capabilities into commercial office towers across the Sydney CBD, strata common area automation across the Eastern Suburbs and North Shore, and warehouse lighting control across Western Sydney's industrial corridors.</div>
</div>
<div class="timeline-item">
<div class="timeline-year">2015</div>
<div class="timeline-title">Dynalite Accreditation</div>
<div class="timeline-body">Achieved official Dynalite accreditation, enabling us to service premium hospitality venues, luxury hotels, and architectural residential estates requiring world-class DyNet lighting control and Antumbra keypad aesthetics.</div>
</div>
<div class="timeline-item">
<div class="timeline-year">2020</div>
<div class="timeline-title">cbusnotworking.com.au Launch</div>
<div class="timeline-body">Launched our dedicated emergency breakdown portal — cbusnotworking.com.au — providing 24/7 technical guidance, error code diagnostics, and emergency dispatch booking for critical C-Bus and Dynalite system failures across NSW.</div>
</div>''',
                ''
            )

            if content != orig_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Claims fixed.")
