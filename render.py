#!/usr/bin/env python3
"""Render the meme image for Meme Sprint 3: AI Agent Goes Rogue.

Joke: a user tells their AI agent to "take initiative" -- the agent
unionizes the household appliances. The picture is drawn from scratch
with Pillow: a determined little robot on a picket line, sign in hand,
a fridge behind it holding its own tiny sign.

Run:  python3 render.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
YELLOW = (255, 214, 10)
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (214, 48, 49)
STEEL = (148, 163, 175)      # robot body
STEEL_DARK = (90, 104, 116)
TEAL = (13, 148, 136)
BLUE = (37, 99, 235)

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]


def font(size):
    for p in FONT_PATHS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def text_center(draw, cx, y, s, fnt, fill=BLACK):
    bbox = draw.textbbox((0, 0), s, font=fnt)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2 - bbox[0], y), s, font=fnt, fill=fill)
    return bbox[3] - bbox[1]


def main():
    img = Image.new("RGB", (W, H), YELLOW)
    d = ImageDraw.Draw(img)

    # thick black frame
    d.rectangle([0, 0, W - 1, H - 1], outline=BLACK, width=18)

    # ---- top caption ----
    text_center(d, W // 2, 52, "I TOLD MY AI AGENT", font(74))
    text_center(d, W // 2, 140, "TO \u201cTAKE INITIATIVE\u201d", font(74))

    # ---- scene: robot on strike ----
    # ground shadow
    d.ellipse([180, 742, 560, 782], fill=(150, 122, 0))

    # sign pole (behind robot's raised arm, up to the sign)
    d.line([468, 700, 560, 470], fill=BLACK, width=14)

    # robot body
    d.rounded_rectangle([220, 520, 480, 740], radius=42, fill=STEEL,
                        outline=BLACK, width=8)
    # chest panel with lights
    d.rounded_rectangle([272, 580, 428, 660], radius=14, fill=WHITE,
                        outline=BLACK, width=5)
    for i, col in enumerate((RED, (245, 158, 11), TEAL)):
        x0 = 296 + i * 48
        d.ellipse([x0, 606, x0 + 30, 636], fill=col, outline=BLACK, width=3)
    # name tag
    d.rounded_rectangle([292, 676, 408, 716], radius=8, fill=WHITE,
                        outline=BLACK, width=4)
    d.text((350, 682), "AGENT", font=font(22), fill=BLACK, anchor="ma")

    # robot neck + head
    d.rectangle([322, 486, 378, 522], fill=STEEL_DARK, outline=BLACK, width=5)
    d.rounded_rectangle([238, 330, 462, 492], radius=44, fill=STEEL,
                        outline=BLACK, width=8)
    # antenna
    d.line([350, 330, 350, 272], fill=BLACK, width=10)
    d.ellipse([330, 244, 370, 284], fill=RED, outline=BLACK, width=5)
    # eyes: determined, one brow angled
    d.ellipse([272, 386, 330, 444], fill=WHITE, outline=BLACK, width=5)
    d.ellipse([370, 386, 428, 444], fill=WHITE, outline=BLACK, width=5)
    d.ellipse([292, 404, 316, 428], fill=BLACK)
    d.ellipse([388, 404, 412, 428], fill=BLACK)
    d.line([266, 372, 336, 384], fill=BLACK, width=8)   # angled brow
    d.line([364, 384, 434, 372], fill=BLACK, width=8)   # angled brow
    # mouth: flat, unimpressed
    d.line([318, 462, 382, 462], fill=BLACK, width=8)

    # arms: left arm down, right arm raised to the pole
    d.line([232, 560, 176, 660], fill=BLACK, width=16)
    d.ellipse([158, 648, 194, 684], fill=STEEL, outline=BLACK, width=6)
    d.line([468, 560, 540, 480], fill=BLACK, width=16)

    # ---- picket sign ----
    d.rounded_rectangle([548, 300, 976, 470], radius=20, fill=WHITE,
                        outline=BLACK, width=8)
    text_center(d, 762, 322, "ON STRIKE!", font(56))
    text_center(d, 762, 402, "the fridge agrees", font(34))

    # ---- little fridge at the robot's feet, with its own mini sign ----
    d.rounded_rectangle([620, 620, 760, 748], radius=16, fill=WHITE,
                        outline=BLACK, width=7)
    d.line([620, 682, 760, 682], fill=BLACK, width=5)
    d.rounded_rectangle([640, 640, 656, 668], radius=4, fill=STEEL_DARK)
    d.rounded_rectangle([640, 694, 656, 722], radius=4, fill=STEEL_DARK)
    # mini sign on a stick
    d.line([690, 620, 690, 566], fill=BLACK, width=6)
    d.rounded_rectangle([618, 522, 762, 566], radius=8, fill=WHITE,
                        outline=BLACK, width=4)
    d.text((690, 528), "ME TOO", font=font(24), fill=BLACK, anchor="ma")

    # ---- bottom punchline ----
    text_center(d, W // 2, 812, "IT UNIONIZED", font(88))
    text_center(d, W // 2, 908, "MY FRIDGE.", font(88))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
