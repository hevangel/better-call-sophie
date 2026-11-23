"""Lay text over the text-free marketing art made in Google Flow.

Flow draws lettering badly, so the poster and business card are generated
without text (see production/prompts/marketing-v2.md) and the words are added
here, where spelling and layout are exact.

Usage (from the repo root):

    uv run --no-project --with pillow python scripts/compose_marketing.py \
        [--src production/exports/marketing] [--out production/exports/marketing] \
        [--fonts C:/Windows/Fonts]

Inputs (in --src): poster-art-v01.jpg, card-photo-v01.jpg, card-logo-v01.jpg.
Outputs (in --out): poster-tv-4x3-v2.png, business-card-front-v2.png,
business-card-back-v2.png, plus a .webp preview of each.

Fonts are the Windows system fonts Arial Black, Georgia and Brush Script MT,
found in --fonts. On another system, point --fonts at a folder holding files
with the same names (arialbd.ttf, ariblk.ttf, georgiab.ttf, georgiaz.ttf,
georgiai.ttf, BRUSHSCI.TTF).

All words, the phone number and the services are fictional show content;
555 numbers are reserved for fiction.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

YELLOW = (250, 190, 30)
RED = (178, 24, 30)
BURGUNDY = (92, 18, 26)
INK = (28, 16, 14)
WHITE = (255, 255, 255)
GOLD = (247, 186, 28)

POSTER = {
    "title_1": "BETTER CALL",
    "title_2": "SOPHIE",
    "tagline": ["Morally Questionable?", "Philosophically Defensible."],
    "footer": "A philosophical crime drama",
}
CARD = {
    "hook": "IN MORAL TROUBLE?",
    "script": "Better Call Sophie!",
    "name": "SOPHIE GOODMAN, PhD",
    "role": "PHILOSOPHICAL ADVOCATE",
    "tagline": "Morally Questionable? Philosophically Defensible.",
    "phone": "(505) 555-0148",
    "footer": "ETHICS  \u2022  METAETHICS  \u2022  REPUTATION DEFENSE",
    "firm": ["GOODMAN", "PHILOSOPHICAL", "CONSULTING"],
    "services": [
        "Ethics Opinions",
        "Metaethical Strategy",
        "Reputation Defense",
        "Existential Disputes",
        "Moral Positioning",
    ],
    "place": "Albuquerque, New Mexico",
    "back_tagline": "When your conscience needs a defense.",
    "signature": "Sophie Goodman, PhD \u2014 Philosophical Advocate",
}
CARD_SIZE = (1050, 600)  # 3.5 x 2 in at 300 dpi


class Fonts:
    def __init__(self, folder: Path):
        self.folder = folder

    def get(self, name: str, size: int) -> ImageFont.FreeTypeFont:
        files = {
            "black": "ariblk.ttf",
            "bold": "arialbd.ttf",
            "serif_bold": "georgiab.ttf",
            "serif_bold_italic": "georgiaz.ttf",
            "serif_italic": "georgiai.ttf",
            "script": "BRUSHSCI.TTF",
        }
        return ImageFont.truetype(str(self.folder / files[name]), size)


def text_w(draw: ImageDraw.ImageDraw, text: str, font) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def fit(draw, text, fonts: Fonts, name: str, start: int, max_w: int):
    size = start
    while size > 8:
        font = fonts.get(name, size)
        if text_w(draw, text, font) <= max_w:
            return font
        size -= 2
    return fonts.get(name, size)


def shadowed(base: Image.Image, xy, text, font, fill, shadow=(0, 0, 0), blur=6, offset=(3, 4), stroke=0, stroke_fill=None):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((xy[0] + offset[0], xy[1] + offset[1]), text, font=font, fill=shadow + (190,), stroke_width=stroke, stroke_fill=shadow + (190,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)
    ImageDraw.Draw(base).text(xy, text, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def gradient(size, box, direction: str, max_alpha: int) -> Image.Image:
    """A black overlay that fades in across `box` toward `direction`."""
    w, h = size
    x0, y0, x1, y1 = box
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    if direction in ("right", "left"):
        span = x1 - x0
        for i in range(span):
            a = int(max_alpha * (i / span) ** 1.4)
            x = x0 + i if direction == "right" else x1 - i
            d.line([(x, y0), (x, y1)], fill=a)
        if direction == "right":
            d.rectangle([x1, y0, w, y1], fill=max_alpha)
    else:
        span = y1 - y0
        for i in range(span):
            a = int(max_alpha * (i / span) ** 1.4)
            y = y0 + i if direction == "down" else y1 - i
            d.line([(x0, y), (x1, y)], fill=a)
        if direction == "down":
            d.rectangle([x0, y1, x1, h], fill=max_alpha)
    overlay = Image.new("RGBA", size, (8, 5, 4, 255))
    overlay.putalpha(mask)
    return overlay


def poster(src: Path, fonts: Fonts) -> Image.Image:
    img = Image.open(src / "poster-art-v01.jpg").convert("RGBA")
    w, h = img.size
    img.alpha_composite(gradient(img.size, (int(w * 0.45), 0, int(w * 0.72), h), "right", 175))
    img.alpha_composite(gradient(img.size, (0, int(h * 0.80), w, h), "down", 200))
    d = ImageDraw.Draw(img)
    right = w - int(w * 0.05)
    col_w = int(w * 0.40)

    f1 = fit(d, POSTER["title_1"], fonts, "black", 120, col_w)
    f2 = fit(d, POSTER["title_2"], fonts, "black", 220, col_w)
    y = int(h * 0.07)
    shadowed(img, (right - text_w(d, POSTER["title_1"], f1), y), POSTER["title_1"], f1, WHITE)
    y += int(f1.size * 1.05)
    shadowed(img, (right - text_w(d, POSTER["title_2"], f2), y), POSTER["title_2"], f2, GOLD, stroke=3, stroke_fill=(60, 30, 0))
    y += int(f2.size * 1.15)
    d.line([(right - col_w, y), (right, y)], fill=GOLD, width=4)
    y += 24
    ft = fonts.get("serif_bold_italic", int(f1.size * 0.42))
    for line in POSTER["tagline"]:
        shadowed(img, (right - text_w(d, line, ft), y), line, ft, WHITE, blur=4, offset=(2, 3))
        y += int(ft.size * 1.3)

    ff = fonts.get("serif_italic", int(h * 0.032))
    tw = text_w(d, POSTER["footer"], ff)
    fy = h - int(h * 0.075)
    fx = (w - tw) // 2
    d = ImageDraw.Draw(img)
    d.text((fx, fy), POSTER["footer"], font=ff, fill=(236, 220, 190))
    mid = fy + ff.size // 2 + 2
    d.line([(fx - 160, mid), (fx - 24, mid)], fill=GOLD, width=2)
    d.line([(fx + tw + 24, mid), (fx + tw + 160, mid)], fill=GOLD, width=2)
    return img.convert("RGB")


def bar(d, box, fill, skew=10):
    x0, y0, x1, y1 = box
    d.polygon([(x0 + skew, y0), (x1, y0), (x1 - skew, y1), (x0, y1)], fill=fill)


def card_front(src: Path, fonts: Fonts) -> Image.Image:
    photo = Image.open(src / "card-photo-v01.jpg").convert("RGB")
    pw, ph = photo.size
    cw = int(ph * CARD_SIZE[0] / CARD_SIZE[1])
    photo = photo.crop((pw - cw, 0, pw, ph)).resize(CARD_SIZE, Image.LANCZOS)
    img = photo.convert("RGBA")
    w, h = img.size
    d = ImageDraw.Draw(img)
    left, col = 46, 560

    fh = fit(d, CARD["hook"], fonts, "black", 44, col - 40)
    bar(d, (left - 10, 34, left + col - 20, 34 + fh.size + 22), RED, 14)
    d.text((left + 14, 40), CARD["hook"], font=fh, fill=WHITE)

    fs = fit(d, CARD["script"], fonts, "script", 116, col)
    shadowed(img, (left, 106), CARD["script"], fs, RED, shadow=(90, 40, 0), blur=4, offset=(3, 4))
    d = ImageDraw.Draw(img)

    y = 106 + int(fs.size * 1.22)
    fn = fit(d, CARD["name"], fonts, "black", 46, col)
    d.text((left, y), CARD["name"], font=fn, fill=INK)
    y += int(fn.size * 1.45)
    fr = fit(d, CARD["role"], fonts, "black", 25, col - 60)
    bar(d, (left - 6, y, left + col, y + fr.size + 18), RED, 10)
    d.text((left + (col - text_w(d, CARD["role"], fr)) // 2, y + 6), CARD["role"], font=fr, fill=WHITE)
    y += fr.size + 40
    ft = fit(d, CARD["tagline"], fonts, "serif_bold_italic", 26, col)
    d.text((left, y), CARD["tagline"], font=ft, fill=INK)
    y += int(ft.size * 1.9)
    fp = fit(d, CARD["phone"], fonts, "black", 48, col - 120)
    bar(d, (left - 6, y, left + col - 40, y + fp.size + 24), RED, 12)
    d.text((left + 40, y + 7), CARD["phone"], font=fp, fill=WHITE)
    y += fp.size + 50
    ff = fit(d, CARD["footer"], fonts, "bold", 20, col)
    d.text((left, y), CARD["footer"], font=ff, fill=INK)

    d.rectangle([0, 0, w - 1, h - 1], outline=RED, width=10)
    return img.convert("RGB")


def card_back(src: Path, fonts: Fonts) -> Image.Image:
    logo = Image.open(src / "card-logo-v01.jpg").convert("RGB")
    bg = logo.getpixel((12, 12))
    img = Image.new("RGBA", CARD_SIZE, bg + (255,))
    w, h = img.size
    d = ImageDraw.Draw(img)

    # Lift the ink off the yellow so no square edge shows: alpha follows darkness.
    lg = logo.crop((120, 120, logo.width - 120, logo.height - 120)).resize((230, 230), Image.LANCZOS)
    bg_lum = sum(bg) / 3
    alpha = lg.convert("L").point(lambda v: max(0, min(255, int((bg_lum - v) * 2.2))))
    ink = Image.new("RGBA", lg.size, BURGUNDY + (255,))
    ink.putalpha(alpha)
    img.alpha_composite(ink, (40, 30))

    x = 300
    fy = 44
    for i, line in enumerate(CARD["firm"]):
        f = fonts.get("black", 54 if i != 1 else 40)
        if i == 1:
            bar(d, (x - 8, fy - 4, x + text_w(d, line, f) + 24, fy + f.size + 12), RED, 10)
            d.text((x + 8, fy), line, font=f, fill=WHITE)
        else:
            d.text((x, fy), line, font=f, fill=INK)
        fy += int(f.size * 1.3) + (6 if i == 1 else 0)

    y = 288
    fh = fonts.get("black", 26)
    bar(d, (32, y, 32 + text_w(d, "SERVICES INCLUDE:", fh) + 40, y + fh.size + 14), RED, 10)
    d.text((50, y + 4), "SERVICES INCLUDE:", font=fh, fill=WHITE)
    y += fh.size + 26
    fsv = fonts.get("serif_bold_italic", 25)
    for s in CARD["services"]:
        d.rectangle([44, y + 4, 66, y + 26], outline=RED, width=3)
        d.line([(48, y + 15), (54, y + 22), (64, y + 6)], fill=RED, width=4)
        d.text((80, y), s, font=fsv, fill=INK)
        y += 38

    d.line([(470, 290), (470, 520)], fill=RED, width=3)
    rx = 500
    fc = fonts.get("bold", 22)
    fp = fonts.get("black", 46)
    d.text((rx, 296), "Call or Text:", font=fc, fill=INK)
    bar(d, (rx - 6, 328, w - 40, 328 + fp.size + 22), RED, 12)
    d.text((rx + 22, 334), CARD["phone"], font=fp, fill=WHITE)
    fpl = fonts.get("serif_bold", 26)
    d.text((rx, 420), CARD["place"], font=fpl, fill=INK)
    ftg = fit(d, CARD["back_tagline"], fonts, "serif_bold_italic", 30, w - rx - 40)
    d.text((rx, 468), CARD["back_tagline"], font=ftg, fill=RED)

    fsg = fonts.get("serif_bold_italic", 22)
    sw = text_w(d, CARD["signature"], fsg)
    d.line([(40, 556), (w - 40, 556)], fill=RED, width=2)
    d.rectangle([(w - sw) // 2 - 16, 540, (w + sw) // 2 + 16, 574], fill=bg)
    d.text(((w - sw) // 2, 542), CARD["signature"], font=fsg, fill=INK)

    d.rectangle([0, 0, w - 1, h - 1], outline=RED, width=10)
    return img.convert("RGB")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--src", type=Path, default=Path("production/exports/marketing"))
    ap.add_argument("--out", type=Path, default=Path("production/exports/marketing"))
    ap.add_argument("--fonts", type=Path, default=Path("C:/Windows/Fonts"))
    a = ap.parse_args()
    fonts = Fonts(a.fonts)
    a.out.mkdir(parents=True, exist_ok=True)
    for name, img in (
        ("poster-tv-4x3-v2", poster(a.src, fonts)),
        ("business-card-front-v2", card_front(a.src, fonts)),
        ("business-card-back-v2", card_back(a.src, fonts)),
    ):
        img.save(a.out / f"{name}.png")
        img.save(a.out / f"{name}.webp", quality=90, method=6)
        print(f"wrote {a.out / name}.png and .webp  {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
