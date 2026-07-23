import os
import re
import glob

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

def update_meta_description(filename, new_desc):
    filepath = os.path.join(DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the existing meta description tag
    new_meta_tag = f'<meta name="description" content="{new_desc}" />'
    
    # Try to find and replace existing
    new_content, count = re.subn(r'<meta[^>]*name=["\']description["\'][^>]*>', new_meta_tag, content, flags=re.IGNORECASE)
    
    # If not found, inject it right below <title>
    if count == 0:
        new_content, count = re.subn(r'(<title>.*?</title>)', r'\1\n  ' + new_meta_tag, content, flags=re.IGNORECASE | re.DOTALL)
        if count == 0:
            print(f"Could not find title or meta description in {filename}")
            return
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated meta description in {filename}")
    else:
        print(f"No changes made to {filename}")

# Target 1: Homepage
update_meta_description('index.html', 'Expert lighting control and smart home automation companies in Sydney. Specializing in C-Bus, Dynalite, and DALI design, installation, repairs, and maintenance.')

# Target 2: Residential Dynalite Servicing
update_meta_description('residential-dynalite-servicing.html', 'Expert residential Signify Dynalite servicing, repairs, and maintenance across Greater Sydney. Fast response for home lighting control faults. Call today.')

# Target 3: Car Park Lighting Variants
update_meta_description('car-park-lighting-repairs-sydney.html', 'Expert car park lighting repairs and maintenance in Sydney. Fast response for C-Bus relay faults, DALI sensor failures, and strata compliance. Call 0422 469 739.')

# Target 4: DALI
update_meta_description('dali-lighting-control-system-sydney.html', 'Expert DALI lighting control system design, repairs, and maintenance in Sydney. Rapid response for commercial and strata DALI faults. Call today.')

# Target 5: Smart Home Suburb pages
suburb_files = glob.glob(os.path.join(DIR, "smart-home-automation-*.html"))
for filepath in suburb_files:
    filename = os.path.basename(filepath)
    if "companies-sydney" in filename:
        continue
        
    suburb_slug = filename.replace('smart-home-automation-', '').replace('.html', '')
    suburb_name = " ".join([word.capitalize() for word in suburb_slug.split('-')])
    
    new_desc = f'Top-rated smart home automation specialists in {suburb_name}. Expert C-Bus and Dynalite installation, upgrades, and repairs for luxury residential properties.'
    update_meta_description(filename, new_desc)

print("All meta descriptions updated successfully.")
