with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_marquee_str = """    <!-- INFINITE BRAND MARQUEE -->
    <div class="marquee-wrapper" style="background: rgba(0, 20, 40, 0.6); border-bottom: 1px solid rgba(240,112,32,0.1); backdrop-filter: blur(10px);">
      <div class="marquee-content">
        <!-- Brand Set 1 -->
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #f07020;"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">CLIPSAL C-BUS</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #fff;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.9 1.2 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">SIGNIFY DYNALITE</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #3dcd58;"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">SCHNEIDER ELECTRIC</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #a8c0e0;"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">DALI ALLIANCE</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #f07020;"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">RAPIX LIGHTING</span>
        </div>
        
        <!-- Duplicated for seamless loop -->
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #f07020;"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">CLIPSAL C-BUS</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #fff;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.9 1.2 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">SIGNIFY DYNALITE</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #3dcd58;"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">SCHNEIDER ELECTRIC</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #a8c0e0;"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">DALI ALLIANCE</span>
        </div>
        <div class="marquee-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 12px; color: #f07020;"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
          <span style="font-weight:800; letter-spacing:1px; font-size:13px;">RAPIX LIGHTING</span>
        </div>
      </div>
    </div>
"""

new_marquee_lines = [line + "\n" for line in new_marquee_str.split("\n")]
# Remove the last empty newline from split if exists
if new_marquee_lines[-1] == "\n":
    new_marquee_lines = new_marquee_lines[:-1]

mq_start, hero_start, trust_start = 1442, 1491, 1530

pre_mq = lines[:mq_start]
hero_block = lines[hero_start:trust_start-1] # trust_start-1 because there's a style block or blank line before trust bar
# Wait, let's just grab exactly up to trust_start
hero_block = lines[hero_start:trust_start]

post_trust = lines[trust_start:]

new_lines = pre_mq + hero_block + new_marquee_lines + post_trust

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Swapped Marquee and Hero successfully.")
