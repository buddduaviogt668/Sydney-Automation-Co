import re

# 1. UPDATE BOOK-SERVICE.HTML
with open('book-service.html', 'r', encoding='utf-8') as f:
    book_html = f.read()

pricing_html = """      <p style="color:#a8c0e0; font-size:14px; line-height:1.6;">As highly specialized automation engineers, our time is strictly allocated. The deposit ensures we only dispatch to serious inquiries and eliminates no-shows, allowing us to maintain our rapid response emergency dispatch across Greater Sydney.</p>
      <div style="background:rgba(240,112,32,0.1); border-left:4px solid #f07020; padding:16px; border-radius:4px; margin-top:20px;">
        <h5 style="color:#f0f4ff; margin-bottom:8px; font-size:16px;">Transparent Pricing Policy</h5>
        <p style="color:#a8c0e0; font-size:14px; line-height:1.6; margin:0;">Our standard diagnostic and repair rate is <strong>$150/hr</strong> (ex GST) with a strict <strong>3-hour minimum callout ($450)</strong>. Your $150 priority deposit securely locks in your dispatch and is fully credited toward your final invoice.</p>
      </div>"""

# Replace the specific paragraph with the new one containing the pricing box
book_html = re.sub(
    r'<p style="color:#a8c0e0; font-size:14px; line-height:1.6;">As highly specialized automation engineers, our time is strictly allocated[^<]+</p>',
    pricing_html,
    book_html
)

with open('book-service.html', 'w', encoding='utf-8') as f:
    f.write(book_html)


# 2. REGENERATE TERMS-OF-SERVICE.HTML PROPERLY
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header from index (up to <div class="page">)
header_match = re.search(r'(.*?<div class="page">)', index_html, re.DOTALL)
header = header_match.group(1) if header_match else ''
header = header.replace('<title>Sydney Automation Co', '<title>Terms of Service | Sydney Automation Co')

# Extract footer
footer_match = re.search(r'(<!-- Repair & Emergency Links -->.*|<footer.*?>.*)', index_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

terms_content = """
<div class="hero"><div class="container">
<h1>Terms of <span class="accent">Service</span></h1>
<p class="lead">Effective Date: January 1, 2026</p>
</div></div>

<div class="section"><div class="container">
<div class="article-body" style="max-width:800px; margin:0 auto; background:#112240; padding:40px; border-radius:16px; border:1px solid rgba(255,255,255,0.05);">
    
    <h2>1. General Agreement</h2>
    <p>By engaging Sydney Automation Co for diagnostic, repair, or programming services relating to C-Bus, Dynalite, DALI, or other automation systems, you agree to these terms. We partner directly with Licensed Electrical Contractors for all 240V high-voltage works, while our engineers focus exclusively on low-voltage network diagnostics and programming.</p>

    <h2>2. Rates & Minimum Callout Charges</h2>
    <p>Sydney Automation Co provides highly specialized engineering services. Our standard rates are as follows:</p>
    <ul>
        <li><strong>Hourly Rate:</strong> $150.00 per hour (excluding GST)</li>
        <li><strong>Minimum Callout:</strong> 3 hours ($450.00 excluding GST)</li>
        <li><strong>Priority Dispatch Deposit:</strong> A $150.00 deposit is required to secure priority or emergency bookings. This deposit is fully credited toward the final invoice but is non-refundable in the event of a cancellation within 24 hours of the scheduled arrival.</li>
    </ul>
    <p>The 3-hour minimum charge applies to all site visits, regardless of whether the fault is resolved in less time. This covers our dispatch, travel, specialized software licensing, and immediate availability.</p>

    <h2>3. Quotes & Estimates</h2>
    <p>All quotes provided are estimates based on initial consultations. Automation faults can often present unforeseen hardware failures once diagnostic software is connected. If additional parts or labor are required beyond the initial minimum callout, the client will be notified prior to proceeding.</p>

    <h2>4. Warranties & Liability</h2>
    <p>We provide a 12-month workmanship warranty on all programming and low-voltage integration performed by our technicians. Hardware warranties are strictly governed by the original manufacturer (e.g., Schneider Electric, Signify). Sydney Automation Co is not liable for pre-existing network degradation, catastrophic hardware failure due to power surges, or unauthorized third-party modifications to the code after our departure.</p>

    <h2>5. Payment Terms</h2>
    <p>Invoices are due strictly within 7 days of the invoice date unless otherwise agreed in writing. Ownership of any supplied hardware and programming files remains with Sydney Automation Co until the invoice is paid in full.</p>

</div>
</div></div>
"""

with open('terms-of-service.html', 'w', encoding='utf-8') as f:
    f.write(header + terms_content + footer)

print("Pricing transparency added to book-service.html and terms-of-service.html regenerated.")
