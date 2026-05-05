import os
import re

BASE_URL = "https://sydneyautomationco.com.au"

def get_canonical_url(filename):
    if filename == "index.html":
        return f"{BASE_URL}/"
    name = filename.replace(".html", "")
    return f"{BASE_URL}/{name}"

def fix_metadata(filepath):
    filename = os.path.basename(filepath)
    target_url = get_canonical_url(filename)
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Handle Canonical Tag
    canonical_pattern = re.compile(r'<link[^>]*rel="canonical"[^>]*>', re.IGNORECASE)
    if canonical_pattern.search(content):
        # Update existing
        content = re.sub(
            r'(<link[^>]*rel="canonical"[^>]*href=")([^"]*)("[^>]*>)',
            rf'\1{target_url}\3',
            content,
            flags=re.IGNORECASE
        )
    else:
        # Insert after <head> or before </head>
        # Better: after <title> or first <meta>
        meta_insert = f'\n<link rel="canonical" href="{target_url}"/>'
        if '<head>' in content:
            content = content.replace('<head>', f'<head>{meta_insert}')
        else:
            # Fallback to beginning of file if no head
            content = meta_insert + "\n" + content

    # 2. Handle OG:URL Tag
    og_url_pattern = re.compile(r'<meta[^>]*property="og:url"[^>]*>', re.IGNORECASE)
    if og_url_pattern.search(content):
        content = re.sub(
            r'(<meta[^>]*property="og:url"[^>]*content=")([^"]*)("[^>]*>)',
            rf'\1{target_url}\3',
            content,
            flags=re.IGNORECASE
        )
    else:
        og_insert = f'\n<meta property="og:url" content="{target_url}"/>'
        if '</head>' in content:
            content = content.replace('</head>', f'{og_insert}\n</head>')
        else:
            content += og_insert

    return content

def main():
    updated_count = 0
    for root, _, files in os.walk("."):
        if any(x in root for x in [".git", "node_modules", "markdown_mirror"]):
            continue
        for file in files:
            if file.endswith(".html"):
                fpath = os.path.join(root, file)
                original_content = ""
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        original_content = f.read()
                    
                    new_content = fix_metadata(fpath)
                    
                    if new_content != original_content:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_count += 1
                        print(f"Fixed: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
