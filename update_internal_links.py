import os
import glob
import re

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

html_files = glob.glob(os.path.join(DIR, "*.html"))

targets = {
    "cbus-not-working-sydney": "cbus-repair-sydney",
    "cbus-fault-finding-sydney": "cbus-repair-sydney",
    "c-bus-repairs-sydney": "cbus-repair-sydney"
}

files_updated = 0

for filepath in html_files:
    if "old_index.html" in filepath:
        continue # skip the broken file
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        new_content = content
        
        for old_link, new_link in targets.items():
            new_content = new_content.replace(old_link, new_link)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(new_content)
            files_updated += 1
            print(f"Updated internal links in {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Finished. Updated internal links across {files_updated} files.")
