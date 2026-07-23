import os
import re

def optimize_conversions():
    """Inject conversion-optimized CTAs and panic-to-peace triggers across all pages"""
    
    # Conversion CTAs to inject
    deposit_cta = """
    <div style="background: linear-gradient(135deg, rgba(240,112,32,0.1) 0%, rgba(77,166,255,0.05) 100%); border: 2px solid #f07020; border-radius: 12px; padding: 30px; margin: 40px 0; text-align: center;">
        <h3 style="color: #fff; margin-top: 0; font-size: 24px;">Secure Your Same-Day Service Call</h3>
        <p style="color: #a8c0e0; font-size: 16px; margin-bottom: 20px;">Don't wait for your lighting system to fail completely. Lock in your appointment with just a $150 deposit.</p>
        <a href="/book-service" style="background-color: #f07020; color: #fff; padding: 15px 40px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; display: inline-block;">Book Service & Pay Deposit →</a>
        <p style="color: #4da6ff; font-size: 13px; margin-top: 15px;">✓ Same-day emergency response | ✓ Expert diagnosis | ✓ Rapid repair</p>
    </div>
    """
    
    panic_trigger = """
    <div style="background: rgba(240,112,32,0.15); border-left: 4px solid #f07020; padding: 20px; margin: 30px 0; border-radius: 4px;">
        <p style="color: #fff; margin: 0; font-weight: 700; font-size: 16px;">⚠️ System Emergency? Call Now: <span style="color: #f07020; font-size: 18px;">0422 469 739</span></p>
        <p style="color: #a8c0e0; margin: 10px 0 0 0; font-size: 14px;">Available for same-day emergency repairs across Greater Sydney</p>
    </div>
    """
    
    directory = "/home/ubuntu/Sydney-Automation-Co"
    count = 0
    
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename not in ["index.html", "test.html"]:
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Inject panic trigger near the top of the page (after hero)
                if "</section>" in content and panic_trigger not in content:
                    first_section_end = content.find("</section>") + len("</section>")
                    content = content[:first_section_end] + panic_trigger + content[first_section_end:]
                
                # Inject deposit CTA before closing main tag
                if "</main>" in content and deposit_cta not in content:
                    main_end = content.find("</main>")
                    content = content[:main_end] + deposit_cta + content[main_end:]
                
                if content != original_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                pass
    
    print(f"✓ Optimized {count} pages with conversion CTAs and panic triggers")

if __name__ == "__main__":
    optimize_conversions()
