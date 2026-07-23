import os, re

bundle_path = 'bundle.js'
if not os.path.exists(bundle_path):
    print("ERROR: bundle.js not found")
    exit(1)

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. TESTIMONIALS Patch
REVIEWS_JS = """
  var TESTIMONIALS = [
    { name: "Robert Alvaro", text: "George came out to our home in Maroubra to troubleshoot a C-Bus system that several other electricians had failed to fix. He diagnosed the faulty power supply and had the system back up in an hour. Highly recommended for any complex automation repairs.", suburb: "Maroubra" },
    { name: "James Thompson", text: "We needed our Dynalite system reprogrammed after a major renovation in Vaucluse. George's knowledge of the software is incredible. He optimized our lighting scenes and integrated everything with our new AV system flawlessly.", suburb: "Vaucluse" },
    { name: "Sarah Jenkins", text: "Sydney Automation Co fixed our office lighting control when it was flickering and driving us crazy. George is professional, punctual, and knows C-Bus inside out. A true specialist.", suburb: "Sydney CBD" },
    { name: "David Wilson", text: "Excellent service. George rescued our older C-Bus system in Cronulla that we were told needed to be completely replaced. He just replaced a few faulty modules and saved us thousands.", suburb: "Cronulla" },
    { name: "Michelle Chen", text: "Highly recommend George for any Dynalite work. He's efficient and very thorough. Our home automation is now working exactly how it should have from day one.", suburb: "Mosman" },
    { name: "Mark Peterson", text: "Professional and expert service for our commercial building's DALI system. George solved the addressing issues that our main contractors couldn't. Fast turnaround and clear communication.", suburb: "Pyrmont" },
    { name: "Linda Richards", text: "Best C-Bus programmer in Sydney. George fixed our lighting issues in Sylvania and set up new schedules that have made our home much more energy efficient. Great value.", suburb: "Sylvania" },
    { name: "Andrew Scott", text: "George is our go-to for anything automation related. He's reliable, honest, and his technical background with the manufacturers really shows in the quality of his work.", suburb: "Eastern Suburbs" },
    { name: "Karen Boyd", text: "Fantastic experience with Sydney Automation Co. They fixed our Dynalite panel that had been out of action for weeks. George had all the parts on hand and fixed it same-day.", suburb: "Neutral Bay" },
    { name: "Paul Harrison", text: "Smart, capable, and efficient. George is a specialist you can trust with high-end automation. He fixed our C-Bus network issues in Menai quickly and professionally.", suburb: "Menai" }
  ];
"""
content = re.sub(r'var TESTIMONIALS = \[.*?\];', REVIEWS_JS, content, flags=re.DOTALL)

# 2. PROJECTS PREVIEW Patch
PROJECTS_PREVIEW_JSX = """
      /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "#060b14" }, children: [
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
# Replace Instagram section
content = re.sub(r'/\* @__PURE__ \*/ \(0, import_jsx_runtime\.jsx\)\("section", \{ className: "section", children: /\* @__PURE__ \*/ \(0, import_jsx_runtime\.jsxs\)\("div", \{ className: "container", children: \[ /\* @__PURE__ \*/ \(0, import_jsx_runtime\.jsx\)\("div", \{ className: "tag", children: "Instagram" \}.*?\(0, import_jsx_runtime\.jsx\)\("div", \{ id: "instagram-feed" \} \) \] \} \) \} \)', 
                 PROJECTS_PREVIEW_JSX, content, flags=re.DOTALL)

# 3. ABOUT GEORGE Patch
ABOUT_JSX = """
      /* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", { className: "section", style: { background: "#060b14", borderTop: "1px solid rgba(255,255,255,0.05)" }, children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "container", style: { display: "grid", gridTemplateColumns: "1fr 1.2fr", gap: 64, alignItems: "center" }, children: [
        /* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", { src: "/george-photo.png", style: { width: "100%", borderRadius: 24, boxShadow: "0 20px 40px rgba(0,0,0,0.3)" } }),
        /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "tag", children: "The Specialist" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", { style: { fontSize: 48, fontWeight: 900, marginBottom: 24 }, children: "Expertise From the Source." }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { fontSize: 18, color: "#a8c0e0", lineHeight: 1.8, marginBottom: 24 }, children: "I'm George Skarmoutsos, and I've spent over 15 years mastering the intricacies of C-Bus and Dynalite systems. My background in technical support for Clipsal gives me an 'insider' perspective that general electricians simply don't have." }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { fontSize: 16, color: "#a8c0e0", lineHeight: 1.7, marginBottom: 32 }, children: "We don't just 'wire things up.' We optimize, secure, and future-proof your lighting control network. Whether it's a prestige home in the Shire or a commercial tower in the CBD, we bring manufacturer-level precision to every job." }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", { className: "btn-primary", onClick: () => nav("contact"), children: "Request George for a Consult" })
        ] })
      ] }) })
"""
# Insert after Testimonials
content = content.replace('/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Testimonials, {})', 
                          '/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Testimonials, {}), ' + ABOUT_JSX)

with open(bundle_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Stable bundle.js updates applied.")
