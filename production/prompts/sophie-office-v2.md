# Prompts: Sophie's office, floor plan v2

**Status:** PROPOSED prompts for the floor plan v2 masters, first used on 2026-11-22. The layout is in [the office README](../../assets/locations/sophie-office/README.md). Results and reviews are in `production/generation-logs/`.

All takes: Flow image mode, Nano Banana 2.1, 16:9, x1, Flow agent off. Each prompt names its reference images in the order they are attached ("first", "second"). The references are earlier takes in the Flow project `d0b10764-5004-4f27-9269-a447a70807fe`:

- **master v02**: Flow media "Philosopher office in strip mall" (`office-master-wide-golden` v02), for the furniture and props.
- **exterior v01**: Flow media "Office storefront in strip mall" (`office-exterior-dusk` v01), for the building.
- **waiting v02**: Flow media "Empty waiting room interior view" (`office-waiting-wide-golden` v02), for the waiting room.

## office-master-wide-golden v03 (`cam-c`, Sophie's private office)

References: master v02.

```text
Use the attached image only as the reference for the furniture, props, materials and colors: the same dark walnut executive desk, high-backed brown leather chair, green glass banker's lamp, stacked books, silver laptop, oxblood tufted leather wingback, brown leather visitor chair, slate chalkboard with the chalk trolley drawing, framed diplomas, two tall dark-wood bookcases and small white bust. Arrange them in a different, enclosed room: the private office at the back of a strip-mall storefront unit, a small closed room with solid walls and no storefront glass. Wide establishing shot from the open office door in the front-right corner of the room, eye level, looking diagonally toward the back-left corner. The back wall faces the camera: one rear window with half-open venetian blinds in the middle, flanked by the two bookcases, the bust on top of the right one. In front of the window stands the desk, facing the camera and the door, with the high-backed chair behind it, so whoever sits there has her back to the window. Two client chairs stand in front of the desk and face it, their backs toward the camera: the oxblood wingback on the left and the visitor chair on the right. The left wall is solid: the chalkboard with only the trolley drawing and no writing, the six framed diplomas beside it, and two battered beige metal filing cabinets near the front corner. Low golden morning sun comes through the rear blinds behind the desk and lays long warm slatted shadows toward the camera across the desk, the rug and the client chairs; the banker's lamp is lit. Warm cream plaster walls, a cheap drop ceiling, a faded Persian-style rug, a worn wood-look floor. A small-time lawyer's private office made scholarly by a young philosopher: confident, a bit shabby, proud, private. No storefront window, no side windows, no classical columns, no round windows. No people, no writing on the chalkboard, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-waiting-wide-golden v01 (`cam-w1`, waiting room toward the storefront)

References: exterior v01.

```text
Use the attached image as the reference for the storefront: the same strip-mall unit, seen now from the inside, with its large window with half-open venetian blinds on the left and its glass front door on the right. Interior of the small waiting room at the front of a one-person philosopher-advocate's office in an Albuquerque strip mall, year 2030. Wide shot from the back of the waiting room, eye level, looking toward the street. The left two-thirds of the front wall is the storefront window with half-open venetian blinds, the parking lot beyond; on the right is the glass front door. Under the window: three mismatched waiting chairs and a low side table with a few magazines. In the left corner: a water cooler and a cheap coffee maker on a small cabinet. Beside the front door: a wooden coat stand and a tired potted plant. In the right foreground, the edge of a small cheap reception desk, unstaffed, with a brass desk bell. Late-afternoon golden sun pours through the blinds and lays warm slatted shadows across the floor and the chairs. Warm cream plaster walls, a cheap drop ceiling with fluorescent panels, worn wood-look laminate floor. Modest, a little shabby, trying to look respectable. This room has no executive desk, no banker's lamp, no chalkboard and no bookcases. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-waiting-wide-golden v02 (`cam-w1`, re-roll)

v01 showed the Sandia mountains through the storefront. In the exterior the mountains are behind the building, so the street side must not show them. References: exterior v01.

```text
Use the attached image as the reference for the storefront: the same strip-mall unit, seen now from the inside, with its large three-pane window with half-open venetian blinds on the left and its glass front door on the right. Interior of the small waiting room at the front of a one-person philosopher-advocate's office in an Albuquerque strip mall, year 2030. Wide shot from the back of the waiting room, eye level, looking toward the street. The left two-thirds of the front wall is the storefront window with half-open venetian blinds; on the right is the glass front door. Through the glass: the strip-mall parking lot, a busy four-lane road, and a row of low flat-roofed commercial buildings and a gas station across the road under a flat open sky. No mountains are visible from this side: the mountains are behind the building. Under the window: three mismatched waiting chairs and a low side table with a few magazines. In the left corner: a water cooler and a cheap coffee maker on a small cabinet. Beside the front door: a wooden coat stand and a tired potted plant. In the right foreground, the edge of a small cheap reception desk, unstaffed, with a brass desk bell. Late-afternoon golden sun pours through the blinds and lays warm slatted shadows across the floor and the chairs. Warm cream plaster walls, a cheap drop ceiling with fluorescent panels, worn wood-look laminate floor. Modest, a little shabby, trying to look respectable. This room has no executive desk, no banker's lamp, no chalkboard and no bookcases. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-waiting-hall-golden v01 (`cam-w2`, waiting room toward the office door)

References: waiting v02 (first), master v02 (second).

```text
Use the first attached image as the reference for the waiting room: the same walls, floor, ceiling, waiting chairs, reception desk and golden light. Use the second attached image only for the gold-framed painting. Interior of the same small waiting room, now seen from just inside the glass front door, eye level, looking into the unit away from the street. The back wall of the waiting room is a solid partition wall. The gaudy gold-framed classical painting of philosophers hangs in the middle of it, the first thing a visitor sees. In front of the painting stands the small cheap reception desk, unstaffed, facing the camera, with a brass desk bell and a card holder. To the right of the partition, an opening leads into a narrow hallway that runs straight back: on the hallway's left side, a closed solid dark-wood office door with a small brass plate and a small white-noise machine on the floor beside it; at the far end of the hallway, a restroom door and a gray steel back door. The waiting chairs and the side table stand along the left wall. Late-afternoon golden sun from the storefront behind the camera throws warm slatted blind shadows across the floor, the desk and the partition. Warm cream plaster walls, a cheap drop ceiling, worn wood-look laminate floor. Sophie's office is hidden behind the partition and the closed door: private. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-waiting-hall-golden v02 (`cam-w2`, re-roll)

v01 put the office door on the hallway's right wall, which is the wall shared with the tax office next door, and showed two water coolers. References: hall v01 (Flow media "Waiting room interior view").

```text
Keep the same room, camera position, framing, golden light, gold-framed painting, reception desk, waiting chairs and side table as the attached image, with these changes only. The narrow hallway on the right runs straight back from the waiting room. Its left wall continues the partition wall that holds the painting, and in that left wall, near the waiting room, is a closed solid dark-wood office door with a small brass plate, with a small white-noise machine on the floor beside it: this door leads to the private office behind the painting. The hallway's right wall is a plain, blank wall with no doors at all. At the far end of the hallway, side by side: a restroom door and a gray steel back door. There is only one water cooler, at the far left of the frame; remove the water cooler and the coffee maker from the right edge. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-waiting-hall-golden v03 (`cam-w2`, re-roll)

v02 still put the office door on the hallway's right wall: from the front door the hallway's left wall is seen almost edge-on, so the model can't show a door there. This prompt asks for the door on the partition's front face. Flow put it at the partition's right end, opening onto the mouth of the hallway, which is where floor plan v2 has it. References: hall v02 (Flow media "Modify waiting room interior design").

```text
Keep the same room, camera position, framing, golden light, gold-framed painting, reception desk, waiting chairs, side table and water cooler as the attached image, with these changes only. Move the dark-wood office door with the small brass plate onto the front face of the partition wall that holds the painting: the door stands at the right end of that wall, to the right of the reception desk, facing the camera and the waiting room, closed. The small white-noise machine sits on the floor beside that door. To the right of the door, the hallway opening leads straight back to a restroom door and a gray steel back door at its far end. The hallway's right wall is a plain, blank wall with no doors at all. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-exterior-dusk v02 (`cam-e`, exterior)

References: exterior v01 (first), waiting v02 (second).

```text
Keep exactly the same strip mall, building, neighboring shops, sign panel, mountains, sky, parking lot, camera position and framing as the first attached image. Change only what is seen through the storefront. Through the window with half-open venetian blinds, the warmly lit waiting room from the second attached image: mismatched waiting chairs, a side table, a water cooler, cream walls. Through the glass door on the right, a narrow hallway running straight back with a closed wooden office door on its left side. There is no desk, no banker's lamp and no bookcase visible from the street: Sophie's private office is a separate room at the back, out of sight. The sign panel above the window is a clean, blank, gaudy yellow and red panel. The neighboring shop signs are blank and out of focus, with no neon lettering. No lens flare. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## Views from the approved office master v03

Each view attaches **office master v03** (Flow media "Lawyer private office layout") as the only reference. Each prompt starts with `<office anchor>`, replaced by the block below before submitting. Take numbers continue from the floor plan v1 takes with the same IDs. The anchor describes the room as v03 shows it: the camera of v03 stands in the open door, at the front end of the right wall.

## Office anchor

```text
Use the attached image as the reference for the room: the same room, same furniture positions, same props, same materials and colors. Sophie Goodman's private office at the back of a strip-mall storefront unit, a small closed room with solid walls. Back wall: one window with half-open venetian blinds in the middle, flanked by two tall dark-wood bookcases packed with worn books, a small white bust on top of the right bookcase. In front of the window: a dark walnut executive desk facing the front of the room, a high-backed brown leather chair behind it, a green glass banker's lamp, three stacked books, a silver laptop and a brass card holder on the desk. In front of the desk, facing it: an oxblood tufted leather wingback on the left and a brown leather visitor chair on the right. Left wall: a slate chalkboard in a wooden frame with only a chalk trolley-problem drawing, six framed diplomas beside it, two battered beige metal filing cabinets near the front corner. Right wall: plain, with a solid dark-wood door at its front end. Warm cream plaster walls, a cheap drop ceiling, a faded Persian-style rug, a worn wood-look floor.
```

## office-cam-a-golden v02 (`cam-a`, toward the desk)

```text
<office anchor> New camera position: medium-wide shot from just behind the two client chairs, at seated eye level, looking straight at the empty desk and the empty high-backed chair. The tops of the wingback (left) and the visitor chair (right) are soft in the foreground. Behind the desk: the window with half-open blinds between the two bookcases, the bust on the right bookcase. The edge of the chalkboard is at the left edge of the frame. Low golden morning sun shines through the blinds behind the desk, toward the camera: a warm backlight, slatted light across the desktop, the banker's lamp lit. No people, no writing on the chalkboard, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-cam-b-golden v02 (`cam-b`, reverse toward the client chairs)

```text
<office anchor> New camera position: the reverse angle. The camera stands behind the desk, just beside the empty high-backed chair, at seated eye level, looking toward the front of the room, away from the window. The edge of the desk, the lit banker's lamp and the stacked books are soft in the foreground. The two empty client chairs face the camera: the wingback on the right of the frame and the visitor chair on the left. Behind them, the plain front wall of the room. On the right of the frame: the chalkboard wall, with the filing cabinets in the front corner. On the left of the frame: the plain wall with the solid dark-wood door at its front end, closed. No storefront glass and no window in view. Low golden morning sun from the window behind the camera lays long warm slatted shadows forward across the rug, the chairs and the front wall. No people, no writing on the chalkboard, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-cam-d-golden v02 (`cam-d`, toward the chalkboard)

```text
<office anchor> New camera position: from the right side of the room, beside the visitor chair, at standing eye level, looking straight at the left wall. The slate chalkboard with the chalk trolley drawing is square to the camera in the center of the frame, the six framed diplomas to its right and the filing cabinets at the right edge. In the left foreground, the end of the desk and the lit banker's lamp; the back of the wingback in the lower right foreground. On the left edge of the frame, the corner of a bookcase and the window blinds. Warm golden morning sun from the window on the left throws slatted light across the chalkboard wall. The chalkboard shows only the trolley drawing: tracks that split, a trolley, small stick figures, a lever, and no words. No people, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-master-wide-day v03 (`cam-c`, day)

```text
<office anchor> Keep exactly the same camera position, framing, furniture and props as the reference image. Relight the whole scene as midday: no golden or orange light anywhere. Bright, neutral white daylight comes through the half-open blinds of the window behind the desk and throws crisp white stripes across the desk, the chairs and the rug. Walls pale cream under neutral light, cool gray shadows. The green banker's lamp is switched OFF and dark. Overall color temperature: cool daylight, around 6500K. No people, no writing on the chalkboard, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```

## office-master-wide-night v02 (`cam-c`, night)

```text
<office anchor> Keep exactly the same camera position, framing, furniture and props as the reference image. Change only the lighting to night: the window behind the desk is black, its blinds almost closed, and the room is dark except for the lit green banker's lamp, which pools warm light on the desk, the stacked books and the two client chairs. A faint warm spill of light comes from the hallway through the open door in the right foreground. Deep shadows on the bookcases, the chalkboard and the ceiling. No people, no writing on the chalkboard, no readable text, no logos, no watermarks. Photorealistic, cinematic, prestige TV production design, 16:9.
```
