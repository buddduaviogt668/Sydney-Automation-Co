#!/usr/bin/env python3
with open("projects.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()
idx = html.find('Morning Setup')
# Find the uluru array end
start = html.find('uluru:')
print("uluru array:")
# Find the end of the uluru array (the ] that closes it)
end_idx = html.find("}]};\nvar currentGallery", start)
print(repr(html[end_idx-80:end_idx+50]))
