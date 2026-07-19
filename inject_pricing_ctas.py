import os
import re
import glob

PRICING_BLOCK = """<!-- PRICING & CALL-OUT GUARANTEE -->
<div class="section" style="background:#0a1828; border-top:1px solid #2a4a80;">
  <div class="container">
    <div class="section-header">
      <div class="tag">Transparent Pricing</div>
      <h2>Pricing &amp; Call-Out <span class="accent">Guarantee</span></h2>
      <p class="dim" style="max-width:540px;margin:0 auto">We believe the prestige market deserves transparent, upfront pricing. No hidden fees, no open-ended hourly rates without approval.</p>
    </div>
    
    <div class="grid-2" style="gap:32px; align-items: stretch;">
      <div class="card" style="background:#0e1f3d;">
        <h3 style="margin-bottom:16px;">Rate Card</h3>
        <ul class="check-list">
          <li><strong style="color:#f0f4ff;">Consultation &amp; Diagnosis:</strong> $150/hr</li>
          <li><strong style="color:#f0f4ff;">C-Bus &amp; Dynalite Programming:</strong> $150/hr</li>
          <li><strong style="color:#f0f4ff;">Re-commissioning / Integration:</strong> $150/hr</li>
          <li><strong style="color:#f0f4ff;">Emergency / AFSS Compliance:</strong> $150/hr + 15% premium</li>
          <li><strong style="color:#f0f4ff;">Minimum Call-Out:</strong> 3 hours ($450)</li>
        </ul>
        <div style="margin-top:24px; padding:16px; background:rgba(240,112,32,0.1); border-left:3px solid #f07020; border-radius:4px;">
          <h4 style="color:#f07020; font-size:14px; margin-bottom:8px;">Prestige Market Premium</h4>
          <p style="font-size:13px; color:#a8c0e0; line-height:1.5;">For harbourside residential (Double Bay, Mosman, Point Piper, etc): 15% risk-loading may apply for high-value home automation failure scenarios or multi-building coordination.</p>
        </div>
      </div>
      
      <div class="card" style="background:#0e1f3d;">
        <h3 style="margin-bottom:16px;">Our Call-Out Guarantee</h3>
        <p class="dim" style="font-size:15px; line-height:1.7; margin-bottom:16px;">We arrive on-site fully equipped with the manufacturer diagnostic toolkit and most common replacement modules.</p>
        <p class="dim" style="font-size:15px; line-height:1.7; margin-bottom:24px;">If the issue requires less than 3 hours to diagnose and fix, you still pay the 3-hour minimum ($450). If it requires more, we bill hourly at $150/hr. <strong>No work proceeds without your approval.</strong></p>
        
        <div class="btns">
          <a href="/book-service" class="btn btn-primary">Book $450 Diagnostic Call</a>
          <a href="tel:0422469739" class="btn btn-outline">Call 0422 469 739</a>
        </div>
      </div>
    </div>
  </div>
</div>
"""

def inject_pricing(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "PRICING & CALL-OUT GUARANTEE" in content:
            return False, "Already injected"
            
        # Target injection points in order of preference
        injection_points = [
            "<!-- CTA BAND -->",
            "<!-- FAQS -->",
            "<!-- SERVICE AREA -->",
            "<!-- RELATED SERVICES -->",
            "<!-- FOOTER -->",
            "<footer>"
        ]
        
        for point in injection_points:
            if point in content:
                new_content = content.replace(point, PRICING_BLOCK + "\n" + point)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True, f"Injected before {point}"
                
        return False, "No injection point found"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    
    # Target all HTML files in current directory
    html_files = glob.glob("*.html")
    
    # Filter for service pages
    pattern = re.compile(r".*(repair|programmer|service|maintenance|upgrade|fault|specialist).*\.html")
    target_files = [f for f in html_files if pattern.match(f)]
    
    print(f"Found {len(target_files)} target service pages.")
    
    success_count = 0
    fail_count = 0
    
    for f in target_files:
        if f == "book-service.html" or f == "services.html" or f == "services-hub.html":
            continue # skip booking page and hubs
            
        success, msg = inject_pricing(f)
        if success:
            success_count += 1
        else:
            fail_count += 1
            # print(f"Failed {f}: {msg}")
            
    print(f"Successfully injected into {success_count} files.")
    print(f"Skipped/Failed {fail_count} files.")
