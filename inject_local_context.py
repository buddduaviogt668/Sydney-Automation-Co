import re
import os

files_to_update = {
    "c-bus-programmer-mosman.html": {
        "landmarks": "<p>We service premium smart homes across Mosman, providing responsive support from Military Road down to Balmoral Esplanade and Awaba Street.</p>",
        "links": '<li><a href="/c-bus-programmer-cremorne" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Cremorne</a></li><li><a href="/c-bus-programmer-neutral-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Neutral Bay</a></li>'
    },
    "c-bus-programmer-cremorne.html": {
        "landmarks": "<p>From waterfront strata complexes to heritage homes, we provide dedicated C-Bus and Dynalite repair across Cremorne and Cremorne Point.</p>",
        "links": '<li><a href="/c-bus-programmer-mosman" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Mosman</a></li><li><a href="/c-bus-programmer-neutral-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Neutral Bay</a></li>'
    },
    "c-bus-programmer-killara.html": {
        "landmarks": "<p>Specializing in prestige residential properties along the Upper North Shore, we offer complete C-Bus programming and fault finding for Killara\'s heritage and modern estates.</p>",
        "links": '<li><a href="/c-bus-programmer-turramurra" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Turramurra</a></li><li><a href="/c-bus-programmer-st-ives" style="color:#f07020;text-decoration:underline;">C-Bus Programmer St Ives</a></li>'
    },
    "dynalite-programmer-turramurra.html": {
        "landmarks": "<p>Serving Turramurra and the surrounding North Shore suburbs, we diagnose and upgrade complex Dynalite systems in premium large-scale residential properties.</p>",
        "links": '<li><a href="/c-bus-programmer-killara" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Killara</a></li><li><a href="/dynalite-programmer-st-ives" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer St Ives</a></li>'
    }
}

count = 0
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
        print(f"SUCCESS: Injected local context into {filename}")
        count += 1
    elif "<!-- LOCAL CONTEXT INJECTED -->" in content:
        print(f"Already injected: {filename}")
    else:
        print(f"Could not find injection point in {filename}")

print(f"Total files updated: {count}")
