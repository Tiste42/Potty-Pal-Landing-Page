"""Generate a dependable, branded 1200x675 WebP hero for Potty Pal articles."""

from __future__ import annotations

import argparse
import hashlib
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 675
PALETTES = [
    ("#EAF8F6", "#C7F0EA", "#1A535C", "#FF6B6B"),
    ("#FFF7EA", "#FFE2B8", "#1A535C", "#F59E5B"),
    ("#F4F0FF", "#DDD4FF", "#263238", "#8B7CF6"),
    ("#EDF7FF", "#CFEAFF", "#1A535C", "#4ECDC4"),
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def wrap_for_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:4]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()
    allowed_root = (repo_root / "images" / "blog").resolve()
    output = Path(args.output).resolve()
    if allowed_root not in output.parents:
        raise SystemExit("Output must stay inside images/blog")
    if output.suffix.lower() != ".webp":
        raise SystemExit("Output must be a .webp file")

    palette_index = int(hashlib.sha256(args.category.encode("utf-8")).hexdigest()[:2], 16) % len(PALETTES)
    background, panel, ink, accent = PALETTES[palette_index]

    image = Image.new("RGB", (WIDTH, HEIGHT), background)
    draw = ImageDraw.Draw(image)

    # Soft branded background shapes.
    draw.ellipse((820, -150, 1320, 350), fill=panel)
    draw.ellipse((-180, 460, 360, 960), fill=panel)
    for x, y, radius in [(875, 370, 18), (1050, 440, 12), (940, 530, 9), (1110, 300, 8)]:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=accent)

    # Simple potty icon, deliberately generic and parent-facing.
    icon_x, icon_y = 900, 145
    draw.rounded_rectangle((icon_x, icon_y, icon_x + 190, icon_y + 215), radius=58, fill="#FFFFFF")
    draw.ellipse((icon_x + 30, icon_y + 25, icon_x + 160, icon_y + 112), fill=panel, outline=ink, width=8)
    draw.rounded_rectangle((icon_x + 52, icon_y + 126, icon_x + 138, icon_y + 188), radius=18, fill=accent)
    draw.rounded_rectangle((icon_x + 25, icon_y + 190, icon_x + 165, icon_y + 210), radius=8, fill=ink)

    brand_font = load_font(28, bold=True)
    title_font = load_font(55, bold=True)
    category_font = load_font(24, bold=True)
    footer_font = load_font(22)

    draw.rounded_rectangle((70, 64, 305, 112), radius=24, fill=ink)
    draw.text((94, 72), "POTTY PAL AI", font=brand_font, fill="#FFFFFF")

    category_label = args.category.replace("-", " ").upper()
    draw.text((72, 154), category_label, font=category_font, fill=accent)

    lines = wrap_for_width(draw, args.title, title_font, 700)
    y = 205
    for line in lines:
        draw.text((70, y), line, font=title_font, fill=ink)
        y += 68

    draw.rounded_rectangle((70, 565, 670, 615), radius=24, fill="#FFFFFF")
    draw.text((94, 576), "Practical help for real potty training days", font=footer_font, fill=ink)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "WEBP", quality=88, method=6)
    print(f"Generated {output} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()
