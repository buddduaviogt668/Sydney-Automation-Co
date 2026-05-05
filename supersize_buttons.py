import os

index_path = 'index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Update the PREMIUM UI BOOSTERS CSS for btn-primary
    NEW_BUTTON_CSS = """
  .btn-primary {
    padding: 20px 48px !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 15px rgba(240, 112, 32, 0.4) !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
  }
  .btn-primary:hover {
    box-shadow: 0 10px 30px rgba(240, 112, 32, 0.6) !important;
    transform: scale(1.05) !important;
  }
"""
    # Replace the old btn-primary style in the boosters
    if '.btn-primary {' in html:
        # Simple replacement for the existing btn-primary block in my injected CSS
        html = re.sub(r'\.btn-primary \{.*?\}', NEW_BUTTON_CSS, html, flags=re.DOTALL)
    else:
        # If not found, inject it into the head
        if '</head>' in html:
            html = html.replace('</head>', f'<style>{NEW_BUTTON_CSS}</style>\n</head>')

    # Increment cache buster to force the new CSS
    html = html.replace('?v=2026-05-06-01-32', '?v=2026-05-06-01-34')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Orange buttons supersized.")
