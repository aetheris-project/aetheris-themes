# Token reference

Every visual decision in the Aetheris platform flows from a small set of
CSS variables declared on `:root`. Tokens are RGB triplets (space-separated)
so they can be composed with Tailwind's alpha syntax; `--aetheris-accent-soft`
is an rgba color used as a translucent wash.

## Neutral surfaces

| Token | Default (dark) | Role |
| --- | --- | --- |
| `--aetheris-bg` | `9 9 11` | Page background |
| `--aetheris-surface` | `20 20 24` | Card background |
| `--aetheris-raised` | `26 26 31` | Raised/hover background, chips |
| `--aetheris-border` | `39 39 42` | Hairline borders and dividers |

## Text

| Token | Default (dark) | Role |
| --- | --- | --- |
| `--aetheris-fg` | `250 250 250` | Primary text |
| `--aetheris-muted` | `161 161 170` | Secondary text |
| `--aetheris-faint` | `113 113 122` | Tertiary text, captions |

## Semantic colors

| Token | Default | Role |
| --- | --- | --- |
| `--aetheris-success` | `16 185 129` | Online, paid, healthy states |
| `--aetheris-warning` | `245 158 11` | Pending, draining states |
| `--aetheris-danger` | `239 68 68` | Offline, overdue, failed states |

## Accent system

| Token | Role |
| --- | --- |
| `--aetheris-accent` | Primary brand accent (buttons, links, active states) |
| `--aetheris-accent-strong` | Darker accent for gradients and hover |
| `--aetheris-accent-soft` | Translucent accent wash behind icons and pills |

The accent is selectable at runtime. Each value sets a `data-accent`
attribute on `<html>`, and a matching CSS block overrides the three accent
tokens:

```css
[data-accent="indigo"] {
  --aetheris-accent: 99 102 241;
  --aetheris-accent-strong: 79 70 229;
  --aetheris-accent-soft: rgba(99, 102, 241, 0.12);
}
```

Adding a new accent means: declare the `[data-accent="..."]` block in the
theme CSS and register the accent name in the whitelabel schema type.

## Shape

| Token | Default | Role |
| --- | --- | --- |
| `--aetheris-radius` | `10px` | Card and button radius scale |

## Light mode

Light mode is a `[data-theme="light"]` override on the same tokens, plus
two composability tweaks (translucent card gradients and a lighter accent
soft):

```css
[data-theme="light"] {
  --aetheris-bg: 250 250 250;
  --aetheris-surface: 255 255 255;
  --aetheris-raised: 244 244 245;
  --aetheris-border: 228 228 231;
  --aetheris-fg: 24 24 27;
  --aetheris-muted: 82 82 91;
  --aetheris-faint: 113 113 122;
  --aetheris-accent-soft: rgba(16, 185, 129, 0.1);
}
```

## Rules

- Keep every token present - the validator fails on missing variables.
- `--aetheris-accent-soft` must be an rgba whose color matches the accent.
- Neutral surfaces must stay within roughly 5-8 steps of each other to
  preserve hierarchy.
- Text tokens must have sufficient contrast on `--aetheris-bg` and
  `--aetheris-surface` (the validator warns when contrast looks risky).
