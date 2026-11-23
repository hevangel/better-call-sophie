# AI-first production pipeline

**Initial environment: Google Flow.** This is a browser-based creative workflow chosen by the showrunner because a subscription is available. The project stays tool-agnostic: alternate video, image, voice, audio, and editing tools may be tested and adopted. Do not assume a public Flow API, CLI, export format, watermark policy, quota, commercial rights, or stable model identifier without current verification.

## Stages

| Stage | Source | Output / gate |
| --- | --- | --- |
| Development | Canon, series bible | Episode treatment with dilemma, counterargument and story cost |
| Screenwriting | Treatment, character files | Scene script, dialogue, continuity review |
| Shot design | Script and locations | Shot IDs and beat-to-shot breakdown |
| Visual reference | Approved character/location assets | Consistent reference images and style anchors |
| Generation | Google Flow first | Versioned candidate clips, exact prompts/settings where known |
| Editorial | Selected clips | Rough cut, pick list, retiming, bridges, credits |
| Audio | Approved voices, effects, score | Mixed dialogue/music/SFX, subtitles |
| QC | Full episode | Continuity, intellectual accuracy, artifact checks, rights review |
| Delivery | QC-approved master | Distribution copies, captions, release notes, manifest |

## Automation

Agents drive Flow and Flow Music through `external/any-agent-orchestrator`, check the outputs and log them. The commands, the known gaps and the per-shot loop are in [flow-automation.md](flow-automation.md). Steps that AAO cannot do yet are done by hand and logged in the same way.

## Post-production text and graphics

**Showrunner direction (2026-11-23), for agents:** add text and graphics to video with **traditional editing tools**. These include ffmpeg filters, OpenCV tracking and warping, Blender's tracker and compositor, and Remotion for animated titles. Do not use AI regeneration, inpainting or video-to-video for this.

- Script the overlay so it can be re-run, and log the tool, version and command or script in the shot record.
- Text on a surface in the scene, such as a chalkboard, sign or screen: corner-pin or track the surface, then matte out anything that passes in front of it. The first worked example is D01 shot 4, in [production/demo/d01-commercial-30s.md](../production/demo/d01-commercial-30s.md#shot-4-test-chalk-text-generated-vs-added-in-post).
- Generating readable text in Flow is allowed only as a showrunner-approved test.

## Episode production directory

~~~text
production/
  google-flow/                  Google Flow setup and export notes
  prompts/                      Reusable prompts and shot-specific prompt records
  shot-lists/s01e01/             Shot breakdown, progress tracking
  generation-logs/              Tool/model/settings/output provenance
  edit-decisions/               Cut plans and editorial notes
  exports/README.md             Where render outputs are stored (large files ignored)
~~~

Prefer one Markdown/YAML record per approved shot, e.g. `s01e01-sc03-sh012.md`:

~~~yaml
id: s01e01-sc03-sh012
status: proposed # proposed | generated | selected | rejected | final
scene: 03
intent: "Sophie reframes the ethics accusation during a hearing."
duration_target_seconds: 8
aspect_ratio: "16:9"
location: "Albuquerque corporate hearing room"
characters:
  - sophie-goodman
continuity:
  wardrobe: "burgundy suit / ivory blouse"
  reference_images: []
tool: "Google Flow"
model: "unknown; record after generation"
prompt: "..."
negative_constraints: "No extra people, captions, logos, or inconsistent wardrobe."
generation_datetime: null
source_export_path: null
selected_export_path: null
review_notes: []
~~~

Copy this as documentation, not a claim that any shot exists yet.

## File naming and storage

- Episode: `s01e01`; scene: `sc03`; shot: `sh012`; take/version: `v03`.
- Small references under `assets/`; prompts, metadata and scripts under `production/`.
- High-resolution image masters, generated video, audio stems and backups live in designated production storage. `production/exports/` is ignored by Git; use a reviewed Git LFS strategy if binaries truly need versioning in GitHub.
- Never commit third-party copyrighted clips, credentials, subscription data, or private account identifiers.
- Preserve **unaltered exports** before retiming, grading or transcription. Save checksum/filename when available.

## Clip acceptance checklist

1. Follows approved scene narrative and philosophical claims.
2. Character face, age, hair, costume, voice, and objects stay consistent.
3. Camera axis, background geometry, hand props, and time-of-day are continuous.
4. Audio and speech match script; no fabricated captions or text in generated frames.
5. Duration, resolution, aspect ratio and technical quality meet edit needs.
6. No unlicensed assets or recognizable real-performer likenesses without clearance.
7. Prompt, tool, model/version (if available), and selection rationale recorded.

## Tool changes

A new generation or editing tool should be evaluated on output consistency, reproducibility, pricing, rights, privacy, and integration cost. Document its role in `tools/README.md` or `spec/third-party.md` if it becomes a dependency. Do not rewrite the story pipeline around a single vendor.
