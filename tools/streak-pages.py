#!/usr/bin/env python3
"""Writes the Brag!! pages streak/<n>/index.html for n = 2..99.

Each page is the streak page with its number built in, so link previews (iMessage, WhatsApp, X...)
show that streak: og:image is img/streak/<n>.png, rendered by the app repo's
scripts/streak-previews.ts (Figma Marketing -> message). Tiers as in the app:
2-3 Cadet, 4-5 Tapper, 6-9 Beast, 10+ Legend. Run from the site root: python3 tools/streak-pages.py
"""
import html
import os

MIN, MAX = 2, 99


def tier(n):
    return 'legend' if n >= 10 else 'beast' if n >= 6 else 'tapper' if n >= 4 else 'cadet'


PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{n} on a roll! Can you beat it? · Pombers</title>
  <meta name="description" content="{n} Pombers wins in a row. Win more in a row to beat it.">
  <meta name="apple-itunes-app" content="app-id=6814720085">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Pombers">
  <meta property="og:url" content="https://pombers.com/streak/{n}/">
  <meta property="og:title" content="{n} Wins. Can you beat it?">
  <meta property="og:description" content="Win more Pombers matches in a row.">
  <meta property="og:image" content="https://pombers.com/img/streak/{n}.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{n} Wins">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="robots" content="noindex">
  <link rel="canonical" href="https://pombers.com/streak/{n}/">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
  <link rel="preload" href="/fonts/dynapuff-semicondensed-semibold.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/style.css">
  <script src="/site.js" defer></script>
</head>
<body>
  <!-- Written by tools/streak-pages.py: a Brag!! link from the app (pombers.com/streak/{n}/). -->
  <div class="page home streak">
    <header class="nav">
      <a href="/" aria-label="Pombers — home">Pombers</a>
    </header>
    <main class="brag">
      <div class="claim">
        <img src="/img/badge-{tier}.svg" width="200" height="117" alt="{name} badge">
        <h1>{n} on a roll!</h1>
        <p>Can you beat it?</p>
      </div>
      <div class="art">
        <img src="/img/pomber.svg" width="912" height="717" alt="A pomber peeking out of its hole">
      </div>
    </main>
    <a class="store" href="https://apps.apple.com/app/id6814720085">
      <img src="/img/app-store.svg" width="140" height="47" alt="Download on the App Store">
    </a>
    <footer class="footer">
      <a href="/terms/">Terms of Use</a>
      <span>©<span data-year>2026</span> Cabral Inc</span>
      <a href="/privacy/">Privacy Policy</a>
    </footer>
  </div>
</body>
</html>
"""

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
for n in range(MIN, MAX + 1):
    t = tier(n)
    d = os.path.join(root, 'streak', str(n))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w') as f:
        f.write(PAGE.format(n=n, tier=t, name=html.escape(t.capitalize())))
print(f'wrote streak/{MIN}..{MAX}')
