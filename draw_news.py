"""Draw the 19 November 2026 world-news front page (1024 x 1024 PNG).

Everything is drawn with Pillow primitives: no network, no fetched assets,
no timestamps, so the output is byte-identical on every run.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 243, 234)
NAVY = (16, 28, 58)
NAVY_SOFT = (28, 44, 82)
GOLD = (212, 160, 32)
WHITE = (255, 255, 255)
INK = (24, 24, 24)
GREY = (96, 96, 96)
CARD = (255, 255, 255)
ICON_BG = (238, 234, 224)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731
REG = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731


STORIES = [
    {
        "kicker": "APEC · SHENZHEN",
        "color": (176, 124, 12),
        "headline": "Trump, Xi and Putin meet in Shenzhen",
        "sub": "Trilateral talks; Xi hugs Trump on arrival",
        "tag": "SHENZHEN · APEC 2026",
        "icon": "flags",
    },
    {
        "kicker": "THE HAGUE",
        "color": (28, 84, 160),
        "headline": "World Court rules on Rohingya case",
        "sub": "Verdict read today; Gambia v. Myanmar",
        "tag": "ICJ · 08:00 GMT",
        "icon": "scales",
    },
    {
        "kicker": "MARKETS · AI",
        "color": (32, 116, 64),
        "headline": "Anthropic debuts in biggest IPO ever",
        "sub": "$81.3bn at $83 a share; trades as ANT",
        "tag": "~$1.5TN VALUATION",
        "icon": "chart",
    },
    {
        "kicker": "CULTURE",
        "color": (120, 52, 150),
        "headline": "GTA VI rolls out worldwide",
        "sub": "Vice City opens at midnight; Metacritic 99",
        "tag": "13 YEARS IN THE MAKING",
        "icon": "city",
    },
    {
        "kicker": "GAZA",
        "color": (178, 44, 32),
        "headline": "Israeli tanks cross Gaza 'Yellow Line'",
        "sub": "First ground incursion since ceasefire",
        "tag": "NUSEIRAT · CENTRAL GAZA",
        "icon": "tank",
    },
    {
        "kicker": "UKRAINE",
        "color": (28, 84, 160),
        "headline": "Crimean Bridge attacked again",
        "sub": "Traffic halted after its span collapsed",
        "tag": "KERCH STRAIT",
        "icon": "bridge",
    },
]

TICKER = (
    "Van Gogh sells for record $190.4m · Cyclone Akvan nears India coast · "
    "Stacy Keach dies at 85 · Estonia to shut Russia border · "
    "Prague crowds protest media law"
)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning lines that fit inside max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def pill(draw, x, y, text, fnt, fg, outline):
    tw = draw.textlength(text, font=fnt)
    pad_x, pad_y = 14, 7
    box = [x, y, x + tw + 2 * pad_x, y + fnt.size + 2 * pad_y]
    draw.rounded_rectangle(box, radius=13, outline=outline, width=2)
    draw.text((x + pad_x, y + pad_y - 1), text, font=fnt, fill=fg)
    return box[2]


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=4)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                 outline=GOLD, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=GOLD, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             start=200, end=340, fill=GOLD, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             start=20, end=160, fill=GOLD, width=3)


def draw_icon(draw, kind, x, y, s):
    """Small pictogram inside a rounded square of side s at (x, y)."""
    draw.rounded_rectangle([x, y, x + s, y + s], radius=12, fill=ICON_BG)
    if kind == "flags":
        for i, cols in enumerate([
            [(222, 32, 32), (255, 215, 0)],
            [(190, 30, 45), (255, 255, 255), (30, 60, 140)],
            [(255, 255, 255), (30, 80, 180), (200, 30, 30)],
        ]):
            fx = x + 14 + i * 34
            draw.rectangle([fx, y + 22, fx + 26, y + 58], fill=cols[0],
                           outline=(120, 120, 120), width=1)
            if i == 0:
                draw.ellipse([fx + 5, y + 27, fx + 12, y + 34], fill=cols[1])
            elif i == 1:
                for k in range(4):
                    draw.rectangle([fx + 2, y + 24 + k * 8, fx + 24,
                                    y + 28 + k * 8],
                                   fill=(190, 30, 45) if k % 2 == 0
                                   else (255, 255, 255))
                draw.rectangle([fx, y + 22, fx + 13, y + 38],
                               fill=(30, 60, 140))
            else:
                draw.rectangle([fx, y + 22, fx + 26, y + 33], fill=cols[0])
                draw.rectangle([fx, y + 33, fx + 26, y + 44], fill=cols[1])
                draw.rectangle([fx, y + 44, fx + 26, y + 58], fill=cols[2])
            draw.line([fx + 13, y + 58, fx + 13, y + 82], fill=(110, 110, 110),
                      width=2)
    elif kind == "scales":
        cx = x + s // 2
        draw.line([cx, y + 14, cx, y + 78], fill=(40, 80, 150), width=5)
        draw.line([x + 14, y + 22, x + s - 14, y + 22], fill=(40, 80, 150),
                  width=5)
        draw.ellipse([cx - 6, y + 12, cx + 6, y + 24], fill=GOLD)
        for side in (-1, 1):
            px = cx + side * (s // 2 - 16)
            draw.line([px, y + 22, px, y + 46], fill=(40, 80, 150), width=3)
            draw.polygon([(px - 20, y + 46), (px + 20, y + 46), (px, y + 66)],
                         fill=(240, 180, 60), outline=(180, 130, 20))
        draw.line([x + 22, y + 78, x + s - 22, y + 78], fill=(40, 80, 150),
                  width=5)
    elif kind == "chart":
        base = y + s - 18
        heights = [26, 44, 34, 58]
        for i, hh in enumerate(heights):
            bx = x + 16 + i * 24
            draw.rectangle([bx, base - hh, bx + 16, base],
                           fill=(32, 116, 64))
        pts = [(x + 16, base - 34), (x + 40, base - 54), (x + 64, base - 42),
               (x + 88, base - 68)]
        draw.line(pts, fill=(220, 140, 20), width=4, joint="curve")
        draw.polygon([(pts[-1][0] - 2, pts[-1][1] + 12), (pts[-1][0] + 12,
                       pts[-1][1] + 2), (pts[-1][0] + 2, pts[-1][1] - 8)],
                     fill=(220, 140, 20))
        draw.line([x + 12, base, x + s - 12, base], fill=INK, width=3)
    elif kind == "city":
        draw.ellipse([x + s - 30, y + 10, x + s - 8, y + 32], fill=(240, 170, 40))
        builds = [(14, 44, 20, 32), (38, 30, 22, 46), (64, 48, 18, 28)]
        for bx, by, bw, bh in builds:
            draw.rectangle([x + bx, y + by, x + bx + bw, y + by + bh],
                           fill=(90, 60, 140))
            for wy in range(by + 7, by + bh - 5, 11):
                for wx in range(bx + 5, bx + bw - 4, 9):
                    draw.rectangle([x + wx, y + wy, x + wx + 4, y + wy + 5],
                                   fill=(255, 220, 90))
        draw.line([x + 10, y + s - 10, x + s - 10, y + s - 10], fill=INK,
                  width=3)
    elif kind == "tank":
        draw.rectangle([x + 20, y + 52, x + s - 20, y + 72], fill=(110, 110, 105))
        draw.rectangle([x + 34, y + 36, x + 66, y + 54], fill=(90, 90, 85))
        draw.rectangle([x + 66, y + 42, x + s - 12, y + 48], fill=(90, 90, 85))
        for i in range(5):
            wx = x + 22 + i * 12
            draw.ellipse([wx, y + 70, wx + 10, y + 80], fill=(40, 40, 40))
        draw.rectangle([x + 16, y + 68, x + s - 16, y + 82], outline=(60, 60, 60),
                       width=2)
    elif kind == "bridge":
        draw.line([x + 10, y + 66, x + s - 10, y + 66], fill=(30, 80, 160),
                  width=6)
        for tx in (x + 26, x + s - 38):
            draw.rectangle([tx, y + 22, tx + 12, y + 66], fill=(30, 80, 160))
        draw.line([x + 32, y + 24, x + s // 2, y + 62], fill=(30, 80, 160),
                  width=3)
        draw.line([x + s - 32, y + 24, x + s // 2, y + 62],
                  fill=(30, 80, 160), width=3)
        draw.line([x + 14, y + 78, x + s - 14, y + 78], fill=(90, 160, 210),
                  width=3)
        draw.line([x + 22, y + 88, x + s - 22, y + 88], fill=(90, 160, 210),
                  width=3)


def draw_header(draw):
    draw.rectangle([0, 0, W, 118], fill=NAVY)
    draw.rectangle([0, 118, W, 124], fill=GOLD)
    draw.text((28, 16), "THE WORLD IN ONE DAY", font=BOLD(30), fill=GOLD)
    draw.text((28, 50), "THURSDAY 19 NOVEMBER 2026", font=BOLD(44),
              fill=WHITE)
    draw_globe(draw, 956, 58, 32)


def draw_panel(draw, story, px, py, pw, ph):
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=10, fill=CARD)
    draw.rectangle([px, py, px + pw, py + 8], fill=story["color"])
    draw.rectangle([px, py + 8, px + 8, py + ph], fill=story["color"])
    tx = px + 24
    draw.text((tx, py + 20), story["kicker"], font=BOLD(24),
              fill=story["color"])
    draw_icon(draw, story["icon"], px + pw - 112, py + 16, 88)
    head_lines = wrap(draw, story["headline"], BOLD(29), pw - 180)[:3]
    hy = py + 56
    for line in head_lines:
        draw.text((tx, hy), line, font=BOLD(29), fill=INK)
        hy += 34
    draw.text((tx, py + 164), story["sub"], font=REG(20), fill=GREY)
    pill(draw, tx, py + ph - 44, story["tag"], BOLD(19),
         story["color"], story["color"])


def draw_footer(draw):
    draw.rectangle([0, 884, W, H], fill=NAVY)
    draw.text((28, 898), "ALSO TODAY", font=BOLD(26), fill=GOLD)
    lines = wrap(draw, TICKER, REG(24), W - 56)
    fy = 930
    for line in lines[:2]:
        draw.text((28, fy), line, font=REG(24), fill=WHITE)
        fy += 30
    draw.text((28, 994), "Sources: NYT, BBC, Reuters, ICJ, The Guardian — 19 Nov 2026",
              font=REG(19), fill=(150, 160, 180))


def build_image():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    gx, gy = 16, 132
    pw, ph = 492, 244
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        draw_panel(draw, story, gx + col * (pw + 16), gy + row * (ph + 10),
                   pw, ph)
    draw_footer(draw)
    return img
