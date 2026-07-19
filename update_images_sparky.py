import json
import re
import urllib.request
import time
import os

def check_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        urllib.request.urlopen(req, timeout=3)
        return True
    except:
        return False

def get_image(brand, part, name):
    part_clean = part.strip()
    
    # Try SparkyDirect for Clipsal
    if brand.lower() in ['c-bus', 'clipsal']:
        urls_to_try = [
            f"https://www.sparkydirect.com.au/assets/full/{part_clean}.jpg",
            f"https://www.sparkydirect.com.au/assets/full/{part_clean}.png"
        ]
        for url in urls_to_try:
            if check_url(url):
                return url
                
    # If not found or different brand, maybe try Bing Image search again, but strictly filter
    # Wait, the prompt says "go online to find them". 
    # Let's try Google search for the part number on an image service.
    
    # Try Middys
    middys_url = f"https://middys.com.au/images/product/medium/{part_clean}.jpg"
    if check_url(middys_url):
        return middys_url
        
    return None

def main():
    with open('products.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    m = re.search(r'const products = (\[.*?\]);', html, re.DOTALL)
    if not m:
        return
        
    prods = json.loads(m.group(1))
    updated = 0
    
    for i, p in enumerate(prods):
        img_val = p.get('img', '')
        if 'unsplash' in img_val or 'og-image' in img_val or 'placeholder' in img_val or img_val == '' or 'ykkap' in img_val or 'wallpaper' in img_val or 'dragoart' in img_val or 'animalspot' in img_val:
            img = get_image(p['brand'], p['part'], p['name'])
            if img:
                p['img'] = img
                updated += 1
                print(f"Found {p['part']} -> {img}")
            else:
                # If we really can't find it directly, at least put a brand-specific logo or a clean placeholder
                pass
            time.sleep(0.1)
            
    if updated > 0:
        new_json = json.dumps(prods, indent=4)
        new_html = html[:m.start(1)] + new_json + html[m.end(1):]
        with open('products.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {updated} images.")
    else:
        print("No images found.")

if __name__ == '__main__':
    main()
