<p align="center">
  <img src="assets/icon.svg" alt="Aetheris Themes" width="88" style="filter: drop-shadow(0 0 20px rgba(139,92,246,0.55))">
</p>

<h1 align="center">Aetheris Themes</h1>

<p align="center">
  <strong>Design tokens, theme templates, ready-made palettes and a CSS-token validator for the entire Aetheris platform</strong>
</p>

<p align="center">
  <a href="https://aetheris-docs.vercel.app/wiki/theming"><img src="https://img.shields.io/badge/Docs-Theming-0EA5E9?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Docs"></a>
  <a href="https://aetheris-docs.vercel.app/wiki/theming-tokens"><img src="https://img.shields.io/badge/Reference-Tokens-8B5CF6?style=for-the-badge&logo=css3&logoColor=white" alt="Tokens"></a>
  <a href="https://discord.gg/6GcfebuT2A"><img src="https://img.shields.io/badge/Discord-Help-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Token--Driven-CSS%20Vars-06B6D4?style=flat-square" alt="Tokens">
  <img src="https://img.shields.io/badge/Dark%2FLight%2FSystem-All%20Supported-10B981?style=flat-square" alt="Themes">
  <img src="https://img.shields.io/badge/Runtime-Whitelabel-F59E0B?style=flat-square" alt="Runtime">
  <img src="https://img.shields.io/badge/WCAG-Contrast%20Hints-EC4899?style=flat-square" alt="WCAG">
  <img src="https://img.shields.io/badge/Tests-Passing-10B981?style=flat-square" alt="Tests">
</p>

---

<br>

> **Everything in Aetheris — marketing site, control panel, wiki, demo panels
> and even the terminal UI — reads from the same small set of CSS custom
> properties.** Swap one JSON document at runtime (the *whitelabel payload*)
> and the ENTIRE platform restyles itself with **zero code changes**. This
> repository is the reference: token definitions, ready-made palettes,
> fill-in templates, a contrast-aware validator and the full authoring guide.

<br>

## ✨ What's Inside

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <h3>📚 Full guide</h3>
      <p>Five Markdown chapters in <code>docs/</code> covering token model → runtime application → Tailwind mapping → publishing.</p>
    </td>
    <td width="33%" align="center" valign="top">
      <h3>📝 Templates</h3>
      <p><code>theme.template.css</code> — every required token commented.<br><code>theme.template.json</code> — full whitelabel manifest.</p>
    </td>
    <td width="33%" align="center" valign="top">
      <h3>🎨 5 pre-built</h3>
      <p>
        💚 Emerald (default)<br>
        💙 Indigo · 🧡 Amber<br>
        🌌 Aurora (custom violet + full rebrand example)
      </p>
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <h3>✅ Validator</h3>
      <p>Checks JSON schema + CSS token set + WCAG contrast hints. Zero stdlib-only Python, no Node needed.</p>
    </td>
    <td align="center" valign="top">
      <h3>⚡ Runtime selectable</h3>
      <p>Accent switcher uses <code>data-accent</code>. Light/dark mode uses <code>data-theme</code>. Both toggle instantly.</p>
    </td>
    <td align="center" valign="top">
      <h3>🧱 Tailwind mapped</h3>
      <p>Every token aliased to <code>bg-surface / border-edge / text-accent / rounded-2xl</code> utilities. Pure utility, no classes to learn.</p>
    </td>
  </tr>
</table>

<br>

## 🚀 Quick Start

```bash
# 1. Validate the bundled palettes — all should PASS
python tools/validate.py \
  themes/*.json themes/*.css templates/theme.template.css

# 2. Copy the starter templates into a new theme
cp templates/theme.template.json themes/my-brand.json
cp templates/theme.template.css  themes/my-brand.css

# 3. Edit tokens in my-brand.css + brand metadata in my-brand.json
#    (see docs/tokens.md for every variable's role)

# 4. Validate the result — schema + tokens + contrast hints
python tools/validate.py themes/my-brand.json themes/my-brand.css

# 5. Register the accent at runtime → data-accent="my-brand" in <html>
#    or publish via the Admin → Whitelabel UI in the control panel.
```

<br>

## 🎨 Token Model

| Group | Tokens | Purpose |
|---|---|---|
| **Surfaces** | `--aetheris-bg` · `--aetheris-surface` · `--aetheris-raised` | Page canvas · cards · elevated chips |
| **Lines** | `--aetheris-border` · `--aetheris-border-strong` | Dividers · inputs · focused states |
| **Text** | `--aetheris-fg` · `--aetheris-muted` · `--aetheris-faint` | Primary · secondary · captions / disabled |
| **Semantic** | `--aetheris-success` · `--aetheris-warning` · `--aetheris-danger` | States + badges |
| **Accent** | `--aetheris-accent` · `--aetheris-accent-strong` · `--aetheris-accent-soft` | Brand color, gradient endpoints |
| **Shape** | `--aetheris-radius` · `--aetheris-radius-sm` | Card / input radii — `0` = square UI |

Full authoritative reference: [docs/tokens.md](docs/tokens.md).

<br>

## 🌌 Aurora Showcase

`aurora` is a complete rebrand example (not just an accent) demonstrating
**every layer of the theming model**:

```css
/* themes/aurora.css — key highlights */
:root[data-accent="aurora"] {
  --aetheris-accent:        #a78bfa;  /* violet base */
  --aetheris-accent-strong: #7c3aed;
  --aetheris-accent-soft:   #c4b5fd33;
  --aetheris-radius:        18px;     /* rounded UI */
  --aetheris-bg:            #0b0720;  /* deep nebula background */
}
```

Load it via `data-accent="aurora"` on the `<html>` element, or drop the
matching `aurora.json` into the control-panel **Whitelabel** editor.

<br>

## 🧩 Repository Layout

```text
aetheris-themes/
├── docs/
│   ├── index.md           # Guide landing · overview + quick tour
│   ├── tokens.md          # Full CSS token reference (the bible)
│   ├── theming.md         # How tokens are applied at runtime (data-accent, data-theme)
│   ├── tailwind.md        # Design-token → Tailwind utility mapping
│   └── publishing.md      # Whitelabel JSON schema + API endpoint for publishing
├── templates/
│   ├── theme.template.css # Fill-in starter with every token + comments
│   └── theme.template.json# Whitelabel manifest: fonts, logo, copy, accent IDs
├── themes/
│   ├── emerald.json       # 💚 Platform default accent
│   ├── indigo.json        # 💙 Deep-blue accent
│   ├── amber.json         # 🧡 Warm amber accent
│   ├── aurora.json        # 🌌 Full rebrand example (violet)
│   └── aurora.css         # Aurora token block + light/dark overrides
├── tools/
│   ├── validate.py        # Stdlib validator: schema ✓ token coverage ✓ WCAG contrast hints ✓
│   └── generate_themes.py # Regenerates the standard three accent JSONs
└── tests/                 # Validator unit tests
```

<br>

## 🧪 Tests

```bash
python -m pip install pytest
python -m pytest -q
```

---

<p align="center">
  <strong>Made with 💚 by <a href="https://github.com/Leo-Galli">Leonardo Galli</a></strong>
</p>

<p align="center">
  <a href="https://github.com/aetheris-project/aetheris-app">App</a>
  ·
  <a href="https://github.com/aetheris-project/aetheris-docs">Docs</a>
  ·
  <a href="https://github.com/aetheris-project/aetheris-website">Website</a>
  ·
  <a href="https://discord.gg/6GcfebuT2A">Discord</a>
  ·
  <a href="https://paypal.me/LeonardoGalliITA">Donate</a>
</p>

## 📄 License

Licensed under **GNU Affero General Public License v3.0 (AGPL-3.0)**.
See [LICENSE.md](LICENSE.md). You may use, study, modify and redistribute
for any purpose provided distributed or network-served modified versions
keep this license, preserve Leonardo Galli's copyright notice and release
source under AGPL-3.0. The Aetheris core and author credit may not be removed.
