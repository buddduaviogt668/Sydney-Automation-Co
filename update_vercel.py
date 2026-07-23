import json
import os

with open('vercel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

wildcard_redirects = [
    {
        "source": "/c-bus-programmer-(?!sydney)(.*)",
        "destination": "/c-bus-programmer-sydney",
        "permanent": True
    },
    {
        "source": "/cbus-programmer-(?!sydney)(.*)",
        "destination": "/c-bus-programmer-sydney",
        "permanent": True
    },
    {
        "source": "/dynalite-programmer-(?!sydney)(.*)",
        "destination": "/dynalite-programmer-sydney",
        "permanent": True
    },
    {
        "source": "/cbus-repair-(?!sydney)(.*)",
        "destination": "/cbus-repair-sydney",
        "permanent": True
    },
    {
        "source": "/dynalite-repair-(?!sydney)(.*)",
        "destination": "/dynalite-repair-sydney",
        "permanent": True
    },
    {
        "source": "/lighting-control-repair-(?!sydney)(.*)",
        "destination": "/cbus-repair-sydney",
        "permanent": True
    }
]

# Insert at the top of the redirects array
if 'redirects' not in data:
    data['redirects'] = []

# Prepend the wildcard redirects
data['redirects'] = wildcard_redirects + data['redirects']

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Added wildcard redirects to vercel.json")
