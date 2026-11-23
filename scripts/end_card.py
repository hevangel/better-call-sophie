"""Render the D01 end card: animated title lettering over a still plate, with traditional tools only.

Pillow draws every frame and ffmpeg encodes them (video only; the mix supplies the sound).
The lettering follows the approved poster (assets/marketing/poster-tv-4x3.webp): "BETTER CALL"
in white heavy italic sans, "SOPHIE" larger in gold heavy italic with a gold swoosh, the phone
number and the fine print in a cream serif italic.

Usage (from the repo root):

    uv run --no-project --with pillow python scripts/end_card.py \
        assets/locations/sophie-office/office-exterior-dusk.webp OUT.mp4 [--sophie-at 2.1]

--sophie-at is when (seconds into the card) "SOPHIE" lands, to meet the sung "Sophie!".
Default fonts are Windows system fonts (Segoe UI Black Italic, Bookman Old Style Bold Italic,
Georgia Italic); check their license before any commercial release, or pass open fonts.
"""

from __future__ import annotations

import argparse
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

WHITE = (255, 255, 255)
GOLD = (247, 183, 33)
CREAM = (240, 228, 200)
DARK = (45, 22, 0)

TITLE_1 = "BETTER CALL"
TITLE_2 = "SOPHIE"
PHONE = "505-555-0148"
FINE_PRINT = "Dr. Goodman is not a lawyer. Nothing in this ad is legal advice. Or moral advice. Probably."


def ease_out(x: float) -> float:
    x = min(1.0, max(0.0, x))
    return 1 - (1 - x) ** 3


def ramp(t: float, start: float, dur: float) -> float:
    return ease_out((t - start) / dur)


def text_layer(text, font, fill, stroke=0, stroke_fill=DARK, shadow=True):
    """Draw text with a soft drop shadow on its own tight RGBA canvas."""
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    l, t, r, b = d.textbbox((0, 0), text, font=font, stroke_width=stroke)
    pad = 30
    w, h = r - l + 2 * pad, b - t + 2 * pad
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    if shadow:
        sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((pad - l + 4, pad - t + 6), text, font=font, fill=(0, 0, 0, 200), stroke_width=stroke, stroke_fill=(0, 0, 0, 200))
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    ImageDraw.Draw(layer).text((pad - l, pad - t), text, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return layer


def swoosh(width: int, height: int, color) -> Image.Image:
    """A tapered gold brush stroke, thick in the middle, curving slightly upward to the right."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    n = 200
    top, bot = [], []
    for i in range(n + 1):
        u = i / n
        x = u * (width - 1)
        y = height * 0.65 - math.sin(u * math.pi * 0.9) * height * 0.25 - u * height * 0.2
        half = max(0.6, math.sin(u * math.pi) ** 0.7 * height * 0.18)
        top.append((x, y - half))
        bot.append((x, y + half))
    d.polygon(top + bot[::-1], fill=color)
    return img.filter(ImageFilter.GaussianBlur(0.6))


def paste_alpha(base: Image.Image, layer: Image.Image, xy, alpha: float, scale: float = 1.0):
    if alpha <= 0:
        return
    if scale != 1.0:
        layer = layer.resize((max(1, round(layer.width * scale)), max(1, round(layer.height * scale))), Image.LANCZOS)
    if alpha < 1:
        a = layer.getchannel("A").point(lambda v: round(v * alpha))
        layer = layer.copy()
        layer.putalpha(a)
    x, y = xy
    base.alpha_composite(layer, (round(x - layer.width / 2), round(y - layer.height / 2)))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plate", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--size", default="1280x720")
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--duration", type=float, default=5.0)
    ap.add_argument("--sophie-at", type=float, default=2.1)
    ap.add_argument("--font-sans", default="C:/Windows/Fonts/seguibli.ttf")
    ap.add_argument("--font-title", default="C:/Windows/Fonts/BOOKOSBI.TTF")
    ap.add_argument("--font-serif", default="C:/Windows/Fonts/georgiai.ttf")
    ap.add_argument("--still", type=float, help="also save the frame at this time as OUT.png")
    a = ap.parse_args()
    W, H = (int(v) for v in a.size.split("x"))

    plate = Image.open(a.plate).convert("RGB")
    s = max(W / plate.width, H / plate.height) * 1.06  # room for the push-in
    plate = plate.resize((round(plate.width * s), round(plate.height * s)), Image.LANCZOS)
    plate = ImageEnhance.Brightness(plate).enhance(0.62)
    # Darken the sky for the title and the lot for the small print.
    grad = Image.new("L", (1, plate.height))
    for y in range(plate.height):
        u = y / plate.height
        grad.putpixel((0, y), round(150 * max(0.0, 1 - u / 0.45) ** 1.5 + 170 * max(0.0, (u - 0.72) / 0.28) ** 1.5))
    shade = Image.new("RGB", plate.size, (8, 6, 14))
    plate = Image.composite(shade, plate, grad.resize(plate.size))

    f1 = ImageFont.truetype(a.font_sans, 84)
    f2 = ImageFont.truetype(a.font_title, 176)
    f3 = ImageFont.truetype(a.font_serif.replace("georgiai", "georgiaz"), 58)
    f4 = ImageFont.truetype(a.font_serif, 21)
    t1 = text_layer(TITLE_1, f1, WHITE)
    t2 = text_layer(TITLE_2, f2, GOLD, stroke=3)
    t3 = text_layer(PHONE, f3, CREAM)
    t4 = text_layer(FINE_PRINT, f4, CREAM, shadow=True)
    sw = swoosh(int(t2.width * 0.78), 46, GOLD)

    cx = W / 2
    y1, y2, ysw, y3, y4 = 78, 205, 300, 575, 680
    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(a.fps), "-i", "-",
         "-c:v", "libopenh264", "-b:v", "8M", "-pix_fmt", "yuv420p", str(a.out)],
        stdin=subprocess.PIPE,
    )
    n = round(a.duration * a.fps)
    for i in range(n):
        t = i / a.fps
        z = 1.0 + 0.035 * (t / a.duration)  # slow push-in
        cw = plate.width / 1.06 / z
        ch = cw * H / W
        left = (plate.width - cw) / 2
        top = (plate.height - ch) * 0.45
        frame = plate.crop((left, top, left + cw, top + ch)).resize((W, H), Image.LANCZOS).convert("RGBA")
        # BETTER CALL slides in from the left.
        k = ramp(t, 0.2, 0.5)
        paste_alpha(frame, t1, (cx - 70 * (1 - k), y1), k)
        # SOPHIE lands on the sung "Sophie!".
        k = ramp(t, a.sophie_at - 0.3, 0.3)
        paste_alpha(frame, t2, (cx, y2), k, scale=1.25 - 0.25 * k)
        # The swoosh wipes left to right.
        k = ramp(t, a.sophie_at, 0.4)
        if k > 0:
            part = sw.crop((0, 0, max(1, round(sw.width * k)), sw.height))
            frame.alpha_composite(part, (round(cx - sw.width / 2 + 40), round(ysw - sw.height / 2)))
        k = ramp(t, a.sophie_at + 0.5, 0.4)
        paste_alpha(frame, t3, (cx, y3 + 12 * (1 - k)), k)
        k = ramp(t, a.sophie_at + 1.0, 0.4)
        paste_alpha(frame, t4, (cx, y4), k)
        rgb = frame.convert("RGB")
        if a.still is not None and i == round(a.still * a.fps):
            rgb.save(a.out.with_suffix(".png"))
        enc.stdin.write(rgb.tobytes())
    enc.stdin.close()
    enc.wait()
    print(f"wrote {a.out} ({n} frames, SOPHIE lands at {a.sophie_at:.2f} s)")


if __name__ == "__main__":
    main()
