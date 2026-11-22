# Tutorial run — results (first pilot experiments)

**Status:** completed by hand by the showrunner and reported on 2026-11-22. This is a learning exercise, not production footage.

## What the showrunner reported

- Ran every experiment in [tutorial-first-pilot.md](tutorial-first-pilot.md) (A, B1/B2, C1–C3, Scenebuilder assembly) with **exactly the tutorial's prompts**, unchanged.
- **Results:** all good enough for learning. **Continuity was the weakest area.**
- **Scorecard:** not filled in, on purpose. It was for learning, not a production gate.
- **Cost:** not tracked. The subscription plan covers it, so credits are not a constraint.
- **Characters:** the Sophie character exists in Flow, but its **character details (info text) and voice have not been set yet**.
- **Published:** the test videos are on YouTube at [@better-call-sophie](https://www.youtube.com/@better-call-sophie).

## Not yet recorded (do not invent)

These will be filled in by the first automated sync (see [spec/flow-automation.md](../../spec/flow-automation.md)) or by the showrunner:

- Flow project ID and title
- The model, resolution and duration actually used for each clip
- Flow character ID(s) and whether a separate "Client" character was created
- Individual YouTube video URLs
- Where the local downloads are stored

## Lessons that change the plan

1. **Continuity is the main technical risk.** Sophie's office now gets a dedicated location reference pack before any more scene work ([assets/locations/sophie-office/README.md](../../assets/locations/sophie-office/README.md)). Every demo test scene also checks continuity explicitly.
2. **Finish the character setup in Flow** (info text and voice) before the next round, so `@Sophie Goodman` carries a fixed voice. A proposed info text is in [assets/characters/sophie-goodman/flow-character.md](../../assets/characters/sophie-goodman/flow-character.md).
3. **Next round is automated.** Agents drive Flow through any-agent-orchestrator. Steps it cannot do yet stay manual but are logged the same way.
