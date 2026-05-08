worktree = r"C:\Users\gaska\OneDrive - Sydney Automation Co\VS Code -SAC Clone\Sydney-Automation-Co.worktrees\copilot-worktree-2026-04-22T07-13-49"

with open(worktree + r"\index.html", 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find all occurrences of TESTIMONIALS to get the array definition
idx = content.find('var TESTIMONIALS')
if idx < 0:
    idx = content.find('TESTIMONIALS = [')
if idx < 0:
    idx = content.find('TESTIMONIALS=[')
if idx > 0:
    with open('testimonials_extract.txt', 'w', encoding='utf-8') as f:
        f.write(content[idx:idx+8000])
    print(f"Found at {idx}, saved 8000 chars")
else:
    # Search for individual review text patterns
    for keyword in ['"text":', 'name:', 'role:']:
        i = content.find(keyword, 500000)  # skip the bundle header
        if i > 0:
            print(f"Found '{keyword}' at {i}")
            with open('testimonials_extract.txt', 'w', encoding='utf-8') as f:
                f.write(content[i-200:i+6000])
            break
    print("Saved fallback extract")