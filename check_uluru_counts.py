#!/usr/bin/env python3
import re
with open("projects.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

imgs = re.findall(r'<img[^>]*src="/uluru-\d+', html)
lb_entries = re.findall(r'"src": "/uluru-\d+', html)
print(f"Gallery <img> tags: {len(imgs)}")
print(f"Lightbox entries: {len(lb_entries)}")
print("OK" if len(imgs) == len(lb_entries) else "MISMATCH")
