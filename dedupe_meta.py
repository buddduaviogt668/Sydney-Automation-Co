import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files:
    print(f"Deduplicating {file}...")
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    new_lines = []
    seen_description = False
    seen_robots = False
    seen_canonical = False
    
    # Priority for description: keep the one that is "better" or just the first one?
    # Usually the one with longer content or specific keywords.
    # For now, I'll keep the FIRST one found for description and robots.
    
    for line in lines:
        is_desc = 'name="description"' in line.lower() or 'name=\'description\'' in line.lower()
        is_robots = 'name="robots"' in line.lower() or 'name=\'robots\'' in line.lower()
        is_canonical = 'rel="canonical"' in line.lower() or 'rel=\'canonical\'' in line.lower()
        
        if is_desc:
            if not seen_description:
                new_lines.append(line)
                seen_description = True
            else:
                continue # Skip duplicates
        elif is_robots:
            if not seen_robots:
                new_lines.append(line)
                seen_robots = True
            else:
                continue
        elif is_canonical:
            if not seen_canonical:
                new_lines.append(line)
                seen_canonical = True
            else:
                continue
        else:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Deduplication complete.")
