import os

# Clean the UTF-16 or corrupted UTF-8 output of deleted_pages.txt
def clean_deleted_pages():
    with open('deleted_pages.txt', 'rb') as f:
        raw = f.read()
    
    # Try decoding as UTF-16-LE or check if it has null bytes
    if b'\x00' in raw:
        try:
            text = raw.decode('utf-16')
        except Exception:
            try:
                text = raw.decode('utf-16-le')
            except Exception:
                text = raw.replace(b'\x00', b'').decode('utf-8', errors='ignore')
    else:
        text = raw.decode('utf-8', errors='ignore')

    lines = [l.strip() for l in text.split('\n') if l.strip()]
    cleaned_lines = []
    for line in lines:
        # Strip any BOM or weird characters
        line = line.replace('\ufeff', '').replace('\u0000', '').strip()
        if line:
            cleaned_lines.append(line)
            
    return cleaned_lines

deleted_files = clean_deleted_pages()
print(f"Total cleaned deleted files: {len(deleted_files)}")

# Get currently existing files
existing = set()
for root, _, files in os.walk('.'):
    if '.git' in root or '.gemini' in root: continue
    for f in files:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, f), '.').replace('\\', '/')
            existing.add(rel)

print(f"Total existing HTML files: {len(existing)}")

still_deleted = [f for f in deleted_files if f not in existing]
print(f"Still deleted: {len(still_deleted)}")

# Categorise still deleted pages
cats = {}
for f in still_deleted:
    if f.startswith('tech-library/'):
        cat = 'tech-library'
    elif 'emergency-lighting' in f or 'afss' in f:
        cat = 'emergency-lighting'
    elif 'strata' in f:
        cat = 'strata'
    elif 'dali' in f:
        cat = 'dali'
    elif 'blog' in f:
        cat = 'blog'
    elif any(x in f for x in ['hotel','hospital','school','gym','warehouse','car-park','car-dealer','aged-care','corporate','boutique','retail','pubs','sporting','funeral','government','shopping']):
        cat = 'commercial-sector'
    else:
        cat = 'other'
    cats.setdefault(cat, []).append(f)

for cat, files in sorted(cats.items(), key=lambda x: -len(x[1])):
    print(f"\n{cat}: {len(files)} files")
    for f in files[:10]:
        print(f"  - {f}")
    if len(files) > 10:
        print(f"  ... and {len(files)-10} more")
