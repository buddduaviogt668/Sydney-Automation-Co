# -*- coding: utf-8 -*-
"""Promote Projects to its own nav item site-wide.

Desktop:
  1. Insert a "Projects" dropdown between Clients and Resources.
  2. Remove the standalone top-level Products link (Products stays in the
     Services mega-menu; added there on pages that lacked it).

Mobile:
  3. Move "Projects" out of the Resources section into its own
     "Projects & Case Studies" section.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

DESKTOP_DROPDOWN = """<div class="nav-dd" id="dd-projects">
  <button class="nav-dd-trigger">Projects</button>
  <div class="nav-dd-panel right">
    <span class="dd-label">Featured Case Studies</span>
    <a href="/case-study-tank-stream-labs">Tank Stream Labs, 333 Kent St</a>
    <a href="/case-study-winten-property-group">Winten Property Group</a>
    <a href="/case-study-kebia-importex-ingleburn">Kebia Importex, Ingleburn</a>
    <a href="/case-study-nsw-planning-the-rocks-lighting-automation">NSW Planning, The Rocks</a>
    <div class="dd-divider"></div>
    <a href="/projects">All Projects</a>
  </div>
</div>
"""

MOBILE_SECTION = ('<div class="mob-section"> '
                  '<div class="mob-section-title">Projects &amp; Case Studies</div>'
                  '<a href="/projects">All Projects</a> '
                  '<a href="/case-study-tank-stream-labs">Tank Stream Labs</a> '
                  '<a href="/case-study-winten-property-group">Winten Property Group</a> '
                  '<a href="/case-study-kebia-importex-ingleburn">Kebia Importex</a> '
                  '</div> ')

DESKTOP_INSERT = re.compile(
    r'(?:(<!--\s*RESOURCES\s*-->)\s*)?(<div class="nav-dd" id="dd-resources">)')

TOP_PRODUCTS_REMOVE = re.compile(
    r'<a href="/products">Products</a>\s*(<a href="/contact(?:\.html)?"[^>]*>)')

MEGA_PRODUCTS_ADD = re.compile(
    r'(<a href="/facilities-lighting-maintenance-sydney">Facilities Maintenance</a>)</div>')

MOBILE_PROJECTS_REMOVE = re.compile(r'\s*<a href="/projects">Projects</a>\s*')

MOBILE_INSERT = re.compile(
    r'(</div>\s*)(<div class="mob-section">\s*<div class="mob-section-title">Resources</div>)')


def desktop_insert(content):
    def rep(m):
        comment = m.group(1)
        tag = m.group(2)
        if comment:
            return DESKTOP_DROPDOWN + comment + ' ' + tag
        return DESKTOP_DROPDOWN + tag
    return DESKTOP_INSERT.sub(rep, content)


def top_products_remove(content):
    return TOP_PRODUCTS_REMOVE.sub(r'\1', content)


def mega_products_add(content):
    return MEGA_PRODUCTS_ADD.sub(r'\1<a href="/products">Products</a></div>', content)


def mobile_remove(content):
    i = content.find('mob-section-title">Resources')
    j = content.find('mob-cta', i if i != -1 else 0)
    if i == -1 or j == -1:
        return content
    region = content[i:j]
    region = MOBILE_PROJECTS_REMOVE.sub(' ', region)
    return content[:i] + region + content[j:]


def mobile_insert(content):
    return MOBILE_INSERT.sub(lambda m: m.group(1) + ' ' + MOBILE_SECTION + m.group(2), content)


def main():
    html_files = sorted(
        f for f in os.listdir(ROOT)
        if f.lower().endswith('.html') and os.path.isfile(os.path.join(ROOT, f)))

    stats = {
        'desktop_insert': 0,
        'top_products_removed': 0,
        'mega_products_added': 0,
        'mobile_removed': 0,
        'mobile_insert': 0,
        'melbourne_mega_added': 0,
    }

    for name in html_files:
        path = os.path.join(ROOT, name)
        with open(path, 'r', encoding='utf-8', errors='ignore', newline='') as fh:
            content = fh.read()
        original = content
        changed = False

        if 'id="dd-resources"' in content:
            content = desktop_insert(content)
            if content != original:
                stats['desktop_insert'] += 1
                changed = True

        before = content
        content = top_products_remove(content)
        if content != before:
            stats['top_products_removed'] += 1
            changed = True

        if '<a href="/products">Products</a></div>' not in content:
            before = content
            content = mega_products_add(content)
            if content != before:
                stats['mega_products_added'] += 1
                changed = True

        before = content
        content = mobile_remove(content)
        if content != before:
            stats['mobile_removed'] += 1
            changed = True

        before = content
        content = mobile_insert(content)
        if content != before:
            stats['mobile_insert'] += 1
            changed = True

        if name == 'melbourne-dali-lighting-control-compliance.html':
            anchor = '<a href="/services">Dynalite Maintenance</a></div></div></div>'
            replacement = ('<a href="/services">Dynalite Maintenance</a>'
                           '<a href="/products">Products</a></div></div></div>')
            if anchor in content:
                content = content.replace(anchor, replacement, 1)
                stats['melbourne_mega_added'] += 1
                changed = True

        if changed:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(content)

    print('=== summary ===')
    for k, v in stats.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
