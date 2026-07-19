import json
with open('vercel.json', 'r') as f:
    data = json.load(f)
redirects = data.get('redirects', [])
print(f'Total redirects: {len(redirects)}')
print('First 20:')
for r in redirects[:20]:
    print("  " + r["source"] + " -> " + r["destination"])
