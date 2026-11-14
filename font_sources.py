"""Builds the font dropdown from the node's font_cache folder, InvokeAI's fonts folder and the installed system fonts.

The list is read once when InvokeAI starts, so restart InvokeAI after adding a font.
"""
import os
from pathlib import Path
from typing import Literal

from PIL import ImageFont

FONT_EXTENSIONS = (".ttf", ".otf")
NODE_FONT_CACHE = Path(__file__).resolve().parent / "font_cache"
NODE_FONT_CACHE.mkdir(exist_ok=True)


def _font_dirs() -> list[Path]:
    dirs = [NODE_FONT_CACHE]
    try:
        from invokeai.app.services.config.config_default import get_config

        dirs.append(Path(get_config().fonts_path))
    except Exception:
        pass
    if os.name == "nt":
        windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
        dirs.append(windir / "Fonts")
        local = os.environ.get("LOCALAPPDATA")
        if local:
            dirs.append(Path(local) / "Microsoft" / "Windows" / "Fonts")
    else:
        dirs += [Path("/usr/share/fonts"), Path("/usr/local/share/fonts"), Path.home() / ".fonts",
                 Path("/Library/Fonts"), Path.home() / "Library" / "Fonts"]
    return dirs


def _display_name(path: Path) -> str:
    try:
        family, style = ImageFont.truetype(str(path), 16).getname()
    except Exception:
        return path.name
    family, style = (family or path.stem).strip(), (style or "").strip()
    return family if style.lower() in ("", "regular", "normal", "roman") else f"{family} {style}"


def scan_fonts() -> dict[str, str]:
    """Return {dropdown label: font file path}. Earlier folders win when labels collide."""
    fonts: dict[str, str] = {}
    for d in _font_dirs():
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*")):
            if p.suffix.lower() not in FONT_EXTENSIONS or not p.is_file():
                continue
            label = _display_name(p)
            if label in fonts:
                if fonts[label] == str(p):
                    continue
                label = f"{label} ({p.name})"
                if label in fonts:
                    continue
            fonts[label] = str(p)
    return dict(sorted(fonts.items(), key=lambda kv: kv[0].lower()))


AVAILABLE_FONTS = scan_fonts()
FontLiteral = Literal[("None", *AVAILABLE_FONTS.keys())]  # type: ignore[valid-type]


def resolve_font(label: str) -> str | None:
    """Map a dropdown label back to a file path (rescans in case files moved since startup)."""
    if label in AVAILABLE_FONTS and os.path.isfile(AVAILABLE_FONTS[label]):
        return AVAILABLE_FONTS[label]
    return scan_fonts().get(label)
