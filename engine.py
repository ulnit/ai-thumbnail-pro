#!/usr/bin/env python3
"""AI Thumbnail Pro - Auto-generate social media graphics with Pillow."""
import os, sys, json, random, textwrap
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    os.system(f"{sys.executable} -m pip install Pillow -q")
    from PIL import Image, ImageDraw, ImageFont

OUT = Path("output")
OUT.mkdir(exist_ok=True)

# ── Design presets ──────────────────────────
PRESETS = {
    "youtube":    {"w": 1280, "h": 720,  "font_scale": 1.0, "label": "YouTube Thumbnail"},
    "blog":       {"w": 1200, "h": 630,  "font_scale": 0.9, "label": "Blog Featured Image"},
    "twitter":    {"w": 1200, "h": 675,  "font_scale": 0.8, "label": "Twitter/X Card"},
    "linkedin":   {"w": 1200, "h": 627,  "font_scale": 0.8, "label": "LinkedIn Post"},
    "instagram":  {"w": 1080, "h": 1080, "font_scale": 0.9, "label": "Instagram Square"},
    "story":      {"w": 1080, "h": 1920, "font_scale": 1.1, "label": "Story / Reel"},
    "product":    {"w": 1200, "h": 800,  "font_scale": 1.0, "label": "Product Hero"},
}

# ── Color palettes ─────────────────────────
PALETTES = [
    ("#6C5CE7", "#A29BFE", "#2D3436", "#FFFFFF"),  # Purple
    ("#00B894", "#55EFC4", "#2D3436", "#FFFFFF"),  # Green
    ("#0984E3", "#74B9FF", "#2D3436", "#FFFFFF"),  # Blue
    ("#E17055", "#FAB1A0", "#2D3436", "#FFFFFF"),  # Orange
    ("#FD79A8", "#FDCB6E", "#2D3436", "#FFFFFF"),  # Pink
    ("#636E72", "#B2BEC3", "#1E272E", "#FFEAA7"),  # Dark
    ("#FDCB6E", "#FFEAA7", "#2D3436", "#2D3436"),  # Yellow
    ("#E84393", "#FD79A8", "#1E272E", "#DFE6E9"),  # Hot Pink
]

ICONS = ["🤖", "🎯", "⚡", "🔥", "🚀", "💡", "🧠", "📊", "🛠️", "🎨", "📈", "💎", "🔮", "⭐"]

def find_font(size=48):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def gradient_bg(draw, w, h, c1, c2):
    for y in range(h):
        r = int(int(c1[1:3], 16) + (int(c2[1:3], 16) - int(c1[1:3], 16)) * y / h)
        g = int(int(c1[3:5], 16) + (int(c2[3:5], 16) - int(c1[3:5], 16)) * y / h)
        b = int(int(c1[5:7], 16) + (int(c2[5:7], 16) - int(c1[5:7], 16)) * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def make_thumbnail(title, preset="youtube", palette=None, subtitle="", icon=None):
    if palette is None:
        palette = random.choice(PALETTES)
    if icon is None:
        icon = random.choice(ICONS)

    bg1, bg2, accent, text_color = palette
    cfg = PRESETS.get(preset, PRESETS["youtube"])
    w, h, fs = cfg["w"], cfg["h"], cfg["font_scale"]

    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, w, h, bg1, bg2)

    # Decorative circles
    for i in range(3):
        cx, cy = random.randint(0, w), random.randint(0, h)
        r = random.randint(60, 200)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=accent, width=2)

    # Icon
    icon_font = find_font(int(80 * fs))
    draw.text((w//2, int(h * 0.15)), icon, fill=text_color, font=icon_font, anchor="mm")

    # Title (split into lines)
    font_big = find_font(int(56 * fs))
    font_small = find_font(int(32 * fs))

    lines = textwrap.wrap(title, width=28)
    y_start = int(h * 0.42)
    for i, line in enumerate(lines[:3]):
        y = y_start + i * int(72 * fs)
        if i == 0:
            draw.text((w//2, y), line, fill=text_color, font=font_big, anchor="mm")
        else:
            draw.text((w//2, y), line, fill=text_color, font=font_small, anchor="mm")

    # Subtitle
    if subtitle:
        draw.text((w//2, int(h * 0.78)), subtitle, fill=accent, font=font_small, anchor="mm")

    # Brand line
    brand_font = find_font(int(20 * fs))
    draw.text((w//2, int(h * 0.92)), "AI Thumbnail Pro · ulnit.github.io", fill=accent, font=brand_font, anchor="mm")

    # Save
    slug = title.lower().replace(" ", "-")[:30]
    fname = OUT / f"{preset}_{slug}_{datetime.now():%H%M%S}.png"
    img.save(fname)
    return str(fname)

def batch_generate(product_name, presets_list=None):
    """Generate thumbnails for all presets."""
    if presets_list is None:
        presets_list = ["youtube", "blog", "twitter", "product"]

    results = []
    for preset in presets_list:
        print(f"  Generating {preset}...")
        path = make_thumbnail(
            title=product_name,
            preset=preset,
            subtitle=f"Built on $35 Raspberry Pi · 100% Automated",
        )
        results.append(path)
    return results

# ── CLI ────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AI Thumbnail Pro")
    parser.add_argument("title", nargs="?", default="AI Automation", help="Thumbnail title")
    parser.add_argument("--preset", default="youtube", choices=list(PRESETS.keys()))
    parser.add_argument("--batch", action="store_true", help="Generate all presets")
    parser.add_argument("--subtitle", default="", help="Subtitle text")
    args = parser.parse_args()

    if args.batch:
        paths = batch_generate(args.title)
        print(f"\n✅ Generated {len(paths)} thumbnails:")
        for p in paths: print(f"   {p}")
    else:
        path = make_thumbnail(args.title, preset=args.preset, subtitle=args.subtitle)
        print(f"✅ Saved: {path}")