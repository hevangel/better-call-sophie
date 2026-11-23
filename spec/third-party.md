# Third-party tools and Git submodules

Third-party repositories are deliberately kept under `external/` as **Git submodules** (mode 160000 gitlinks plus `.gitmodules`), pinned to identified commits. They are used for **evaluation, reference or optional local production tasks**, not required by Google Flow. Initial production is Google Flow-first.

| Local path | Upstream | Purpose | License note |
| --- | --- | --- | --- |
| `external/comfyui` | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Optional node-based local image/video generation experiments and workflow reference | GPL-3.0; review when distributing modified/combined software |
| `external/remotion` | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | Code-driven video assembly, animated titles, lower thirds, credits | Multiple/project-specific license terms; verify commercial conditions |
| `external/auto-editor` | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | Optional automatic timing/edit experiments | Unlicense (verify included components) |
| `external/whisper` | [openai/whisper](https://github.com/openai/whisper) | Speech transcription and subtitle/QC reference | MIT; verify model/audio usage terms |
| `external/any-agent-orchestrator` | [hevangel/any-agent-orchestrator](https://github.com/hevangel/any-agent-orchestrator) | The showrunner's own agent orchestrator. Its playwright-cli drivers let agents drive Google Flow and Flow Music in the user's Chrome; see [flow-automation.md](flow-automation.md) | MIT. Its own nested `external/` submodules have separate licenses and are not needed for Flow |
| `external/youtube-mcp` | [pratikgh0se/youtube-mcp](https://github.com/pratikgh0se/youtube-mcp) | MCP server for the YouTube Data API: uploads to the show's channel and sets metadata (tags, category, made for kids, altered or synthetic content), each write behind a preview-and-approve step | MIT. Needs the showrunner's own Google Cloud API key and Desktop OAuth client (never committed) |

Pinned at initialization (2026-11-14):
- ComfyUI: `eee59185ff4f43ae2d9ad122b245619d27d9daad`
- Remotion: `cc7879e13f7dc5ef33d8d735ffee33c94e983b47`
- Auto-Editor: `4fe66bae4965b9bcc0a71cebd8a4e5e08beefb81`
- Whisper: `86098128c0b4f24f0e2aa2994de830614b474227`

Added 2026-11-22:
- any-agent-orchestrator: `00ba2498cf9653a6f3a3bf581b03eb790525879f` (upstream `main`, 2026-11-22). Added because the showrunner chose it for Flow automation. Fix Flow-driver gaps upstream and then bump this pin; do not patch it here. Its nested submodules are not needed: initialize them only when using AAO features beyond Flow.

Added 2026-11-23:
- youtube-mcp: `b21d71b064854618655299a8aa179230ddffec3c` (upstream `main`, release v0.3.3, 2026-11-08). Added at the showrunner's request to upload the demo videos to [@better-call-sophie](https://www.youtube.com/@better-call-sophie) instead of uploading by hand. Review before first use (2026-11-23): MIT; dependencies `googleapis`, `@modelcontextprotocol/sdk`, `youtube-transcript`, `zod`; network calls only to `googleapis.com` and a local `127.0.0.1` sign-in callback; tokens stored in `~/.youtube-mcp` (or `YOUTUBE_MCP_STATE_DIR`), outside the repo. It asks for the broad `youtube` and `youtube.force-ssl` scopes plus `yt-analytics.readonly`, not just upload. Install and build from the pinned checkout with `npm ci` in `external/youtube-mcp` (its `node_modules/` and `dist/` are ignored upstream); run `node external/youtube-mcp/dist/index.js`. Its own setup guide is `external/youtube-mcp/docs/SETUP.md`.
## Working with submodules

~~~bash
git clone https://github.com/hevangel/better-call-sophie.git
cd better-call-sophie
git submodule update --init --recursive

# When deliberately reviewing an upstream update:
git -C external/comfyui fetch
git -C external/comfyui checkout <reviewed-commit>
git add external/comfyui
~~~

Do **not** blindly update all submodules or assume installing them makes a functional end-to-end video pipeline. Many require GPUs, packages, model downloads, extra storage, and their own dependencies. Never commit model weights or downloads simply because a submodule mentions them. Record upstream licenses, pinned revisions, security/quality review and rationale when updating.

## Google Flow

Google Flow is a **hosted video production application**, not a Git submodule. Store prompts and exported results under the project conventions; don't assume an official scriptable API. Automation runs through AAO's browser drivers ([flow-automation.md](flow-automation.md)), not through a Google API. See `production/google-flow/README.md`.
