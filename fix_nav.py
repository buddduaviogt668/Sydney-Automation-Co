import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<a href="/automation-specialists">Automation Specialists</a>\n', '')
content = content.replace('<a href="/sydney-automation-specialists-cbus-dynalite-partnership">Automation Specialist Partnership</a>\n', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")