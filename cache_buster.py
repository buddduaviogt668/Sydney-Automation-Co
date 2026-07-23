import os, re

index_path = 'index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Robust replace using regex to handle existing version strings
    new_v = '2026-05-06-01-45'
    html = re.sub(r'bundle\.js(\?v=[^"\']*)?', f'bundle.js?v={new_v}', html)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"SUCCESS: Cache buster updated to {new_v}")
