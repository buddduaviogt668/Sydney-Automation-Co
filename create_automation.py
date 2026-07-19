with open("c-bus-programmer-sydney.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace C-Bus Programmer specific content with generic Automation Sydney content
new_content = content.replace("<title>C-Bus Programmer Sydney | Expert C-Bus Repairs &amp; Upgrades</title>", "<title>Automation Sydney | Smart Home &amp; Commercial Systems Integration</title>")
new_content = new_content.replace('content="Expert C-Bus programmer in Sydney.', 'content="Leading Automation company in Sydney.')
new_content = new_content.replace('<h1>Sydney\'s Elite <span class="accent">C-Bus Programmer</span></h1>', '<h1><span class="accent">Automation Sydney</span></h1>')
new_content = new_content.replace('<p class="lead">System crashed? Lights stuck ON? We solve the complex C-Bus faults that regular electricians can\'t. Accredited experts serving Greater Sydney.</p>', '<p class="lead">From luxury smart homes to commercial high-rises, we are Sydney\'s leading automation specialists. Expert integration, programming, and repair for C-Bus, Dynalite, and DALI systems.</p>')

# Replace the specific C-Bus text with general automation text
new_content = new_content.replace('<h2>Why Choose a Specialist C-Bus Programmer?</h2>', '<h2>Why Choose Sydney Automation Co?</h2>')
new_content = new_content.replace('<p>Most regular electricians can install standard lighting, but <strong>C-Bus is a complex, software-driven network</strong>.', '<p>Most regular electricians can install standard lighting, but <strong>modern automation is a complex, software-driven network</strong>.')

with open("automation-sydney.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Created automation-sydney.html from template")
