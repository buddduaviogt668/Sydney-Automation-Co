#!/usr/bin/env python3
"""
Run from inside your Sydney-Automation-Co repo folder:
  python apply_seo_fixes.py

What it does:
  1. Adds FAQPage schema to c-bus-repairs-sydney.html
  2. Fixes schema URL (.html → clean URL)
  3. Upgrades anchor text → "C-Bus Repairs Sydney" on 9 high-authority pages
  4. Upgrades anchor text → "C-Bus Repairs Sydney" on 36 suburb repair pages
"""

import os
import re
import glob

# ── 1. Fix c-bus-repairs-sydney.html ─────────────────────────────────────────

FAQ_SCHEMA = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How quickly can you attend a C-Bus repair in Sydney?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Same-day callouts are available across the Sutherland Shire and most of Greater Sydney. For urgent faults — commercial buildings, strata complexes or safety lighting issues — call directly on 0422 469 739 and we'll prioritise your job."
      }
    },
    {
      "@type": "Question",
      "name": "Do you carry replacement C-Bus hardware on the van?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We carry the most commonly replaced C-Bus units — relay modules, dimmer modules and power supplies. For less common units we can usually source and return within 1–2 business days."
      }
    },
    {
      "@type": "Question",
      "name": "My electrician looked at the C-Bus system and couldn't fix it. Can you?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost certainly. The majority of C-Bus faults require C-Bus Toolkit software and accreditation to diagnose properly. A general electrician can check physical wiring and replace modules, but they can't see the network, resolve address conflicts or recover corrupted programming. That's what we do."
      }
    },
    {
      "@type": "Question",
      "name": "What if the original C-Bus project file has been lost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We can scan the live network using C-Bus Toolkit to extract the current programming from units on the bus. This lets us rebuild the project file and restore functionality even without the original installer's files."
      }
    },
    {
      "@type": "Question",
      "name": "Do you repair C-Bus systems in commercial and strata buildings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — commercial, strata and residential. We work with facility managers, strata managers, body corporates and building owners across Sydney. We can provide service reports and documentation on request."
      }
    }
  ]
}
</script>"""

repairs_file = "c-bus-repairs-sydney.html"
if os.path.exists(repairs_file):
    with open(repairs_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix schema URL
    content = content.replace(
        '"url": "https://sydneyautomationco.com.au/c-bus-repairs-sydney.html"',
        '"url": "https://sydneyautomationco.com.au/c-bus-repairs-sydney"'
    )

    # Inject FAQPage schema before robots meta (only if not already present)
    if "FAQPage" not in content:
        content = content.replace(
            '<meta content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1" name="robots"/>',
            FAQ_SCHEMA + '\n<meta content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1" name="robots"/>'
        )
        print(f"✅ FAQPage schema injected into {repairs_file}")
    else:
        print(f"⏭  FAQPage schema already present in {repairs_file}")

    with open(repairs_file, "w", encoding="utf-8") as f:
        f.write(content)
else:
    print(f"❌ {repairs_file} not found — are you in the right directory?")
    exit(1)

# ── 2. Upgrade anchor text on high-authority pages ───────────────────────────

authority_pages = [
    "cbus-not-working-sydney.html",
    "cbus-fault-finding-sydney.html",
    "emergency-repair-sydney.html",
    "lighting-control-repair-sydney.html",
    "cbus-specialist-sydney.html",
    "c-bus-programmer-sydney.html",
    "cbus-maintenance-sydney.html",
    "index.html",
    "services.html",
]

# ── 3. Upgrade anchor text on all suburb repair pages ────────────────────────

suburb_pages = glob.glob("cbus-repair-*.html")

all_pages = authority_pages + suburb_pages
upgraded = 0

for fname in all_pages:
    if not os.path.exists(fname):
        continue
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r'(<a[^>]*href="/c-bus-repairs-sydney"[^>]*>)C-Bus Repairs(</a>)',
        r'\1C-Bus Repairs Sydney\2',
        content
    )

    if new_content != content:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(new_content)
        upgraded += 1

print(f"✅ Anchor text upgraded to 'C-Bus Repairs Sydney' in {upgraded} pages")

# ── Done ─────────────────────────────────────────────────────────────────────

print("\nAll done. Now run:")
print("  git add -A")
print('  git commit -m "SEO: FAQPage schema + C-Bus Repairs Sydney anchor text site-wide"')
print("  git push origin main")
