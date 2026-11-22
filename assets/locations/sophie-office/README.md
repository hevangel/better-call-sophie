# Location: Goodman Philosophical Consulting — Sophie's office

**Status:** design **APPROVED** by the showrunner (2026-11-22): concept, floor plan and fixed set list. The **master wide (v02) is APPROVED** (2026-11-22; see Decisions). The other views of the reference pack are **not generated yet**. From now on, changes to the floor plan or set list need a documented reason. Needed before the next round of Flow tests, because continuity was the weakest result of the tutorial run.

## Concept

A cheap storefront office in an Albuquerque strip mall, in **2030**, between a vape shop and a tax preparer. It's a deliberate echo of grandpa's back-room nail-salon office. Sophie has made it look **smarter than it can afford**: wall-to-wall philosophy books, a slate chalkboard, one good leather chair for clients. The street side is gaudy Goodman yellow and red. The inside is warm, scholarly and a little shabby.

The 2030 touches stay small: a thin wireless display, a phone used as a document scanner, an AI-assistant speaker she never trusts. No holograms, no glass-cube futurism.

## Floor plan (fixed for continuity)

```text
            BACK WALL: floor-to-ceiling bookshelves (philosophy, law, a few novels)
   ┌──────────────────────────────────────────────────────────────┐
   │ [chalkboard]                                  [door to back  │
   │  left wall                                     room/kitchen] │
   │                                                              │
   │        [SOPHIE'S DESK]  ← faces the front window             │
   │        green banker's lamp, stacked books, laptop            │
   │                                                              │
   │   [client leather chair]   [second visitor chair]            │
   │                                                              │
   │ [coat stand]        [small waiting bench]   [water cooler]   │
   └────────[ FRONT DOOR ]────────[ FRONT WINDOW, ad decal ]──────┘
            STREET SIDE: strip-mall parking lot, mountains in the distance
```

**Screen direction:** when Sophie sits at her desk, the window is in front of her (camera behind the client sees the bookshelves behind her), and the chalkboard is on her **right**, which is screen left from the client's eyeline. Keep this fixed.

## Fixed set elements (the continuity checklist)

| Element | Exact description |
| --- | --- |
| Desk | Dark walnut, scuffed, with a green glass banker's lamp, three stacked books (top one red), a closed silver laptop and a brass nameplate reading "Dr. S. Goodman". Add the nameplate text in post if it renders wrong |
| Chalkboard | Slate, wooden frame. A hand-drawn trolley-problem diagram, plus "IS ≠ OUGHT" circled. The contents change only when the script says so |
| Bookshelves | Full back wall, dark wood, mixed spines, a small bust of Socrates on the top-right shelf |
| Client chair | Oxblood leather wingback, slightly worn |
| Window | Large storefront glass with a reversed yellow-red decal reading "BETTER CALL SOPHIE" (add the text in post when legible). Venetian blinds, half open |
| Floor | Worn wood-look laminate, a faded Persian-style rug under the desk |
| Walls | Warm cream plaster; framed PhD diploma behind the desk, left of the shelves |
| Props that travel | Goodman business cards in a brass holder on the desk; Sophie's worn paperback (dark green cover) |

## Lighting states

| State | Use | Description |
| --- | --- | --- |
| **Day** | Consultations | Hard New Mexico daylight through the blinds; slatted shadows on the floor; cool fill |
| **Golden hour** | Default "hero" look, as in the poster | Warm orange light from the window; banker's lamp on |
| **Night** | Quiet character scenes | Only the banker's lamp and the yellow-red decal glow from the street sign; deep shadows on the shelves |

## Camera positions

| ID | Position | Typical use |
| --- | --- | --- |
| `cam-a` | Over the client's shoulder, toward Sophie and the bookshelves | Sophie's coverage |
| `cam-b` | Reverse from behind Sophie's shoulder, toward the client with the window behind | Client coverage |
| `cam-c` | Wide from the front-door corner, showing desk, chalkboard and shelves | Establishing and entrances |
| `cam-d` | Side-on beside the chalkboard | Sophie at the board, profile two-shots |
| `cam-e` | Exterior, across the parking lot, toward the storefront | Establishing and the commercial |

## Reference pack to generate (PROPOSED)

Generate these as **images** in Flow (Nano Banana) from **one master image**: generate the wide shot first, then make each later view as an edit or variation of it, so the room stays one room. Use empty-set plates (no people), so they can serve as location ingredients alongside the character references.

| File | View | Lighting |
| --- | --- | --- |
| `office-master-wide-golden.png` | `cam-c` wide, empty | Golden hour |
| `office-cam-a-golden.png` | `cam-a`, empty desk | Golden hour |
| `office-cam-b-golden.png` | `cam-b`, empty client chair | Golden hour |
| `office-cam-d-golden.png` | `cam-d`, chalkboard | Golden hour |
| `office-master-wide-day.png` | `cam-c` | Day |
| `office-master-wide-night.png` | `cam-c` | Night |
| `office-exterior-dusk.png` | `cam-e` storefront | Dusk |

### Showrunner direction for the re-roll (2026-11-22)

Take v01 was rejected for a re-roll. The direction:

- It must read as a **lawyer's office in a strip mall**. Take inspiration from Saul Goodman's office, but don't copy it: **no columns and no round windows**.
- Make it fit **Sophie's personality**, and show that she is a **philosopher**.
- There must be a **chair for the client**, facing the desk.
- **Keep the trolley drawing on the chalkboard** (v01's version was liked).

How the v02 prompt applies this: a big executive desk facing two client chairs, framed credentials and a waiting bench give the "small-time lawyer" read. It tries a little too hard to look important, in a gold-framed print of a classical painting of philosophers debating (PROPOSED set element). Books, the bust and the chalkboard make it a philosopher's room. The storefront window is put behind the camera, so its light comes in without a side wall of glass, which v01 got wrong.

### Master prompt v02 (PROPOSED, used for take v02)

```text
Empty interior of a small storefront office in an Albuquerque strip mall, year 2030, set up like a small-time lawyer's office but run by a young moral philosopher. Wide establishing shot from the front-door corner, eye level, 16:9. The back wall is floor-to-ceiling dark-wood bookshelves packed with worn philosophy books, with a small white marble Socrates bust on the top-right shelf. In front of the shelves stands a large, slightly scuffed dark walnut executive desk facing the front of the room, with a high-backed leather desk chair behind it; on the desk are a lit green glass banker's lamp, three stacked books, a closed silver laptop and a brass business-card holder. Two client chairs face the desk from the front: an oxblood leather wingback and a simpler matching visitor chair. On the left wall hangs a large slate chalkboard in a wooden frame with a hand-drawn chalk trolley-problem diagram: a trolley on tracks that split toward small stick figures. Beside the shelves hang framed diplomas and certificates, and a gaudy gold-framed print of a classical painting of ancient philosophers debating. A small waiting bench and a coat stand sit near the front. Warm cream plaster walls, a cheap drop ceiling, a faded Persian-style rug, a worn wood-look floor. The storefront window is behind the camera: golden-hour sun pours through its half-open venetian blinds and lays warm slatted shadows across the floor, desk and chairs. The mood is a strip-mall lawyer's office that tries a little too hard to look important, made scholarly and personal by its philosopher owner: confident, theatrical, a bit shabby, proud. No classical columns, no round windows, no flags, no statues of liberty. Photorealistic, cinematic, prestige TV production design. No people, no readable text, no logos, no watermarks.
```

### Master prompt v01 (superseded; used for take v01)

```text
Empty interior of a small philosophical consulting office in an Albuquerque strip-mall storefront, year 2030, wide establishing shot from the front-door corner, eye level, 16:9. Floor-to-ceiling dark-wood bookshelves cover the back wall, with a small Socrates bust on the top-right shelf. A scuffed dark walnut desk faces the front window, holding a green glass banker's lamp (lit), three stacked books and a closed silver laptop. An oxblood leather wingback client chair faces the desk. A slate chalkboard on the left wall shows a hand-drawn trolley-problem diagram. Warm cream plaster walls, a framed diploma, a faded Persian-style rug, wood-look floor. Golden-hour sunlight through half-open venetian blinds casts warm slatted shadows. Slightly shabby but proud and scholarly. Photorealistic, cinematic, prestige TV production design. No people, no readable text, no logos, no watermarks.
```

For each later view, use the master image as the reference and state the camera position from the table above. Keep the instruction "same room, same furniture positions, same props" and change only the camera or the lighting.

## Acceptance checks for the pack

1. Every view shows the same desk, lamp, chair, chalkboard, shelves and bust, in positions consistent with the floor plan.
2. Screen direction matches the floor plan (chalkboard on Sophie's right).
3. No people, no garbled text, no logos.
4. The showrunner approves the master wide. Only then are the other views generated, uploaded to the Flow project (`aao flow upload`), and logged here with Flow media names.

## Decisions

1. ~~Concept~~: strip-mall storefront, approved 2026-11-22.
2. ~~Floor plan and fixed set list~~: approved 2026-11-22.
3. Still open: approve the generated master wide image before the other views are made.
   - **v01** (2026-11-22): re-roll requested. [Log](../../../production/generation-logs/office-master-wide-golden-v01.yaml).
   - **v02** (2026-11-22, prompt v02, Nano Banana 2.1, 16:9, High): reads as a strip-mall lawyer's office with diplomas, two client chairs and the trolley chalkboard. Main deviations: the client chairs stand against the left wall instead of facing the desk, garbled chalk text beside the trolley, and the window is on the right wall again. [Log](../../../production/generation-logs/office-master-wide-golden-v02.yaml).
   - Images are in production storage (`production/exports/locations/sophie-office/`).
4. ~~Master wide~~: **v02 APPROVED by the showrunner on 2026-11-22.** The repo reference copy is [office-master-wide-golden.webp](office-master-wide-golden.webp). Its known deviations are accepted as they are: the client chairs stand against the left wall, there's garbled chalk text beside the trolley, the window is on the right wall, and the bookcases are freestanding. Later views should match the image, not the original floor plan, where the two differ.
5. Next: generate the other views from the master (`cam-a`, `cam-b`, `cam-d`, then day and night), upload the master and the views to the Flow project, and log each one.
