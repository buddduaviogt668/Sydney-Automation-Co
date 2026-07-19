import os

with open('deleted_pages.txt', 'rb') as f:
    raw = f.read()

# Clean null bytes if UTF-16-LE
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

deleted = [l.strip().replace('\ufeff', '').replace('\u0000', '') for l in text.split('\n') if l.strip()]

search_terms = ['c-bus-repairs-sydney', 'dynalite-fault-finding', 'cbus-fault-finding', 'cbus-maintenance', 'how-to-choose', 'cbus-relay-making-buzzing-noise-sydney', 'dynalite-maintenance', 'rapix-emergency', 'cbus-automation-north-shore-sydney', 'c-bus-vs-dynalite-vs-knx-comparison-sydney']

for term in search_terms:
    matches = [d for d in deleted if term in d]
    print(f"Matches for {term}:")
    for m in matches:
        print(f"  - {m}")
