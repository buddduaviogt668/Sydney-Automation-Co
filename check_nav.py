import re

# Check what link should replace /automation-specialists
# Look at the nav structure to understand what it should point to
with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find nav section
nav_match = re.search(r'<nav.*?</nav>', content, re.DOTALL)
if nav_match:
    nav = nav_match.group(0)
    # Find all links
    links = re.findall(r'href="([^"]+)"', nav)
    print("Nav links on homepage:")
    for l in links:
        print(f"  {l}")

# Check what automation-related pages exist
import glob
auto_pages = [f for f in glob.glob('*.html') if 'automat' in f.lower()]
print(f"\nAutomation pages: {auto_pages}")
