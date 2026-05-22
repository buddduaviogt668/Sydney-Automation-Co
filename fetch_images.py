import urllib.request
import urllib.parse
import re
import json
import time
import os

def get_bing_image(query):
    url = 'https://www.bing.com/images/search?q=' + urllib.parse.quote(query) + '+product+image'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', html)
        if matches:
            for m in matches:
                # avoid facebook lookaside or weird cdns if possible
                if 'lookaside' not in m and 'fbcdn' not in m and 'licdn' not in m:
                    return m
            return matches[0]
    except Exception as e:
        print(f"Error fetching {query}: {e}")
    return None

def main():
    with open('products.html', 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    m = re.search(r'const products = (\[.*?\]);', html, re.DOTALL)
    if not m:
        print("Could not find products array.")
        return
        
    prods = json.loads(m.group(1))
    updated = 0
    total_to_update = sum(1 for p in prods if 'unsplash' in p['img'] or 'og-image' in p['img'] or 'placeholder' in p['img'])
    print(f"Found {total_to_update} placeholders to update.")
    
    for i, p in enumerate(prods):
        if 'unsplash' in p['img'] or 'og-image' in p['img'] or 'placeholder' in p['img']:
            q = f"{p['brand']} {p['part']}"
            print(f"[{i+1}/{len(prods)}] Fetching image for: {q}")
            img = get_bing_image(q)
            if img:
                p['img'] = img
                updated += 1
                print(f" -> Found: {img}")
            else:
                print(" -> Not found.")
            time.sleep(0.3)
            
    if updated > 0:
        new_json = json.dumps(prods, indent=4)
        new_html = html[:m.start(1)] + new_json + html[m.end(1):]
        with open('products.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Finished. Successfully updated {updated} images.")
    else:
        print("No images were updated.")

if __name__ == '__main__':
    main()
