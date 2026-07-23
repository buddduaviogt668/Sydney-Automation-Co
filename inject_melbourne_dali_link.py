"""
inject_melbourne_dali_link.py
Adds Melbourne DALI page to:
1. sitemap.xml
2. High-authority DALI pages (dali-lighting-repair, dali2-compliance-nsw-commercial,
   dali-2-lighting-control-implementation-compliance, automation-sydney, brisbane page)
"""
import re

MELBOURNE_SITEMAP_ENTRY = """  <url>
      <loc>https://sydneyautomationco.com.au/melbourne-dali-lighting-control-compliance</loc>
      <lastmod>2026-06-21</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>"""

# ── 1. SITEMAP ────────────────────────────────────────────────────────────────
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

if 'melbourne-dali' not in sitemap:
    # Insert after the Melbourne-closest alphabetical neighbour (after 'matraville' block)
    # Safe anchor: insert before the first <url> that starts with 'mcmahons'
    sitemap = sitemap.replace(
        '  <url>\n      <loc>https://sydneyautomationco.com.au/mcmahons',
        f'{MELBOURNE_SITEMAP_ENTRY}\n  <url>\n      <loc>https://sydneyautomationco.com.au/mcmahons',
        1
    )
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✅ sitemap.xml updated")
else:
    print("ℹ️  sitemap.xml already contains melbourne-dali entry")

# ── 2. TARGETED IN-BODY LINKS on high-authority DALI pages ───────────────────
# We inject a contextual paragraph/link into the body of relevant pages,
# NOT the nav (nav is shared and lives in hundreds of files).
PAGES = {
    'dali-lighting-repair.html': {
        'anchor': 'class="footer-copy"',
        'inject_before': True,
        'html': '''<section style="background:#001428;padding:32px 24px;border-top:1px solid #2a4a80">
<div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
<div>
<p style="color:#f0c040;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Barlow Condensed',sans-serif;">INTERSTATE SERVICE</p>
<p style="color:#a8c0e0;font-size:14px;line-height:1.6">Need DALI commissioning or compliance remediation outside Sydney?<br>George services Melbourne, Brisbane, and Gold Coast remotely via IP.</p>
</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">
<a href="/melbourne-dali-lighting-control-compliance" style="background:#132647;color:#f07020;padding:10px 18px;border-radius:8px;font-weight:700;font-size:14px;text-decoration:none;border:1px solid rgba(240,112,32,0.4)">💡 Melbourne DALI Compliance</a>
<a href="/brisbane-cbus-dynalite-programmer" style="background:#132647;color:#a8c0e0;padding:10px 18px;border-radius:8px;font-weight:600;font-size:14px;text-decoration:none;border:1px solid #2a4a80">🗺️ Brisbane Service</a>
</div>
</div>
</section>
'''
    },
    'dali2-compliance-nsw-commercial.html': {
        'anchor': 'class="footer-copy"',
        'inject_before': True,
        'html': '''<section style="background:#001428;padding:32px 24px;border-top:1px solid #2a4a80">
<div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
<div>
<p style="color:#f0c040;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;font-family:'Barlow Condensed',sans-serif;">DALI COMPLIANCE — MELBOURNE</p>
<p style="color:#a8c0e0;font-size:14px;line-height:1.6">Melbourne building? George also handles DALI-2 compliance and remote commissioning for VIC commercial buildings.</p>
</div>
<a href="/melbourne-dali-lighting-control-compliance" style="background:#132647;color:#f07020;padding:10px 18px;border-radius:8px;font-weight:700;font-size:14px;text-decoration:none;border:1px solid rgba(240,112,32,0.4);white-space:nowrap">💡 Melbourne DALI Compliance →</a>
</div>
</section>
'''
    },
    'brisbane-cbus-dynalite-programmer.html': {
        'anchor': '</section>\n\n  <!-- MAIN CONTENT -->',
        'inject_before': False,
        'html': '''
  <!-- INTERSTATE PEERS -->
  <section style="background:#0d1a30;padding:24px;border-top:1px solid #2a4a80;border-bottom:1px solid #2a4a80">
    <div style="max-width:960px;margin:0 auto;display:flex;flex-wrap:wrap;gap:12px;align-items:center">
      <span style="color:#a8c0e0;font-size:13px;font-weight:600;margin-right:8px">Also available remotely:</span>
      <a href="/gold-coast-cbus-dynalite-programmer" style="background:#132647;color:#a8c0e0;padding:8px 14px;border-radius:6px;font-size:13px;font-weight:600;text-decoration:none;border:1px solid #2a4a80">Gold Coast</a>
      <a href="/melbourne-dali-lighting-control-compliance" style="background:#132647;color:#f07020;padding:8px 14px;border-radius:6px;font-size:13px;font-weight:700;text-decoration:none;border:1px solid rgba(240,112,32,0.35)">Melbourne (DALI)</a>
    </div>
  </section>
'''
    },
    'automation-sydney.html': {
        'anchor': '</footer>',
        'inject_before': True,
        'html': '''  <!-- INTERSTATE DALI LINK -->
  <section style="background:#001428;padding:28px 24px;border-top:1px solid #2a4a80">
    <div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
      <p style="color:#a8c0e0;font-size:14px;line-height:1.6">Need lighting control outside Sydney? Remote DALI commissioning and C-Bus/Dynalite programming is also available for Melbourne, Brisbane, and Gold Coast.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a href="/melbourne-dali-lighting-control-compliance" style="background:#132647;color:#f07020;padding:9px 16px;border-radius:7px;font-weight:700;font-size:13px;text-decoration:none;border:1px solid rgba(240,112,32,0.4)">Melbourne DALI</a>
        <a href="/brisbane-cbus-dynalite-programmer" style="background:#132647;color:#a8c0e0;padding:9px 16px;border-radius:7px;font-weight:600;font-size:13px;text-decoration:none;border:1px solid #2a4a80">Brisbane</a>
        <a href="/gold-coast-cbus-dynalite-programmer" style="background:#132647;color:#a8c0e0;padding:9px 16px;border-radius:7px;font-weight:600;font-size:13px;text-decoration:none;border:1px solid #2a4a80">Gold Coast</a>
      </div>
    </div>
  </section>
'''
    }
}

for filename, config in PAGES.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'melbourne-dali' in content:
            print(f"ℹ️  {filename} — already has melbourne-dali link, skipping")
            continue

        anchor = config['anchor']
        inject_html = config['html']

        if anchor not in content:
            print(f"⚠️  {filename} — anchor not found: '{anchor[:60]}...'")
            continue

        if config['inject_before']:
            content = content.replace(anchor, inject_html + anchor, 1)
        else:
            content = content.replace(anchor, anchor + inject_html, 1)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅  {filename} — Melbourne DALI link injected")

    except FileNotFoundError:
        print(f"⚠️  {filename} — file not found")

print("\nDone.")
