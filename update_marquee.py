import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS to inject into the head or replace in styles
marquee_css = """
    .marquee-item {
      display: inline-flex;
      align-items: center;
      margin: 0 60px;
      color: rgba(255, 255, 255, 0.6);
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      transition: all 0.3s;
      text-decoration: none;
    }

    .marquee-item:hover {
      color: #f07020;
      transform: scale(1.05);
    }

    .marquee-item img {
      height: 32px;
      margin-right: 15px;
      object-fit: contain;
      filter: grayscale(100%) brightness(200%) opacity(70%);
      transition: all 0.3s;
    }

    .marquee-item:hover img {
      filter: grayscale(0%) brightness(100%) opacity(100%);
    }
"""

# Replace old marquee-item CSS
html = re.sub(r'\.marquee-item\s*\{.*?\}(?=\s*\.marquee-item:hover)', '', html, flags=re.DOTALL)
html = re.sub(r'\.marquee-item:hover\s*\{.*?\}', '', html, flags=re.DOTALL)
html = re.sub(r'\.marquee-item\s*i\s*\{.*?\}', '', html, flags=re.DOTALL)

if '@keyframes marqueeRun' in html:
    html = html.replace('@keyframes marqueeRun', marquee_css + '\n    @keyframes marqueeRun')

new_marquee = """
    <!-- INFINITE BRAND MARQUEE -->
    <div class="marquee-wrapper" style="background: rgba(0, 20, 40, 0.6); border-bottom: 1px solid rgba(240,112,32,0.1); backdrop-filter: blur(10px);">
      <div class="marquee-content">
        <!-- Brand Set 1 -->
        <a href="/c-bus-programmer-sydney" class="marquee-item">
          <img src="/clipsal c-bus.png" alt="Clipsal C-Bus Programmer">
          <span>CLIPSAL C-BUS</span>
        </a>
        <a href="/dynalite-programmer-sydney" class="marquee-item">
          <img src="/signdyn-logo.png" alt="Signify Dynalite System Designer">
          <span>SIGNIFY DYNALITE</span>
        </a>
        <a href="/cbus-specialist-sydney" class="marquee-item">
          <img src="/schneider electric.png" alt="Schneider Electric EcoXpert">
          <span>SCHNEIDER ELECTRIC</span>
        </a>
        <a href="/dali2-compliance-nsw-commercial" class="marquee-item">
          <img src="/DALI-AllianceLOGORBLACK-1.png" alt="DALI-2 Compliance NSW">
          <span>DALI ALLIANCE</span>
        </a>
        <a href="/what-is-rapix-sydney-buildings" class="marquee-item">
          <img src="/rapix.png" alt="RAPIX Commercial Lighting Control">
          <span>RAPIX LIGHTING</span>
        </a>
        
        <!-- Duplicated for seamless loop -->
        <a href="/c-bus-programmer-sydney" class="marquee-item">
          <img src="/clipsal c-bus.png" alt="Clipsal C-Bus Programmer">
          <span>CLIPSAL C-BUS</span>
        </a>
        <a href="/dynalite-programmer-sydney" class="marquee-item">
          <img src="/signdyn-logo.png" alt="Signify Dynalite System Designer">
          <span>SIGNIFY DYNALITE</span>
        </a>
        <a href="/cbus-specialist-sydney" class="marquee-item">
          <img src="/schneider electric.png" alt="Schneider Electric EcoXpert">
          <span>SCHNEIDER ELECTRIC</span>
        </a>
        <a href="/dali2-compliance-nsw-commercial" class="marquee-item">
          <img src="/DALI-AllianceLOGORBLACK-1.png" alt="DALI-2 Compliance NSW">
          <span>DALI ALLIANCE</span>
        </a>
        <a href="/what-is-rapix-sydney-buildings" class="marquee-item">
          <img src="/rapix.png" alt="RAPIX Commercial Lighting Control">
          <span>RAPIX LIGHTING</span>
        </a>
      </div>
    </div>
"""

html = re.sub(r'<!-- INFINITE BRAND MARQUEE -->.*?</div>\s*</div>', new_marquee.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated marquee with images and links!")
