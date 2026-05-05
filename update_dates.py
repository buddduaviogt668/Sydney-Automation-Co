import os
import re

def update_dates(content):
    # Update years 2024, 2025 to 2026
    content = content.replace("2024", "2026")
    content = content.replace("2025", "2026")
    
    # Update specific month/year mentions to May 2026
    # Examples: "Mar 12, 2025", "January 2025", etc.
    content = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, 202\d', 'May 05, 2026', content, flags=re.IGNORECASE)
    content = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* 202\d', 'May 2026', content, flags=re.IGNORECASE)
    
    return content

def main():
    updated_count = 0
    for root, _, files in os.walk("."):
        if any(x in root for x in [".git", "node_modules", "markdown_mirror"]):
            continue
        for file in files:
            if file.endswith(".html"):
                fpath = os.path.join(root, file)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        original_content = f.read()
                    
                    new_content = update_dates(original_content)
                    
                    if new_content != original_content:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_count += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\nTotal files updated with new dates: {updated_count}")

if __name__ == "__main__":
    main()
