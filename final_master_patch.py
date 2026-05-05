import os, re

bundle_path = 'bundle.js'
index_path = 'index.html'

if not os.path.exists(bundle_path):
    print("ERROR: bundle.js not found")
    exit(1)

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. REAL REVIEWS ARRAY (Exactly as they appear on your site)
REAL_REVIEWS = """
  var TESTIMONIALS = [
    { name: "Verified Client", text: "Literally a lifesaver... George came out in 24 hours, diagnosed the problem with the CBUS system that two previous 'specialists' couldn't — fixed it — and then checked in two days later to make sure it was still working. This is your guy for all CBUS and installation works." },
    { name: "Verified Client", text: "Highly recommended! George was amazing — came out at last notice when all our office lights went on the blink, found the problem in our C-Bus system, rush-ordered the parts, and had everything back up within no time. We now have him as our go-to expert for all things C-Bus." },
    { name: "Verified Client", text: "Extremely happy with the C-Bus automation services. They helped repair and reprogram our Clipsal C-Bus lighting system which had ongoing faults that previous electricians couldn't resolve. Very responsive, explained the issues clearly, and went the extra mile." },
    { name: "Verified Client", text: "Honest and reliable C-Bus installer in Sydney. Extremely knowledgeable and took the time to explain our C-Bus options clearly without rushing us. The quality of the installation and products was excellent and we're very happy with the end result." },
    { name: "Verified Client", text: "Fantastic service. George resolved all issues and reprogrammed our Clipsal C-Bus system with custom options — above and beyond our expectations. Great efficient work with sharp pricing. Highly recommended!" },
    { name: "Verified Client", text: "Verified Client", text: "I recently hired Sydney Automation to upgrade our home with a fully automated lighting system and the experience was fantastic! Professional, knowledgeable, and customised the system to perfectly suit our needs. Highly recommended." },
    { name: "Verified Client", text: "George was really helpful in my system set up. As someone who knew nothing about this space, he guided me to the right programs and got it all installed hassle free. I've since recommended him to several friends and family. 10/10." },
    { name: "Verified Client", text: "Sydney Automation Co. provides outstanding smart lighting solutions, combining impressive technology with excellent customer service. I highly recommend them to anyone considering office automation!" },
    { name: "Verified Client", text: "During a recent home renovation George and the team fitted out my media room. We couldn't be happier with the all round service — the lighting set up in particular is incredible!" },
    { name: "Verified Client", text: "George was highly professional and prompt in fixing the CBUS issues we had downstairs — very knowledgeable, highly recommended." }
  ];
"""
content = re.sub(r'var TESTIMONIALS = \[.*?\];', REAL_REVIEWS, content, flags=re.DOTALL)

# 2. PROJECTS PREVIEW JSX (Replacing Instagram)
PROJECTS_JSX = """
      /* PROJECTS PREVIEW */
      /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "#060b14", padding: "120px 0" }, children: [
        /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "container", style: { textAlign: "center", marginBottom: 56 }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "tag", children: "Recent Work" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", { style: { fontSize: 42, fontWeight: 900, marginBottom: 12 }, children: "Project Highlights" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { color: "#a8c0e0", fontSize: 16 }, children: "Expert automation solutions delivered across commercial and prestige residential sites." })
        ] }),
        /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "container", children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 32 }, children: [
          { title: "Winten Property Group", suburb: "North Sydney", img: "/winten-11-winten-reception.jpg", tag: "C-Bus Upgrade" },
          { title: "WSU Parramatta", suburb: "Parramatta", img: "/wsu-05-teaching-studio-in-use.jpg", tag: "Blind Control" },
          { title: "Kebia Importex", suburb: "Kingsgrove", img: "/kebia-01.jpg", tag: "SpaceLogic Relay" },
          { title: "Uluru Meeting Place", suburb: "Yulara, NT", img: "/og-image.jpg", tag: "Dynalite (Coming Soon)" }
        ].map((p, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "card", style: { overflow: "hidden" }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", { src: p.img, style: { width: "100%", height: 200, objectFit: "cover" } }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { padding: 24 }, children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { color: "#f07020", fontSize: 12, fontWeight: 700, textTransform: "uppercase", marginBottom: 8 }, children: p.tag }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", { style: { fontSize: 20, marginBottom: 4 }, children: p.title }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { color: "#a8c0e0", fontSize: 14 }, children: p.suburb })
          ] })
        ] }, i)) }) }),
        /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { textAlign: "center", marginTop: 48 }, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", { className: "btn-outline", onClick: () => nav("projects"), children: "View All Projects" }) })
      ] })
"""

# Finding the Instagram target by searching for the "tag", children: "Instagram" line and its parent
# Using a simpler target for replacement
INSTA_TARGET = '/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { id: "instagram-feed" })'
# We'll find the section start before it
if INSTA_TARGET in content:
    # Go back to find the section start
    insta_start = content.rfind('/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section"', 0, content.find(INSTA_TARGET))
    insta_end = content.find(') })', content.find(INSTA_TARGET)) + 4
    if insta_start != -1 and insta_end != -1:
        content = content[:insta_start] + PROJECTS_JSX + content[insta_end:]
        print("SUCCESS: Replaced Instagram with Projects")

# Save bundle.js
with open(bundle_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. CLEAN index.html (Remove static reviews)
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Remove the "WHAT CLIENTS SAY" section
    # It starts around line 760 usually
    html = re.sub(r'<!-- Testimonials -->.*?<!-- End Testimonials -->', '', html, flags=re.DOTALL)
    # If comments aren't there, use text anchors
    html = re.sub(r'<section[^>]*>.*?WHAT CLIENTS SAY.*?10 five-star Google reviews.*?<\/section>', '', html, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: Removed static reviews from index.html")
