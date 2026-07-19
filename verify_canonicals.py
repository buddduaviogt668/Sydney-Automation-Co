#!/usr/bin/env python3
import subprocess, re, os

SITE = "https://sydneyautomationco.com.au"
result = subprocess.run(["git", "ls-files", "--cached", "*.html"], capture_output=True, text=True, check=True)
tracked = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

wrong = 0
missing = 0
for fp in tracked:
    with open(fp, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    fname = os.path.basename(fp)
    slug = fname.replace(".html", "")
    expected = f"{SITE}/{slug}.html"
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, re.IGNORECASE)
    if m:
        if m.group(1) != expected:
            wrong += 1
            print(f"WRONG: {fp} -> {m.group(1)} (expected {expected})")
    else:
        missing += 1
        print(f"MISSING: {fp}")

print(f"\nWrong: {wrong}, Missing: {missing}")
