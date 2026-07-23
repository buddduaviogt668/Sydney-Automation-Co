
import os
import re
from datetime import datetime

def generate_dynalite_suburb_pages():
    suburbs_file = "/home/ubuntu/suburbs_list.txt"
    output_dir = "/home/ubuntu/Sydney-Automation-Co"
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(suburbs_file, 'r') as f:
        suburbs_raw = f.read().strip()
    suburbs = [s.strip() for s in suburbs_raw.split(',') if s.strip()]

    # Dynalite-specific template for suburb pages
    template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynalite Repair {SUBURB_NAME} | Philips Dynalite Fault Finding Sydney</title>
    <meta name="description" content="Expert Philips Dynalite repair, programming & fault finding in {SUBURB_NAME}, Sydney. Same-day emergency Dynalite services. Book your service call today.">
    <link rel="canonical" href="https://sydneyautomationco.com.au/{SUBURB_SLUG}-dynalite-repair-sydney">
    <link rel="stylesheet" href="/style.css"> <!-- Assuming a global style.css -->
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #0a1628; color: #a8c0e0; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background-color: #001f3d; color: #fff; padding: 1rem 0; text-align: center; }
        header h1 { margin: 0; font-size: 2.5em; }
        .hero { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('/images/hero-bg.jpg') no-repeat center center/cover; color: #fff; padding: 100px 0; text-align: center; }
        .hero h2 { font-size: 3em; margin-bottom: 20px; }
        .hero p { font-size: 1.2em; margin-bottom: 30px; }
        .cta-button { background-color: #f07020; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }
        .section { padding: 60px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .section h3 { color: #fff; font-size: 2em; margin-bottom: 20px; }
        .faq-item { background-color: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 20px; margin-bottom: 15px; border-radius: 8px; }
        .faq-item h4 { color: #fff; margin-top: 0; }
        footer { background-color: #001f3d; color: #a8c0e0; text-align: center; padding: 20px 0; margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Sydney Automation Co.</h1>
            <p>Expert Lighting Control & Automation Services in Sydney</p>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container">
                <h2>Emergency Philips Dynalite Repair in {SUBURB_NAME}</h2>
                <p>Dynalite system crashed? Keypads unresponsive? Lights flickering? We diagnose and fix complex Philips Dynalite faults that others can't — same day, across {SUBURB_NAME} and Greater Sydney.</p>
                <a href="/book-service" class="cta-button">Book Your Same-Day Dynalite Service Call →</a>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>Our Philips Dynalite Services in {SUBURB_NAME}</h3>
                <p>Sydney Automation Co. provides rapid response and expert fault finding for all Philips Dynalite lighting control systems in {SUBURB_NAME}. Whether you're dealing with a Dynalite processor failure, network communication issues, or keypad malfunctions, our certified technicians are ready to assist.</p>
                <ul>
                    <li>Philips Dynalite System Repair & Programming</li>
                    <li>Dynalite Fault Finding & Diagnostics (DyNet, Envision)</li>
                    <li>Dynalite Keypad & Sensor Troubleshooting</li>
                    <li>Same-Day Emergency Service for Dynalite Systems</li>
                    <li>Commercial & Residential Dynalite Automation Support</li>
                </ul>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h3>Common Dynalite Questions in {SUBURB_NAME}</h3>
                <div class="faq-item">
                    <h4>My Dynalite keypad in {SUBURB_NAME} is unresponsive. What's the issue?</h4>
                    <p>Unresponsive Dynalite keypads often indicate a network communication problem, a faulty keypad unit, or a processor issue. Our {SUBURB_NAME} Dynalite specialists can quickly diagnose the root cause and restore control to your system.</p>
                </div>
                <div class="faq-item">
                    <h4>My Philips Dynalite lights in {SUBURB_NAME} are flickering. Can you help?</h4>
                    <p>Flickering Dynalite lights can be caused by faulty dimmer modules, network instability, or incorrect programming. Our expert technicians in {SUBURB_NAME} are equipped to identify and rectify these issues, ensuring stable and reliable lighting.</p>
                </div>
                <div class="faq-item">
                    <h4>Do you offer emergency Dynalite repair in {SUBURB_NAME}?</h4>
                    <p>Yes, we provide urgent emergency repair services for Philips Dynalite systems across {SUBURB_NAME} and Greater Sydney. Critical system failures require immediate attention to maintain functionality and safety. Call us for rapid assistance.</p>
                </div>
            </div>
        </section>

        <section class="section" style="text-align: center;">
            <div class="container">
                <h3>Ready for a Dynalite Solution in {SUBURB_NAME}?</h3>
                <p>Don't let Dynalite problems disrupt your home or business. Get expert help now.</p>
                <a href="/book-service" class="cta-button">Secure Your Dynalite Service Call with a Deposit →</a>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; {CURRENT_YEAR} Sydney Automation Co. All rights reserved. Serving {SUBURB_NAME} and Greater Sydney.</p>
        </div>
    </footer>
</body>
</html>
"""

    current_year = datetime.now().year

    for suburb in suburbs:
        suburb_name = suburb.strip()
        if not suburb_name: # Skip empty strings
            continue
        
        suburb_slug = suburb_name.lower().replace(' ', '-')
        
        # Populate template
        page_content = template.replace("{SUBURB_NAME}", suburb_name)
        page_content = page_content.replace("{SUBURB_SLUG}", suburb_slug)
        page_content = page_content.replace("{CURRENT_YEAR}", str(current_year))

        # Write to file
        output_filename = os.path.join(output_dir, f"{suburb_slug}-dynalite-repair-sydney.html")
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generated: {output_filename}")

if __name__ == "__main__":
    from datetime import datetime # Import datetime here for the script to run standalone
    generate_dynalite_suburb_pages()
