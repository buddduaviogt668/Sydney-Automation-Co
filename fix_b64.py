import re, os, base64

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

os.makedirs('assets/img/projects', exist_ok=True)

counter = [0]

def replace_b64(match):
    mime = match.group(1)  # e.g. image/jpeg
    data = match.group(2)
    ext = mime.split('/')[-1].replace('jpeg','jpg')
    counter[0] += 1
    filename = f'assets/img/projects/img_{counter[0]:03d}.{ext}'
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(data))
    print(f'Extracted: {filename}')
    return f'src="{filename}"'

html = re.sub(r'src="data:(image/[^;]+);base64,([^"]+)"', replace_b64, html)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. {counter[0]} images extracted.')