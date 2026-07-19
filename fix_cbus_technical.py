import os, re

BASE = r'C:\Users\gaska\Sydney-Automation-Co'

def read_file(fp):
    for enc in ('utf-8','latin1','cp1252'):
        try:
            with open(fp,'r',encoding=enc) as f: return f.read()
        except: continue
    return None

def write_file(fp, c):
    with open(fp,'w',encoding='utf-8',errors='replace') as f: f.write(c)

fixes = 0

# ============================================================
# Fix all C-Bus RS-485 references -> RS-232
# Fix voltage 5-11.5V -> 15-36V
# Fix "network analyser" -> meter
# ============================================================

# Files to check (all files we modified + any that might have old content)
ALL_FILES = []
for fn in os.listdir(BASE):
    if fn.endswith('.html'):
        ALL_FILES.append(os.path.join(BASE, fn))
for fn in os.listdir(os.path.join(BASE, 'blog')):
    if fn.endswith('.html'):
        ALL_FILES.append(os.path.join(BASE, 'blog', fn))

for fp in ALL_FILES:
    c = read_file(fp)
    if not c:
        continue
    
    original = c
    
    # Fix RS-485 references for C-Bus (not Dynalite - DyNet IS RS-485)
    # Only fix lines that mention C-Bus in the same context
    
    # Fix BLUF paragraphs and text content
    # Replace "RS-485 bus voltage analysis" with correct terminology
    c = c.replace('RS-485 bus voltage analysis (normal range: 5–11.5V)', 'C-Bus network voltage check with a multimeter (normal range: 15–36V DC)')
    c = c.replace('RS-485 bus voltage analysis', 'C-Bus network voltage check')
    c = c.replace('RS-485 bus diagnostics', 'C-Bus network diagnostics')
    c = c.replace('perform an RS-485 bus voltage analysis', 'measure the C-Bus network voltage with a multimeter')
    c = c.replace('RS-485 based lighting control protocol', 'proprietary lighting control protocol (RS-232 bus)')
    c = c.replace('RS-485 bus analyser for C-Bus and DyNet', 'Multimeter for C-Bus voltage checks and RS-485 bus analyser for DyNet')
    
    # Fix voltage ranges (5-11.5V -> 15-36V for C-Bus)
    c = c.replace('should read 5–11.5V DC', 'should read 15–36V DC')
    c = c.replace('should read 5-11.5V DC', 'should read 15-36V DC')
    c = c.replace('normal range: 5–11.5V', 'normal range: 15–36V DC')
    c = c.replace('5 to 11.5V DC', '15 to 36V DC')
    c = c.replace('5-11.5V DC', '15-36V DC')
    c = c.replace('providing 5-11.5V DC', 'providing 15-36V DC')
    c = c.replace('5V DC indicates', '15V DC indicates')
    c = c.replace('Below 5V indicates', 'Below 15V indicates')
    
    # Fix "network analyser" references for C-Bus
    c = c.replace('test bus communication with a specialist analyser', 'measure network voltage with a multimeter')
    c = c.replace('RS-485 bus analysers, and common replacement Dynalite hardware', 'a multimeter, and common replacement Dynalite hardware')
    
    if c != original:
        fn = os.path.basename(fp)
        write_file(fp, c)
        changes = sum(1 for a,b in zip(original,c) if a!=b) + abs(len(c)-len(original))
        print(f"  FIXED: {fn}")
        fixes += 1

print(f"\nTotal files fixed: {fixes}")
