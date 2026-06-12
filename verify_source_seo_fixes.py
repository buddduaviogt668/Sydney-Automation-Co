from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json, re

ROOT=Path('.')
DOMAIN='https://sydneyautomationco.com.au'


def sitemap_paths():
    tree=ET.parse(ROOT/'sitemap.xml')
    ns={'sm':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    out=[]
    for loc in tree.findall('.//sm:loc', ns):
        p=urlparse(loc.text.strip()).path.rstrip('/') or '/'
        out.append(p)
    return sorted(set(out))


def path_to_file(path):
    if path=='/': return ROOT/'index.html'
    return ROOT/(path.lstrip('/')+'.html')


def file_to_path(f):
    rel=str(f.relative_to(ROOT))
    if rel=='index.html': return '/'
    return '/' + rel[:-5]


def collect_links():
    links=[]
    inlinks={p:set() for p in sitemap_paths()}
    sitemap_set=set(inlinks)
    missing=[]
    for f in ROOT.rglob('*.html'):
        if '.git' in f.parts: continue
        src=file_to_path(f)
        soup=BeautifulSoup(f.read_text(encoding='utf-8', errors='ignore'),'html.parser')
        for a in soup.find_all('a', href=True):
            href=a['href'].strip()
            if not href or href.startswith(('tel:','mailto:','#','javascript:')): continue
            if href.startswith(DOMAIN): target=urlparse(href).path
            elif href.startswith('/'): target=urlparse(href).path
            else: continue
            target=target.rstrip('/') or '/'
            links.append((src,target))
            if target in sitemap_set and target!=src:
                inlinks[target].add(src)
            # ignore assets, anchors resolved as paths, and legacy external directories not in sitemap
            if target.startswith('/wp-') or target in {'/privacy-policy'}:
                pass
    return links,inlinks


def audit_faq():
    problems=[]
    for f in ROOT.rglob('*.html'):
        if '.git' in f.parts: continue
        soup=BeautifulSoup(f.read_text(encoding='utf-8', errors='ignore'),'html.parser')
        faq_jsonld=0; invalid=[]
        for i,s in enumerate(soup.find_all('script', type='application/ld+json'),1):
            txt=(s.string or s.get_text() or '').strip()
            if 'FAQPage' in txt: faq_jsonld += txt.count('FAQPage')
            try: json.loads(txt)
            except Exception as e: invalid.append((i,str(e)))
        micro=len(soup.select('[itemtype="https://schema.org/FAQPage"],[itemtype="http://schema.org/FAQPage"]'))
        if faq_jsonld+micro>1 or invalid:
            problems.append((str(f),faq_jsonld,micro,invalid))
    return problems


def main():
    sp=sitemap_paths()
    missing_files=[p for p in sp if not path_to_file(p).exists()]
    links,inlinks=collect_links()
    no_inlinks=[p for p in sp if p!='/' and not inlinks[p] and path_to_file(p).exists()]
    faq=audit_faq()
    data=json.loads((ROOT/'vercel.json').read_text())
    blog_redirects=[r for r in data.get('redirects',[]) if r.get('source') in {'/blog/:slug','/blog/:slug/'}]
    print(f'Sitemap URLs: {len(sp)}')
    print(f'Sitemap URLs missing source HTML files: {len(missing_files)}')
    print(f'Sitemap source pages with no internal inlinks: {len(no_inlinks)}')
    print(f'Structured data duplicate/invalid FAQ problems: {len(faq)}')
    print(f'Problematic /blog/:slug redirects remaining: {len(blog_redirects)}')
    if missing_files:
        print('\nMissing source files:')
        for p in missing_files[:100]: print(p)
    if no_inlinks:
        print('\nNo-inlink sitemap pages:')
        for p in no_inlinks[:100]: print(p)
    if faq:
        print('\nFAQ problems:')
        for row in faq[:20]: print(row)

if __name__=='__main__':
    main()
