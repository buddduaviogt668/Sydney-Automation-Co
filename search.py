import os
import re

pages = [
    'cbus-repair-sydney', 'c-bus-programmer-sydney',
    'dynalite-programmer-sydney', 'dynalite-repair-sydney',
    'cbus-relay-power-supply-replacement-sydney',
    'remote-cbus-dynalite-commissioning',
    'services', 'electricians', 'contact',
    'lighting-control-service-sydney', 'cbus-upgrade-sydney',
    'emergency-repair-sydney', 'dali-lighting-repair',
]

patterns = re.compile(r'\$\s*\d+|per\s*hour|GST|deposit|refundable|non.?refund|minimum.*hour|call.?out.?fee|rate.?card', re.IGNORECASE)

for p in pages:
    path = f'{p}.html'
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        content = f.read()
    matches = patterns.findall(content)
    if matches:
        print(f'\n=== {p}.html ({len(matches)} matches) ===')
        for m in patterns.finditer(content):
            start = max(0, m.start() - 40)
            end = min(len(content), m.end() + 60)
            ctx = content[start:end].replace('\n', ' ')
            print(f'  ...{ctx.strip()}...')
