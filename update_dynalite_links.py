import os
import glob

DIR = r"c:\Users\gaska\OneDrive\Documents\Sydney-Automation-Co"

html_files = glob.glob(os.path.join(DIR, "*.html"))

targets = {
    "dynalite-not-working-sydney": "dynalite-repair-sydney",
    "dynalite-fault-finding-sydney-common-faults": "dynalite-repair-sydney"
}

files_updated = 0

for filepath in html_files:
    if "old_index.html" in filepath:
        continue
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

print(f"Finished. Updated dynalite internal links across {files_updated} files.")

# Remove the file itself
fault_file = os.path.join(DIR, "dynalite-fault-finding-sydney-common-faults.html")
if os.path.exists(fault_file):
    os.remove(fault_file)
    print(f"Deleted {fault_file}")
