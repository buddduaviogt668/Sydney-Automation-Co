import os
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

def update_title(filename, new_title):
    filepath = os.path.join(DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the exact <title> block
    new_content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.IGNORECASE | re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated title in {filename}")
    else:
        print(f"No changes made to {filename}")

# Target 1: Homepage
update_title('index.html', 'Top Automation Companies Sydney | C-Bus &amp; Dynalite Experts')

# Target 2: Residential Dynalite Servicing
update_title('residential-dynalite-servicing.html', 'Residential Dynalite Servicing Sydney | Repairs &amp; Maintenance')

# Target 3: Car Park Lighting Variants (we'll update the main one to hit the umbrella terms)
update_title('car-park-lighting-repairs-sydney.html', 'Car Park Lighting Installation, Repairs &amp; Solutions Sydney')

# Target 4: DALI
update_title('dali-lighting-control-system-sydney.html', 'DALI Lighting Control System Sydney | Automation &amp; Repairs')

# Target 5: Smart Home Suburb pages
import glob
suburb_files = glob.glob(os.path.join(DIR, "smart-home-automation-*.html"))
for filepath in suburb_files:
    filename = os.path.basename(filepath)
    # Extract suburb name from filename: smart-home-automation-turramurra.html -> Turramurra
    # Exclude the "companies-sydney" one
    if "companies-sydney" in filename:
        continue
        
    suburb_slug = filename.replace('smart-home-automation-', '').replace('.html', '')
    suburb_name = " ".join([word.capitalize() for word in suburb_slug.split('-')])
    
    new_title = f'Smart Home Automation {suburb_name} | Sydney Automation Co'
    update_title(filename, new_title)

print("All targeted titles updated successfully.")
