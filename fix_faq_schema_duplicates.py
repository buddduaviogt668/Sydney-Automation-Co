from pathlib import Path
from bs4 import BeautifulSoup
import json
import copy

ROOT = Path('.')
SCHEMA_URL = 'https://schema.org'


def as_list(v):
    return v if isinstance(v, list) else [v]


def collect_faq_entities(obj):
    entities = []
    if isinstance(obj, list):
        for item in obj:
            entities.extend(collect_faq_entities(item))
    elif isinstance(obj, dict):
        typ = obj.get('@type')
        types = typ if isinstance(typ, list) else [typ]
        if 'FAQPage' in types:
            main = obj.get('mainEntity') or []
            if isinstance(main, dict):
                main = [main]
            for q in main:
                if isinstance(q, dict):
                    entities.append(q)
        if '@graph' in obj:
            entities.extend(collect_faq_entities(obj['@graph']))
    return entities


def is_faq_jsonld_text(txt):
    return 'FAQPage' in txt or '"mainEntity"' in txt and 'Question' in txt and 'acceptedAnswer' in txt


def clean_double_braced_json(txt):
    stripped = txt.strip()
    # Some blog FAQ scripts were generated with Python-template escaped braces, e.g. {{ ... }}.
    # Repeatedly collapse only outer doubled braces until normal JSON is reached.
    while stripped.startswith('{{') and stripped.endswith('}}'):
        stripped = stripped[1:-1].strip()
    return stripped


def unique_questions(questions):
    seen = set()
    out = []
    for q in questions:
        if not isinstance(q, dict):
            continue
        name = str(q.get('name', '')).strip()
        answer = q.get('acceptedAnswer')
        answer_text = ''
        if isinstance(answer, dict):
            answer_text = str(answer.get('text', '')).strip()
        key = (name.lower(), answer_text.lower())
        if name and answer_text and key not in seen:
            seen.add(key)
            out.append(q)
    return out


def strip_faq_microdata(soup):
    changed = False
    # Remove duplicate microdata only from FAQ/Question/Answer schema blocks.
    selectors = [
        '[itemtype="https://schema.org/FAQPage"]', '[itemtype="http://schema.org/FAQPage"]',
        '[itemtype="https://schema.org/Question"]', '[itemtype="http://schema.org/Question"]',
        '[itemtype="https://schema.org/Answer"]', '[itemtype="http://schema.org/Answer"]',
    ]
    roots = soup.select(','.join(selectors))
    for root in roots:
        for node in [root] + list(root.find_all(True)):
            for attr in ('itemscope', 'itemtype', 'itemprop'):
                if node.has_attr(attr):
                    del node[attr]
                    changed = True
    return changed


def fix_file(path: Path):
    html = path.read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script', type='application/ld+json')
    faq_scripts = []
    faq_entities = []
    repaired_invalid = False

    for s in scripts:
        txt = (s.string or s.get_text() or '').strip()
        if not is_faq_jsonld_text(txt):
            continue
        candidate = clean_double_braced_json(txt)
        parsed = None
        try:
            parsed = json.loads(candidate)
        except Exception:
            # If it still cannot parse, leave it alone unless it is an obvious FAQ script.
            continue
        entities = collect_faq_entities(parsed)
        if entities:
            faq_scripts.append(s)
            faq_entities.extend(copy.deepcopy(entities))
            if candidate != txt:
                repaired_invalid = True

    microdata_changed = strip_faq_microdata(soup)

    faq_entities = unique_questions(faq_entities)
    jsonld_changed = False
    if faq_entities and (len(faq_scripts) > 1 or repaired_invalid):
        # Remove all existing FAQPage JSON-LD scripts and insert one consolidated version.
        first_location = faq_scripts[0]
        for s in faq_scripts:
            s.decompose()
        faq_obj = {
            '@context': SCHEMA_URL,
            '@type': 'FAQPage',
            'mainEntity': faq_entities,
        }
        new_script = soup.new_tag('script', type='application/ld+json')
        new_script.string = '\n' + json.dumps(faq_obj, ensure_ascii=False, indent=2) + '\n'
        if soup.head:
            # Place after existing non-FAQ JSON-LD scripts in the head when possible.
            head_scripts = soup.head.find_all('script', type='application/ld+json')
            if head_scripts:
                head_scripts[-1].insert_after(new_script)
            else:
                soup.head.append(new_script)
        else:
            soup.insert(0, new_script)
        jsonld_changed = True

    if microdata_changed or jsonld_changed:
        path.write_text(str(soup), encoding='utf-8')
        return {'file': str(path), 'jsonld_changed': jsonld_changed, 'microdata_changed': microdata_changed, 'faq_questions': len(faq_entities), 'faq_scripts': len(faq_scripts)}
    return None


def main():
    changed = []
    for path in sorted(ROOT.rglob('*.html')):
        if '.git' in path.parts:
            continue
        res = fix_file(path)
        if res:
            changed.append(res)
    print(f'Changed files: {len(changed)}')
    for r in changed[:500]:
        print(f"{r['file']} | jsonld={r['jsonld_changed']} microdata={r['microdata_changed']} questions={r['faq_questions']} faq_scripts={r['faq_scripts']}")

if __name__ == '__main__':
    main()
