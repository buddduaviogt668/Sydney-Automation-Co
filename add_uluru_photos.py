#!/usr/bin/env python3
import re

with open("projects.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

# 6 new photo entries to add to gallery grid + lightbox
new_photos = [
    ("uluru-07.jpg", "Uluru Meeting Place \u2014 Site Photo"),
    ("uluru-08.jpg", "Uluru Meeting Place \u2014 Site Photo"),
    ("uluru-09.jpg", "Uluru Meeting Place \u2014 Evening Site Photo"),
    ("uluru-10.jpg", "Uluru Meeting Place \u2014 Evening Site Photo"),
    ("uluru-11.jpg", "Uluru Meeting Place \u2014 Morning Site Photo"),
    ("uluru-12-graduation.jpg", "Uluru Meeting Place \u2014 Graduation Event"),
]

# --- Update gallery grid ---
# Find the last uluru gallery div (closing </div></div> of the gallery-grid)
gallery_end_marker = """\t<img alt="Uluru Meeting Place \u2014 Morning Setup" loading="lazy" src="/uluru-06-morning-setup.jpg" style="width:100%;height:200px;object-fit:cover;display:block"/>
\t</div>
\t</div>
\t</div>"""

# Build new gallery entries
new_grid_entries = ""
for i, (filename, title) in enumerate(new_photos):
    idx = i + 6  # Start at index 6
    new_grid_entries += f"""\t<div onclick="openLightbox('uluru', {idx})" onmouseout="this.style.transform='none';this.style.borderColor='#2a4a80'" onmouseover="this.style.transform='translateY(-3px)';this.style.borderColor='rgba(240,112,32,0.5)'" style="background:#132647;border:1px solid #2a4a80;border-radius:14px;overflow:hidden;cursor:pointer;transition:transform 0.2s,border-color 0.2s">
\t<img alt="{title}" loading="lazy" src="/{filename}" style="width:100%;height:200px;object-fit:cover;display:block"/>
\t</div>
"""

# Insert after the last existing gallery entry
old_grid = """\t<img alt="Uluru Meeting Place \u2014 Morning Setup" loading="lazy" src="/uluru-06-morning-setup.jpg" style="width:100%;height:200px;object-fit:cover;display:block"/>
\t</div>
\t</div>
\t</div>"""

new_grid = """\t<img alt="Uluru Meeting Place \u2014 Morning Setup" loading="lazy" src="/uluru-06-morning-setup.jpg" style="width:100%;height:200px;object-fit:cover;display:block"/>
\t</div>
""" + new_grid_entries + """\t</div>
\t</div>"""

html = html.replace(old_grid, new_grid)

# --- Update lightbox JS ---
# Build new lightbox entries
new_lb_entries = ""
for filename, title in new_photos:
    new_lb_entries += f', {{"src": "/{filename}", "title": "{title}"}}'

# Find uluru array in lightbox JS and insert new entries before closing ]
uluru_arr_start = html.find('uluru:[')
if uluru_arr_start > 0:
    # Find the closing ] of the uluru array
    # The uluru array ends with "}]};\nvar currentGallery"
    # Find the last occurrence of "}]" within a reasonable range
    search_start = uluru_arr_start + 7  # skip 'uluru:['
    close_bracket = html.find(']', search_start + 300)  # past the last entry
    if close_bracket > 0:
        html = html[:close_bracket] + new_lb_entries + html[close_bracket:]
        print(f"Inserted {len(new_photos)} lightbox entries at position {close_bracket}")
    else:
        print("ERROR: Could not find closing bracket for uluru array")
else:
    print("ERROR: Could not find uluru array in lightbox")

with open("projects.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done - added 6 new photos to gallery grid and lightbox")
