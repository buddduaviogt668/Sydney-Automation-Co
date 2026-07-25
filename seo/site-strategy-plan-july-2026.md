# Site Strategy Plan — July 2026

## Context

Three channels drive ~55% of revenue but the website barely serves them:

1. **Trade partner referrals** — 15+ electricians and AV integrators (AJB Electrical, Sharper Automation, Blinds Quickly, Matrix Electrical, Dreamtech AV etc.)
2. **C-Bus relay/power supply failures** — ~30 of 87 recent jobs were ageing 2000s-era hardware failures across Sydney
3. **Remote Dynalite commissioning** — Dreamtech AV in NT alone generated $8,050. No local competitors offer this.

## Execution (Completed July 2026)

### Phase 1 — Redirect Thin Pages (Low Effort)
**Goal:** Consolidate SEO authority from ~882 thin pages into main service pages.

**Actions:**
- Added 6 redirect rules to `vercel.json` covering:
  - 588 tech library pages → `/tech-library`
  - 67 C-Bus programmer suburb pages → `/c-bus-programmer-sydney`
  - 65 Dynalite programmer suburb pages → `/dynalite-programmer-sydney`
  - 68 C-Bus repair suburb pages → `/cbus-repair-sydney`
  - 40 Dynalite repair suburb pages → `/dynalite-repair-sydney`
  - 50 smart home automation suburb pages → `/services`

**Impact:** Eliminates duplicate/thin content dilution. Page authority consolidates into canonical service pages.

### Phase 2 — Fix Meta Titles (Low Effort)
**Goal:** Clean up dated and poorly structured title tags on core pages.

| Page | Old Title | New Title |
|------|-----------|-----------|
| `/locations` | Automation Sydney 2026 \| C-Bus & Smart Home Service Areas | C-Bus & Dynalite Service Areas Sydney \| Sydney Automation Co |
| `/contact` | Contact Sydney Automation Co. \| Request a Quote — C-Bus. | Contact \| Sydney Automation Co — C-Bus & Dynalite Specialists |
| `/services` | Lighting Automation Services Sydney \| C-Bus, Dynalite, DALI | Lighting Control Services Sydney \| C-Bus, Dynalite & DALI Specialists |

### Phase 3 — Rewrite /electricians (Medium Effort)
**Goal:** Convert a non-performing page into a proper trade partner landing page.

**Changes:**
- Title: `C-Bus & Dynalite Trade Partner | Sydney Electricians & AV Integrators`
- Hero rewritten to target electricians/AV integrators, not "Automation Specialists"
- Named 5 trade partners in hero copy (AJB Electrical, Sharper Automation, etc.)
- Zero competitive overlap messaging sharpened
- "15+ trade partners" social proof added

### Phase 4 — New Page: C-Bus Relay/Power Supply Replacement (Medium Effort)
**URL:** `/cbus-relay-power-supply-replacement-sydney`

**Content covers:**
- Stats: ~30 of 87 recent jobs were relay/PSU failures
- Signs of failure: buzzing, lights stuck on/off, flickering, dead zones
- Common models: L5504RSF, L5504PSF, 5104D20RS, 5500PS/RS, L5504D20RS
- 4-step replacement process
- Transparent pricing
- Schema.org Service JSON-LD

### Phase 5 — New Page: Remote C-Bus/Dynalite Commissioning (Medium Effort)
**URL:** `/remote-cbus-dynalite-commissioning`

**Content covers:**
- Dreamtech AV case: $8,050 generated from remote commissioning
- Australia-wide service
- C-Bus and Dynalite capabilities (Toolkit, System Builder)
- 4-step process
- Target audiences: regional electricians, AV integrators, building managers, trade partners
- Pricing: $150/hr, no minimum, no travel

### Phase 6 — Internal Links (Low Effort)
**Goal:** Link from ranking pages → case studies to improve case study visibility and distribute authority.

**Links added:**
- `/electricians` → 4 case study links (Henley, Kebia, Winten, The Rocks)
- `/cbus-relay-power-supply-replacement-sydney` → 2 case study links (Henley, Kebia)
- `/remote-cbus-dynalite-commissioning` → 2 case study links (Mosman, Winten)

## What Not To Do

- ❌ More suburb pages (all redirected to canonical pages)
- ❌ More tech library pages (entire directory redirected to hub)
- ❌ A blog content machine
- ❌ A redesign (core pages work, strategy was the problem)

## Next Opportunities

- Add `/cbus-relay-power-supply-replacement-sydney` and `/remote-cbus-dynalite-commissioning` to sitemap
- Monitor Google Search Console for redirect traffic and indexing changes
- Consider adding case study links to `/cbus-repair-sydney` directly (page uses uncommon encoding, needs byte-level edit)
