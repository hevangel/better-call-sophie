"""Transcribe clips with Whisper and compare each with its scripted line, word by word.

Usage (from the repo root; Whisper is the project's submodule):

    uv run --no-project --with ./external/whisper python scripts/check_lines.py \
        CLIP.wav "Scripted line." [CLIP2.wav "Line 2." ...] [--model small.en]

Audio is read with Python's wave module (16 kHz mono 16-bit WAV, made with
``ffmpeg -i clip.mp4 -vn -ac 1 -ar 16000 clip.wav``), so Whisper does not call ffmpeg.
The model file must already be in Whisper's cache (~/.cache/whisper); on Windows,
Whisper's own HTTPS download can fail with "OPENSSL_Uplink ... no OPENSSL_Applink"
after torch is imported, so fetch the file from the URL in whisper._MODELS with curl.
Prints one JSON object per clip: the transcript, the word-level match and the timing.
For a silent shot pass an empty line (""). Whisper may still "hear" words in sound
effects (D01 shot 2's phone buzz came out as "Vroom, vroom" or "denote States"), so
check no_speech_prob and listen before calling a silent shot clean.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import wave

import numpy as np
import whisper


def words(s: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", s.lower().replace("’", "'"))


def load_wav(path: str) -> np.ndarray:
    with wave.open(path) as w:
        if w.getframerate() != 16000 or w.getnchannels() != 1 or w.getsampwidth() != 2:
            raise SystemExit(f"{path}: need 16 kHz mono 16-bit WAV")
        return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768.0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="+", help="CLIP.wav LINE pairs")
    ap.add_argument("--model", default="small.en")
    a = ap.parse_args()
    if len(a.pairs) % 2:
        raise SystemExit("give CLIP LINE pairs")
    model = whisper.load_model(a.model)
    for clip, line in zip(a.pairs[0::2], a.pairs[1::2]):
        r = model.transcribe(load_wav(clip), language="en", fp16=False, word_timestamps=True)
        heard, want = words(r["text"]), words(line)
        ops = [op for op in difflib.SequenceMatcher(a=want, b=heard).get_opcodes() if op[0] != "equal"]
        diffs = [{"op": t, "script": " ".join(want[i1:i2]), "heard": " ".join(heard[j1:j2])} for t, i1, i2, j1, j2 in ops]
        segs = r.get("segments", [])
        print(json.dumps({
            "clip": clip,
            "transcript": r["text"].strip(),
            "word_match": not diffs,
            "differences": diffs,
            "speech_start_s": round(segs[0]["start"], 2) if segs else None,
            "speech_end_s": round(segs[-1]["end"], 2) if segs else None,
            # High values mean Whisper thinks a segment is not speech (for silent shots, sound effects).
            "no_speech_prob": [round(s["no_speech_prob"], 2) for s in segs],
            "whisper_model": a.model,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
