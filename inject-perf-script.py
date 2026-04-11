import os
import re

HTML_DIR = "."
OLD_SCRIPT_TAG = '<script src="/perf-optimise.js" defer></script>'
NEW_SCRIPT_TAG = '<script src="/perf-init.js" defer></script>'

FB_INLINE_PATTERN = re.compile(
    r'<script[^>]*>!function\(f,b,e,v,n,t,s\).*?fbq\(\'track\', ?\'PageView\'\);?\s*</script>(\s*<noscript>[^<]*<img[^>]*facebook[^>]*>[^<]*</noscript>)?',
    re.DOTALL
)
CLARITY_INLINE_PATTERN = re.compile(
    r'<!-- Microsoft Clarity --><script[^>]*>\(function\(c,l,a,r,i,t,y\).*?</script>',
    re.DOTALL
)

updated = []
skipped = []

for root, dirs, files in os.walk(HTML_DIR):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.github', 'dist', 'mnt']]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            original = content

            # Remove hardcoded FB Pixel and Clarity
            content = FB_INLINE_PATTERN.sub('', content)
            content = CLARITY_INLINE_PATTERN.sub('', content)

            # Remove old perf-optimise.js tag
            content = content.replace(OLD_SCRIPT_TAG, '')

            # Inject perf-init.js if not already present
            if NEW_SCRIPT_TAG not in content and '</body>' in content:
                content = content.replace('</body>', f'  {NEW_SCRIPT_TAG}\n</body>')

            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated.append(fpath)
            else:
                skipped.append(fpath)
        except OSError:
            pass

print(f"✅ Updated: {len(updated)} files")
print(f"⏭️  Skipped: {len(skipped)} files")
