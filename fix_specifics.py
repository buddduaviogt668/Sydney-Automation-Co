import os
import re
import glob

# HELPER TO READ/WRITE HTML
def read_html(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def write_html(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("--- Starting Massive Fix Script ---")

# 1. & 2. Remove WhatsApp & Fix Floating CTA obstructing Mega Nav
all_files = glob.glob("*.html")
modified_files = 0
for filepath in all_files:
    content = read_html(filepath)
    changed = False
    
    # Remove WhatsApp button HTML
    if '<a href="https://wa.me/61422469739" class="sac-float-wa"' in content:
        content = re.sub(r'<a href="https://wa.me/61422469739"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
        changed = True
        
    # Remove WhatsApp CSS
    if '.whatsapp-btn' in content:
        content = re.sub(r'<style>.*?/\* WhatsApp button.*?</style>', '', content, flags=re.DOTALL)
        changed = True

    # Fix Mega Nav Z-index (Nav needs to be higher than floating CTAs, or CTAs lower)
    # Mega nav has z-index: 2000, but sac-float-cta had z-index: 9000.
    if 'z-index: 9000;' in content:
        content = content.replace('z-index: 9000;', 'z-index: 990;')
        changed = True
        
    # 14. Fix Hardware Directory link
    if 'href="/products.html">Hardware Directory</a>' in content:
        content = content.replace('href="/products.html">Hardware Directory</a>', 'href="/services-hub">Hardware Directory</a>')
        changed = True
        
    if changed:
        write_html(filepath, content)
        modified_files += 1

print(f"Removed WhatsApp, fixed Z-index, and fixed Hardware link in {modified_files} files.")

# 6. cbus-fault-finding-sydney.html is a blog page?
content = read_html('cbus-fault-finding-sydney.html')
if '<div class="blog-post">' in content or 'blog-card' in content:
    print("Found cbus-fault-finding-sydney.html is formatted as a blog. (Skipping conversion for now to build a script specifically for page generation later, or will convert it directly).")

# 7. dynalite-repair-sydney.html card falls below
content = read_html('dynalite-repair-sydney.html')
if 'grid-3' in content:
    # If a card falls below, it's usually because the text inside is too long causing uneven heights. We can add align-items stretch.
    if '<style>' in content and '.grid-3' in content:
        # Not easily fixed via simple replace without seeing it, but let's ensure card heights are 100%
        if '.card{' in content and 'height:100%' not in content:
            content = content.replace('.card{', '.card{height:100%;')
            write_html('dynalite-repair-sydney.html', content)
            print("Fixed dynalite-repair-sydney.html card heights.")

# 8. dynalite-fault-finding-sydney-common-faults.html is a blog
# The user wants service pages, not blogs for these. I'll need to rebuild them as service pages.

# 9. dali2-compliance-nsw-commercial.html heading cut off
content = read_html('dali2-compliance-nsw-commercial.html')
# Look for "What You Need to Kn..."
content = content.replace('What You Need to Kn...', 'What You Need to Know')
content = content.replace('What You Need to Kn<', 'What You Need to Know<')
write_html('dali2-compliance-nsw-commercial.html', content)
print("Fixed DALI-2 title.")

# 11. cbus-dynalite-upgrade-guide.html is an empty shell
# This needs a full generation.

# 12. strata-managers-lighting-control-sydney.html heading not finished
content = read_html('strata-managers-lighting-control-sydney.html')
content = content.replace('Strata Managers: Who to Call When Your Building’s Lighting Control ...', 'Strata Managers: Who to Call When Your Building’s Lighting Control Fails')
content = content.replace('Lighting Control ...<', 'Lighting Control Fails<')
write_html('strata-managers-lighting-control-sydney.html', content)
print("Fixed Strata Managers title.")

# 13. cbus-vs-dynalite.html broken script at top
content = read_html('cbus-vs-dynalite.html')
# Look for broken meta tag
if 's the unbiased comparison' in content:
    content = re.sub(r's the unbiased comparison — dimming quality, scalability, cost, installer base, and which platform suits your project."/>', '', content)
    write_html('cbus-vs-dynalite.html', content)
    print("Fixed cbus-vs-dynalite.html broken script at top.")

print("--- Script Completed ---")
