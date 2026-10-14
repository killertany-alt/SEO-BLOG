"""Static blog generator (flat folder, no subfolders).
Usage:  python build.py [site_url] [image_ext]
  python build.py https://seo-blog-nine.vercel.app          -> generated SVG illustrations
  python build.py https://seo-blog-nine.vercel.app jpg      -> uses your own photos named <image-name>.jpg
Edit articles in content.py.
"""
import sys, re, html, json
from content import POSTS, HOME
from content_extra import EXTRA
for _p in POSTS:
    _p['sections'] = _p['sections'] + EXTRA.get(_p['slug'], [])

SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://seo-blog-nine.vercel.app").rstrip("/")
EXT = sys.argv[2] if len(sys.argv) > 2 else "svg"
NAME = "AI Marketing Playbook"
E = html.escape

PALETTE = [("#7c5cff", "#00d4ff"), ("#ff5c8a", "#ffb35c"), ("#00e0a4", "#2f7bff"), ("#ffd35c", "#ff5c5c"), ("#5cf0ff", "#7c5cff")]
W = 'fill="#fff"'
S = 'stroke="#fff" fill="none" stroke-linecap="round" stroke-linejoin="round"'

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
        nodes = '<circle cx="250" cy="200" r="22" fill="#fff" opacity=".5"/><circle cx="950" cy="500" r="26" fill="#fff" opacity=".5"/><circle cx="930" cy="180" r="18" fill="#fff" opacity=".4"/><circle cx="270" cy="500" r="18" fill="#fff" opacity=".4"/>'
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
        heart = '<path d="M600 440 C540 395 520 355 545 325 C570 295 600 310 600 335 C600 310 630 295 655 325 C680 355 660 395 600 440 Z" fill="#fff" opacity=".9"/>'
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
    return ""

def svg_for(i, p):
    a, b = PALETTE[i % len(PALETTE)]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" role="img" aria-label="{E(p["alt"])}"><title>{E(p["alt"])}</title>'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'
            f'<rect width="1200" height="675" fill="url(#g)"/><circle cx="1080" cy="90" r="210" fill="#fff" opacity=".1"/><circle cx="90" cy="620" r="170" fill="#fff" opacity=".08"/>{icon(p["icon"])}</svg>')

CSS = """:root{--bg:#0b0b12;--card:#14141f;--text:#e8e8f0;--mute:#a3a3b8;--acc:#8f78ff;--line:#23233a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;line-height:1.75;font-size:17px}
a{color:var(--acc);text-decoration:underline;text-underline-offset:3px}a:hover{color:#b6a7ff}
header,footer{max-width:1100px;margin:auto;padding:24px 20px}
header{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
header a.logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.4rem;color:var(--text);text-decoration:none}
nav a{margin-left:18px;font-size:.95rem}
main{max-width:1100px;margin:auto;padding:0 20px 50px}
h1,h2,h3{font-family:'Syne',sans-serif;line-height:1.2}
.hero h1{font-size:clamp(2rem,5vw,3.2rem);margin:20px 0 10px}.hero p{color:var(--mute);max-width:760px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;margin:30px 0}
.card{background:var(--card);border-radius:16px;overflow:hidden;border:1px solid var(--line);transition:.2s}
.card:hover{transform:translateY(-4px);border-color:var(--acc)}
.card img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block}
.card div{padding:16px 18px 20px}.card h3{font-size:1.1rem;margin:0 0 8px}.card h3 a{color:var(--text);text-decoration:none}
.card p{color:var(--mute);font-size:.92rem;margin:0;line-height:1.6}
article{max-width:760px;margin:auto}article h1{font-size:clamp(1.8rem,4vw,2.6rem);margin:10px 0}
article h2{font-size:1.45rem;margin:2.2em 0 .5em}
article img{width:100%;height:auto;border-radius:16px;margin:16px 0}
article p{margin:0 0 1.1em}article ul{padding-left:1.2em}article li{margin:.5em 0}
.lead{font-size:1.15rem;color:#f1f1f8}
.meta{color:var(--mute);font-size:.9rem}.more{margin-top:46px;border-top:1px solid var(--line);padding-top:10px}.more li{margin:6px 0}
footer{color:var(--mute);font-size:.9rem;border-top:1px solid var(--line)}footer a{margin-right:14px;white-space:nowrap}
footer p{margin:.6em 0}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Syne:wght@700;800&display=swap" rel="stylesheet">'

def link(text):
    """Escape text and turn [[slug|anchor]] into internal links."""
    t = E(text)
    return re.sub(r"\[\[([a-z0-9-]+)\|([^\]]+)\]\]", lambda m: f'<a href="/{m.group(1)}.html">{m.group(2)}</a>', t)

def plain(text):
    return re.sub(r"\[\[[a-z0-9-]+\|([^\]]+)\]\]", r"\1", text)

def img_file(p): return f"{p['img']}.{EXT}"

def page(title, desc, path, body, og_img, extra=""):
    url = f"{SITE}/{path}"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}<link rel="stylesheet" href="/style.css">{extra}</head><body>
<header><a class="logo" href="/">{NAME}</a><nav><a href="/">Home</a><a href="/what-is-seo-beginners-guide.html">SEO basics</a><a href="/google-search-console-guide.html">Search Console guide</a></nav></header>
{body}
<footer><p><strong>All guides:</strong></p><p>{"".join(f'<a href="/{q["slug"]}.html">{E(q["title"].split(":")[0])}</a>' for q in POSTS)}</p><p>&copy; 2026 {NAME}. Built for an SEO learning project.</p></footer></body></html>"""

def faq_ld(pairs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}) + "</script>"

open("style.css", "w").write(CSS)
stats = []

for i, p in enumerate(POSTS):
    if EXT == "svg":
        open(img_file(p), "w").write(svg_for(i, p))
    related = [q for q in POSTS if q["slug"] != p["slug"]]
    j = i
    nxt = [POSTS[(j + k) % len(POSTS)] for k in (1, 2, 3)]
    body_html, pairs, words = "", [], len(p["intro"].split())
    for q, paras in p["sections"]:
        body_html += f"<h2>{E(q)}</h2>"
        ans = ""
        for para in paras:
            if isinstance(para, tuple):
                body_html += "<ul>" + "".join(f"<li>{link(x)}</li>" for x in para[1]) + "</ul>"
                words += sum(len(x.split()) for x in para[1])
            else:
                body_html += f"<p>{link(para)}</p>"
                words += len(plain(para).split())
                ans = ans or plain(para)
        pairs.append((q, ans))
    more = "".join(f'<li><a href="/{q["slug"]}.html">{E(q["title"])}</a></li>' for q in nxt)
    body = (f'<main><article><p class="meta"><a href="/">Home</a> / {E(p["title"])}</p><h1>{E(p["title"])}</h1>'
            f'<img src="/{img_file(p)}" width="1200" height="675" alt="{E(p["alt"])}">'
            f'<p class="lead">{link(p["intro"])}</p>{body_html}'
            f'<div class="more"><h2>What should you read next?</h2><ul>{more}</ul></div></article></main>')
    ld = ('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
          "description": p["desc"], "image": f"{SITE}/{img_file(p)}", "keywords": ", ".join([p["kw"]] + p["rel"]),
          "mainEntityOfPage": f"{SITE}/{p['slug']}.html", "author": {"@type": "Organization", "name": NAME}}) + "</script>") + faq_ld(pairs)
    open(f"{p['slug']}.html", "w").write(page(p["title"], p["desc"], f"{p['slug']}.html", body, img_file(p), ld))
    stats.append((p["slug"], len(p["title"]), len(p["desc"]), words))

cards = "".join(
    f'<div class="card"><a href="/{p["slug"]}.html"><img src="/{img_file(p)}" width="1200" height="675" alt="{E(p["alt"])}" loading="lazy"></a>'
    f'<div><h3><a href="/{p["slug"]}.html">{E(p["title"])}</a></h3><p>{E(p["desc"])}</p></div></div>' for p in POSTS)
faq_html = "".join(f"<h2>{E(q)}</h2><p>{link(a)}</p>" for q, a in HOME["faqs"])
home = (f'<main><section class="hero"><h1>{E(HOME["h1"])}</h1><p>{E(HOME["intro"])}</p></section>'
        f'<h2>What are the best digital marketing guides for beginners?</h2><div class="grid">{cards}</div><article>{faq_html}</article></main>')
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
