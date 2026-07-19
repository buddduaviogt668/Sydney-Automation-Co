import os
import glob
import re

print("Starting global feature injection (AI Bot + Exit Intent) and Blog formatting...")

new_features = """
<!-- AI Assistant Widget -->
<style>
.sac-ai-widget { position: fixed; bottom: 30px; right: 30px; z-index: 9999; display: flex; flex-direction: column; align-items: flex-end; font-family: 'Inter', sans-serif; }
.sac-ai-toggle { width: 60px; height: 60px; background: linear-gradient(135deg, #f07020, #ff8c42); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(240, 112, 32, 0.4); cursor: pointer; transition: transform 0.3s; }
.sac-ai-toggle:hover { transform: scale(1.1); }
.sac-ai-toggle svg { color: white; width: 30px; height: 30px; }
.sac-ai-chat-window { display: none; width: 350px; height: 450px; background: #112240; border: 1px solid rgba(240, 112, 32, 0.3); border-radius: 16px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); overflow: hidden; flex-direction: column; }
.sac-ai-chat-header { background: #0a192f; padding: 15px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); display: flex; justify-content: space-between; align-items: center; }
.sac-ai-chat-header h4 { margin: 0; color: #ccd6f6; font-size: 16px; font-weight: 600; }
.sac-ai-close { color: #8892b0; cursor: pointer; font-size: 20px; }
.sac-ai-chat-body { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
.sac-ai-msg { max-width: 80%; padding: 12px 16px; border-radius: 12px; font-size: 14px; line-height: 1.5; }
.sac-ai-msg.bot { background: rgba(255, 255, 255, 0.05); color: #ccd6f6; align-self: flex-start; border-bottom-left-radius: 4px; }
.sac-ai-msg.user { background: rgba(240, 112, 32, 0.15); color: #fff; border: 1px solid rgba(240, 112, 32, 0.3); align-self: flex-end; border-bottom-right-radius: 4px; }
.sac-ai-chat-input { padding: 15px; background: rgba(0, 0, 0, 0.2); border-top: 1px solid rgba(255, 255, 255, 0.05); display: flex; gap: 10px; }
.sac-ai-chat-input input { flex: 1; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); padding: 10px 15px; border-radius: 20px; color: white; outline: none; }
.sac-ai-chat-input button { background: #f07020; color: white; border: none; border-radius: 20px; padding: 0 15px; cursor: pointer; font-weight: 600; }
</style>
<div class="sac-ai-widget">
  <div class="sac-ai-chat-window" id="sacAiWindow">
    <div class="sac-ai-chat-header"><h4>George - AI Virtual Assistant</h4><span class="sac-ai-close" onclick="document.getElementById('sacAiWindow').style.display='none'">×</span></div>
    <div class="sac-ai-chat-body" id="sacAiBody"><div class="sac-ai-msg bot">Hi! I'm the Sydney Automation Co virtual assistant. Are you having an issue with a C-Bus or Dynalite system today?</div></div>
    <div class="sac-ai-chat-input"><input type="text" id="sacAiInput" placeholder="Type your question..." onkeypress="if(event.key === 'Enter') sendSacMsg()"><button onclick="sendSacMsg()">Send</button></div>
  </div>
  <div class="sac-ai-toggle" onclick="toggleSacAi()"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
</div>

<!-- Exit Intent Popup -->
<style>
.sac-exit-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 10, 20, 0.85); backdrop-filter: blur(5px); z-index: 10000; display: none; align-items: center; justify-content: center; }
.sac-exit-modal { background: #112240; border: 1px solid rgba(240, 112, 32, 0.3); padding: 40px; border-radius: 20px; max-width: 500px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.5); position: relative; }
.sac-exit-close { position: absolute; top: 15px; right: 20px; color: #8892b0; font-size: 24px; cursor: pointer; }
.sac-exit-modal h2 { color: #ccd6f6; margin-bottom: 15px; font-size: 28px; }
.sac-exit-modal h2 span { color: #f07020; }
.sac-exit-modal p { color: #8892b0; margin-bottom: 25px; line-height: 1.6; }
.sac-exit-form input { width: 100%; padding: 15px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; margin-bottom: 15px; color: white; box-sizing: border-box; }
.sac-exit-form button { width: 100%; padding: 15px; background: #f07020; color: white; border: none; border-radius: 8px; font-weight: 600; font-size: 16px; cursor: pointer; transition: background 0.3s; }
.sac-exit-form button:hover { background: #ff8c42; }
</style>
<div class="sac-exit-overlay" id="sacExitPopup">
  <div class="sac-exit-modal">
    <span class="sac-exit-close" onclick="document.getElementById('sacExitPopup').style.display='none'">×</span>
    <h2>Wait! Before you go... <br><span>Don't rip out your C-Bus.</span></h2>
    <p>Many electricians will tell you to completely replace a failing lighting system. Let us give you a free second opinion. Enter your details and we will call you back within 15 minutes.</p>
    <div class="sac-exit-form"><input type="text" placeholder="Your Name" id="exitName"><input type="tel" placeholder="Phone Number" id="exitPhone"><button onclick="submitExit()">Get Free Second Opinion</button></div>
  </div>
</div>

<script>
function toggleSacAi() { const win = document.getElementById('sacAiWindow'); win.style.display = win.style.display === 'flex' ? 'none' : 'flex'; }
function sendSacMsg() {
  const input = document.getElementById('sacAiInput'); const body = document.getElementById('sacAiBody');
  if(!input.value.trim()) return;
  const uDiv = document.createElement('div'); uDiv.className = 'sac-ai-msg user'; uDiv.textContent = input.value; body.appendChild(uDiv);
  input.value = ''; body.scrollTop = body.scrollHeight;
  setTimeout(() => {
    const bDiv = document.createElement('div'); bDiv.className = 'sac-ai-msg bot'; bDiv.innerHTML = "Thanks for reaching out! Our AI assistant is currently being upgraded. For immediate assistance with C-Bus or Dynalite, please call George directly at <a href='tel:0422469739' style='color:#f07020'>0422 469 739</a>.";
    body.appendChild(bDiv); body.scrollTop = body.scrollHeight;
  }, 1000);
}
let exitTriggered = false;
document.addEventListener('mouseleave', (e) => { if(e.clientY < 0 && !exitTriggered) { exitTriggered = true; document.getElementById('sacExitPopup').style.display = 'flex'; }});
function submitExit() { document.getElementById('sacExitPopup').innerHTML = "<div class='sac-exit-modal'><h2>Request Sent!</h2><p>George will call you back shortly.</p><button onclick=\\"document.getElementById('sacExitPopup').style.display='none'\\" style='padding:10px 20px; background:#f07020; border:none; border-radius:5px; color:white; cursor:pointer;'>Close</button></div>"; }
</script>
</body>
"""

blog_css = """
<style>
.blog-post-content { max-width: 800px; margin: 0 auto; padding: 40px 20px; background: rgba(0, 20, 40, 0.7); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; margin-top: -60px; position: relative; z-index: 10; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
.blog-post-content p { font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem; color: #a8c0e0; }
.blog-post-content h2 { color: #fff; margin-top: 2rem; margin-bottom: 1rem; font-size: 2rem; }
.blog-post-content h3 { color: #f07020; margin-top: 1.5rem; margin-bottom: 1rem; font-size: 1.5rem; }
.blog-post-content ul { margin-bottom: 1.5rem; padding-left: 20px; }
.blog-post-content li { color: #a8c0e0; font-size: 1.1rem; line-height: 1.8; margin-bottom: 0.5rem; }
</style>
"""

# Process all files
modified = 0
for filepath in glob.glob("*.html"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        
        # 1. Inject AI Bot + Exit Intent
        if 'class="sac-ai-widget"' not in content and '</body>' in content:
            content = content.replace('</body>', new_features)
            changed = True
            
        # 2. Fix older blogs formatting
        if filepath.startswith('blog-') and filepath != 'blog.html':
            if 'blog-post-content' not in content:
                # Wrap the main body in blog-post-content if it's missing (heuristically after hero)
                # First, ensure blog_css is added
                if '<style>.blog-post-content' not in content:
                    content = content.replace('</head>', blog_css + '\n</head>')
                    changed = True
                    
                # A very basic wrapping heuristic: if it has container but not blog-post-content
                # we'll look for `<div class="container">` that occurs after `<div class="hero">`
                if '<div class="container">' in content and '<div class="hero">' in content:
                    # Let's just wrap the text inside container with blog-post-content
                    content = re.sub(r'(<div class="container">)(\s*<h2)', r'\1\n<div class="blog-post-content">\2', content)
                    if '<div class="blog-post-content">' in content:
                        content = content.replace('<!-- End Content -->', '</div><!-- End Content -->')
                        if '</div><!-- End Content -->' not in content:
                            # fallback close
                            content = re.sub(r'(</section>|</div>\s*<footer)', r'</div>\1', content, count=1)
                    changed = True
                    
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified += 1
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Injected features and fixed blog formatting in {modified} files.")
