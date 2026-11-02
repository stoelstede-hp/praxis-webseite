# Übergabe: Webseite Heilpraxis Toelstede

Liebe Simone,

Elias hat dir eine neue Webseite gebaut. Sie ist fertig zum Weiterarbeiten: Texte ändern, Bilder tauschen, neue Seiten ergänzen. Das geht ab jetzt mit deinem eigenen Claude auf deinem Rechner. Du musst nichts programmieren, du sagst Claude einfach, was du willst.

**Wichtig vorweg:** Die Seite ist noch **nicht** im Netz. Deine bisherige Seite heilpraxis-toelstede.de bleibt unverändert online, bis du selbst entscheidest umzuziehen. GitHub und Netlify (die beiden Dienste, über die die Seite später veröffentlicht wird) sind noch **nicht eingerichtet**. Das machen wir in Teil 2 gemeinsam mit Claude.

---

## Teil 1: Loslegen (ca. 10 Minuten)

1. **Ordner entpacken.** Entpacke `heilpraxis-toelstede-website.zip` an einen Ort, den du wiederfindest, zum Beispiel `Dokumente/heilpraxis-toelstede-website`.
2. **Seite ansehen.** Doppelklick auf `index.html`. Sie öffnet sich im Browser. Mit der Maus durch die Menüpunkte klicken, am Handy-Format kannst du die Fenstergröße verkleinern.
3. **Claude mit dem Ordner verbinden.** Öffne die Claude-App (oder Claude Code) und wähle diesen Ordner als Arbeitsordner. Claude liest dann automatisch die Datei `CLAUDE.md`, darin steht alles, was es über die Seite wissen muss: Aufbau, Farben, Schriften, Regeln, offene Punkte.
4. **Erste Nachricht an Claude** (einfach kopieren):

   > Lies bitte CLAUDE.md und UEBERGABE.md in diesem Ordner. Das ist meine neue Webseite. Mach dich damit vertraut, öffne sie lokal und sag mir kurz, was du gesehen hast und welche Punkte noch offen sind.

Danach kannst du ganz normal schreiben, zum Beispiel:

- „Ändere auf der Seite Stressdiagnostik den ersten Absatz so: …"
- „Tausche das Bild oben auf der Seite Darmgesundheit gegen dieses Foto." (Foto anhängen)
- „Die Preise für Infusionstherapie sind jetzt 70 €."
- „Bau eine neue Seite für Akupunktur im gleichen Stil wie Ohrakupunktur."
- „Prüfe die ganze Seite auf Fehler, am Desktop und am Handy."

Claude ändert die Dateien im Ordner. Zum Ansehen genügt es, `index.html` im Browser neu zu laden.

**Gut zu wissen**
- Texte sind in deiner Ich-Form geschrieben. Claude ändert Texte nur, wenn du es sagst.
- Neue Fotos bitte von Claude vor dem Einbau verkleinern lassen (Webgröße), sonst wird die Seite langsam.
- Du kannst jederzeit eine Sicherung machen: den ganzen Ordner kopieren. Sobald GitHub eingerichtet ist (Teil 2), hast du automatisch jede alte Version.

---

## Teil 2: Veröffentlichen einrichten (GitHub und Netlify)

Das ist einmalige Arbeit, danach gilt: **Änderung gemacht, Claude sagt „veröffentliche", fertig.**

Sag deinem Claude am besten: „Führe mich Schritt für Schritt durch Teil 2 der UEBERGABE.md. Mach alles, was du selbst kannst, und sag mir genau, wo ich klicken oder etwas eingeben muss." Hier der Ablauf:

### 2.1 GitHub (der Speicherort für die Seite und ihre Versionen)
1. Konto anlegen auf **github.com** (kostenlos), am besten mit der Praxis-E-Mail. Zwei-Faktor-Anmeldung einschalten.
2. Neues **privates** Repository anlegen, Name: `heilpraxis-toelstede-website`. Ohne README, ohne .gitignore (beides ist schon im Ordner).
3. Claude verbindet den Ordner mit dem Repository und lädt alles hoch (`git init`, `git remote add`, `git push`). Falls Git auf deinem Rechner fehlt, installiert Claude es oder führt dich durch die Installation von **GitHub Desktop** (die einfachere Variante mit Knöpfen statt Befehlen).
4. Anmeldung bei GitHub: Passwörter und Zugangscodes tippst **du** selbst ein, nicht Claude.

### 2.2 Netlify (das Hosting, das die Seite ins Netz stellt)
1. Konto anlegen auf **netlify.com** (kostenlos reicht), Anmeldung über „Mit GitHub fortfahren".
2. „Add new site", „Import an existing project", GitHub wählen, das Repository `heilpraxis-toelstede-website` auswählen.
3. Einstellungen: **Build command** leer lassen, **Publish directory** `.` (ein Punkt). Die Datei `netlify.toml` setzt das bereits.
4. „Deploy". Nach einer Minute gibt Netlify eine Adresse wie `irgendwas.netlify.app`. Das ist deine Testseite. Prüfe dort alle Seiten, am Handy und am Rechner.
5. Ab jetzt: Jede Änderung, die in GitHub landet (Claude: „committe und pushe"), wird automatisch veröffentlicht.

### 2.3 Eigene Adresse umziehen (erst am Schluss, wenn du bereit bist)
1. In Netlify unter „Domain management" die Domain `heilpraxis-toelstede.de` hinzufügen. Netlify zeigt dann, welche DNS-Einträge nötig sind.
2. Diese Einträge beim Anbieter eintragen, bei dem die Domain liegt (dort, wo du die Domain verwaltest, nicht unbedingt, wo die alte Seite läuft). Wenn du unsicher bist, lass Claude die Anleitung für deinen Anbieter heraussuchen.
3. Die bisherige Seite bleibt bis zum Umstellen online. Netlify stellt das HTTPS-Zertifikat automatisch aus.
4. **Vorher** die Punkte aus `docs/OFFENE-PUNKTE.md` unter „Vor dem Livegang" erledigen (vor allem Impressum, Datenschutz und die Schriften).

### 2.4 Der tägliche Ablauf, wenn alles eingerichtet ist
1. Du sagst Claude, was geändert werden soll.
2. Du schaust es dir lokal an (`index.html` im Browser).
3. Du sagst: „Passt, veröffentliche das." Claude führt `python3 tools/check.py` aus, committet und pusht. Nach etwa einer Minute ist es live.
4. Etwas ist schiefgegangen? Sag: „Mach die letzte Veröffentlichung rückgängig." Dank GitHub ist jede frühere Version abrufbar.

---

## Was in diesem Ordner liegt

| Datei / Ordner | Wofür |
|---|---|
| `index.html` | die komplette Webseite (Texte, Gestaltung, Verhalten) |
| `img/` | alle Bilder, die auf der Seite verwendet werden |
| `_reserve/` | Bilder und Grafiken, die ausprobiert wurden, aber nicht verwendet werden (z. B. Darm-Fotos, Darm-Illustrationen) |
| `CLAUDE.md` | die Arbeitsanweisung für Claude, bitte nicht löschen |
| `docs/` | Änderungsprotokoll, offene Punkte, Bildquellen |
| `tools/check.py` | prüft alle 12 Seiten auf Fehler (Claude startet das selbst) |
| `tools/bild-optimieren.py` | macht Fotos webtauglich |
| `netlify.toml`, `.gitignore` | Einstellungen für Hosting und GitHub |

## Wenn etwas hakt
- **Seite sieht komisch aus:** Browser-Fenster neu laden (Strg/Cmd + Shift + R).
- **Claude findet den Ordner nicht:** Arbeitsordner in der Claude-App neu auswählen.
- **Du hast etwas kaputt gemacht:** Sag Claude „Stelle den Stand von vorhin wieder her". Ohne GitHub hilft die kopierte Sicherung des Ordners.
- **Fragen zum Aufbau:** Elias (elias@paurnfeindt-eyss.com).

Viel Freude damit!
