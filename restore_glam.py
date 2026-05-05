import os, re

bundle_path = 'bundle.js'
if os.path.exists(bundle_path):
    with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

# 1. SLEEK CSS (Injecting into index.html is safer)
PREMIUM_CSS = """
  /* PREMIUM UI BOOSTERS */
  .card, .tm-card {
    backdrop-filter: blur(12px) !important;
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
  }
  .card:hover, .tm-card:hover {
    background: rgba(255, 255, 255, 0.06) !important;
    border-color: rgba(240, 112, 32, 0.4) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(240, 112, 32, 0.1) !important;
    transform: translateY(-8px) !important;
  }
  .btn-primary {
    box-shadow: 0 4px 15px rgba(240, 112, 32, 0.3) !important;
    transition: all 0.3s ease !important;
  }
  nav {
    backdrop-filter: blur(20px) !important;
    background: rgba(11, 22, 40, 0.85) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    height: 80px !important;
  }
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  section {
    animation: fadeInUp 0.8s cubic-bezier(0.165, 0.84, 0.44, 1) both;
  }
"""

# 2. COMPARISON & AEO & SHIRE Sections
# I'll build them as a single big block to inject once
GLAM_SECTIONS_JSX = """
      /* SHIRE HERO SECTION */
      , /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "linear-gradient(135deg, #0d1a30, #162a4d)", padding: "120px 0" }, children: [
        /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "container", style: { display: "grid", gridTemplateColumns: "1.2fr 1fr", gap: 64, alignItems: "center" }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "tag", style: { background: "#f07020", color: "#fff" }, children: "Local Shire Specialist" }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", { style: { fontSize: 44, fontWeight: 900, marginBottom: 20 }, children: "Based in Menai. Serving the Shire & Sydney." }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { fontSize: 18, color: "#c8daf0", lineHeight: 1.8, marginBottom: 24 }, children: "Why wait for a technician to travel from North Sydney or Bella Vista? We are based right here in Menai. We provide priority emergency response for C-Bus and Dynalite systems across Cronulla, Miranda, Sylvania, and the Sutherland Shire." }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", { className: "btn-primary", onClick: () => nav("contact"), children: "Request Priority Shire Service" })
          ] }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { background: "rgba(255,255,255,0.03)", padding: 40, borderRadius: 24, border: "1px solid rgba(255,255,255,0.1)" }, children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", { style: { fontSize: 24, marginBottom: 16 }, children: "Local Response Times" }),
            [
              { s: "Menai / Illawong", t: "15-30 Mins" },
              { s: "Miranda / Sylvania", t: "20-40 Mins" },
              { s: "Cronulla / Woolooware", t: "30-50 Mins" },
              { s: "Eastern Suburbs", t: "45-60 Mins" }
            ].map((r, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { display: "flex", justifyContent: "space-between", padding: "12px 0", borderBottom: i === 3 ? "none" : "1px solid rgba(255,255,255,0.1)" }, children: [
              /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { style: { fontWeight: 600 }, children: r.s }),
              /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { style: { color: "#f07020", fontWeight: 800 }, children: r.t })
            ] }, i))
          ] })
        ] })
      ] }),
      /* SPECIALIST COMPARISON SECTION */
      /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "#060b14", padding: "120px 0" }, children: [
        /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "container", style: { textAlign: "center", marginBottom: 56 }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "tag", children: "Why Choose Us?" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", { style: { fontSize: 42, fontWeight: 900, marginBottom: 12 }, children: "The Specialist Difference" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { color: "#a8c0e0", fontSize: 16 }, children: "General electricians are great for wiring, but complex automation requires a Programmer." })
        ] }),
        /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "container", children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { background: "#0b1628", borderRadius: 24, border: "1px solid rgba(255,255,255,0.1)", overflow: "hidden" }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { display: "grid", gridTemplateColumns: "1.5fr 1fr 1fr", background: "rgba(255,255,255,0.03)", borderBottom: "1px solid rgba(255,255,255,0.1)", padding: "20px 32px" }, children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { fontWeight: 800, color: "#a8c0e0" }, children: "SERVICE FEATURE" }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { fontWeight: 800, color: "#f07020", textAlign: "center" }, children: "SYDNEY AUTOMATION" }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { fontWeight: 800, color: "#a8c0e0", textAlign: "center" }, children: "GENERAL ELECTRICIAN" })
          ] }),
          [
            { f: "Manufacturer-Level Programming (Clipsal/Philips)", sa: true, ge: false },
            { f: "Network Burden & Voltage Analysis", sa: true, ge: false },
            { f: "Logic & Scene Optimization", sa: true, ge: "Basic Only" },
            { f: "Same-Day System Resurrection", sa: true, ge: "Rare" },
            { f: "Legacy Integration Specialist", sa: true, ge: false }
          ].map((row, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { display: "grid", gridTemplateColumns: "1.5fr 1fr 1fr", padding: "18px 32px", borderBottom: i === 4 ? "none" : "1px solid rgba(255,255,255,0.05)" }, children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { fontWeight: 600 }, children: row.f }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { textAlign: "center", color: "#00A651" }, children: row.sa === true ? "✔" : row.sa }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { textAlign: "center", color: row.ge === false ? "#ff4d4d" : "#a8c0e0" }, children: row.ge === false ? "✘" : row.ge })
          ] }, i))
        ] }) })
      ] }),
      /* AEO FAQ SECTION */
      /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "#060b14", padding: "120px 0" }, children: [
        /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "container", style: { textAlign: "center", marginBottom: 56 }, children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "tag", children: "Answers & Solutions" }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", { style: { fontSize: 42, fontWeight: 900, marginBottom: 12 }, children: "Common C-Bus & Dynalite Problems — Solved." }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { color: "#a8c0e0", fontSize: 16 }, children: "Expert answers to the most common lighting control failures in Sydney." })
        ] }),
        /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "container", children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))", gap: 32 }, children: [
          { q: "Why are my C-Bus lights flickering or not turning off?", a: "This is often caused by a failed power supply or a network 'burden' issue. We perform manufacturer-level diagnostics to find the exact module at fault, saving you from a full system replacement." },
          { q: "My Dynalite system has crashed. Can it be recovered?", a: "Yes. Most Dynalite 'crashes' are due to corrupted logic or a failed gateway. We use proprietary Envision software to restore your configuration and stabilize the network—often in a single visit." },
          { q: "Do I need to replace my 15-year-old C-Bus system?", a: "Almost never. C-Bus hardware is incredibly robust. By updating your relays and adding a modern bridge (like Apple HomeKit or Google Home), we can make an old system feel brand new for a fraction of the cost." }
        ].map((faq, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { className: "card", children: [
          /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("h3", { style: { fontSize: 20, color: "#f07020", marginBottom: 16 }, children: ["Q: ", faq.q] }),
          /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { style: { color: "#a8c0e0", fontSize: 15, lineHeight: 1.7 }, children: faq.a })
        ] }, i)) }) })
      ] })
"""

# 3. Inject Glam Sections after About George
# We'll search for the end of the About section I just added
if "Request George for a Consult\" }) ] })" in content:
    content = content.replace("Request George for a Consult\" }) ] })", 
                              "Request George for a Consult\" }) ] })" + GLAM_SECTIONS_JSX)

# 4. Inject aggressive CTAs
content = content.replace('children: "Get a Free Quote"', 'children: "Fix My System Today — Call 0422 469 739"')
content = content.replace('children: "Learn More"', 'children: "Stop the Flickering"')

with open(bundle_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 5. Inject CSS into index.html
if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    if '</head>' in html:
        html = html.replace('</head>', f'<style>{PREMIUM_CSS}</style>\n</head>')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS: Full Glam & Kill strategy restored safely.")
