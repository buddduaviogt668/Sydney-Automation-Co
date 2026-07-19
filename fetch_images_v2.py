import urllib.request
import urllib.parse
import re
import json
import time

def get_bing_image(query):
    # add site restrictions to ensure we get real electrical products, not random animals
    url = 'https://www.bing.com/images/search?q=' + urllib.parse.quote(query) + '&FORM=HDRSC2'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    })
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        # match murl":"https://..."
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', html)
        
        # Prefer images from trusted domains
        trusted_domains = ['clipsal', 'sparkydirect', 'mmem', 'middys', 'lighting.philips', 'se.com']
        
        for m in matches:
            for td in trusted_domains:
                if td in m.lower():
                    return m
                    
        # If no trusted domain match, return the first one that doesn't look like facebook/linkedin
        if matches:
            for m in matches:
                if 'lookaside' not in m and 'fbcdn' not in m and 'licdn' not in m:
                    return m
            return matches[0]
            
    except Exception as e:
        print(f"Error for {query}: {str(e)}")
        
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
    
    for i, p in enumerate(prods):
        img_val = p.get('img', '')
        if 'unsplash' in img_val or 'og-image' in img_val or 'placeholder' in img_val or img_val.strip() == '':
            # build targeted query
            q = f"{p['brand']} {p['part']} product"
            img = get_bing_image(q)
            if img:
                p['img'] = img
                updated += 1
                # print without crashing on cp1252
                print(f"[{i+1}/{len(prods)}] {p['part']} -> {img.encode('ascii', 'ignore').decode('ascii')}")
            else:
                print(f"[{i+1}/{len(prods)}] {p['part']} -> Not found.")
            time.sleep(0.1)
            
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
