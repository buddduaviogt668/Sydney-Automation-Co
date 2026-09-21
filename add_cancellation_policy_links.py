import os
import re

HTML_DIR = "."

NAV_COMPANY_LINK = '<a href="/booking-and-cancellation-policy">Booking &amp; Cancellation Policy</a>'
MOB_NAV_LINK = '<a href="/booking-and-cancellation-policy">Booking &amp; Cancellation Policy</a>'

# Patterns
# 1) Nav Resources -> Company dropdown: after "George's Background"
re_nav_geo = re.compile(
    r'(?P<indent>^\s*)<a href="/4-years-building-facilities-management-jll-pbmg"[^>]*>.*?</a>',
    re.MULTILINE
)
# 2) Mobile nav Resources section: About link immediately followed by the section closing div
re_mob_about = re.compile(
    r'(<a href="/about">About</a>\n\s*)(</div>)'
)
# 3) Footer-copy: the sitemap anchor; mirror its style attribute
re_sitemap = re.compile(r'(<a href="/sitemap\.xml"[^>]*>)([^<]*)(</a>)')
re_style = re.compile(r'style="[^"]*"')
# 3b) Fallback footer-copy: insert after the privacy-policy anchor (pages without a footer sitemap link)
re_privacy = re.compile(r'(<a href="/privacy-policy"[^>]*>)[^<]*(</a>)')


def footer_link_for(anchor_match):
    attrs = ''
    full_anchor = anchor_match.group(0)
    m = re_style.search(full_anchor)
    if m:
        attrs += ' ' + m.group(0)
    return '<a href="/booking-and-cancellation-policy"' + attrs + '>Booking &amp; Cancellation Policy</a>'


def add_footer(content):
    new, count = re_sitemap.subn(
        lambda m: m.group(0) + '\n' + footer_link_for(m),
        content
    )
    if count == 0:
        new = re_privacy.sub(
            lambda m: m.group(0) + '\n' + footer_link_for(m),
            new
        )
    return new


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
        except OSError:
            skipped.append(fpath)
            continue

        original = content

        has_policy_link = '/booking-and-cancellation-policy' in content
        footer_region = re.search(r'class="footer-copy".*?</footer>', content, re.S)
        footer_missing = bool(footer_region) and '/booking-and-cancellation-policy' not in footer_region.group(0)

        # Nav Company dropdown + mobile nav only if not already added
        if not has_policy_link:
            content = re_nav_geo.sub(
                lambda m: m.group(0) + '\n' + m.group('indent') + NAV_COMPANY_LINK,
                content
            )
            content = re_mob_about.sub(
                lambda m: m.group(1) + m.group(2) + '\n    ' + MOB_NAV_LINK,
                content
            )

        # Footer-copy
        if footer_missing:
            content = add_footer(content)

        # Homepage (index.html): noscript crawl-anchor block
        if fname == 'index.html' and '/booking-and-cancellation-policy' not in content.replace("  |  \n    <a href=\"/booking-and-cancellation-policy\" style=\"color:#f07020\">Booking &amp; Cancellation Policy</a>", ""):
            content = content.replace(
                '    <a href="/privacy-policy" style="color:#f07020">Privacy Policy</a>',
                '    <a href="/privacy-policy" style="color:#f07020">Privacy Policy</a>  |  \n    <a href="/booking-and-cancellation-policy" style="color:#f07020">Booking &amp; Cancellation Policy</a>'
            )

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated.append(fpath)
        else:
            skipped.append(fpath)

print("Updated: %d files" % len(updated))
print("Skipped: %d files" % len(skipped))
