import os
import re

# The full Premium Carousel HTML + CSS + JS block
CAROUSEL_BLOCK = """<!-- ===== PREMIUM TESTIMONIALS CAROUSEL ===== -->
<section id="testimonials" style="background:#0e1f3d;padding:80px 0;overflow:hidden;border-top:1px solid rgba(240,112,32,0.1);">
  <div class="container" style="max-width:1200px;margin:0 auto;padding:0 24px;">
    <div style="text-align:center;margin-bottom:48px;">
      <span style="color:#f07020;font-weight:700;letter-spacing:3px;text-transform:uppercase;font-size:12px;display:block;margin-bottom:12px;">CLIENT REVIEWS</span>
      <h2 style="color:#fff;font-size:clamp(32px,5vw,46px);margin:0;font-family:'Barlow Condensed',sans-serif;font-weight:900;line-height:1.1;">TRUSTED ACROSS SYDNEY</h2>
      <div style="width:60px;height:4px;background:#f07020;margin:24px auto;"></div>
    </div>

    <div class="tm-viewport" style="position:relative;margin:0 -200vw;">
      <div id="tm-track" style="display:flex;gap:24px;padding:20px 200vw;overflow-x:auto;scroll-behavior:smooth;scroll-snap-type:x mandatory;scrollbar-width:none;-ms-overflow-style:none;">
        
        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Literally a lifesaver… George came out in 24 hours, diagnosed the problem with the CBUS system that two previous 'specialists' couldn't — fixed it — and then checked in two days later to make sure it was still working."</p>
          <div class="tm-footer">
            <div class="tm-author">Adam Ziino</div>
            <div class="tm-role">C-Bus Repair, Little Bay</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Highly recommended! George was amazing — came out at last notice when all our office lights went on the blink, found the problem in our C-Bus system, rush-ordered the parts, and had everything back up within no time."</p>
          <div class="tm-footer">
            <div class="tm-author">Phillipa Brown</div>
            <div class="tm-role">Winten Property Group — North Sydney</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Extremely happy with the C-Bus automation services. They helped repair and reprogram our Clipsal C-Bus lighting system which had ongoing faults that previous electricians couldn't resolve. Very responsive."</p>
          <div class="tm-footer">
            <div class="tm-author">Vasilios Tsopanas</div>
            <div class="tm-role">C-Bus Fault Finding, Marrickville</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Honest and reliable C-Bus installer in Sydney. Extremely knowledgeable and took the time to explain our C-Bus options clearly without rushing us. The quality of the installation was excellent."</p>
          <div class="tm-footer">
            <div class="tm-author">Helen Poulos</div>
            <div class="tm-role">Ask Allied Health — Earlwood</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Fantastic service. George resolved all issues and reprogrammed our Clipsal C-Bus system with custom options — above and beyond our expectations. Great efficient work with sharp pricing."</p>
          <div class="tm-footer">
            <div class="tm-author">Easyfix Electrics</div>
            <div class="tm-role">Commercial Client, Matraville</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"I recently hired Sydney Automation to upgrade our home with a fully automated lighting system and the experience was fantastic! Professional, knowledgeable, and customised the system perfectly."</p>
          <div class="tm-footer">
            <div class="tm-author">Tim Reyes</div>
            <div class="tm-role">Home Automation, Norwest</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"George was really helpful in my system set up. As someone who knew nothing about this space, he guided me to the right programs and got it all installed hassle free. 10/10."</p>
          <div class="tm-footer">
            <div class="tm-author">Imran Hamidi</div>
            <div class="tm-role">Laing + Simmons East Group — Potts Point</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"Sydney Automation Co. provides outstanding smart lighting solutions, combining impressive technology with excellent customer service. I highly recommend them for office automation!"</p>
          <div class="tm-footer">
            <div class="tm-author">Miro Krpelán</div>
            <div class="tm-role">Katalyst Facilities Management — Bondi Junction</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"During a recent home renovation George and the team fitted out my media room. We couldn't be happier with the all round service — the lighting set up in particular is incredible!"</p>
          <div class="tm-footer">
            <div class="tm-author">Jamie Patterson</div>
            <div class="tm-role">Residential Client, Lugarno</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"George was highly professional and prompt in fixing the CBUS issues we had downstairs — very knowledgeable, highly recommended."</p>
          <div class="tm-footer">
            <div class="tm-author">Robert Alvaro</div>
            <div class="tm-role">C-Bus Fault Finding, Maroubra</div>
          </div>
        </div>

        <div class="tm-card">
          <div class="tm-stars">★★★★★</div>
          <p class="tm-text">"George from Sydney Auto did a great job repairing & replacing our a C-Bus electrical relay and would highly recommend him and use him again."</p>
          <div class="tm-footer">
            <div class="tm-author">Jim Vassil</div>
            <div class="tm-role">Kebia Importex</div>
          </div>
        </div>

      </div>

      <div class="tm-controls">
        <button onclick="tmSlide(-1)" class="tm-btn">←</button>
        <button onclick="tmSlide(1)" class="tm-btn">→</button>
      </div>
    </div>

    <div style="text-align:center;margin-top:40px;">
      <a href="https://g.page/r/CQK7ChOgqNZ2EBM/review" target="_blank" class="tm-google-link">
        LEAVE A 5-STAR GOOGLE REVIEW
      </a>
    </div>
  </div>
</section>

<style>
  .tm-viewport { position: relative; width: 100%; }
  #tm-track::-webkit-scrollbar { display: none; }
  .tm-card {
    flex: 0 0 380px;
    scroll-snap-align: center;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 40px 32px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  }
  .tm-card:hover { background: rgba(255,255,255,0.06); border-color: rgba(240,112,32,0.3); transform: translateY(-5px); }
  .tm-stars { color: #f07020; font-size: 16px; letter-spacing: 4px; }
  .tm-text { color: #e2e8f0; font-size: 16px; line-height: 1.7; margin: 0; font-family: 'Barlow', sans-serif; font-style: italic; flex-grow: 1; }
  .tm-footer { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }
  .tm-author { font-weight: 800; color: #fff; font-size: 16px; font-family: 'Barlow Condensed', sans-serif; text-transform: uppercase; letter-spacing: 1px; }
  .tm-role { font-size: 13px; color: #a8c0e0; font-family: 'Barlow', sans-serif; margin-top: 4px; }
  .tm-controls { position: absolute; top: 50%; left: 0; right: 0; transform: translateY(-50%); display: flex; justify-content: space-between; padding: 0 20px; pointer-events: none; z-index: 10; }
  .tm-btn { width: 48px; height: 48px; background: #f07020; color: #fff; border: none; border-radius: 50%; font-size: 20px; cursor: pointer; pointer-events: auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(240,112,32,0.4); }
  .tm-google-link { display: inline-block; padding: 14px 32px; background: transparent; border: 2px solid #f07020; color: #f07020; text-decoration: none; font-weight: 800; font-family: 'Barlow Condensed', sans-serif; font-size: 14px; letter-spacing: 1px; border-radius: 50px; transition: all 0.3s; }
  .tm-google-link:hover { background: #f07020; color: #fff; }
  @media (max-width: 768px) { .tm-card { flex: 0 0 85vw; } .tm-controls { display: none; } }
</style>

<script>
  (function(){
    const track = document.getElementById('tm-track');
    let isPaused = false;
    window.tmSlide = function(d) {
      if(!track) return;
      const cardWidth = track.querySelector('.tm-card').offsetWidth + 24;
      track.scrollBy({ left: d * cardWidth, behavior: 'smooth' });
    };
    setInterval(() => {
      if(isPaused || !track) return;
      const cardWidth = track.querySelector('.tm-card').offsetWidth + 24;
      if (track.scrollLeft + track.offsetWidth >= track.scrollWidth - 10) { track.scrollTo({ left: 0, behavior: 'smooth' }); }
      else { track.scrollBy({ left: cardWidth, behavior: 'smooth' }); }
    }, 5000);
    track.addEventListener('mouseenter', () => isPaused = true);
    track.addEventListener('mouseleave', () => isPaused = false);
  })();
</script>
<!-- ===== /PREMIUM TESTIMONIALS CAROUSEL ===== -->"""

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. REMOVE PREVIOUS MARKED BLOCKS (Idempotency)
        content = re.sub(r'<!-- ===== PREMIUM TESTIMONIALS CAROUSEL ===== -->.*?<!-- ===== /PREMIUM TESTIMONIALS CAROUSEL ===== -->', '', content, flags=re.DOTALL)

        # 2. REMOVE LEGACY/UNMARKED TESTIMONIAL SECTIONS
        # a. Standard section id="testimonials"
        content = re.sub(r'<section id="testimonials".*?</section>', '', content, flags=re.DOTALL)
        
        # b. Homepage style legacy sections (div class="section" with "What Our Clients Say")
        content = re.sub(r'<!-- TESTIMONIALS -->.*?What Our <span class="accent">Clients Say</span>.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
        
        # c. Any section containing "What Our Clients Say"
        content = re.sub(r'<div class="section">\s*<div class="container">\s*<div class="section-header">\s*<h2>What Our <span class="accent">Clients Say</span></h2>.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

        # d. Catch-all for any tag with id="tm-track" that isn't already inside a marked block
        content = re.sub(r'<div[^>]*id="tm-track".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

        # 3. Update reviewCount to 11 in schema
        content = re.sub(r'("reviewCount":\s*)"\d+"', r'\1"11"', content)
        
        # 4. Add the new block before </body>
        if '</body>' in content:
            content = content.replace('</body>', CAROUSEL_BLOCK + '\n</body>')
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"ERROR processing {filepath}: {e}")
    return False

# Main rollout
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
count = 0
for f in html_files:
    if update_file(f):
        count += 1
        print(f"UPDATED: {f}")

print(f"DONE: Rolled out to {count} files.")
