#!/usr/bin/env python3
"""Fix canonical tags, add missing canonicals and OG tags - TRACKED FILES ONLY."""
import subprocess
import re
import os

SITE = "https://sydneyautomationco.com.au"

# Get only tracked HTML files
result = subprocess.run(
    ["git", "ls-files", "--cached", "*.html"],
    capture_output=True, text=True, check=True
)
tracked = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
print(f"Processing {len(tracked)} tracked HTML files...")

fixed_wrong_canonical = 0
added_canonical = 0
added_og = 0
errors = []

for filepath in tracked:
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            html = f.read()

        original = html
        fname = os.path.basename(filepath)

        # Derive correct slug from filename
        slug = fname.replace(".html", "")

        # --- Fix wrong canonical tags ---
        canonical_pattern = re.compile(
            r'<link\s+rel="canonical"\s+href="([^"]+)"', re.IGNORECASE
        )
        m = canonical_pattern.search(html)
        if m:
            current_url = m.group(1)
            expected_url = f"{SITE}/{slug}.html"
            if current_url != expected_url:
                # Wrong canonical - fix it
                html = html[:m.start(1)] + expected_url + html[m.end(1):]
                fixed_wrong_canonical += 1
        else:
            # --- Add missing canonical tag ---
            canonical_tag = f'<link rel="canonical" href="{SITE}/{slug}.html">'
            # Insert after <title> tag or after </title>
            title_match = re.search(r'</title>', html, re.IGNORECASE)
            if title_match:
                insert_pos = title_match.end()
                # Skip any whitespace/newline after </title>
                while insert_pos < len(html) and html[insert_pos] in '\r\n ':
                    insert_pos += 1
                html = html[:insert_pos] + '\n    ' + canonical_tag + '\n' + html[insert_pos:]
                added_canonical += 1
            else:
                # No title tag - insert after </head> or before <body
                head_match = re.search(r'</head>', html, re.IGNORECASE)
                if head_match:
                    html = html[:head_match.start()] + '    ' + canonical_tag + '\n' + html[head_match.start():]
                    added_canonical += 1
                else:
                    errors.append(f"{filepath}: no </title> or </head> found")

        # --- Add OG tags if missing ---
        og_tags = [
            f'<meta property="og:title"',
            f'<meta property="og:description"',
            f'<meta property="og:url"',
            f'<meta property="og:type"',
            f'<meta property="og:site_name"',
        ]

        has_og = any(tag in html for tag in og_tags)
        if not has_og:
            # Extract title for og:title
            title_m = re.search(r'<title>([^<]+)</title>', html, re.IGNORECASE)
            page_title = title_m.group(1).strip() if title_m else slug.replace("-", " ").title()

            # Extract meta description for og:description
            desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html, re.IGNORECASE)
            page_desc = desc_m.group(1).strip() if desc_m else f"Professional C-Bus and Dynalite services in Sydney."

            og_block = f'''    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <meta property="og:url" content="{SITE}/{slug}.html">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Sydney Automation Co">'''

            # Insert after canonical tag or after </title>
            canonical_m = re.search(r'<link\s+rel="canonical"[^>]*>', html, re.IGNORECASE)
            if canonical_m:
                insert_pos = canonical_m.end()
                html = html[:insert_pos] + '\n' + og_block + html[insert_pos:]
                added_og += 1
            else:
                # Insert after </title>
                title_m2 = re.search(r'</title>', html, re.IGNORECASE)
                if title_m2:
                    insert_pos = title_m2.end()
                    while insert_pos < len(html) and html[insert_pos] in '\r\n ':
                        insert_pos += 1
                    html = html[:insert_pos] + '\n' + og_block + '\n' + html[insert_pos:]
                    added_og += 1

        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

    except Exception as e:
        errors.append(f"{filepath}: {e}")

print(f"\nResults:")
print(f"  Fixed wrong canonicals: {fixed_wrong_canonical}")
print(f"  Added missing canonicals: {added_canonical}")
print(f"  Added OG tags: {added_og}")
print(f"  Errors: {len(errors)}")
for err in errors[:10]:
    print(f"    {err}")
