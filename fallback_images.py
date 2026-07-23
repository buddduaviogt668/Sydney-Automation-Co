import json
import re

def main():
    with open('products.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    m = re.search(r'const products = (\[.*?\]);', html, re.DOTALL)
    if not m:
        return
        
    prods = json.loads(m.group(1))
    updated = 0
    
    for p in prods:
        img_val = p.get('img', '')
        # identify bad images or placeholders
        bad_words = ['unsplash', 'og-image', 'placeholder', 'ykkap', 'wallpaper', 'dragoart', 'animalspot', 'africanarguments', 'misesapo', 'yamasahouse', 'freshop', 'tiktak', 'sampleformats', 'makeshop', 'mbmart', 'thehansindia', 'images-spe', 'kaigoshoku', 'lib.berkeley', 'tetrahedron']
        
        needs_fallback = img_val == ''
        for bw in bad_words:
            if bw in img_val:
                needs_fallback = True
                
        if needs_fallback:
            if p['brand'].lower() in ['c-bus', 'clipsal']:
                p['img'] = '/clipsal c-bus.png'
            elif p['brand'].lower() == 'rapix':
                p['img'] = '/rapix.png'
            elif p['brand'].lower() == 'dynalite':
                p['img'] = '/signdyn-logo.png'
            else:
                p['img'] = '/favicon.png'
            updated += 1
            
    if updated > 0:
        new_json = json.dumps(prods, indent=4)
        new_html = html[:m.start(1)] + new_json + html[m.end(1):]
        with open('products.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Applied fallback brand logos to {updated} products.")
    else:
        print("No updates needed.")

if __name__ == '__main__':
    main()
