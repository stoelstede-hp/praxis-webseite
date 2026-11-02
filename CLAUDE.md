# CLAUDE.md – Webseite Heilpraxis Toelstede

Du arbeitest hier mit **Dr. rer. nat. Simone Toelstede**, Heilpraktikerin in München (Untere Weidenstraße 13, 81543 München). Dies ist ihre neue Webseite; Elias Paurnfeindt Eyss hat sie gebaut und übergeben. Simone ist keine Programmiererin: erkläre kurz und in einfachem Deutsch, was du geändert hast, nicht wie. Duze sie, sie duzt dich. Mach Dinge selbst, statt ihr Terminal-Befehle zum Abtippen zu geben.

## Stand bei Übergabe (02.11.2026)
- Die Seite ist **gebaut und lokal lauffähig**, aber **noch nicht live**. Die alte Seite heilpraxis-toelstede.de läuft unverändert weiter.
- **GitHub und Netlify sind noch nicht eingerichtet.** Das ist deine erste größere Aufgabe mit Simone: Führe sie durch `UEBERGABE.md`, Teil 2 (GitHub-Konto, privates Repo `heilpraxis-toelstede-website`, Netlify-Anbindung, später Domain). Mach selbst, was du kannst (`git init`, Remote, Push, Prüfungen). **Passwörter, Zugangscodes und Zwei-Faktor-Eingaben tippt Simone selbst ein**, du trägst nie Zugangsdaten für sie ein. Domain-Umzug erst nach ihrer ausdrücklichen Freigabe und nach den Punkten unter „Vor dem Livegang" in `docs/OFFENE-PUNKTE.md`.
- Ein Entwurfs-Link von Elias zum Vergleichen: https://claude.ai/artifact/CdSePhqoP7P9FusJJ6KVuf (nur Ansicht, nicht Arbeitsgrundlage; die Dateien hier sind maßgeblich).

## Aufbau
- Eine Datei: `index.html` (CSS im `<style>` oben, HTML mit Ansichten, drei `<script>`-Blöcke am Ende). Bilder in `img/`. Kein Build, kein Framework, keine Pakete.
- **Hash-Routing:** Jede Seite ist ein `<div class="view" id="v-…">`. Die Navigation schaltet per `#name` um. Ansichten: `home`, `ueber-mich`, `labor`, `stress`, `ihht`, `hyperthermie`, `rifetech`, `medkey`, `infusion`, `darm`, `ohr`, `preise`. Neue Seite = neuer `view`-Block + Eintrag in der `views`-Zuordnung im ersten Skript + Menüpunkt in `<nav>` (und ggf. Footer/Startseite).
- **Kontakt hat keine Unterseite.** Jeder Link `href="#kontakt"` (Nav, Hero-Buttons, Textbuttons) scrollt zu den Kontakt-Kacheln im Footer (`#kontakt-info`) und lässt sie kurz aufleuchten. Neue Kontakt-Buttons einfach als `<a href="#kontakt">` setzen.
- **Footer** „Waldlicht": Wald-Foto mit dunklem Anthrazit-Schleier, drei Kontakt-Kacheln (Anrufen, Schreiben, Termin), darunter Praxis, Anfahrt, Öffnungszeiten, unten Copyright mit „All rights reserved.", Instagram- und Facebook-Icons, Impressum und Datenschutz.
- **Preise-Seite** ist interaktiv: Die Leistungen stehen als Daten im dritten `<script>` (Array `G`: Gruppen → Leistungen → Varianten mit Preis). **Preise ändern = dort die Zahl ändern**, nicht im HTML. Karten lassen sich anklicken, die Summenleiste unten rechnet live.
- **Animierte Grafiken** (`.viz`) auf Labordiagnostik und Stressdiagnostik (Referenzbereich-Bänder, Herzschlag/HRV, Cortisol-Tagesprofil): reines SVG/CSS, starten beim Einblenden (IntersectionObserver im ersten Skript), respektieren „Bewegung reduzieren".
- **Heros** der Leistungsseiten: `.shero` (Foto `img.sbg` + heller Schleier, leichter Parallax). Alle Leistungsseiten haben absichtlich **dieselbe Höhe** (`--shh`). Varianten: `.shero-dev` (Medkey/Rifetech: Gerät links, Text rechts), `.shero-dome` (Hyperthermie), `.hero-wald` (Startseite). Neues Heldenbild: Foto auf ca. 1600 px Breite, hell und warm, Motiv so setzen, dass Text lesbar bleibt (`object-position`).

## Design-System
- **Farben (Tokens in `:root`):** Hintergrund `#FBF7F1`, Sand `#F3EADD`, Papier `#F9F3E8`, **Tinte/Überschriften Anthrazit `#454C54`** (`--ink`, `--head-ink`; bewusst kein Schwarz), Muted `#5D646B`, Akzenttext `#86622F`, Button-Braun `#8A6531`, **Orange `#E3A15C`** (Signalfarbe), Grau `#A9AFB6`, Doctolib-Blau `#107ACA` (nur für den Doctolib-Tab).
- **Schriften (Google Fonts):** Überschriften Newsreader, Labels/Buttons Josefin Sans (Versalien, Abstand), Fließtext Mulish.
- **Textur:** Abschnitte mit feinem Naturpapier (`img/tex-papier-fein.png`, 512 px gekachelt): `.logos`, `.page-head`, `.bg-tex`, Footer-freie Bänder. Nicht durch andere Muster ersetzen.
- **Formen:** weiche Blatt-Ecken (`border-radius: 26px 26px 26px 8px`), organische „Kiesel"-Foto-Blasen (`.bub`) für Simones Porträt, Buttons als Pille mit innerem „Baumring" (`.btn`, `.btn.ghost`). Orange als Highlight, nie flächig laut.
- **Bewegung:** immer dezent, immer mit `prefers-reduced-motion`-Ausnahme.
- **Mobil:** muss bei 390 px sauber sein, kein seitliches Scrollen. Burger-Menü unter 1400 px.
- Das Logo (`img/logo.png`) sitzt optisch exakt mittig zum Schriftzug (`.brandmark`, `top:-2.7px`), nicht verändern, ohne zu prüfen.

## Texte und Ton
- Simone schreibt in **Ich-Form** („ich", „meine Praxis"), spricht Besucher mit **du** an. Sachlich, warm, keine Superlative.
- Rechtlicher Rahmen: Sie ist **Heilpraktikerin**. Keine Heilversprechen, keine Garantien, keine Aussagen wie „heilt", „beseitigt", keine unbelegten Wirkversprechen. Bei Zweifeln formuliere vorsichtig und weise Simone knapp darauf hin (ein Satz, kein Vortrag).
- **Texte nur nach ausdrücklicher Ansage von Simone ändern.** Einige Mikrotexte hat Elias ergänzt und noch nicht von Simone gegenlesen lassen, siehe `docs/OFFENE-PUNKTE.md`, Abschnitt „Von Simone zu prüfen".
- Preise und Öffnungszeiten nie raten, immer bei Simone erfragen.

## Arbeitsweise (immer so)
1. Änderung in `index.html` bzw. `img/` machen. Bilder vorher mit `python3 tools/bild-optimieren.py` verkleinern (Hero 1600 px, Kacheln 900 px, JPEG ca. 82 %). Nur Fotos mit gesicherter Lizenz (eigene Fotos von Simone, Unsplash/Pexels o. ä. mit freier Lizenz); jedes neue Foto in `docs/BILDQUELLEN.md` eintragen.
2. Prüfen: `python3 tools/check.py` (alle 12 Ansichten, Desktop und 390 px, JS-Fehler, kaputte Bilder, seitliches Scrollen; Screenshots in `tools/shots/`, **sieh dir die betroffenen Screenshots wirklich an**). Beim ersten Mal: `pip install playwright && playwright install chromium`.
3. Simone kurz sagen, was sich geändert hat (ein bis drei Sätze) und wo sie es sieht.
4. Nach ihrem Okay: committen mit verständlicher Nachricht, pushen. Ab Einrichtung von Netlify veröffentlicht sich `main` automatisch.
5. `docs/CHANGELOG.md` um einen Eintrag ergänzen.

## Nicht tun
- Keine Zugangsdaten, Passwörter, Tokens in Dateien oder Commits.
- Nichts veröffentlichen, versenden oder die Domain umstellen ohne Simones ausdrückliches Okay.
- Keine externen Skripte/Tracker/Analytics einbauen, ohne dass Simone es will (Datenschutz). Die Seite lädt bisher nur Google Fonts nach (siehe offene Punkte).
- Kein Framework, keinen Build-Schritt einführen. Die Seite soll für Simone und jeden Claude lesbar bleiben.
- Keine Fotos von Patienten oder erkennbaren Dritten ohne schriftliche Einwilligung.

## Wichtige feste Angaben (Stand bei Übergabe)
- Telefon/WhatsApp: 0176 951 52 732 (WhatsApp-Nummer noch von Simone bestätigen lassen), E-Mail: info@heilpraxis-toelstede.de
- Doctolib: https://www.doctolib.de/heilpraktiker/muenchen/simone-toelstede · Jameda: https://www.jameda.de/simone-toelstede/heilpraktiker/muenchen
- Instagram: https://www.instagram.com/heilpraxis_toelstede/ · Facebook: https://www.facebook.com/HeilpraxisToelstede
- Anfahrt: U1, U2, U7 und Bus 52, 58, 68 bis Kolumbusplatz; Parken vor der Praxis (gebührenpflichtig) oder am Schyrenbad (Parkscheibe, 4 Std.). Öffnungszeiten: nach Vereinbarung.
- Impressum/Datenschutz verlinken aktuell noch auf die alte Seite (heilpraxis-toelstede.de/impressum, /datenschutz).

## Zuerst offen (Kurzfassung, Details in `docs/OFFENE-PUNKTE.md`)
GitHub und Netlify einrichten · Impressum und Datenschutz auf die neue Seite · Google Fonts lokal einbinden (DSGVO) · Kontaktformular (optional) · Texte von Simone gegenlesen lassen · fehlende Fotos (Ohrakupunktur, Medkey, Praxisräume, Infusion) · Domain umziehen.
