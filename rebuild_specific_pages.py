import os
import re

# We will use index.html as a shell to generate full service pages
with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

match = re.search(r'<nav>.*?</nav>', html, flags=re.DOTALL)
header_end = re.search(r'</nav>', html, flags=re.DOTALL).end()
footer_start = re.search(r'<footer.*?>', html, flags=re.DOTALL).start()

shell_head = html[:header_end]
shell_foot = html[footer_start:]

# 1. cbus-fault-finding-sydney.html
page1_head = re.sub(r'<title>.*?</title>', '<title>C-Bus Fault Finding Sydney | Network Analysis & Repairs</title>', shell_head)
page1_head = re.sub(r'<meta content="[^"]+" name="description" />', '<meta content="Expert C-Bus fault finding in Sydney. We use C-Bus Toolkit and Network Analysers to diagnose burden issues, clock collisions, and voltage drops instantly." name="description" />', page1_head)

page1_content = """
<div class="page">
    <div class="hero">
        <div class="container-sm">
            <span class="tag">EMERGENCY FAULT FINDING</span>
            <h1>C-Bus Fault Finding <span>Sydney</span></h1>
            <p class="lead">Is your C-Bus system unresponsive, flickering, or randomly turning lights on and off? We deploy advanced C-Bus Network Analysers to diagnose and repair your system on the spot.</p>
            <div class="btns">
                <a href="tel:0422469739" class="btn btn-primary">📞 Call for Immediate Support</a>
                <a href="/cbus-fault-finder" class="btn btn-outline">Interactive Fault Finder →</a>
            </div>
        </div>
    </div>
    
    <div class="section">
        <div class="container">
            <div class="section-header">
                <h2>Why is your C-Bus System Failing?</h2>
                <p class="lead">C-Bus relies on a delicate balance of voltage, network clocks, and burdens. When one fails, the whole system can crash.</p>
            </div>
            
            <div class="grid-3">
                <div class="card">
                    <div class="icon-box">⚡</div>
                    <h3>Network Voltage Drop</h3>
                    <p class="dim">If a C-Bus Power Supply (e.g., 5500PS) fails, network voltage drops below 15V. Units lose communication, and button LEDs may flash or completely die.</p>
                </div>
                <div class="card">
                    <div class="icon-box">⏱️</div>
                    <h3>Clock Collisions</h3>
                    <p class="dim">Every C-Bus network requires exactly one System Clock enabled. If multiple clocks are running (or none at all), commands collide and lights become unresponsive.</p>
                </div>
                <div class="card">
                    <div class="icon-box">🔌</div>
                    <h3>Burden Issues</h3>
                    <p class="dim">A hardware burden is required to dampen communication signals. Missing or double-burdened networks experience severe communication lag and missed commands.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="section" style="background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
        <div class="container">
            <div class="grid-2" style="align-items: center;">
                <div>
                    <h2>Our Diagnostic Process</h2>
                    <p class="dim" style="font-size: 16px; margin-bottom: 24px; max-width: 500px;">We don't guess. We use the <strong>C-Bus Toolkit</strong> and dedicated diagnostic hardware to monitor network traffic in real-time. This allows us to instantly identify failing relays, corrupted PCI interfaces, and wiring faults without tearing your walls apart.</p>
                    <ul class="check-list">
                        <li>Real-time C-Bus Traffic Analysis</li>
                        <li>Power Supply Voltage Testing</li>
                        <li>Clock & Burden Verification</li>
                        <li>Unit Firmware Flashing</li>
                    </ul>
                </div>
                <div style="background: #0e1f3d; padding: 40px; border-radius: 16px; border: 1px solid #2a4a80;">
                    <h3 style="margin-bottom: 16px; color: #f07020;">Need a Fast Fix?</h3>
                    <p style="color: #a8c0e0; margin-bottom: 24px;">Our service vehicles carry stock of all common C-Bus modules including 5504RVF relays, 5504D2A dimmers, and PCIs to ensure same-day resolution.</p>
                    <a href="tel:0422469739" class="btn btn-primary" style="width: 100%; justify-content: center;">Call George: 0422 469 739</a>
                </div>
            </div>
        </div>
    </div>
</div>
"""
with open('cbus-fault-finding-sydney.html', 'w', encoding='utf-8') as f:
    f.write(page1_head + page1_content + shell_foot)


# 2. dynalite-fault-finding-sydney-common-faults.html
page2_head = re.sub(r'<title>.*?</title>', '<title>Signify Dynalite Fault Finding Sydney | Expert Diagnostics</title>', shell_head)
page2_head = re.sub(r'<meta content="[^"]+" name="description" />', '<meta content="Expert Signify Dynalite fault finding in Sydney. We diagnose Dynet RS485 communication failures, corrupted controller firmware, and unresponsive panels." name="description" />', page2_head)

page2_content = """
<div class="page">
    <div class="hero">
        <div class="container-sm">
            <span class="tag">EXPERT DIAGNOSTICS</span>
            <h1>Signify Dynalite <span>Fault Finding</span></h1>
            <p class="lead">From commercial tower RS485 communication failures to corrupted residential controller configurations. We provide expert EnvisionProject diagnostics across Sydney.</p>
            <div class="btns">
                <a href="tel:0422469739" class="btn btn-primary">📞 Request Diagnostic Callout</a>
            </div>
        </div>
    </div>
    
    <div class="section">
        <div class="container">
            <div class="section-header">
                <h2>The 3 Most Common Dynalite Failures</h2>
                <p class="lead">Signify Dynalite is incredibly robust, but incorrect programming or hardware aging can bring a network down. Here is what we look for.</p>
            </div>
            
            <div class="grid-3">
                <div class="card">
                    <div class="icon-box">🔗</div>
                    <h3>DyNet RS485 Cable Faults</h3>
                    <p class="dim">Dynalite uses an RS485 daisy-chain network. A single shorted cable, reversed D+/D- wire, or faulty network bridge can isolate an entire floor of lighting controllers.</p>
                </div>
                <div class="card">
                    <div class="icon-box">🧠</div>
                    <h3>Corrupted Logic / Envision</h3>
                    <p class="dim">Power surges can corrupt the internal memory of leading-edge dimmers (like the DDLE801). We extract the existing programming via EnvisionProject and re-flash the hardware.</p>
                </div>
                <div class="card">
                    <div class="icon-box">🎛️</div>
                    <h3>Unresponsive Antumbra Panels</h3>
                    <p class="dim">When Antumbra keypads stop responding, it's often a firmware mismatch or a failure in the underlying DACM module. We can re-assign the network IDs and restore operation.</p>
                </div>
            </div>
        </div>
    </div>
    
    <div class="cta-band container">
        <h2 style="font-size: 32px; margin-bottom: 16px;">Don't let amateur electricians guess with your Dynalite.</h2>
        <p style="color: #a8c0e0; font-size: 18px; margin-bottom: 32px;">Dynalite requires proprietary software and specialized training. We are Signify accredited system designers.</p>
        <a href="tel:0422469739" class="btn btn-primary">Book a System Audit Now</a>
    </div>
</div>
"""
with open('dynalite-fault-finding-sydney-common-faults.html', 'w', encoding='utf-8') as f:
    f.write(page2_head + page2_content + shell_foot)


# 3. cbus-dynalite-upgrade-guide.html (Populating the empty shell)
page3_head = re.sub(r'<title>.*?</title>', '<title>C-Bus & Dynalite System Upgrade Guide | Sydney</title>', shell_head)
page3_head = re.sub(r'<meta content="[^"]+" name="description" />', '<meta content="A complete guide to upgrading obsolete Clipsal C-Bus and Signify Dynalite lighting control systems to modern hardware and smart device integration." name="description" />', page3_head)

page3_content = """
<div class="page">
    <div class="hero">
        <div class="container-sm">
            <span class="tag">SYSTEM UPGRADES</span>
            <h1>Legacy System <span>Upgrade Guide</span></h1>
            <p class="lead">Is your C-Bus or Dynalite system over 15 years old? Learn how we migrate obsolete, failing hardware to modern SpaceLogic modules and smart phone control without rewiring your home or building.</p>
            <div class="btns">
                <a href="tel:0422469739" class="btn btn-primary">📞 Call to Discuss an Upgrade</a>
            </div>
        </div>
    </div>
    
    <div class="section">
        <div class="container">
            <div class="grid-2">
                <div>
                    <h2 style="margin-bottom: 24px;">The 3 Phases of a Seamless Upgrade</h2>
                    
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 24px; margin-bottom: 16px;">
                        <h4 style="color: #f07020;">1. Database Extraction & Audit</h4>
                        <p class="dim" style="font-size: 15px;">Before touching any hardware, we connect to your existing network and extract the legacy programming database. This ensures we don't lose any of your custom lighting scenes, schedules, or logic.</p>
                    </div>
                    
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 24px; margin-bottom: 16px;">
                        <h4 style="color: #f07020;">2. Hardware Swap-Out</h4>
                        <p class="dim" style="font-size: 15px;">We systematically remove the failing components (e.g., old pink/blue C-Bus relays) and install modern, energy-efficient equivalents like the new SpaceLogic C-Bus modules or current-generation Dynalite controllers.</p>
                    </div>
                    
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 24px;">
                        <h4 style="color: #f07020;">3. Network Expansion (Wiser / Apple HomeKit)</h4>
                        <p class="dim" style="font-size: 15px;">Once the backbone is stable, we integrate modern gateways. This bridges your hardwired lighting system to your WiFi, allowing full control via Apple Home, Google Assistant, or dedicated automation apps.</p>
                    </div>
                </div>
                
                <div>
                    <div class="stat-box" style="margin-bottom: 24px;">
                        <div class="stat-num">0%</div>
                        <div class="stat-label">Need for Wall Rewiring</div>
                        <p class="dim" style="margin-top: 12px; font-size: 14px;">Because your home is already wired for a proprietary automation bus, we simply utilize the existing Cat5 cable architecture.</p>
                    </div>
                    
                    <div style="background: linear-gradient(135deg, rgba(240,112,32,0.1), rgba(14,31,61,0.8)); border: 1px solid rgba(240,112,32,0.3); border-radius: 16px; padding: 32px; text-align: center;">
                        <h3 style="margin-bottom: 12px;">Get a Firmware & Hardware Assessment</h3>
                        <p class="dim" style="margin-bottom: 24px;">We can evaluate your site to determine if you need a full hardware swap or just a firmware update.</p>
                        <a href="tel:0422469739" class="btn btn-primary" style="width: 100%; justify-content: center;">Call George: 0422 469 739</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""
with open('cbus-dynalite-upgrade-guide.html', 'w', encoding='utf-8') as f:
    f.write(page3_head + page3_content + shell_foot)

print("Generated full service pages for cbus-fault-finding, dynalite-fault-finding, and the upgrade guide.")
