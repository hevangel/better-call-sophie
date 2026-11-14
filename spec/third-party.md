# Third-party tools and Git submodules

Third-party repositories are deliberately kept under `external/` as **Git submodules** (mode 160000 gitlinks plus `.gitmodules`), pinned to identified commits. They are used for **evaluation, reference or optional local production tasks**, not required by Google Flow. Initial production is Google Flow-first.

| Local path | Upstream | Purpose | License note |
| --- | --- | --- | --- |
| `external/comfyui` | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Optional node-based local image/video generation experiments and workflow reference | GPL-3.0; review when distributing modified/combined software |
| `external/remotion` | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | Code-driven video assembly, animated titles, lower thirds, credits | Multiple/project-specific license terms; verify commercial conditions |
| `external/auto-editor` | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | Optional automatic timing/edit experiments | Unlicense (verify included components) |
| `external/whisper` | [openai/whisper](https://github.com/openai/whisper) | Speech transcription and subtitle/QC reference | MIT; verify model/audio usage terms |

Pinned at initialization (2026-11-14):
- ComfyUI: `eee59185ff4f43ae2d9ad122b245619d27d9daad`
- Remotion: `cc7879e13f7dc5ef33d8d735ffee33c94e983b47`
- Auto-Editor: `4fe66bae4965b9bcc0a71cebd8a4e5e08beefb81`
- Whisper: `86098128c0b4f24f0e2aa2994de830614b474227`

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

Google Flow is a **hosted video production application**, not a Git submodule. Store prompts and exported results under the project conventions; don't assume an official scriptable API. See `production/google-flow/README.md`.
