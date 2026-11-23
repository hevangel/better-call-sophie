#!/usr/bin/env python3
"""Lightweight validation for Better Call Sophie text/project conventions."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "spec/canon.md", "spec/series-bible.md",
    "spec/production-pipeline.md", "spec/third-party.md", ".gitmodules",
]
ART = [
    "assets/marketing/poster-tv-4x3.webp",
    "assets/marketing/business-card-front.webp",
    "assets/marketing/business-card-back.webp",
]
SUBMODULES = [
    "external/comfyui", "external/remotion", "external/auto-editor", "external/whisper",
    "external/any-agent-orchestrator", "external/youtube-mcp",
]


def main() -> int:
    errors: list[str] = []
    for name in REQUIRED + ART:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")

    modules = (ROOT / ".gitmodules").read_text(encoding="utf-8") if (ROOT / ".gitmodules").exists() else ""
    for path in SUBMODULES:
        if f"path = {path}" not in modules:
            errors.append(f"Missing .gitmodules entry: {path}")

    for path in list((ROOT / "story").rglob("*.md")) if (ROOT / "story").exists() else []:
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "Status:" not in text and "PROPOSED" not in text:
            errors.append(f"Story file missing status marker: {path.relative_to(ROOT)}")

    # Check that README refers to local artwork paths.
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    for name in ART:
        if name not in readme:
            errors.append(f"README does not reference: {name}")

    if errors:
        print("Project validation FAILED:\n" + "\n".join(f"- {err}" for err in errors))
        return 1
    print("Project validation passed: required docs, artwork and submodule declarations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
