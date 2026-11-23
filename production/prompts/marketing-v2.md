# Marketing v2 — poster and business card art

**Status:** PROPOSED prompts, first used on 2026-11-23. Showrunner direction (2026-11-23): regenerate the TV poster and the business card with Sophie's approved face; set the poster in her approved office; make text-free art in Flow and add all lettering afterwards; card logo is the owl with scales and **no column**.

All takes: Google Flow image mode, Nano Banana 2.1, x1, Flow agent off, in the work project. References are Flow media names in that project. Lettering is added by [scripts/compose_marketing.py](../../scripts/compose_marketing.py), so each prompt asks for no text and leaves room for it.

## poster-art v01 (4:3, Sophie in her office)

References, in this order: `Character design reference photo…` (portrait v02, its media name in the work project), `Lawyer private office layout` (office master v03).

```text
Use the first attached image only for the woman's face, hair, earrings and coloring, and the second attached image for the room: Sophie Goodman's private office in a strip-mall storefront, with the walnut desk, green banker's lamp, the slate chalkboard with the chalk trolley-problem drawing, framed diplomas, tall dark-wood bookcases with worn books and a small white bust, half-open venetian blinds. A cinematic TV-series key art photograph, 4:3 horizontal. Sophie Goodman, a confident woman in her late twenties, stands on the left third of the frame, leaning back against the front edge of her desk, in a deep burgundy tailored pantsuit and cream silk blouse, small gold hoop earrings, dark wavy hair loosely pinned up with a few loose curls. One hand in her trouser pocket, the other holding a closed, worn leather-bound book against her hip. A wry, self-assured half-smile, looking straight at the camera. Behind her on the left, the chalkboard with only the trolley drawing; behind her on the right, the window and bookcases. Warm golden late-day light slants through the blinds in long stripes; deep rich shadows; shallow depth of field. The upper right third of the frame is calm and uncluttered, darker blinds and bookcase in soft focus, leaving room for a title to be added later. No words, letters, numbers, logos or signs anywhere: the book cover and spine are blank, the diplomas unreadable, the chalkboard has no writing. No other people, no watermarks. Photorealistic, prestige TV production design.
```

## poster-lettered v01 (4:3, poster with generated title lettering)

Showrunner request (2026-11-23): "for the tv poster, generate one with the text, using the font of the old poster." This is an exception to adding text afterwards; check the spelling before approving.

References, in this order: `Woman standing in office` (poster-art v01, the approved poster art), `sophie-poster-concept-ref.png` (the 2026-11-14 concept poster, for its lettering only).

```text
Use the first attached image as the finished photograph: keep the woman, her face, pose, clothes, the office, the light and the framing exactly as they are. Add TV-series poster lettering that copies the typography of the second attached image, an older poster for the same show, and take nothing else from that second image. In the upper right: "BETTER CALL" in bold white italic sans-serif capitals, and directly below it "SOPHIE" much larger, in heavy golden-yellow italic capitals with a slight forward slant and a thin gold swoosh underline. Under that, on two lines in an elegant cream serif italic: "Morally Questionable?" and "Philosophically Defensible.", followed by a thin gold swoosh. Along the bottom center, small, widely letter-spaced cream serif italic: "A philosophical crime drama", between two short thin horizontal lines. A soft dark shadow behind the lettering so it reads clearly over the window. Spell every word exactly as given. No other words, logos or watermarks; the book, diplomas and chalkboard stay blank. 4:3 horizontal.
```

## card-photo v01 (16:9, card front photo)

Reference: `Character design reference photo…` (portrait v02).

```text
Use the attached image as the reference for the woman: the same face, age, dark wavy hair loosely pinned up with loose curls, small gold hoop earrings, cream blouse and deep burgundy tailored blazer. A bold, bright advertising photograph for a small business card, 16:9 horizontal. She stands on the right third of the frame, waist up, turned slightly toward the left, pointing her right index finger straight at the camera with a confident, playful half-smile and one eyebrow slightly raised, like a local TV-ad lawyer. Flat, seamless, saturated warm yellow studio backdrop filling the whole frame, even bright commercial lighting with a soft shadow. The left two-thirds of the frame is plain yellow and empty, leaving room for text to be added later. No words, letters, numbers, logos, props, other people or watermarks. Photorealistic.
```

## card-logo v01 (1:1, emblem)

No reference.

```text
A flat, two-color vector-style emblem on a plain saturated warm yellow background, centered, 1:1. A wise owl of Minerva perched on top of a classic brass balance scale with two hanging pans, framed below by a pair of curved laurel branches. Dark burgundy-brown ink on the yellow, bold clean shapes, simple line detail, like a vintage legal-office logo or a rubber stamp. No column, no pillar, no pedestal, no building. No words, letters, numbers, banners or watermarks.
```
