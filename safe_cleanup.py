import os

# 1. Read the exact string to remove from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- AI Assistant Widget -->'
end_marker = '</script>\n<script src="/chatbot.js"></script>'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    # find the end of the </script> tag before chatbot.js
    end_idx = content.find(end_marker)
    
    # The string to remove is exactly from start_marker to the start of end_marker
    to_remove = content[start_idx:end_idx + 9] # include </script>
    
    # 2. Iterate through all html files and do a simple string replace
    count = 0
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as fh:
                        file_content = fh.read()
                except:
                    continue
                
                if to_remove in file_content:
                    new_content = file_content.replace(to_remove, '')
                    with open(filepath, 'w', encoding='utf-8') as fh:
                        fh.write(new_content)
                    count += 1
    
    print(f"Safely removed old AI widget from {count} files.")
else:
    print("Could not find the markers in index.html")
