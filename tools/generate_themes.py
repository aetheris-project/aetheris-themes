"""
Standard theme generator.

Derives the emerald, indigo and amber whitelabel JSON documents from the
template, only changing the accent and the brand identity. Keeps the
standard themes in sync with the template schema by construction.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "templates" / "theme.template.json"
OUT_DIR = ROOT / "themes"

STANDARD = {
    "emerald": {
        "name": "Aetheris",
        "tagline": "Billing and virtualization control plane for the enterprise",
        "domain": "aetheris.enterprise",
        "email": "ops@aetheris.enterprise",
        "support": "https://support.aetheris.enterprise",
        "twitter": "https://x.com/aetheris",
        "accent": "emerald",
    },
    "indigo": {
        "name": "Aetheris",
        "tagline": "Billing and virtualization control plane for the enterprise",
        "domain": "aetheris.enterprise",
        "email": "ops@aetheris.enterprise",
        "support": "https://support.aetheris.enterprise",
        "twitter": "https://x.com/aetheris",
        "accent": "indigo",
    },
    "amber": {
        "name": "Aetheris",
        "tagline": "Billing and virtualization control plane for the enterprise",
        "domain": "aetheris.enterprise",
        "email": "ops@aetheris.enterprise",
        "support": "https://support.aetheris.enterprise",
        "twitter": "https://x.com/aetheris",
        "accent": "amber",
    },
}


def main() -> None:
    template = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(exist_ok=True)
    for slug, identity in STANDARD.items():
        theme = json.loads(json.dumps(template))
        theme["theme"]["accent"] = identity["accent"]
        theme["brand"]["name"] = identity["name"]
        theme["brand"]["tagline"] = identity["tagline"]
        theme["brand"]["domain"] = identity["domain"]
        theme["contact"]["email"] = identity["email"]
        theme["contact"]["supportUrl"] = identity["support"]
        theme["contact"]["twitterUrl"] = identity["twitter"]
        target = OUT_DIR / f"{slug}.json"
        target.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
