import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]
images = set()

# Get all images in directory
local_images = set(os.listdir('.'))

broken_images = []

for file in files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Simple regex for img src
    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in srcs:
        if src.startswith('http') or src.startswith('data:'):
            continue
        
        # Clean query strings if any
        path = src.split('?')[0].lstrip('/')
        
        if path not in local_images:
            broken_images.append({'file': file, 'image': src})

if not broken_images:
    print("No broken local images found.")
else:
    print(f"Found {len(broken_images)} potential broken images:")
    for item in broken_images:
        print(f"- {item['file']}: {item['image']}")
