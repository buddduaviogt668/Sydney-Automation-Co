import os, glob

files_to_check = ['index.html', 'contact.html', 'terms-of-service.html', 'lighting-control-service-sydney.html', 'lighting-automation-cost-calculator-sydney.html']

for fname in files_to_check:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replacements
    content = content.replace('Or book online — $650 + GST total ($200 + GST upfront, $450 + GST on the day) →', 'Or call to arrange an immediate dispatch →')
    content = content.replace('Site Diagnostic: <span style=\"color: #fff;\">$650 + GST (3-hour minimum)</span>', 'Site Diagnostic: <span style=\"color: #fff;\">Priority Dispatch</span>')
    content = content.replace("The $650 + GST covers George's specialist time and expertise regardless of outcome.", "This covers George's specialist time and expertise regardless of outcome.")
    content = content.replace('Why is the fee $650 + GST regardless of outcome?', 'Why is there a fixed diagnostic structure?')
    content = content.replace('Book Online — $200 + GST to Lock In Your Slot', 'Call Now to Lock In Your Slot')
    content = content.replace('A <strong>$200 + GST Site Fee</strong> (ex GST) applies to all callouts — this covers our travel, on-site fault diagnosis, and written report, and is <strong></strong> toward further work. Subsequent repair or programming is charged at <strong>$150/hr + GST</strong> with a <strong>3-hour minimum</strong>.', 'Our comprehensive service covers travel, on-site fault diagnosis, and a detailed written report. Please call to discuss your specific requirements.')
    content = content.replace('<strong>Callout Fee:</strong> $200 + GST — covers travel, on-site diagnosis with manufacturer software, and a written fault report.', '<strong>Callout Service:</strong> covers travel, on-site diagnosis with manufacturer software, and a written fault report.')
    content = content.replace('Every callout is <strong>$650 + GST</strong> — $200 + GST paid upfront, plus $150/hr + GST (3-hour minimum, $450 + GST) billed on the day. Covers travel, on-site fault diagnosis with manufacturer software, and a written report.', 'Every callout covers travel, on-site fault diagnosis with manufacturer software, and a written report. Please contact us for specific scoping.')
    content = content.replace('Book &amp; Pay $200 + GST Site Fee', 'Call for Priority Dispatch')
    
    # In cost calculator
    content = content.replace('$200 + GST Site Fee - $1,050*', 'Custom Estimate Provided on Call*')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print('Replaced missed pricing text')
