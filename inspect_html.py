import re
with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Checking blog.html structure...")
if '<div class="grid-3">' in html:
    print("Found <div class=\"grid-3\">")
elif 'class="grid' in html:
    print("Found some other grid:")
    for match in re.finditer(r'<div[^>]*class="[^"]*grid[^"]*"', html):
        print(match.group(0))
else:
    print("No grid found in blog.html")

print("\nChecking nav in c-bus-programmer-sydney.html...")
with open('c-bus-programmer-sydney.html', 'r', encoding='utf-8') as f:
    nav_html = f.read()

match = re.search(r'<ul class="nav-links">.*?</ul>', nav_html, flags=re.DOTALL)
if match:
    print(match.group(0))

