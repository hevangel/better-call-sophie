# Instructions for AI agents — Better Call Sophie

Read this file **before** changing anything. It is short by design; detailed instructions are under `spec/`.

## Mission

Help the human showrunner develop and produce **Better Call Sophie**, an AI-generated philosophical drama. The show is collaboratively directed by the user and ChatGPT; Google Flow is the *initial* video-generation environment, not an exclusive or permanent dependency.

## Current direction (showrunner, 2026-11-22)

- **The milestone is a technical demo, not the pilot:** a 30 s show commercial first, then an opening title sequence (OP) and short test scenes under one minute each. Together they prove every technical piece a 5–8 minute pilot needs. Plan: [production/demo/README.md](production/demo/README.md).
- **Agents drive Google Flow and Flow Music** through `external/any-agent-orchestrator` (AAO), then check and log the results. See [spec/flow-automation.md](spec/flow-automation.md). Music and songs come from **Flow Music**.
- **Don't optimize for quality or cost yet.** Draft quality is fine, other tools may be tried later, and the subscription plan covers credits. Continuity is the known weak spot, so build the reference packs (Sophie's character, [Sophie's office](assets/locations/sophie-office/README.md)) before scenes.
- **Era is 2030; Sophie starts mixed** (principled and mercenary). Both are LOCKED in `spec/canon.md`.
- **Videos are published** on YouTube at [@better-call-sophie](https://www.youtube.com/@better-call-sophie).

## Required reading and priority

1. **This file** — work process and non-negotiables.
2. [spec/canon.md](spec/canon.md) — accepted facts; never silently contradict these.
3. [spec/series-bible.md](spec/series-bible.md) — premise, cast, themes, evolving setting.
4. [spec/style-guide.md](spec/style-guide.md) — creative and visual consistency.
5. [spec/production-pipeline.md](spec/production-pipeline.md), [spec/flow-automation.md](spec/flow-automation.md) and [spec/asset-manifest.md](spec/asset-manifest.md) — generated asset workflow, Flow automation, storage, provenance. The hand-run Flow tutorial is done ([results](production/google-flow/tutorial-run-results.md)).
6. [spec/ai-creative-policy.md](spec/ai-creative-policy.md) and [spec/third-party.md](spec/third-party.md) — disclosure, intellectual property, external code and licensing.

For episode work, also read `story/season-01/overview.md`, the character files, and any episode treatment before inventing a new scene.

## Creative rules

- Sophie Goodman is a **female PhD philosopher and Saul Goodman's granddaughter**, a **philosophical advocate**, not a lawyer. She defends the strongest *defensible* argument for a client's position, including normative and metaethical challenges.
- Her opponents must get credible arguments. Distinguish **validity**, **soundness**, **persuasiveness**, and **moral permissibility**; never treat moral skepticism as proof that anything is allowed.
- Prioritize character, escalating stakes, irony, and moral consequences. Avoid turning episodes into classroom lectures.
- Differentiate the **canon** from **proposals**. The series bible is a working draft; only the explicit locked entries in `spec/canon.md` are fixed.
- Keep Sophie visually consistent with the approved burgundy-suit, dark-wavy-hair concept art unless a scene requires a documented change.
- Do **not** treat scenes, scripts, tools, videos, casting, voice, or production status as finished unless files or records substantiate it.

## Repository workflow

- Inspect existing content and `git status`; avoid overwriting the user's work. Make focused changes and summarize what changed.
- For new creative ideas: write them as **PROPOSED** and list the decision needed. Only promote to **LOCKED** after explicit showrunner approval.
- Keep prose/story in Markdown; prompts, shot lists and output manifests in stable text formats. Use descriptive filenames such as `s01e01-sc03-sh012`.
- Maintain a source-of-truth reference in `spec/` rather than duplicating contradictory instructions across many files.
- For any new shot, record the prompt, continuity anchors, tool/model version if known, output ID/path, and review state. Never invent technical parameters or generation provenance.
- Add scripts only for concrete repetitive needs. Prefer stdlib/simple dependencies; document CLI use.
- Keep heavyweight renders and experimental generated files out of normal Git. Use production storage and/or Git LFS when intentionally configured.
- Run `python scripts/validate_project.py` after changing docs/assets when available.
- Do not put secrets, API keys, personal data, or credentials in the repo.

## External dependencies

`external/` contains **Git submodules**, not original show assets. Do not edit their upstream source in place, paste their licenses into project-owned code, or update gitlinks casually. Explain why a new submodule is needed and document license and pinned revision in `spec/third-party.md`.

Google Flow is a web service and is not a submodule; there is no Flow API. Drive it only through the commands that AAO (`external/any-agent-orchestrator`, the showrunner's own repo) actually implements. Follow AAO's own `AGENTS.md` when running it: use `uv run`, and never type passwords; the showrunner signs in to Google. Flow driving works only on the showrunner's computer with Chrome, not from a cloud container. When AAO lacks a feature (see the gaps in `spec/flow-automation.md`), propose the change upstream in AAO and do that step by hand in Flow meanwhile. Never patch the submodule here.

## Rights and attribution

The project's original show content is intended to be AI-generated with human direction. It currently references copyrighted TV characters and universe elements; treat the project as **unofficial fan fiction** unless rights are secured. Do not imply endorsement or commercial permissions. Verify asset reuse rights and third-party licenses prior to distribution.

## What 'done' means

A story edit has coherent continuity and a clearly updated status. A production change has usable instructions plus an audit trail. A tooling change has documentation and a reproducible validation path. When a task is blocked (e.g., no access to a Google Flow account), describe the exact boundary rather than claiming to have generated/exported anything.
