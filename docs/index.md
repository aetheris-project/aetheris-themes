# Aetheris theming guide

The Aetheris platform is token-driven: every color, radius and font used by
the website, the demo panels, the docs and the control plane flows from a
small set of CSS variables and a runtime whitelabel configuration. This
repository is the complete reference for creating, validating and shipping
your own theme.

## What a theme is

A theme in Aetheris is two coordinated files:

1. **A CSS variable set** (tokens) - see `templates/theme.template.css`.
   It defines the neutral palette, the semantic colors and the accent
   system for both dark and light mode.
2. **A whitelabel JSON document** - see `templates/theme.template.json`.
   It carries the brand name, tagline, logo, domain, accent selection,
   navigation and module toggles, and is served at runtime by the Admin
   Panel through `GET /api/whitelabel`.

The CSS tokens give the platform its look. The JSON gives it its identity.
Both are validated by `tools/validate.py`.

## The token model

| Group | Variables |
| --- | --- |
| Surfaces | `--aetheris-bg`, `--aetheris-surface`, `--aetheris-raised` |
| Lines | `--aetheris-border` |
| Text | `--aetheris-fg`, `--aetheris-muted`, `--aetheris-faint` |
| Semantic | `--aetheris-success`, `--aetheris-warning`, `--aetheris-danger` |
| Accent | `--aetheris-accent`, `--aetheris-accent-strong`, `--aetheris-accent-soft` |
| Shape | `--aetheris-radius` |

The accent is selectable at runtime (emerald / indigo / amber by default)
through the `data-accent` attribute; light and dark mode are switched with
`data-theme="light"`. See [tokens.md](tokens.md) for the full reference.

## Guide contents

- [Token reference](tokens.md) - every CSS variable, its role and defaults.
- [How themes are applied](theming.md) - `data-accent`, `data-theme`, the
  whitelabel provider and the anti-flash bootstrap.
- [Tailwind mapping](tailwind.md) - how tokens map to Tailwind utilities.
- [Publishing](publishing.md) - the whitelabel JSON schema and how to
  serve a theme at runtime.

## Quick start

```bash
# 1. Copy the template CSS and fill in your palette
cp templates/theme.template.css themes/my-theme.css

# 2. Copy the template JSON and set your brand + accent
cp templates/theme.template.json themes/my-theme.json

# 3. Validate both files
python tools/validate.py themes/my-theme.json themes/my-theme.css
```

Use the ready-made themes in `themes/` as starting points: `emerald.json`,
`indigo.json`, `amber.json` and the custom `aurora.json` example.

## Standards

- English only, no emojis.
- Keep `--aetheris-accent-soft` translucent (an rgba of the accent) - it is
  used as a wash behind accent text and icons.
- Validate before committing: the validator checks every token is present,
  colors are valid, contrast hints are sane and the JSON matches the
  whitelabel schema.
