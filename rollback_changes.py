import re
import os

def rollback_index():
    """Remove Energy ROI sections from homepage"""
    path = "/home/ubuntu/Sydney-Automation-Co/index.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all Energy ROI sections (they appear multiple times due to the insertion)
    # Pattern: <!-- ENERGY ROI & BUILDING OPTIMIZATION --> ... </section>
    pattern = r'  <!-- ENERGY ROI & BUILDING OPTIMIZATION -->.*?</section>\n\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Also remove the nav label changes for Energy ROI
    content = content.replace('Energy ROI & LED Upgrades', 'LED Upgrades & Car Parks')
    content = content.replace('AFSS & Compliance Audit', 'Emergency Lighting AFSS')
    content = content.replace('DALI-2 Compliance & ROI', 'DALI-2 Compliance NSW')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Removed Energy ROI sections from homepage")

def remove_false_accreditations():
    """Remove false DALI-2 and AFSS accreditation claims site-wide"""
    directory = "/home/ubuntu/Sydney-Automation-Co"
    
    # Patterns to remove
    false_claims = [
        'accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification, and Signify Dynalite System Design',
        'Accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification, and Signify Dynalite System Design',
        'accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification',
        'Accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification',
        'DALI-2 Compliance Expert',
        'Compliance Expert',
        'Are you accredited for DALI-2 and emergency lighting compliance?',
        'Yes, we are accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification, and Signify Dynalite System Design. We support commercial strata and building compliance across NSW.',
    ]
    
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "test.html":
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Remove false accreditation claims
                for claim in false_claims:
                    if claim in content:
                        content = content.replace(claim, '')
                        count += 1
                
                # Also remove FAQ sections that mention false accreditations
                pattern = r'<h3[^>]*>Are you accredited for DALI-2.*?</div>\s*</div>'
                content = re.sub(pattern, '', content, flags=re.DOTALL)
                
                if content != original_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
            except Exception as e:
                pass
    
    print(f"✓ Removed false accreditation claims from {count} files")

if __name__ == "__main__":
    rollback_index()
    remove_false_accreditations()
