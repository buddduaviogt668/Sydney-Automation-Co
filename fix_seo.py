import os, re

BASE_URL = "https://sydneyautomationco.com.au/"
files = [f for f in os.listdir('.') if f.endswith('.html')]

# List of files that SHOULD NOT be indexed
NO_INDEX = ['404.html', 'suburb-directory-snippet.html']

for file in files:
    print(f"Processing {file}...")
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # 1. Ensure robots meta exists
    if file in NO_INDEX:
        robots_tag = '<meta name="robots" content="noindex, nofollow"/>'
    else:
        robots_tag = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>'
    
    if 'name="robots"' in html.lower() or 'name=\'robots\'' in html.lower():
        # Update existing
        html = re.sub(r'<meta[^>]*name=["\']robots["\'][^>]*>', robots_tag, html, flags=re.IGNORECASE)
    else:
        # Inject after <head> or before </head>
        if '<head>' in html:
            html = html.replace('<head>', f'<head>\n{robots_tag}')
        else:
            # If no head, inject at top
            html = robots_tag + "\n" + html

    # 2. Ensure canonical tag exists
    slug = file.replace('.html', '')
    if slug == 'index':
        canonical_url = BASE_URL
    else:
        canonical_url = f"{BASE_URL}{slug}"
    
    canonical_tag = f'<link rel="canonical" href="{canonical_url}"/>'
    
    if 'rel="canonical"' in html.lower() or 'rel=\'canonical\'' in html.lower():
        # Update existing
        html = re.sub(r'<link[^>]*rel=["\']canonical["\'][^>]*>', canonical_tag, html, flags=re.IGNORECASE)
    else:
        # Inject after robots tag or after <head>
        html = html.replace(robots_tag, f"{robots_tag}\n{canonical_tag}")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("SEO fix complete for all HTML files.")
