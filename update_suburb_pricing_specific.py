import os
import re

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

# Target specific files we just restored
restore_files = [
    'cbus-programming-chatswood.html',
    'cbus-programming-lindfield.html',
    'cbus-vs-dynalite.html',
    'dynalite-vs-cbus-sydney.html'
]

updated = 0
for f in restore_files:
    if os.path.exists(f):
        if update_pricing(f):
            updated += 1

print(f"Updated pricing on {updated} newly restored pages.")
