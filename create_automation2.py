import re

with open("automation-sydney.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update Canonical URL
content = re.sub(r'<link rel="canonical" href="[^"]+"/>', '<link rel="canonical" href="https://sydneyautomationco.com.au/automation-sydney"/>', content)

# Make sure H1 is exactly "Automation Sydney" as requested
content = content.replace('<h1><span class="accent">Automation Sydney</span></h1>', '<h1>Automation Sydney</h1>')

# Ensure the framework elements exist
framework_content = """
    <div class="content-block">
      <h2>Leading Automation Sydney Services</h2>
      <p>Operating across Greater Sydney, from the Eastern Suburbs and North Shore down to the Sutherland Shire and out to Western Sydney, we provide elite smart home and commercial automation solutions.</p>
      <p>Whether you're managing luxury harbourside residences, premium hospitality venues, or Sydney CBD commercial towers, our certified programmers ensure your systems operate flawlessly.</p>
      
      <h3>Building Stock & Systems Integration</h3>
      <p>Sydney's building stock ranges from heritage retrofits to ultra-modern new builds. We specialize in diagnosing, upgrading, and programming industry-standard systems including <strong>C-Bus, Signify Dynalite, DALI, and KNX</strong>. Common faults we resolve include sticking relays, unresponsive keypads, and network communication failures.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Why hire a specialist automation company?</h4>
        <p>Standard electricians install cables, but automation systems like Dynalite and C-Bus require complex software programming and network diagnostics. Our technicians are specialized system integrators.</p>
        <h4>Do you service all of Sydney?</h4>
        <p>Yes, our mobile technicians cover all of Greater Sydney, providing fast response times for critical system failures in both residential and commercial sectors.</p>
      </div>

      <h3>Explore Our Regional Hubs</h3>
      <ul style="line-height: 1.8;">
        <li><a href="/c-bus-programmer-sutherland-shire" style="color: #f07020; text-decoration: underline;">Sutherland Shire</a></li>
        <li><a href="/c-bus-programmer-north-shore" style="color: #f07020; text-decoration: underline;">North Shore</a></li>
        <li><a href="/c-bus-programmer-eastern-suburbs" style="color: #f07020; text-decoration: underline;">Eastern Suburbs</a></li>
        <li><a href="/c-bus-programmer-sydney-cbd" style="color: #f07020; text-decoration: underline;">Sydney CBD</a></li>
      </ul>
    </div>
"""

# Replace the "Why Choose" block with our framework
content = re.sub(r'<h2>Why Choose Sydney Automation Co\?</h2>.*?</div>', framework_content, content, flags=re.DOTALL)

with open("automation-sydney.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Framework injected into automation-sydney.html")
