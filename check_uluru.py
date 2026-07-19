#!/usr/bin/env python3
import re
with open("projects.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

count = html.count("Uluru Meeting Place")
print(f"Uluru Meeting Place references: {count}")

m = re.search(r"uluru:\[.*?\]", html)
if m:
    img_count = len(re.findall(r'"src"', m.group()))
    print(f"Uluru gallery images in lightbox: {img_count}")

gallery_imgs = re.findall(r"uluru-\d+", html)
print(f"Uluru gallery image tags: {len(gallery_imgs)}")

print("OK" if img_count == len(gallery_imgs) else "MISMATCH")
