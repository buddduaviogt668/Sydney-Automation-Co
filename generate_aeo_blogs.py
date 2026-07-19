import os
import re

blogs = [
    {
        "filename": "blog-cbus-not-working-repair-guide.html",
        "title": "C-Bus Not Working? A Practical Troubleshooting Guide for Sydney Homes",
        "category": "Troubleshooting",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80",
        "excerpt": "When your C-Bus system stops responding, it can be frustrating. Learn the common causes of C-Bus faults and how our Sydney specialists diagnose them.",
        "content": """
<h2>Why is my C-Bus System Not Working?</h2>
<p>One of the most frequent calls we get at Sydney Automation Co is: "My C-Bus is not working." Whether it's a single switch that has stopped responding, lights that are stuck on, or a complete system blackout, the causes usually fall into a few specific categories.</p>
<h3>1. Power Supply Issues</h3>
<p>The C-Bus network relies on dedicated power supplies to keep the data bus active. If a C-Bus power supply fails (which is common in systems over 10-15 years old), the voltage on the pink cable drops, and switches lose their ability to communicate with the relays.</p>
<h3>2. Corrupted Programming or Scene Loss</h3>
<p>Sometimes, a power surge or a failing component can cause the network to lose its programming. This is why having an accredited programmer with the C-Bus Toolkit is essential. We can plug directly into your network, read the current state, and restore or rebuild the lost programming.</p>
<h3>3. Failed Relay or Dimmer Modules</h3>
<p>If only one circuit or a specific room isn't working, the issue is often a failed channel on a relay or dimmer module in your switchboard. We carry spare modules and can often replace and reprogram these on the spot during our same-day service calls across Sydney.</p>
<p><strong>Need emergency C-Bus repairs in Sydney?</strong> Don't wait. Call George on <a href="tel:0422469739">0422 469 739</a> for rapid fault finding.</p>
"""
    },
    {
        "filename": "blog-dynalite-repairs-electrician-sydney.html",
        "title": "Dynalite Repairs: Why You Need a Specialist Programmer, Not Just an Electrician",
        "category": "Troubleshooting",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1586528116311-ad8ed7fc5180?w=800&q=80",
        "excerpt": "Experiencing issues with your Philips Dynalite system? Discover why calling a certified Dynalite system builder is crucial for prompt and effective repairs in Sydney.",
        "content": """
<h2>The Complexity of Dynalite Systems</h2>
<p>Philips Dynalite is a highly robust lighting control system used in high-end residential homes and commercial buildings throughout Sydney. However, when things go wrong—such as keypads becoming unresponsive or lighting scenes failing to trigger—a standard electrician often lacks the software tools and training to fix it.</p>
<h3>Software vs. Hardware Faults</h3>
<p>Many Dynalite issues are actually software conflicts or network communication errors on the DyNet bus. A specialist equipped with the Dynalite System Builder software can log onto your network, trace the data packets, and pinpoint exactly where the communication is failing. A regular electrician might recommend replacing expensive hardware when a simple reprogramming is all that's needed.</p>
<h3>Common Dynalite Faults We Fix:</h3>
<ul>
<li>Unresponsive Antumbra or Revolution keypads</li>
<li>Lights flashing or flickering unpredictably</li>
<li>Integration issues with third-party AV or HVAC systems</li>
<li>Complete network failure due to cable faults or power supply failure</li>
</ul>
<p>If you need expert Dynalite repairs anywhere in Greater Sydney, contact Sydney Automation Co today. We provide same-day response and expert diagnosis.</p>
"""
    },
    {
        "filename": "blog-dali-lighting-control-system-repair.html",
        "title": "DALI Lighting Control System Repairs & Maintenance in Sydney",
        "category": "Maintenance",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=80",
        "excerpt": "DALI systems offer incredible flexibility for commercial lighting, but require specialist knowledge to maintain. Learn about common DALI faults and repair strategies.",
        "content": """
<h2>Understanding DALI Lighting Faults</h2>
<p>The Digital Addressable Lighting Interface (DALI) is the gold standard for commercial and high-end residential lighting control in Sydney. But when a DALI line drops out, it can take down lighting for an entire floor or car park.</p>
<h3>Common DALI Issues</h3>
<p>The most frequent issues we encounter involve addressing conflicts, failed LED drivers, or short circuits on the DALI bus. Because DALI devices are daisy-chained, a fault in one section of the cabling can sometimes disrupt communication for all 64 devices on that line.</p>
<h3>Our Diagnostic Approach</h3>
<p>At Sydney Automation Co, we don't guess. We use specialized DALI testing equipment to monitor traffic on the bus, identify short circuits, and re-address replacement drivers without disrupting the rest of the network. Whether it's a DALI-2 compliance upgrade or fixing a broken emergency lighting automated test sequence, we have the tools and the expertise.</p>
<p>Are you a facility manager dealing with DALI lighting issues? <a href="/book-service">Book a service call</a> with our accredited technicians today.</p>
"""
    },
    {
        "filename": "blog-smart-home-automation-sydney-installers.html",
        "title": "Smart Home Automation Troubleshooting: When to Call the Experts",
        "category": "How-To",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1506953823976-52e1fdc0149a?w=800&q=80",
        "excerpt": "From unresponsive apps to failing network bridges, smart home automation can sometimes fail. Here's how to know when it's time to call a professional Sydney integrator.",
        "content": """
<h2>When Smart Homes Stop Being Smart</h2>
<p>Modern smart home automation systems are incredibly convenient—until they stop working. Whether you're in the Eastern Suburbs, North Shore, or Sutherland Shire, a failing automation system can disrupt your daily routine.</p>
<h3>Basic Troubleshooting Steps</h3>
<p>Before calling an expert, try these steps:</p>
<ol>
<li><strong>Check the network:</strong> Ensure your Wi-Fi router is functioning and the automation bridge is connected.</li>
<li><strong>Power cycle:</strong> Restart your control processor or network gateway.</li>
<li><strong>Check the app:</strong> Look for any error messages or updates pending in your system's app.</li>
</ol>
<h3>When to Call Sydney Automation Co</h3>
<p>If power cycling doesn't work, the issue likely lies deeper in the programming or involves a hardware failure. Systems like C-Bus and Dynalite require proprietary software to diagnose. Our certified programmers can identify the root cause quickly, ensuring your home returns to seamless operation without the guesswork.</p>
"""
    },
    {
        "filename": "blog-car-park-lighting-upgrades-sydney.html",
        "title": "Car Park Lighting Maintenance & LED Upgrades for Strata",
        "category": "Commercial",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1576495199011-eb94736d05d6?w=800&q=80",
        "excerpt": "Discover how upgrading your strata car park lighting to automated LED systems can drastically reduce energy consumption and improve security.",
        "content": """
<h2>Optimizing Strata Car Park Lighting</h2>
<p>For strata buildings across Sydney, car park lighting is often one of the largest ongoing energy expenses. Lights left running 24/7 consume massive amounts of electricity, but safety and security cannot be compromised.</p>
<h3>The Solution: Automated LED Upgrades</h3>
<p>By upgrading to modern LED fixtures integrated with intelligent sensors (such as DALI or standalone microwave sensors), you can ensure lights are only at full brightness when a vehicle or pedestrian is present. During empty periods, the lights can dim to a safe background level (e.g., 20%), slashing energy usage while maintaining security.</p>
<h3>Maintenance and Repairs</h3>
<p>If your existing car park automation system is failing—lights staying on all day or not turning on when triggered—Sydney Automation Co can help. We repair and optimize legacy systems, or provide complete upgrade paths to modern, energy-efficient solutions.</p>
"""
    },
    {
        "filename": "blog-smart-light-switch-replacement-sydney.html",
        "title": "Smart Light Switch Replacement: Upgrading Your Broken Keypads",
        "category": "How-To",
        "date": "May 2026",
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
        "excerpt": "Got a broken C-Bus or Dynalite wall switch? Learn what's involved in replacing smart light switches and keypads in your Sydney home.",
        "content": """
<h2>Replacing Broken Smart Switches</h2>
<p>Standard light switches are simple to replace, but smart keypads—like C-Bus Neo or Saturn series, or Dynalite Antumbra keypads—are a different story. If a button stops clicking or the LEDs fail, the switch usually needs to be replaced.</p>
<h3>Why You Can't Just Swap It Out</h3>
<p>Unlike a standard 240V switch, a smart keypad is essentially a small computer connected to a data network. When you install a new smart switch, it comes blank from the factory. It must be programmed with its specific network address and configured so that each button triggers the correct lighting scene or group.</p>
<h3>Our Replacement Service</h3>
<p>At Sydney Automation Co, we stock common C-Bus and Dynalite keypads. We can come to your property, safely remove the faulty unit, install the new switch, and program it to function exactly as the old one did—or even update the programming to better suit your current needs.</p>
<p>Don't put up with broken switches. Call us on <strong>0422 469 739</strong> for professional replacement and programming.</p>
"""
    }
]

template_html = ""
with open("blog.html", "r", encoding="utf-8") as f:
    template_html = f.read()

# Extract the header/nav and footer from blog.html
# We'll split around `<div class="hero">` and `<div class="blog-grid" id="blogGrid">` to build our blog page.
# Actually, the blog post pages have a slightly different structure. Let's look at blog-strata-lighting-energy-savings-sydney.html
with open("blog-strata-lighting-energy-savings-sydney.html", "r", encoding="utf-8") as f:
    sample_blog = f.read()

head_match = re.search(r'(.*?<div class="page">)', sample_blog, re.DOTALL)
footer_match = re.search(r'(<footer>.*)', sample_blog, re.DOTALL)

if not head_match or not footer_match:
    print("Could not find header/footer in sample blog")
    exit(1)

head = head_match.group(1)
footer = footer_match.group(1)

for blog in blogs:
    # customize the head title and description
    custom_head = head.replace("<title>Strata Lighting Energy Savings Sydney | Expert Guide</title>", f"<title>{blog['title']} | Sydney Automation Co</title>")
    custom_head = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{blog["excerpt"]}" name="description"/>', custom_head)
    
    html = custom_head + f"""
<div class="hero" style="padding:80px 24px 60px;">
  <div class="container-sm">
    <div class="tag">{blog['category']}</div>
    <h1>{blog['title']}</h1>
    <div class="meta" style="margin-top:16px;">{blog['date']} • By George Skarmoutsos</div>
  </div>
</div>
<div class="section" style="padding-top:0;">
  <div class="container-sm">
    <img src="{blog['image']}" style="width:100%; border-radius:16px; margin: -40px 0 40px; border: 1px solid #2a4a80; box-shadow: 0 10px 30px rgba(0,0,0,0.3);" alt="{blog['title']}">
    <div class="blog-post">
      {blog['content']}
    </div>
    
    <div class="cta-band" style="margin-top:64px;">
      <h2 style="font-size:28px;margin-bottom:16px;">Need Expert Automation Help?</h2>
      <p style="color:#a8c0e0;margin-bottom:24px;">Sydney's leading C-Bus and Dynalite specialists. Same-day emergency response available.</p>
      <div class="btns" style="justify-content:center;">
        <a href="tel:0422469739" class="btn btn-primary">📞 Call George: 0422 469 739</a>
        <a href="/book-service" class="btn btn-outline">Book & Pay Deposit</a>
      </div>
    </div>
  </div>
</div>
""" + footer

    with open(blog['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {blog['filename']}")

# Now append to blog.html
blog_index = ""
with open("blog.html", "r", encoding="utf-8") as f:
    blog_index = f.read()

# Find where to insert cards: after <div class="blog-grid" id="blogGrid">
insert_pos = blog_index.find('<div class="blog-grid" id="blogGrid">')
if insert_pos != -1:
    insert_pos += len('<div class="blog-grid" id="blogGrid">')
    
    cards_html = "\n"
    for blog in blogs:
        cards_html += f"""
      <a href="/{blog['filename'].replace('.html', '')}" class="blog-card" data-category="{blog['category']}">
        <div class="blog-image" style="background-image: url('{blog['image']}')"></div>
        <div class="blog-content">
          <div class="blog-card-meta">
            <span class="badge">{blog['category']}</span>
            <span>📅 {blog['date']}</span>
          </div>
          <h3 class="blog-card-title">{blog['title']}</h3>
          <p class="blog-card-excerpt">{blog['excerpt']}</p>
          <div class="blog-card-footer">
            <div class="blog-tech-stack">
              <span class="tech-tag">New</span>
            </div>
            <span class="read-more">Read Article →</span>
          </div>
        </div>
      </a>
"""
    
    new_blog_index = blog_index[:insert_pos] + cards_html + blog_index[insert_pos:]
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(new_blog_index)
    print("Updated blog.html with new articles")
