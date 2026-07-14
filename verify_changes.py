import os

BASE = r'C:\Users\gaska\Sydney-Automation-Co'

checks = {
    'BLUF paragraphs': 0,
    'HowTo schema': 0,
    'Service schema': 0,
    'EducationalOccupationalCredential': 0,
    'SoftwareApplication (protocol)': 0,
    'ItemList (products)': 0,
    'Manufacturer-Accredited Specialist (outbound links)': 0,
    'Coastal Alert': 0,
    'FAQPage schema': 0,
}

for fn in os.listdir(BASE):
    if not fn.endswith('.html'): continue
    fp = os.path.join(BASE, fn)
    for enc in ('utf-8','latin1','cp1252'):
        try:
            with open(fp,'r',encoding=enc) as f: c = f.read()
            break
        except: continue
    else:
        continue
    
    if 'border-left:4px solid #f07020' in c and ('To repair' in c or 'To diagnose' in c or 'To fix' in c or 'To commission' in c or 'To complete' in c or 'To upgrade' in c or 'Sydney Automation Co. provides specialist' in c or 'Browse our complete' in c):
        checks['BLUF paragraphs'] += 1
    if 'HowTo' in c and 'application/ld+json' in c:
        checks['HowTo schema'] += 1
    if 'Service' in c and '"@type"' in c and 'application/ld+json' in c:
        checks['Service schema'] += 1
    if 'EducationalOccupationalCredential' in c:
        checks['EducationalOccupationalCredential'] += 1
    if 'SoftwareApplication' in c and 'application/ld+json' in c:
        checks['SoftwareApplication (protocol)'] += 1
    if 'ItemList' in c and 'application/ld+json' in c:
        checks['ItemList (products)'] += 1
    if 'Manufacturer-Accredited Specialist' in c:
        checks['Manufacturer-Accredited Specialist (outbound links)'] += 1
    if 'Coastal Alert' in c:
        checks['Coastal Alert'] += 1
    if 'FAQPage' in c and 'application/ld+json' in c:
        checks['FAQPage schema'] += 1

print("=== VERIFICATION REPORT ===")
for k,v in checks.items():
    print(f"  {k}: {v} pages")
