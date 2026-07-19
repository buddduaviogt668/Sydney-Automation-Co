from pathlib import Path
from bs4 import BeautifulSoup
import json

changed=[]
for path in sorted(Path('blog').glob('*.html')):
    html=path.read_text(encoding='utf-8', errors='ignore')
    soup=BeautifulSoup(html,'html.parser')
    file_changed=False
    for script in soup.find_all('script', type='application/ld+json'):
        txt=(script.string or script.get_text() or '').strip()
        if 'FAQPage' not in txt:
            continue
        candidate=txt.replace('{{','{').replace('}}','}')
        try:
            json.loads(candidate)
        except Exception:
            continue
        if candidate!=txt:
            script.string='\n'+json.dumps(json.loads(candidate), ensure_ascii=False, indent=2)+'\n'
            file_changed=True
    if file_changed:
        path.write_text(str(soup), encoding='utf-8')
        changed.append(str(path))
print(f'Repaired blog FAQ JSON-LD files: {len(changed)}')
for p in changed:
    print(p)
