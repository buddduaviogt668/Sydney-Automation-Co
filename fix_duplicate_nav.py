import glob

duplicate_nav = """<a href="/services-hub" style="color:#f07020;">★ All Services Hub (400+ Pages)</a>
<div class="dd-divider"></div>
<a href="/services-hub" style="color:#f07020;">★ All Services Hub (400+ Pages)</a>"""

correct_nav = """<div class="dd-divider"></div>
<a href="/services-hub" style="color:#f07020;">★ All Services Hub (400+ Pages)</a>"""

count = 0
for filepath in glob.glob("*.html"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if duplicate_nav in content:
            content = content.replace(duplicate_nav, correct_nav)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(f"Error on {filepath}: {e}")

print(f"Removed duplicate All Services Hub link in {count} files.")
