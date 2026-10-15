"""Static blog generator (flat folder, no subfolders).
Usage:  python build.py [site_url] [image_ext]
  python build.py https://seo-blog-nine.vercel.app          -> generated SVG illustrations
  python build.py https://seo-blog-nine.vercel.app jpg      -> uses your own photos named <image-name>.jpg
Edit articles in content.py.
"""
import sys, re, html, json
from content import POSTS, HOME
from content_extra import EXTRA
from content_inline import INLINE
for _p in POSTS:
    _p['sections'] = _p['sections'] + EXTRA.get(_p['slug'], [])

SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://seo-blog-nine.vercel.app").rstrip("/")
EXT = sys.argv[2] if len(sys.argv) > 2 else "svg"
NAME = "AI Marketing Playbook"
E = html.escape

PALETTE = [("#141118", "#3b2a17"), ("#0f1519", "#1f3a3d"), ("#1a1216", "#4a2530"), ("#12141c", "#2b3150"), ("#17140e", "#4d3d1c")]
W = 'fill="#ecd8a8"'
S = 'stroke="#ecd8a8" fill="none" stroke-linecap="round" stroke-linejoin="round"'

def icon(name):
    if name == "search":
        return f'<rect x="270" y="130" width="600" height="400" rx="26" {W} opacity=".18"/><rect x="310" y="175" width="300" height="26" rx="13" {W} opacity=".5"/><rect x="310" y="235" width="220" height="18" rx="9" {W} opacity=".3"/><rect x="310" y="290" width="260" height="18" rx="9" {W} opacity=".3"/><rect x="310" y="345" width="200" height="18" rx="9" {W} opacity=".3"/><circle cx="760" cy="360" r="105" {S} stroke-width="24"/><line x1="836" y1="436" x2="930" y2="530" {S} stroke-width="30"/>'
    if name == "tags":
        tags = [(230, 330, 190), (440, 330, 150), (610, 330, 230), (860, 330, 110), (290, 420, 160), (470, 420, 240), (730, 420, 190), (400, 510, 210), (630, 510, 150)]
        t = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="62" rx="31" {W} opacity="{0.22 + (i % 3) * 0.12:.2f}"/>' for i, (x, y, w) in enumerate(tags))
        return f'<rect x="220" y="140" width="760" height="100" rx="50" {W} opacity=".22"/><circle cx="290" cy="190" r="26" {S} stroke-width="9"/><line x1="309" y1="209" x2="326" y2="226" {S} stroke-width="9"/><rect x="360" y="178" width="360" height="24" rx="12" {W} opacity=".6"/>' + t
    if name == "checklist":
        rows = "".join(f'<circle cx="470" cy="{y}" r="34" {W} opacity=".3"/><polyline points="453,{y} 466,{y + 14} 490,{y - 16}" {S} stroke-width="11"/><rect x="535" y="{y - 14}" width="{w}" height="28" rx="14" {W} opacity=".5"/>' for y, w in [(235, 210), (335, 170), (435, 230)])
        return f'<rect x="380" y="90" width="440" height="500" rx="30" {W} opacity=".2"/><rect x="470" y="130" width="260" height="20" rx="10" {W} opacity=".4"/>' + rows + f'<circle cx="470" cy="520" r="34" {W} opacity=".3"/><rect x="535" y="506" width="140" height="28" rx="14" {W} opacity=".35"/>'
    if name == "chip":
        pins = "".join(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" {S} stroke-width="14" opacity=".7"/>' for x in (520, 600, 680) for y1, y2 in ((215, 245), (430, 460)))
        pins += "".join(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" {S} stroke-width="14" opacity=".7"/>' for y in (295, 340, 385) for x1, x2 in ((440, 470), (730, 760)))
        nodes = '<circle cx="250" cy="200" r="22" fill="#ecd8a8" opacity=".5"/><circle cx="950" cy="500" r="26" fill="#ecd8a8" opacity=".5"/><circle cx="930" cy="180" r="18" fill="#ecd8a8" opacity=".4"/><circle cx="270" cy="500" r="18" fill="#ecd8a8" opacity=".4"/>'
        links = f'<polyline points="250,200 440,295" {S} stroke-width="5" opacity=".5"/><polyline points="760,385 950,500" {S} stroke-width="5" opacity=".5"/><polyline points="730,295 930,180" {S} stroke-width="5" opacity=".5"/><polyline points="470,385 270,500" {S} stroke-width="5" opacity=".5"/>'
        return links + nodes + pins + f'<rect x="470" y="245" width="260" height="185" rx="32" {W} opacity=".28"/><circle cx="600" cy="338" r="48" {S} stroke-width="12"/><circle cx="600" cy="338" r="14" {W}/>'
    if name == "grid":
        out = ""
        for r in range(2):
            for c in range(3):
                x, y = 250 + c * 250, 140 + r * 230
                out += f'<rect x="{x}" y="{y}" width="210" height="190" rx="34" {W} opacity="{0.18 + 0.07 * (r * 3 + c) / 2:.2f}"/><circle cx="{x + 105}" cy="{y + 80}" r="36" {W} opacity=".55"/><rect x="{x + 45}" y="{y + 140}" width="120" height="16" rx="8" {W} opacity=".5"/>'
        return out
    if name == "pen":
        lines = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="20" rx="10" {W} opacity=".45"/>' for x, y, w in [(330, 250, 400), (330, 310, 360), (330, 370, 380), (330, 430, 250)])
        return f'<rect x="290" y="110" width="520" height="460" rx="30" {W} opacity=".2"/><rect x="330" y="150" width="280" height="40" rx="20" {W} opacity=".6"/>' + lines + f'<g transform="rotate(40 850 330)"><rect x="830" y="190" width="42" height="260" rx="10" {W}/><polygon points="830,450 872,450 851,505" {W} opacity=".8"/><rect x="830" y="190" width="42" height="40" rx="10" {W} opacity=".6"/></g>'
    if name == "bubbles":
        heart = '<path d="M600 440 C540 395 520 355 545 325 C570 295 600 310 600 335 C600 310 630 295 655 325 C680 355 660 395 600 440 Z" fill="#ecd8a8" opacity=".9"/>'
        return f'<rect x="240" y="150" width="400" height="250" rx="44" {W} opacity=".25"/><polygon points="300,400 290,470 370,400" {W} opacity=".25"/><rect x="520" y="260" width="440" height="280" rx="48" {W} opacity=".3"/><polygon points="880,540 920,610 840,540" {W} opacity=".3"/>' + f'<g transform="translate(0,-5)">{heart}</g><rect x="290" y="210" width="260" height="22" rx="11" {W} opacity=".6"/><rect x="290" y="260" width="200" height="22" rx="11" {W} opacity=".4"/>'
    if name == "chart":
        bars = "".join(f'<rect x="{x}" y="{560 - h}" width="90" height="{h}" rx="14" {W} opacity="{o}"/>' for x, h, o in [(260, 150, .3), (400, 210, .35), (540, 290, .4), (680, 340, .45), (820, 420, .55)])
        return f'<rect x="210" y="100" width="780" height="500" rx="34" {W} opacity=".12"/>' + bars + f'<polyline points="305,380 445,320 585,250 725,215 865,130" {S} stroke-width="14"/><circle cx="865" cy="130" r="22" {W}/>'
    if name == "gauge":
        return f'<path d="M280 470 A320 320 0 0 1 920 470" {S} stroke-width="44" opacity=".35"/><path d="M280 470 A320 320 0 0 1 760 205" {S} stroke-width="44"/><line x1="600" y1="470" x2="790" y2="300" {S} stroke-width="22"/><circle cx="600" cy="470" r="44" {W}/><rect x="440" y="540" width="320" height="26" rx="13" {W} opacity=".5"/>'
    if name == "rocket":
        cloud = f'<g {W} opacity=".28"><circle cx="360" cy="500" r="80"/><circle cx="470" cy="470" r="105"/><circle cx="610" cy="500" r="85"/><circle cx="720" cy="520" r="65"/><rect x="300" y="500" width="470" height="85" rx="40"/></g>'
        rocket = f'<g transform="rotate(35 860 260)"><ellipse cx="860" cy="260" rx="55" ry="130" {W}/><polygon points="805,320 740,400 810,375" {W} opacity=".8"/><polygon points="915,320 980,400 910,375" {W} opacity=".8"/><circle cx="860" cy="225" r="26" fill="#7c5cff" opacity=".6"/><polygon points="835,385 885,385 860,470" {W} opacity=".55"/></g>'
        arrow = f'<line x1="520" y1="470" x2="520" y2="330" {S} stroke-width="22"/><polyline points="465,370 520,315 575,370" {S} stroke-width="22"/>'
        return cloud + arrow + rocket
    if name == "nodes":
        pts = [(600,340),(330,200),(870,200),(300,480),(900,490),(600,560)]
        ln = "".join(f'<line x1="600" y1="340" x2="{x}" y2="{y}" {S} stroke-width="8" opacity=".55"/>' for x, y in pts[1:])
        dots = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" {W} opacity="{o}"/>' for (x, y), r, o in zip(pts, (70, 45, 45, 40, 50, 38), (.6, .4, .4, .35, .4, .35)))
        return ln + dots
    if name == "bulb":
        rays = "".join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {S} stroke-width="14" opacity=".6"/>' for x1, y1, x2, y2 in [(600,70,600,120),(400,130,435,165),(800,130,765,165),(310,290,360,290),(890,290,840,290)])
        return rays + f'<circle cx="600" cy="300" r="140" {W} opacity=".3"/><circle cx="600" cy="300" r="95" {W} opacity=".25"/><rect x="535" y="430" width="130" height="34" rx="14" {W} opacity=".6"/><rect x="550" y="478" width="100" height="30" rx="14" {W} opacity=".5"/><rect x="565" y="520" width="70" height="26" rx="13" {W} opacity=".45"/>'
    if name == "calendar":
        cells = "".join(f'<rect x="{370 + c * 110}" y="{290 + r * 90}" width="80" height="62" rx="14" {W} opacity="{0.7 if (r, c) in ((0, 2), (1, 4), (2, 1)) else 0.25}"/>' for r in range(3) for c in range(5))
        return f'<rect x="310" y="120" width="580" height="450" rx="36" {W} opacity=".2"/><rect x="310" y="120" width="580" height="110" rx="36" {W} opacity=".35"/><rect x="400" y="80" width="26" height="80" rx="13" {W}/><rect x="780" y="80" width="26" height="80" rx="13" {W}/>' + cells
    if name == "phone":
        return f'<rect x="460" y="70" width="280" height="540" rx="50" {W} opacity=".28"/><rect x="490" y="120" width="220" height="410" rx="28" {W} opacity=".2"/><rect x="515" y="150" width="170" height="90" rx="16" {W} opacity=".5"/><rect x="515" y="262" width="170" height="18" rx="9" {W} opacity=".5"/><rect x="515" y="302" width="130" height="18" rx="9" {W} opacity=".35"/><rect x="515" y="342" width="150" height="18" rx="9" {W} opacity=".35"/><rect x="515" y="400" width="170" height="90" rx="16" {W} opacity=".4"/><rect x="555" y="565" width="90" height="12" rx="6" {W} opacity=".7"/>'
    return ""

def svg_for(i, p):
    return svg_make(i, p["icon"], p["alt"])

def svg_make(i, icon_name, alt):
    a, b = PALETTE[i % len(PALETTE)]
    p = {"alt": alt, "icon": icon_name}
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" role="img" aria-label="{E(p["alt"])}"><title>{E(p["alt"])}</title>'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'
            f'<rect width="1200" height="675" fill="url(#g)"/><circle cx="1080" cy="90" r="210" fill="#d4b06a" opacity=".08"/><circle cx="90" cy="620" r="170" fill="#d4b06a" opacity=".06"/>{icon(p["icon"])}</svg>')

CSS = """:root{--ink:#0d0c0f;--panel:#15131a;--rule:#2b2731;--bone:#efe9de;--mute:#a8a29a;--gold:#d4b06a;--gold-soft:#ecd8a8}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--bone);font:400 18px/1.75 'DM Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--gold);text-underline-offset:4px;text-decoration-thickness:1px}
a:hover{color:var(--gold-soft)}
:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:2px}
img{max-width:100%}
h1,h2,h3{font-family:'Instrument Serif',Georgia,serif;font-weight:400;margin:0}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(20px,4vw,48px)}
.progress{position:fixed;top:0;left:0;width:100%;height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;z-index:50}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:12px 28px;flex-wrap:wrap;padding-top:28px;padding-bottom:28px}
.brand{font-family:'Instrument Serif',Georgia,serif;font-size:1.9rem;line-height:1;color:var(--bone);text-decoration:none;letter-spacing:-.01em}
.top nav a{color:var(--mute);text-decoration:none;margin-right:26px;font-size:.95rem}
.top nav a:last-child{margin-right:0}
.top nav a:hover{color:var(--bone)}
@keyframes rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
.hero{padding:clamp(24px,5vw,72px) 0 clamp(24px,4vw,56px)}
.hero h1{font-size:clamp(3.3rem,9.5vw,8.4rem);line-height:.92;letter-spacing:-.025em;max-width:11ch;animation:rise .9s cubic-bezier(.2,.7,.2,1) both}
.cover{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);gap:clamp(24px,4vw,64px);margin-top:clamp(32px,5vw,64px);align-items:end}
.cover-img{display:block;overflow:hidden;border-radius:6px}
.cover-img img{width:100%;height:auto;display:block;border-radius:6px}
.lead{font-size:1.2rem;line-height:1.65;color:var(--bone);margin:0 0 1.2em}
.note{color:var(--mute);font-size:.98rem;margin:0}
.section-title{font-size:clamp(2rem,4vw,3rem);line-height:1.05;letter-spacing:-.01em;max-width:22ch;margin:clamp(40px,6vw,88px) 0 28px}
.guides{border-bottom:1px solid var(--rule)}
.guide{position:relative;display:grid;grid-template-columns:240px minmax(0,1fr) auto;gap:8px 36px;align-items:center;padding:28px 0;border-top:1px solid var(--rule)}
.guide-img{display:block;overflow:hidden;border-radius:4px}
.guide-img img{width:100%;height:auto;display:block;transition:transform .5s ease}
.guide:hover .guide-img img{transform:scale(1.04)}
.guide h3{font-size:clamp(1.6rem,2.6vw,2.15rem);line-height:1.1;letter-spacing:-.01em}
.guide h3 a{color:var(--bone);text-decoration:none}
.guide h3 a::after{content:"";position:absolute;inset:0}
.guide:hover h3 a{color:var(--gold)}
.guide p{margin:.5em 0 0;color:var(--mute);font-size:.98rem;line-height:1.6;max-width:62ch}
.guide .time{color:var(--mute);font-size:.9rem;white-space:nowrap}
.faqs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px;margin:8px 0 0}
.faqs h3{font-size:1.55rem;line-height:1.15;margin-bottom:.5em}
.faqs p{color:var(--mute);margin:0;font-size:1rem;line-height:1.7}
.art-head{padding:clamp(16px,3vw,40px) 0 28px;max-width:980px}
.crumb{color:var(--mute);font-size:.9rem;margin:0 0 20px}
.crumb a{color:var(--mute)}
.art-head h1{font-size:clamp(2.6rem,6.2vw,5.2rem);line-height:.98;letter-spacing:-.02em;animation:rise .8s cubic-bezier(.2,.7,.2,1) both}
.meta{color:var(--mute);font-size:.95rem;margin:20px 0 0}
.art-cover{display:block;width:100%;height:auto;border-radius:6px}
.art{display:grid;grid-template-columns:230px minmax(0,680px);gap:clamp(32px,6vw,88px);margin-top:clamp(32px,5vw,64px);justify-content:center}
.toc{position:sticky;top:28px;align-self:start;font-size:.93rem}
.toc summary{cursor:pointer;color:var(--bone);font-family:'Instrument Serif',Georgia,serif;font-size:1.35rem;margin-bottom:12px}
.toc ul{list-style:none;margin:0;padding:0;border-left:1px solid var(--rule)}
.toc li{margin:0}
.toc a{display:block;padding:5px 0 5px 16px;color:var(--mute);text-decoration:none;line-height:1.4}
.toc a:hover{color:var(--gold)}
.body .standfirst{font-family:'Instrument Serif',Georgia,serif;font-size:clamp(1.5rem,2.4vw,1.9rem);line-height:1.35;color:var(--bone);margin:0 0 1.4em}
.body h2{font-size:clamp(1.8rem,3vw,2.3rem);line-height:1.1;letter-spacing:-.01em;margin:2.1em 0 .55em;scroll-margin-top:24px}
.body p{margin:0 0 1.15em;color:#ddd7cc}
.body ul{padding-left:1.1em;margin:0 0 1.3em;color:#ddd7cc}
.body li{margin:.55em 0;padding-left:.3em}
.body li::marker{color:var(--gold)}
.body figure{margin:2.4em 0}
.body figure img{display:block;width:100%;height:auto;border-radius:6px}
.more{margin-top:clamp(56px,8vw,112px)}
.foot{margin-top:clamp(56px,8vw,112px);border-top:1px solid var(--rule);padding-top:40px;padding-bottom:48px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:32px}
.foot .brand{font-size:1.6rem}
.foot p{color:var(--mute);font-size:.92rem;margin:.5em 0 0}
.foot ul{list-style:none;margin:0;padding:0;columns:2;column-gap:32px;font-size:.95rem}
.foot li{margin:0 0 .5em;break-inside:avoid}
.foot a{color:var(--mute);text-decoration:none}
.foot a:hover{color:var(--gold)}
@media (min-width:1100px){.body figure{margin-left:-56px;margin-right:-56px}}
@media (max-width:999px){.art{grid-template-columns:minmax(0,1fr)}.toc{position:static;border-bottom:1px solid var(--rule);padding-bottom:16px}.cover{grid-template-columns:minmax(0,1fr)}.faqs{grid-template-columns:minmax(0,1fr)}}
@media (max-width:720px){body{font-size:17px}.guide{grid-template-columns:minmax(0,1fr)}.guide .time{margin-top:6px}.foot{grid-template-columns:minmax(0,1fr)}.foot ul{columns:1}.top nav a{margin-right:18px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.hero h1,.art-head h1{animation:none}.guide-img img{transition:none}}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'

SCRIPT = "<script>(function(){var b=document.querySelector('.progress');if(b){var f=function(){var h=document.documentElement,m=h.scrollHeight-h.clientHeight;b.style.transform='scaleX('+(m>0?h.scrollTop/m:0)+')'};addEventListener('scroll',f,{passive:true});f()}var t=document.querySelector('.toc');if(t&&matchMedia('(min-width:1000px)').matches)t.open=true})();</script>"

def link(text):
    """Escape text and turn [[slug|anchor]] into internal links."""
    t = E(text)
    return re.sub(r"\[\[([a-z0-9-]+)\|([^\]]+)\]\]", lambda m: f'<a href="/{m.group(1)}.html">{m.group(2)}</a>', t)

def plain(text):
    return re.sub(r"\[\[[a-z0-9-]+\|([^\]]+)\]\]", r"\1", text)

def img_file(p): return f"{p['img']}.{EXT}"

def slugify(q): return re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")[:60]

def count_words(p):
    n = len(p["intro"].split())
    for q, paras in p["sections"]:
        for para in paras:
            n += sum(len(x.split()) for x in para[1]) if isinstance(para, tuple) else len(plain(para).split())
    return n

for _p in POSTS: _p["words"] = count_words(_p); _p["mins"] = max(1, round(_p["words"] / 200))

def page(title, desc, path, body, og_img, extra="", progress=False):
    url = f"{SITE}/{path}"
    foot_links = "".join(f'<li><a href="/{q["slug"]}.html">{E(q["title"])}</a></li>' for q in POSTS)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0d0c0f">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}<link rel="stylesheet" href="/style.css">{extra}</head><body>
{'<div class="progress" aria-hidden="true"></div>' if progress else ''}
<div class="wrap top"><a class="brand" href="/">{NAME}</a><nav aria-label="Main"><a href="/#guides">All guides</a><a href="/what-is-seo-beginners-guide.html">SEO basics</a><a href="/google-search-console-guide.html">Search Console guide</a></nav></div>
{body}
<footer class="wrap foot"><div><a class="brand" href="/">{NAME}</a><p>Plain-language guides to SEO, AI tools and getting a website found.</p><p>&copy; 2026 {NAME}</p></div><ul>{foot_links}</ul></footer>{SCRIPT}</body></html>"""

def faq_ld(pairs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}) + "</script>"

def guide_row(p, lazy=True):
    return (f'<div class="guide"><a class="guide-img" href="/{p["slug"]}.html" tabindex="-1"><img src="/{img_file(p)}" width="1200" height="675" alt="{E(p["alt"])}"{" loading=lazy" if lazy else ""}></a>'
            f'<div><h3><a href="/{p["slug"]}.html">{E(p["title"])}</a></h3><p>{E(p["desc"])}</p></div><span class="time">{p["mins"]} min read</span></div>')

open("style.css", "w").write(CSS)
stats = []

for i, p in enumerate(POSTS):
    if EXT == "svg":
        open(img_file(p), "w").write(svg_for(i, p))
    nxt = [POSTS[(i + k) % len(POSTS)] for k in (1, 2, 3)]
    body_html, pairs, toc = "", [], []
    inl = {x[0]: x for x in INLINE.get(p["slug"], [])}
    for si, (q, paras) in enumerate(p["sections"]):
        hid = slugify(q)
        toc.append((hid, q))
        body_html += f'<h2 id="{hid}">{E(q)}</h2>'
        ans = ""
        for para in paras:
            if isinstance(para, tuple):
                body_html += "<ul>" + "".join(f"<li>{link(x)}</li>" for x in para[1]) + "</ul>"
            else:
                body_html += f"<p>{link(para)}</p>"
                ans = ans or plain(para)
        pairs.append((q, ans))
        if si in inl:
            _, ic, fn, al = inl[si]
            if EXT == "svg":
                open(f"{fn}.svg", "w").write(svg_make(i + si + 2, ic, al))
            body_html += f'<figure><img src="/{fn}.{EXT}" width="1200" height="675" alt="{E(al)}" loading="lazy"></figure>'
    toc_html = "".join(f'<li><a href="#{h}">{E(q)}</a></li>' for h, q in toc)
    body = (f'<main class="wrap"><div class="art-head"><p class="crumb"><a href="/">Home</a> / {E(p["title"])}</p><h1>{E(p["title"])}</h1><p class="meta">{p["mins"]} min read</p></div>'
            f'<img class="art-cover" src="/{img_file(p)}" width="1200" height="675" alt="{E(p["alt"])}">'
            f'<div class="art"><aside><details class="toc"><summary>In this guide</summary><ul>{toc_html}</ul></details></aside>'
            f'<article class="body"><p class="standfirst">{link(p["intro"])}</p>{body_html}</article></div>'
            f'<section class="more"><h2 class="section-title">What should you read next?</h2><div class="guides">{"".join(guide_row(q) for q in nxt)}</div></section></main>')
    ld = ('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
          "description": p["desc"], "image": f"{SITE}/{img_file(p)}", "keywords": ", ".join([p["kw"]] + p["rel"]),
          "mainEntityOfPage": f"{SITE}/{p['slug']}.html", "author": {"@type": "Organization", "name": NAME}}) + "</script>") + faq_ld(pairs)
    open(f"{p['slug']}.html", "w").write(page(p["title"], p["desc"], f"{p['slug']}.html", body, img_file(p), ld, progress=True))
    stats.append((p["slug"], len(p["title"]), len(p["desc"]), p["words"]))

f0 = POSTS[0]
faq_html = "".join(f"<div><h3>{E(q)}</h3><p>{link(a)}</p></div>" for q, a in HOME["faqs"])
home = (f'<main class="wrap"><section class="hero"><h1>{E(HOME["h1"])}</h1>'
        f'<div class="cover"><a class="cover-img" href="/{f0["slug"]}.html" tabindex="-1"><img src="/{img_file(f0)}" width="1200" height="675" alt="{E(f0["alt"])}"></a>'
        f'<div><p class="lead">{E(HOME["intro"])}</p><p class="note">New to this? Read <a href="/{f0["slug"]}.html">{E(f0["title"])}</a> first.</p></div></div></section>'
        f'<section id="guides"><h2 class="section-title">What are the best digital marketing guides for beginners?</h2><div class="guides">{"".join(guide_row(p) for p in POSTS)}</div></section>'
        f'<section><h2 class="section-title">Common questions from new marketers</h2><div class="faqs">{faq_html}</div></section></main>')
home_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/"}) + "</script>" + faq_ld([(q, plain(a)) for q, a in HOME["faqs"]])
open("index.html", "w").write(page(HOME["title"], HOME["desc"], "", home, img_file(POSTS[0]), home_ld))
stats.append(("index", len(HOME["title"]), len(HOME["desc"]), len(HOME["intro"].split())))

urls = [""] + [f"{p['slug']}.html" for p in POSTS]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"<url><loc>{SITE}/{u}</loc></url>" for u in urls) + "\n</urlset>")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

print(f"{'page':48}{'title':>6}{'desc':>6}{'words':>7}")
for s in stats:
    flag = "" if (s[1] <= 60 and 140 <= s[2] <= 160) else "  <-- CHECK"
    print(f"{s[0]:48}{s[1]:>6}{s[2]:>6}{s[3]:>7}{flag}")
