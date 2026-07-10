import json
import os
import re

# Get all href values pointing to /c-bus-programmer-*, /dynalite-programmer-*, 
# /cbus-repair-*, /dynalite-repair-* that DON'T have a physical file

def get_all_broken_suburb_hrefs(directory, prefixes):
    html_files = []
    for root, _, files in os.walk(directory):
        if '.git' in root or '.gemini' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    href_pattern = re.compile(r'href="(/[^"#?]+)"')
    all_hrefs = set()

    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        for href in href_pattern.findall(content):
            for prefix in prefixes:
                if href.startswith(prefix):
                    all_hrefs.add(href)

    # Now filter to only ones that don't have a physical file
    broken = set()
    for href in all_hrefs:
        path = href.lstrip('/')
        possible1 = os.path.join(directory, path + '.html')
        possible2 = os.path.join(directory, path)
        possible3 = os.path.join(directory, path, 'index.html')
        if not (os.path.exists(possible1) or os.path.exists(possible2) or os.path.exists(possible3)):
            broken.add(href)

    return sorted(broken)

# Also scan git history/logs for deleted pages
# We'll use a comprehensive list of known deleted patterns from the nav menus

prefixes = [
    '/c-bus-programmer-',
    '/cbus-programmer-',
    '/dynalite-programmer-',
    '/cbus-repair-',
    '/dynalite-repair-',
    '/lighting-control-repair-',
]

broken_hrefs = get_all_broken_suburb_hrefs('.', prefixes)
print(f"Found {len(broken_hrefs)} unique broken suburb URLs")

# Build mapping
def get_destination(href):
    if href.startswith('/c-bus-programmer-') or href.startswith('/cbus-programmer-'):
        return '/c-bus-programmer-sydney'
    elif href.startswith('/dynalite-programmer-'):
        return '/dynalite-programmer-sydney'
    elif href.startswith('/cbus-repair-'):
        return '/cbus-repair-sydney'
    elif href.startswith('/dynalite-repair-'):
        return '/dynalite-repair-sydney'
    elif href.startswith('/lighting-control-repair-'):
        return '/cbus-repair-sydney'
    return '/services'

redirects = []
for href in broken_hrefs:
    redirects.append({
        "source": href,
        "destination": get_destination(href),
        "permanent": True
    })

# Also add the most common ones from the site that might not be linked but are in Google
common_deleted = [
    ('/c-bus-programmer-sutherland-shire', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-eastern-suburbs', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-north-shore', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-northern-beaches', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-inner-west', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-hills-district', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-st-george', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-parramatta', '/c-bus-programmer-sydney'),
    ('/c-bus-programmer-sydney-cbd', '/c-bus-programmer-sydney'),
    ('/facility-managers-cbus-dynalite-dali-guide', '/building-managers-lighting-control-nsw'),
    ('/cbus-maintenance-sydney', '/services'),
    ('/dynalite-maintenance-sydney', '/services'),
    ('/cbus-vs-dynalite', '/cbus-vs-dynalite'),  # This page exists, skip
    ('/rapix-emergency-lighting-sydney', '/rapix-lighting-control'),
    ('/emergency-lighting-train-stations-infrastructure-sydney', '/emergency-lighting-compliance-afss-sydney'),
    ('/lighting-control-repair-sydney', '/cbus-repair-sydney'),
]

# Filter out ones where source == destination, and ones already in redirects list
existing_sources = {r['source'] for r in redirects}
for source, dest in common_deleted:
    if source != dest and source not in existing_sources:
        # Check it doesn't already exist as a file
        path = source.lstrip('/')
        possible1 = os.path.join('.', path + '.html')
        possible2 = os.path.join('.', path)
        if not (os.path.exists(possible1) or os.path.exists(possible2)):
            redirects.append({'source': source, 'destination': dest, 'permanent': True})
            existing_sources.add(source)

print(f"Total explicit redirects to add: {len(redirects)}")

# Load vercel.json and update - REMOVE the broken wildcard rules first, add explicit ones
with open('vercel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove the old broken wildcard redirects
bad_sources = {
    '/c-bus-programmer-(?!sydney)(.*)',
    '/cbus-programmer-(?!sydney)(.*)',
    '/dynalite-programmer-(?!sydney)(.*)',
    '/cbus-repair-(?!sydney)(.*)',
    '/dynalite-repair-(?!sydney)(.*)',
    '/lighting-control-repair-(?!sydney)(.*)',
}

existing_redirects = [r for r in data.get('redirects', []) if r.get('source') not in bad_sources]

# Prepend our new explicit redirects
data['redirects'] = redirects + existing_redirects

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("vercel.json updated successfully with explicit redirects.")
