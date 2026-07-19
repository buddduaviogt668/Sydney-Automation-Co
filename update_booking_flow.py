import re

# Read template header/footer from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'(.*?<div class="page">)', html, re.DOTALL)
header = header_match.group(1) if header_match else ''
footer_match = re.search(r'(<!-- Repair & Emergency Links -->.*|<footer.*?>.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

header_book = header.replace('<title>About George Skarmoutsos', '<title>Secure Your Booking - Priority Service Call')
header_schedule = header.replace('<title>About George Skarmoutsos', '<title>Select Your Time Slot - Microsoft Bookings')

# 1. Update book-service.html to be the Stripe Deposit page
book_content = """
<div class="hero"><div class="container">
<div class="tag" style="background:rgba(39, 174, 96, 0.2);color:#2ecc71;border:1px solid #2ecc71;">🔒 SECURE CHECKOUT</div>
<h1>Secure Your <span class="accent">Priority Service Call</span></h1>
<p class="lead">To ensure rapid response times across Greater Sydney, we require a fully refundable deposit to secure your booking. Once confirmed, you will instantly unlock George's live Outlook calendar to select your exact arrival time.</p>
</div></div>

<div class="section"><div class="container">
<div class="grid-2" style="gap:64px; align-items: start;">
  
  <!-- Left Side: Value Prop -->
  <div>
    <h2 style="font-size:32px; margin-bottom:24px;">How this works</h2>
    
    <div style="display:flex; gap:16px; margin-bottom:24px;">
      <div style="width:40px; height:40px; border-radius:50%; background:#f07020; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">1</div>
      <div>
        <h3 style="font-size:20px; margin-bottom:8px;">Secure Deposit (Stripe)</h3>
        <p style="color:#a8c0e0; line-height:1.6;">Click the button to pay a secure deposit via Stripe. This is fully credited toward your final diagnostic/repair invoice.</p>
      </div>
    </div>

    <div style="display:flex; gap:16px; margin-bottom:24px;">
      <div style="width:40px; height:40px; border-radius:50%; background:#f07020; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">2</div>
      <div>
        <h3 style="font-size:20px; margin-bottom:8px;">Unlock Live Calendar</h3>
        <p style="color:#a8c0e0; line-height:1.6;">Immediately after payment, you will be redirected to our live Microsoft Bookings calendar to pick an available time slot.</p>
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
      <p style="color:#a8c0e0; font-size:14px; line-height:1.6;">As highly specialized automation engineers, our time is strictly allocated. The deposit ensures we only dispatch to serious inquiries and eliminates no-shows, allowing us to maintain our rapid response emergency dispatch across Greater Sydney.</p>
    </div>
  </div>

  <!-- Right Side: Stripe Button -->
  <div style="background:#fff; border-radius:16px; padding:40px 32px; box-shadow:0 20px 40px rgba(0,0,0,0.4); text-align:center;">
    <div style="color:#0e1f3d; font-family:'Barlow Condensed', sans-serif; font-size:32px; font-weight:900; margin-bottom:16px; text-transform:uppercase;">Priority Booking Deposit</div>
    <p style="color:#4a6a9a; margin-bottom:32px; font-size:16px; font-weight:600;">Fully credited towards your final invoice.</p>
    
    <!-- STRIPE PAYMENT LINK GOES HERE -->
    <a href="#" class="sac-stripe-btn" style="display:inline-block; background:#635BFF; color:#fff; font-size:18px; font-weight:bold; padding:20px 40px; border-radius:12px; text-decoration:none; box-shadow:0 10px 20px rgba(99, 91, 255, 0.3); transition:all 0.2s; width:100%;">
      💳 Pay Deposit via Stripe
    </a>
    <p style="color:#6a8cb5; font-size:13px; margin-top:24px; max-width:300px; margin-left:auto; margin-right:auto;">
      *Replace the href="#" above with your actual Stripe Payment Link URL.
    </p>
    
    <div style="margin-top:32px; display:flex; justify-content:center; gap:16px; opacity:0.6;">
      <span style="color:#0e1f3d; font-weight:bold; font-size:24px;">🔒</span>
      <span style="color:#0e1f3d; font-weight:bold; font-size:24px;">💳</span>
      <span style="color:#0e1f3d; font-weight:bold; font-size:24px;">🍎</span>
    </div>
  </div>

</div>
</div></div>
</div>
"""

with open('book-service.html', 'w', encoding='utf-8') as f:
    f.write(header_book + book_content + footer)

# 2. Create schedule-booking.html for the MS Bookings iframe
schedule_content = """
<div class="hero"><div class="container" style="text-align:center;">
<div class="tag" style="background:rgba(39, 174, 96, 0.2);color:#2ecc71;border:1px solid #2ecc71;">🟢 PAYMENT CONFIRMED</div>
<h1>Select Your <span class="accent">Time Slot</span></h1>
<p class="lead" style="margin: 0 auto;">Your deposit has been successfully captured. Please select a convenient time from George's live schedule below to finalize your dispatch.</p>
</div></div>

<div class="section"><div class="container" style="max-width:1000px; margin:0 auto;">
  
  <div style="background:#fff; border-radius:16px; padding:24px; box-shadow:0 20px 40px rgba(0,0,0,0.4); text-align:center; min-height:600px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    
    <!-- MS BOOKINGS IFRAME GOES HERE -->
    <div style="border:2px dashed #a8c0e0; border-radius:12px; height:400px; width:100%; display:flex; align-items:center; justify-content:center; background:#f8f9fa; flex-direction:column; gap:16px;">
      <div style="font-size:48px;">📅</div>
      <div style="color:#4a6a9a; font-weight:bold; font-size:18px;">[ MICROSOFT BOOKINGS IFRAME GOES HERE ]</div>
      <p style="color:#6a8cb5; font-size:14px; max-width:350px;">Paste the iframe embed code from your Microsoft Bookings dashboard here.</p>
    </div>

  </div>

</div></div>
</div>
"""

with open('schedule-booking.html', 'w', encoding='utf-8') as f:
    f.write(header_schedule + schedule_content + footer)

print("Updated booking flow for Stripe + Microsoft Bookings")
