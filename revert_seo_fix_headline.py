import os, re

bundle_path = 'bundle.js'
index_path = 'index.html'

# 1. REVERT INDEX.HTML
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Revert Title
    html = re.sub(r'<title>.*?</title>', 
                  '<title>C-Bus &amp; DALI Lighting Control Specialists Sydney | Sydney Automation Co</title>', 
                  html)
    
    # Revert Meta Description
    # We need to be careful with the description since it might have been changed multiple times.
    # We'll replace the one we just injected.
    new_desc = 'Sydney\'s #1 Emergency C-Bus &amp; Dynalite Resurrection Team. Based in Menai. Same-day fault finding, manufacturer-level repairs and system stabilization. Don\'t replace—restore. Call 0422 469 739.'
    old_desc = 'Accredited C-Bus programmer and Dynalite system designer based in Menai, Sydney. Same-day fault finding, repairs and commissioning. Call 0422 469 739.'
    
    html = html.replace(new_desc, old_desc)
    # Also handle the variant if the first replace failed
    html = re.sub(r'<meta content="Sydney\'s #1 Emergency.*?" name="description"/>',
                  f'<meta content="{old_desc}" name="description"/>',
                  html)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Reverted index.html Title and Meta Description.")

# 2. UPDATE BUNDLE.JS HEADLINE
if os.path.exists(bundle_path):
    with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace "Resurrection Team" with "Emergency Team"
    # We injected "Sydney\'s #1 Emergency C-Bus & Dynalite Resurrection Team"
    old_headline = "Sydney's #1 Emergency C-Bus & Dynalite Resurrection Team"
    new_headline = "Sydney's #1 Emergency C-Bus & Dynalite Emergency Team"
    
    content = content.replace(old_headline, new_headline)
    
    with open(bundle_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated Hero Headline in bundle.js.")

# 3. RUN CACHE BUSTER
# (Will run separately via command line)
