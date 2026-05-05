import os, re

index_path = 'index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    NEW_BUTTON_CSS = """
  .btn-primary {
    padding: 22px 52px !important;
    font-size: 22px !important;
    font-weight: 900 !important;
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
    # Replace or Inject
    if '/* PREMIUM UI BOOSTERS */' in html:
        html = html.replace('/* PREMIUM UI BOOSTERS */', '/* PREMIUM UI BOOSTERS */\n' + NEW_BUTTON_CSS)
    else:
        if '</head>' in html:
            html = html.replace('</head>', f'<style>{NEW_BUTTON_CSS}</style>\n</head>')

    # Increment cache buster
    html = html.replace('?v=2026-05-06-01-34', '?v=2026-05-06-01-35')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Orange buttons supersized (v2).")
