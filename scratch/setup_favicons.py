#!/usr/bin/env python3
"""Copy favicon assets to site root, generate dark variant, inject links in HTML."""

import re
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FAVICON_DIR = ROOT / "favicon"

FAVICON_FILES = [
    "favicon.svg",
    "favicon-96x96.png",
    "favicon.ico",
    "apple-touch-icon.png",
    "site.webmanifest",
    "web-app-manifest-192x192.png",
    "web-app-manifest-512x512.png",
]

FAVICON_BLOCK = """  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" media="(prefers-color-scheme: light)">
  <link rel="icon" type="image/png" href="/favicon-96x96-dark.png" sizes="96x96" media="(prefers-color-scheme: dark)">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <meta name="apple-mobile-web-app-title" content="Filos">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#041830" media="(prefers-color-scheme: dark)">
"""


def create_dark_png() -> None:
    src = FAVICON_DIR / "favicon-96x96.png"
    dst = FAVICON_DIR / "favicon-96x96-dark.png"
    image = Image.open(src).convert("RGBA")
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a:
                pixels[x, y] = (255 - r, 255 - g, 255 - b, a)

    image.save(dst)


def copy_assets_to_root() -> None:
    for name in FAVICON_FILES:
        shutil.copy2(FAVICON_DIR / name, ROOT / name)

    shutil.copy2(FAVICON_DIR / "favicon-96x96-dark.png", ROOT / "favicon-96x96-dark.png")


def inject_favicon_links() -> int:
    updated = 0
    marker = "<!-- Favicon -->"

    for html_path in ROOT.rglob("*.html"):
        if "scratch" in html_path.parts:
            continue

        content = html_path.read_text(encoding="utf-8")
        if marker in content:
            continue

        patterns = [
            r'(<meta[^>]+name=["\']viewport["\'][^>]*>)',
            r'(<meta[^>]+content=["\'][^"\']*["\'][^>]+name=["\']viewport["\'][^>]*>)',
        ]

        new_content = None
        for pattern in patterns:
            match = re.search(pattern, content, flags=re.IGNORECASE)
            if match:
                insert_at = match.end()
                new_content = content[:insert_at] + "\n" + FAVICON_BLOCK + content[insert_at:]
                break

        if new_content is None:
            head_match = re.search(r"<head[^>]*>", content, flags=re.IGNORECASE)
            if not head_match:
                continue
            insert_at = head_match.end()
            new_content = content[:insert_at] + "\n" + FAVICON_BLOCK + content[insert_at:]

        html_path.write_text(new_content, encoding="utf-8")
        updated += 1

    return updated


def main() -> None:
    create_dark_png()
    copy_assets_to_root()
    count = inject_favicon_links()
    print(f"Favicons configured. Updated {count} HTML files.")


if __name__ == "__main__":
    main()
