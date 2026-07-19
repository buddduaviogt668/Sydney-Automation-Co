import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract from <head> to end of <nav> and start of <div class="page">
header_match = re.search(r'(.*?<div class="page">)', html, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract footer
footer_match = re.search(r'(<!-- Repair & Emergency Links -->.*|<footer.*?>.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

header = header.replace('<title>About George Skarmoutsos', '<title>Book a Service Call - Live Availability')

book_content = """
<div class="hero"><div class="container">
<div class="tag" style="background:rgba(39, 174, 96, 0.2);color:#2ecc71;border:1px solid #2ecc71;">🟢 LIVE OUTLOOK CALENDAR SYNC</div>
<h1>Book a <span class="accent">Priority Service Call</span></h1>
<p class="lead">Secure your spot with Sydney's accredited C-Bus and Dynalite specialists. Choose an available time slot below. A fully refundable deposit is required to secure your booking and eliminate no-shows.</p>
</div></div>

<div class="section"><div class="container">
<div class="grid-2" style="gap:64px; align-items: start;">
  
  <!-- Left Side: Value Prop -->
  <div>
    <h2 style="font-size:32px; margin-bottom:24px;">What happens next?</h2>
    
    <div style="display:flex; gap:16px; margin-bottom:24px;">
      <div style="width:40px; height:40px; border-radius:50%; background:#f07020; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">1</div>
      <div>
        <h3 style="font-size:20px; margin-bottom:8px;">Pick Your Time</h3>
        <p style="color:#a8c0e0; line-height:1.6;">Select a time that works for you. Our calendar is synced live with George's schedule. You'll receive instant email confirmation.</p>
      </div>
    </div>

    <div style="display:flex; gap:16px; margin-bottom:24px;">
      <div style="width:40px; height:40px; border-radius:50%; background:#f07020; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">2</div>
      <div>
        <h3 style="font-size:20px; margin-bottom:8px;">Secure Deposit (Stripe)</h3>
        <p style="color:#a8c0e0; line-height:1.6;">We take a small deposit via secure Stripe checkout to confirm your priority booking. This is fully credited toward your final invoice.</p>
      </div>
    </div>

    <div style="display:flex; gap:16px; margin-bottom:24px;">
      <div style="width:40px; height:40px; border-radius:50%; background:#f07020; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">3</div>
      <div>
        <h3 style="font-size:20px; margin-bottom:8px;">Expert Diagnostic</h3>
        <p style="color:#a8c0e0; line-height:1.6;">George arrives fully equipped with manufacturer software and diagnostic tools to isolate your network fault with zero guesswork.</p>
      </div>
    </div>

    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); padding:24px; border-radius:12px; margin-top:40px;">
      <h4 style="color:#f0f4ff; margin-bottom:12px;">Why do we require a deposit?</h4>
      <p style="color:#a8c0e0; font-size:14px; line-height:1.6;">As highly specialized automation engineers, our time is strictly allocated. The deposit ensures we only dispatch to serious inquiries, allowing us to maintain our rapid response times across Greater Sydney.</p>
    </div>
  </div>

  <!-- Right Side: Calendar Embed -->
  <div style="background:#fff; border-radius:16px; padding:32px; box-shadow:0 20px 40px rgba(0,0,0,0.4); text-align:center;">
    <div style="color:#0e1f3d; font-family:'Barlow Condensed', sans-serif; font-size:28px; font-weight:900; margin-bottom:16px; text-transform:uppercase;">Select a Time Slot</div>
    <p style="color:#4a6a9a; margin-bottom:24px;">This is where your live Outlook calendar will appear. Customers will click a time, enter their details, and pay the deposit via Stripe.</p>
    
    <!-- Placeholder for Cal.com or Calendly Widget -->
    <div style="border:2px dashed #a8c0e0; border-radius:12px; height:400px; display:flex; align-items:center; justify-content:center; background:#f8f9fa; flex-direction:column; gap:16px;">
      <div style="font-size:48px;">📅</div>
      <div style="color:#4a6a9a; font-weight:bold; font-size:18px;">[ CALENDAR WIDGET GOES HERE ]</div>
      <p style="color:#6a8cb5; font-size:14px; max-width:250px;">Setup required: Connect your Outlook and Stripe to Cal.com or Calendly to generate your embed code.</p>
    </div>

  </div>

</div>
</div></div>
</div>
"""

with open('book-service.html', 'w', encoding='utf-8') as f:
    f.write(header + book_content + footer)

print('Created book-service.html')
