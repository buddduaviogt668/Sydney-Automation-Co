import os
import re

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"

html_files = []
for root, dirs, files in os.walk(DIR):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

modified_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact string to find:
    # body { padding-top: 72px !important; }
    # Let's replace it with:
    # body { padding-top: 72px !important; } nav { top: 72px !important; }
    
    # We use regex to handle any whitespace variations
    pattern = r'(body\s*\{\s*padding-top:\s*72px\s*!important;\s*\})'
    
    # Check if nav { top: 72px !important; } is already there
    if 'nav { top: 72px !important; }' in content:
        continue

    # Only replace if the file HAS #sticky-cta-bar
    if 'id="sticky-cta-bar"' in content and re.search(pattern, content):
        new_content = re.sub(pattern, r'\1\n      nav { top: 72px !important; }', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_count += 1

print(f"Fixed banner blocking hamburger in {modified_count} files.")
