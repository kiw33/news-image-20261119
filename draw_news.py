#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

A flat vector-style newspaper page: one headline banner, six illustrated
story panels and an "also today" ticker. Pure Pillow, no network, no
external assets, so re-running it produces byte-identical output.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (16, 35, 63)
PAPER = (244, 241, 234)
GOLD = (232, 163, 61)
WHITE = (255, 255, 255)
INK = (20, 20, 20)
GREY = (90, 90, 90)
TILE = (238, 238, 232)

STORIES = [
    dict(kicker="APEC \u00b7 SHENZHEN", color=(176, 120, 31),
         head="Trump, Xi and Putin meet in Shenzhen",
         sub="Trilateral talks at APEC; Xi hugs Trump on arrival",
         tag="SHENZHEN \u00b7 APEC 2026", icon="flags"),
    dict(kicker="THE HAGUE", color=(31, 95, 168),
         head="World Court rules on Rohingya genocide case",
         sub="Verdict read today; Gambia v. Myanmar, 2017 case",
         tag="ICJ \u00b7 08:00 GMT", icon="scales"),
    dict(kicker="MARKETS \u00b7 AI", color=(46, 111, 80),
         head="Anthropic debuts in biggest IPO ever",
         sub="$81.3bn at $83 a share; trades today as ANT",
         tag="~$1.5TN VALUATION", icon="chart"),
    dict(kicker="CULTURE", color=(120, 60, 150),
         head="GTA VI rolls out worldwide",
         sub="Vice City opens at midnight; Metacritic 99",
         tag="13 YEARS IN THE MAKING", icon="city"),
    dict(kicker="GAZA", color=(192, 57, 43),
         head="Israeli tanks cross Gaza \u2018Yellow Line\u2019",
         sub="First ground incursion since the ceasefire",
         tag="NUSEIRAT \u00b7 CENTRAL GAZA", icon="tank"),
    dict(kicker="UKRAINE", color=(46, 111, 183),
         head="Crimea Bridge attacked again",
         sub="Traffic halted days after its span collapsed",
         tag="KERCH STRAIT", icon="bridge"),
]

TICKER = [
    "Van Gogh sells for record $190.4m \u00b7 Cyclone Akvan nears India coast",
    "Stacy Keach dies at 85 \u00b7 Estonia to shut Russia border \u00b7 Prague crowds protest media law",
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def star(d, cx, cy, r1, r2, n, fill):
    pts = []
    for i in range(2 * n):
        r = r1 if i % 2 == 0 else r2
        a = math.pi * i / n - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=fill)


def draw_icon(d, kind, x, y, s):
    """Flat pictogram inside an s x s box at (x, y)."""
    if kind == "flags":
        # Three small simplified flags: China, USA, Russia.
        d.rectangle([x + 2, y + 8, x + s * 0.32, y + s * 0.55],
                    fill=(222, 41, 16))
        star(d, x + s * 0.13, y + s * 0.22, 9, 4, 5, (255, 222, 0))
        d.rectangle([x + s * 0.36, y + 8, x + s * 0.66, y + s * 0.55],
                    fill=(255, 255, 255), outline=(180, 180, 180))
        for i in range(4):
            d.rectangle([x + s * 0.36, y + 8 + i * 11,
                         x + s * 0.66, y + 8 + i * 11 + 5],
                        fill=(178, 34, 52))
        d.rectangle([x + s * 0.36, y + 8, x + s * 0.5, y + s * 0.3],
                    fill=(60, 59, 110))
        d.rectangle([x + s * 0.7, y + 8, x + s - 2, y + s * 0.55],
                    fill=(255, 255, 255), outline=(180, 180, 180))
        d.rectangle([x + s * 0.7, y + s * 0.23, x + s - 2, y + s * 0.4],
                    fill=(0, 57, 166))
        d.rectangle([x + s * 0.7, y + s * 0.4, x + s - 2, y + s * 0.55],
                    fill=(213, 0, 50))
        for fx in (0.17, 0.51, 0.85):
            d.line([x + s * fx, y + s * 0.55, x + s * fx, y + s * 0.92],
                   fill=(120, 120, 120), width=3)
    elif kind == "scales":
        # Scales of justice: pillar, beam, two pans.
        d.rectangle([x + s * 0.47, y + s * 0.14, x + s * 0.53, y + s * 0.82],
                    fill=(31, 95, 168))
        d.rectangle([x + s * 0.34, y + s * 0.82, x + s * 0.66, y + s * 0.9],
                    fill=(31, 95, 168))
        d.line([x + s * 0.12, y + s * 0.22, x + s * 0.88, y + s * 0.22],
               fill=(31, 95, 168), width=5)
        d.ellipse([x + s * 0.44, y + s * 0.08, x + s * 0.56, y + s * 0.18],
                  fill=(232, 163, 61))
        for px in (0.18, 0.82):
            d.line([x + s * px, y + s * 0.22, x + s * (px - 0.1),
                    y + s * 0.42], fill=(31, 95, 168), width=3)
            d.line([x + s * px, y + s * 0.22, x + s * (px + 0.1),
                    y + s * 0.42], fill=(31, 95, 168), width=3)
            d.pieslice([x + s * (px - 0.12), y + s * 0.36,
                        x + s * (px + 0.12), y + s * 0.56],
                       0, 180, fill=(232, 163, 61))
    elif kind == "chart":
        # Rising bar chart with an arrow.
        bars = [(0.12, 0.45), (0.32, 0.6), (0.52, 0.38), (0.72, 0.72)]
        for bx, bh in bars:
            d.rectangle([x + s * bx, y + s * (0.85 - bh),
                         x + s * (bx + 0.14), y + s * 0.85],
                        fill=(46, 111, 80))
        d.line([x + s * 0.08, y + s * 0.85, x + s * 0.92, y + s * 0.85],
               fill=(20, 20, 20), width=3)
        d.line([x + s * 0.1, y + s * 0.42, x + s * 0.34, y + s * 0.28,
                x + s * 0.58, y + s * 0.38, x + s * 0.86, y + s * 0.1],
               fill=(232, 163, 61), width=5)
        d.polygon([(x + s * 0.86, y + s * 0.1), (x + s * 0.72, y + s * 0.1),
                   (x + s * 0.86, y + s * 0.24)], fill=(232, 163, 61))
    elif kind == "city":
        # Neon skyline: towers, windows, a setting sun.
        d.ellipse([x + s * 0.62, y + s * 0.12, x + s * 0.9, y + s * 0.4],
                  fill=(232, 163, 61))
        for bx, bw, bh in [(0.06, 0.2, 0.55), (0.3, 0.16, 0.7),
                           (0.5, 0.2, 0.45), (0.74, 0.18, 0.62)]:
            d.rectangle([x + s * bx, y + s * (0.9 - bh),
                         x + s * (bx + bw), y + s * 0.9],
                        fill=(120, 60, 150))
            for wy in range(3):
                for wx in range(2):
                    d.rectangle([x + s * (bx + 0.03 + wx * 0.08),
                                 y + s * (0.9 - bh + 0.08 + wy * 0.14),
                                 x + s * (bx + 0.07 + wx * 0.08),
                                 y + s * (0.9 - bh + 0.15 + wy * 0.14)],
                                fill=(255, 222, 0))
        d.rectangle([x + s * 0.06, y + s * 0.9, x + s * 0.94, y + s * 0.94],
                    fill=(20, 20, 20))
    elif kind == "tank":
        # Simple tank: hull, turret, barrel, tracks.
        d.rectangle([x + s * 0.12, y + s * 0.52, x + s * 0.88, y + s * 0.72],
                    fill=(110, 110, 100))
        d.rectangle([x + s * 0.32, y + s * 0.34, x + s * 0.62, y + s * 0.52],
                    fill=(140, 140, 128))
        d.line([x + s * 0.62, y + s * 0.42, x + s * 0.94, y + s * 0.36],
               fill=(140, 140, 128), width=7)
        d.rectangle([x + s * 0.08, y + s * 0.72, x + s * 0.92, y + s * 0.86],
                    fill=(60, 60, 55))
        for wx in range(5):
            d.ellipse([x + s * (0.14 + wx * 0.16), y + s * 0.75,
                       x + s * (0.22 + wx * 0.16), y + s * 0.83],
                      fill=(200, 200, 190))
    elif kind == "bridge":
        # Broken bridge: two deck ends, a fallen span, water below.
        d.rectangle([x + 4, y + s * 0.3, x + s * 0.4, y + s * 0.4],
                    fill=(70, 90, 120))
        d.rectangle([x + s * 0.6, y + s * 0.3, x + s - 4, y + s * 0.4],
                    fill=(70, 90, 120))
        d.polygon([(x + s * 0.42, y + s * 0.52), (x + s * 0.6, y + s * 0.46),
                   (x + s * 0.58, y + s * 0.56), (x + s * 0.4, y + s * 0.62)],
                  fill=(192, 57, 43))
        d.line([x + s * 0.2, y + s * 0.3, x + s * 0.2, y + s * 0.08],
               fill=(46, 111, 183), width=4)
        d.line([x + s * 0.8, y + s * 0.3, x + s * 0.8, y + s * 0.08],
               fill=(46, 111, 183), width=4)
        d.line([x + s * 0.2, y + s * 0.08, x + s * 0.4, y + s * 0.3],
               fill=(46, 111, 183), width=3)
        d.line([x + s * 0.8, y + s * 0.08, x + s * 0.6, y + s * 0.3],
               fill=(46, 111, 183), width=3)
        for yy in (0.78, 0.88):
            d.arc([x + 4, y + s * yy, x + s - 4, y + s * (yy + 0.12)],
                  0, 180, fill=(46, 111, 183), width=4)


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ----
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 134], fill=GOLD)
    d.text((24, 16), "THE WORLD IN ONE DAY",
           font=font(BOLD, 26), fill=GOLD)
    d.text((24, 50), "THURSDAY 19 NOVEMBER 2026",
           font=font(BOLD, 46), fill=WHITE)
    # small globe mark, top right
    gx, gy = 946, 32
    d.ellipse([gx, gy, gx + 56, gy + 56], outline=GOLD, width=4)
    d.ellipse([gx + 14, gy, gx + 42, gy + 56], outline=GOLD, width=3)
    d.line([gx, gy + 28, gx + 56, gy + 28], fill=GOLD, width=3)
    d.arc([gx + 5, gy + 11, gx + 51, gy + 45], 200, 340, fill=GOLD, width=3)

    # ---- six story panels, 2 x 3 ----
    px, py, pw, ph, gap = 16, 146, 490, 242, 12
    for i, st in enumerate(STORIES):
        x = px + (i % 2) * (pw + gap)
        y = py + (i // 2) * (ph + gap)
        d.rounded_rectangle([x, y, x + pw, y + ph], radius=10, fill=WHITE)
        d.rounded_rectangle([x, y, x + pw, y + 8], radius=4,
                            fill=st["color"])
        d.rectangle([x, y + 4, x + pw, y + 8], fill=st["color"])
        # icon tile, top right
        ix, iy, isz = x + pw - 122, y + 22, 100
        d.rounded_rectangle([ix, iy, ix + isz, iy + isz], radius=8,
                            fill=TILE)
        draw_icon(d, st["icon"], ix, iy, isz)
        # kicker + headline + sub
        tx = x + 18
        d.text((tx, y + 20), st["kicker"], font=font(BOLD, 20),
               fill=st["color"])
        head_lines = wrap(d, st["head"], font(BOLD, 28), 340)
        yy = y + 50
        for ln in head_lines[:3]:
            d.text((tx, yy), ln, font=font(BOLD, 28), fill=INK)
            yy += 34
        sub_lines = wrap(d, st["sub"], font(REG, 20), 452)
        yy = yy + 10
        for ln in sub_lines[:2]:
            d.text((tx, yy), ln, font=font(REG, 20), fill=GREY)
            yy += 25
        # fact chip along the panel's bottom edge
        chip_fnt = font(BOLD, 17)
        tw = d.textlength(st["tag"], font=chip_fnt)
        cy = max(y + ph - 42, yy + 8)
        d.rounded_rectangle([tx, cy, tx + tw + 20, cy + 28], radius=14,
                            outline=st["color"], width=2)
        d.text((tx + 10, cy + 4), st["tag"], font=chip_fnt, fill=st["color"])

    # ---- footer ticker ----
    d.rectangle([0, 902, W, H], fill=NAVY)
    d.text((24, 912), "ALSO TODAY", font=font(BOLD, 20), fill=GOLD)
    d.text((24, 938), TICKER[0], font=font(REG, 18), fill=WHITE)
    d.text((24, 964), TICKER[1], font=font(REG, 18), fill=WHITE)
    d.text((24, 994), "Sources: NYT, BBC, Reuters, ICJ, The Guardian \u2014 19 Nov 2026",
           font=font(REG, 15), fill=(160, 170, 185))

    img.save(path, "PNG", optimize=True)


if __name__ == "__main__":
    import sys
    build(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
