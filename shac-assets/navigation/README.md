# SHAC Studio Navigation Controls

These controls are the display-ready HOME, BACK, and NEXT buttons for the generic SHAC Studio automation UI screens. They are designed for placement over the 1024 × 600 tablet sample screens and are also supplied as standalone SVG assets for integrators to place in their own layouts.

## Visual specification

The controls follow the original SHAC premium icon family: a 128px-derived simplified icon language, rounded line ends and joins, a five-pixel reference stroke, champagne-brass `#D6A354` linework, and the deep burgundy `#5A233D` inset treatment. Each button uses a dark burgundy fill with a brass border so the control covers the background beneath it instead of becoming visually lost on the display artwork.

The labels are rendered exactly as uppercase **HOME**, **BACK**, and **NEXT**. No client name, group address, alignment guide, instructional copy, or other non-client-facing text is included in the controls.

## 1024 × 600 placement

The controls are embedded in the v2.0 package screens under `SampleProjects/`. Internal pages such as room detail, scene control, and status dashboard use the full **BACK**, **HOME**, **NEXT** row. The Home/floor-plan screen is intentionally different: it contains **NEXT** only, with no HOME or BACK because it is the entry page. The shared placement group uses the screen SVG coordinate system (`1600 × 960` viewBox) and is positioned at `translate(252 842)`, with controls scaled to `.78` for consistent display spacing.

Because the screen files are SVG, the controls preserve their geometry when imported into a 1024 × 600 display layout. The controls are not stretched independently; the full screen preserves its aspect ratio when placed in the integrator’s project.

## Package verification

The following v2.0 archives were updated with the standalone files in their root `Navigation/` folder and with navigation controls embedded on their 1024 × 600 sample screens. Home/floor-plan screens use NEXT only; internal sample screens use the full row:

| Package | 1024 × 600 screens updated |
| --- | ---: |
| `SHAC_Commercial_Venue_Add-on_v2.0.zip` | 20 |
| `SHAC_Complete_Studio_v2.0.zip` | 32 |
| `SHAC_Essentials_Icons_v2.0.zip` | 8 |
| `SHAC_Foundation_Bundle_v2.0.zip` | 12 |
| `SHAC_Integrator_Edition_v2.0.zip` | 32 |
| `SHAC_Outdoor_Pack_v2.0.zip` | 4 |
| `SHAC_Residential_Starter_v2.0.zip` | 8 |
| `SHAC_Theatre_AV_Pack_v2.0.zip` | 8 |

Verification checks confirmed that each refreshed archive contains `Navigation/back_gold.svg`, `Navigation/home_gold.svg`, and `Navigation/next_gold.svg`; each Home/floor-plan screen contains only the `shac-next` control, while internal screens contain the exact BACK, HOME, and NEXT labels.
