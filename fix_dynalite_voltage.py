import os

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
    
    # Fix Dynalite voltage: 9.6-42V -> up to 16V
    c = c.replace('9.6–42V DC', 'up to 16V DC (data lines 0–3V)')
    c = c.replace('9.6–42v DC', 'up to 16V DC (data lines 0–3V)')
    c = c.replace('9.6 to 42V DC', 'up to 16V DC (data lines 0–3V)')
    c = c.replace('9.6V indicates', 'Below operating voltage indicates')
    c = c.replace('Below 9.6V indicates', 'Below operating voltage indicates')
    c = c.replace('Below 9.6V', 'Below operating voltage')
    
    if c != original:
        fn = os.path.basename(fp)
        write_file(fp, c)
        print(f"  FIXED: {fn}")
        fixes += 1

print(f"\nTotal files fixed: {fixes}")
