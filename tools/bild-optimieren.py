"""Bild für die Seite aufbereiten: python3 tools/bild-optimieren.py eingabe.jpg img/ausgabe.jpg [breite]
Standard 1600 px Breite für Hero-Bilder, 900 für Kacheln. JPEG ca. 82 %. Benötigt: pip install pillow"""
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
im = Image.open(src).convert("RGB")
im.thumbnail((w, w))
im.save(dst, quality=82, optimize=True)
print(dst, im.size)
