import re
import os

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('--- blog.html Content ---')
match = re.search(r'<div class="grid.*?">.*?</div>', html, flags=re.DOTALL)
if match:
    print('Found grid element:')
    print(match.group(0)[:500])
else:
    print('No grid element found. Looking for <a> tags to see what blog links look like:')
    for m in re.finditer(r'<a[^>]+href="[^"]*blog-[^"]*"[^>]*>.*?</a>', html, flags=re.DOTALL):
        print(m.group(0)[:200])

print('\n--- index.html Mega Nav ---')
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

match = re.search(r'<div class="nav-dd-panel mega">.*?</div>', index_html, flags=re.DOTALL)
if match:
    print(match.group(0)[:800])
else:
    print('No mega nav found.')
