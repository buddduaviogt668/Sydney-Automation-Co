#!/usr/bin/env python3
import re
import subprocess
import re

result = subprocess.run(["git", "ls-files", "--cached", "*.html"], capture_output=True, text=True, check=True)
tracked = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

has_og = 0
no_og = 0
for fp in tracked:
    with open(fp, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    og_tags = ["og:title", "og:description", "og:url", "og:type", "og:site_name"]
    if any(tag in html for tag in og_tags):
        has_og += 1
    else:
        no_og += 1

print(f"Files with OG tags: {has_og}")
print(f"Files without OG tags: {no_og}")
