# Show canon and open decisions

**This document controls continuity.** Last initialized: 2026-11-14. Items become LOCKED only with the showrunner's explicit approval, not because an assistant invented them.

## LOCKED — series foundation

- **Title:** Better Call Sophie.
- **Lead:** **Dr. Sophie Goodman**, a woman who studied philosophy, is **Saul Goodman's granddaughter**.
- **Premise:** She operates a philosophical advocacy/consulting business, providing moral defenses with arguments from applied ethics, normative theory, and metaethics, in a Saul Goodman-inspired style.
- **Approach:** The entire original show production is intended to be **AI-generated**, with the user and ChatGPT as creative collaborators/directors.
- **Initial video-generation tool:** **Google Flow** (the stack may change or expand).
- **Visual development:** Promotional poster and two-sided Goodman Philosophical Consulting business-card concept art have already been generated.
- **Tone direction:** Philosophical drama/dark comedy inspired by Saul-style commercial bravado; serious philosophical conflict should underpin stories.
- **Era (LOCKED 2026-11-22):** The show is set in **2030**.
- **Sophie's age (LOCKED 2026-11-22):** **26–28 in 2030**, so born 2002–2004. That keeps the Goodman family timeline plausible. The exact birth year is still open, within that range.
- **Sophie's starting stance (LOCKED 2026-11-22):** **Mixed.** She starts as a deliberate hybrid: a principled advocate who also enjoys money, publicity and winning.

## LOCKED — production direction (showrunner, 2026-11-22)

- **Next milestone:** a **technical demo**, not the pilot. It is a 30-second commercial for the show, an opening title sequence (OP), and a few short test scenes under one minute each. Together they prove every technical piece a 5–8 minute pilot needs. Plan: `production/demo/README.md`.
- **Automation:** AI agents (Claude first) drive Google Flow and Google Flow Music through `external/any-agent-orchestrator` and check the outputs. The showrunner signs in to Google. See `spec/flow-automation.md`.
- **Music:** songs and score are generated with **Google Flow Music**.
- **Quality and cost:** draft quality is fine for now, and other tools may be tried later. The subscription plan covers credits, so cost does not limit tests.
- **Distribution:** test and demo videos go to the YouTube channel [@better-call-sophie](https://www.youtube.com/@better-call-sophie).
- **Sophie's office (APPROVED 2026-11-22):** the strip-mall storefront concept in `assets/locations/sophie-office/README.md`. The first floor plan was approved, then reopened the same day by the showrunner: the unit is mid-row, and Sophie's office is a private room separate from the waiting room. Floor plan v2 and its set list are PROPOSED until approved.
- **Sophie's Flow character info text (APPROVED 2026-11-22):** see `assets/characters/sophie-goodman/flow-character.md`. Her voice is not chosen yet.

## PROPOSED — do not mistake for final canon

- **Location:** Albuquerque, New Mexico, with national and international cases.
- **Family:** An unacknowledged daughter of Jimmy/Saul (working name Rebecca); Sophie adopting the Goodman professional name; Jimmy alive and incarcerated.
- **Supporting cast:** Professor Elena Salazar (academic rival), Daniel Park (AI/marketing partner), Maria Ortega (attorney), Rebecca Hart (mother).
- **Main antagonist:** A private ethics-rating organization dubbed The Integrity Index.
- **Season 1:** 10 episodes; tentative titles and plots in `story/season-01/overview.md`.
- **Client model:** Mix of pro bono cases and profitable corporate clients.
- **Taglines:** "Morally Questionable? Philosophically Defensible."; "Grandpa found loopholes in the law. I find loopholes in morality."

## Open decisions

1. Determine the exact family tree/timeline that respects or deliberately departs from existing franchise continuity.
2. Sophie's age is resolved (26–28, LOCKED above); her exact birth year and her mother's timeline are still open. Also decide whether original TV characters appear, and how direct the franchise references are.
3. Define season length, episode duration (the pilot target is 5–8 minutes, pending the demo), screen aspect ratio, audio languages and target release format.
4. Approve a canonical Sophie face/voice/wardrobe reference set; current art is **concept**.
5. ~~Sophie's starting stance~~ — resolved: mixed (LOCKED above).
6. Establish the practical institution that can make philosophical arguments dramatically consequential.
7. Review third-party franchise rights before any external distribution or commercialization.

## How to change canon

Propose a change as a separate paragraph with implications for affected characters, episodes and assets. Ask for explicit showrunner acceptance if needed. Once approved, mark it LOCKED here and update any affected `story/` files and production prompts. Preserve major retired choices in an ADR or commit message; don't silently rewrite history.
