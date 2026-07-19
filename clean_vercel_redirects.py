import json
import os

# Load vercel.json
with open('vercel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get all existing HTML files (clean URLs without .html)
existing_paths = set()
for root, _, files in os.walk('.'):
    if '.git' in root or '.gemini' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, file), '.').replace('\\', '/')
            # Convert to clean URL
            if rel == 'index.html':
                existing_paths.add('/')
            elif rel.endswith('.html'):
                existing_paths.add('/' + rel[:-5])

# Filter out redirects where the source path now has an actual file
# (i.e., file has been restored and redirect is no longer needed)
redirects = data.get('redirects', [])
original_count = len(redirects)
kept = []
removed = []

for r in redirects:
    source = r.get('source', '')
    # Only remove if it's an exact path match (no regex/wildcards) AND the file now exists
    if ':' not in source and '(' not in source and source in existing_paths:
        removed.append(source)
    else:
        kept.append(r)

data['redirects'] = kept

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Original redirects: {original_count}")
print(f"Removed {len(removed)} stale redirects for restored pages:")
for r in removed:
    print(f"  - {r}")
print(f"Remaining redirects: {len(kept)}")
