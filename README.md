# pombers.com

The Pombers website: home, Privacy Policy, Terms of Use, Support, and `app-ads.txt` for AdMob.
Static files served by GitHub Pages from `main` (custom domain in `CNAME`).

Design: Figma "Site" (file `biXcGBHwDKVTsxxL7rRehY`, node `2829:1745`). Type: DynaPuff
SemiCondensed (SIL Open Font License, `fonts/OFL.txt`) — the app's typeface — for the title,
headings and footer; the legal pages' body text uses the system font. The footer's year is set by
`site.js`, so it's always the current one.

| Path | What |
|---|---|
| `/` | Home: the pomber, App Store badge |
| `/privacy/` | Privacy Policy (App Store Connect privacy policy URL) |
| `/terms/` | Terms of Use |
| `/support/` | Support (App Store Connect support URL) |
| `/add?tag=4412` | Invite links: the friend's tag and the App Store (`add.html`) |
| `/streak/?n=7` | Brag links: a friend's victory streak, its tier badge (2–3 Cadet · 4–5 Tapper · 6–9 Beast · 10+ Legend) and the App Store. Link preview: `img/share.png` (Figma `message` 2926:27006) |
| `/streak/7/` | The same with the number built in, for 2–99, so link previews show it: `og:image` is `img/streak/<n>.png` (Figma `message` 2952:16642). Pages written by `tools/streak-pages.py`; images rendered by the app repo's `scripts/streak-previews.ts`. The app's Brag!! links here. |
| `/app-ads.txt` | AdMob publisher declaration |

Tier badges (`img/badge-*.svg`) are the app's `BADGES` art (Figma `badge` Level 1–4) in each tier's colour.
