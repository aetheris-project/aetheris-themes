# How themes are applied

## The runtime chain

1. `WhitelabelProvider` (in `aetheris-website/lib/theme`) loads the
   whitelabel JSON - either the static default or the remote
   `NEXT_PUBLIC_WHITELABEL_URL` endpoint served by the control panel.
2. It writes `data-accent` on `document.documentElement`, which activates
   the matching `[data-accent="..."]` CSS block.
3. A theme toggle writes `data-theme="light"` or `"dark"` (or removes it
   for system), persisted in `localStorage`.
4. An inline anti-flash script in `<head>` applies the persisted theme
   before first paint, so there is no flash of the wrong theme and no
   layout shift.

## Accent selection

The accent is part of the whitelabel config (`theme.accent`) but can be
changed live from the interactive demo. Because the demo and the site share
the same `WhitelabelProvider`, switching the accent in the demo repaints the
whole page - that is the exact mechanism a branded customer sees.

## Dark / light / system

| `data-theme` | Behavior |
| --- | --- |
| (unset) | Follows `prefers-color-scheme` |
| `dark` | Forces dark tokens |
| `light` | Forces light tokens |

The toggle cycles system -> light -> dark and persists the choice.

## Where tokens are consumed

- `app/globals.css` - token declarations and component classes
  (`.aetheris-btn-primary`, `.aetheris-card`, `.aetheris-frame`).
- `tailwind.config.ts` - maps tokens to utilities:
  `bg-surface`, `border-edge`, `text-muted`, `text-accent`, etc.
- Demo panels - all use the token utilities, so a new theme restyles the
  demo with zero changes.

## Zero layout shift

Token changes never alter layout: surfaces, borders and text colors swap
in place. The platform reserves fixed heights for demo panels, skeleton
placeholders match final dimensions, and toasts are mounted in reserved
space. When designing a theme, keep all size tokens (`--aetheris-radius`)
and font stacks constant unless you intend a global restyle.
