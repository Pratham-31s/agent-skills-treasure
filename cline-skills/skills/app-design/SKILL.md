---
name: app-design
description: Picks a color theme, type, and layout rules that fit the project's domain so the UI looks human-designed, not AI-generated. Use whenever building or styling any UI, website, landing page, dashboard, or app screen, choosing colors or themes, or when asked to "make it look better". Brand colors given by the user always override this.
---
# App Design

## 1. Pick the theme
Identify the domain (from the request, README, package.json). Take the closest row; if none fits, use **Fallback**.

| Domain | Primary | Accent | Bg | Text | Type (heading / body) |
|---|---|---|---|---|---|
| Fintech, banking, insurance | #0B3A5B | #12A594 | #F6F8FA | #0F1B2A | Source Serif 4 / Source Sans 3 |
| Healthcare, wellness | #0E7490 | #E8836B | #F3FAFA | #12303A | Nunito Sans / Nunito Sans |
| Education, e-learning | #2E5AAC | #F2B33D | #FBFAF6 | #1E2433 | DM Sans / DM Sans |
| E-commerce, retail | #1F2933 | #E4572E | #FFFFFF | #1F2933 | Archivo / Inter |
| Food, restaurant, cafe | #A63D1F | #5F7A3A | #FBF3E6 | #2A1C14 | Fraunces / DM Sans |
| Travel, hospitality | #0D5C7C | #EE9B4D | #FAF6EE | #14303B | Fraunces / Source Sans 3 |
| SaaS, productivity, dev tools | #2A5BD7 | #F0A202 | #FAFAF9 | #18181B | IBM Plex Sans / IBM Plex Sans |
| Data, analytics, AI (dark) | #38D39F | #F5A524 | #0E1116 | #E6EDF3 | IBM Plex Sans / IBM Plex Mono for numbers |
| Gaming, entertainment, music (dark) | #FF4D6D | #C8F135 | #0D0F14 | #ECEEF2 | Barlow Condensed / Barlow |
| Fitness, sports (dark) | #FF6A1A | #D4F53C | #111214 | #F2F2F2 | Barlow Condensed / Barlow |
| Portfolio, creative, agency | #141414 | #FF5A2C | #F4EFE6 | #141414 | Fraunces / DM Sans |
| Sustainability, agriculture, outdoors | #2E5B3C | #C79A2B | #F3F1E6 | #1B2A1F | Source Serif 4 / Source Sans 3 |
| Corporate, legal, real estate, consulting | #1B2A41 | #A98455 | #F6F4F0 | #1A1F29 | Source Serif 4 / Source Sans 3 |
| Social, community, messaging | #3673D9 | #FF7A66 | #FFFFFF | #1C2330 | DM Sans / DM Sans |
| ERP, logistics, admin, internal tools | #1F4E79 | #E8A317 | #F2F4F7 | #1B2430 | IBM Plex Sans / IBM Plex Sans |
| Beauty, fashion, luxury | #1C1917 | #B47B7B | #FAF6F3 | #1C1917 | Fraunces / DM Sans |
| Nonprofit, government, civic | #1A4F8B | #E0A100 | #FFFFFF | #1B2430 | Source Sans 3 / Source Sans 3 |
| **Fallback (anything else)** | #2563EB | #F59E0B | #FFFFFF | #0F172A | system-ui stack / system-ui stack |

Also define: muted text `#64748B`, border `#E2E8F0` (light) or a 1-step lighter tint of bg (dark), surface = bg ±1 step. Status: success `#16A34A`, warning `#D97706`, error `#DC2626`.
Button text: white on Primary (light themes), `#0E1116` on Primary (dark themes), `#111` on Accent (white on Food's Accent).

## 2. Apply it
- Define tokens once (CSS variables, or the project's Tailwind/MUI/etc. theme). Never hard-code hex in components.
- 60/30/10: 60% bg/neutral, 30% surface/primary, 10% accent. Accent marks one main action per view.
- Contrast: body text ≥4.5:1, UI edges/icons ≥3:1. Check any color you change.
- Fonts: max 2 families, 16px body, 1.25 scale, line-height 1.5 body / 1.2 headings. Load only the weights used.
- 4/8px spacing grid. Pick ONE corner radius (4, 8, or 12px) and reuse it.
- Dark theme only if the table row says so or the user asks; otherwise offer via tokens.

## 3. Avoid the "AI look"
- No purple/blue/pink gradients, blob or glow backgrounds, neon shadows (gaming excepted).
- No glassmorphism/blur cards everywhere. Use borders, dividers, and whitespace instead of shadowed rounded cards on everything.
- No emoji as icons. One icon set (Lucide or Phosphor), one stroke weight.
- Skip the template: centered hero + gradient CTA + three identical icon cards. Left-align text, vary section layouts, let content decide structure.
- Write real, domain-specific copy. Ban "Unlock", "Seamless", "Elevate", "Revolutionize", lorem ipsum.
- Use realistic sample data: uneven numbers, varied real-sounding names. No "John Doe", 100/200/300, round totals.
- Motion: 150–200ms ease-out for state changes only. No bounce, parallax, or scroll-jacking.
- Shadows: max 2 levels, low opacity, same direction. No gradient buttons.
- Design empty, loading, and error states.

## Output
Theme tokens file in the project's stack + a 2-line note: domain matched (or "fallback") and why.
