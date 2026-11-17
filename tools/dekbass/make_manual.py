#!/usr/bin/env python3
"""Build docs/manual/index.html, the designed DekBass manual, from docs/manual/{de,en,hi,or}.md.

One self-contained page: the four languages behind a switch (#de #en #hi #or), Konark wheels drawn as SVG.
Run from the repository root:  python3 tools/dekbass/make_manual.py
"""
import html
import math
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "docs" / "manual"
OUT = SRC / "index.html"

LANGS = [  # code, switch label, html lang, UI strings
    ("de", "Deutsch", "de", {"sub": "Handbuch · Firmware v1.0 für M-VAVE FM-1 und M-Vave SMK-37",
                             "toc": "Kapitel", "fig": "Vier Voices, vier Räder: V1 Kick 4 Schläge, V2 Snare 2 (Rotation 4), "
                             "V3 Perc 7, V4 FX 3. Breite Speichen = Achtel, schmale = Sechzehntel dazwischen.",
                             "foot": "DekBass ist freie Software unter GPL-3.0, aufgebaut auf Felucca."}),
    ("en", "English", "en", {"sub": "User manual · firmware v1.0 for the M-VAVE FM-1 and the M-Vave SMK-37",
                             "toc": "Chapters", "fig": "Four voices, four wheels: V1 kick 4 hits, V2 snare 2 (rotate 4), "
                             "V3 perc 7, V4 FX 3. Wide spokes = eighth notes, narrow = the sixteenths between.",
                             "foot": "DekBass is free software under GPL-3.0, built on Felucca."}),
    ("hi", "हिन्दी", "hi", {"sub": "यूज़र मैनुअल · M-VAVE FM-1 और M-Vave SMK-37 के लिए फ़र्मवेयर v1.0",
                           "toc": "अध्याय", "fig": "चार वॉइस, चार पहिए: V1 किक 4 हिट, V2 स्नेयर 2 (रोटेट 4), V3 पर्क 7, "
                           "V4 FX 3। चौड़ी तीलियाँ = आठवें नोट, पतली = बीच के सोलहवें नोट।",
                           "foot": "DekBass GPL-3.0 के तहत मुफ़्त सॉफ़्टवेयर है, Felucca पर आधारित।"}),
    ("or", "ଓଡ଼ିଆ", "or", {"sub": "ବ୍ୟବହାରକାରୀ ମାନୁଆଲ · M-VAVE FM-1 ଓ M-Vave SMK-37 ପାଇଁ ଫର୍ମୱେୟାର v1.0",
                         "toc": "ଅଧ୍ୟାୟ", "fig": "ଚାରୋଟି ଭଏସ, ଚାରୋଟି ଚକ: V1 କିକ 4 ହିଟ, V2 ସ୍ନେୟାର 2 (ରୋଟେଟ 4), V3 ପର୍କ 7, "
                         "V4 FX 3। ଚଉଡ଼ା ଅର = ଆଠ ଭାଗ, ପତଳା ଅର = ମଝିର ଷୋହଳ ଭାଗ।",
                         "foot": "DekBass GPL-3.0 ଅଧୀନରେ ମୁକ୍ତ ସଫ୍ଟୱେୟାର, Felucca ଉପରେ ଆଧାରିତ।"}),
]

VOICE = {1: "var(--red)", 2: "var(--ochre)", 3: "var(--indigo)", 4: "var(--grey)"}

# DekBass functions and the printed button names of both boards, shown as keycaps
KEYS = ["NOTE REPEAT", "KNOB BANK", "FADER BANK", "SEQ PLAY", "SEQ REC", "OCTAVE−", "OCTAVE+", "OCT−", "OCT+",
        "PLAY", "REC", "SEQ", "SHIFT", "PAGE", "BANK", "MENU", "DROP", "BUILD", "CUT", "FILL", "KONARK", "TEMPO",
        "PRESETS", "PRESET", "MASTER", "SELECT", "ALGORITHM", "HOME", "SAVE", "GLO", "GLOBE", "EDIT", "PARA", "ARP",
        "SEL", "SCALE", "PATCH", "CHORD", "BT", "FOCUS", "FOKUS"]
KEY_RE = re.compile(r"(?<![\w/−+-])(" + "|".join(re.escape(k) for k in sorted(KEYS, key=len, reverse=True))
                    + r")(?![\w−+-])")
VIEW_RE = re.compile(r"(?<![\w-])(BASS|EUCLID)(?![\w-])")
V_RE = re.compile(r"(?<![\w-])V([1-4])(?![\w])")


def euclid(k, n=16, rot=0):
    hits = [((i * k) % n) < k for i in range(n)] if k else [False] * n
    return hits[-rot:] + hits[:-rot] if rot else hits


def wheel(cx, cy, r, color, hits, spoke_w=1.0):
    """One Konark wheel: rim, hub, 16 spokes (wide on the eighths), lit where a step hits."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{3*spoke_w:.1f}" opacity=".9"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{r*0.18:.1f}" fill="var(--ink)" stroke="{color}" stroke-width="{2*spoke_w:.1f}"/>']
    for i in range(16):
        a = -math.pi / 2 + i * math.pi / 8
        x1, y1 = cx + math.cos(a) * r * 0.24, cy + math.sin(a) * r * 0.24
        x2, y2 = cx + math.cos(a) * r * 0.92, cy + math.sin(a) * r * 0.92
        w = (5.5 if i % 2 == 0 else 2.2) * spoke_w
        col = color if hits[i] else "var(--spoke)"
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" '
                   f'stroke-width="{w:.1f}" stroke-linecap="round"/>')
        if hits[i]:
            out.append(f'<circle cx="{cx + math.cos(a) * r:.1f}" cy="{cy + math.sin(a) * r:.1f}" r="{3.2*spoke_w:.1f}" fill="{color}"/>')
    return "".join(out)


PATTERNS = {1: euclid(4), 2: euclid(2, rot=4), 3: euclid(7), 4: euclid(3, rot=2)}


def hero_svg():
    """The Konark view: four concentric rings, one voice each, and a playhead."""
    c, parts = 200, []
    radii = [(150, 186), (112, 146), (74, 108), (40, 70)]
    for v, (ri, ro) in zip((1, 2, 3, 4), radii):
        parts.append(f'<circle cx="{c}" cy="{c}" r="{ro}" fill="none" stroke="{VOICE[v]}" stroke-width="2" opacity=".55"/>')
        for i in range(16):
            a = -math.pi / 2 + i * math.pi / 8
            on = PATTERNS[v][i]
            w = 7 if i % 2 == 0 else 3
            parts.append(f'<line x1="{c+math.cos(a)*ri:.1f}" y1="{c+math.sin(a)*ri:.1f}" x2="{c+math.cos(a)*(ro-4):.1f}" '
                         f'y2="{c+math.sin(a)*(ro-4):.1f}" stroke="{VOICE[v] if on else "var(--spoke)"}" stroke-width="{w}" '
                         f'stroke-linecap="round"/>')
    parts.append(f'<circle cx="{c}" cy="{c}" r="26" fill="var(--ink)" stroke="var(--grey)" stroke-width="2"/>')
    parts.append(f'<circle cx="{c}" cy="{c}" r="8" fill="var(--ochre)"/>')
    parts.append(f'<g class="playhead"><line x1="{c}" y1="{c-30}" x2="{c}" y2="{c-194}" stroke="var(--text)" '
                 f'stroke-width="2.5" stroke-linecap="round" opacity=".85"/></g>')
    return (f'<svg class="konark" viewBox="0 0 400 400" role="img" aria-label="Konark view: four voices as rings">'
            + "".join(parts) + "</svg>")


def figure_svg(caption):
    cells = []
    for idx, v in enumerate((1, 2, 3, 4)):
        cx, cy = 90 + (idx % 2) * 180, 84 + (idx // 2) * 196
        cells.append(wheel(cx, cy, 66, VOICE[v], PATTERNS[v]))
        cells.append(f'<text x="{cx}" y="{cy+98}" text-anchor="middle" class="vlabel" fill="{VOICE[v]}">V{v}</text>')
    return (f'<figure class="wheels"><svg viewBox="0 0 360 380" role="img" aria-label="{html.escape(caption)}">'
            + "".join(cells) + f'</svg><figcaption>{html.escape(caption)}</figcaption></figure>')


def decorate(fragment):
    """Keycaps, view pills and voice chips, only in text outside tags."""
    def text_sub(t):
        t = KEY_RE.sub(r'<kbd>\1</kbd>', t)
        t = VIEW_RE.sub(lambda m: f'<span class="view view-{m.group(1).lower()}">{m.group(1)}</span>', t)
        return V_RE.sub(lambda m: f'<span class="vchip v{m.group(1)}">V{m.group(1)}</span>', t)
    parts = re.split(r"(<[^>]+>)", fragment)
    in_heading = False
    for i, p in enumerate(parts):
        if p.startswith("<"):
            if re.match(r"<h[12]\b", p):
                in_heading = True
            elif re.match(r"</h[12]>", p):
                in_heading = False
            continue
        if not in_heading:
            parts[i] = text_sub(p)
    return "".join(parts)


def build_lang(code, ui):
    text = (SRC / f"{code}.md").read_text(encoding="utf-8")
    title_line, body_md = text.split("\n", 1)
    title = title_line.lstrip("# ").strip()
    body = markdown.markdown(body_md, extensions=["tables"])
    # chapters: id, big number, toc
    toc, n = [], 0

    def h2(m):
        nonlocal n
        n += 1
        label = re.sub(r"^\d+\.\s*", "", m.group(1))
        toc.append((n, label))
        return (f'<h2 id="{code}-{n}"><span class="num">{n:02d}</span>'
                f'<span class="ht">{label}</span></h2>')
    body = re.sub(r"<h2>(.*?)</h2>", h2, body)
    # tables scroll on their own on small screens
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    # first paragraph after the title = lead
    lead_m = re.match(r"\s*<p>(.*?)</p>", body, re.S)
    lead = lead_m.group(1) if lead_m else ""
    body = body[lead_m.end():] if lead_m else body
    body = decorate(body)
    # the wheels figure after the first table of chapter 7
    k = body.find(f'id="{code}-7"')
    t = body.find("</table></div>", k)
    if k >= 0 and t >= 0:
        t += len("</table></div>")
        body = body[:t] + figure_svg(ui["fig"]) + body[t:]
    toc_html = "".join(f'<li><a href="#{code}-{i}"><span class="tn">{i:02d}</span>{html.escape(l)}</a></li>' for i, l in toc)
    title_main = title.split("–")[0].strip()
    return f"""
<section class="lang" id="{code}" lang="{code}" data-lang="{code}">
  <header class="hero">
    <div class="hero-text">
      <p class="eyebrow">{html.escape(ui['sub'])}</p>
      <h1><span class="word">{html.escape(title_main.split()[0].upper())}</span><span class="board">{html.escape(' '.join(title_main.split()[1:]))} · SMK-37</span></h1>
      <p class="lead">{decorate(lead)}</p>
    </div>
    {hero_svg()}
  </header>
  <div class="layout">
    <nav class="toc" aria-label="{html.escape(ui['toc'])}"><p class="toc-h">{html.escape(ui['toc'])}</p><ol>{toc_html}</ol></nav>
    <article class="body">{body}
      <footer class="foot"><p>{html.escape(ui['foot'])} <a href="https://github.com/g0rst/DekBass-FM1">github.com/g0rst/DekBass-FM1</a></p></footer>
    </article>
  </div>
</section>"""


CSS = """
:root{
  /* DekBass: night sound-system poster. Black ground, the four voice colours, Konark wheel as the grid. */
  --ink:#0c0a08; --panel:#15110d; --line:#2b241c; --spoke:#2e2720;
  --text:#ece6db; --muted:#a39886;
  --red:#d2343e; --ochre:#d9a032; --indigo:#7c7ff0; --grey:#c8c8c8;
  --display:"Big Shoulders Display","Noto Sans Devanagari","Noto Sans Oriya",Impact,sans-serif;
  --body:"IBM Plex Sans","Noto Sans Devanagari","Noto Sans Oriya",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
  color-scheme:dark;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--text);font:16px/1.65 var(--body);
  background-image:radial-gradient(1200px 600px at 85% -10%,rgba(217,160,50,.10),transparent 60%),
                   radial-gradient(900px 500px at -10% 30%,rgba(124,127,240,.07),transparent 60%);}
a{color:var(--ochre)} a:focus-visible,button:focus-visible{outline:2px solid var(--ochre);outline-offset:3px}
.bar{position:sticky;top:0;z-index:5;display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:10px max(16px,4vw);background:rgba(12,10,8,.88);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.brand{font:900 22px/1 var(--display);letter-spacing:.06em;color:var(--text);text-decoration:none;display:flex;align-items:center;gap:10px}
.brand i{display:inline-flex;gap:3px}.brand i b{width:7px;height:18px;border-radius:2px}
.switch{display:flex;gap:4px;flex-wrap:wrap}
.switch a{font:600 14px/1 var(--body);color:var(--muted);text-decoration:none;padding:8px 12px;border:1px solid var(--line);border-radius:999px}
.switch a[aria-current="true"]{color:var(--ink);background:var(--ochre);border-color:var(--ochre)}
.lang{display:none;scroll-margin-top:120px}.lang.on{display:block}
.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:clamp(16px,4vw,56px);align-items:center;
  padding:clamp(28px,6vw,72px) max(16px,4vw) clamp(20px,4vw,40px);max-width:1240px;margin:0 auto}
.eyebrow{font:500 13px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ochre);margin:0 0 14px}
h1{margin:0;display:flex;flex-direction:column;gap:6px;text-wrap:balance}
h1 .word{font:900 clamp(56px,min(9.5vw,15vh),150px)/.86 var(--display);letter-spacing:.01em;
  background:linear-gradient(180deg,var(--text) 55%,var(--ochre));-webkit-background-clip:text;background-clip:text;color:transparent}
h1 .board{font:700 clamp(18px,2.6vw,28px)/1.1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.lead{max-width:58ch;color:var(--text);font-size:17px;margin:22px 0 0}
.konark{width:100%;max-width:420px;justify-self:center;filter:drop-shadow(0 0 40px rgba(217,160,50,.12))}
.playhead{transform-origin:200px 200px;animation:spin 8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.playhead{animation:none}html{scroll-behavior:auto}}
.layout{display:grid;grid-template-columns:230px minmax(0,1fr);gap:clamp(20px,4vw,56px);max-width:1240px;margin:0 auto;padding:0 max(16px,4vw) 80px}
.toc{position:sticky;top:70px;align-self:start;border-left:2px solid var(--line);padding-left:16px}
.toc-h{font:600 12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:6px 0 12px}
.toc ol{list-style:none;margin:0;padding:0;display:grid;gap:2px}
.toc a{display:flex;gap:10px;align-items:baseline;color:var(--text);text-decoration:none;padding:5px 0;font-size:14.5px;line-height:1.3}
.toc a:hover{color:var(--ochre)} .tn{font:600 12px var(--mono);color:var(--ochre);min-width:20px}
.body{max-width:76ch;min-width:0}
h2{display:flex;align-items:baseline;gap:16px;margin:64px 0 18px;padding-top:18px;border-top:1px solid var(--line);
  font:800 clamp(30px,4.2vw,44px)/1.05 var(--display);letter-spacing:.02em;text-wrap:balance;scroll-margin-top:70px}
h2 .num{font:900 .9em/1 var(--display);color:var(--ochre);min-width:1.4em}
.body > h2:first-child{margin-top:8px}
h3{font:700 15px/1.3 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ochre);margin:34px 0 10px}
p{margin:0 0 14px} strong{color:#fff;font-weight:600}
ul,ol{padding-left:1.25em;margin:0 0 16px} li{margin:4px 0} li::marker{color:var(--ochre)}
.body ol>li::marker{font-family:var(--mono);font-weight:600}
.tablewrap{overflow-x:auto;margin:6px 0 22px;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:14.5px;font-variant-numeric:tabular-nums}
th{text-align:left;font:600 12px/1.3 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ochre);
  padding:12px 14px;border-bottom:1px solid var(--line);background:#1b1611;white-space:nowrap}
td{padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0} tbody tr:nth-child(even) td{background:rgba(255,255,255,.015)}
kbd{font:600 .78em/1 var(--mono);letter-spacing:.03em;color:var(--text);background:#1f1913;border:1px solid #3a3026;
  border-bottom-width:3px;border-radius:5px;padding:3px 6px 2px;white-space:nowrap;display:inline-block}
.view{font:700 .76em/1 var(--mono);letter-spacing:.08em;padding:3px 7px;border-radius:999px;white-space:nowrap}
.view-bass{background:var(--ochre);color:var(--ink)} .view-euclid{background:var(--indigo);color:var(--ink)}
.vchip{font:700 .8em/1 var(--mono);padding:2px 6px;border-radius:4px;color:var(--ink);white-space:nowrap}
.v1{background:var(--red)}.v2{background:var(--ochre)}.v3{background:var(--indigo)}.v4{background:var(--grey)}
.wheels{margin:8px 0 26px;padding:18px;border:1px solid var(--line);border-radius:12px;background:var(--panel);display:grid;
  grid-template-columns:minmax(0,300px) 1fr;gap:20px;align-items:center}
.wheels svg{width:100%} .vlabel{font:900 22px var(--display)}
.wheels figcaption{color:var(--muted);font-size:14.5px}
.foot{margin-top:72px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:14px}
@media (max-width:860px){
  .hero{grid-template-columns:1fr}.konark{max-width:300px;order:-1}
  .layout{grid-template-columns:1fr}.toc{position:static;border-left:0;padding:0;border-top:1px solid var(--line);padding-top:14px}
  .toc ol{grid-template-columns:repeat(2,minmax(0,1fr));column-gap:16px}
  .wheels{grid-template-columns:1fr}
}
@media (max-width:480px){.toc ol{grid-template-columns:1fr}.switch{gap:3px}.switch a{padding:7px 8px;font-size:13px}.brand{font-size:18px}.brand i{display:none}}
"""

JS = """
(function(){
  var codes=["de","en","hi","or"];
  function pick(){
    var h=(location.hash||"").slice(1), code=h.split("-")[0];
    if(codes.indexOf(code)<0) code="de";
    codes.forEach(function(c){
      document.getElementById(c).classList.toggle("on",c===code);
      var a=document.querySelector('.switch a[href="#'+c+'"]'); if(a) a.setAttribute("aria-current",c===code?"true":"false");
    });
    document.documentElement.lang=code;
    if(h && h.indexOf("-")>0){var t=document.getElementById(h); if(t) t.scrollIntoView();}
    else window.scrollTo(0,0);
  }
  window.addEventListener("hashchange",pick); pick();
  window.addEventListener("load",function(){ if((location.hash||"").indexOf("-")<0) window.scrollTo(0,0); });
})();
"""


def main():
    sections = "".join(build_lang(c, ui) for c, _, _, ui in LANGS)
    switch = "".join(f'<a href="#{c}" lang="{hl}">{html.escape(lbl)}</a>' for c, lbl, hl, _ in LANGS)
    page = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DekBass Handbuch</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=Noto+Sans+Devanagari:wght@400;600;700&family=Noto+Sans+Oriya:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="bar">
  <a class="brand" href="#de"><i aria-hidden="true"><b style="background:var(--red)"></b><b style="background:var(--ochre)"></b><b style="background:var(--indigo)"></b><b style="background:var(--grey)"></b></i>DEKBASS</a>
  <nav class="switch" aria-label="Language">{switch}</nav>
</div>
{sections}
<script>{JS}</script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page)//1024} KB)")


if __name__ == "__main__":
    main()
