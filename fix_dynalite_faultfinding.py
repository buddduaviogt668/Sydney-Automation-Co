import re

with open('dynalite-fault-finding-sydney-common-faults.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_body = '''<body>
<div id="top-bar" style="position:fixed;top:0;left:0;right:0;z-index:1100;background:#f07020;color:#fff;font-size:13px;font-weight:700;text-align:center;padding:10px 16px;letter-spacing:0.5px">
  ⚡ SYSTEM DOWN? SAME-DAY RESPONSE — <a href="tel:0422469739" style="color:#fff;text-decoration:underline">CALL 0422 469 739 NOW</a>
</div>
<nav>
  <a class="logo" href="/"><span class="logo-main">SYDNEY AUTOMATION CO.</span><span class="logo-line"></span><span class="logo-sub">LIGHTING CONTROL SPECIALISTS</span></a>
  <div class="nav-links">
    <div class="nav-dd" id="dd-services">
      <button class="nav-dd-trigger">Services</button>
      <div class="nav-dd-panel wide">
        <div class="dd-label">C-Bus</div>
        <a href="/c-bus-programmer-sydney">C-Bus Programming</a>
        <a href="/c-bus-repairs-sydney">C-Bus Repairs</a>
        <a href="/cbus-upgrade-sydney">C-Bus Upgrades</a>
        <a href="/cbus-fault-finding-sydney">C-Bus Fault Finding</a>
        <a href="/cbus-specialist-sydney">C-Bus Specialist</a>
        <a href="/c-bus-apple-homekit-sydney">C-Bus &amp; Apple HomeKit</a>
        <div class="dd-divider"></div>
        <div class="dd-label">Dynalite</div>
        <a href="/dynalite-programmer-sydney">Dynalite Programming</a>
        <a href="/dynalite-repair-sydney">Dynalite Repairs</a>
        <a href="/dynalite-fault-finding-sydney-common-faults" class="active">Dynalite Fault Finding</a>
        <div class="dd-divider"></div>
        <div class="dd-label">Lighting Control</div>
        <a href="/lighting-control-service-sydney">Lighting Control Service</a>
        <a href="/lighting-control-repair-sydney">Lighting Control Repair</a>
        <a href="/led-upgrade-carpark-lighting-sydney">LED Upgrades &amp; Car Parks</a>
        <a href="/carpark-lighting-upgrades-sydney">Car Park Upgrades</a>
        <a href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>
        <div class="dd-divider"></div>
        <div class="dd-label">Emergency &amp; Compliance</div>
        <a href="/emergency-lighting-compliance-afss-sydney">Emergency Lighting AFSS</a>
        <a href="/rapix-emergency-lighting-sydney">RAPIX Emergency Lighting</a>
        <a href="/emergency-lighting-hotels-hospitality-sydney">Hotels &amp; Hospitality</a>
        <a href="/emergency-lighting-train-stations-infrastructure-sydney">Train Stations &amp; Infrastructure</a>
        <a href="/emergency-repair-sydney">Emergency Repair</a>
        <div class="dd-divider"></div>
        <div class="dd-label">DALI &amp; RAPIX</div>
        <a href="/dali-lighting-repair">DALI Lighting Repair</a>
        <a href="/dali2-compliance-nsw-commercial">DALI-2 Compliance NSW</a>
        <a href="/rapix-lighting-control">RAPIX Lighting Control</a>
        <a href="/what-is-rapix-sydney-buildings">What is RAPIX?</a>
        <div class="dd-divider"></div>
        <div class="dd-label">Maintenance &amp; Contracts</div>
        <a href="/lighting-control-maintenance-sydney">Lighting Control Maintenance</a>
        <a href="/cbus-maintenance-sydney">C-Bus Maintenance</a>
        <a href="/dynalite-maintenance-sydney">Dynalite Maintenance</a>
        <a href="/lighting-control-service-contract-sydney">Service Contracts</a>
        <a href="/building-automation-maintenance-sydney">Building Automation</a>
        <a href="/facilities-lighting-maintenance-sydney">Facilities Maintenance</a>
        <div class="dd-divider"></div>
        <a href="/services">All Services →</a>
      </div>
    </div>
    <div class="nav-dd" id="dd-areas">
      <button class="nav-dd-trigger">Areas</button>
      <div class="nav-dd-panel">
        <div class="dd-label">Sydney Regions</div>
        <a href="/c-bus-programmer-sutherland-shire">Sutherland Shire</a>
        <a href="/c-bus-programmer-north-shore">North Shore</a>
        <a href="/c-bus-programmer-eastern-suburbs">Eastern Suburbs</a>
        <a href="/c-bus-programmer-inner-west">Inner West</a>
        <a href="/c-bus-programmer-northern-beaches">Northern Beaches</a>
        <a href="/c-bus-programmer-hills-district">Hills District</a>
        <a href="/c-bus-programmer-parramatta">Parramatta</a>
        <a href="/c-bus-programmer-st-george">St George</a>
        <a href="/c-bus-programmer-sydney-cbd">Sydney CBD</a>
        <div class="dd-divider"></div>
        <a href="/shire">Sutherland Shire Hub</a>
        <a href="/locations">All Service Areas →</a>
      </div>
    </div>
    <div class="nav-dd" id="dd-clients">
      <button class="nav-dd-trigger">Clients</button>
      <div class="nav-dd-panel">
        <a href="/strata-managers-lighting-control-sydney">Strata Managers</a>
        <a href="/building-manager-lighting-support-sydney">Building Managers</a>
        <a href="/facility-managers-cbus-dynalite-dali-guide">Facility Managers</a>
        <a href="/electricians">Electricians</a>
        <a href="/sydney-electricians-cbus-dynalite-partnership">Electrician Partnership</a>
        <a href="/real-estate-cbus-audit-sydney">Real Estate Agents</a>
        <a href="/strata-lighting-compliance-sydney">Strata Compliance</a>
        <a href="/strata">Strata &amp; FM Hub</a>
      </div>
    </div>
    <div class="nav-dd" id="dd-resources">
      <button class="nav-dd-trigger">Resources</button>
      <div class="nav-dd-panel">
        <div class="dd-label">Guides &amp; Blog</div>
        <a href="/blog">Blog</a>
        <a href="/guides">Guides</a>
        <a href="/cbus-vs-dynalite">C-Bus vs Dynalite</a>
        <a href="/dynalite-vs-cbus-sydney">Dynalite vs C-Bus</a>
        <a href="/how-to-choose-cbus-specialist-sydney">How to Choose a C-Bus Specialist</a>
        <a href="/cbus-dynalite-upgrade-guide">C-Bus &amp; Dynalite Upgrade Guide</a>
        <a href="/blog-dali-2-compliance-guide-sydney-building-managers">DALI-2 Compliance Guide</a>
        <a href="/blog-strata-lighting-energy-savings-sydney">Strata Energy Savings</a>
        <div class="dd-divider"></div>
        <div class="dd-label">Company</div>
        <a href="/projects">Projects</a>
        <a href="/about">About</a>
        <a href="/4-years-building-facilities-management-jll-pbmg">George's Background</a>
      </div>
    </div>
    <a href="/contact">Contact</a>
    <a href="tel:0422469739" class="nav-cta">📞 Call Now</a>
  </div>
  <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>
<div class="mob-nav" id="mob-nav">
  <div class="mob-section"><div class="mob-section-title">C-Bus Services</div>
    <a href="/c-bus-programmer-sydney">C-Bus Programming</a>
    <a href="/c-bus-repairs-sydney">C-Bus Repairs</a>
    <a href="/cbus-upgrade-sydney">C-Bus Upgrades</a>
    <a href="/cbus-fault-finding-sydney">C-Bus Fault Finding</a>
    <a href="/cbus-specialist-sydney">C-Bus Specialist</a>
    <a href="/c-bus-apple-homekit-sydney">C-Bus &amp; Apple HomeKit</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Dynalite Services</div>
    <a href="/dynalite-programmer-sydney">Dynalite Programming</a>
    <a href="/dynalite-repair-sydney">Dynalite Repairs</a>
    <a href="/dynalite-fault-finding-sydney-common-faults">Dynalite Fault Finding</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Lighting Control</div>
    <a href="/lighting-control-service-sydney">Lighting Control Service</a>
    <a href="/lighting-control-repair-sydney">Lighting Control Repair</a>
    <a href="/led-upgrade-carpark-lighting-sydney">LED Upgrades</a>
    <a href="/carpark-lighting-upgrades-sydney">Car Park Upgrades</a>
    <a href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Emergency &amp; Compliance</div>
    <a href="/emergency-lighting-compliance-afss-sydney">Emergency Lighting AFSS</a>
    <a href="/rapix-emergency-lighting-sydney">RAPIX Emergency Lighting</a>
    <a href="/emergency-lighting-hotels-hospitality-sydney">Hotels &amp; Hospitality</a>
    <a href="/emergency-lighting-train-stations-infrastructure-sydney">Train Stations &amp; Infrastructure</a>
    <a href="/emergency-repair-sydney">Emergency Repair</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">DALI &amp; RAPIX</div>
    <a href="/dali-lighting-repair">DALI Lighting Repair</a>
    <a href="/dali2-compliance-nsw-commercial">DALI-2 Compliance NSW</a>
    <a href="/rapix-lighting-control">RAPIX Lighting Control</a>
    <a href="/what-is-rapix-sydney-buildings">What is RAPIX?</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Maintenance &amp; Contracts</div>
    <a href="/lighting-control-maintenance-sydney">Lighting Control Maintenance</a>
    <a href="/cbus-maintenance-sydney">C-Bus Maintenance</a>
    <a href="/dynalite-maintenance-sydney">Dynalite Maintenance</a>
    <a href="/lighting-control-service-contract-sydney">Service Contracts</a>
    <a href="/building-automation-maintenance-sydney">Building Automation</a>
    <a href="/facilities-lighting-maintenance-sydney">Facilities Maintenance</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Service Areas</div>
    <a href="/c-bus-programmer-sutherland-shire">Sutherland Shire</a>
    <a href="/c-bus-programmer-north-shore">North Shore</a>
    <a href="/c-bus-programmer-eastern-suburbs">Eastern Suburbs</a>
    <a href="/c-bus-programmer-northern-beaches">Northern Beaches</a>
    <a href="/c-bus-programmer-sydney-cbd">Sydney CBD</a>
    <a href="/locations">All Service Areas</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Clients</div>
    <a href="/strata-managers-lighting-control-sydney">Strata Managers</a>
    <a href="/building-manager-lighting-support-sydney">Building Managers</a>
    <a href="/facility-managers-cbus-dynalite-dali-guide">Facility Managers</a>
    <a href="/electricians">Electricians</a>
  </div>
  <div class="mob-section"><div class="mob-section-title">Resources</div>
    <a href="/blog">Blog</a>
    <a href="/guides">Guides</a>
    <a href="/projects">Projects</a>
    <a href="/about">About</a>
  </div>
  <a href="tel:0422469739" class="mob-cta">📞 Call Now — 0422 469 739</a>
</div>

<div class="page">

  <!-- HERO -->
  <div class="hero">
    <div class="container-sm">
      <div class="tag">⚡ Dynalite Fault Finding</div>
      <h1>The 5 Most Common <span class="accent">Dynalite Faults</span> We See On Sydney Sites</h1>
      <p class="lead">Dynalite is the dominant lighting control platform in Sydney's commercial buildings, hotels and prestige residential properties — and remarkably reliable. But when it fails, you need a specialist who knows exactly where to look.</p>
      <div class="btns">
        <a href="tel:0422469739" class="btn btn-primary">📞 Call 0422 469 739</a>
        <a href="/dynalite-repair-sydney" class="btn btn-outline">Dynalite Repairs →</a>
      </div>
    </div>
  </div>

  <!-- INTRO -->
  <div class="section" style="padding-bottom:0">
    <div class="container-sm">
      <p style="font-size:17px;line-height:1.8;color:#a8c0e0">We have commissioned and fault-found Dynalite systems across Sydney's CBD, North Shore, Eastern Suburbs, Sutherland Shire and regional NSW. The same five faults come up again and again — here's what to look for and what's actually causing them.</p>
    </div>
  </div>

  <!-- 5 FAULTS -->
  <div class="section">
    <div class="container-sm">
      <div style="display:flex;flex-direction:column;gap:24px">

        <div class="card">
          <div style="display:flex;align-items:flex-start;gap:20px">
            <div style="min-width:48px;height:48px;border-radius:50%;background:rgba(240,112,32,0.15);border:1px solid rgba(240,112,32,0.4);display:flex;align-items:center;justify-content:center;font-family:\'Barlow Condensed\',sans-serif;font-size:22px;font-weight:900;color:#f07020">1</div>
            <div>
              <h3>DPDBC Controller Communication Loss</h3>
              <p style="color:#a8c0e0;line-height:1.8">The most common Dynalite fault on large commercial sites is a controller dropping off the RS485 network. Symptoms include zones going to default levels, scenes not responding, or the entire network becoming unresponsive. The usual cause is a failed controller, a loose termination on the RS485 bus, or a missing termination resistor at one end of the network. We always check the physical layer before assuming a software fault.</p>
            </div>
          </div>
        </div>

        <div class="card">
          <div style="display:flex;align-items:flex-start;gap:20px">
            <div style="min-width:48px;height:48px;border-radius:50%;background:rgba(240,112,32,0.15);border:1px solid rgba(240,112,32,0.4);display:flex;align-items:center;justify-content:center;font-family:\'Barlow Condensed\',sans-serif;font-size:22px;font-weight:900;color:#f07020">2</div>
            <div>
              <h3>Scene and Preset Corruption</h3>
              <p style="color:#a8c0e0;line-height:1.8">After a power outage or surge, Dynalite controllers can lose their scene programming. This is particularly common in Sydney buildings on older electrical infrastructure — strata buildings in the Eastern Suburbs and inner city are frequent offenders. A full system backup before any major electrical work is essential. If no backup exists, we can often rebuild the programming from scratch using the physical installation as a guide.</p>
            </div>
          </div>
        </div>

        <div class="card">
          <div style="display:flex;align-items:flex-start;gap:20px">
            <div style="min-width:48px;height:48px;border-radius:50%;background:rgba(240,112,32,0.15);border:1px solid rgba(240,112,32,0.4);display:flex;align-items:center;justify-content:center;font-family:\'Barlow Condensed\',sans-serif;font-size:22px;font-weight:900;color:#f07020">3</div>
            <div>
              <h3>DyNet Protocol Address Conflicts</h3>
              <p style="color:#a8c0e0;line-height:1.8">The DyNet protocol is Dynalite's proprietary RS485 network communication standard — elegant but unforgiving of address conflicts. When two devices share the same channel number, one or both behave unpredictably. This is most common after additional Dynalite devices are added to an existing network without checking the existing address map — often following fit-out works or equipment additions. Diagnosing this requires proper Dynalite software tools and experience. It is not something a general electrician can fix.</p>
            </div>
          </div>
        </div>

        <div class="card">
          <div style="display:flex;align-items:flex-start;gap:20px">
            <div style="min-width:48px;height:48px;border-radius:50%;background:rgba(240,112,32,0.15);border:1px solid rgba(240,112,32,0.4);display:flex;align-items:center;justify-content:center;font-family:\'Barlow Condensed\',sans-serif;font-size:22px;font-weight:900;color:#f07020">4</div>
            <div>
              <h3>DALI Integration Failures</h3>
              <p style="color:#a8c0e0;line-height:1.8">Many modern Dynalite installations use DALI drivers for LED dimming. When a DALI driver fails, the controller reports the device missing and scenes break. We carry a DALI analyser to quickly identify failed drivers versus controller faults — a critical distinction that saves significant diagnostic time and avoids unnecessary hardware replacements.</p>
            </div>
          </div>
        </div>

        <div class="card">
          <div style="display:flex;align-items:flex-start;gap:20px">
            <div style="min-width:48px;height:48px;border-radius:50%;background:rgba(240,112,32,0.15);border:1px solid rgba(240,112,32,0.4);display:flex;align-items:center;justify-content:center;font-family:\'Barlow Condensed\',sans-serif;font-size:22px;font-weight:900;color:#f07020">5</div>
            <div>
              <h3>Gateway and Integration Faults (BMS, Crestron, Savant)</h3>
              <p style="color:#a8c0e0;line-height:1.8">Large commercial sites and prestige homes often integrate Dynalite with a BMS or AV control system. When the gateway fails or loses configuration, the whole integration breaks. We have resolved integration faults across major Sydney sites using Dynalite's DyNet gateway tools and third-party integration software.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- WHY SPECIALIST -->
  <div class="section" style="background:#0a1828;border-top:1px solid #2a4a80;border-bottom:1px solid #2a4a80">
    <div class="container">
      <div class="section-header">
        <div class="tag">Why Accreditation Matters</div>
        <h2>Dynalite Requires a <span class="accent">Certified Specialist</span></h2>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="icon-box">🔧</div>
          <h3>Proper Diagnostic Tools</h3>
          <p style="color:#a8c0e0;line-height:1.7">We use Dynalite Envision software, DALI analysers and RS485 network testing equipment — tools a general electrician won't have on their van.</p>
        </div>
        <div class="card">
          <div class="icon-box">📋</div>
          <h3>Philips Dynalite Accredited</h3>
          <p style="color:#a8c0e0;line-height:1.7">As an accredited Philips Dynalite system designer, we can access system backups, Envision databases and technical support unavailable to non-accredited trades.</p>
        </div>
        <div class="card">
          <div class="icon-box">⚡</div>
          <h3>Same-Day Response</h3>
          <p style="color:#a8c0e0;line-height:1.7">Commercial lighting faults cost money. We offer same-day fault finding across the CBD, North Shore, Eastern Suburbs and Sutherland Shire for urgent calls.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- CTA -->
  <div class="section">
    <div class="container-sm" style="text-align:center">
      <div class="tag" style="margin:0 auto 20px">Dynalite Fault Finding Sydney</div>
      <h2>Dynalite System Not Responding?</h2>
      <p style="color:#a8c0e0;font-size:17px;line-height:1.8;margin-bottom:32px">Call us on 0422 469 739 for same-day Dynalite fault finding across Sydney — CBD, Eastern Suburbs, North Shore and Sutherland Shire. We carry common Dynalite hardware for immediate replacement.</p>
      <div class="btns" style="justify-content:center">
        <a href="tel:0422469739" class="btn btn-primary">📞 Call 0422 469 739</a>
        <a href="/contact" class="btn btn-outline">Send an Enquiry</a>
      </div>
    </div>
  </div>

  <!-- RELATED -->
  <div class="section" style="padding-top:0">
    <div class="container-sm">
      <h3 style="margin-bottom:16px;color:#a8c0e0;font-size:14px;font-weight:700;letter-spacing:2px;text-transform:uppercase">Related Pages</h3>
      <div class="grid-2">
        <a href="/dynalite-repair-sydney" class="card" style="display:block">
          <div style="font-weight:700;margin-bottom:6px">Dynalite Repair Sydney →</div>
          <div style="color:#a8c0e0;font-size:14px">Accredited Philips Dynalite repair specialists. Same-day commercial fault finding.</div>
        </a>
        <a href="/dynalite-programmer-sydney" class="card" style="display:block">
          <div style="font-weight:700;margin-bottom:6px">Dynalite Programming Sydney →</div>
          <div style="color:#a8c0e0;font-size:14px">Scene programming, commissioning and system configuration across Greater Sydney.</div>
        </a>
        <a href="/dali-lighting-repair" class="card" style="display:block">
          <div style="font-weight:700;margin-bottom:6px">DALI Lighting Repair →</div>
          <div style="color:#a8c0e0;font-size:14px">DALI driver analysis and repair for integrated Dynalite/DALI systems.</div>
        </a>
        <a href="/dynalite-vs-cbus-sydney" class="card" style="display:block">
          <div style="font-weight:700;margin-bottom:6px">Dynalite vs C-Bus →</div>
          <div style="color:#a8c0e0;font-size:14px">Which lighting control system is right for your building?</div>
        </a>
      </div>
    </div>
  </div>

</div>

<footer>
  <div class="footer-grid">
    <div>
      <div class="logo" style="margin-bottom:16px"><span class="logo-main">SYDNEY AUTOMATION CO.</span><span class="logo-line"></span><span class="logo-sub">LIGHTING CONTROL SPECIALISTS</span></div>
      <p style="color:#6a8cb5;font-size:14px;line-height:1.7">Accredited C-Bus Programmer and Dynalite System Designer. Based in Menai, serving all of Greater Sydney. Same-day fault finding. Fixed-price programming.</p>
    </div>
    <div>
      <div style="font-size:11px;font-weight:700;color:#4a6a9a;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px">Services</div>
      <a href="/cbus-repair-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">C-Bus Repair Sydney</a>
      <a href="/dynalite-repair-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">Dynalite Repair Sydney</a>
      <a href="/emergency-repair-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">🚨 Emergency Repair</a>
      <a href="/c-bus-programmer-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">C-Bus Programming</a>
      <a href="/dynalite-programmer-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">Dynalite Programming</a>
      <a href="/cbus-upgrade-sydney" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">C-Bus Upgrade</a>
      <a href="/services" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">All Services</a>
      <a href="/electricians" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">For Electricians</a>
      <a href="/strata" style="display:block;color:#6a8cb5;font-size:14px">Strata &amp; FM</a>
    </div>
    <div>
      <div style="font-size:11px;font-weight:700;color:#4a6a9a;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px">Contact</div>
      <a href="tel:0422469739" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">📞 0422 469 739</a>
      <a href="mailto:george@sydneyautomationco.com.au" style="display:block;color:#6a8cb5;font-size:14px;margin-bottom:8px">george@sydneyautomationco.com.au</a>
      <p style="color:#6a8cb5;font-size:14px;margin-bottom:8px">Menai, Sutherland Shire NSW 2234</p>
      <p style="color:#6a8cb5;font-size:14px">Mon–Fri 7am–5pm</p>
    </div>
  </div>
  <div class="footer-copy">
    <span>© 2025 Sydney Automation Co. ABN 61 136 364 150. All rights reserved.</span>
    <span style="display:flex;gap:16px"><a href="/privacy-policy" style="color:#6a8cb5">Privacy Policy</a><a href="/sitemap.xml" style="color:#6a8cb5">Sitemap</a></span>
  </div>
</footer>

<!-- Floating CTA -->
<div style="position:fixed;bottom:24px;right:24px;display:flex;flex-direction:column;gap:10px;z-index:500">
  <a href="tel:0422469739" style="display:flex;align-items:center;gap:10px;background:#f07020;color:#fff;padding:12px 18px;border-radius:50px;font-weight:700;font-size:14px;box-shadow:0 4px 20px rgba(240,112,32,0.4)">📞 Call Now</a>
  <a href="https://wa.me/61422469739" style="display:flex;align-items:center;gap:10px;background:#25D366;color:#fff;padding:12px 18px;border-radius:50px;font-weight:700;font-size:14px;box-shadow:0 4px 20px rgba(37,211,102,0.4)">💬 WhatsApp</a>
</div>

<script>
document.querySelectorAll('.nav-dd').forEach(dd=>{
  const trigger=dd.querySelector('.nav-dd-trigger');
  trigger.addEventListener('click',e=>{e.stopPropagation();document.querySelectorAll('.nav-dd').forEach(o=>{if(o!==dd)o.classList.remove('open')});dd.classList.toggle('open')});
});
document.addEventListener('click',()=>document.querySelectorAll('.nav-dd').forEach(dd=>dd.classList.remove('open')));
const ham=document.getElementById('hamburger');
const mob=document.getElementById('mob-nav');
ham.addEventListener('click',()=>{mob.classList.toggle('open');ham.classList.toggle('open')});
</script>
</body>
</html>'''

# Replace everything from <body> to end of file
new_content = re.sub(r'<body>.*$', new_body, content, flags=re.DOTALL)

with open('dynalite-fault-finding-sydney-common-faults.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
