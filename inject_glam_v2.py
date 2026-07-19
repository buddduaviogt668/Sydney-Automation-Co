import os, re

bundle_path = 'bundle.js'
index_path = 'index.html'

if not os.path.exists(bundle_path):
    print("ERROR: bundle.js not found")
    exit(1)

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. CONVERTING PHRASES & CATCHY HEADLINES
print("Applying Catchy Phrases...")
# Main Hero Headline
content = content.replace('children: "Lighting Control Specialists"', 'children: "Sydney\'s #1 Emergency C-Bus & Dynalite Resurrection Team"')
content = content.replace('children: "C-Bus & Dynalite Specialists"', 'children: "Sydney\'s #1 Emergency C-Bus & Dynalite Resurrection Team"')

# CTAs
content = content.replace('children: "Get a Free Quote"', 'children: "Stop the Flickering — Fix My System"')
content = content.replace('children: "Learn More"', 'children: "Emergency Service 0422 469 739"')
content = content.replace('children: "Contact Us"', 'children: "Resurrect My System"')

# 2. GLITZ & GLAM SECTIONS (JSX)
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

# Robust injection for Glam Sections
# Looking for the "Request George for a Consult" button container
marker = 'children: "Request George for a Consult" })'
if marker in content:
    print("Found About Section Marker. Injecting Glam...")
    # Find the end of the button's parent div/section
    # The structure is usually: ...button...}) ] }) ] })
    # We'll search for the next "] })" after the marker
    pos = content.find(marker)
    end_pos = content.find('] })', pos) + 4
    end_pos = content.find('] })', end_pos) + 4
    
    content = content[:end_pos] + GLAM_SECTIONS_JSX + content[end_pos:]
    print("SUCCESS: Glitz & Glam sections injected.")
else:
    print("WARNING: Could not find injection marker for Glam sections.")

# 3. SAVE BUNDLE
with open(bundle_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 4. INDEX.HTML UPDATES (Meta tags & Static backup)
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Update title for maximum glam
    html = html.replace('<title>C-Bus &amp; DALI Lighting Control Specialists Sydney | Sydney Automation Co</title>', 
                        '<title>Sydney\'s #1 Emergency C-Bus &amp; Dynalite Repair | Sydney Automation Co</title>')
    
    # Update Meta Description
    html = html.replace('content="Accredited C-Bus programmer and Dynalite system designer based in Menai, Sydney. Same-day fault finding, repairs and commissioning. Call 0422 469 739."',
                        'content="Sydney\'s #1 Emergency C-Bus &amp; Dynalite Resurrection Team. Based in Menai. Same-day fault finding, manufacturer-level repairs and system stabilization. Don\'t replace—restore. Call 0422 469 739."')

    with open(index_path, 'w', encoding='utf-8') as f:
        html = f.write(html)
    print("SUCCESS: index.html meta-glam updated.")

print("GLAM & KILL Strategy fully deployed.")
