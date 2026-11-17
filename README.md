# DekBass

Bass and Euclid-drum firmware for the M-VAVE FM-1 and the M-Vave SMK-37, made for Dek bass, box competitions and
sound-system sessions: a mono bass with long glide and deep pitch sweeps, four Euclidean drum voices drawn as Konark
wheels, and DROP / BUILD / CUT / FILL at hand.

**Status: phase 0, setup.** This repository holds the starting point, not DekBass yet: Felucca 1.6.1 with the SMK-37
board layer (branch `smk37` of genkigenki/Felucca, = hugelton/Felucca#237). Both boards build from one source tree from
day one. Nothing here is ready to install as DekBass.

- **SMK-37:** every mapping decision is in [smk37-port.yaml](smk37-port.yaml), made with the
  [fm1-to-smk37](https://github.com/genkigenki/fm1-to-smk37) kit. The base's SMK-37 notes: [SMK37.md](SMK37.md).
- **Manual** (Deutsch, English, हिन्दी, ଓଡ଼ିଆ): [docs/manual/](docs/manual/), as Markdown and as one designed page,
  `docs/manual/index.html` (rebuild with `python3 tools/dekbass/make_manual.py`).
- **Plan and next steps:** [docs/dekbass/PLAN.md](docs/dekbass/PLAN.md).
- **Building:** [BUILDING.md](BUILDING.md). Clone with the engines' submodule:
  `git clone --recurse-submodules <this repository>`.
- **The base:** Felucca's own README is kept as [README.felucca.md](README.felucca.md).

## Boards

| Board | Build | Package (once renamed) |
|---|---|---|
| M-VAVE FM-1 | `sh build.sh` | `dekbass.fwsc` |
| SMK-37 Pro (also Starrykey 37 Play) | `BOARD=smk37 sh build.sh` | `dekbass-smk37.fwsc` |
| SMK-37 Elite | `BOARD=smk37 MODEL=elite sh build.sh` | `dekbass-smk37-elite.fwsc` |
| MKE-P37 | `BOARD=smk37 MODEL=mke sh build.sh` | `dekbass-smk37-mke.fwsc` |

Until the rename (see the plan), the builds still produce Felucca's package names.

## Safety

Custom firmware is installed at your own risk. On the SMK-37, make a full flash backup before the first install, and
never write the protected flash ranges (`0x00000-0x03FFF`, `0xC0000-0xC1FFF`, `0xF4000-0xFDFFF`, `0xFF000-0xFFFFF`):
they hold the unit's calibration and keys. M-VAVE's own updater takes either board back to the stock firmware.

## Credits and license

DekBass builds on [Felucca](https://github.com/hugelton/Felucca) by Leo Kuroshita / Hügelton Instruments and on the
SMK-37 board layer and porting kit by genkigenki. See [CREDITS.md](CREDITS.md) and [LICENSING.md](LICENSING.md).

The firmware is licensed under GPL-3.0-only ([LICENSE](LICENSE)); the engines' submodule is MIT. "Felucca" and
"Hügelton Instruments" are names of Hügelton Instruments; DekBass uses its own name and look. M-VAVE, FM-1 and SMK-37
are names of their owners. This project is not affiliated with M-VAVE or JieLi.
