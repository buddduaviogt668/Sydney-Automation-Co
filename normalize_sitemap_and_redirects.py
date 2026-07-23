from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json

ROOT=Path('.')
DOMAIN='https://sydneyautomationco.com.au'
SM_NS='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', SM_NS)


def clean_path(path):
    path = path.rstrip('/') or '/'
    if path.endswith('.html'):
        path = path[:-5]
    return path or '/'


def path_exists(path):
    if path == '/':
        return (ROOT/'index.html').exists()
    return (ROOT/(path.lstrip('/')+'.html')).exists()


def normalize_redirects():
    vf=ROOT/'vercel.json'
    data=json.loads(vf.read_text(encoding='utf-8'))
    redirect_map={}
    for r in data.get('redirects',[]):
        src=clean_path(r.get('source',''))
        dest=r.get('destination','')
        if dest.startswith('/'):
            redirect_map[src]=clean_path(dest)
        if r.get('destination') in {'/dynalite-repair-sydney.html'}:
            r['destination']='/dynalite-repair-sydney'
    vf.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    return redirect_map


def normalize_sitemap(redirect_map):
    sf=ROOT/'sitemap.xml'
    tree=ET.parse(sf)
    root=tree.getroot()
    url_nodes=list(root.findall(f'{{{SM_NS}}}url'))
    canonical=[]
    removed=[]
    changed=[]
    for url_node in url_nodes:
        loc=url_node.find(f'{{{SM_NS}}}loc')
        if loc is None or not loc.text:
            root.remove(url_node); continue
        old_url=loc.text.strip()
        old_path=urlparse(old_url).path.rstrip('/') or '/'
        p=clean_path(old_path)
        if not path_exists(p):
            dest=redirect_map.get(p)
            if dest and path_exists(dest):
                p=dest
            else:
                removed.append(old_path)
                root.remove(url_node)
                continue
        new_url=DOMAIN + ('' if p=='/' else p)
        if new_url != old_url:
            changed.append((old_url,new_url))
        loc.text=new_url
        canonical.append((p,url_node))
    seen=set()
    for p,node in canonical:
        if p in seen and node in list(root):
            root.remove(node)
        seen.add(p)
    tree.write(sf, encoding='utf-8', xml_declaration=True)
    return changed, removed, len(seen)


def main():
    redirects=normalize_redirects()
    changed, removed, count=normalize_sitemap(redirects)
    print(f'Canonical sitemap URLs retained: {count}')
    print(f'Sitemap URLs normalized: {len(changed)}')
    print(f'Non-resolving sitemap URLs removed: {len(removed)}')
    if removed:
        print('Removed:')
        for r in removed: print(r)

if __name__=='__main__':
    main()
