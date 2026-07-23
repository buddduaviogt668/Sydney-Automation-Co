import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # 1. Update the bottom property in CSS for .sac-float-cta
    content = re.sub(
        r'(\.sac-float-cta\s*\{[^}]*bottom:\s*)28px', 
        r'\g<1>100px', 
        content
    )
    
    # 2. Remove the WhatsApp button HTML
    content = re.sub(
        r'<a\s+class="sac-float-wa"[^>]*>.*?</a>', 
        '', 
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Overlap and WhatsApp fix complete.")
