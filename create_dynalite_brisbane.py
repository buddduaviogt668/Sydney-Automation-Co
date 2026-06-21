import sys

with open('brisbane-cbus-dynalite-programmer.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace titles and meta
html = html.replace('<title>C-Bus & Dynalite Remote Programming Brisbane | Sydney Automation Co.</title>', '<title>Dynalite Brisbane | Remote Programming & Support Specialists</title>')
html = html.replace('C-Bus and Dynalite remote programming for Brisbane.', 'Philips Dynalite remote programming and support for Brisbane commercial buildings and hotels.')
html = html.replace('href="https://sydneyautomationco.com.au/brisbane-cbus-dynalite-programmer"', 'href="https://sydneyautomationco.com.au/dynalite-brisbane"')

# Replace Hero
html = html.replace('BRISBANE — REMOTE PROGRAMMING &amp; LOCAL SPECIALISTS', 'BRISBANE DYNALITE — REMOTE PROGRAMMING &amp; LOCAL SPECIALISTS')
html = html.replace('C-Bus &amp; Dynalite Remote Programming — Brisbane', 'Dynalite Brisbane Remote Programming')
html = html.replace('Your Brisbane C-Bus or Dynalite system has a fault.', 'Your Brisbane Philips Dynalite system has a fault.')

# Replace body text
html = html.replace('C-Bus or Dynalite network', 'Dynalite network')
html = html.replace('C-Bus and Dynalite in office towers', 'Dynalite in office towers')
html = html.replace('C-Bus or Dynalite installation experience', 'Dynalite installation experience')
html = html.replace('C-Bus or Dynalite programming expertise', 'Dynalite programming expertise')
html = html.replace('C-Bus or Dynalite not communicating', 'Dynalite not communicating')
html = html.replace('Remote C-Bus &amp; Dynalite Expertise', 'Remote Dynalite Expertise')

with open('dynalite-brisbane.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('dynalite-brisbane.html created')
