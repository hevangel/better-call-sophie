# Location: Goodman Philosophical Consulting — Sophie's office

**Status:** design **APPROVED** by the showrunner (2026-11-22): concept, floor plan and fixed set list. The reference pack is **not generated yet**. From now on, changes to the floor plan or set list need a documented reason. Needed before the next round of Flow tests, because continuity was the weakest result of the tutorial run.

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

### Master prompt (PROPOSED)

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
3. Still open: approve the generated master wide image before the other views are made. **Take v01 was generated on 2026-11-22** (Nano Banana 2.1, 16:9, High). It's logged with an agent review in [production/generation-logs/office-master-wide-golden-v01.yaml](../../../production/generation-logs/office-master-wide-golden-v01.yaml); the image itself is in production storage (`production/exports/locations/sophie-office/`). Main deviations: the storefront glass is on the right wall instead of the front, the client chair doesn't face the desk, and the shelves are not floor-to-ceiling. **Decision needed:** approve v01 as the master, or re-roll.
