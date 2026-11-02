# Offene Punkte

## Zuerst: Veröffentlichung einrichten
- [ ] GitHub-Konto und privates Repo `heilpraxis-toelstede-website` (siehe UEBERGABE.md, 2.1)
- [ ] Netlify-Konto, Repo anbinden, Testadresse prüfen (2.2)
- [ ] Domain `heilpraxis-toelstede.de` umziehen (2.3), erst nach „Vor dem Livegang"

## Vor dem Livegang (rechtlich und technisch)
- [ ] **Impressum und Datenschutzerklärung** auf der neuen Seite bereitstellen. Die Links im Footer zeigen noch auf die alte Seite (`heilpraxis-toelstede.de/impressum/`, `/datenschutz/`). Eigene Seiten oder Texte aus der alten Seite übernehmen und prüfen lassen (Angaben nach § 5 DDG, Heilpraktiker-Berufsangaben, Aufsichtsbehörde).
- [ ] **Google Fonts lokal einbinden** (Newsreader, Josefin Sans, Mulish als Dateien in `fonts/` ablegen, per `@font-face` laden, die Google-Links aus `<head>` entfernen). Grund: Beim Nachladen von Google-Servern wird die IP-Adresse der Besucher übertragen, das gilt in Deutschland als datenschutzrelevant. Danach in der Datenschutzerklärung nichts zu Google Fonts mehr nötig.
- [ ] Externe Verweise prüfen: Doctolib, Jameda, Instagram, Facebook, Google Maps sind reine Links (keine Einbindung), das ist unproblematisch.
- [ ] WhatsApp-Nummer bestätigen (derzeit 0176 951 52 732; im schwebenden Kontakt-Button unten rechts).
- [ ] Cookie-Banner nur nötig, wenn später Tracking/Einbettungen ergänzt werden. Aktuell setzt die Seite keine Cookies.
- [ ] Domain-Umzug: Wo liegt die Domain, wo die bisherige Seite? Klären, bevor DNS geändert wird. E-Mail (`info@…`) darf dabei nicht unterbrochen werden (MX-Einträge unverändert lassen).

## Von Simone zu prüfen (Texte, die Elias ergänzt hat)
- Footer: Überschrift „Ich freue mich auf dich." und Kachel-Untertexte („Gern auch eine Nachricht hinterlassen", „Ich melde mich zeitnah", „Direkt freie Zeiten sehen")
- Preise: Hero-Satz „Transparent und ohne Kleingedrucktes. Klick dir dein Paket zusammen und sieh sofort, was es kostet.", die Schritt-Überschriften und Zeilen („Ankommen", „Beratung", „Messen & Verstehen", „Behandeln") mit ihren Untertiteln, der Hinweis „Richtwert, zzgl. Material bzw. Leihgebühr, wo angegeben", Kurztitel „Hand anlegen, Spannung lösen" bei Manuelle Therapien
- Labordiagnostik: Satz unter der Grafik („Jeder Wert wird im Verhältnis zum Referenzbereich eingeordnet …")
- Stressdiagnostik: Satz unter der Cortisol-Grafik („… kann sich dieser Verlauf abflachen"); Herzschlag-Grafik nutzt Simones eigenen Satz
- Bildunterzeilen „Schematische Darstellung, keine Messwerte"
- Alle übrigen Texte stammen von Simones alter Seite (unverändert übernommen).

## Inhalte, die noch fehlen
- [ ] Fotos: Ohrakupunktur, Medkey (Behandlung), Praxisräume, Infusion. Ideal sind echte Fotos von Simone und der Praxis statt Stockfotos.
- [ ] Rifetech: Geräte-Foto ist niedrig aufgelöst (2× hochgerechnet), besseres Produktfoto besorgen.
- [ ] Hyperthermie: Im Foto ist der Produktname „KENKO-DÔME" sichtbar; prüfen, ob das gewollt ist, sonst Foto tauschen.
- [ ] Text „Craniosacrale Therapie" ist noch nicht lektoriert.
- [ ] Kontaktformular (optional; Netlify Forms wäre möglich, datenschutzrechtlich mit Hinweis zu ergänzen).
- [ ] Mitgliedschaften/Logos (Fachverband, Aponeo) auf Aktualität und Nutzungserlaubnis prüfen.
- [ ] „Über mich"- und Preise-Seitenkopf sind schlichter als die Leistungsseiten; auf Wunsch mit Foto-Hero im gleichen Stil gestalten.

## Ideen
- Kurze Praxis-Rundgang-Galerie, Kundenstimmen (nur mit Einwilligung), Blog/Aktuelles-Bereich (die Startseite hat bereits „Aus der Praxis").
