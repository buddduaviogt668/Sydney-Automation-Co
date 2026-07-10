import os
import re

# Update old pricing on all restored suburb pages
# Old pricing patterns to replace
replacements = [
    # Old diagnostic fee / deposit references
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

# Get all restored suburb pages
restore_patterns = [
    'c-bus-programmer-',
    'dynalite-programmer-',
    'cbus-repair-',
    'dynalite-repair-',
    'smart-home-automation-',
    'smart-home-',
    'lighting-automation-',
    'lighting-control-',
]

updated = 0
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    for p in restore_patterns:
        if f.startswith(p):
            if update_pricing(f):
                updated += 1
            break

print(f"Updated pricing on {updated} suburb pages.")
