import os, glob, re

root = r'C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co'
files = glob.glob(os.path.join(root, '*.html'))

NAV_HTML = '''
<nav style="background:#001226;padding:10px 0;text-align:center;border-bottom:1px solid rgba(255,255,255,0.08);position:sticky;top:44px;z-index:9000;">
  <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:center;gap:24px;flex-wrap:wrap;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:14px;">
    <a href="/" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;transition:color 0.2s;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">🏠 Home</a>
    <a href="/automation-sydney" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">⚡ Automation</a>
    <a href="/afss-emergency-lighting-services" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">🚨 Emergency Lighting</a>
    <a href="/blog" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">📝 Blog</a>
    <a href="/about" style="color:#a8c0e0;text-decoration:none;padding:6px 10px;border-radius:4px;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#a8c0e0'">👤 About</a>
    <a href="/book-service" style="background:#f07020;color:#fff;text-decoration:none;padding:6px 16px;border-radius:4px;font-weight:700;" onmouseover="this.style.background='#d06010'" onmouseout="this.style.background='#f07020'">📅 Book Service</a>
    <a href="tel:0422469739" style="color:#4da6ff;text-decoration:none;padding:6px 10px;border-radius:4px;font-weight:600;" onmouseover="this.style.color='#f07020'" onmouseout="this.style.color='#4da6ff'">📞 0422 469 739</a>
  </div>
</nav>
'''

fixed = 0
skipped = 0

for f in files:
    name = os.path.basename(f)
    if name in ('test.html', 'old_index.html'):
        continue
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    
    # Skip if already has a nav element
    if '<nav' in content or 'href="/"' in content or 'href="/index' in content:
        skipped += 1
        continue
    
    # Find the closing </header> tag and insert nav after it
    if '</header>' in content:
        new_content = content.replace('</header>', '</header>' + NAV_HTML, 1)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        fixed += 1
    elif '<body>' in content:
        # fallback: insert after <body>
        new_content = content.replace('<body>', '<body>' + NAV_HTML, 1)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        fixed += 1
    else:
        skipped += 1

print(f'Nav injected into {fixed} pages.')
print(f'Already had nav (skipped): {skipped}')