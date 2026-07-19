import os
import re

def optimize_dynalite_conversions():
    """Inject Dynalite-specific authority triggers and conversion CTAs"""
    
    # Dynalite authority CTA
    dynalite_authority_cta = """
    <div style="background: linear-gradient(135deg, rgba(240,112,32,0.1) 0%, rgba(77,166,255,0.05) 100%); border: 2px solid #f07020; border-radius: 12px; padding: 30px; margin: 40px 0; text-align: center;">
        <h3 style="color: #fff; margin-top: 0; font-size: 24px;">Dynalite Certified Technicians Ready Now</h3>
        <p style="color: #a8c0e0; font-size: 16px; margin-bottom: 20px;">Our team is certified in Philips Dynalite system repair, Envision software, and DyNet diagnostics. Same-day emergency service available across Greater Sydney.</p>
        <a href="/book-service" style="background-color: #f07020; color: #fff; padding: 15px 40px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; display: inline-block;">Book Your Dynalite Service & Secure Deposit →</a>
        <p style="color: #4da6ff; font-size: 13px; margin-top: 15px;">✓ Envision Certified | ✓ DyNet Diagnostics | ✓ Emergency Response</p>
    </div>
    """
    
    # Dynalite panic trigger
    dynalite_panic_trigger = """
    <div style="background: rgba(240,112,32,0.15); border-left: 4px solid #f07020; padding: 20px; margin: 30px 0; border-radius: 4px;">
        <p style="color: #fff; margin: 0; font-weight: 700; font-size: 16px;">⚠️ Dynalite Emergency? Call Now: <span style="color: #f07020; font-size: 18px;">0422 469 739</span></p>
        <p style="color: #a8c0e0; margin: 10px 0 0 0; font-size: 14px;">Certified Dynalite technicians available for same-day repairs across Greater Sydney</p>
    </div>
    """
    
    directory = "/home/ubuntu/Sydney-Automation-Co"
    count = 0
    
    for filename in os.listdir(directory):
        # Target Dynalite pages only
        if filename.endswith("-dynalite-repair-sydney.html"):
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Inject Dynalite panic trigger near the top
                if "</section>" in content and dynalite_panic_trigger not in content:
                    first_section_end = content.find("</section>") + len("</section>")
                    content = content[:first_section_end] + dynalite_panic_trigger + content[first_section_end:]
                
                # Inject Dynalite authority CTA before closing main tag
                if "</main>" in content and dynalite_authority_cta not in content:
                    main_end = content.find("</main>")
                    content = content[:main_end] + dynalite_authority_cta + content[main_end:]
                
                if content != original_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                pass
    
    print(f"✓ Optimized {count} Dynalite pages with authority triggers and conversion CTAs")

if __name__ == "__main__":
    optimize_dynalite_conversions()
