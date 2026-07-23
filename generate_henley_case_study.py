import os
import re

with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

head_match = re.search(r'(.*?<div class="page">)', template, re.DOTALL)
footer_match = re.search(r'(<footer.*)', template, re.DOTALL)

if not head_match or not footer_match:
    print("Could not parse template")
    exit(1)

head = head_match.group(1)
footer = footer_match.group(1)

content_html = """
<div style="color:#f0f4ff;line-height:1.8;font-size:1.05rem;">
    <div style="display:flex;gap:20px;margin-bottom:32px;flex-wrap:wrap;">
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">📍 Location: Henley, Sydney</span>
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">⚙️ System: Clipsal C-Bus</span>
        <span style="background:rgba(240,112,32,0.15);color:#f07020;padding:6px 12px;border-radius:6px;font-weight:700;font-size:0.9rem;">🛠️ Service: Fault Finding & Hardware Upgrade</span>
    </div>

    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">The Problem: Dead Switches & Lights Failing</h2>
    <p style="margin-bottom:20px;">The client in Henley was experiencing complete system unresponsiveness—lights were failing to turn on, and multiple C-Bus wall switches appeared completely dead. This is a common symptom when the C-Bus network loses its underlying data voltage.</p>
    
    <div style="margin:40px 0;text-align:center;">
        <img src="/images/henley-cbus-repair-1.jpg" alt="Faulty C-Bus Power Supplies in Henley Switchboard" style="max-width:100%;border-radius:12px;border:1px solid #2a4a80;box-shadow:0 8px 32px rgba(0,0,0,0.4);">
        <p style="color:#7a9cc0;font-size:0.9rem;margin-top:12px;">Diagnosing the main C-Bus distribution board.</p>
    </div>

    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">The Diagnosis & Repair</h2>
    <p style="margin-bottom:20px;">Upon arriving in Henley, our initial diagnostics with the C-Bus toolkit revealed massive communication faults across the network. Many Clipsal C-Bus relays, dimmers, and power supplies installed in the early 2000s are now reaching the end of their operational lifespan. Over time, internal capacitors fail, making them highly susceptible to power surges and storm activity.</p>
    
    <div style="margin:40px 0;display:grid;grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));gap:24px;">
        <div>
            <img src="/images/henley-cbus-repair-2.jpg" alt="New SpaceLogic C-Bus Dimmer Installation" style="width:100%;border-radius:12px;border:1px solid #2a4a80;">
            <p style="color:#7a9cc0;font-size:0.9rem;margin-top:12px;">Upgrading legacy blue units to modern SpaceLogic dimmers.</p>
        </div>
        <div>
            <img src="/images/henley-cbus-repair-3.jpg" alt="Restored C-Bus Staircase Lighting in Henley" style="width:100%;border-radius:12px;border:1px solid #2a4a80;">
            <p style="color:#7a9cc0;font-size:0.9rem;margin-top:12px;">Full lighting functionality restored to the client's stairwell.</p>
        </div>
    </div>

    <h2 style="color:#f07020;font-size:1.8rem;margin-bottom:20px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;">The Outcome</h2>
    <p style="margin-bottom:20px;">This project involved replacing the faulty legacy C-Bus power supplies and dimmers with modern, robust equivalents (including the new SpaceLogic range). Following the hardware replacement, we worked closely with the site electrician to troubleshoot multiple network cabling faults that were pulling down the data bus.</p>
    
    <div style="background:rgba(14,31,61,0.5);border:1px solid #2a4a80;padding:24px;border-radius:12px;margin-bottom:32px;">
        <h3 style="color:#fff;margin-bottom:12px;font-weight:700;">Result</h3>
        <p style="margin:0;">Reliable system operation was fully restored. The client regained complete control of their smart home lighting, and the new power supplies provide a stabilized network foundation for the next decade.</p>
    </div>
</div>
"""

custom_head = head.replace("<title>C-Bus &amp; Dynalite Repairs Sydney | Same-Day Automation Fault Finding | Sydney Automation Co.</title>", "<title>Case Study: C-Bus System Repair & Upgrade in Henley</title>")
custom_head = re.sub(r'<meta content=".*?" name="description"/>', '<meta content="Read our case study on repairing and upgrading an early 2000s C-Bus lighting control system in Henley, Sydney. We replaced faulty power supplies and dimmers." name="description"/>', custom_head)

html = custom_head + f"""
<div class="hero" style="padding:100px 24px 60px;">
  <div class="container-sm">
    <div class="tag">Case Study</div>
    <h1 style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:clamp(2.5rem,5vw,4rem);text-transform:uppercase;line-height:1;margin-bottom:16px;">
        C-Bus System Repair & Upgrade: Henley
    </h1>
    <p class="lead" style="font-size:1.15rem;color:#a8c0e0;max-width:700px;margin:0 auto 32px;">Resolving complete system failure by replacing end-of-life power supplies and troubleshooting complex network cabling faults.</p>
  </div>
</div>
<div class="section" style="padding-top:20px;">
  <div class="container-sm">
    {content_html}
    <div class="cta-band" style="margin-top:64px;background:rgba(240,112,32,0.1);border:1px solid rgba(240,112,32,0.3);border-radius:16px;padding:40px;text-align:center;">
      <h2 style="font-size:28px;margin-bottom:16px;font-family:'Barlow Condensed',sans-serif;font-weight:800;">Are your C-Bus lights failing?</h2>
      <p style="color:#c8d8ec;margin-bottom:24px;">Don't let legacy hardware keep you in the dark. Call George for a complete system health check.</p>
      <a href="tel:0422469739" class="btn btn-primary" style="font-size:1.1rem;padding:14px 32px;">📞 Call George: 0422 469 739</a>
    </div>
  </div>
</div>
""" + footer

with open("case-study-cbus-repair-henley.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Created Henley case study page.")
