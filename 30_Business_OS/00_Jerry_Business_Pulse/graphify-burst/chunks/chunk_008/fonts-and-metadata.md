---
title: Fonts + Metadata
---

## Fonts (3, via next/font/google)

Configured in `src/app/layout.tsx`, exposed as CSS variables on `<html>`:

| Variable | Font | Use |
|----------|------|-----|
| `--font-display` | `Instrument_Serif` (400, normal+italic) | Editorial display |
| `--font-mono` | `JetBrains_Mono` (300, 400, 500) | Code, technical accents |
| `--font-sans` | `Geist` (300, 400, 500, 600) | Body, UI |

All use `display: "swap"` (no FOIT, only FOUT).

## Pattern (in layout.tsx)

```ts
import { Instrument_Serif, JetBrains_Mono, Geist } from "next/font/google";

const instrumentSerif = Instrument_Serif({
  weight: "400",
  subsets: ["latin"],
  style: ["normal", "italic"],
  variable: "--font-display",
  display: "swap",
});
// ... same for jetbrainsMono + geist

return (
  <html
    lang="en"
    className={`${instrumentSerif.variable} ${jetbrainsMono.variable} ${geist.variable}`}
    data-archetype="aaa"
    data-density="comfortable"
  >
    <body>{children}</body>
  </html>
);
```

## Don't

- ❌ Add a 4th font without a clear use case — perf budget
- ❌ Use `<link>` to Google Fonts CDN — defeats `next/font` optimization
- ❌ Set `display: "block"` — causes invisible text during swap

## Metadata (always complete)

```ts
export const metadata: Metadata = {
  title: "…",
  description: "…",
  keywords: ["…", "…"],
  openGraph: { title, description, type, locale },
  twitter: { card, title, description },
  robots: { index: true, follow: true },
};
```

Every public page MUST export a full `metadata` object. No half-baked
titles. See `src/app/layout.tsx` for the canonical example.

## Why

- SEO + social share cards need all 4 blocks (basic + OG + Twitter + robots)
- `data-archetype` / `data-density` on `<html>` are CSS theming hooks
  for the page's reactive state (see `src/app/page.tsx` `useEffect`)
