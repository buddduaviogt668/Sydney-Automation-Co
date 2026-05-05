import os

index_path = 'index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Add cache buster to bundle.js
    html = html.replace('bundle.js', 'bundle.js?v=2026-05-06-01-32')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Cache buster added to index.html")
