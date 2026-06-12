import re
import os

def fix_hero_text():
    """Restore original hero text"""
    path = "/home/ubuntu/Sydney-Automation-Co/index.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the modified hero text with the original
    old_text = "System crashed? Lights stuck on? Scenes not responding? We diagnose complex C-Bus, Dynalite &amp; DALI faults that regular electricians can't. **Cut energy overheads by up to 60%** with our building optimization and DALI-2 compliance audits — same day, across Greater Sydney."
    new_text = "System crashed? Lights stuck on? Scenes not responding? We diagnose and fix the complex C-Bus, Dynalite &amp; DALI lighting faults that regular electricians can't — same day, across Greater Sydney."
    
    content = content.replace(old_text, new_text)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Restored original hero text")

def remove_broken_faqs():
    """Remove all broken FAQ sections site-wide"""
    directory = "/home/ubuntu/Sydney-Automation-Co"
    
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "test.html":
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Remove the entire Common Questions section and all broken FAQ content
                # Pattern: <!-- AEO FAQ for Featured Snippets --> ... </section>
                pattern = r'  <!-- AEO FAQ for Featured Snippets -->.*?</section>'
                content = re.sub(pattern, '', content, flags=re.DOTALL)
                
                # Also remove any broken FAQ divs with incomplete text
                pattern = r'<div style="background: rgba\(255,255,255,0\.02\);.*?Are you accredited.*?</div>\s*</div>'
                content = re.sub(pattern, '', content, flags=re.DOTALL)
                
                # Remove any remaining broken "Yes, we are ." text
                content = content.replace('Yes, we are . We support commercial strata and building compliance across NSW.', '')
                content = content.replace('Yes, we are .', '')
                
                # Remove any orphaned "Common Questions" headers
                content = re.sub(r'<h2[^>]*>Common Questions</h2>', '', content)
                
                if content != original_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    
            except Exception as e:
                pass
    
    print(f"✓ Removed broken FAQ sections from {count} files")

if __name__ == "__main__":
    fix_hero_text()
    remove_broken_faqs()
