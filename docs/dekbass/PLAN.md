# DekBass: plan

The full concept and the four manuals (Deutsch, English, Hindi, Odia) live in the owner's DekBass document. This file is
the working plan for the repository.

## Phases

| Phase | Content | Done when |
|---|---|---|
| 0 Setup | This repository on Felucca 1.6.1 + SMK-37 layer, `smk37-port.yaml` decided, baseline build | the baseline hashes are recorded |
| 1 MVP | SUB + FX engines, filter, drive, limiter, 16-step bass sequencer, Euclid HITS + LEVEL, 2 x 2 wheel view | playable on a sound system |
| 2 Core | FM + PD, ROTATE + SOUND pages, locks, ratchets, probability, DROP / BUILD / CUT / FILL, presets and patterns | complete for live use |
| 3 Release | 64 steps, chains, conditions, Konark view, MIDI clock, factory presets, manuals | version 1.0 |

## Next steps (fm1-to-smk37 kit, AGENTS.md)

1. **Close the open questions** at the end of `smk37-port.yaml` with the owner.
2. **Baseline** on a machine with the JieLi toolchain (BUILDING.md; on Windows inside WSL):
   `sh build.sh`, then record `sha256sum build/felucca.bin build/felucca.fwsc build/loader/ota.bin`, run
   `sh tests/run_tests.sh` and note the failures that exist before any change.
3. **Rename to DekBass** in one commit: package stems in `tools/build.py` (`BOARD_STEM`), `build.sh`, `BUILDING.md`,
   `tests/run_tests.sh`; data family `DEKBASS` (and the owner-tag test, `tests/smk_owner_test.c`); USB / MIDI name
   `DekBass` and every installer filter; splash and name on screen. From here DekBass is its own firmware, so the
   FM-1 build is no longer compared with Felucca's: the new baseline is the renamed build.
4. **Storage:** list every stored object; on the SMK keep the store window and the protected ranges as the layer has
   them (AGENTS.md step 3).
5. **DekBass itself**, phase 1, written against the capability layer (fm1-to-smk37 docs/07): one source, both
   boards. SMK extras (pads per view, macro faders, bend +-12, BUILD on the mod wheel, outer keys as more notes) as
   in `smk37-port.yaml`.
6. **Build both** (SMK first, FM-1 last), all three SMK models, host tests.
7. **Device loop:** the owner installs after a verified full flash backup and reports; nothing is installed by an
   agent.

## Rules kept from the kit

- Never write the SMK's protected flash ranges; keep the allow-list, the asserts and the flash-driver guard.
- SMK code stays in board files and short `#if BOARD_SMK37` blocks.
- No stock firmware, dumps or disassembly in this repository; no local paths, port names, serial numbers or e-mail
  addresses in published files.
- The owner merges, pushes, tags and publishes releases.
