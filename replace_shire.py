import re

with open("shire.html", "r", encoding="cp1252") as f:
    content = f.read()

target = '<div class="suburb-card"><h4>Kurnell &amp; Bundeena</h4><p>Remote Shire locations serviced. Call to confirm availability.</p></div>'
replacement = '<div class="suburb-card"><h4><a href="/cbus-dynalite-planning-checklist-new-builds-menai" style="color: #f0f4ff; text-decoration: underline;">Menai</a></h4><p>C-Bus & Dynalite planning and installation for new builds in Menai.</p></div>\n<div class="suburb-card"><h4>Kurnell &amp; Bundeena</h4><p>Remote Shire locations serviced. Call to confirm availability.</p></div>'

new_content = content.replace(target, replacement)

# We can safely write it back as utf-8 if the site uses utf-8
with open("shire.html", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Replaced successfully and converted to utf-8")
