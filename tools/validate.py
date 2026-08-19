"""
Aetheris theme validator.

Validates a whitelabel JSON document against the runtime schema and a
theme CSS file against the required token set. Pure standard library.

Exit codes: 0 = valid, 1 = errors found, 2 = usage error.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

REQUIRED_JSON_KEYS = {
    "brand": {"name", "tagline", "logoUrl", "logoDarkUrl", "domain"},
    "theme": {"accent", "radius", "fontFamily"},
    "navigation": None,  # list
    "contact": {"email", "supportUrl", "twitterUrl"},
    "seo": {"defaultTitle", "defaultDescription", "ogImage", "keywords"},
    "modules": {"billing", "vncConsole", "pterodactyl", "proxmox", "virtfusion", "registrars"},
    "integrations": {"stripe", "paypal", "mollie", "namecheap", "cloudflare", "cpanel", "directadmin"},
}

ALLOWED_ACCENTS = {"emerald", "indigo", "amber", "violet"}

REQUIRED_CSS_TOKENS = {
    "--aetheris-bg",
    "--aetheris-surface",
    "--aetheris-raised",
    "--aetheris-border",
    "--aetheris-fg",
    "--aetheris-muted",
    "--aetheris-faint",
    "--aetheris-success",
    "--aetheris-danger",
    "--aetheris-warning",
    "--aetheris-accent",
    "--aetheris-accent-strong",
    "--aetheris-accent-soft",
    "--aetheris-radius",
}

def validate_json(path: Path, errors: List[str], warnings: List[str]) -> bool:
    """Validate a whitelabel JSON document. Returns True when valid."""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON ({exc})")
        return False

    ok = True

    for key, required in REQUIRED_JSON_KEYS.items():
        if key not in payload:
            errors.append(f"{path}: missing top-level key '{key}'")
            ok = False
            continue
        if required is None:
            if not isinstance(payload[key], list):
                errors.append(f"{path}: '{key}' must be a list")
                ok = False
            continue
        if isinstance(payload[key], dict):
            missing = required - set(payload[key].keys())
            if missing:
                errors.append(f"{path}: '{key}' missing {sorted(missing)}")
                ok = False

    # Theme-specific rules.
    theme = payload.get("theme", {})
    accent = theme.get("accent")
    if accent is not None and accent not in ALLOWED_ACCENTS:
        errors.append(f"{path}: accent '{accent}' is not registered in ALLOWED_ACCENTS")
        ok = False
    radius = theme.get("radius")
    if isinstance(radius, int) and not (0 <= radius <= 32):
        errors.append(f"{path}: radius {radius} out of range 0-32")
        ok = False
    if isinstance(radius, bool):
        errors.append(f"{path}: radius must be an integer")
        ok = False

    # Navigation items.
    navigation = payload.get("navigation")
    if isinstance(navigation, list):
        for item in navigation:
            if not isinstance(item, dict) or not {"label", "href", "cta"} <= set(item.keys()):
                errors.append(f"{path}: navigation item missing label/href/cta")
                ok = False
            elif not isinstance(item.get("cta"), bool):
                errors.append(f"{path}: navigation 'cta' must be boolean")
                ok = False

    # Contrast hint: fg against bg must be readable (WCAG-style luminance check).
    css = path.with_suffix(".css")
    if css.exists():
        validate_css(css, errors, warnings)

    return ok


def _luminance(rgb: Tuple[int, int, int]) -> float:
    def channel(value: float) -> float:
        value /= 255.0
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def _contrast_ratio(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> float:
    la, lb = _luminance(a), _luminance(b)
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


def validate_css(path: Path, errors: List[str], warnings: List[str]) -> bool:
    """Validate a theme CSS file contains all required tokens. Returns True when valid."""
    try:
        css = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{path}: cannot read ({exc})")
        return False

    ok = True
    missing = REQUIRED_CSS_TOKENS - set(re.findall(r"(--aetheris-[a-z-]+)\s*:", css))
    if missing:
        errors.append(f"{path}: missing tokens {sorted(missing)}")
        ok = False

    # Light mode override must exist and keep bg/surface/raised/fg coherent.
    if "[data-theme=\"light\"]" not in css:
        warnings.append(f"{path}: no [data-theme=\"light\"] block - light mode will fall back to dark tokens")

    if ok and path.name.endswith(".css"):
        # Accent-soft must be an rgba containing the accent RGB values.
        soft_match = re.search(
            r"--aetheris-accent-soft:\s*rgba\((\d+),\s*(\d+),\s*(\d+)",
            css,
        )
        accent_match = re.search(r"--aetheris-accent:\s*(\d+)\s+(\d+)\s+(\d+)", css)
        if soft_match and accent_match:
            soft_rgb = tuple(int(g) for g in soft_match.groups())
            accent_rgb = tuple(int(g) for g in accent_match.groups())
            if soft_rgb[:3] != accent_rgb[:3]:
                warnings.append(
                    f"{path}: --aetheris-accent-soft rgb {soft_rgb} does not match accent {accent_rgb}"
                )
        else:
            warnings.append(f"{path}: could not verify accent-soft matches accent")

    # Contrast check for fg vs bg in the dark block.
    fg = re.search(r"--aetheris-fg:\s*(\d+)\s+(\d+)\s+(\d+)", css)
    bg = re.search(r"--aetheris-bg:\s*(\d+)\s+(\d+)\s+(\d+)", css)
    if fg and bg:
        ratio = _contrast_ratio(
            tuple(int(v) for v in fg.groups()),
            tuple(int(v) for v in bg.groups()),
        )
        if ratio < 4.5:
            warnings.append(f"{path}: fg/bg contrast ratio {ratio:.1f}:1 is below 4.5:1")

    return ok


def main(argv: Optional[List[str]] = None) -> int:
    args = list(argv) if argv is not None else sys.argv[1:]
    if not args:
        print("usage: python tools/validate.py <theme.json> [theme.css]", file=sys.stderr)
        return 2

    errors: List[str] = []
    warnings: List[str] = []
    ok = True

    for arg in args:
        path = Path(arg)
        if path.suffix == ".json":
            ok = validate_json(path, errors, warnings) and ok
        elif path.suffix == ".css":
            ok = validate_css(path, errors, warnings) and ok
        else:
            print(f"unsupported file: {path}", file=sys.stderr)
            ok = False

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")

    if errors:
        print(f"theme invalid: {len(errors)} error(s)")
        return 1
    if warnings:
        print(f"theme valid with {len(warnings)} warning(s)")
    else:
        print("theme valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
