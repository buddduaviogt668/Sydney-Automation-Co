import os

directory = '.'

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            orig_content = content

            # Update Copyright year
            content = content.replace("© 2025 Sydney Automation Co.", "© 2026 Sydney Automation Co.")

            # Add legal links to footer
            target_str = '<a href="/services-hub">All Services Hub</a> · <a href="/services-hub">All Services</a>'
            replacement_str = '<a href="/services-hub">All Services Hub</a> · <a href="/services-hub">All Services</a> · <a href="/privacy-policy">Privacy Policy</a> · <a href="/terms-of-service">Terms of Service</a> · <a href="/sitemap.html">Sitemap</a>'
            
            # Since some pages might have it differently formatted:
            target_str_2 = '<a href="/services">All Services</a>'
            replacement_str_2 = '<a href="/services">All Services</a> · <a href="/privacy-policy">Privacy Policy</a> · <a href="/terms-of-service">Terms of Service</a> · <a href="/sitemap.html">Sitemap</a>'

            if target_str in content:
                content = content.replace(target_str, replacement_str)
            elif target_str_2 in content:
                content = content.replace(target_str_2, replacement_str_2)
            else:
                # If neither is found, look for something common in footer
                target_str_3 = '<a href="/afss-testing-sydney">AFSS Testing</a>'
                replacement_str_3 = '<a href="/afss-testing-sydney">AFSS Testing</a> · <a href="/privacy-policy">Privacy Policy</a> · <a href="/terms-of-service">Terms of Service</a> · <a href="/sitemap.html">Sitemap</a>'
                content = content.replace(target_str_3, replacement_str_3)

            if content != orig_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Updated copyright and footer links.")
