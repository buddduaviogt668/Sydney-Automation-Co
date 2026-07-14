import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def read_file(filepath):
    for enc in ('utf-8', 'latin1', 'cp1252'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    return None

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
        f.write(content)

# ============================================================
# 1. CERTIFICATION SCHEMA for about.html
# ============================================================
print("=== 1. Certification Schema (about.html) ===")

cert_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOccupationalCredential",
  "name": "Clipsal C-Bus Accredited Programmer",
  "credentialCategory": "Professional Certification",
  "recognizedBy": {
    "@type": "Organization",
    "name": "Schneider Electric / Clipsal",
    "url": "https://www.se.com/au/"
  },
  "credentialIssuer": {
    "@type": "Organization",
    "name": "Schneider Electric Australia"
  },
  "about": {
    "@type": "Person",
    "name": "George Skarmoutsos"
  },
  "description": "Accredited C-Bus programmer certified by Schneider Electric/Clipsal for programming, commissioning, and fault finding of Clipsal C-Bus lighting control systems using C-Bus Toolkit software."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOccupationalCredential",
  "name": "Signify Dynalite Accredited System Designer",
  "credentialCategory": "Professional Certification",
  "recognizedBy": {
    "@type": "Organization",
    "name": "Signify (Philips Dynalite)",
    "url": "https://www.signify.com/"
  },
  "credentialIssuer": {
    "@type": "Organization",
    "name": "Signify Australia"
  },
  "about": {
    "@type": "Person",
    "name": "George Skarmoutsos"
  },
  "description": "Accredited Dynalite system designer certified by Signify for programming, design, and commissioning of Philips Dynalite lighting control systems using Dynalite EnvisionProject software."
}
</script>'''

about_content = read_file(os.path.join(BASE, 'about.html'))
if about_content and 'EducationalOccupationalCredential' not in about_content:
    about_content = about_content.replace(
        '<style>\n/* DROPDOWN NAV */',
        cert_schema + '\n<style>\n/* DROPDOWN NAV */',
        1
    )
    write_file(os.path.join(BASE, 'about.html'), about_content)
    print("  OK: Added certification schema to about.html")
else:
    print("  SKIP: Certification schema already exists")

# ============================================================
# 2. OUTBOUND AUTHORITY LINKS - Manufacturer Partners section
# ============================================================
print("\n=== 2. Outbound Authority Links ===")

MANUFACTURER_SECTION = '''
<section style="background:#0d1e3c;border-top:1px solid #1a2a4a;padding:40px 24px">
<div class="container" style="max-width:1000px;margin:0 auto;text-align:center">
<h2 style="color:#fff;font-family:'Barlow Condensed',sans-serif;font-size:1.5rem;margin-bottom:8px">Manufacturer-Accredited Specialist</h2>
<p style="color:#a8c0e0;font-size:14px;margin-bottom:24px">We are accredited by the original equipment manufacturers. Our certifications are verifiable:</p>
<div style="display:flex;justify-content:center;gap:32px;flex-wrap:wrap">
<a href="https://www.se.com/au/" target="_blank" rel="noopener" style="color:#a8c0e0;font-size:13px;text-decoration:none;padding:12px 20px;border:1px solid #2a4a80;border-radius:8px;transition:all 0.2s">Schneider Electric (Clipsal C-Bus) &rarr;</a>
<a href="https://www.signify.com/" target="_blank" rel="noopener" style="color:#a8c0e0;font-size:13px;text-decoration:none;padding:12px 20px;border:1px solid #2a4a80;border-radius:8px;transition:all 0.2s">Signify (Philips Dynalite) &rarr;</a>
<a href="https://www.dali-alliance.org/" target="_blank" rel="noopener" style="color:#a8c0e0;font-size:13px;text-decoration:none;padding:12px 20px;border:1px solid #2a4a80;border-radius:8px;transition:all 0.2s">DALI Alliance (DiiA) &rarr;</a>
<a href="https://www.clipsal.com/" target="_blank" rel="noopener" style="color:#a8c0e0;font-size:13px;text-decoration:none;padding:12px 20px;border:1px solid #2a4a80;border-radius:8px;transition:all 0.2s">Clipsal Product Portal &rarr;</a>
</div>
</div>
</section>
'''

# Pages to add manufacturer section before footer
LINK_PAGES = [
    'cbus-specialist-sydney.html',
    'services.html',
    'about.html',
    'index.html',
    'c-bus-programmer-sydney.html',
    'cbus-repair-sydney.html',
    'cbus-upgrade-sydney.html',
    'dynalite-programmer-sydney.html',
    'dynalite-repair-sydney.html',
    'dynalite-not-working-sydney.html',
    'dali-lighting-control-system-sydney.html',
    'afss-emergency-lighting-services.html',
    'emergency-repair-sydney.html',
    'cbus-fault-finding-sydney.html',
    'dynalite-fault-finding-sydney-common-faults.html',
]

for filename in LINK_PAGES:
    filepath = os.path.join(BASE, filename)
    content = read_file(filepath)
    if not content:
        print(f"  SKIP (not found): {filename}")
        continue
    
    if 'Manufacturer-Accredited Specialist' in content or 'Schneider Electric (Clipsal C-Bus)' in content:
        print(f"  SKIP (already has links): {filename}")
        continue
    
    # Try to insert before <footer
    if '<footer' in content:
        # Find the first <footer tag
        footer_pos = content.find('<footer')
        if footer_pos > 0:
            # Find the previous closing tag
            prev_close = content.rfind('</section>', 0, footer_pos)
            if prev_close > 0:
                insert_after = prev_close + len('</section>')
                content = content[:insert_after] + '\n' + MANUFACTURER_SECTION + content[insert_after:]
                write_file(filepath, content)
                print(f"  OK: {filename}")
                continue
            
            # Fallback: insert right before <footer
            content = content[:footer_pos] + MANUFACTURER_SECTION + content[footer_pos:]
            write_file(filepath, content)
            print(f"  OK (before footer): {filename}")
            continue
    
    print(f"  FAIL (no footer found): {filename}")


# ============================================================
# 3. PROTOCOL-SPECIFIC SCHEMA for key pages
# ============================================================
print("\n=== 3. Protocol-Specific Schema ===")

protocol_schema_cbus = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Clipsal C-Bus Toolkit",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Windows",
  "description": "Official programming and commissioning software for Clipsal C-Bus 2 lighting control systems by Schneider Electric.",
  "provider": {
    "@type": "Organization",
    "name": "Schneider Electric",
    "url": "https://www.se.com/au/"
  },
  "softwareVersion": "5.15.0",
  "url": "https://www.clipsal.com/products/c-bus-software"
}
</script>'''

protocol_schema_dynalite = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Dynalite EnvisionProject",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Windows",
  "description": "Official system design, programming and commissioning software for Philips Dynalite DyNet lighting control systems by Signify.",
  "provider": {
    "@type": "Organization",
    "name": "Signify",
    "url": "https://www.signify.com/"
  },
  "url": "https://www.signify.com/en-gb/our-products/brand/dynalite"
}
</script>'''

# C-Bus Toolkit schema goes on C-Bus pages
CBUS_SCHEMA_PAGES = [
    'cbus-specialist-sydney.html',
    'cbus-repair-sydney.html',
    'cbus-fault-finding-sydney.html',
    'cbus-upgrade-sydney.html',
    'c-bus-programmer-sydney.html',
]

for filename in CBUS_SCHEMA_PAGES:
    filepath = os.path.join(BASE, filename)
    content = read_file(filepath)
    if not content:
        continue
    if 'C-Bus Toolkit' in content and 'SoftwareApplication' in content:
        print(f"  SKIP (already has protocol schema): {filename}")
        continue
    if '<head>' in content:
        content = content.replace('<head>', '<head>\n' + protocol_schema_cbus, 1)
        write_file(filepath, content)
        print(f"  OK: {filename}")

# Dynalite EnvisionProject schema goes on Dynalite pages
DYN_SCHEMA_PAGES = [
    'dynalite-programmer-sydney.html',
    'dynalite-repair-sydney.html',
    'dynalite-not-working-sydney.html',
    'dynalite-fault-finding-sydney-common-faults.html',
]

for filename in DYN_SCHEMA_PAGES:
    filepath = os.path.join(BASE, filename)
    content = read_file(filepath)
    if not content:
        continue
    if 'EnvisionProject' in content and 'SoftwareApplication' in content:
        print(f"  SKIP (already has protocol schema): {filename}")
        continue
    if '<head>' in content:
        content = content.replace('<head>', '<head>\n' + protocol_schema_dynalite, 1)
        write_file(filepath, content)
        print(f"  OK: {filename}")


# ============================================================
# 4. COASTAL SALT/HUMIDITY CONTENT for Cronulla pages
# ============================================================
print("\n=== 4. Coastal Corrosion Content (Cronulla pages) ===")

COASTAL_BLUF = '''<div style="background:#132647;border-left:4px solid #0ea5e9;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px">
<strong style="color:#0ea5e9;font-size:1.05rem">Coastal Alert:</strong> <span style="color:#a8c0e0">Properties in Cronulla and surrounding coastal suburbs face accelerated corrosion on C-Bus and Dynalite terminal connections due to salt-laden air. We recommend annual bus termination inspections for all coastal installations to prevent communication faults caused by oxidised connectors.</span>
</div>'''

CRONULLA_PAGES = [
    'c-bus-programmer-cronulla.html',
    'c-bus-repair-cronulla.html',
    'dynalite-programmer-cronulla.html',
]

for filename in CRONULLA_PAGES:
    filepath = os.path.join(BASE, filename)
    content = read_file(filepath)
    if not content:
        print(f"  SKIP (not found): {filename}")
        continue
    if 'Coastal Alert' in content or 'salt-laden air' in content:
        print(f"  SKIP (already has coastal content): {filename}")
        continue
    
    # Insert before <div class="page">
    if '<div class="page">' in content:
        content = content.replace('<div class="page">', COASTAL_BLUF + '\n<div class="page">', 1)
        write_file(filepath, content)
        print(f"  OK: {filename}")
    elif '<div class="hero"' in content:
        hero_match = re.search(r'(<div class="hero"[^>]*>)', content)
        if hero_match:
            content = content.replace(hero_match.group(1), COASTAL_BLUF + '\n' + hero_match.group(1), 1)
            write_file(filepath, content)
            print(f"  OK (before hero): {filename}")
    else:
        print(f"  FAIL: {filename}")


print("\n=== All schema/link tasks complete ===")
