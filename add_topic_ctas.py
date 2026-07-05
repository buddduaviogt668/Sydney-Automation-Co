"""
add_topic_ctas.py — Adds topic-matched end-of-post CTAs to all blog posts.
Inserts a direct service CTA between the lead magnet and related reading sections.
"""
import os, glob, re

TOPIC_CTAS = {
    "cbus": {
        "heading": "Need C-Bus Repairs?",
        "body": "Our accredited C-Bus programmers diagnose and repair all C-Bus hardware — 5500PC, 5508RVF, 5100PS, Saturn, Neo, and legacy models. Same-day service across Sydney.",
        "cta": "Call 0422 469 739"
    },
    "dynalite": {
        "heading": "Dynalite System Fault?",
        "body": "We are certified Dynalite system builders and repair all Dynalite hardware — DDNG232, DDBC1200, DDMC802, DUS360CS, and touch screens. Fast turnaround Sydney-wide.",
        "cta": "Call 0422 469 739"
    },
    "dali": {
        "heading": "Need DALI-2 Compliance?",
        "body": "Our technicians are accredited in DALI-2 commissioning, emergency lighting testing, and AFSS documentation. We ensure your building meets NCC 2022 requirements.",
        "cta": "Call 0422 469 739"
    },
    "emergency": {
        "heading": "Emergency Lighting Issue?",
        "body": "We provide priority same-day response for emergency lighting faults across Sydney. Fully accredited AFSS inspectors. Don't risk non-compliance — call now.",
        "cta": "Call 0422 469 739"
    },
    "afss": {
        "heading": "AFSS Compliance Due?",
        "body": "We handle full AFSS emergency lighting inspections, log book management, and defect rectification. Accredited and experienced with Sydney buildings of all types.",
        "cta": "Call 0422 469 739"
    },
    "smart": {
        "heading": "Upgrade to Smart Control?",
        "body": "Integrate your C-Bus or Dynalite system with Apple HomeKit, Google Home, or Amazon Alexa. Voice control, remote access, and automation from your phone.",
        "cta": "Call 0422 469 739"
    },
    "strata": {
        "heading": "Strata Lighting Compliance?",
        "body": "We specialise in strata common area lighting, AFSS compliance, car park sensor upgrades, and energy-saving LED retrofits. Fixed-price quotes for Sydney strata.",
        "cta": "Call 0422 469 739"
    },
    "commercial": {
        "heading": "Commercial Lighting Support?",
        "body": "We provide end-to-end commercial lighting services — DALI-2 commissioning, BMS integration, emergency compliance, and ongoing maintenance contracts for Sydney businesses.",
        "cta": "Call 0422 469 739"
    },
    "residential": {
        "heading": "Smart Home Lighting?",
        "body": "Transform your home with C-Bus or Dynalite automation. Scene control, scheduling, and remote access — designed and programmed by accredited specialists.",
        "cta": "Call 0422 469 739"
    },
    "suburb": {
        "heading": "Local Sydney Repairs?",
        "body": "We cover all Sydney suburbs from Menai. Same-day response for urgent C-Bus and Dynalite faults. Accredited, insured, and local.",
        "cta": "Call 0422 469 739"
    },
}

def get_topic_cta(filename):
    f = filename.lower()
    # Emergency first (some files have "emergency" AND "cbus")
    if "emergency" in f or "ess" in f:
        return TOPIC_CTAS["emergency"]
    if "afss" in f:
        return TOPIC_CTAS["afss"]
    if "dali" in f:
        return TOPIC_CTAS["dali"]
    if "dynalite" in f:
        return TOPIC_CTAS["dynalite"]
    if "cbus" in f or "clipsal" in f:
        return TOPIC_CTAS["cbus"]
    if "smart" in f or "homekit" in f or "alexa" in f or "google" in f or "voice" in f or "ifttt" in f:
        return TOPIC_CTAS["smart"]
    if "strata" in f:
        return TOPIC_CTAS["strata"]
    if "commercial" in f or "office" in f or "retail" in f or "hotel" in f or "hospital" in f or "industrial" in f:
        return TOPIC_CTAS["commercial"]
    if any(x in f for x in ["-home-", "residential", "apartment", "house", "villa", "townhouse", "terrace"]):
        return TOPIC_CTAS["residential"]
    if any(x in f for x in ["sydney-", "suburb", "eastern", "northern", "sutherland", "hills-", "parramatta",
                              "macquarie", "chatswood", "bondi", "mosman", "rose-bay", "vaucluse",
                              "paddington", "surry", "newtown", "darling", "alexandria", "mascot",
                              "kingsford", "maroubra", "coogee", "randwick", "strathfield", "burwood",
                              "rhodes", "epping", "ryde", "gordon", "pymble", "wahroonga", "penrith",
                              "camden", "liverpool", "campbelltown", "castle-hill", "hornsby"]):
        return TOPIC_CTAS["suburb"]
    return TOPIC_CTAS["commercial"]

CTA_HTML = '''<div class="topic-cta" style="margin:32px 0;padding:28px;background:rgba(240,112,32,0.06);border:1px solid rgba(240,112,32,0.2);border-radius:12px;text-align:center;">
  <h3 style="color:#fff;margin:0 0 8px;font-family:\'Barlow Condensed\',sans-serif;font-size:20px;">{heading}</h3>
  <p style="color:#a8c0e0;font-size:14px;margin:0 0 16px;">{body}</p>
  <a href="tel:+61422469739" style="display:inline-block;padding:14px 32px;background:#f07020;color:#fff;border-radius:50px;text-decoration:none;font-weight:800;font-size:15px;">{cta}</a>
</div>'''

def add_cta(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        filename = os.path.basename(filepath)
        topic_cta = get_topic_cta(filename)
        new_block = CTA_HTML.format(**topic_cta)
        
        # Check if already has topic-cta
        if 'class="topic-cta"' in content:
            return False  # already has one
        
        # Insert before "Related Reading" or "sac-related-reading" or the footer
        # Try to find the lead magnet CTA section first (to insert after it)
        insert_before = content.find('class="sac-related-reading"')
        if insert_before == -1:
            insert_before = content.find('sac-related-reading')
        if insert_before == -1:
            insert_before = content.find('Related Reading')
        if insert_before == -1:
            insert_before = content.find('<footer')
        if insert_before == -1:
            return False  # can't find insertion point
        
        new_content = content[:insert_before] + new_block + "\n\n" + content[insert_before:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"  Error {filepath}: {e}")
        return False

def main():
    blog_files = glob.glob("blog*.html") + glob.glob("blog/*.html")
    blog_files = sorted(set(f for f in blog_files if f != "blog.html" and os.path.isfile(f)))
    
    updated = 0
    skipped = 0
    for f in blog_files:
        if add_cta(f):
            updated += 1
        else:
            skipped += 1
    
    print(f"Topic CTAs: {updated} added, {skipped} skipped (already has or no insertion point)")

if __name__ == "__main__":
    main()
