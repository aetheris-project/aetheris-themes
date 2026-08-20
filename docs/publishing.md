# Publishing a theme

A theme is published by serving its whitelabel JSON from the control panel.
The Admin Panel stores the configuration in PostgreSQL (cached in Redis)
and exposes it at `GET /api/whitelabel`. The marketing site and client
portal fetch it when `NEXT_PUBLIC_WHITELABEL_URL` points at that endpoint,
and merge it over the static defaults at runtime - no rebuild.

## Schema

```json
{
  "brand": {
    "name": "string (required)",
    "tagline": "string (required)",
    "logoUrl": "string (required)",
    "logoDarkUrl": "string (required)",
    "domain": "string (required)"
  },
  "theme": {
    "accent": "emerald | indigo | amber (or a custom registered accent)",
    "radius": "integer 0-32",
    "fontFamily": "string, empty for the default stack"
  },
  "navigation": [
    { "label": "string", "href": "string", "cta": "boolean" }
  ],
  "contact": {
    "email": "string",
    "supportUrl": "string",
    "twitterUrl": "string"
  },
  "seo": {
    "defaultTitle": "string",
    "defaultDescription": "string",
    "ogImage": "string",
    "keywords": ["string"]
  },
  "modules": {
    "billing": "boolean",
    "vncConsole": "boolean",
    "pterodactyl": "boolean",
    "proxmox": "boolean",
    "virtfusion": "boolean",
    "registrars": "boolean"
  },
  "integrations": {
    "stripe": "boolean",
    "paypal": "boolean",
    "mollie": "boolean",
    "namecheap": "boolean",
    "cloudflare": "boolean",
    "cpanel": "boolean",
    "directadmin": "boolean"
  }
}
```

## Serving the config

- Development: set `NEXT_PUBLIC_WHITELABEL_URL` on the website to the
  control panel's `https://app.example.com/api/whitelabel`.
- Production: the Admin Panel persists the config and serves it from the
  same endpoint, cached in Redis with a short TTL.

## Validation

Always run the validator before shipping:

```bash
python tools/validate.py themes/my-theme.json themes/my-theme.css
```

The validator checks:

- The JSON parses and matches the whitelabel schema (types, required keys,
  allowed accent values, module booleans).
- The CSS contains every required token and valid color values.
- Accent soft matches the accent color, and contrast warnings are raised
  when a foreground/background pair looks risky.

## Adding a new accent

1. Add the `[data-accent="name"]` block to the theme CSS with the three
   accent tokens.
2. Register the accent name in the whitelabel schema's `AccentName` union
   and in the validator's allowed set.
3. Set `theme.accent` to the new name in the JSON.
