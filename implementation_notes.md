# Implementation notes

## Changes made

1. Homepage metadata now targets C-Bus and Dynalite repairs in Sydney, with fault finding, programming and upgrades in the description and title.
2. Homepage hero now explicitly says Sydney repair, fault finding and programming specialists.
3. Homepage hero copy now explains the network-level specialist differentiator and names residential, strata and commercial systems.
4. Homepage secondary CTA now says: “Book a diagnostic visit or call to arrange priority support →”.
5. C-Bus vs Dynalite comparison page opening now links to C-Bus Repairs Sydney, Dynalite Repairs Sydney and a specialist upgrade assessment.

## Verification

- `git diff --check` passed with no whitespace errors.
- Local homepage preview rendered with the revised title, hero headline, CTA and existing service links visible.
- Local comparison-page preview rendered with all three new internal conversion links visible above the comparison content.
- No build script is provided for the static HTML pages; package.json contains workspace/typecheck scripts unrelated to the static pages.

## Service-page improvement pass

Updated C-Bus Repair Sydney, Dynalite Repair Sydney, and C-Bus Upgrade Sydney.

- Repair-page meta descriptions now target specific faults and specialist services.
- C-Bus Repair hero copy now explains network-first diagnosis, distinguishes repair from modernisation, and links to the C-Bus upgrade service.
- Dynalite Repair hero copy now explains live DyNet network diagnosis and links to C-Bus repairs for visitors on the wrong system path.
- C-Bus Upgrade hero copy now explains assessment, preservation of existing programming, written scope, and upgrade categories; its CTA now requests an upgrade assessment before a direct-call fallback.
- Local browser previews of C-Bus Repair and Dynalite Repair rendered correctly with revised copy, badges, CTAs and internal links visible.
- Initial `git diff --check` caught existing trailing whitespace on the edited C-Bus repair metadata line; it was removed, and the check now passes.
