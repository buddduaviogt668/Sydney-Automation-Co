from pathlib import Path
from bs4 import BeautifulSoup
import json, re, html
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

ROOT = Path('.')
DOMAIN = 'https://sydneyautomationco.com.au'
CARD_STYLE = "display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;"
HOVER = "this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'"
OUT = "this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'"


def slug_to_title(slug):
    slug = slug.strip('/').split('/')[-1]
    words = []
    for part in slug.replace('-', ' ').split():
        if part.lower() in {'cbus', 'c bus'}:
            words.append('C-Bus')
        elif part.lower() == 'dynalite':
            words.append('Dynalite')
        elif part.lower() == 'dali':
            words.append('DALI')
        elif part.lower() == 'sydney':
            words.append('Sydney')
        elif part.lower() == 'afss':
            words.append('AFSS')
        elif part.lower() == 'cbd':
            words.append('CBD')
        else:
            words.append(part.capitalize())
    return ' '.join(words)


def sitemap_paths():
    tree = ET.parse(ROOT / 'sitemap.xml')
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    paths = []
    for loc in tree.findall('.//sm:loc', ns):
        url = loc.text.strip()
        p = urlparse(url).path.rstrip('/') or '/'
        paths.append(p)
    return sorted(set(paths))


def html_file_for_path(path):
    if path == '/':
        return ROOT / 'index.html'
    return ROOT / (path.lstrip('/') + '.html')


def collect_source_inlinks():
    inlinks = {p: set() for p in sitemap_paths()}
    sitemap_set = set(inlinks)
    for f in ROOT.rglob('*.html'):
        if '.git' in f.parts:
            continue
        src_path = '/' if f.name == 'index.html' and f.parent == ROOT else '/' + str(f.relative_to(ROOT)).replace('.html', '').replace('index', '').strip('/')
        if src_path != '/':
            src_path = src_path.rstrip('/')
        try:
            soup = BeautifulSoup(f.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
        except Exception:
            continue
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            if not href or href.startswith(('tel:', 'mailto:', '#', 'javascript:')):
                continue
            if href.startswith(DOMAIN):
                target = urlparse(href).path
            elif href.startswith('/'):
                target = urlparse(href).path
            else:
                continue
            target = target.rstrip('/') or '/'
            if target in sitemap_set and target != src_path:
                inlinks[target].add(src_path)
    return inlinks


def build_section(paths):
    blog = [p for p in paths if p.startswith('/blog/')]
    service = [p for p in paths if p not in blog]
    def cards(items):
        return '\n'.join(
            f'  <a href="{html.escape(p)}" style="{CARD_STYLE}" onmouseover="{HOVER}" onmouseout="{OUT}">{html.escape(slug_to_title(p))}</a>'
            for p in items
        )
    section = f'''
<section id="crawlable-service-areas" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">📍</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">Crawlable Service Areas & Guides</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">This directory links sitemap pages that previously had no internal inlinks, so visitors and search crawlers can reach every live suburb, repair, and guide page from the main site navigation.</p>
    </div>
  </div>
  <h3 style="font-family:'Barlow Condensed',sans-serif;font-size:24px;font-weight:800;color:#f0f4ff;margin:24px 0 12px;">Suburb C-Bus & Dynalite Repair Pages</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
{cards(service)}
  </div>
  <h3 style="font-family:'Barlow Condensed',sans-serif;font-size:24px;font-weight:800;color:#f0f4ff;margin:36px 0 12px;">Technical Blog Guides</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
{cards(blog)}
  </div>
</section>
'''
    return section


def fix_services_hub():
    hub = ROOT / 'services-hub.html'
    text = hub.read_text(encoding='utf-8', errors='ignore')
    stripped = re.sub(r'\n<section id="crawlable-service-areas".*?</section>\n', '\n', text, flags=re.S)
    if stripped != text:
        hub.write_text(stripped, encoding='utf-8')
    inlinks = collect_source_inlinks()
    no_inlinks = sorted([p for p, links in inlinks.items() if p != '/' and not links and html_file_for_path(p).exists()])
    text = hub.read_text(encoding='utf-8', errors='ignore')
    section = build_section(no_inlinks)
    marker = '\n\n\n<footer>'
    if marker not in text:
        raise RuntimeError('Could not find services hub footer marker')
    text = text.replace(marker, '\n' + section + marker, 1)
    hub.write_text(text, encoding='utf-8')
    return no_inlinks


def fix_vercel_blog_redirects():
    vf = ROOT / 'vercel.json'
    data = json.loads(vf.read_text(encoding='utf-8'))
    before = len(data.get('redirects', []))
    data['redirects'] = [r for r in data.get('redirects', []) if r.get('source') not in {'/blog/:slug', '/blog/:slug/'}]
    after = len(data['redirects'])
    vf.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    return before - after


def main():
    no_inlinks = fix_services_hub()
    removed = fix_vercel_blog_redirects()
    print(f'Inserted crawlable links for {len(no_inlinks)} sitemap pages with no source inlinks.')
    print(f'Removed {removed} blog redirect rules that made /blog/:slug resolve to root URLs.')
    for p in no_inlinks[:200]:
        print(p)

if __name__ == '__main__':
    main()
