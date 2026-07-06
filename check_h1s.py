#!/usr/bin/env python3
import subprocess, re

result = subprocess.run(["git", "ls-files", "--cached", "*.html"], capture_output=True, text=True, check=True)
tracked = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

h1s = {}
for fp in tracked:
    with open(fp, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
    if h1_m:
        h1_text = h1_m.group(1).strip()
        h1s.setdefault(h1_text, []).append(fp)

print("Duplicate H1s:")
found = False
for h1, files in h1s.items():
    if len(files) > 1:
        found = True
        print(f'  "{h1}" appears in {len(files)} files:')
        for f in files:
            print(f"    - {f}")
if not found:
    print("  None found")
