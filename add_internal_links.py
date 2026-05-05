import os
import re

# Define key terms and their target URLs
KEYWORDS = {
    "C-Bus": "/c-bus-programmer-sydney",
    "Dynalite": "/dynalite-programmer-sydney",
    "DALI": "/dali-lighting-repair",
    "lighting control": "/lighting-control-service-sydney",
    "smart home": "/",
    "Sydney": "/",
    "repairs": "/c-bus-repairs-sydney",
    "fault finding": "/dynalite-fault-finding-sydney-common-faults",
    "RAPIX": "/rapix-lighting-control"
}

def add_links(content, current_file):
    # Only link in paragraph tags to avoid breaking headers or existing links
    # Also limit to one link per keyword per page to avoid over-optimization
    
    # Extract paragraphs
    paragraphs = re.findall(r'<p[^>]*>.*?</p>', content, re.DOTALL | re.IGNORECASE)
    
    for kw, url in KEYWORDS.items():
        # Skip if current file is the target URL
        if current_file.replace(".html", "") == url.strip("/"):
            continue
        if url == "/" and current_file == "index.html":
            continue
            
        linked = False
        new_paragraphs = []
        for p in paragraphs:
            if not linked and kw in p and f'href="{url}"' not in p and '<a ' not in p:
                # Basic replacement: first occurrence of keyword in a paragraph that doesn't have a link
                # Using a slightly more careful regex to avoid matching inside tags
                pattern = re.compile(rf'(?<![">])\b{re.escape(kw)}\b(?![^<]*>)')
                if pattern.search(p):
                    new_p = pattern.sub(f'<a href="{url}">{kw}</a>', p, count=1)
                    content = content.replace(p, new_p)
                    linked = True
            
    return content

def main():
    updated_count = 0
    for root, _, files in os.walk("."):
        if any(x in root for x in [".git", "node_modules", "markdown_mirror"]):
            continue
        for file in files:
            if file.endswith(".html"):
                fpath = os.path.join(root, file)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        original_content = f.read()
                    
                    new_content = add_links(original_content, file)
                    
                    if new_content != original_content:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_count += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\nTotal files updated with internal links: {updated_count}")

if __name__ == "__main__":
    main()
