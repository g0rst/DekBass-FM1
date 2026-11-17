# DekBass FM-1 – User Manual

Firmware v1.0 for the M-VAVE FM-1 and the M-Vave SMK-37. Names in CAPITALS are DekBass functions; chapter 4 shows which button carries each one on the FM-1 and on the SMK-37. What the SMK-37 adds is in chapter 12.

## 1. Safety

- DekBass produces very low frequencies. Always bring up the mixer and sound system level slowly.
- The built-in speaker cannot reproduce sub-bass. Never dial in sounds on the speaker alone – on a real system the bass will be far too loud.
- The subsonic filter and limiter are on by default. Only switch them off if you know exactly what your system can handle.
- Wear ear protection at loud sessions.

## 2. Installation

1. Fully charge the FM-1 and connect it to your computer via USB-C.
2. Open the DekBass installer in your browser (Chrome or Edge).
3. **Make a backup** of the presets and settings of your current firmware.
4. Choose “Install” and wait until the FM-1 restarts. Do not unplug the cable.
5. **Back to the original firmware:** reinstall firmware V15 with the official M-VAVE updater.

Install at your own risk.

## 3. The idea

DekBass has two views: **BASS** and **EUCLID**. Both always run at the same time. **Long-press SEQ** only changes what you see and what the four knobs control – the sound keeps playing.

The top of the screen always shows tempo, the current preset (e.g. A07) and a small indicator for the other view. The bottom shows the four parameters the knobs control right now.

## 4. Controls

| Function | FM-1 | SMK-37 | What it does |
|---|---|---|---|
| Knob 1–4 | KNOB 1–4 | K5–K8 | The four parameters of the current page |
| MASTER | MASTER | K1 | Master volume |
| TEMPO | SELECT | K2 | Tempo |
| ENGINE / FOCUS | ALGORITHM | K3 | BASS: choose the engine. EUCLID: the voice in focus |
| PRESET | PRESETS | K4 | Choose a sound preset |
| PLAY | PLAY | SEQ PLAY | Start/stop |
| REC | REC | SEQ REC | Live recording into the bass sequencer |
| SEQ | SEQ | SEQ | Short: edit sequencer. Long: BASS ↔ EUCLID |
| MENU | HOME | PATCH | Settings |
| BANK | SAVE | BT | Load presets; with SHIFT: save |
| SHIFT | GLO | GLOBE | Second layer of every button |
| PAGE | EDIT | PARA | Next page. SHIFT + PAGE: the page's four values back to default |
| DROP | FX | FX | Performance (chapter 8) |
| BUILD | ARP | ARP | Performance (chapter 8) |
| CUT | ENV | CHORD | Performance (chapter 8) |
| FILL | LFO | NOTE REPEAT | Performance (chapter 8) |
| KONARK | SEL | SCALE | Konark view on/off |
| OCT− / OCT+ | OCT− / OCT+ | OCTAVE− / OCTAVE+ | Octave |
| White keys | F3–G5 | middle 27 keys | Notes; in the sequencer: steps 1–16; in EUCLID: F3–B3 = mute V1–V4 |

The knobs cannot be pressed. Everything you trigger is on a button.

## 5. Playing bass

### Engines

The ENGINE encoder (FM-1: ALGORITHM, SMK-37: K3) selects one of four engines:

- **SUB** – pure, deep sine bass with harmonics. For box basses and long drops.
- **FM** – hard, metallic basses.
- **PD** – growls and “talking” mids.
- **FX** – siren, laser, horn, noise.

The four knobs on ENGINE are macros of the selected engine. All other pages are the same for every engine.

### Pages

| Page | Knob 1 | Knob 2 | Knob 3 | Knob 4 |
|---|---|---|---|---|
| PERFORM | Cutoff | Resonance | Drive | Glide |
| ENGINE | Macro 1 | Macro 2 | Macro 3 | Macro 4 |
| PITCH | Pitch env depth | Pitch env time | Sub level | Octave/tune |
| ENV | Attack | Decay | Sustain | Release |
| LFO | Rate | Depth | Target | Shape |
| FX | Chain | Crush | Delay | Space |

With SHIFT: ENV → filter envelope, LFO → LFO 2, FX → delay time, feedback, space size, output level.

**Tip for the classic dek bass sweep:** PITCH page, pitch env depth +24, time around 300 ms, then add a little glide on PERFORM.

### Effect chains

- **CLASSIC:** drive before the filter – warm.
- **DIRTY:** drive after the filter – aggressive.
- **SUB-SAFE:** distortion only in the mids, the sub stays clean. Recommended for big systems.

## 6. Bass sequencer

1. Short-press SEQ → sequencer edit.
2. **Enter a step:** hold the white key for the step and play a note.
3. **Record live:** REC, then PLAY, then play.
4. **Step details:** hold a step and turn the knobs – knob 1 gate/tie, knob 2 probability, knob 3 ratchet (1–4), knob 4 slide/accent.
5. **Parameter lock:** hold a step and turn a parameter on any sound page. Up to 4 different parameters per pattern.
6. **Length:** SHIFT + SEQ, then knob 1 (1–64 steps). In sequencer edit, PAGE moves through steps 1–16, 17–32 and so on. On the SMK-37, < and > also show the step pages on the pads outside the editor.
7. **Conditions:** hold step + SHIFT + knob 2: always, every 2nd pass, every 4th pass, FILL only.
8. **Swing:** in MENU, 50–75 %.

## 7. Euclid drums

### The four wheels

Each voice is a wheel with 16 spokes – one spoke per step. Wide spokes sit on the eighth notes, narrow ones in between. Lit spokes are hits.

| Wheel | Colour | Default | Models |
|---|---|---|---|
| V1 | Red | Kick | Kick, Sub kick, Box kick |
| V2 | Ochre | Snare | Snare, Clap, Rim |
| V3 | Indigo | Perc | Hat, Metal perc, Shaker |
| V4 | Grey | FX | Siren hit, Laser, Horn, Noise |

### Pages

- **HITS:** number of hits per voice (0–16). SHIFT + turn = voice length (1–16) for polyrhythms.
- **ROTATE:** shifts the pattern (0–15 steps).
- **LEVEL:** volume – the wheel grows or shrinks.
- **SOUND:** tune, decay, tone, drive of the focused voice. Change model: SHIFT + knob 1.

### Mute, solo, focus

- **Mute:** in the EUCLID view, the white keys F3, G3, A3 and B3 mute or unmute V1–V4. On the SMK-37, pads 5–8 do the same.
- **Solo:** SHIFT + the same key or pad.
- **Focus:** the FOCUS encoder (FM-1: ALGORITHM, SMK-37: K3). The last voice you changed gets focus automatically.
- The other keys keep playing the bass in the EUCLID view.

### More settings (MENU)

- **Distribution:** Euclidean (even) or block.
- **Mutate:** small random variation per bar, 0–100 %.
- **Duck:** the kick briefly lowers the bass so both stay clear.

**Konark view:** the KONARK button (FM-1: SEL, SMK-37: SCALE) shows all four voices as rings in one large wheel. Press it again to go back.

## 8. Performance

| Button | Effect |
|---|---|
| **DROP** (hold) | Pitch falls, filter closes, delay rises, only the kick plays. Release = back on the next downbeat |
| **BUILD** (hold) | Riser over 1/2/4/8 bars (set in MENU). Release = drop on the next downbeat |
| **CUT** (tap) | Everything silent until the next downbeat |
| **FILL** (hold) | Snare and perc double, FILL steps in the bass play |

## 9. Presets and patterns

- **Banks:** A and B are factory presets (protected), C and D are yours. C01–C04 hold neutral starting points.
- **Quick change:** the PRESET encoder (FM-1: PRESETS, SMK-37: K4).
- **Load from the bank page:** press BANK, knob 1 selects the bank, knob 2 the preset.
- **Save:** SHIFT + BANK, choose a slot in C or D, confirm. The unit asks whether to link the current pattern.
- **Patterns** (bassline + drums) have 64 slots of their own: SEQ + BANK.
- **Load mode** (MENU): “SOUND” changes only the sound – drums keep running. “SOUND + PATTERN” changes both on the next downbeat.
- **Init sound:** hold SHIFT + BANK.

## 10. Settings (MENU)

Set the tempo with the TEMPO encoder (FM-1: SELECT, SMK-37: K2). In MENU: clock (internal / MIDI slave / MIDI master), MIDI channel, subsonic filter (20/25/30/35 Hz), limiter, mono sum, load mode, swing, BUILD length, display brightness, key velocity (SMK-37 only), factory reset (sounds / patterns / settings separately).

## 11. Troubleshooting

| Problem | Solution |
|---|---|
| No bass audible | Use headphones or a system – the speaker does not play sub. Check load mode and mutes |
| Bass gets quieter during sweeps | The subsonic filter removes frequencies below its limit. Intended, for protection |
| Drums don’t follow external clock | MENU → set clock to MIDI slave |
| Preset cannot be saved | Banks A and B are protected – save to C or D |
| Unit no longer starts | Install firmware V15 with the official M-VAVE updater, then reinstall DekBass |

## 12. SMK-37

DekBass also runs on the SMK-37 Pro, the SMK-37 Elite and the MKE-P37; the Starrykey 37 Play uses the Pro package. Everything in chapters 3–11 applies there too. In addition:

| Control | Function |
|---|---|
| 10 outer keys (C3–E3, G♯5–C6) | More bass notes, mainly downwards |
| Pads in BASS | The 16 steps of the current step page in ochre, playhead bright |
| Pads in EUCLID | 1–4 play V1–V4 by hand, 5–8 mute V1–V4 (SHIFT: solo), 9–12 DROP, BUILD, CUT, FILL, 13–16 patterns 1–4 (change on the next downbeat) |
| Faders 1–4 | Pitch-sweep depth, delay throw, duck, bass/drums balance. A fader acts only once you move it |
| Pitch wheel | Bend on the bass, ±12 semitones |
| Mod wheel | BUILD by hand: filter opens, noise rises, ratchets double |
| KNOB BANK | Pattern chain |
| FADER BANK | Shows the four fader macros large |
| < / > | Move through the bass sequencer's step pages |

- The SMK-37 has no TRS MIDI input: MIDI clock comes over USB only.
- Make a full flash backup before the first install (instructions in SMK37.md in the repository). The calibration and the way back to the stock firmware stay untouched.
- On its first start, DekBass clears the stock firmware's settings area.
- Packages: dekbass-smk37.fwsc (Pro), dekbass-smk37-elite.fwsc, dekbass-smk37-mke.fwsc.
