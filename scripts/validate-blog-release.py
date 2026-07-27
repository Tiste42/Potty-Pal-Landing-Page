"""Fail-closed validation for one Potty Pal blog release."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--category", required=True)
    args = parser.parse_args()

    root = Path.cwd().resolve()
    article = root / "blog" / f"{args.slug}.html"
    image_path = root / "images" / "blog" / f"{args.slug}.webp"
    blog_index = root / "blog" / "index.html"
    category_page = root / "blog" / "category" / f"{args.category}.html"
    sitemap = root / "sitemap.xml"
    errors: list[str] = []

    for path in [article, image_path, blog_index, category_page, sitemap]:
        require(path.is_file(), f"Missing required file: {path.relative_to(root)}", errors)

    if errors:
        raise SystemExit("\n".join(errors))

    article_html = article.read_text(encoding="utf-8")
    require(
        f"https://www.pottypalai.com/blog/{args.slug}.html" in article_html,
        "Article canonical URL is missing or incorrect",
        errors,
    )
    require(f"../images/blog/{args.slug}.webp" in article_html, "Article hero reference is missing", errors)
    require(article_html.lower().count("<h1") == 1, "Article must contain exactly one H1", errors)
    require("<h2>Frequently Asked Questions</h2>" in article_html, "FAQ section is missing", errors)

    with Image.open(image_path) as hero:
        require(hero.format == "WEBP", "Hero image is not WebP", errors)
        require(hero.size == (1200, 675), f"Hero image is {hero.size}, expected (1200, 675)", errors)

    for path, label in [(blog_index, "blog index"), (category_page, "category page"), (sitemap, "sitemap")]:
        require(f"{args.slug}.html" in path.read_text(encoding="utf-8"), f"{label} does not reference the article", errors)

    for href in re.findall(r'href=["\']([^"\']+)["\']', article_html, flags=re.IGNORECASE):
        parsed = urlparse(href)
        if parsed.scheme in {"http", "https", "mailto", "tel"} or href.startswith(("#", "javascript:")):
            continue
        target = (article.parent / parsed.path).resolve()
        if parsed.path.endswith("/"):
            target = target / "index.html"
        require(target.exists(), f"Broken internal link: {href}", errors)

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated blog/{args.slug}.html and all release references")


if __name__ == "__main__":
    main()
