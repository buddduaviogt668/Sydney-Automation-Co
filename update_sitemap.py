import os
import xml.etree.ElementTree as ET
from datetime import datetime

def update_sitemap():
    """Add new suburb and blog pages to sitemap.xml"""
    sitemap_path = "/home/ubuntu/Sydney-Automation-Co/sitemap.xml"
    
    # Parse existing sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    # Define namespace
    ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Find all suburb pages
    suburb_pages = []
    for filename in os.listdir("/home/ubuntu/Sydney-Automation-Co"):
        if filename.endswith("-cbus-dynalite-repair-sydney.html"):
            suburb_pages.append(filename)
    
    # Find all blog pages
    blog_pages = []
    blog_dir = "/home/ubuntu/Sydney-Automation-Co/blog"
    if os.path.exists(blog_dir):
        for filename in os.listdir(blog_dir):
            if filename.endswith(".html"):
                blog_pages.append(filename)
    
    # Add suburb pages to sitemap
    for page in suburb_pages:
        page_slug = page.replace(".html", "")
        url_elem = ET.SubElement(root, '{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        loc = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        loc.text = f"https://sydneyautomationco.com.au/{page_slug}"
        changefreq = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
        changefreq.text = "weekly"
        priority = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
        priority.text = "0.8"
    
    # Add blog pages to sitemap
    for page in blog_pages:
        page_slug = page.replace(".html", "")
        url_elem = ET.SubElement(root, '{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        loc = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        loc.text = f"https://sydneyautomationco.com.au/blog/{page_slug}"
        changefreq = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
        changefreq.text = "weekly"
        priority = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
        priority.text = "0.7"
    
    # Write updated sitemap
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    print(f"Updated sitemap with {len(suburb_pages)} suburb pages and {len(blog_pages)} blog pages")

if __name__ == "__main__":
    update_sitemap()
