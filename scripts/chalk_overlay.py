"""Composite chalk text onto a board in a video clip, with traditional tools only.

Used for D01 shot 4, version B (production/demo/d01-commercial-30s.md): the text is
rendered from a font, pinned to four board corners picked on one reference frame,
tracked through the clip with OpenCV, and shown only where the board is dark, so
anything lighter in front of the board (a hand, a sleeve) covers it.

Usage (from the repo root):

    uv run --no-project --with opencv-python --with numpy --with pillow \
        python scripts/chalk_overlay.py IN.mp4 OUT.mp4 \
        --quad 830,79,1230,65,1230,160,830,164 --ref-time 4.0 --text "IS ≠ OUGHT"

--quad is top-left, top-right, bottom-right, bottom-left in pixels on the frame at
--ref-time. Add --static to skip tracking, --no-key to skip the luminance matte.
ffmpeg must be on PATH; the original audio is copied.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

CHALK = (238, 232, 218)  # warm off-white, like the existing chalk lines


def render_text(text: str, font_path: str, width: int, height: int, seed: int) -> np.ndarray:
    """Return an RGBA float image (0..1) of rough chalk lettering filling width x height.

    The not-equal sign is drawn by hand ("=" plus a slash), so it never depends on
    the font having the glyph.
    """
    rng = np.random.default_rng(seed)
    scale = 4  # draw large, then shrink, for clean edges before roughening
    w, h = width * scale, height * scale
    img = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(img)
    pieces = text.split("≠")
    size = int(h * 0.82)
    font = ImageFont.truetype(font_path, size)
    gap = int(size * 0.28)
    neq_w = int(size * 0.62)
    widths = [d.textlength(p.strip(), font=font) for p in pieces]
    total = sum(widths) + (len(pieces) - 1) * (neq_w + 2 * gap)
    if total > w:  # shrink to fit
        size = int(size * w / total * 0.97)
        font = ImageFont.truetype(font_path, size)
        gap, neq_w = int(size * 0.28), int(size * 0.62)
        widths = [d.textlength(p.strip(), font=font) for p in pieces]
        total = sum(widths) + (len(pieces) - 1) * (neq_w + 2 * gap)
    x = (w - total) / 2
    asc, desc = font.getmetrics()
    y = (h - (asc + desc)) / 2
    stroke = max(2, size // 14)
    for i, p in enumerate(pieces):
        d.text((x, y), p.strip(), font=font, fill=255)
        x += widths[i]
        if i < len(pieces) - 1:
            x += gap
            cy = y + asc * 0.62
            for dy in (-size * 0.11, size * 0.11):
                d.line([(x, cy + dy), (x + neq_w, cy + dy)], fill=255, width=stroke)
            d.line([(x + neq_w * 0.7, cy - size * 0.3), (x + neq_w * 0.3, cy + size * 0.3)], fill=255, width=stroke)
            x += neq_w + gap
    img = img.resize((width, height), Image.LANCZOS)
    a = np.asarray(img, dtype=np.float32) / 255.0
    # Chalk: broken, grainy strokes with soft edges.
    grain = rng.random(a.shape).astype(np.float32)
    a = a * np.clip(0.45 + grain * 0.75, 0, 1)
    a = np.asarray(Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6)), dtype=np.float32) / 255.0
    a = np.clip(a * 0.92, 0, 1)
    rgba = np.zeros((height, width, 4), np.float32)
    rgba[..., :3] = np.array(CHALK, np.float32) / 255.0
    rgba[..., 3] = a
    return rgba


def read_frames(path: Path) -> tuple[list[np.ndarray], float]:
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(f)
    cap.release()
    return frames, fps


def track_homographies(frames: list[np.ndarray], ref: int, board: np.ndarray) -> list[np.ndarray]:
    """Homography from the reference frame to every frame, from board features.

    Points are found inside the board polygon on the reference frame and followed with
    pyramidal Lucas-Kanade, frame to frame, in both directions. RANSAC drops points on
    anything that moves over the board.
    """
    gray = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY) for f in frames]
    mask = np.zeros_like(gray[ref])
    cv2.fillPoly(mask, [board.astype(np.int32)], 255)
    p0 = cv2.goodFeaturesToTrack(gray[ref], maxCorners=600, qualityLevel=0.01, minDistance=6, mask=mask)
    hs: list[np.ndarray | None] = [None] * len(frames)
    hs[ref] = np.eye(3)
    for step in (1, -1):
        ref_pts = p0.copy()
        cur = p0.copy()
        i = ref
        while 0 <= i + step < len(frames):
            nxt, st, _ = cv2.calcOpticalFlowPyrLK(gray[i], gray[i + step], cur, None, winSize=(21, 21), maxLevel=3)
            back, st2, _ = cv2.calcOpticalFlowPyrLK(gray[i + step], gray[i], nxt, None, winSize=(21, 21), maxLevel=3)
            good = (st.ravel() == 1) & (st2.ravel() == 1) & (np.linalg.norm((back - cur).reshape(-1, 2), axis=1) < 1.0)
            ref_pts, cur = ref_pts[good], nxt[good]
            i += step
            if len(cur) < 12:
                hs[i] = hs[i - step]
                continue
            h, inl = cv2.findHomography(ref_pts, cur, cv2.RANSAC, 2.0)
            hs[i] = h if h is not None else hs[i - step]
    return [h if h is not None else np.eye(3) for h in hs]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--quad", required=True, help="x1,y1,...,x4,y4: TL, TR, BR, BL on the reference frame")
    ap.add_argument("--board", help="x1,y1,...: polygon of the whole board on the reference frame (for tracking); defaults to the quad grown 3x")
    ap.add_argument("--ref-time", type=float, default=0.0)
    ap.add_argument("--text", default="IS ≠ OUGHT")
    ap.add_argument("--font", default="C:/Windows/Fonts/Inkfree.ttf")
    ap.add_argument("--static", action="store_true", help="no tracking: pin to the same pixels in every frame")
    ap.add_argument("--no-key", action="store_true", help="no luminance matte")
    ap.add_argument("--key-low", type=float, default=0.30, help="luma (0..1) at or below which the text is fully shown")
    ap.add_argument("--key-high", type=float, default=0.45, help="luma (0..1) at or above which the text is hidden")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--report", type=Path, help="write per-frame corner positions as JSON")
    a = ap.parse_args()

    frames, fps = read_frames(a.src)
    ref = min(len(frames) - 1, round(a.ref_time * fps))
    quad = np.array([float(v) for v in a.quad.split(",")], np.float32).reshape(4, 2)
    if a.board:
        board = np.array([float(v) for v in a.board.split(",")], np.float32).reshape(-1, 2)
    else:
        c = quad.mean(axis=0)
        board = (quad - c) * 3 + c
    tw = int(np.linalg.norm(quad[1] - quad[0]))
    th = int(np.linalg.norm(quad[3] - quad[0]))
    text = render_text(a.text, a.font, tw, th, a.seed)
    rect = np.array([[0, 0], [tw - 1, 0], [tw - 1, th - 1], [0, th - 1]], np.float32)
    base = cv2.getPerspectiveTransform(rect, quad)
    hs = [np.eye(3)] * len(frames) if a.static else track_homographies(frames, ref, board)

    hgt, wid = frames[0].shape[:2]
    encoders = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
    # libx264 is not in every ffmpeg build (the WinGet build has OpenH264 instead).
    vcodec = ["-c:v", "libx264", "-crf", "16"] if " libx264 " in encoders else ["-c:v", "libopenh264", "-b:v", "12M"]
    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{wid}x{hgt}", "-r", str(fps), "-i", "-",
         "-i", str(a.src), "-map", "0:v", "-map", "1:a?", *vcodec, "-pix_fmt", "yuv420p", "-c:a", "copy", str(a.out)],
        stdin=subprocess.PIPE,
    )
    rng = np.random.default_rng(a.seed + 1)
    corners = []
    for i, f in enumerate(frames):
        m = hs[i] @ base
        warped = cv2.warpPerspective(text, m, (wid, hgt), flags=cv2.INTER_LINEAR)
        alpha = warped[..., 3:4]
        img = f.astype(np.float32) / 255.0
        if not a.no_key:
            luma = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
            luma = cv2.GaussianBlur(luma, (0, 0), 1.2)
            key = np.clip((a.key_high - luma) / (a.key_high - a.key_low), 0, 1)[..., None]
            alpha = alpha * key
        # Light from the scene: chalk under the warm sun stripes picks up their color.
        chalk = warped[..., [2, 1, 0]] * (0.75 + 0.5 * img)
        chalk = np.clip(chalk, 0, 1)
        screen = 1 - (1 - img) * (1 - chalk * alpha)
        out = img * (1 - alpha) + screen * alpha
        out += (rng.standard_normal(out.shape[:2])[..., None] * 0.008) * (alpha > 0.01)  # match the clip's grain
        enc.stdin.write((np.clip(out, 0, 1) * 255).astype(np.uint8).tobytes())
        corners.append(cv2.perspectiveTransform(quad[None], hs[i])[0].round(1).tolist())
    enc.stdin.close()
    enc.wait()
    if a.report:
        drift = [float(np.abs(np.array(c) - quad).max()) for c in corners]
        a.report.write_text(json.dumps({"fps": fps, "frames": len(frames), "ref_frame": ref, "static": a.static,
                                        "max_corner_drift_px": max(drift), "corners": corners}, indent=1))
    print(f"wrote {a.out} ({len(frames)} frames, ref frame {ref}, tracking {'off' if a.static else 'on'}, key {'off' if a.no_key else 'on'})")


if __name__ == "__main__":
    main()
