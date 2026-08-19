# Tailwind mapping

The platform maps CSS tokens to Tailwind utilities in `tailwind.config.ts`
so components use semantic names instead of raw values:

```ts
colors: {
  base: "rgb(var(--aetheris-bg) / <alpha-value>)",
  surface: "rgb(var(--aetheris-surface) / <alpha-value>)",
  raised: "rgb(var(--aetheris-raised) / <alpha-value>)",
  edge: "rgb(var(--aetheris-border) / <alpha-value>)",
  ink: "rgb(var(--aetheris-fg) / <alpha-value>)",
  muted: "rgb(var(--aetheris-muted) / <alpha-value>)",
  faint: "rgb(var(--aetheris-faint) / <alpha-value>)",
  accent: {
    DEFAULT: "rgb(var(--aetheris-accent) / <alpha-value>)",
    strong: "rgb(var(--aetheris-accent-strong) / <alpha-value>)",
    soft: "var(--aetheris-accent-soft)"
  },
  success: "rgb(var(--aetheris-success) / <alpha-value>)",
  danger: "rgb(var(--aetheris-danger) / <alpha-value>)",
  warning: "rgb(var(--aetheris-warning) / <alpha-value>)"
}
```

## Utility reference

| Utility | Token | Use |
| --- | --- | --- |
| `bg-base` | `--aetheris-bg` | Page background |
| `bg-surface` | `--aetheris-surface` | Card background |
| `bg-raised` | `--aetheris-raised` | Chips, hovers, inputs |
| `border-edge` | `--aetheris-border` | Borders and dividers |
| `text-ink` | `--aetheris-fg` | Primary text |
| `text-muted` | `--aetheris-muted` | Secondary text |
| `text-faint` | `--aetheris-faint` | Captions |
| `text-accent` | `--aetheris-accent` | Brand text and icons |
| `bg-accent` | `--aetheris-accent` | Primary buttons, active states |
| `bg-accent-soft` | `--aetheris-accent-soft` | Accent washes |
| `text-success` / `bg-success` | semantic | Online/paid states |
| `text-warning` / `bg-warning` | semantic | Pending states |
| `text-danger` / `bg-danger` | semantic | Failed states |

## Component classes

Design-system classes are built on the same tokens in `globals.css`:

- `.aetheris-btn-primary` - gradient from accent to accent-strong.
- `.aetheris-btn-secondary` - raised surface with edge border.
- `.aetheris-card` - surface background with a subtle top highlight.
- `.aetheris-frame` - gradient-border frame used around the demo.
- `.aetheris-kicker` - uppercase accent label.
- `.text-gradient` - text fading from fg into accent.

When building a theme, reuse these classes instead of inventing new color
utilities - it keeps every panel, page and the demo consistent.
