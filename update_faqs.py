import re

def update_faq_schema(filepath, new_schema_items, new_html_items):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    schema_end_match = re.search(r'("mainEntity": \[.*?)(}\s*\])', content, re.DOTALL)
    if schema_end_match:
        new_schema_str = "},\n" + ",\n".join(new_schema_items) + "\n      ]"
        content = content[:schema_end_match.start(2)] + new_schema_str + content[schema_end_match.end(2):]

    html_match = re.search(r'(<div class="faq-item">.*?</div></div>)\s*</div>\s*</section>', content, re.DOTALL)
    
    if not html_match:
        html_match = list(re.finditer(r'(<div class="faq-item">.*?</div></div>)', content, re.DOTALL))[-1]
        
    if isinstance(html_match, re.Match):
        insert_pos = html_match.end(1)
        content = content[:insert_pos] + "\n" + "\n".join(new_html_items) + content[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

cbus_schema = [
    '''      {
        "@type": "Question",
        "name": "Why are my C-Bus lights stuck on and won't turn off?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When C-Bus lights are stuck on, it's typically caused by a failed relay module, a stuck physical contact, or a C-Bus network communication failure where the switch command isn't reaching the dimmer/relay. We carry replacement Clipsal C-Bus modules in our vans and can fix this on the spot."
        }
      }''',
    '''      {
        "@type": "Question",
        "name": "Why is my C-Bus keypad flashing or completely blank?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A flashing or blank C-Bus keypad usually indicates a loss of network burden, a failed C-Bus power supply, or a severed bus cable. The keypad isn't receiving enough voltage or network clock pulses to operate. We diagnose these network faults within 30 minutes of arriving."
        }
      }''',
    '''      {
        "@type": "Question",
        "name": "Who can fix a broken C-Bus system today in Sydney?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sydney Automation Co provides same-day emergency C-Bus repairs across Greater Sydney. Call George directly on 0422 469 739 for immediate assistance with residential and commercial Clipsal C-Bus faults."
        }
      }'''
]

cbus_html = [
    '<div class="faq-item"><div class="faq-q">Why are my C-Bus lights stuck on and won\'t turn off? <span>+</span></div><div class="faq-a">When C-Bus lights are stuck on, it\'s typically caused by a failed relay module, a stuck physical contact, or a C-Bus network communication failure where the switch command isn\'t reaching the dimmer/relay. We carry replacement Clipsal C-Bus modules in our vans and can fix this on the spot.</div></div>',
    '<div class="faq-item"><div class="faq-q">Why is my C-Bus keypad flashing or completely blank? <span>+</span></div><div class="faq-a">A flashing or blank C-Bus keypad usually indicates a loss of network burden, a failed C-Bus power supply, or a severed bus cable. The keypad isn\'t receiving enough voltage or network clock pulses to operate. We diagnose these network faults within 30 minutes of arriving.</div></div>',
    '<div class="faq-item"><div class="faq-q">Who can fix a broken C-Bus system today in Sydney? <span>+</span></div><div class="faq-a">Sydney Automation Co provides same-day emergency C-Bus repairs across Greater Sydney. Call George directly on 0422 469 739 for immediate assistance with residential and commercial Clipsal C-Bus faults.</div></div>'
]

dynalite_schema = [
    '''      {
        "@type": "Question",
        "name": "Why is my Dynalite keypad not responding?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An unresponsive Signify Dynalite keypad is usually caused by a faulty DyNet network connection, a failed DBC power supply elsewhere on the network, or the keypad losing its programming address. We can reconnect with the DyNet network to restore communication."
        }
      }''',
    '''      {
        "@type": "Question",
        "name": "How do I reset a Signify Dynalite system after a power outage?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "If a Dynalite system doesn't recover after a power outage, it may be due to a blown internal fuse on a dimmer module (like a DDMC802) or a damaged power supply. Attempting a hard reset at the breaker may help, but if the issue persists, a technician needs to test the DyNet voltage."
        }
      }''',
    '''      {
        "@type": "Question",
        "name": "Who does urgent Dynalite repairs in Sydney?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sydney Automation Co specializes in urgent Signify Dynalite repairs. We offer same-day service for critical commercial and residential lighting faults. Call 0422 469 739 to speak with an accredited Dynalite programmer."
        }
      }'''
]

dynalite_html = [
    '<div class="faq-item"><div class="faq-q">Why is my Dynalite keypad not responding? <span>+</span></div><div class="faq-a">An unresponsive Signify Dynalite keypad is usually caused by a faulty DyNet network connection, a failed DBC power supply elsewhere on the network, or the keypad losing its programming address. We can reconnect with the DyNet network to restore communication.</div></div>',
    '<div class="faq-item"><div class="faq-q">How do I reset a Signify Dynalite system after a power outage? <span>+</span></div><div class="faq-a">If a Dynalite system doesn\'t recover after a power outage, it may be due to a blown internal fuse on a dimmer module (like a DDMC802) or a damaged power supply. Attempting a hard reset at the breaker may help, but if the issue persists, a technician needs to test the DyNet voltage.</div></div>',
    '<div class="faq-item"><div class="faq-q">Who does urgent Dynalite repairs in Sydney? <span>+</span></div><div class="faq-a">Sydney Automation Co specializes in urgent Signify Dynalite repairs. We offer same-day service for critical commercial and residential lighting faults. Call 0422 469 739 to speak with an accredited Dynalite programmer.</div></div>'
]

update_faq_schema('cbus-repair-sydney.html', cbus_schema, cbus_html)
update_faq_schema('dynalite-repair-sydney.html', dynalite_schema, dynalite_html)

print("FAQ Schema and HTML updated successfully.")
