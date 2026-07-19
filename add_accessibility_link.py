import os

count = 0
for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    content = fh.read()
            except:
                continue
            orig = content
            # Add accessibility link to footer if not already there
            if '/accessibility' not in content and '/sitemap.html' in content:
                content = content.replace(
                    '<a href="/sitemap.html">Sitemap</a>',
                    '<a href="/sitemap.html">Sitemap</a> &middot; <a href="/accessibility">Accessibility</a>'
                )
            if content != orig:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                count += 1

print(f'Added accessibility link to {count} footers')
