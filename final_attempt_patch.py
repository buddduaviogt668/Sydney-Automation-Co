import os, re

bundle_path = 'bundle.js'
if os.path.exists(bundle_path):
    with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

# THE CORRECT TARGET in the original bundle.js
TARGET = '/* @__PURE__ */ (0, import_jsx_runtime.jsx)(TestimonialsSection, {})'

if TARGET in content:
    # 1. ABOUT GEORGE
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
      ] }) }),
    """
    content = content.replace(TARGET, TARGET + "," + ABOUT_JSX)
    print("SUCCESS: Added About George")

    # 2. SHIRE HERO & COMPARISON & AEO
    GLAM_SECTIONS = """
      /* SHIRE HERO */
      /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { className: "section", style: { background: "linear-gradient(135deg, #0d1a30, #162a4d)", padding: "120px 0" }, children: [
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
      /* COMPARISON TABLE */
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
            { f: "Manufacturer-Level Programming", sa: "✔", ge: "✘" },
            { f: "Network Burden Analysis", sa: "✔", ge: "✘" },
            { f: "Logic Optimization", sa: "✔", ge: "Basic" },
            { f: "Same-Day Rescue", sa: "✔", ge: "Rare" }
          ].map((row, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { style: { display: "grid", gridTemplateColumns: "1.5fr 1fr 1fr", padding: "18px 32px", borderBottom: i === 3 ? "none" : "1px solid rgba(255,255,255,0.05)" }, children: [
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { fontWeight: 600 }, children: row.f }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { textAlign: "center", color: "#00A651" }, children: row.sa }),
            /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: { textAlign: "center", color: row.ge === "✘" ? "#ff4d4d" : "#a8c0e0" }, children: row.ge })
          ] }, i))
        ] }) })
      ] }),
    """
    content = content.replace(ABOUT_JSX, ABOUT_JSX + GLAM_SECTIONS)
    print("SUCCESS: Added Glam Sections")

    with open(bundle_path, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("ERROR: Target not found")
