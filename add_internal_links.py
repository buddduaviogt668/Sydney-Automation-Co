import os

pages = [
    'index.html',
    'services.html',
    'about.html',
    'cbus-vs-dynalite.html',
    'cbus-specialist-sydney.html',
    'lighting-control-repair-sydney.html',
    'building-automation-maintenance-sydney.html',
    'emergency-repair-sydney.html'
]

link_block = """
<!-- RELATED REPAIR LINKS -->
<section style="padding: 40px 0; background: #00111f; border-top: 1px solid rgba(255,255,255,0.05);">
  <div style="max-width: 1100px; margin: 0 auto; padding: 0 24px; text-align: center;">
    <h3 style="font-family: 'Barlow Condensed', sans-serif; font-size: 24px; color: #f0f4ff; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px;">Specialist Repair Services</h3>
    <p style="color: #a8c0e0; font-size: 15px; max-width: 600px; margin: 0 auto 24px auto; line-height: 1.6;">
      Experiencing a critical lighting failure? We offer dedicated <a href="/cbus-repair-sydney" style="color: #f07020; text-decoration: underline;">C-Bus Repair in Sydney</a> as well as expert <a href="/dynalite-repair-sydney" style="color: #f07020; text-decoration: underline;">Dynalite Repair in Sydney</a>. Our certified technicians carry replacement parts for both systems to ensure same-day resolution for most faults.
    </p>
  </div>
</section>
"""

for page in pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "<!-- RELATED REPAIR LINKS -->" not in content:
            # Find footer to insert before it
            if "<footer>" in content:
                content = content.replace("<footer>", link_block + "\n<footer>")
            else:
                # Some pages might have a different footer format, let's try a fallback
                content = content.replace("<!-- FOOTER -->", link_block + "\n<!-- FOOTER -->")
                
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added internal links to {page}")
    else:
        print(f"File not found: {page}")
