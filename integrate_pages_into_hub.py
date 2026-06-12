
import os
import re

def integrate_pages_into_hub(services_hub_path):
    with open(services_hub_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define new sections to add before the footer
    new_sections = """
<section id="technical-authority-pages" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">🔬</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">Technical Authority Guides</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">Comprehensive deep-dive guides on C-Bus, Dynalite, KNX, DALI-2, and emerging smart home standards. Establish your expertise and dominate technical searches.</p>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
  <a href="/c-bus-network-deep-dive-advanced-diagnostics" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">C-Bus Network Deep Dive: Advanced Diagnostics</a>
  <a href="/dynalite-system-architecture-design-installation" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Dynalite System Architecture: Design & Installation</a>
  <a href="/knx-protocol-explained-integration-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">KNX Protocol Explained: Integration for Sydney</a>
  <a href="/dali-2-lighting-control-commercial-buildings" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">DALI-2 Lighting Control: Commercial Implementation</a>
  <a href="/matter-thread-smart-homes-interoperability-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Matter & Thread: The Future of Smart Homes</a>
  </div>
</section>

<section id="industry-vertical-pages" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">🏢</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">Industry-Specific Solutions</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">Tailored automation solutions for tech hubs, luxury estates, hospitality venues, warehouses, and retail. Target high-value commercial and residential segments.</p>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
  <a href="/intelligent-workspace-automation-north-sydney-tech-hubs" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Intelligent Workspace Automation for Tech Hubs</a>
  <a href="/luxury-smart-home-integration-eastern-suburbs-estates" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Luxury Smart Home Integration for Eastern Suburbs</a>
  <a href="/smart-lighting-energy-management-sydney-hospitality" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Smart Lighting for Sydney Hospitality Venues</a>
  <a href="/industrial-automation-high-bay-lighting-western-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Industrial Automation for Western Sydney Warehouses</a>
  <a href="/atmospheric-lighting-automation-sydney-cbd-retailers" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Atmospheric Lighting for Sydney CBD Retailers</a>
  </div>
</section>

<section id="decision-support-pages" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">📊</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">Comparison & ROI Guides</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">Help clients make informed decisions with system comparisons, ROI calculators, and transparent cost guides. Capture users in the research phase.</p>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
  <a href="/c-bus-vs-dynalite-vs-knx-comparison-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">C-Bus vs Dynalite vs KNX: System Comparison</a>
  <a href="/smart-home-roi-calculator-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Smart Home ROI Calculator for Sydney</a>
  <a href="/sydney-home-automation-cost-guide-2026" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Sydney Home Automation Cost Guide 2026</a>
  </div>
</section>

<section id="solution-service-pages" style="margin-bottom:72px;">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;border-bottom:2px solid #1a2a4a;padding-bottom:20px;">
    <span style="font-size:40px;">⚡</span>
    <div>
      <h2 style="font-family:'Barlow Condensed',sans-serif;font-size:clamp(24px,3vw,36px);font-weight:900;color:#fff;margin:0 0 6px;">Advanced Solutions & Services</h2>
      <p style="color:#a8c0e0;font-size:15px;margin:0;">Expand beyond repairs to installations, retrofits, AI-driven systems, heritage solutions, and premium audiovisual integration.</p>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:20px;">
  <a href="/ai-driven-smart-lighting-energy-management-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">AI-Driven Smart Lighting & Energy Management</a>
  <a href="/invisible-automation-heritage-retrofitting-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">Invisible Automation & Heritage Retrofitting</a>
  <a href="/high-end-home-cinema-multi-room-audio-sydney" style="display:block;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px 16px;color:#a8c0e0;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'" onmouseout="this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'">High-End Home Cinema & Multi-Room Audio</a>
  </div>
</section>
"""

    # Find the closing </div> tag before the footer or body closing tag
    # Look for a suitable insertion point - typically before the last closing tags
    insert_position = content.rfind('</div>')
    if insert_position != -1:
        # Find the last occurrence of </section> before the end
        last_section_end = content.rfind('</section>')
        if last_section_end != -1 and last_section_end > insert_position:
            insert_position = last_section_end + len('</section>')
    
    # If we can't find a good spot, insert before </body>
    if insert_position == -1 or insert_position < len(content) - 1000:
        insert_position = content.rfind('</body>')
        if insert_position == -1:
            insert_position = content.rfind('</html>')
    
    # Insert the new sections
    updated_content = content[:insert_position] + new_sections + content[insert_position:]
    
    with open(services_hub_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Successfully integrated new pages into services hub at position {insert_position}")

# Run the integration
services_hub_path = "/home/ubuntu/Sydney-Automation-Co/services-hub.html"
integrate_pages_into_hub(services_hub_path)
