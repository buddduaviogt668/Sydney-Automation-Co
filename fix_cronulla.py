import os, re

BASE = r'C:\Users\gaska\Sydney-Automation-Co'

COASTAL_BLUF = '<div style="background:#132647;border-left:4px solid #0ea5e9;padding:16px 20px;border-radius:0 8px 8px 0;margin:0 0 24px">\n<strong style="color:#0ea5e9;font-size:1.05rem">Coastal Alert:</strong> <span style="color:#a8c0e0">Properties in Cronulla and surrounding coastal suburbs face accelerated corrosion on C-Bus and Dynalite terminal connections due to salt-laden air. We recommend annual bus termination inspections for all coastal installations to prevent communication faults caused by oxidised connectors.</span>\n</div>'

def read_file(fp):
    for enc in ('utf-8','latin1','cp1252'):
        try:
            with open(fp,'r',encoding=enc) as f: return f.read()
        except: continue
    return None

for fn in ['cbus-repair-cronulla.html','dynalite-programmer-cronulla.html']:
    fp = os.path.join(BASE, fn)
    c = read_file(fp)
    if not c: print(f'SKIP {fn}'); continue
    if 'Coastal Alert' in c: print(f'SKIP (exists) {fn}'); continue
    if '<div class="page">' in c:
        c = c.replace('<div class="page">', COASTAL_BLUF + '\n<div class="page">', 1)
        with open(fp,'w',encoding='utf-8',errors='replace') as f: f.write(c)
        print(f'OK: {fn}')
    else:
        m = re.search(r'(<div class="hero"[^>]*>)', c)
        if m:
            c = c.replace(m.group(1), COASTAL_BLUF + '\n' + m.group(1), 1)
            with open(fp,'w',encoding='utf-8',errors='replace') as f: f.write(c)
            print(f'OK (hero): {fn}')
        else:
            print(f'FAIL: {fn}')
