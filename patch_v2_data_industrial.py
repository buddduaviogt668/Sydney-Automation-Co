"""
patch_v2_data_industrial.py
Targeted patch for data-centre and industrial pages.
Replaces their hero subtitle to make LIGHTING CONTROL unmistakably clear,
and adds the brand pill bar right after the header.
"""
import os, glob, re

BASE_DIR = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'

target_files = (
    glob.glob(os.path.join(BASE_DIR, 'data-centres-and-it-facilities-*.html')) +
    glob.glob(os.path.join(BASE_DIR, 'industrial-and-warehouse-facilities-*.html'))
)

print(f"Targeting {len(target_files)} data-centre/industrial pages")

DATA_DISCLAIMER = (
    '<p style="color:#f0c040;font-size:13px;font-weight:600;margin-top:10px;">'
    '&#9888; We service <u>lighting control systems</u> (C-Bus, Dynalite, DALI-2, Rapix) only — '
    'not IT infrastructure, servers, cooling, or factory machinery.</p>'
)

BRAND_PILLS = '''<div style="background:rgba(0,20,50,0.9);border:1px solid rgba(77,166,255,0.25);border-radius:10px;padding:18px 22px;margin:20px 0 0 0;">
  <p style="color:#4da6ff;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">Lighting Control Systems — Our Only Speciality</p>
  <div style="display:flex;flex-wrap:wrap;gap:9px;">
    <a href="/automation-sydney" style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:13px;text-decoration:none;border:1px solid rgba(240,112,32,0.4);">C-Bus</a>
    <a href="/automation-sydney" style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:13px;text-decoration:none;border:1px solid rgba(240,112,32,0.4);">Dynalite</a>
    <a href="/automation-sydney" style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:13px;text-decoration:none;border:1px solid rgba(240,112,32,0.4);">DALI-2</a>
    <a href="/automation-sydney" style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:13px;text-decoration:none;border:1px solid rgba(240,112,32,0.4);">Rapix</a>
    <span style="background:#001f3d;color:#a8c0e0;padding:6px 14px;border-radius:20px;font-size:12px;border:1px solid rgba(255,255,255,0.1);">Emergency Lighting</span>
    <span style="background:#001f3d;color:#a8c0e0;padding:6px 14px;border-radius:20px;font-size:12px;border:1px solid rgba(255,255,255,0.1);">AFSS AS 2293</span>
    <span style="background:#001f3d;color:#a8c0e0;padding:6px 14px;border-radius:20px;font-size:12px;border:1px solid rgba(255,255,255,0.1);">Lighting Scene Programming</span>
  </div>
  <p style="color:#a8c0e0;font-size:11px;margin-top:10px;margin-bottom:0;">Not general electrical. Not IT. Not HVAC. <strong style="color:#fff;">Lighting control only.</strong></p>
</div>'''

patched = 0
already = 0

for filepath in target_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Lighting Control Systems — Our Only Speciality' in content:
        already += 1
        continue

    # 1. Add disclaimer to the hero subtitle paragraph
    # Pattern: find <p> inside .hero that talks about the facility
    content = re.sub(
        r'(<section class="hero"[^>]*>.*?<div class="container">.*?<p[^>]*>)(.*?)(</p>)',
        lambda m: m.group(1) + m.group(2) + ' <strong style="color:#f0c040;">Lighting control systems only — C-Bus, Dynalite, DALI-2, Rapix.</strong>' + m.group(3),
        content,
        count=1,
        flags=re.DOTALL
    )

    # 2. Insert brand pills block after </section> (after the hero closes) before <div class="container">
    hero_close = '</section>'
    # Find first occurrence after the hero
    idx = content.find(hero_close)
    if idx != -1:
        insert_pos = idx + len(hero_close)
        content = (
            content[:insert_pos]
            + '\n\n<div class="container">\n' + BRAND_PILLS + '\n</div>\n'
            + content[insert_pos:]
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    patched += 1

print(f"Patched: {patched}")
print(f"Already done: {already}")
print(f"Total targeted: {len(target_files)}")
