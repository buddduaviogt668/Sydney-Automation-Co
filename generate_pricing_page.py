import re

with open('book-service.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title and Meta
html = re.sub(r'<title>.*?</title>', '<title>Pricing & Call-Out Rates | Sydney Automation Co.</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Transparent C-Bus and Dynalite repair pricing in Sydney. $150/hr with a 3-hour minimum call-out. No hidden fees.">', html)
html = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Pricing & Call-Out Rates | Sydney Automation Co.">', html)
html = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Transparent C-Bus and Dynalite repair pricing in Sydney. $150/hr with a 3-hour minimum.">', html)
html = html.replace('https://sydneyautomationco.com.au/book-service', 'https://sydneyautomationco.com.au/pricing-sydney')

# Replace Hero
hero_old = r'<div class="hero">.*?</div>\s*</div>\s*<!-- MAIN CONTENT -->'
hero_new = '''<div class="hero">
    <div class="hero-bg">
      <div class="hero-bg-img img1 active"></div>
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="tag" style="display:inline-flex; align-items:center; gap:8px; background:rgba(240,112,32,0.15); color:#f07020; border:1px solid rgba(240,112,32,0.35); border-radius:50px; padding:6px 16px; font-size:13px; font-weight:700; margin-bottom:20px;">Transparent Rates</div>
      <h1>Our <span class="accent">Pricing Structure</span></h1>
      <p>We believe the prestige market deserves transparent, upfront pricing. No open-ended hourly rates without your approval.</p>
    </div>
  </div>
  
  <!-- MAIN CONTENT -->'''
html = re.sub(hero_old, hero_new, html, flags=re.DOTALL)

# Replace Main Grid Content
main_grid_old = r'<!-- LEFT COLUMN -->.*?</div><!-- /sidebar -->'
main_grid_new = '''<!-- LEFT COLUMN -->
    <div>
      <div class="section-label">The Rate Card</div>
      <div class="section-title">Call-Out &amp; Service Rates</div>

      <div style="background:#132647; border:1px solid #2a4a80; border-radius:12px; padding:32px; margin-bottom:40px;">
        <ul class="check-list">
          <li style="font-size:16px; padding:12px 0;"><strong style="color:#f0f4ff;">Consultation &amp; Diagnosis:</strong> $150 / hr</li>
          <li style="font-size:16px; padding:12px 0;"><strong style="color:#f0f4ff;">Standard C-Bus / Dynalite Programming:</strong> $150 / hr</li>
          <li style="font-size:16px; padding:12px 0;"><strong style="color:#f0f4ff;">Re-commissioning / Integration:</strong> $150 / hr</li>
          <li style="font-size:16px; padding:12px 0;"><strong style="color:#f0f4ff;">Emergency / AFSS Compliance:</strong> $150 / hr + 15% premium</li>
        </ul>
      </div>

      <div class="section-label">The Guarantee</div>
      <div class="section-title">3-Hour Minimum Call-Out</div>
      <div style="background:#0d1e3c; border-left:4px solid #f07020; padding:24px; border-radius:4px; margin-bottom:40px;">
        <p style="color:#a8c0e0; font-size:16px; line-height:1.7; margin-bottom:16px;">We arrive on-site fully equipped with the manufacturer diagnostic toolkit and most common replacement modules.</p>
        <p style="color:#f0f4ff; font-size:16px; line-height:1.7; font-weight:600;">If the issue requires less than 3 hours to diagnose and fix, you still pay the 3-hour minimum ($450). If it requires more, we bill hourly at $150/hr.</p>
      </div>

      <div class="section-label">Risk Loading</div>
      <div class="section-title">Prestige Market Premium</div>
      <p style="color:#a8c0e0; font-size:15px; line-height:1.7; margin-bottom:24px;">For harbourside residential properties (e.g. Double Bay, Mosman, Point Piper, Vaucluse): A 15% risk-loading may apply for high-value home automation failure scenarios or multi-building coordination. This ensures we can dedicate the exact resources required to protect your asset.</p>

      <div class="call-box" style="text-align:left; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">
        <p style="margin:0; font-size:16px; color:#f0f4ff; font-weight:600;">Ready to book your diagnostic call?</p>
        <a class="btn btn-primary" href="/book-service" style="font-size:16px;">Book Online Now →</a>
      </div>

    </div>

    <!-- SIDEBAR -->
    <div class="sidebar">
      <div class="info-card">
        <img class="george-photo" src="/george-photo.webp" alt="George">
        <h3>No Surprises</h3>
        <p>Most of our callouts are fixing systems left broken by others. We quote diagnostic time upfront. We provide a written scope before work proceeds. No open-ended billing without your sign-off.</p>
      </div>

      <div class="info-card">
        <h3>Payment Methods</h3>
        <p>We accept Visa, Mastercard, Amex, and Apple Pay via Stripe for priority deposits. Remaining balances can be paid via card or invoice upon completion.</p>
      </div>
    </div>'''
html = re.sub(main_grid_old, main_grid_new, html, flags=re.DOTALL)

with open('pricing-sydney.html', 'w', encoding='utf-8') as f:
    f.write(html)
