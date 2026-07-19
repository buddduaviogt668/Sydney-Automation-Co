import os
import json

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"
VERCEL_JSON = os.path.join(DIR, "vercel.json")

# 1. Update vercel.json
with open(VERCEL_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# The new champion is /cbus-repair-sydney
champion = "/cbus-repair-sydney"

redirects_to_add = [
    {"source": "/cbus-not-working-sydney", "destination": champion, "permanent": True},
    {"source": "/cbus-not-working-sydney.html", "destination": champion, "permanent": True},
    {"source": "/cbus-fault-finding-sydney", "destination": champion, "permanent": True},
    {"source": "/cbus-fault-finding-sydney.html", "destination": champion, "permanent": True},
    {"source": "/c-bus-repairs-sydney", "destination": champion, "permanent": True},
    {"source": "/c-bus-repairs-sydney.html", "destination": champion, "permanent": True}
]

# Add new redirects
if "redirects" not in data:
    data["redirects"] = []

data["redirects"].extend(redirects_to_add)

# Update existing /cbus-repairs-sydney redirects to point to champion
for r in data["redirects"]:
    if r.get("destination") == "/c-bus-repairs-sydney" or r.get("source") == "/cbus-repairs-sydney":
        r["destination"] = champion

with open(VERCEL_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated vercel.json with new 301 redirects.")

# 2. Delete the cannibalizing files
files_to_delete = [
    "cbus-not-working-sydney.html",
    "cbus-fault-finding-sydney.html",
    "c-bus-repairs-sydney.html"
]

for file in files_to_delete:
    filepath = os.path.join(DIR, file)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted {file}")
    else:
        print(f"{file} already gone.")
