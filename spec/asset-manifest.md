# Asset manifest — original concept artwork

The first table lists the 2026-11-14 concept art (made in ChatGPT); the v2 section below lists the approved replacements made in Google Flow. Approved is not the same as released or locked. The repository tracks practical README previews in `assets/marketing/`. The original high-resolution outputs were produced in ChatGPT; keep/backup full-size masters in durable production storage rather than assuming the GitHub preview is the master.

| Repo preview | Source concept | Status | Notes |
| --- | --- | --- | --- |
| `assets/marketing/poster-tv-4x3.webp` | 4:3 horizontal Better Call Sophie TV poster | replaced by v2 on 2026-11-23 | Burgundy suit, office, philosophical chalkboard, Albuquerque dusk; generated 2026-11-14 |
| `assets/marketing/business-card-front.webp` | Goodman Philosophical Consulting card front | replaced by v2 on 2026-11-23 | Yellow/red ad-style, portrait and fictional phone 505-555-0148; generated 2026-11-14 |
| `assets/marketing/business-card-back.webp` | Business card back | replaced by v2 on 2026-11-23 | Services and fictional contact information; generated 2026-11-14 |

The concept files remain in Git history (last at commit `94575f2`). The concept poster is also in the Flow work project as `sophie-poster-concept-ref.png`.

**Source session file names** (not necessarily published to repo at full size):
- `better_call_sophie_moral_loopholes.png` (the more recent 4:3 poster was chosen).
- `a_bold_graphic_advertising_style_poster_business.png` (business-card front).
- `better_call_sophie_business_card.png` (business-card back).

## v2 poster and business card (APPROVED 2026-11-23)

Showrunner direction (2026-11-23): regenerate the poster and card with Sophie's approved face ([reference-front.webp](../assets/characters/sophie-goodman/reference-front.webp)); set the poster in her approved office; generate text-free art and add all lettering afterwards; card logo is the owl with scales, no column. The showrunner approved all three on 2026-11-23 ("Approve all three"); the composed WebP files now replace the concept files at the repo paths above, and the three art images are uploaded to the show project.

| Piece | Art (Google Flow, Nano Banana 2.1) | Composed output | Repo file |
| --- | --- | --- | --- |
| TV poster 4:3 | `poster-art` v01, [log](../production/generation-logs/poster-art-v01.yaml) | `production/exports/marketing/poster-tv-4x3-v2.png` (1200x896) | `assets/marketing/poster-tv-4x3.webp` |
| Card front | `card-photo` v01, [log](../production/generation-logs/card-photo-v01.yaml) | `production/exports/marketing/business-card-front-v2.png` (1050x600, 3.5x2 in at 300 dpi) | `assets/marketing/business-card-front.webp` |
| Card back | `card-logo` v01, [log](../production/generation-logs/card-logo-v01.yaml) | `production/exports/marketing/business-card-back-v2.png` (1050x600) | `assets/marketing/business-card-back.webp` |

**Poster with Flow-generated lettering (PROPOSED, 2026-11-23):** at the showrunner's request ("generate one with the text, using the font of the old poster"), Flow lettered the approved poster art, using the concept poster as the lettering reference: `poster-lettered` v01, [log](../production/generation-logs/poster-lettered-v01.yaml), `production/exports/marketing/poster-lettered-v01.jpg` (1200x896, gitignored). It is a candidate to replace the composed poster; the repo file stays the composed v2 until the showrunner picks one.

- Prompts: [production/prompts/marketing-v2.md](../production/prompts/marketing-v2.md).
- Lettering: [scripts/compose_marketing.py](../scripts/compose_marketing.py), run with `uv run --no-project --with pillow python scripts/compose_marketing.py`. It uses the Windows system fonts Arial Black, Georgia and Brush Script MT; check their license terms before any commercial print run, or swap in open-licensed fonts.
- The v2 card keeps the fictional 555 phone number and drops the concept card's email and web addresses, because those domains may belong to real people. It adds "Albuquerque, New Mexico".

Avoid relying on the fictional email/web addresses as real, registered services. Before print, web deployment, or release, verify names and text with a human-readable final proof. Future assets should list prompt, tool, model if available, reference images, versions, review decision and license/rights notes. Distinguish **concept**, **approved**, and **released**.

## Namespaces

- `assets/marketing/`: approved preview/brand identity files, not camera originals.
- `assets/characters/`: character-turnaround and continuity references.
- `assets/locations/`: reusable environment references.
- `production/`: shot-specific prompt records and generated candidates.
- Large masters/videos: external production storage with a documented manifest, not unbounded Git history.
