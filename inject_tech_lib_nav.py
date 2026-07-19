import os
import re

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"

html_files = []
for root, dirs, files in os.walk(DIR):
    if '.git' in root or 'tech-library' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

tech_lib_dir = os.path.join(DIR, 'tech-library')
if os.path.exists(tech_lib_dir):
    for f in os.listdir(tech_lib_dir):
        if f.endswith('.html'):
            html_files.append(os.path.join(tech_lib_dir, f))

modified_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected (but allow the tech-library.html file itself to get its own nav updated)
    if content.count('href="/tech-library.html"') > 1 or (content.count('href="/tech-library.html"') > 0 and 'tech-library.html' not in file_path):
        continue

    def replace_func(match):
        whitespace = match.group(1) or ''
        li_open = match.group(2) or ''
        li_close = match.group(3) or ''
        
        new_line = f'{whitespace}{li_open}<a href="/tech-library.html">Tech Library</a>{li_close}\n{match.group(0)}'
        return new_line

    new_content = re.sub(r'^([ \t]*)(<li>)?<a href="/blog">Blog</a>(</li>)?\s*$', replace_func, content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1

print(f"Injected into {modified_count} files.")
