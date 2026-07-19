import os

print("Updating Navigation and Blogs...")

new_blogs = [
    ('blog-strata-lighting-energy-savings-sydney', 'Strata Lighting Energy Savings', 'How strata managers can reduce common area electricity consumption by 30-60%.', 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80', 'Commercial'),
    ('blog-western-sydney-warehouse-lighting-repairs', 'Western Sydney Warehouse Lighting', 'Fixing burnt-out contactors and stuck-on high bay lighting in industrial warehouses.', 'https://images.unsplash.com/photo-1586528116311-ad8ed7fc5180?w=800&q=80', 'Commercial'),
    ('blog-sydney-cbd-commercial-tower-lighting-nabers', 'Sydney CBD Tower Automation & NABERS', 'How building managers improve NABERS energy ratings using C-Bus and Dynalite.', 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=80', 'Commercial'),
    ('blog-eastern-suburbs-strata-lighting-automation', 'Eastern Suburbs Coastal Sensor Maintenance', 'Combatting salt spray corrosion on external DALI sensors in waterfront strata complexes.', 'https://images.unsplash.com/photo-1506953823976-52e1fdc0149a?w=800&q=80', 'Maintenance'),
    ('blog-parramatta-institutional-lighting-dali-cbus', 'Parramatta Institutional Lighting', 'DALI emergency lighting compliance and automation for schools and hospitals.', 'https://images.unsplash.com/photo-1576495199011-eb94736d05d6?w=800&q=80', 'Compliance'),
    ('blog-regional-nsw-hospitality-lighting-dynalite', 'Regional NSW Hospitality Dynalite', 'Priority Dynalite programming for Southern Highlands and Illawarra luxury venues.', 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80', 'Commercial'),
    ('blog-how-to-partner-cbus-programmer', 'Electrician Partner Program', 'How electricians can partner with us for white-label accredited programming.', 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80', 'How-To'),
    ('blog-why-consultants-switch-rapix-cbus', 'Why Consultants Switch from RAPIX to C-Bus', 'Comparing commercial DALI lighting control systems for engineering specifications.', 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80', 'Comparison')
]

cards_html = ""
for link, title, desc, img, cat in new_blogs:
    cards_html += f'''
      <!-- NEW CARD: {title} -->
      <a href="/{link}" class="blog-card" data-category="{cat}">
        <div class="blog-image" style="background-image: url('{img}')"></div>
        <div class="blog-content">
          <div class="blog-card-meta">
            <span class="badge">{cat}</span>
            <span>📅 May 2026</span>
          </div>
          <h3 class="blog-card-title">{title}</h3>
          <p class="blog-card-excerpt">{desc}</p>
          <div class="blog-card-footer">
            <div class="blog-tech-stack">
              <span class="tech-tag">New</span>
            </div>
            <span class="read-more">Read Article →</span>
          </div>
        </div>
      </a>
'''

try:
    with open('blog.html', 'r', encoding='utf-8') as f:
        blog_html = f.read()
    
    if '<div class="blog-grid" id="blogGrid">' in blog_html and 'Strata Lighting Energy Savings' not in blog_html:
        blog_html = blog_html.replace('<div class="blog-grid" id="blogGrid">', f'<div class="blog-grid" id="blogGrid">\n{cards_html}')
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(blog_html)
        print("Updated blog.html")
except Exception as e:
    print("Error updating blog.html:", e)


# Update navigation on all HTML pages
main_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0

for file in main_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changed = False
        
        # 1. Update Mega Nav link
        if 'href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>' in content and 'href="/services-hub">All Services Hub (400+ Pages)</a>' not in content:
            content = content.replace('href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>', 
                'href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>\n<div class="dd-divider"></div>\n<a href="/services-hub" style="color:#f07020;">★ All Services Hub (400+ Pages)</a>')
            changed = True
            
        # 2. Update Mobile Nav link
        if 'href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>' in content and 'href="/services-hub">All Services Hub' not in content:
            content = content.replace('href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>', 
                'href="/building-lighting-upgrades-sydney">Building Lighting Upgrades</a>\n<a href="/services-hub" style="color:#f07020;">★ All Services Hub (400+ Pages)</a>')
            changed = True
            
        if changed:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
    except Exception as e:
        continue

print(f"Updated Navigation on {updated_count} files!")
