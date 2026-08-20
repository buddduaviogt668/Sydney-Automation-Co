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
