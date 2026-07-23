import os
import glob
import re

html_files = glob.glob('*.html', root_dir='c:/Users/gaska/Sydney-Automation-Co', recursive=True)

pattern1 = re.compile(r'A \$200 diagnostic fee applies to all callouts.*?No work proceeds without your approval\.</strong>', re.IGNORECASE | re.DOTALL)
pattern2 = re.compile(r'A \$200 diagnostic fee applies to all callouts.*?we bill hourly at \$150/hr \+ GST\.', re.IGNORECASE | re.DOTALL)
pattern3 = re.compile(r'A \$200 diagnostic fee applies to all callouts.*?with a 3-hour minimum \(\$450 \+ GST\)\.', re.IGNORECASE | re.DOTALL)
pattern4 = re.compile(r'A \$200 diagnostic fee applies to all.*?before works commence\.', re.IGNORECASE | re.DOTALL)
pattern5 = re.compile(r'A \$200 diagnostic fee applies to all.*?with a 3-hour minimum\.', re.IGNORECASE | re.DOTALL)
pattern6 = re.compile(r'A \$200 diagnostic fee applies to all callouts.*?</p>', re.IGNORECASE | re.DOTALL)

replacement = 'Your $200 initial callout fee guarantees priority dispatch and a comprehensive on-site diagnostic assessment by a certified automation specialist, ensuring you get exactly what you pay for—expert insight and a clear path forward. For ongoing quality service, our premium repair and programming rate is $150/hr + GST (standard 3-hour minimum applies for initial visits). We pride ourselves on absolute transparency: <strong>no work proceeds without your full approval.</strong>'

replacement_faq = 'Your $200 initial callout fee guarantees priority dispatch and a comprehensive on-site diagnostic assessment by a certified specialist. This ensures you receive premium quality service and exactly what you pay for—expert insight and a definitive path forward. Subsequent expert repair or programming is provided at $150/hr + GST (with a standard 3-hour minimum). All pricing is entirely transparent and scope-defined before any further works commence.'

changed_count = 0

for file in html_files:
    filepath = os.path.join('c:/Users/gaska/Sydney-Automation-Co', file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    new_content, c4 = pattern4.subn(replacement_faq, new_content)
    new_content, c5 = pattern5.subn(replacement_faq, new_content)
    
    new_content, c1 = pattern1.subn(replacement, new_content)
    new_content, c2 = pattern2.subn(replacement, new_content)
    new_content, c3 = pattern3.subn(replacement, new_content)
    
    # Fallback to replace anything from A $200 diagnostic fee to </p> with the replacement + </p>
    def fallback_repl(match):
        text = match.group(0)
        if 'diagnostic' in text.lower():
            if 'transparent' in text.lower():
                return replacement_faq + '</p>'
            return replacement + '</p>'
        return text
    
    if new_content == content:
         new_content, c6 = pattern6.subn(fallback_repl, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed_count += 1
        print(f"Updated {file}")

print(f'Total files updated: {changed_count}')
