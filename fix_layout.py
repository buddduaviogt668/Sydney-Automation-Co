import glob

fixed_count = 0

for html_file in sorted(glob.glob('*.html')):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix the floating CTA structure - break it into multiple lines
    # Pattern 1: with proper emojis all on one line
    content = content.replace(
        '<div class="sac-float-cta">  <a href="tel:0422469739" class="sac-float-call">📞 Call Now</a>  <a href="https://wa.me/61422469739" target="_blank" rel="noopener" class="sac-float-wa">💬 WhatsApp</a></div>',
        '<div class="sac-float-cta">\n  <a href="tel:0422469739" class="sac-float-call">📞 Call Now</a>\n  <a href="https://wa.me/61422469739" target="_blank" rel="noopener" class="sac-float-wa">💬 WhatsApp</a>\n</div>'
    )
    
    # Pattern 2: with ?? on one line
    content = content.replace(
        '<div class="sac-float-cta">  <a href="tel:0422469739" class="sac-float-call">?? Call Now</a>  <a href="https://wa.me/61422469739" target="_blank" rel="noopener" class="sac-float-wa">?? WhatsApp</a></div>',
        '<div class="sac-float-cta">\n  <a href="tel:0422469739" class="sac-float-call">📞 Call Now</a>\n  <a href="https://wa.me/61422469739" target="_blank" rel="noopener" class="sac-float-wa">💬 WhatsApp</a>\n</div>'
    )
    
    if content != original:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1

print(f'Fixed layout in {fixed_count} files')
