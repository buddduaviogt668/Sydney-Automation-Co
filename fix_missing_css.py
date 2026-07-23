import glob

count = 0
for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        if 'index.css' not in html:
            print(f'{filepath} is missing index.css')
            html = html.replace('</head>', '<link rel="stylesheet" href="/index.css">\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
    except Exception as e:
        print(f"Error on {filepath}: {e}")
        
print(f'Fixed {count} files by adding index.css')
