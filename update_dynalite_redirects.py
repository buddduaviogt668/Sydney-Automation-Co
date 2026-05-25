import os
import json

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"
vercel_path = os.path.join(DIR, "vercel.json")

try:
    with open(vercel_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    redirects = data.get("redirects", [])
    
    new_redirects = [
        {"source": "/dynalite-not-working-sydney", "destination": "/dynalite-repair-sydney.html", "permanent": True},
        {"source": "/dynalite-fault-finding-sydney-common-faults", "destination": "/dynalite-repair-sydney.html", "permanent": True}
    ]
    
    for r in new_redirects:
        # Check if already exists
        if not any(existing.get('source') == r['source'] for existing in redirects):
            redirects.append(r)
            
    data["redirects"] = redirects
    
    with open(vercel_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print("Updated vercel.json successfully.")
except Exception as e:
    print(f"Error updating vercel.json: {e}")
