"""Prüft alle Ansichten der Seite: JS-Fehler, seitliches Scrollen, kaputte Bilder, Screenshots.

Aufruf (im Projektordner):  python3 tools/check.py
Einmalig vorher:            pip install playwright && playwright install chromium
Ergebnis: Konsolenbericht + Screenshots in tools/shots/
"""
import os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "file://" + os.path.join(ROOT, "index.html")
ROUTES = ["home", "ueber-mich", "labor", "stress", "ihht", "hyperthermie", "rifetech",
          "medkey", "infusion", "darm", "ohr", "preise"]
WIDTHS = [1280, 390]
OUT = os.path.join(ROOT, "tools", "shots")
os.makedirs(OUT, exist_ok=True)
problems = 0

with sync_playwright() as p:
    b = p.chromium.launch()
    for w in WIDTHS:
        for r in ROUTES:
            pg = b.new_page(viewport={"width": w, "height": 900})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(f"{URL}#{r}")
            pg.reload()
            pg.wait_for_timeout(700)
            overflow = pg.evaluate("document.documentElement.scrollWidth > innerWidth + 1")
            broken = pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.getAttribute('src'))")
            active = pg.evaluate("document.querySelector('.view.active')?.id")
            pg.screenshot(path=os.path.join(OUT, f"{r}-{w}.png"), full_page=True)
            flag = errs or overflow or broken or active != "v-" + r
            problems += bool(flag)
            print(("FEHLER " if flag else "ok     ") + f"{r:13} {w}px", errs or "", "seitlich scrollbar" if overflow else "", broken or "", "" if active == "v-" + r else f"zeigt {active}")
            pg.close()
    b.close()
print("\nAlles in Ordnung." if not problems else f"\n{problems} Ansicht(en) mit Problemen.")
sys.exit(1 if problems else 0)
