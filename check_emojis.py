import glob

missing_buttons = []
has_issues = []
all_files = sorted(glob.glob('*.html'))

for html_file in all_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'sac-float-cta' not in content:
        missing_buttons.append(html_file)
    elif '??' in content and ('Call Now' in content or 'WhatsApp' in content):
        has_issues.append(html_file)

proper_count = len(all_files) - len(missing_buttons) - len(has_issues)
print(f'Total files: {len(all_files)}')
print(f'Files with PROPER emojis: {proper_count}')
print(f'Files MISSING floating CTA: {len(missing_buttons)}')
print(f'Files with CORRUPTED emojis: {len(has_issues)}')

if has_issues:
    print(f'\nFiles needing emoji fixes:')
    for f in has_issues[:20]:
        print(f'  - {f}')
