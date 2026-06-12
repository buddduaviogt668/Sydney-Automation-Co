import os
import re

def update_html_files():
    directory = "/home/ubuntu/Sydney-Automation-Co"
    
    # New Nav Labels
    nav_replacements = [
        ('LED Upgrades & Car Parks', 'Energy ROI & LED Upgrades'),
        ('Emergency Lighting AFSS', 'AFSS & Compliance Audit'),
        ('DALI-2 Compliance NSW', 'DALI-2 Compliance & ROI'),
        ('Are you an Electrician or Builder?', 'Trade Partner? White-Label Support')
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                new_content = content
                
                # Update Nav Labels
                for old, new in nav_replacements:
                    new_content = new_content.replace(old, new)
                
                # Update Title for 2026 and SEO
                if '<title>' in new_content:
                    title_match = re.search(r'<title>(.*?)</title>', new_content)
                    if title_match:
                        current_title = title_match.group(1)
                        if "2026" not in current_title:
                            new_title = current_title.replace("Sydney", "Sydney 2026")
                            new_content = new_content.replace(f"<title>{current_title}</title>", f"<title>{new_title}</title>")

                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    # print(f"Updated {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_html_files()
