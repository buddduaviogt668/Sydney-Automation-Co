from bs4 import BeautifulSoup
from pathlib import Path
import json, re

root = Path('.')
rows = []
for path in sorted(root.rglob('*.html')):
    if '.git' in path.parts:
        continue
    html = path.read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script', type='application/ld+json')
    faq_jsonld = 0
    invalid = []
    for i, s in enumerate(scripts, 1):
        txt = (s.string or s.get_text() or '').strip()
        faq_jsonld += txt.count('"FAQPage"') + txt.count("'FAQPage'")
        try:
            json.loads(txt)
        except Exception as e:
            invalid.append(f'script {i}: {e}')
    faq_microdata = len(soup.select('[itemscope][itemtype="https://schema.org/FAQPage"], [itemscope][itemtype="http://schema.org/FAQPage"]'))
    if faq_jsonld + faq_microdata > 1 or invalid:
        rows.append({
            'file': str(path),
            'jsonld_scripts': len(scripts),
            'faq_jsonld': faq_jsonld,
            'faq_microdata': faq_microdata,
            'invalid_jsonld': invalid,
        })

print(f'Problematic structured data pages: {len(rows)}')
for r in rows[:300]:
    print(f"{r['file']} | scripts={r['jsonld_scripts']} faq_jsonld={r['faq_jsonld']} faq_microdata={r['faq_microdata']} invalid={len(r['invalid_jsonld'])}")
    for inv in r['invalid_jsonld'][:3]:
        print('  -', inv)
