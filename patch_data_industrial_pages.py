"""
patch_data_industrial_pages.py
Updates all data-centres and industrial pages to:
1. Make crystal clear = LIGHTING CONTROL only (not IT/server/factory automation)
2. Hammer C-Bus, Dynalite, DALI-2, Rapix brand names throughout
"""

import os
import glob

BASE_DIR = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'

# Find all data-centre and industrial pages
target_files = (
    glob.glob(os.path.join(BASE_DIR, 'data-centres-and-it-facilities-*.html')) +
    glob.glob(os.path.join(BASE_DIR, 'industrial-and-warehouse-facilities-*.html'))
)

print(f"Found {len(target_files)} data-centre/industrial pages to patch")

DATA_CENTRE_CLARITY_BLOCK = """
        <div style="background:rgba(240,112,32,0.08);border:2px solid #f07020;border-radius:10px;padding:24px;margin:28px 0;">
          <h3 style="color:#f07020;margin-top:0;font-size:1.2em;">Important: We Service Lighting Control Systems Only</h3>
          <p style="color:#fff;margin-bottom:10px;">Sydney Automation Co. specialises exclusively in <strong>commercial lighting control systems</strong> — C-Bus, Dynalite, DALI-2, and Rapix. We do <em>not</em> service IT infrastructure, servers, networking, or data centre cooling systems.</p>
          <p style="color:#a8c0e0;margin:0;">If your data centre or IT facility has a <strong>C-Bus, Dynalite, DALI-2, or Rapix lighting control system</strong> that needs repair, programming, or AFSS emergency lighting compliance — that's exactly what we do. Every day.</p>
        </div>
"""

INDUSTRIAL_CLARITY_BLOCK = """
        <div style="background:rgba(240,112,32,0.08);border:2px solid #f07020;border-radius:10px;padding:24px;margin:28px 0;">
          <h3 style="color:#f07020;margin-top:0;font-size:1.2em;">Important: We Service Lighting Control Systems Only</h3>
          <p style="color:#fff;margin-bottom:10px;">Sydney Automation Co. specialises exclusively in <strong>industrial lighting control systems</strong> — C-Bus, Dynalite, DALI-2, Rapix, and motion-sensor-driven high-bay lighting. We do <em>not</em> service machinery, PLCs, factory process automation, or industrial control systems.</p>
          <p style="color:#a8c0e0;margin:0;">If your warehouse, factory, or industrial facility has a <strong>C-Bus, Dynalite, DALI-2, or Rapix lighting system</strong> that needs repair, sensor integration, energy optimisation, or AS 2293 emergency lighting compliance — we are Sydney's specialists.</p>
        </div>
"""

# Brand injection: make sure these terms appear prominently
BRAND_INJECTION = """
        <div style="background:rgba(0,31,61,0.8);border:1px solid rgba(77,166,255,0.2);border-radius:8px;padding:20px;margin:24px 0;">
          <h4 style="color:#4da6ff;margin-top:0;">Lighting Control Systems We Specialise In</h4>
          <div style="display:flex;flex-wrap:wrap;gap:12px;">
            <span style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:14px;">C-Bus</span>
            <span style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:14px;">Dynalite</span>
            <span style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:14px;">DALI-2</span>
            <span style="background:#001f3d;color:#f07020;padding:6px 14px;border-radius:20px;font-weight:700;font-size:14px;">Rapix</span>
            <span style="background:#001f3d;color:#4da6ff;padding:6px 14px;border-radius:20px;font-size:14px;">Emergency Lighting</span>
            <span style="background:#001f3d;color:#4da6ff;padding:6px 14px;border-radius:20px;font-size:14px;">AFSS Compliance</span>
            <span style="background:#001f3d;color:#4da6ff;padding:6px 14px;border-radius:20px;font-size:14px;">AS 2293</span>
            <span style="background:#001f3d;color:#4da6ff;padding:6px 14px;border-radius:20px;font-size:14px;">Lighting Scene Programming</span>
          </div>
        </div>
"""

patched = 0
for filepath in target_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already patched
    if 'Lighting Control Systems Only' in content:
        continue

    is_datacentre = 'data-centres' in filepath

    # Inject clarity block right after the first </section> in main
    clarity = DATA_CENTRE_CLARITY_BLOCK if is_datacentre else INDUSTRIAL_CLARITY_BLOCK

    # Insert after the hero section closes
    insert_marker = '<div class="container">\n      <div class="alert">'
    if insert_marker in content:
        content = content.replace(
            insert_marker,
            '<div class="container">\n' + clarity + BRAND_INJECTION + '\n      <div class="alert">',
            1
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        patched += 1

print(f"Patched {patched} pages with clarity + brand blocks")
print(f"Skipped (already done): {len(target_files) - patched}")
