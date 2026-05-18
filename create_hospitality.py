with open("automation-sydney.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update Canonical URL & Title
content = content.replace('<link rel="canonical" href="https://sydneyautomationco.com.au/automation-sydney"/>', '<link rel="canonical" href="https://sydneyautomationco.com.au/hospitality-automation-sydney"/>')
content = content.replace('<title>Automation Sydney | Smart Home &amp; Commercial Systems Integration</title>', '<title>Hospitality Automation Sydney | Lighting Control for Venues</title>')
content = content.replace('content="Leading Automation company in Sydney.', 'content="Expert Hospitality Automation in Sydney.')

# H1 Hero
content = content.replace('<h1>Automation Sydney</h1>', '<h1>Hospitality Automation <span class="accent">Sydney</span></h1>')
content = content.replace('<p class="lead">From luxury smart homes to commercial high-rises, we are Sydney\'s leading automation specialists. Expert integration, programming, and repair for C-Bus, Dynalite, and DALI systems.</p>', '<p class="lead">Specialized lighting control and automation programming for Sydney\'s restaurants, clubs, bars, and hotels. Expert integration for C-Bus, Dynalite, and DALI to ensure perfect venue ambiance.</p>')

# Replace Framework content
new_framework = """
    <div class="content-block">
      <h2>Lighting Control for Hospitality Venues</h2>
      <p>Operating across Greater Sydney, from the Eastern Suburbs to the Sutherland Shire, we provide specialized automation solutions for the hospitality sector.</p>
      <p>Whether you manage a premium harbourside restaurant, a bustling CBD nightclub, or a boutique hotel, our certified programmers ensure your lighting systems operate flawlessly and enhance the guest experience.</p>
      
      <h3>Building Stock & Venue Systems</h3>
      <p>Sydney's hospitality venues rely on robust control systems. We specialize in diagnosing, upgrading, and programming industry-standard systems including <strong>Signify Dynalite, C-Bus, and DALI</strong>. Common faults we resolve include failed lighting scenes, unresponsive touch screens, and scheduling issues.</p>

      <h3>Frequently Asked Questions</h3>
      <div class="faq-accordion">
        <h4>Can you program automated lighting scenes for different times of day?</h4>
        <p>Yes, we design complex scheduling and mood lighting scenes that transition automatically from lunch service to dinner and late-night ambiance.</p>
        <h4>Do you offer emergency callouts for venues?</h4>
        <p>Absolutely. We understand that a lighting failure can halt operations. We provide rapid emergency response for hospitality venues across Sydney.</p>
      </div>

      <h3>Explore Our Regional Hubs</h3>
      <ul style="line-height: 1.8;">
        <li><a href="/c-bus-programmer-sydney-cbd" style="color: #f07020; text-decoration: underline;">Sydney CBD Commercial</a></li>
        <li><a href="/c-bus-programmer-eastern-suburbs" style="color: #f07020; text-decoration: underline;">Eastern Suburbs Venues</a></li>
        <li><a href="/c-bus-programmer-sutherland-shire" style="color: #f07020; text-decoration: underline;">Sutherland Shire Hospitality</a></li>
      </ul>
    </div>
"""

import re
content = re.sub(r'<div class="content-block">.*?</ul>\s*</div>', new_framework, content, flags=re.DOTALL)

with open("hospitality-automation-sydney.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Created hospitality-automation-sydney.html")
