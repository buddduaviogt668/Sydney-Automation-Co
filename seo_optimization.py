import os
import re
from datetime import datetime

def add_seo_enhancements():
    """
    Add SEO/AEO/GEO enhancements to all HTML files:
    - AEO: Answer Engine Optimization (clear definitions, FAQs, step-by-step guides)
    - GEO: Geographic Optimization (location-based schema, local business markup)
    - SEO: Traditional search engine optimization (meta tags, structured data)
    """
    
    directory = "/home/ubuntu/Sydney-Automation-Co"
    
    # AEO FAQ Template for common questions
    aeo_faq_template = """
  <!-- AEO FAQ for Featured Snippets -->
  <section style="background: #0a1628; padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.05);">
    <div class="container">
      <div style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-size: 32px; color: #fff; margin-bottom: 40px; font-family: 'Barlow Condensed', sans-serif;">Common Questions</h2>
        <div style="display: grid; gap: 20px;">
          <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 25px; border-radius: 12px;">
            <h3 style="color: #fff; margin-bottom: 12px; font-size: 18px;">What is the typical response time for emergency repairs?</h3>
            <p class="dim" style="margin: 0; line-height: 1.6;">We offer same-day fault finding and emergency repairs across Greater Sydney. Most issues are diagnosed and resolved within 24 hours. For urgent support, call 0422 469 739.</p>
          </div>
          <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 25px; border-radius: 12px;">
            <h3 style="color: #fff; margin-bottom: 12px; font-size: 18px;">Are you accredited for DALI-2 and emergency lighting compliance?</h3>
            <p class="dim" style="margin: 0; line-height: 1.6;">Yes, we are accredited in DALI-2 Compliance, AFSS Emergency Lighting Certification, and Signify Dynalite System Design. We support commercial strata and building compliance across NSW.</p>
          </div>
          <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 25px; border-radius: 12px;">
            <h3 style="color: #fff; margin-bottom: 12px; font-size: 18px;">What areas do you service?</h3>
            <p class="dim" style="margin: 0; line-height: 1.6;">We service Greater Sydney including Menai, Sutherland Shire, Eastern Suburbs, North Shore, Sydney CBD, and surrounding regions. We offer mobile callouts and emergency support across all areas.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

    # GEO Schema enhancement for local business
    geo_schema = """
  <!-- Enhanced GEO Schema for Local Search -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://sydneyautomationco.com.au/",
  "name": "Sydney Automation Co.",
  "url": "https://sydneyautomationco.com.au/",
  "telephone": "+61422469739",
  "email": "service@sydneyautomationco.com.au",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Menai",
    "addressLocality": "Menai",
    "addressRegion": "NSW",
    "postalCode": "2234",
    "addressCountry": "AU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -34.0167,
    "longitude": 151.0167
  },
  "areaServed": [
    {
      "@type": "City",
      "name": "Sydney"
    },
    {
      "@type": "City",
      "name": "Menai"
    },
    {
      "@type": "City",
      "name": "Cronulla"
    },
    {
      "@type": "City",
      "name": "Parramatta"
    }
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "07:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "$$",
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61570407305417",
    "https://www.instagram.com/sydneyautomationco/",
    "https://www.linkedin.com/company/sydney-automation-co/"
  ],
  "knowsAbout": ["C-Bus Programming", "Dynalite Repair", "DALI-2 Compliance", "Emergency Lighting", "Lighting Control", "Building Automation"]
}
</script>
"""

    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "test.html":
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Skip if already updated
                if 'Common Questions' in content:
                    continue

                # Add AEO FAQ section before footer if it doesn't exist
                if '</main>' in content or '<footer>' in content:
                    insert_point = content.find('</main>')
                    if insert_point == -1:
                        insert_point = content.find('<footer>')
                    
                    if insert_point > 0:
                        content = content[:insert_point] + aeo_faq_template + content[insert_point:]

                # Update meta description to include 2026 and ROI keywords if it's a service page
                if any(keyword in filename for keyword in ['led', 'energy', 'dali', 'compliance', 'cbus', 'dynalite']):
                    # Add ROI and energy savings keywords to meta description
                    old_meta = re.search(r'<meta name="description" content="([^"]*)"', content)
                    if old_meta:
                        old_desc = old_meta.group(1)
                        if 'ROI' not in old_desc and 'energy' not in old_desc.lower():
                            new_desc = old_desc.replace('Sydney', 'Sydney 2026').replace('.', ' with energy ROI and compliance support.')
                            content = content.replace(old_meta.group(0), f'<meta name="description" content="{new_desc}"')

                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            except Exception as e:
                pass  # Skip files with encoding issues

if __name__ == "__main__":
    add_seo_enhancements()
