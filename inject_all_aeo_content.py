import os
import re

def get_suburb_and_system(filename):
    # Extract system and suburb from filenames like:
    # cbus-repair-suburb-name.html
    # dynalite-programmer-suburb-name.html
    # c-bus-programmer-suburb-name.html
    
    if filename.startswith('cbus-repair-'):
        system = "C-Bus"
        suburb = filename.replace('cbus-repair-', '').replace('.html', '').replace('-', ' ').title()
    elif filename.startswith('dynalite-programmer-') or filename.startswith('dynalite-repair-'):
        system = "Dynalite"
        suburb = filename.replace('dynalite-programmer-', '').replace('dynalite-repair-', '').replace('.html', '').replace('-', ' ').title()
    elif filename.startswith('c-bus-programmer-'):
        system = "C-Bus"
        suburb = filename.replace('c-bus-programmer-', '').replace('.html', '').replace('-', ' ').title()
    else:
        return None, None
        
    return system, suburb

def make_faq_html(suburb, system):
    s = system
    sl = system.lower()
    return f"""
  <!-- AEO FAQ: conversational Q&As for AI search & rich snippets -->
  <section style="background:rgba(255,255,255,0.02);border-top:1px solid rgba(240,112,32,0.15);padding:60px 24px;max-width:860px;margin:0 auto;">
    <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:800;color:#fff;margin-bottom:8px;">
      Real Questions We Get Asked in {suburb}
    </h2>
    <p style="color:#7a9cc0;font-size:14px;margin-bottom:40px;">Answered honestly — no fluff, no jargon.</p>

    <div itemscope itemtype="https://schema.org/FAQPage">

      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"
           style="border-bottom:1px solid rgba(255,255,255,0.06);padding:24px 0;">
        <h3 itemprop="name" style="font-size:1.05rem;font-weight:700;color:#f0c040;margin-bottom:10px;">
          "My {s} lights aren't responding at all in {suburb} — is it the programming or a hardware fault?"
        </h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text" style="color:#c8d8ec;line-height:1.75;font-size:0.95rem;">
            This is the most common call we get from {suburb}. Nine times out of ten, it's one of three things:
            a corrupted group address in the {s} network, a failed relay module, or a communication dropout on the bus cable.
            When we arrive, the first thing we do is plug in the {s} toolkit and read the
            live network — within 10–15 minutes we can usually tell you exactly which unit is at fault and whether it can
            be fixed on the spot or needs a part ordered. We carry the most common {s} modules in the van, so most {suburb}
            jobs are resolved same-day.
          </p>
        </div>
      </div>

      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"
           style="border-bottom:1px solid rgba(255,255,255,0.06);padding:24px 0;">
        <h3 itemprop="name" style="font-size:1.05rem;font-weight:700;color:#f0c040;margin-bottom:10px;">
          "How long does a {s} repair or reprogramming visit in {suburb} actually take?"
        </h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text" style="color:#c8d8ec;line-height:1.75;font-size:0.95rem;">
            For a straightforward reprogramming job — say, scenes not working properly or a new switch that needs
            to be commissioned — plan for 2–3 hours. Fault-finding jobs, especially in older
            {suburb} buildings where the {sl} cabling hasn't been touched in 10+ years, can run 3–5 hours if there's
            physical bus damage involved. We'll always give you a clear estimate before we start and call you if we find
            something unexpected mid-job. No surprises.
          </p>
        </div>
      </div>

      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"
           style="border-bottom:1px solid rgba(255,255,255,0.06);padding:24px 0;">
        <h3 itemprop="name" style="font-size:1.05rem;font-weight:700;color:#f0c040;margin-bottom:10px;">
          "Can you reprogram my {s} system without replacing any hardware in {suburb}?"
        </h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text" style="color:#c8d8ec;line-height:1.75;font-size:0.95rem;">
            Absolutely — and this is actually the most satisfying part of the job. We've had {suburb} clients who were
            quoted full system replacements by other tradespeople, only to find out the entire issue was a scene that
            had been accidentally overwritten or a unit ID conflict that takes 20 minutes to fix in software.
            George has been programming {s} systems since the Clipsal national support days, so he knows every quirk
            of the platform. If it can be fixed in software, we'll fix it in software — no unnecessary hardware costs.
          </p>
        </div>
      </div>

      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"
           style="padding:24px 0;">
        <h3 itemprop="name" style="font-size:1.05rem;font-weight:700;color:#f0c040;margin-bottom:10px;">
          "Who do I call in {suburb} when my {s} system stops working after hours or on a weekend?"
        </h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text" style="color:#c8d8ec;line-height:1.75;font-size:0.95rem;">
            Call us directly on <a href="tel:0422469739" style="color:#f07020;font-weight:700;">0422 469 739</a>.
            We cover {suburb} and surrounding areas for emergency callouts. We prioritise situations
            where you've lost control of essential lighting — security lights, common area lights in strata buildings,
            or systems that have simply gone dark. We don't outsource to a call centre; you'll speak directly to George,
            who makes the call on whether we can diagnose remotely via the {s} toolkit or need to be on-site same day.
          </p>
        </div>
      </div>

    </div>

    <div style="margin-top:40px;text-align:center;">
      <a href="tel:0422469739"
         style="display:inline-block;background:#f07020;color:#fff;font-weight:800;padding:16px 40px;border-radius:8px;font-size:1rem;text-decoration:none;letter-spacing:0.5px;">
        📞 Call Now — {suburb} {s} Specialist
      </a>
    </div>
  </section>
"""

def make_faq_schema(suburb, system):
    sl = system.lower()
    return f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "My {system} lights aren't responding in {suburb} — is it programming or hardware?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Most {suburb} {sl} call-outs are caused by corrupted group addresses, a failed relay module, or a bus dropout. George connects the {sl} toolkit on arrival and reads the live network — most issues are diagnosed within 15 minutes and resolved same-day."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How long does a {system} repair take in {suburb}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Reprogramming visits typically take 2–3 hours. Fault-finding in older {suburb} properties with aged cabling can run 3–5 hours. We always give a clear estimate before starting."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can my {system} system in {suburb} be fixed without replacing hardware?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Often yes. Many {suburb} clients are quoted full replacements when the fix is a 20-minute software correction. If it can be resolved in the {sl} toolkit, we will do that first."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Who do I call in {suburb} for emergency {system} repairs after hours?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Call 0422 469 739 directly. We cover {suburb} for emergency callouts and you speak directly to George — no call centre."
        }}
      }}
    ]
  }}
  </script>
"""

def inject_into_page(filepath, suburb, system):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Skip if already enhanced
    if 'AEO FAQ: conversational' in content:
        return False

    faq_html = make_faq_html(suburb, system)
    faq_schema = make_faq_schema(suburb, system)

    # Insert schema into <head> before </head>
    content = content.replace('</head>', faq_schema + '\n</head>', 1)

    # Insert FAQ section before </main> or before <footer>
    if '</main>' in content:
        content = content.replace('</main>', faq_html + '\n</main>', 1)
    elif '<footer' in content:
        content = content.replace('<footer', faq_html + '\n<footer', 1)
    else:
        # fallback: before </body>
        content = content.replace('</body>', faq_html + '\n</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

enhanced = 0
for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
        
    system, suburb = get_suburb_and_system(filename)
    if system and suburb:
        result = inject_into_page(filename, suburb, system)
        if result:
            enhanced += 1

print(f'\nDone — {enhanced} location pages enhanced with AEO conversational content.')
