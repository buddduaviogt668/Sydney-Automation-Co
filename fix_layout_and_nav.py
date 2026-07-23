import os
import re
import json

# 1. Regenerate services-hub.html using index.html as the shell
with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

match = re.search(r'<nav>.*?</nav>', html, flags=re.DOTALL)
nav_block = match.group(0) if match else ''

match_header = re.search(r'</nav>', html, flags=re.DOTALL)
header_end = match_header.end() if match_header else 0

match_footer = re.search(r'<footer.*?>', html, flags=re.DOTALL)
footer_start = match_footer.start() if match_footer else len(html)

shell_head = html[:header_end]
shell_foot = html[footer_start:]

# Fix canonical and meta tags in shell_head
shell_head = re.sub(r'<title>.*?</title>', '<title>All Services Hub | Sydney Automation Co. | 400+ C-Bus & Dynalite Pages</title>', shell_head)
shell_head = re.sub(r'<meta content="[^"]+" name="description" />', '<meta content="Complete directory of all accredited C-Bus, Dynalite, DALI, strata, commercial, and warehouse lighting automation services by Sydney Automation Co. across NSW." name="description" />', shell_head)
shell_head = re.sub(r'<link rel="canonical" href="[^"]+" />', '<link rel="canonical" href="https://sydneyautomationco.com.au/services-hub" />', shell_head)
shell_head = re.sub(r'<meta content="[^"]+" property="og:url" />', '<meta content="https://sydneyautomationco.com.au/services-hub" property="og:url" />', shell_head)

# Get the generated services hub content
with open('services-hub.html', 'r', encoding='utf-8', errors='ignore') as f:
    sh_content = f.read()

sh_body_match = re.search(r'<div class="content">(.*?)</div>\s*<div class="cta-bar">', sh_content, flags=re.DOTALL)
sh_inner = sh_body_match.group(1) if sh_body_match else ''

# Clean up styles in the inner content to match main site
sh_inner = sh_inner.replace('background:#0e1f3d;border:1px solid #1a2a4a', 'background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1)')
sh_inner = sh_inner.replace("onmouseover=\"this.style.borderColor='#f07020';this.style.color='#f07020'\"", "onmouseover=\"this.style.background='rgba(240,112,32,0.1)';this.style.borderColor='#f07020'\"")
sh_inner = sh_inner.replace("onmouseout=\"this.style.borderColor='#1a2a4a';this.style.color='#a8c0e0'\"", "onmouseout=\"this.style.background='transparent';this.style.borderColor='rgba(255,255,255,0.1)'\"")

new_hub_content = f'''
<div class="page">
    <div class="hero">
        <div class="container-sm">
            <span class="tag">DIRECTORY</span>
            <h1>All Services <span>Hub</span></h1>
            <p class="lead" style="margin: 0 auto; text-align: center;">Your one-stop directory to all 400+ accredited C-Bus, Signify Dynalite, DALI-2, strata, commercial, warehouse, and suburb-specific lighting automation services across Greater Sydney and Regional NSW.</p>
        </div>
    </div>
    <div class="section">
        <div class="container">
            {sh_inner}
        </div>
    </div>
</div>
'''

final_hub = shell_head + new_hub_content + shell_foot
with open('services-hub.html', 'w', encoding='utf-8') as f:
    f.write(final_hub)
print('Updated services-hub.html to match site template.')

# 2. Update navigation in all main files to include Services Hub
main_files = [f for f in os.listdir('.') if f.endswith('.html')]

modified_nav_count = 0
for mf in main_files:
    try:
        with open(mf, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Insert into mega nav after AFSS Testing
        if 'href="/afss-testing-sydney">AFSS Testing</a>' in content and 'href="/services-hub">All Services Hub</a>' not in content:
            content = content.replace('href="/afss-testing-sydney">AFSS Testing</a>', 'href="/afss-testing-sydney">AFSS Testing</a>\n            <div class="dd-divider"></div>\n            <a href="/services-hub">All Services Hub</a>')
            with open(mf, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_nav_count += 1
    except Exception as e:
        pass
print(f'Updated navigation in {modified_nav_count} files.')

# 3. Update blog.html to include the new blogs
try:
    with open('blog.html', 'r', encoding='utf-8') as f:
        blog_content = f.read()

    new_blogs = [
        ('blog-strata-lighting-energy-savings-sydney.html', 'Strata Lighting Energy Savings', 'How strata managers can reduce common area electricity consumption by 30-60%.', 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80'),
        ('blog-western-sydney-warehouse-lighting-repairs.html', 'Western Sydney Warehouse Lighting', 'Fixing burnt-out contactors and stuck-on high bay lighting in industrial warehouses.', 'https://images.unsplash.com/photo-1586528116311-ad8ed7fc5180?w=800&q=80'),
        ('blog-sydney-cbd-commercial-tower-lighting-nabers.html', 'Sydney CBD Tower Automation & NABERS', 'How building managers improve NABERS energy ratings using C-Bus and Dynalite.', 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=80'),
        ('blog-eastern-suburbs-strata-lighting-automation.html', 'Eastern Suburbs Coastal Sensor Maintenance', 'Combatting salt spray corrosion on external DALI sensors in waterfront strata complexes.', 'https://images.unsplash.com/photo-1506953823976-52e1fdc0149a?w=800&q=80'),
        ('blog-parramatta-institutional-lighting-dali-cbus.html', 'Parramatta Institutional Lighting', 'DALI emergency lighting compliance and automation for schools and hospitals.', 'https://images.unsplash.com/photo-1576495199011-eb94736d05d6?w=800&q=80'),
        ('blog-regional-nsw-hospitality-lighting-dynalite.html', 'Regional NSW Hospitality Dynalite', 'Priority Dynalite programming for Southern Highlands and Illawarra luxury venues.', 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80'),
        ('blog-how-to-partner-cbus-programmer.html', 'Electrician Partner Program', 'How electricians can partner with us for white-label accredited programming.', 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80'),
        ('blog-why-consultants-switch-rapix-cbus.html', 'Why Consultants Switch from RAPIX to C-Bus', 'Comparing commercial DALI lighting control systems for engineering specifications.', 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80')
    ]

    cards_html = ""
    for link, title, desc, img in new_blogs:
        cards_html += f'''
        <a href="/{link}" class="blog-card">
            <div class="bc-img" style="background-image:url('{img}');"></div>
            <div class="bc-content">
                <div class="bc-tag">New Resource</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
        </a>
    '''

    if '<div class="blog-grid">' in blog_content and 'Strata Lighting Energy Savings' not in blog_content:
        blog_content = blog_content.replace('<div class="blog-grid">', f'<div class="blog-grid">\n{cards_html}')
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(blog_content)
        print('Updated blog.html with 8 new blog cards.')
    else:
        print('Could not find <div class="blog-grid"> in blog.html or cards already present.')
except FileNotFoundError:
    print('blog.html not found.')
