import os
import glob
import re
from collections import defaultdict

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

html_files = glob.glob(os.path.join(DIR, "*.html"))
all_basenames = [os.path.basename(f) for f in html_files]

# 1. ORPHAN CHECK
print("--- ORPHAN CHECK ---")
linked_files = set()

# We consider a file linked if its basename appears in an href anywhere.
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # find all hrefs
            hrefs = re.findall(r'href=["\']/?([^"\']*\.html?)["\']', content)
            hrefs_no_ext = re.findall(r'href=["\']/?([^"\']+)["\']', content)
            
            for h in hrefs:
                linked_files.add(os.path.basename(h))
            for h in hrefs_no_ext:
                # Add .html to see if it matches a file
                if not h.endswith(".html") and not h.startswith("http") and not h.startswith("#") and not h.startswith("tel:") and not h.startswith("mailto:"):
                    linked_files.add(os.path.basename(h) + ".html")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

# The sitemap.html is linked from the footer usually, and it links to a lot of things.
orphans = []
for base in all_basenames:
    if base not in linked_files and base != "index.html" and base != "old_index.html":
        orphans.append(base)

print(f"Found {len(orphans)} orphaned HTML files (not linked anywhere internally):")
if len(orphans) < 20:
    for o in orphans:
        print("  -", o)
else:
    print(f"  {len(orphans)} files... (too many to print, will link them all via a location index update)")

# 2. DUPLICATE CHECK (Cannibalization)
print("\n--- DUPLICATE CONTENT CHECK ---")
title_map = defaultdict(list)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                title_map[title].append(os.path.basename(filepath))
    except Exception:
        pass

duplicates = {t: files for t, files in title_map.items() if len(files) > 1}
if duplicates:
    print(f"Found {len(duplicates)} exact <title> duplicates (potential cannibalization):")
    count = 0
    for t, files in duplicates.items():
        if count < 10:
            print(f"Title: '{t}' is used by:")
            for f in files:
                print(f"  - {f}")
        count += 1
else:
    print("No exact title duplicates found! Great SEO hygiene.")

# 3. CHECK INNER CITY SUBURBS
print("\n--- INNER CITY SUBURBS CHECK ---")
inner_city = ["Sydney CBD", "Surry Hills", "Darlinghurst", "Redfern", "Pyrmont", "Ultimo", 
              "Haymarket", "Potts Point", "Woolloomooloo", "Paddington", "Alexandria", 
              "Waterloo", "Zetland"]

missing = []
for suburb in inner_city:
    slug = suburb.lower().replace(" ", "-")
    expected_repair = f"cbus-repair-{slug}.html"
    if expected_repair not in all_basenames:
        missing.append(suburb)

print(f"Missing full targeted coverage for {len(missing)} Inner City suburbs: {', '.join(missing)}")
