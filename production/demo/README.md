# Technical demo — plan

**Status:** milestone LOCKED by the showrunner (2026-11-22); all scene content and scripts below are **PROPOSED**. Nothing has been generated for the demo yet.

**Purpose:** find out what Google Flow (with Flow Music and post-production) can do **reliably**, using short pieces, before writing the 5–8 minute pilot. Quality is not the goal yet. The goal is to have every technical piece working at least once, and repeatably, with agents driving the work ([spec/flow-automation.md](../../spec/flow-automation.md)).

## Pieces

| ID | Piece | Length | File |
| --- | --- | --- | --- |
| **D01** | Show commercial (Sophie's TV ad) — **first deliverable** | 30 s | [d01-commercial-30s.md](d01-commercial-30s.md) |
| **OP** | Opening title sequence with theme song | 30 s (60 s full version optional) | [op-opening-titles.md](op-opening-titles.md) |
| **T1** | The Consultation — two-person dialogue | ~45 s | [t1-consultation.md](t1-consultation.md) |
| **T2** | Walk and Talk — movement, interior → exterior | ~40 s | [t2-walk-and-talk.md](t2-walk-and-talk.md) |
| **T3** | The Hearing — group scene, long argument | ~55 s | [t3-hearing.md](t3-hearing.md) |
| **T4** | After Hours — night lighting, voice-over, screen insert | ~40 s | [t4-after-hours.md](t4-after-hours.md) |

## What each piece proves

The pilot needs every row. ● = the main test, ○ = also used.

| Technical piece | D01 | OP | T1 | T2 | T3 | T4 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| Sophie's identity across many shots | ● | ○ | ● | ○ | ○ | ○ |
| A second or third recurring character | | | ● | ● | ● | |
| Office continuity (the [location pack](../../assets/locations/sophie-office/README.md)) | ● | ○ | ● | ○ | | ● |
| Same set, different lighting state | | | | | | ● |
| New locations (exterior, institution) | | ○ | | ● | ● | |
| Single-speaker dialogue and lip sync | ● | | ● | ○ | ● | |
| Shot/reverse shot, eyelines | | | ● | | ● | |
| Three or more people in one scene | | | | | ● | |
| A speech longer than one generation (Extend or split coverage) | | | | | ● | |
| Camera and character movement | | ○ | | ● | | |
| Prop continuity and hand-offs | ○ | | ● | ● | | |
| Silent stylized shots and cutting to music | | ● | | | | |
| Text added in post (titles, end card, phone screen) | ● | ● | | | | ● |
| Theme song (Flow Music) | | ● | | | | |
| Jingle, score cue (Flow Music) | ● | | | | | ● |
| Voice-over, room tone, sound effects, final mix | ● | ○ | ○ | ● | ○ | ● |
| Assembly outside Flow (ffmpeg / Remotion) vs Scenebuilder | ● | ● | ○ | ○ | ○ | ○ |
| Subtitles (Whisper) | ○ | | ● | ○ | ● | ○ |
| Agent loop: generate → download → check → log | ● | ● | ● | ● | ● | ● |
| YouTube upload with disclosure | ● | ● | ○ | ○ | ○ | ○ |

## Order of work

1. **Automation setup** on the showrunner's computer: AAO prerequisites, Google sign-in, and a check with `aao flow status` ([spec/flow-automation.md](../../spec/flow-automation.md#where-it-runs)).
2. **Character sync:** copy the Sophie character from Flow into [assets/characters/sophie-goodman/flow-character.md](../../assets/characters/sophie-goodman/flow-character.md). Check that the portrait reads as 26–28 and regenerate it if not. Enter the approved info text, then choose the voice.
3. **Office reference pack** (design approved; [assets/locations/sophie-office/README.md](../../assets/locations/sophie-office/README.md)): the master wide shot, then the other angles once the showrunner approves the master.
4. **D01 commercial**, the first deliverable.
5. **OP**, which can run in parallel with step 4 because it needs few character shots.
6. **T1 → T2 → T3 → T4.** Each adds one hard problem.
7. **Write-up:** what Flow does reliably, what needs other tools, and what the pilot script must avoid. This decides the pilot's format and how it is written.

## Shared conventions

- Shot IDs: `demo-d01-sh01`, `demo-op-sh03`, `demo-t2-sh04`; takes `-v01`, `-v02`.
- Every shot gets a record in `production/shot-lists/demo/` and a generation log ([production-pipeline.md](../../spec/production-pipeline.md)).
- 16:9, one output per generation. Use whichever Flow model `aao flow options` shows. Omni Flash 1.2 is the working default, because Veo 3.1 Fast/Quality and Omni Flash 1.1 retire on 2026-12-05.
- **Only lock down what is reused** (showrunner, 2026-11-23). Characters, locations and props that come back in other shots get reference images and continuity checks. One-shot cameos and throwaway locations (such as the client and kitchen in D01 shot 2) are described in the prompt and need no reference or continuity.
- **One speaker per generation.** Readable text (logos, phone numbers, screens, nameplates) is added in post, never generated. The exception is a showrunner-approved comparison test, such as D01 shot 4, which makes the same shot with generated text and with text added in post.
- **Text and graphics in post use traditional editing tools** (ffmpeg, OpenCV, Blender, Remotion), not AI regeneration. See [production-pipeline.md](../../spec/production-pipeline.md#post-production-text-and-graphics).
- Original fictional people only: no real actors' likenesses or voices, and no franchise footage or music.
