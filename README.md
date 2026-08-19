<p align="center">
  <img src="assets/icon.svg" alt="Aetheris Themes" width="88">
</p>

<h1 align="center">Aetheris Themes</h1>

<p align="center">
  <strong>Theme guide, templates and validator for the Aetheris platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/token--driven-CSS%20variables-06B6D4" alt="Token-driven">
  <img src="https://img.shields.io/badge/dark%2Flight%2Fsystem-supported-success" alt="Theme modes">
  <img src="https://img.shields.io/badge/tests-passing-success" alt="Tests passing">
</p>

---

The complete reference for creating, validating and shipping themes for the
Aetheris platform. Everything the platform renders - marketing site, demo
panels, docs and control plane - is driven by a small set of CSS tokens and
a runtime whitelabel document, so a new theme restyles the entire platform
with no code changes.

## What you get

- **Guide** (`docs/`) - the token system, how themes are applied, the
  Tailwind mapping and how to publish a theme at runtime.
- **Templates** (`templates/`) - a fill-in theme CSS with every required
  token and a complete whitelabel JSON document.
- **Ready-made themes** (`themes/`) - `emerald`, `indigo` and `amber`
  matching the platform defaults, plus `aurora`, a custom example with a
  violet accent and rebranded identity.
- **Validator** (`tools/validate.py`) - checks the JSON against the
  whitelabel schema and the CSS against the required token set, with
  contrast hints.

## Quick start

```bash
# Validate the shipped themes (all must pass)
python tools/validate.py themes/*.json templates/theme.template.css

# Create your own theme from the templates
cp templates/theme.template.json themes/my-theme.json
cp templates/theme.template.css themes/my-theme.css
# edit both, then:
python tools/validate.py themes/my-theme.json themes/my-theme.css
```

## The token model

| Group | Tokens | Role |
| --- | --- | --- |
| Surfaces | `--aetheris-bg`, `--aetheris-surface`, `--aetheris-raised` | Page, cards, raised |
| Lines | `--aetheris-border` | Borders and dividers |
| Text | `--aetheris-fg`, `--aetheris-muted`, `--aetheris-faint` | Primary / secondary / captions |
| Semantic | `--aetheris-success`, `--aetheris-warning`, `--aetheris-danger` | States |
| Accent | `--aetheris-accent`, `--aetheris-accent-strong`, `--aetheris-accent-soft` | Brand |
| Shape | `--aetheris-radius` | Corner radius |

Accent is selectable at runtime via `data-accent` (emerald / indigo /
amber, or a custom registered accent); light and dark mode switch with
`data-theme`. Full reference: [docs/tokens.md](docs/tokens.md).

## Repository layout

```text
aetheris-themes/
├── docs/
│   ├── index.md              # Guide landing
│   ├── tokens.md             # CSS token reference
│   ├── theming.md            # How themes are applied at runtime
│   ├── tailwind.md           # Token to Tailwind utility mapping
│   └── publishing.md         # Whitelabel JSON schema + serving
├── templates/
│   ├── theme.template.css    # Required tokens, accents, light mode
│   └── theme.template.json   # Full whitelabel schema
├── themes/
│   ├── emerald.json          # Platform default accent
│   ├── indigo.json
│   ├── amber.json
│   └── aurora.json           # Custom accent + rebranded identity
├── tools/
│   ├── validate.py           # Schema + token validator (stdlib)
│   └── generate_themes.py    # Regenerates the standard themes
└── tests/                    # Validator unit tests
```

## Tests

```bash
python -m pip install pytest
python -m pytest -q
```

## License

Proprietary enterprise software. See the license agreement distributed with
the organization account.
