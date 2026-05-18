import re
import os

files_to_update = {
    "cbus-repair-mosman.html": {
        "landmarks": "<p>We service premium smart homes across Mosman, providing responsive support from Military Road down to Balmoral Esplanade and Awaba Street.</p>",
        "links": '<li><a href="/cbus-repair-cremorne" style="color:#f07020;text-decoration:underline;">C-Bus Repair Cremorne</a></li><li><a href="/smart-home-automation-neutral-bay" style="color:#f07020;text-decoration:underline;">Automation Neutral Bay</a></li>'
    },
    "cbus-repair-cremorne.html": {
        "landmarks": "<p>From waterfront strata complexes to heritage homes, we provide dedicated C-Bus and Dynalite repair across Cremorne and Cremorne Point.</p>",
        "links": '<li><a href="/cbus-repair-mosman" style="color:#f07020;text-decoration:underline;">C-Bus Repair Mosman</a></li><li><a href="/smart-home-automation-neutral-bay" style="color:#f07020;text-decoration:underline;">Automation Neutral Bay</a></li>'
    },
    "cbus-repair-killara.html": {
        "landmarks": "<p>Specializing in prestige residential properties along the Upper North Shore, we offer complete C-Bus programming and fault finding for Killara's heritage and modern estates.</p>",
        "links": '<li><a href="/smart-home-automation-turramurra" style="color:#f07020;text-decoration:underline;">Automation Turramurra</a></li><li><a href="/smart-home-automation-st-ives" style="color:#f07020;text-decoration:underline;">Automation St Ives</a></li>'
    },
    "dynalite-repair-turramurra.html": {
        "landmarks": "<p>Serving Turramurra and the surrounding North Shore suburbs, we diagnose and upgrade complex Dynalite systems in premium large-scale residential properties.</p>",
        "links": '<li><a href="/cbus-repair-killara" style="color:#f07020;text-decoration:underline;">C-Bus Repair Killara</a></li><li><a href="/smart-home-automation-st-ives" style="color:#f07020;text-decoration:underline;">Automation St Ives</a></li>'
    }
}

for filename, data in files_to_update.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename}, does not exist.")
        continue
        
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filename, "r", encoding="cp1252") as f:
            content = f.read()

    match = re.search(r'(<h2.*?>.*?</h2>)', content)
    if match and "<!-- LOCAL CONTEXT INJECTED -->" not in content:
        injection = f"""
      <h3>Local Geography & Facilities</h3>
      {data['landmarks']}
      
      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        {data['links']}
      </ul>
      <!-- LOCAL CONTEXT INJECTED -->
      
"""
        content = content[:match.start()] + injection + content[match.start():]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
