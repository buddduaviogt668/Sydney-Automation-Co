# SEMrush issue fix notes

## Spreadsheet findings applied

The uploaded SEMrush pages export showed a cluster of pages with missing titles and descriptions that corresponded to route mismatches rather than missing metadata in the underlying HTML files. The strongest pattern was:

- `/blog/<slug>` URLs being crawled even though the site content lives at `/<slug>.html`
- clean URLs such as `/cbus`, `/locations`, and legacy path variants such as `/cbus-repairs-sydney.html` lacking correct redirects
- the live `.com.au` domain being served from Vercel project `project-on1b4`

## Direct fixes made

On branch `main` in repository `buddduaviogt668/Sydney-Automation-Co`, commit `dd42321e2fff9a7d4ace941dfafb7d5476fd087b` updated `vercel.json` to add permanent redirects for:

- `/blog/:slug` -> `/:slug.html`
- `/cbus` -> `/c-bus-programmer-sydney.html`
- `/cbus-repairs-sydney` and `/cbus-repairs-sydney.html` -> `/c-bus-repairs-sydney.html`
- `/locations` -> `/locations.html`
- `/projects` -> `/projects.html`

## Deployment validation

The Git push triggered a new production Vercel deployment:

- Project ID: `prj_1SoRts3KlmtfUzpU6UDdmXz5huev`
- Deployment ID: `dpl_12yYb1FxLxmM9tbGuFad6FqjiNt8`
- State: `READY`
- Aliases include `sydneyautomationco.com.au` and `www.sydneyautomationco.com.au`

A live browser check confirmed that `https://sydneyautomationco.com.au/blog/dali2-compliance-nsw-commercial` now resolves to `https://sydneyautomationco.com.au/dali2-compliance-nsw-commercial.html` and shows the intended DALI-2 article with a real title.
