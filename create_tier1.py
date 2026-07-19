import os
import re

new_pages = {
    "cbus-programming-chatswood.html": {
        "title": "C-Bus Programming Chatswood | Commercial & Residential Automation",
        "h1": "C-Bus Programming <span class='accent'>Chatswood</span>",
        "lead": "Expert lighting control systems integration for Chatswood's commercial towers and residential complexes. Certified C-Bus, Dynalite, and DALI specialists.",
        "framework": """
      <h3>Local Geography & Commercial Hub</h3>
      <p>Serving the North Shore's premier commercial and retail district, we provide advanced automation programming for towers along the Pacific Highway and high-density residential properties in Chatswood.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Chatswood features a dense mix of modern commercial high-rises and premium apartments. We specialize in diagnosing, upgrading, and programming industry-standard systems including <strong>C-Bus, Signify Dynalite, and DALI</strong>. Common issues we resolve include network communication failures in multi-story buildings and complex scene programming for corporate offices.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Can you integrate DALI and C-Bus in commercial towers?</h4>
        <p>Yes, we are highly experienced in DALI to C-Bus gateways, ensuring seamless control over vast commercial floorplates and precise energy management.</p>
        <h4>Do you service Chatswood retail spaces?</h4>
        <p>Absolutely. We provide rapid-response repairs and programming adjustments for retail lighting schedules in and around the Chatswood CBD.</p>
      </div>

      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        <li><a href="/smart-home-automation-neutral-bay" style="color:#f07020;text-decoration:underline;">Automation Neutral Bay</a></li>
        <li><a href="/cbus-repair-killara" style="color:#f07020;text-decoration:underline;">C-Bus Repair Killara</a></li>
      </ul>
"""
    },
    "lighting-control-rose-bay.html": {
        "title": "Lighting Control Rose Bay | Premium Smart Home Automation",
        "h1": "Lighting Control <span class='accent'>Rose Bay</span>",
        "lead": "Specialist Dynalite and C-Bus programming for ultra-prestige harbourside residences in Rose Bay and the Eastern Suburbs.",
        "framework": """
      <h3>Local Geography & Premium Residences</h3>
      <p>Servicing the Eastern Suburbs' elite waterfront properties, we offer discreet, high-end smart home automation support across Rose Bay, from New South Head Road to the quiet harbourside enclaves.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Rose Bay's architectural landscape includes ultra-modern new builds and grand heritage estates. We specialize in maintaining and upgrading complex lighting networks, primarily <strong>Signify Dynalite and C-Bus</strong>. We resolve issues such as unresponsive touchscreens, faulty dimming channels, and integration failures with AV systems.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Can you upgrade older C-Bus systems in heritage homes?</h4>
        <p>Yes. We routinely upgrade legacy C-Bus networks to modern standards without requiring complete rewiring, preserving the integrity of heritage properties while delivering modern smart control.</p>
        <h4>Do you offer preventative maintenance?</h4>
        <p>We provide ongoing maintenance agreements for large estates to ensure lighting, shading, and automation systems run flawlessly year-round.</p>
      </div>

      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        <li><a href="/smart-home-installation-bellevue-hill" style="color:#f07020;text-decoration:underline;">Automation Bellevue Hill</a></li>
        <li><a href="/c-bus-programmer-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Eastern Suburbs Hub</a></li>
      </ul>
"""
    },
    "smart-home-installation-bellevue-hill.html": {
        "title": "Smart Home Installation Bellevue Hill | Elite Automation Integration",
        "h1": "Smart Home Automation <span class='accent'>Bellevue Hill</span>",
        "lead": "Delivering flawless C-Bus and Dynalite systems integration for high-value residential properties in Bellevue Hill.",
        "framework": """
      <h3>Local Geography & Elite Estates</h3>
      <p>Providing top-tier automation support for Bellevue Hill's expansive estates and architectural masterpieces, ensuring lighting and smart systems operate to the highest standards.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Bellevue Hill properties often feature extensive, multi-level automation networks. We are experts in <strong>C-Bus and Signify Dynalite</strong> programming, addressing complex faults like network overloads, touchscreen failures, and synchronization issues across large footprints.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Can you integrate existing lighting with new AV systems?</h4>
        <p>Yes, we specialize in bridging C-Bus and Dynalite networks with high-end AV processors (like Control4 or Crestron) for unified smart home control.</p>
      </div>

      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        <li><a href="/lighting-control-rose-bay" style="color:#f07020;text-decoration:underline;">Lighting Control Rose Bay</a></li>
        <li><a href="/c-bus-programmer-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Eastern Suburbs Hub</a></li>
      </ul>
"""
    },
    "c-bus-programmer-caringbah.html": {
        "title": "C-Bus Programmer Caringbah | Commercial & Residential Repairs",
        "h1": "C-Bus Programmer <span class='accent'>Caringbah</span>",
        "lead": "The Sutherland Shire's local C-Bus and Dynalite experts, providing rapid fault finding for Caringbah's commercial zones and residential areas.",
        "framework": """
      <h3>Local Geography & Commercial Hub</h3>
      <p>Centrally located to service Caringbah's bustling commercial and industrial sectors along Captain Cook Drive, as well as the surrounding residential neighborhoods.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Caringbah features a diverse mix of commercial showrooms, warehouses, and modern homes. We handle everything from <strong>DALI and Dynalite</strong> high-bay lighting control in commercial spaces to <strong>C-Bus</strong> repairs in residential properties. Common faults include sensor failures and relay module burnouts.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Do you service commercial properties in Caringbah?</h4>
        <p>Yes, we provide specialized diagnostic and repair services for commercial showrooms, offices, and warehouses utilizing automated lighting.</p>
      </div>

      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        <li><a href="/c-bus-programmer-engadine" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Engadine</a></li>
        <li><a href="/shire" style="color:#f07020;text-decoration:underline;">Sutherland Shire Hub</a></li>
      </ul>
"""
    },
    "c-bus-programmer-engadine.html": {
        "title": "C-Bus Programmer Engadine | Local Shire Automation Expert",
        "h1": "C-Bus Programmer <span class='accent'>Engadine</span>",
        "lead": "Expert local C-Bus and Dynalite repairs for established residential properties in Engadine and the southern Sutherland Shire.",
        "framework": """
      <h3>Local Geography & Community</h3>
      <p>Providing dedicated, fast-response smart home automation repairs and programming for the Engadine community and surrounding southern Shire suburbs.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Engadine contains many established homes that adopted early-generation smart lighting. We specialize in repairing, maintaining, and upgrading these legacy <strong>C-Bus systems</strong>, resolving issues like flickering lights, stuck relays, and failing wall switches without the need for full rewiring.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Can you fix older C-Bus switches that have stopped working?</h4>
        <p>Yes, we carry a wide range of replacement parts and can either repair legacy C-Bus components or program modern replacements to seamlessly join your existing network.</p>
      </div>

      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        <li><a href="/c-bus-programmer-caringbah" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Caringbah</a></li>
        <li><a href="/shire" style="color:#f07020;text-decoration:underline;">Sutherland Shire Hub</a></li>
      </ul>
"""
    }
}

try:
    with open("c-bus-programmer-sydney.html", "r", encoding="utf-8") as f:
        template = f.read()
except UnicodeDecodeError:
    with open("c-bus-programmer-sydney.html", "r", encoding="cp1252") as f:
        template = f.read()

for filename, data in new_pages.items():
    # Replace title
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', template)
    # Replace Canonical URL
    content = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{filename.replace(".html", "")}"/>', content)
    
    # Replace H1
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', content)
    # Replace Lead Paragraph
    content = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{data["lead"]}</p>', content)

    # Inject framework replacing the "Why Choose" section
    match = re.search(r'(<h2>Why Choose a Specialist C-Bus Programmer\?</h2>.*?</div>)', content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + '<div class="content-block">\n' + data['framework'] + '</div>' + content[match.end():]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Created {filename}")
