import os

DIR = r"c:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"

blogs = [
    {
        "slug": "blog-blinking-leds-lighting-network",
        "title": "The Hidden Cost of Ignoring Blinking LEDs on Your Lighting Control Network",
        "desc": "A blinking LED on a C-Bus or Dynalite module isn't just an annoyance—it's a warning. Learn why ignoring network clock issues leads to hardware failure.",
        "category": "Troubleshooting",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80",
        "body": """<h2>The Warning Sign You Shouldn't Ignore</h2>
<p>If you manage a commercial building or a high-end smart home, you might have noticed a red blinking LED on your electrical switchboard. Many electricians assume it's normal network traffic. It's not.</p>
<p>A blinking LED on a Clipsal C-Bus or Philips Dynalite system indicates a dropped network clock or a failing power supply. This means the communication data packets are colliding, and the system is straining to keep the lights on.</p>
<h3>What Causes the Blinking LED?</h3>
<ol>
<li><strong>Failed Network Clock Driver:</strong> The software module responsible for syncing data has crashed.</li>
<li><strong>Voltage Drop:</strong> The 36V DC bus voltage has dropped below 22V, causing transceivers to brown-out.</li>
<li><strong>Burden Failure:</strong> The network termination resistor has blown.</li>
</ol>
<p>If ignored, the constant data collisions will overheat the microprocessors on your relays and dimmers, leading to total hardware failure.</p>
<p>Need specific help? Visit our technical library to learn <a href="/tech-library/clipsal-c-bus-5508rvf-blinking-led-codes-sydney-cbd">how to fix a blinking red LED on a C-Bus 5508RVF</a>.</p>
"""
    },
    {
        "slug": "blog-electricians-vs-smart-home-relays",
        "title": "Why Traditional Electricians Struggle with Modern Smart Home Relays",
        "desc": "Smart home relays like C-Bus and Dynalite require a programmer, not just an electrician. Learn why standard fault finding techniques fail on automated networks.",
        "category": "How-To",
        "image": "https://images.unsplash.com/photo-1586528116311-ad8ed7fc5180?w=800&q=80",
        "body": """<h2>The Difference Between Electrical and Data</h2>
<p>When a light won't turn on, the traditional electrical response is to check the bulb, the switch, and the breaker. But in a home equipped with C-Bus or Dynalite, the switch doesn't carry 240V power—it only carries a 36V data signal.</p>
<h3>Why Standard Techniques Fail</h3>
<p>A standard multimeter can tell you if power is reaching the relay, but it cannot read the hexadecimal data packets traveling across the pink Cat5E network cable. If an electrician replaces a "faulty" switch without reprogramming its group address, the new switch will do absolutely nothing.</p>
<p>We frequently see cases where electricians have accidentally factory-reset entire networks trying to solve a simple stuck channel.</p>
<h3>The Solution</h3>
<p>Smart home lighting is IT infrastructure. It requires a laptop, specialized toolkit software, and an understanding of network topology.</p>
<p>If you're dealing with stuck-on channels, check our library guide on <a href="/tech-library/dynalite-ddrc1220-stuck-on-channels-north-shore">diagnosing stuck-on channels in Dynalite DDRC1220 controllers</a> before calling a standard electrician.</p>
"""
    },
    {
        "slug": "blog-remote-ip-diagnostics-commercial",
        "title": "How Remote IP Diagnostics are Changing Commercial Lighting Maintenance",
        "desc": "Commercial building managers in Brisbane and Melbourne are slashing maintenance costs by utilizing remote IP diagnostics for their lighting systems.",
        "category": "Commercial",
        "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=80",
        "body": """<h2>The Old Way: Expensive Call-Out Fees</h2>
<p>Historically, when a DALI emergency lighting test failed or a C-Bus schedule didn't fire in a commercial tower, the facility manager had to pay a minimum 4-hour callout fee for a technician to simply plug in a laptop and identify the issue.</p>
<h3>The New Way: IP Gateways</h3>
<p>By upgrading legacy systems with modern Ethernet gateways (like the 5500CN or Dynalite PDEG), specialist programmers can now VPN directly into the building's lighting network from anywhere in the country.</p>
<ul>
<li><strong>Real-Time Monitoring:</strong> We can watch the network traffic live as the fault occurs.</li>
<li><strong>Software Fixes:</strong> Schedules, logic errors, and duplicate addresses can be fixed instantly.</li>
<li><strong>Targeted Hardware Swaps:</strong> If a part is physically broken, we can tell the local electrician exactly which part to bring, eliminating the diagnostic visit entirely.</li>
</ul>
<p>This is exactly how we manage <a href="/dynalite-brisbane">remote Dynalite programming for Brisbane</a> and <a href="/melbourne-dali-lighting-control-compliance">DALI compliance for Melbourne</a> from our Sydney headquarters.</p>
"""
    }
]

base_template_path = os.path.join(DIR, "index.html")
with open(base_template_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Generate blog post HTML files
for blog in blogs:
    filepath = os.path.join(DIR, f"{blog['slug']}.html")
    
    # Simple replacement string construction
    content = base_html.replace('<title>Sydney Automation Co. | C-Bus & Dynalite Lighting Control</title>', f'<title>{blog["title"]} | Sydney Automation Co.</title>')
    content = content.replace('name="description" content="Sydney\'s premier C-Bus and Signify Dynalite lighting control specialists. 24/7 emergency repair, programming, strata maintenance, and LED upgrades. Call 0422 469 739."', f'name="description" content="{blog["desc"]}"')
    
    hero_html = f'''
    <div class="hero" style="padding-top:120px; padding-bottom:60px;">
        <div class="container text-center">
            <div class="tag">{blog["category"]}</div>
            <h1>{blog["title"]}</h1>
            <p class="subtitle" style="max-width:800px; margin:0 auto;">{blog["desc"]}</p>
        </div>
    </div>
    '''
    
    body_content = f'''
    {hero_html}
    <div class="section">
        <div class="container-sm blog-post">
            {blog["body"]}
            <div style="margin-top:50px; text-align:center; padding:30px; background:rgba(240, 112, 32, 0.1); border-radius:8px;">
                <h3>Need professional help?</h3>
                <p>Contact our certified programming team for remote or on-site support.</p>
                <a href="/contact" class="nav-cta" style="display:inline-block; margin-top:20px; padding:15px 30px!important; font-size:16px;">Book a Service Call</a>
            </div>
        </div>
    </div>
    '''
    
    if '</nav>' in content and '<footer' in content:
        head_nav = content.split('</nav>')[0] + '</nav>'
        footer_end = '<footer' + content.split('<footer')[1]
        content = head_nav + body_content + footer_end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath}")

# Update blog.html
blog_index = os.path.join(DIR, "blog.html")
with open(blog_index, 'r', encoding='utf-8') as f:
    blog_html = f.read()

new_cards = ""
for blog in blogs:
    card = f'''
      <a href="/{blog['slug']}" class="blog-card" data-category="{blog['category']}">
        <div class="blog-image" style="background-image: url('{blog['image']}')"></div>
        <div class="blog-content">
          <div class="blog-card-meta">
            <span class="badge">{blog['category']}</span>
            <span>📅 June 2026</span>
          </div>
          <h3 class="blog-card-title">{blog['title']}</h3>
          <p class="blog-card-excerpt">{blog['desc']}</p>
          <div class="blog-card-footer">
            <div class="blog-tech-stack">
              <span class="tech-tag">New</span>
            </div>
            <span class="read-more">Read Article →</span>
          </div>
        </div>
      </a>
'''
    new_cards += card

if '<div class="blog-grid" id="blogGrid">' in blog_html:
    blog_html = blog_html.replace('<div class="blog-grid" id="blogGrid">', '<div class="blog-grid" id="blogGrid">\n' + new_cards)
    with open(blog_index, 'w', encoding='utf-8') as f:
        f.write(blog_html)
    print("Updated blog.html")

# Update sitemap.xml
sitemap_xml = os.path.join(DIR, "sitemap.xml")
if os.path.exists(sitemap_xml):
    with open(sitemap_xml, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    for blog in blogs:
        if blog['slug'] not in xml:
            url_block = f"\n  <url>\n    <loc>https://sydneyautomationco.com.au/{blog['slug']}</loc>\n    <lastmod>2026-06-21</lastmod>\n    <priority>0.70</priority>\n  </url>"
            xml = xml.replace("</urlset>", f"{url_block}\n</urlset>")
            
    with open(sitemap_xml, 'w', encoding='utf-8') as f:
        f.write(xml)
    print("Updated sitemap.xml")
