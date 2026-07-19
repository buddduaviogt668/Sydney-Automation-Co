import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]
issues = []

for file in files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check robots meta
    has_robots = re.search(r'<meta[^>]*name=["\']robots["\'][^>]*content=["\']index, follow["\'][^>]*>', content, re.IGNORECASE) or \
                 re.search(r'<meta[^>]*content=["\']index, follow["\'][^>]*name=["\']robots["\'][^>]*>', content, re.IGNORECASE)
    
    # Check canonical
    has_canonical = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'][^"\']+["\'][^>]*>', content, re.IGNORECASE)
    
    if not has_robots or not has_canonical:
        issues.append({
            'file': file,
            'missing_robots': not has_robots,
            'missing_canonical': not has_canonical
        })

if not issues:
    print("All pages have robots and canonical tags.")
else:
    print(f"Found {len(issues)} pages with missing tags:")
    for issue in issues:
        print(f"- {issue['file']}: {'Robots' if issue['missing_robots'] else ''} {'Canonical' if issue['missing_canonical'] else ''}")
