import re
import os

replacements = [
    (r'\$650', '$200 diagnostic fee'),
    (r'\$150 deposit', '$200 diagnostic fee'),
    (r'pay \$150', 'pay $200 diagnostic fee'),
    (r'Book \$450 Diagnostic Call', 'Book $200 Diagnostic Visit'),
    (r'\$450 diagnostic', '$200 diagnostic'),
    (r'no call-out surcharge for metro Sydney', "we don't charge a call-out fee, just a standard $200 diagnostic fee"),
    (r'Same accredited technician, same-day response, no call-out surcharge for metro Sydney\.', 
     "Same accredited technician, same-day response. We don't charge a call-out fee — just a standard $200 diagnostic fee."),
]

patterns = [(re.compile(p, re.IGNORECASE), r) for p, r in replacements]

def update_pricing(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for pattern, replacement in patterns:
            content = pattern.sub(replacement, content)
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error on {filepath}: {e}")
    return False

restored_files = [
    'c-bus-repairs-sydney.html',
    'c-bus-vs-dynalite-vs-knx-comparison-sydney.html',
    'cbus-automation-north-shore-sydney.html',
    'cbus-fault-finding-sydney.html',
    'cbus-maintenance-sydney.html',
    'cbus-relay-making-buzzing-noise-sydney.html',
    'dynalite-fault-finding-sydney-common-faults.html',
    'dynalite-maintenance-sydney.html',
    'how-to-choose-cbus-specialist-sydney.html',
    'rapix-emergency-lighting-sydney.html'
]

updated = 0
for f in restored_files:
    if os.path.exists(f):
        if update_pricing(f):
            updated += 1

print(f"Updated pricing on {updated} files.")
