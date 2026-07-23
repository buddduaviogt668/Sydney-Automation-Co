import os, glob, re
from collections import Counter

root = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'
files = glob.glob(os.path.join(root, '*.html'))

print(f'Total HTML files: {len(files)}')

# Check URL cleanliness
bad_urls = []
for f in files:
    name = os.path.basename(f)
    if re.search(r'[A-Z _]', name) or '--' in name or name.startswith('-') or name.endswith('-.html'):
        bad_urls.append(name)

print(f'Bad/unclean URLs: {len(bad_urls)}')
if bad_urls[:5]:
    print('Samples:', bad_urls[:5])

# Check canonical tags in sample
no_canonical = []
for f in files[:100]:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    if 'rel="canonical"' not in content:
        no_canonical.append(os.path.basename(f))

print(f'Missing canonical (sample 100): {len(no_canonical)}')

# Check sitemap
sitemap = os.path.join(root, 'sitemap.xml')
if os.path.exists(sitemap):
    with open(sitemap, 'r', encoding='utf-8', errors='ignore') as fh:
        sm_content = fh.read()
    url_count = sm_content.count('<url>')
    print(f'Sitemap URL entries: {url_count}')
else:
    print('sitemap.xml NOT FOUND')

# Check nav/home links in sample
no_nav = []
for f in files[:50]:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    has_home = ('href="/"' in content or 'href="/index' in content or '<nav' in content)
    if not has_home:
        no_nav.append(os.path.basename(f))

print(f'Pages with no nav/home link (sample 50): {len(no_nav)}')

# Check word count / thin content
thin_pages = []
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    text = re.sub(r'<[^>]+>', ' ', content)
    words = len(text.split())
    if words < 200:
        thin_pages.append((os.path.basename(f), words))

print(f'Pages with < 200 words of text: {len(thin_pages)}')
if thin_pages[:5]:
    print('Sample thin pages:', thin_pages[:5])
