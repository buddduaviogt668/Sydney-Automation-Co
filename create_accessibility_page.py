import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header (everything up to and including <div class="page">)
header_match = re.search(r'(.*?<div class="page">)', html, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract footer (from the footer tag onwards)
footer_match = re.search(r'(<footer.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Clean header for accessibility page
header = header.replace(
    '<title>About George Skarmoutsos',
    '<title>Accessibility Statement'
)
header = re.sub(
    r'<meta content="[^"]*" name="description"\s*/?>',
    '<meta content="Accessibility commitment for Sydney Automation Co. website." name="description" />',
    header,
    count=1
)

accessibility_content = """
<div class="hero"><div class="container">
<div class="tag">Accessibility</div>
<h1>Accessibility <span class="accent">Statement</span></h1>
<p class="lead">Sydney Automation Co. is committed to ensuring digital accessibility for people of all abilities. We continually improve the user experience for everyone and apply the relevant accessibility standards.</p>
</div></div>

<div class="section"><div class="container" style="max-width:800px;margin:0 auto">

<h2>Our Commitment</h2>
<p>We strive to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 at the AA level. These guidelines explain how to make web content more accessible for people with disabilities and more user-friendly for everyone.</p>

<h2>Measures We Take</h2>
<ul style="color:#a8c0e0;line-height:2;margin-bottom:32px;padding-left:24px">
<li>Semantic HTML structure with proper heading hierarchy</li>
<li>Descriptive alt text for all meaningful images</li>
<li>Sufficient colour contrast ratios across all text elements</li>
<li>Keyboard navigable interface with visible focus indicators</li>
<li>ARIA labels on interactive elements where appropriate</li>
<li>Responsive design that scales across all device sizes</li>
<li>Clear, readable typography using the Barlow font family</li>
</ul>

<h2>Known Limitations</h2>
<p>While we strive for full WCAG 2.1 AA compliance, some content may not yet fully meet all criteria. We are actively working to address these areas, including:</p>
<ul style="color:#a8c0e0;line-height:2;margin-bottom:32px;padding-left:24px">
<li>Some older service pages may have decorative images without alt text</li>
<li>PDF documents linked from this site may not be fully accessible</li>
</ul>

<h2>Feedback</h2>
<p>We welcome your feedback on the accessibility of the Sydney Automation Co. website. If you encounter any accessibility barriers or have suggestions for improvement, please contact us:</p>
<ul style="color:#a8c0e0;line-height:2;margin-bottom:32px;padding-left:24px">
<li><strong>Phone:</strong> <a href="tel:0422469739" style="color:#f07020">0422 469 739</a></li>
<li><strong>Email:</strong> <a href="mailto:service@sydneyautomationco.com.au" style="color:#f07020">service@sydneyautomationco.com.au</a></li>
</ul>

<h2>Standards Applied</h2>
<p>This website aims to conform to:</p>
<ul style="color:#a8c0e0;line-height:2;margin-bottom:32px;padding-left:24px">
<li>Web Content Accessibility Guidelines (WCAG) 2.1 Level AA</li>
<li>Disability Discrimination Act 1992 (Cth) — Australia</li>
<li>Web Accessibility National Transition Strategy (NTS)</li>
</ul>

<p style="color:#4a6a9a;font-size:14px;margin-top:48px">This statement was last updated in May 2026.</p>

</div></div>
</div>
"""

with open('accessibility.html', 'w', encoding='utf-8') as f:
    f.write(header + accessibility_content + footer)

print("Created accessibility.html")
