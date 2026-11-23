# Prompts: Sophie's office reference views (v01)

**Status:** SUPERSEDED on 2026-11-22 by floor plan v2 ([prompts](sophie-office-v2.md)). These prompts were used for the first generation of each view on 2026-11-22, and are kept because the logs in `production/generation-logs/office-*-v01.yaml` point here. The floor plan v1 master prompts are at the end of this file.

Each view is made in Flow image mode (Nano Banana 2.1, 16:9, High, x1), with the **approved master wide v02** attached as the only reference image (Flow's "Add to prompt"). The master is [office-master-wide-golden.webp](../../assets/locations/sophie-office/office-master-wide-golden.webp), Flow media "Philosopher office in strip mall" in project `d0b10764-5004-4f27-9269-a447a70807fe`.

The prompts describe the room **as the master shows it**, not as the original floor plan drew it, because the showrunner accepted v02's layout (see the office README, decision 4). In the master, the camera is at the front-door corner. The left wall has the chalkboard, the diplomas and the two client chairs. The back wall has two freestanding bookcases with the gold-framed painting between them. The desk faces the camera. The right wall has the window with blinds, the coat stand and the bench.

## Shared anchor (starts every prompt)

```text
Use the attached image as the reference for the room: the same room, same furniture positions, same props, same materials and colors. The room: a small strip-mall office of a young philosopher, set up like a small-time lawyer's office. Left wall: a large slate chalkboard in a wooden frame with a chalk trolley-problem drawing, six framed diplomas beside it, an oxblood tufted leather wingback and a brown leather visitor chair standing against the wall. Back wall: two freestanding dark-wood bookcases full of worn books, a gold-framed classical painting between them, a small white bust on top of the right bookcase. Center: a dark walnut executive desk with a high-backed brown leather chair behind it, a green glass banker's lamp, three stacked books and a silver laptop. Right wall: a window with half-open venetian blinds, a wooden coat stand and a small upholstered bench. Drop ceiling, cream plaster walls, faded Persian-style rug, worn wood-look floor.
```

## Views

### office-cam-a-golden (`cam-a`, empty desk, golden hour)

```text
<shared anchor> New camera position: medium-wide shot from the client side of the desk, at seated eye level, about two meters in front of the desk, looking straight at the empty desk and the empty high-backed leather chair behind it. The bookcases, the gold-framed painting and the bust fill the background. The banker's lamp is lit. Golden-hour sun from the window on the right throws warm slatted shadows across the desk and the back wall. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-cam-b-golden (`cam-b`, reverse toward the client chairs and the front)

```text
<shared anchor> New camera position: the reverse angle. The camera stands just behind the empty desk chair at seated eye level and looks toward the front of the room. The edge of the desk and the lit banker's lamp are soft in the foreground. Across the room, the oxblood wingback and the leather visitor chair now stand against the wall on the right of the frame, below the chalkboard's edge, and the window with venetian blinds is on the left of the frame. Straight ahead is the storefront: a glass front door and a large front window with half-open blinds, a strip-mall parking lot outside, golden-hour sun pouring in. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-cam-d-golden (`cam-d`, beside the chalkboard)

```text
<shared anchor> New camera position: side-on, standing against the left wall right beside the chalkboard, looking across the room toward the window. The chalkboard with the chalk trolley drawing is large in the left foreground, at a steep angle. The desk and the empty high-backed chair are in profile in the middle ground. The coat stand, the bench and the window with half-open venetian blinds are in the background, with golden-hour sunlight streaming through the slats. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-master-wide-day (`cam-c`, day)

```text
<shared anchor> Keep exactly the same camera position and framing as the reference image. Change only the lighting to midday: hard, bright New Mexico daylight through the half-open blinds on the right, crisp slatted shadows on the floor, rug and furniture, a cool neutral fill, and the banker's lamp switched off. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-master-wide-day-v02 (`cam-c`, day; re-roll)

v01 of the day view came back still golden, with the lamp on. This version names the change more strongly.

```text
<shared anchor> Keep exactly the same camera position, framing, furniture and props as the reference image. Relight the whole scene as harsh high noon: no golden or orange light anywhere. Cool, bright, white New Mexico daylight blasts through the half-open blinds on the right and throws crisp, high-contrast white stripes on the floor, rug and chairs. The walls look pale cream under neutral light, with cool bluish-gray shadows. The green banker's lamp is switched OFF and dark. Overall color temperature: cool daylight, around 6500K. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-master-wide-night (`cam-c`, night)

```text
<shared anchor> Keep exactly the same camera position and framing as the reference image. Change only the lighting to night: the room is dark except for the lit green banker's lamp, which pools warm light on the desk and the nearby chairs, and a yellow and red glow from an outdoor street sign coming through the blinds on the right. Deep shadows on the bookcases, the painting and the ceiling. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

### office-exterior-dusk (`cam-e`, exterior)

```text
Use the attached image as the reference for the office interior seen through the window. Exterior of that office: a small storefront unit in a single-story Albuquerque strip mall at dusk, year 2030, seen from across the parking lot at eye level, 16:9. It sits between a vape shop and a tax-preparation office. The storefront has a glass door and a large window with half-open venetian blinds; through them you can glimpse the warm interior from the reference image: the bookcases, the lit green banker's lamp and the desk. Above the window, a gaudy bright yellow and red sign panel with blank lettering. The neighboring shop signs are plain and out of focus. Sandia mountains are silhouetted in the distance under a purple and orange sky; parking lot lights are coming on over empty spaces. Gaudy outside, scholarly inside. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design.
```

## Floor plan v1 masters (superseded)

Moved here from the office README on 2026-11-22, when floor plan v2 replaced it.

### Master prompt v02 (used for office-master-wide-golden v02)

```text
Empty interior of a small storefront office in an Albuquerque strip mall, year 2030, set up like a small-time lawyer's office but run by a young moral philosopher. Wide establishing shot from the front-door corner, eye level, 16:9. The back wall is floor-to-ceiling dark-wood bookshelves packed with worn philosophy books, with a small white marble Socrates bust on the top-right shelf. In front of the shelves stands a large, slightly scuffed dark walnut executive desk facing the front of the room, with a high-backed leather desk chair behind it; on the desk are a lit green glass banker's lamp, three stacked books, a closed silver laptop and a brass business-card holder. Two client chairs face the desk from the front: an oxblood leather wingback and a simpler matching visitor chair. On the left wall hangs a large slate chalkboard in a wooden frame with a hand-drawn chalk trolley-problem diagram: a trolley on tracks that split toward small stick figures. Beside the shelves hang framed diplomas and certificates, and a gaudy gold-framed print of a classical painting of ancient philosophers debating. A small waiting bench and a coat stand sit near the front. Warm cream plaster walls, a cheap drop ceiling, a faded Persian-style rug, a worn wood-look floor. The storefront window is behind the camera: golden-hour sun pours through its half-open venetian blinds and lays warm slatted shadows across the floor, desk and chairs. The mood is a strip-mall lawyer's office that tries a little too hard to look important, made scholarly and personal by its philosopher owner: confident, theatrical, a bit shabby, proud. No classical columns, no round windows, no flags, no statues of liberty. Photorealistic, cinematic, prestige TV production design. No people, no readable text, no logos, no watermarks.
```

### Master prompt v01 (used for office-master-wide-golden v01)

```text
Empty interior of a small philosophical consulting office in an Albuquerque strip-mall storefront, year 2030, wide establishing shot from the front-door corner, eye level, 16:9. Floor-to-ceiling dark-wood bookshelves cover the back wall, with a small Socrates bust on the top-right shelf. A scuffed dark walnut desk faces the front window, holding a green glass banker's lamp (lit), three stacked books and a closed silver laptop. An oxblood leather wingback client chair faces the desk. A slate chalkboard on the left wall shows a hand-drawn trolley-problem diagram. Warm cream plaster walls, a framed diploma, a faded Persian-style rug, wood-look floor. Golden-hour sunlight through half-open venetian blinds casts warm slatted shadows. Slightly shabby but proud and scholarly. Photorealistic, cinematic, prestige TV production design. No people, no readable text, no logos, no watermarks.
```
