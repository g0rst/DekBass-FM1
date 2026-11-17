# DekBass FM-1 – Handbuch

Firmware v1.0 für den M-VAVE FM-1 und das M-Vave SMK-37. Namen in GROSSBUCHSTABEN sind DekBass-Funktionen; welche Taste am FM-1 und am SMK-37 dazu gehört, steht in Kapitel 4. Was das SMK-37 zusätzlich kann, steht in Kapitel 12.

## 1. Sicherheit

- DekBass erzeugt sehr tiefe Frequenzen. Lautstärke an Mixer und Anlage immer langsam hochziehen.
- Der eingebaute Lautsprecher gibt keinen Sub-Bass wieder. Sounds nie nur am Lautsprecher einstellen – auf der Anlage wird der Bass sonst viel zu laut.
- Subsonic-Filter und Limiter sind ab Werk an. Nur abschalten, wenn du genau weißt, was deine Anlage verträgt.
- Bei lauten Sessions Gehörschutz tragen.

## 2. Installation

1. FM-1 voll aufladen und per USB-C mit dem Computer verbinden.
2. Den DekBass-Installer im Browser öffnen (Chrome oder Edge).
3. **Backup erstellen:** Presets und Einstellungen der aktuellen Firmware sichern.
4. „Installieren“ wählen und warten, bis der FM-1 neu startet. Kabel währenddessen nicht trennen.
5. **Zurück zur Original-Firmware:** mit dem offiziellen M-VAVE-Updater die Firmware V15 neu aufspielen.

Die Installation erfolgt auf eigenes Risiko.

## 3. Das Prinzip

DekBass hat zwei Ansichten: **BASS** und **EUCLID**. Beide laufen immer gleichzeitig. **SEQ lang drücken** wechselt nur, was du siehst und was die vier Knobs steuern – der Sound läuft weiter.

Oben im Display steht immer: Tempo, aktueller Preset (z. B. A07) und ein kleiner Indikator der anderen Ansicht. Unten stehen die vier Parameter, die die Knobs gerade steuern.

## 4. Bedienelemente

| Funktion | FM-1 | SMK-37 | Was sie tut |
|---|---|---|---|
| Knob 1–4 | KNOB 1–4 | K5–K8 | Die vier Parameter der aktuellen Seite |
| MASTER | MASTER | K1 | Gesamtlautstärke |
| TEMPO | SELECT | K2 | Tempo |
| ENGINE / FOKUS | ALGORITHM | K3 | BASS: Engine wählen. EUCLID: Voice im Fokus |
| PRESET | PRESETS | K4 | Sound-Preset wählen |
| PLAY | PLAY | SEQ PLAY | Start/Stopp |
| REC | REC | SEQ REC | Live-Aufnahme in den Bass-Sequencer |
| SEQ | SEQ | SEQ | Kurz: Sequencer-Bearbeitung. Lang: BASS ↔ EUCLID |
| MENU | HOME | PATCH | Einstellungen |
| BANK | SAVE | BT | Presets laden; mit SHIFT speichern |
| SHIFT | GLO | GLOBE | Zweite Ebene jeder Taste |
| PAGE | EDIT | PARA | Nächste Seite. SHIFT + PAGE: die vier Werte der Seite auf Standard |
| DROP | FX | FX | Performance (Kapitel 8) |
| BUILD | ARP | ARP | Performance (Kapitel 8) |
| CUT | ENV | CHORD | Performance (Kapitel 8) |
| FILL | LFO | NOTE REPEAT | Performance (Kapitel 8) |
| KONARK | SEL | SCALE | Konark-Ansicht an/aus |
| OCT− / OCT+ | OCT− / OCT+ | OCTAVE− / OCTAVE+ | Oktave |
| Weiße Tasten | F3–G5 | mittlere 27 Tasten | Noten; im Sequencer Steps 1–16; in EUCLID: F3–B3 = Mute V1–V4 |

Die Drehregler lassen sich nicht drücken. Alles, was du auslöst, liegt auf Tasten.

## 5. Bass spielen

### Engines

Mit dem Encoder ENGINE (FM-1: ALGORITHM, SMK-37: K3) wählst du eine von vier Engines:

- **SUB** – reiner, tiefer Sinus-Bass mit Obertönen. Für Box-Bässe und lange Drops.
- **FM** – harte, metallische Bässe.
- **PD** – Growls und „sprechende“ Mitten.
- **FX** – Sirene, Laser, Horn, Noise.

Die vier Knobs auf ENGINE sind Makros der gewählten Engine. Alle anderen Seiten sind für alle Engines gleich.

### Seiten

| Seite | Knob 1 | Knob 2 | Knob 3 | Knob 4 |
|---|---|---|---|---|
| PERFORM | Cutoff | Resonanz | Drive | Glide |
| ENGINE | Makro 1 | Makro 2 | Makro 3 | Makro 4 |
| PITCH | Pitch-Env Tiefe | Pitch-Env Zeit | Sub-Pegel | Oktave/Tune |
| ENV | Attack | Decay | Sustain | Release |
| LFO | Rate | Tiefe | Ziel | Form |
| FX | Kette | Crush | Delay | Space |

Mit SHIFT: ENV → Filter-Hüllkurve, LFO → LFO 2, FX → Delay-Zeit, Feedback, Space-Größe, Ausgangspegel.

**Tipp für den klassischen Dek-Bass-Sweep:** Seite PITCH, Pitch-Env Tiefe auf +24, Zeit auf ca. 300 ms, Glide auf PERFORM leicht aufdrehen.

### Effektketten

- **CLASSIC:** Drive vor dem Filter – warm.
- **DIRTY:** Drive nach dem Filter – aggressiv.
- **SUB-SAFE:** Verzerrung nur in den Mitten, der Sub bleibt sauber. Empfohlen für große Anlagen.

## 6. Bass-Sequencer

1. SEQ kurz drücken → Sequencer-Bearbeitung.
2. **Step setzen:** weiße Taste für den Step halten und eine Note spielen.
3. **Live aufnehmen:** REC, dann PLAY, dann spielen.
4. **Step-Details:** Step halten und Knobs drehen – Knob 1 Gate/Tie, Knob 2 Wahrscheinlichkeit, Knob 3 Ratchet (1–4), Knob 4 Slide/Accent.
5. **Parameter-Lock:** Step halten und den Parameter auf einer Klangseite drehen. Bis zu 4 verschiedene Parameter pro Pattern.
6. **Länge:** SHIFT + SEQ, dann Knob 1 (1–64 Steps). In der Sequencer-Bearbeitung blättert PAGE durch die Step-Seiten 1–16, 17–32 usw. Auf dem SMK-37 zeigen < und > die Step-Seiten auch außerhalb der Bearbeitung auf den Pads.
7. **Bedingungen:** Step halten + SHIFT + Knob 2: immer, jeder 2. Durchlauf, jeder 4. Durchlauf, nur bei FILL.
8. **Swing:** im MENU, 50–75 %.

## 7. Euclid-Drums

### Die vier Räder

Jede Voice ist ein Rad mit 16 Speichen – eine Speiche pro Step. Breite Speichen liegen auf den Achteln, schmale dazwischen. Leuchtende Speichen sind Schläge.

| Rad | Farbe | Standard | Modelle |
|---|---|---|---|
| V1 | Rot | Kick | Kick, Sub-Kick, Box-Kick |
| V2 | Ocker | Snare | Snare, Clap, Rim |
| V3 | Indigo | Perc | Hat, Metal-Perc, Shaker |
| V4 | Grau | FX | Siren-Hit, Laser, Horn, Noise |

### Seiten

- **HITS:** Anzahl der Schläge pro Voice (0–16). SHIFT + drehen = Länge der Voice (1–16) für Polyrhythmen.
- **ROTATE:** verschiebt das Muster (0–15 Steps).
- **LEVEL:** Lautstärke – das Rad wird größer oder kleiner.
- **SOUND:** Tune, Decay, Tone, Drive der Voice im Fokus. Modell wechseln: SHIFT + Knob 1.

### Stummschalten, Solo, Fokus

- **Mute:** In der EUCLID-Ansicht schalten die weißen Tasten F3, G3, A3 und B3 die Voices V1–V4 stumm oder laut. Auf dem SMK-37 auch die Pads 5–8.
- **Solo:** SHIFT + dieselbe Taste bzw. dasselbe Pad.
- **Fokus:** Encoder FOKUS (FM-1: ALGORITHM, SMK-37: K3). Die zuletzt geänderte Voice bekommt den Fokus automatisch.
- Die übrigen Tasten spielen in der EUCLID-Ansicht weiter den Bass.

### Weitere Einstellungen (MENU)

- **Verteilung:** euklidisch (gleichmäßig) oder Block.
- **Mutate:** zufällige kleine Variation pro Takt, 0–100 %.
- **Duck:** Die Kick senkt den Bass kurz ab, damit beide klar bleiben.

**Konark-Ansicht:** Die Taste KONARK (FM-1: SEL, SMK-37: SCALE) zeigt alle vier Voices als Ringe in einem großen Rad. Nochmal drücken schaltet zurück.

## 8. Performance

| Taste | Wirkung |
|---|---|
| **DROP** (halten) | Pitch fällt, Filter schließt, Delay steigt, nur die Kick spielt. Loslassen = zurück auf die nächste Eins |
| **BUILD** (halten) | Riser über 1/2/4/8 Takte (im MENU). Loslassen = Drop auf die nächste Eins |
| **CUT** (tippen) | Alles stumm bis zur nächsten Eins |
| **FILL** (halten) | Snare und Perc doppelt, FILL-Steps im Bass spielen |

## 9. Presets und Pattern

- **Banks:** A und B sind Werks-Presets (geschützt), C und D sind für dich. C01–C04 enthalten neutrale Startpunkte.
- **Schnell wechseln:** Encoder PRESET (FM-1: PRESETS, SMK-37: K4).
- **Laden über die Bank-Seite:** BANK drücken, mit Knob 1 Bank, mit Knob 2 Preset wählen.
- **Speichern:** SHIFT + BANK, Platz in C oder D wählen, bestätigen. Das Gerät fragt, ob das aktuelle Pattern verknüpft werden soll.
- **Pattern** (Bassline + Drums) haben 64 eigene Plätze: SEQ + BANK.
- **Lade-Modus** (MENU): „SOUND“ wechselt nur den Klang – Drums laufen weiter. „SOUND + PATTERN“ wechselt auf die nächste Eins beides.
- **Init-Sound:** SHIFT + BANK lang halten.

## 10. Einstellungen (MENU)

Das Tempo stellst du mit dem Encoder TEMPO ein (FM-1: SELECT, SMK-37: K2). Im MENU: Clock (intern / MIDI-Slave / MIDI-Master), MIDI-Kanal, Subsonic-Filter (20/25/30/35 Hz), Limiter, Mono-Summe, Lade-Modus, Swing, BUILD-Länge, Display-Helligkeit, Tastendynamik (nur SMK-37), Werksreset (Sounds / Pattern / Einstellungen getrennt).

## 11. Fehlerbehebung

| Problem | Lösung |
|---|---|
| Kein Bass hörbar | Kopfhörer oder Anlage benutzen – der Lautsprecher spielt keinen Sub. Lade-Modus und Mutes prüfen |
| Bass wird bei Sweeps leiser | Subsonic-Filter fängt Frequenzen unter dem Grenzwert ab. Gewollt zum Schutz |
| Drums laufen nicht mit externer Clock | MENU → Clock auf MIDI-Slave stellen |
| Preset lässt sich nicht speichern | Bank A und B sind geschützt – in C oder D speichern |
| Gerät startet nicht mehr | Mit dem offiziellen M-VAVE-Updater Firmware V15 aufspielen, dann DekBass neu installieren |

## 12. SMK-37

DekBass läuft auch auf dem SMK-37 Pro, dem SMK-37 Elite und dem MKE-P37; das Starrykey 37 Play nutzt das Pro-Paket. Alles aus den Kapiteln 3–11 gilt auch dort. Dazu kommen:

| Bedienelement | Funktion |
|---|---|
| 10 äußere Tasten (C3–E3, G♯5–C6) | Weitere Bass-Noten, vor allem nach unten |
| Pads in BASS | Die 16 Steps der aktuellen Step-Seite in Ocker, Playhead hell |
| Pads in EUCLID | 1–4 spielen V1–V4 von Hand, 5–8 Mute V1–V4 (mit SHIFT Solo), 9–12 DROP, BUILD, CUT, FILL, 13–16 Pattern 1–4 (Wechsel auf die nächste Eins) |
| Fader 1–4 | Pitch-Sweep-Tiefe, Delay-Throw, Duck, Balance Bass/Drums. Ein Fader greift erst, wenn du ihn bewegst |
| Pitch-Wheel | Bend auf dem Bass, ±12 Halbtöne |
| Mod-Wheel | BUILD von Hand: Filter öffnet, Noise steigt, Ratchets verdoppeln sich |
| KNOB BANK | Pattern-Kette |
| FADER BANK | Zeigt die vier Fader-Makros groß an |
| < / > | Blättert durch die Step-Seiten des Bass-Sequencers |

- Das SMK-37 hat keinen TRS-MIDI-Eingang: MIDI-Clock kommt nur über USB.
- Vor der ersten Installation eine vollständige Flash-Sicherung machen (Anleitung in SMK37.md im Repository). Kalibrierung und Rückweg zur Original-Firmware bleiben unberührt.
- Beim ersten Start löscht DekBass den Einstellungsbereich der Original-Firmware.
- Pakete: dekbass-smk37.fwsc (Pro), dekbass-smk37-elite.fwsc, dekbass-smk37-mke.fwsc.
