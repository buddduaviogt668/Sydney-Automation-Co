import re

def update_index():
    path = "/home/ubuntu/Sydney-Automation-Co/index.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Hero Lead Text for Energy ROI
    old_lead = 'System crashed? Lights stuck on? Scenes not responding? We diagnose and fix the complex C-Bus, Dynalite &amp; DALI lighting faults that regular electricians can\'t — same day, across Greater Sydney.'
    new_lead = 'System crashed? Lights stuck on? Scenes not responding? We diagnose complex C-Bus, Dynalite &amp; DALI faults that regular electricians can\'t. **Cut energy overheads by up to 60%** with our building optimization and DALI-2 compliance audits — same day, across Greater Sydney.'
    content = content.replace(old_lead, new_lead)

    # 2. Add Energy ROI Section before "Specialist Services"
    energy_roi_section = """
  <!-- ENERGY ROI & BUILDING OPTIMIZATION -->
  <section style="background: #001f3d; padding: 100px 0; border-top: 1px solid rgba(255,255,255,0.05);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
        <div>
          <span style="color: #f07020; font-weight: 800; letter-spacing: 3px; text-transform: uppercase; font-size: 13px; display: block; margin-bottom: 15px;">Building Optimization</span>
          <h2 style="font-size: clamp(32px, 4vw, 48px); line-height: 1.1; color: #fff; margin-bottom: 25px;">Stop Overpaying for <span class="accent">Commercial Lighting</span></h2>
          <p class="dim" style="font-size: 18px; line-height: 1.8; margin-bottom: 30px;">In a tightening economy, lighting isn't just an expense—it's an opportunity for ROI. We frame DALI-2, RAPIX, and C-Bus SpaceLogic upgrades around **measurable energy savings**, not just "new bulbs."</p>
          
          <div style="display: grid; gap: 20px;">
            <div style="display: flex; gap: 15px;">
              <div style="color: #f07020; font-size: 24px;">📊</div>
              <div>
                <h4 style="color: #fff; margin-bottom: 5px;">Baseline Power Reduction</h4>
                <p class="dim" style="font-size: 15px;">Slashing baseline power bills by optimizing dimming curves and sensor timeouts.</p>
              </div>
            </div>
            <div style="display: flex; gap: 15px;">
              <div style="color: #f07020; font-size: 24px;">☀️</div>
              <div>
                <h4 style="color: #fff; margin-bottom: 5px;">Daylight Harvesting</h4>
                <p class="dim" style="font-size: 15px;">Automated adjustment of internal lighting based on natural ambient light levels.</p>
              </div>
            </div>
            <div style="display: flex; gap: 15px;">
              <div style="color: #f07020; font-size: 24px;">⚖️</div>
              <div>
                <h4 style="color: #fff; margin-bottom: 5px;">DALI-2 Compliance ROI</h4>
                <p class="dim" style="font-size: 15px;">Meeting NSW energy mandates while improving long-term asset value.</p>
              </div>
            </div>
          </div>
          
          <a href="/led-upgrade-carpark-lighting-sydney" class="nav-cta" style="display: inline-block; margin-top: 40px; padding: 15px 30px !important; font-size: 16px;">Request an Energy ROI Audit →</a>
        </div>
        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; right: 0; padding: 20px; background: #f07020; color: #fff; font-weight: 900; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; transform: rotate(45deg) translate(30px, -20px); width: 150px; text-align: center;">2026 Ready</div>
          <h3 style="color: #fff; font-family: 'Barlow Condensed', sans-serif; font-size: 28px; margin-bottom: 20px;">Projected Savings Table</h3>
          <table style="width: 100%; border-collapse: collapse; color: #a8c0e0; font-size: 14px;">
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
              <th style="text-align: left; padding: 12px 0; color: #fff;">Building Type</th>
              <th style="text-align: right; padding: 12px 0; color: #fff;">Est. ROI</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
              <td style="padding: 12px 0;">Commercial Office (CBD)</td>
              <td style="text-align: right; color: #4da6ff;">14 - 18 Months</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
              <td style="padding: 12px 0;">Industrial Warehouse</td>
              <td style="text-align: right; color: #4da6ff;">11 - 15 Months</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
              <td style="padding: 12px 0;">Strata Car Park</td>
              <td style="text-align: right; color: #4da6ff;">9 - 12 Months</td>
            </tr>
          </table>
          <p style="margin-top: 20px; font-size: 12px; font-style: italic; opacity: 0.6;">*Based on average 2026 NSW energy tariffs and intelligent sensor integration.</p>
        </div>
      </div>
    </div>
  </section>
"""
    # Insert before <section class="services-section" id="services">
    content = content.replace('<section class="services-section" id="services">', energy_roi_section + '\n  <section class="services-section" id="services">')

    # 3. Update Trade Partner Section (B2B WEDGE)
    # Using a regex to find the B2B WEDGE block more reliably
    pattern = r'<!-- B2B WEDGE -->.*?Partner with us\s+→</a>\s+</p>\s+</div>'
    new_b2b_wedge = """      <!-- WHITE-LABEL TRADE PARTNER SECTION -->
      <div style="margin-top: 100px; padding: 60px; background: linear-gradient(135deg, rgba(77,166,255,0.08) 0%, rgba(0,0,0,0) 100%); border: 1px solid rgba(77,166,255,0.2); border-radius: 32px; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(77,166,255,0.1) 0%, transparent 70%); z-index: 0;"></div>
        <div style="position: relative; z-index: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; text-align: left;">
          <div>
            <h2 style="color: #fff; font-family: 'Barlow Condensed', sans-serif; font-size: 42px; margin-bottom: 20px;">Your Secret <span style="color: #4da6ff;">Technical Partner</span></h2>
            <p class="dim" style="font-size: 18px; line-height: 1.8; margin-bottom: 25px;">Keep the client, we’ll do the programming. We provide **100% White-Label Support** for electricians and builders who are stuck on-site with complex C-Bus Pascal scripting or Dynalite task-based programming.</p>
            <ul style="list-style: none; padding: 0; margin-bottom: 30px; display: grid; gap: 12px;">
              <li style="display: flex; gap: 10px; align-items: center; color: #a8c0e0;"><span style="color: #4da6ff;">✔</span> No Logos, Total Discretion</li>
              <li style="display: flex; gap: 10px; align-items: center; color: #a8c0e0;"><span style="color: #4da6ff;">✔</span> Specialist Tier Commissioning</li>
              <li style="display: flex; gap: 10px; align-items: center; color: #a8c0e0;"><span style="color: #4da6ff;">✔</span> Remote & On-Site Programming</li>
            </ul>
            <a href="/trade-partner-electrician-support-sydney" class="nav-cta" style="background: #4da6ff !important; padding: 15px 30px !important; font-size: 16px;">View Trade Partnership Terms →</a>
          </div>
          <div style="background: rgba(0,0,0,0.3); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.05);">
            <h4 style="color: #fff; margin-bottom: 15px; font-family: 'Barlow Condensed', sans-serif; letter-spacing: 1px; text-transform: uppercase;">Why Partner With Us?</h4>
            <div style="display: grid; gap: 20px;">
              <div style="padding: 15px; background: rgba(255,255,255,0.02); border-radius: 12px;">
                <p style="color: #fff; font-weight: 700; margin-bottom: 4px; font-size: 14px;">Protect Your Reputation</p>
                <p style="font-size: 13px; color: #a8c0e0;">We solve the logic issues that make systems look "broken" to your clients.</p>
              </div>
              <div style="padding: 15px; background: rgba(255,255,255,0.02); border-radius: 12px;">
                <p style="color: #fff; font-weight: 700; margin-bottom: 4px; font-size: 14px;">Expert Commissioning</p>
                <p style="font-size: 13px; color: #a8c0e0;">Accredited in DALI-2, C-Bus, and Signify Dynalite System Design.</p>
              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    content = re.sub(pattern, new_b2b_wedge, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_index()
