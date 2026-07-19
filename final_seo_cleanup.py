import os, re

# 1. FIX BROKEN IMAGES IN projects.html
projects_path = 'projects.html'
if os.path.exists(projects_path):
    with open(projects_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove Kebia images or replace with placeholders
    # The audit found /kebia-01.jpg and /kebia-02.jpg are broken.
    # I'll replace them with a 'Coming Soon' div or just remove the img tags.
    placeholder_html = '<div style="width:100%;height:200px;background:#0d1a30;display:flex;align-items:center;justify-content:center;color:#6a8cb5;font-size:12px;font-weight:700">IMAGE COMING SOON</div>'
    
    content = re.sub(r'<img[^>]+src=["\']/kebia-01\.jpg["\'][^>]*>', placeholder_html, content)
    content = re.sub(r'<img[^>]+src=["\']/kebia-02\.jpg["\'][^>]*>', placeholder_html, content)
    
    # Also update the gallery script for Kebia
    content = content.replace('{"src": "/kebia-01.jpg", "title": ""}', '{"src": "/og-image.jpg", "title": "Kebia - Image Coming Soon"}')
    content = content.replace('{"src": "/kebia-02.jpg", "title": ""}', '{"src": "/og-image.jpg", "title": "Kebia - Image Coming Soon"}')

    with open(projects_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Fixed broken images in projects.html")

# 2. FIX CANONICALS & NOINDEX
files_to_noindex = ['404.html', 'suburb-directory-snippet.html']
for file in files_to_noindex:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        # Ensure noindex
        if 'noindex' not in html:
            html = re.sub(r'<head>', '<head>\n<meta name="robots" content="noindex, nofollow"/>', html)
        
        # Remove canonical or point to home
        html = re.sub(r'<link rel="canonical" href="[^"]+"/>', '', html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"SUCCESS: Cleaned up SEO tags for {file}")

# 3. GLOBAL DEDUPE & NORMALIZATION
files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    new_lines = []
    seen_desc = False
    seen_robots = False
    seen_canonical = False
    
    for line in lines:
        is_desc = 'name="description"' in line.lower()
        is_robots = 'name="robots"' in line.lower()
        is_canonical = 'rel="canonical"' in line.lower()
        
        if is_desc:
            if not seen_desc:
                new_lines.append(line)
                seen_desc = True
            continue
        if is_robots:
            if not seen_robots:
                new_lines.append(line)
                seen_robots = True
            continue
        if is_canonical:
            if not seen_canonical:
                new_lines.append(line)
                seen_canonical = True
            continue
        new_lines.append(line)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("SUCCESS: Global meta deduplication complete.")
