import os

case_study_block = """
<!-- DWELL TIME: REMOTE COMMISSIONING CASE STUDY -->
<section style="padding: 80px 0; background: linear-gradient(180deg, #001428 0%, #00111f 100%); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
  <div style="max-width: 900px; margin: 0 auto; padding: 0 24px;">
    <div style="text-align: center; margin-bottom: 40px;">
      <h2 style="font-family: 'Barlow Condensed', sans-serif; font-size: 32px; color: #f0f4ff; margin-bottom: 16px; text-transform: uppercase;">Recent Project Highlight</h2>
      <p style="color: #a8c0e0; font-size: 16px; max-width: 600px; margin: 0 auto;">Beyond local Sydney repairs, our expertise allows us to resolve complex lighting control faults anywhere in Australia.</p>
    </div>
    
    <div style="background: rgba(0, 20, 40, 0.4); border: 1px solid rgba(240,112,32,0.15); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;">
      <img src="/uluru-12-graduation.jpg" alt="Uluru Meeting Place - Graduation Event at Ayers Rock Resort" style="width: 100%; height: 300px; object-fit: cover;" loading="lazy">
      <div style="padding: 32px;">
        <div style="display: flex; gap: 8px; margin-bottom: 16px;">
          <span style="background: rgba(240,112,32,0.1); color: #f07020; padding: 4px 12px; border-radius: 100px; font-size: 13px; font-weight: 600;">DALI-2 / Dynalite</span>
          <span style="background: rgba(168,192,224,0.1); color: #a8c0e0; padding: 4px 12px; border-radius: 100px; font-size: 13px; font-weight: 600;">Remote Delivery</span>
        </div>
        <h3 style="color: #f0f4ff; font-size: 24px; margin-bottom: 16px; line-height: 1.3;">Uluru Meeting Place (Ayers Rock Resort)</h3>
        <p style="color: #a8c0e0; font-size: 16px; line-height: 1.7; margin-bottom: 24px;">
          Sydney Automation Co. was engaged to commission a new DALI lighting installation in the Ballrooms at the iconic Uluru Meeting Place. Replacing older DSI fittings with modern DALI LED drivers, we programmed complex room-join functionality across the ballroom and foyer — <strong>delivered entirely remotely from Sydney</strong>. This demonstrates our ability to troubleshoot and resolve advanced network faults and configuration issues regardless of distance.
        </p>
        <a href="/projects#uluru" style="display: inline-flex; align-items: center; gap: 8px; color: #f07020; font-weight: 700; text-decoration: none;">View Full Project Details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg></a>
      </div>
    </div>
  </div>
</section>
"""

def add_case_study(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "<!-- DWELL TIME: REMOTE COMMISSIONING CASE STUDY -->" not in content:
            # Insert just before the FAQ section
            if "<!-- FAQ -->" in content:
                content = content.replace("<!-- FAQ -->", case_study_block + "\n<!-- FAQ -->")
            else:
                # Fallback, find the first faq-item and insert before its parent container
                faq_index = content.find('<div class="faq-item">')
                if faq_index != -1:
                    # Find the nearest section start tag before the faq-item
                    section_index = content.rfind('<section', 0, faq_index)
                    if section_index == -1:
                        section_index = content.rfind('<div class="section"', 0, faq_index)
                        
                    if section_index != -1:
                        content = content[:section_index] + case_study_block + "\n" + content[section_index:]
                        
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added case study to {filepath}")
    else:
        print(f"File not found: {filepath}")

add_case_study('cbus-repair-sydney.html')
add_case_study('dynalite-repair-sydney.html')
