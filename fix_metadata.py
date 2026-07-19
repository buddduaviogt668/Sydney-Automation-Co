
import os
import re
from bs4 import BeautifulSoup

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text) # Remove non-alphanumeric characters
    text = re.sub(r'\s+', '-', text) # Replace spaces with hyphens
    text = re.sub(r'-+', '-', text) # Replace multiple hyphens with single
    return text.strip('-')

def fix_metadata(file_path, base_url="https://sydneyautomationco.com.au/"):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Extract title
    title_tag = soup.find('title')
    if not title_tag:
        print(f"No title tag found in {file_path}")
        return
    page_title = title_tag.get_text().replace(' | Sydney Automation Co', '').strip()
    
    # Generate slug from title
    page_slug = slugify(page_title)
    page_url = f"{base_url}{page_slug}"

    # Update meta description
    description_tag = soup.find('meta', {'name': 'description'})
    if description_tag:
        # Create a more generic description based on the title if possible, or use a default
        new_description = f"Comprehensive guide to {page_title.lower()} by Sydney Automation Co. Learn about design, installation, and troubleshooting for smart automation systems in Sydney." # Customize this
        description_tag['content'] = new_description
    else:
        print(f"No meta description found in {file_path}")

    # Update canonical URL
    canonical_tag = soup.find('link', {'rel': 'canonical'})
    if canonical_tag:
        canonical_tag['href'] = page_url
    else:
        print(f"No canonical link found in {file_path}")

    # Update Open Graph tags
    og_url_tag = soup.find('meta', {'property': 'og:url'})
    if og_url_tag:
        og_url_tag['content'] = page_url
    else:
        print(f"No og:url found in {file_path}")

    og_title_tag = soup.find('meta', {'property': 'og:title'})
    if og_title_tag:
        og_title_tag['content'] = page_title + ' | Sydney Automation Co'
    else:
        print(f"No og:title found in {file_path}")

    og_description_tag = soup.find('meta', {'property': 'og:description'})
    if og_description_tag:
        og_description_tag['content'] = new_description # Reuse generated description
    else:
        print(f"No og:description found in {file_path}")

    # Update LocalBusiness schema URL
    local_business_schema = soup.find('script', {'type': 'application/ld+json'}, text=re.compile(r'LocalBusiness'))
    if local_business_schema:
        schema_content = local_business_schema.string
        schema_content = re.sub(r'"url": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"url": "{page_url}"', schema_content)
        local_business_schema.string = schema_content
    else:
        print(f"No LocalBusiness schema found in {file_path}")

    # Update BreadcrumbList schema
    breadcrumb_schema = soup.find('script', {'type': 'application/ld+json'}, text=re.compile(r'BreadcrumbList'))
    if breadcrumb_schema:
        schema_content = breadcrumb_schema.string
        # Assuming a structure of Home -> Page Title
        schema_content = re.sub(r'"name": "C-Bus Programmer Sydney"', f'"name": "{page_title}"', schema_content)
        schema_content = re.sub(r'"item": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"item": "{page_url}"', schema_content)
        breadcrumb_schema.string = schema_content
    else:
        print(f"No BreadcrumbList schema found in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated metadata for {file_path}")


# List of new pages to process (from pasted_content.txt and previous audit)
new_pages = [
    "c-bus-network-deep-dive-advanced-diagnostics.html",
    "dynalite-system-architecture-design-installation.html",
    "knx-protocol-explained-integration-sydney.html",
    "dali-2-lighting-control-commercial-buildings.html",
    "matter-thread-smart-homes-interoperability-sydney.html",
    "intelligent-workspace-automation-north-sydney-tech-hubs.html",
    "luxury-smart-home-integration-eastern-suburbs-estates.html",
    "smart-lighting-energy-management-sydney-hospitality.html",
    "industrial-automation-high-bay-lighting-western-sydney.html",
    "atmospheric-lighting-automation-sydney-cbd-retailers.html",
    "c-bus-vs-dynalite-vs-knx-comparison-sydney.html",
    "smart-home-roi-calculator-sydney.html",
    "sydney-home-automation-cost-guide-2026.html",
    "ai-driven-smart-lighting-energy-management-sydney.html",
    "invisible-automation-heritage-retrofitting-sydney.html",
    "high-end-home-cinema-multi-room-audio-sydney.html"
]

repo_path = "/home/ubuntu/Sydney-Automation-Co"

for page in new_pages:
    full_path = os.path.join(repo_path, page)
    if os.path.exists(full_path):
        fix_metadata(full_path)
    else:
        print(f"Warning: Page file not found: {full_path}")

print("Metadata correction script finished.")
