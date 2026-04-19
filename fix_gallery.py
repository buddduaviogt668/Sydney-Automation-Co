with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

old = '.gallery-grid img{width:100%;height:auto;display:block;max-height:400px;object-fit:cover}'

new = '''.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.gallery-grid img{width:100%;height:200px;display:block;object-fit:cover;border-radius:8px;transition:filter 0.3s ease,transform 0.3s ease;cursor:pointer}
.gallery-grid img:hover{filter:blur(2px) brightness(1.1);transform:scale(1.03)}'''

html = html.replace(old, new)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done.')