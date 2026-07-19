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

# Fix llms.txt
fp = os.path.join(BASE, 'llms.txt')
c = read_file(fp)
if c and 'EnvisionProject' in c:
    c = c.replace('EnvisionProject', 'System Builder')
    write_file(fp, c)
    print("  FIXED: llms.txt")
    fixes += 1

# Fix all HTML files
for fn in os.listdir(BASE):
    if not fn.endswith('.html'): continue
    fp = os.path.join(BASE, fn)
    c = read_file(fp)
    if not c or 'EnvisionProject' not in c: continue
    c = c.replace('EnvisionProject', 'System Builder')
    write_file(fp, c)
    print(f"  FIXED: {fn}")
    fixes += 1

# Fix blog subdirectory
for fn in os.listdir(os.path.join(BASE, 'blog')):
    if not fn.endswith('.html'): continue
    fp = os.path.join(BASE, 'blog', fn)
    c = read_file(fp)
    if not c or 'EnvisionProject' not in c: continue
    c = c.replace('EnvisionProject', 'System Builder')
    write_file(fp, c)
    print(f"  FIXED: blog/{fn}")
    fixes += 1

# Fix tech-library subdirectory
tl_dir = os.path.join(BASE, 'tech-library')
if os.path.isdir(tl_dir):
    for fn in os.listdir(tl_dir):
        if not fn.endswith('.html'): continue
        fp = os.path.join(tl_dir, fn)
        c = read_file(fp)
        if not c or 'EnvisionProject' not in c: continue
        c = c.replace('EnvisionProject', 'System Builder')
        write_file(fp, c)
        print(f"  FIXED: tech-library/{fn}")
        fixes += 1

print(f"\nTotal files fixed: {fixes}")
