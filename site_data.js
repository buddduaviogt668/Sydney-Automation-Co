
/* SITE DATA - CLEANED */
var MANUFACTURERS = [
  {
    name: "Clipsal C-Bus",
    byLine: "by Schneider Electric",
    accred: "Accredited C-Bus Programmer",
    url: "https://www.clipsal.com/products/smart-home-solutions/c-bus-control-management-system",
    color: "#00A651",
    desc: "Accredited C-Bus Programmer with 15+ years experience across residential and commercial C-Bus installations, programming and fault finding across Greater Sydney.",
    badge: "Accredited Programmer"
  },
  {
    name: "Dynalite",
    byLine: "by Signify (Philips)",
    accred: "Accredited Dynalite System Designer",
    url: "https://www.dynalite.com/",
    color: "#0068B5",
    desc: "Accredited Dynalite System Designer for luxury residential, hospitality and large-scale commercial environments across Sydney and the Sutherland Shire.",
    badge: "Accredited System Designer"
  },
  {
    name: "RAPIX",
    byLine: "by Ozuno",
    accred: "Experienced Integrator",
    url: "https://ozuno.com/rapix-lighting-control-system/",
    color: "#E8A020",
    desc: "Experienced in RAPIX networked lighting control for commercial fitouts, train stations and infrastructure projects. RAPIX does not operate a formal accreditation programme.",
    badge: "Experienced Integrator"
  }
];

var SERVICES = [
  { title: "C-Bus Automation", slug: "cbus", tagline: "C-Bus fault finding & commissioning - Menai, Sutherland Shire & Greater Sydney", features: ["Scene programming", "Energy monitoring", "Remote control", "Legacy integration"], productUrl: "https://www.clipsal.com/products/smart-home-solutions/c-bus-control-management-system" },
  { title: "Dynalite Systems", slug: "dynalite", tagline: "Dynalite fault finding & programming - hospitality-grade precision control", features: ["Hotel-grade dimming", "Multi-zone control", "DALI integration", "Mood scenes"], productUrl: "https://www.dynalite.com/" },
  { title: "RAPIX & DALI", slug: "rapix", tagline: "Commercial networked lighting control - RAPIX & DALI specialists", features: ["Emergency lighting", "Occupancy sensors", "Energy compliance", "BMS integration"], productUrl: "https://ozuno.com/rapix-lighting-control-system/" },
  { title: "Smart Home Integration", slug: "smarthome", tagline: "Everything connected, beautifully simple", features: ["Voice control", "App automation", "Climate integration", "Security linkage"], productUrl: "https://www.clipsal.com/" },
  { title: "Fault Finding & Repairs", slug: "repairs", tagline: "Same-day fault finding - Menai, Sutherland Shire & all of Sydney", features: ["Same-day callout", "All brands serviced", "Warranty on repairs", "Remote diagnosis"], productUrl: null },
  { title: "Design & Consultation", slug: "consult", tagline: "Get it right from day one - serving Greater Sydney", features: ["CAD drawings", "Spec documents", "Builder liaison", "Future-proofing"], productUrl: null }
];

var LOCATIONS = [
  { name: "Sutherland Shire", suburbs: "Menai, Sutherland, Miranda, Cronulla, Caringbah, Gymea, Engadine, Jannali, Heathcote, Bundeena", projects: "Home base", featured: true },
  { name: "Menai (Home Base)", suburbs: "Our workshop & team are based right here - fastest response times guaranteed for all Menai locals", projects: "Based here", featured: true },
  { name: "Eastern Suburbs", suburbs: "Bondi, Double Bay, Vaucluse, Paddington, Woollahra, Randwick", projects: "Active area", featured: false },
  { name: "North Shore", suburbs: "Mosman, Cremorne, Kirribilli, Chatswood, St Leonards, Lane Cove", projects: "Active area", featured: false },
  { name: "Northern Beaches", suburbs: "Manly, Dee Why, Freshwater, Balgowlah, Mona Vale", projects: "Active area", featured: false },
  { name: "Inner West", suburbs: "Balmain, Leichhardt, Glebe, Newtown, Marrickville", projects: "Active area", featured: false },
  { name: "Hills District", suburbs: "Castle Hill, Kellyville, Baulkham Hills, Rouse Hill, Norwest", projects: "Active area", featured: false },
  { name: "Parramatta", suburbs: "Parramatta, Westmead, Merrylands, Granville, Auburn", projects: "Active area", featured: false }
];

var BLOG = [
  {
    title: "C-Bus Fault Finding in Sydney: What to Check Before Calling a Technician",
    slug: "cbus-fault-finding-sydney",
    cat: "Troubleshooting",
    date: "Feb 12, 2025",
    read: "5 min",
    suburb: "Greater Sydney - Menai, Sutherland Shire, Eastern Suburbs",
    excerpt: "Most C-Bus faults in Sydney come down to 3 causes. Check these first - you may be able to describe the fault accurately and save time."
  },
  {
    title: "Dynalite vs C-Bus: Which Lighting Control System Is Right for Your Sydney Project?",
    slug: "dynalite-vs-cbus-sydney",
    cat: "Comparison",
    date: "Jan 28, 2025",
    read: "8 min",
    suburb: "Sutherland Shire, North Shore, Eastern Suburbs, CBD",
    excerpt: "Dynalite and C-Bus are both excellent - but built for very different contexts. An honest comparison from a specialist accredited on both."
  },
  {
    title: "DALI-2 Compliance for NSW Commercial Buildings: What You Need to Know in 2025",
    slug: "dali2-compliance-nsw-commercial",
    cat: "Compliance",
    date: "Jan 15, 2025",
    read: "6 min",
    suburb: "Greater Sydney - Commercial, Strata, Infrastructure",
    excerpt: "NCC 2022 introduced stricter DALI-2 emergency lighting requirements for NSW commercial buildings. Here’s what you need to know."
  },
  {
    title: "Does C-Bus or Dynalite Automation Add Value to Sutherland Shire Properties?",
    slug: "cbus-dynalite-property-value-sutherland-shire",
    cat: "Investment",
    date: "Dec 20, 2024",
    read: "7 min",
    suburb: "Sutherland Shire - Menai, Cronulla, Miranda, Caringbah, Gymea",
    excerpt: "Sutherland Shire buyers increasingly expect smart lighting. An honest look at where C-Bus and Dynalite genuinely moves the needle on property value."
  },
  {
    title: "C-Bus Scene Programming Guide for Sutherland Shire Homeowners",
    slug: "cbus-scene-programming-guide-sutherland-shire",
    cat: "How-To",
    date: "Dec 5, 2024",
    read: "10 min",
    suburb: "Sutherland Shire - Menai, Sutherland, Miranda, Caringbah",
    excerpt: "You don’t need a programmer for every change. Here’s exactly what you can do yourself on your C-Bus system - and what needs a specialist."
  },
  {
    title: "C-Bus and Dynalite Planning Checklist for New Builds in Menai and the Sutherland Shire",
    slug: "cbus-dynalite-planning-checklist-new-builds-menai",
    cat: "Planning",
    date: "Nov 18, 2024",
    read: "9 min",
    suburb: "Menai, Sutherland Shire - New Builds and Renovations",
    excerpt: "Building in the Sutherland Shire? Here’s the C-Bus and Dynalite checklist your builder needs before the electrician starts rough-in."
  },
  {
    title: "Why C-Bus Fault Finding in the Sutherland Shire Is Different to the Rest of Sydney",
    slug: "cbus-fault-finding-sutherland-shire",
    cat: "Troubleshooting",
    date: "Mar 5, 2025",
    read: "5 min",
    suburb: "Sutherland Shire - Menai, Cronulla, Miranda, Caringbah, Gymea, Engadine",
    excerpt: "The Shire has a unique mix of older C-Bus installs, coastal humidity and rapid new development. Here's what that means for fault finding in your suburb."
  },
  {
    title: "Dynalite Fault Finding Sydney: The 5 Most Common Faults We See On-Site",
    slug: "dynalite-fault-finding-sydney-common-faults",
    cat: "Troubleshooting",
    date: "Mar 12, 2025",
    read: "6 min",
    suburb: "Sydney - CBD, North Shore, Eastern Suburbs, Sutherland Shire, Hotels, Commercial",
    excerpt: "Dynalite is incredibly reliable - until it’s not. The 5 most common Dynalite faults George sees on Sydney commercial and residential sites."
  },
  {
    title: "A Message to Sydney Electricians: Here's How We Can Work Together",
    slug: "sydney-electricians-cbus-dynalite-partnership",
    cat: "Trade & Electricians",
    date: "Mar 19, 2025",
    read: "4 min",
    suburb: "Greater Sydney - Sutherland Shire, Eastern Suburbs, North Shore, CBD, Parramatta",
    excerpt: "Sydney Automation Co. are not electricians - no competition, no overlap. A reliable C-Bus and Dynalite specialist you can refer jobs to with confidence."
  },
  {
    title: "C-Bus Scene Programming: How to Get the Most Out of Your Sydney Home",
    slug: "cbus-scene-programming-sydney-home",
    cat: "How-To",
    date: "Mar 26, 2025",
    read: "7 min",
    suburb: "Sydney Residential - Sutherland Shire, Eastern Suburbs, North Shore, Inner West",
    excerpt: "Most C-Bus homes use less than 20% of what their system can do. Here's how to set up scenes that actually make life better - not just turn lights on."
  },
  {
    title: "How to Choose a C-Bus Specialist in Sydney (And What to Avoid)",
    slug: "how-to-choose-cbus-specialist-sydney",
    cat: "How-To",
    date: "Apr 2, 2025",
    read: "5 min",
    suburb: "Greater Sydney - All Suburbs",
    excerpt: "Not everyone who calls themselves a C-Bus specialist has the accreditation to back it up. Here's what to ask before you book anyone to touch your system."
  },
  {
    title: "What Is RAPIX and Why More Sydney Buildings Are Switching to It",
    slug: "what-is-rapix-sydney-buildings",
    cat: "Commercial",
    date: "Apr 9, 2025",
    read: "5 min",
    suburb: "Sydney Commercial - CBD, Parramatta, North Sydney, Infrastructure",
    excerpt: "RAPIX is quietly becoming the go-to networked lighting platform for mid-to-large commercial buildings across Sydney. Here's what it is and when to use it."
  },
  {
    title: "C-Bus and Dynalite Fault Finding in Sydney's Eastern Suburbs: What We See Most",
    slug: "cbus-dynalite-fault-finding-eastern-suburbs",
    cat: "Troubleshooting",
    date: "Mar 5, 2025",
    read: "6 min",
    suburb: "Eastern Suburbs - Paddington, Bondi, Woollahra, Double Bay",
    excerpt: "The Eastern Suburbs has some of Sydney’s most complex C-Bus and Dynalite installations. Here’s what goes wrong most often."
  }
];
