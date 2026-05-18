with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# find marquee start
mq_start = -1
mq_end = -1
hero_start = -1
hero_end = -1

for i, line in enumerate(lines):
    if "<!-- INFINITE BRAND MARQUEE -->" in line:
        mq_start = i
    if mq_start != -1 and mq_end == -1 and '</div>' in line and i > mq_start + 10:
        if "    </div>" in line and "</div>" in lines[i-1]: # heuristic to find end of marquee wrapper
            # wait, it's safer to count divs
            pass
            
# A better way to swap the two blocks is to find their exact line numbers.
# I will print the line numbers and then do a multi_replace_file_content with correct target content.
for i, line in enumerate(lines):
    if "<!-- INFINITE BRAND MARQUEE -->" in line: print(f"MQ START: {i}")
    if "<!-- HERO -->" in line: print(f"HERO START: {i}")
    if "<!-- TRUST BAR -->" in line: print(f"TRUST START: {i}")
