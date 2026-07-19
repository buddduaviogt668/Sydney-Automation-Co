import os
import glob

print("Starting AI Bot position and name fix...")
modified = 0

for filepath in glob.glob("*.html"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        
        # 1. Move widget to the left
        if '.sac-ai-widget { position: fixed; bottom: 30px; right: 30px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-end;' in content:
            content = content.replace(
                '.sac-ai-widget { position: fixed; bottom: 30px; right: 30px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-end;',
                '.sac-ai-widget { position: fixed; bottom: 30px; left: 30px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-start;'
            )
            changed = True
            
        # 2. Change name
        if '<h4>George - AI Virtual Assistant</h4>' in content:
            content = content.replace('<h4>George - AI Virtual Assistant</h4>', '<h4>Sparky - The AI Diagnostics Tech</h4>')
            changed = True
            
        # 3. Change response text
        if 'please call George directly at' in content:
            content = content.replace('please call George directly at', 'please call our human engineers directly at')
            changed = True
            
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified += 1
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Updated AI bot position and name in {modified} files.")
