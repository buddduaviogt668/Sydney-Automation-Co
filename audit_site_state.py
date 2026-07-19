import os
import re
import glob

DIR = r"C:\Users\gaska\Documents\antigravity\lucid-babbage\Sydney-Automation-Co"

def main():
    html_files = glob.glob(os.path.join(DIR, "*.html"))
    total_pages = len(html_files)
    
    # 1. Clean URLs check
    unclean_urls = []
    for f in html_files:
        basename = os.path.basename(f)
        if basename in ['404.html']: continue
        name_without_ext = basename[:-5]
        # Check if it contains uppercase, spaces, or weird chars
        if not re.match(r'^[a-z0-9\-]+$', name_without_ext):
            unclean_urls.append(basename)
            
    # 2. Sitemap check
    with open(os.path.join(DIR, "sitemap.xml"), "r", encoding="utf-8", errors="replace") as f:
        xml_content = f.read()
    with open(os.path.join(DIR, "sitemap.html"), "r", encoding="utf-8", errors="replace") as f:
        html_sitemap_content = f.read()
        
    missing_from_xml = []
    missing_from_html_sitemap = []
    
    for f in html_files:
        basename = os.path.basename(f)
        url_path = f"/{basename.replace('.html', '')}"
        full_url = f"https://sydneyautomationco.com.au{url_path}"
        
        # We might have the full .html in some old sitemaps, or the clean one. 
        # Just check if the basename without extension is in there.
        base = basename.replace('.html', '')
        if base not in xml_content and basename not in xml_content:
            missing_from_xml.append(basename)
        if base not in html_sitemap_content and basename not in html_sitemap_content:
            missing_from_html_sitemap.append(basename)
            
    # 3. Orphan check (Very basic: check if the filename appears in ANY other html file besides sitemap.html)
    # We will build a set of all links found across all pages
    all_links = set()
    for f in html_files:
        basename = os.path.basename(f)
        if basename == 'sitemap.html': continue
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as file:
                content = file.read()
                # Find all href="/something" or href="something.html"
                links = re.findall(r'href=["\']/?([^"\']+)["\']', content)
                for link in links:
                    link = link.split('#')[0].strip('/')
                    if link.endswith('.html'):
                        all_links.add(link)
                    else:
                        all_links.add(link + '.html')
        except Exception:
            pass
            
    orphaned_pages = []
    for f in html_files:
        basename = os.path.basename(f)
        if basename not in all_links and basename != 'index.html' and basename != 'sitemap.html':
            orphaned_pages.append(basename)

    print(f"Total HTML Pages: {total_pages}")
    print(f"Unclean URLs: {len(unclean_urls)}")
    if unclean_urls: print(f"  Examples: {unclean_urls[:5]}")
    
    print(f"Missing from sitemap.xml: {len(missing_from_xml)}")
    print(f"Missing from sitemap.html: {len(missing_from_html_sitemap)}")
    
    print(f"Orphaned pages (only linked from sitemap, not from content pages): {len(orphaned_pages)}")
    if orphaned_pages: print(f"  Examples: {orphaned_pages[:5]}")

if __name__ == "__main__":
    main()
