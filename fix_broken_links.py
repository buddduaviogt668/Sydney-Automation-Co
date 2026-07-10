import os
import re
from urllib.parse import urlparse

def get_mapped_url(url):
    path = urlparse(url).path
    if not path:
        return url
        
    path = '/' + path.lstrip('/')
    
    # Mapping rules
    if path.startswith('/c-bus-programmer-') or path.startswith('/cbus-programmer-'):
        return '/c-bus-programmer-sydney'
    elif path.startswith('/dynalite-programmer-'):
        return '/dynalite-programmer-sydney'
    elif path.startswith('/lighting-control-repair-sydney'):
        return '/cbus-repair-sydney'
    elif path.startswith('/cbus-repair-'):
        return '/cbus-repair-sydney'
    elif path.startswith('/dynalite-repair-'):
        return '/dynalite-repair-sydney'
    elif 'rapix' in path:
        return '/services'
    elif 'emergency-lighting' in path:
        return '/emergency-lighting-compliance-afss-sydney'
    elif path.startswith('/cbus-maintenance-sydney') or path.startswith('/dynalite-maintenance-sydney'):
        return '/services'
    elif path.startswith('/cbus-vs-dynalite'):
        return '/c-bus-vs-dynalite-vs-knx-comparison-sydney' # Best match for comparison page
    elif path.startswith('/real-estate-cbus-audit-sydney') or path.startswith('/how-to-choose-cbus-specialist-sydney'):
        return '/cbus-specialist-sydney'
    elif path.startswith('/dynalite-vs-cbus-sydney'):
        return '/c-bus-vs-dynalite-vs-knx-comparison-sydney'
    elif path.startswith('/facility-managers-cbus-dynalite-dali-guide'):
        return '/building-managers-lighting-control-nsw'
    else:
        # Fallback for remaining broken links
        return '/services'

def fix_broken_links(directory):
    html_files = []
    for root, _, files in os.walk(directory):
        if '.git' in root or '.gemini' in root: continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    valid_paths = set()
    for file in html_files:
        rel_path = os.path.relpath(file, directory).replace('\\', '/')
        if rel_path == 'index.html':
            valid_paths.add('/')
        else:
            valid_paths.add('/' + rel_path)
            if rel_path.endswith('.html'):
                valid_paths.add('/' + rel_path[:-5])
            if rel_path.endswith('/index.html'):
                valid_paths.add('/' + rel_path[:-11])

    href_pattern = re.compile(r'href="([^"]+)"')
    files_updated = 0
    links_fixed = 0
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                original_content = f.read()
            except Exception:
                continue
                
        links = href_pattern.findall(original_content)
        replacements = {}
        
        for link in links:
            if link.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                continue
                
            parsed = urlparse(link)
            path = parsed.path
            if not path:
                continue
                
            test_path = '/' + path.lstrip('/')
            
            if test_path not in valid_paths:
                possible_file1 = os.path.join(directory, test_path.lstrip('/') + '.html')
                possible_file2 = os.path.join(directory, test_path.lstrip('/'))
                possible_file3 = os.path.join(directory, test_path.lstrip('/'), 'index.html')
                
                if not (os.path.exists(possible_file1) or os.path.exists(possible_file2) or os.path.exists(possible_file3)):
                    # Link is broken! Map it.
                    mapped = get_mapped_url(link)
                    replacements[f'href="{link}"'] = f'href="{mapped}"'
                    
        if replacements:
            new_content = original_content
            for old_str, new_str in replacements.items():
                new_content = new_content.replace(old_str, new_str)
                links_fixed += new_content.count(new_str) - original_content.count(new_str) # Rough estimate
            
            if new_content != original_content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                
    return files_updated, links_fixed

files, links = fix_broken_links('.')
print(f"Updated {files} files and rewrote approximately {links} links.")
