"""Static blog generator.
Usage:  python build.py                      -> uses SVG placeholder images
        python build.py jpg https://my-site.vercel.app   -> uses your own images/post-N.jpg and sets real URL
"""
import sys, os, html

EXT = sys.argv[1] if len(sys.argv) > 1 else "svg"
SITE = (sys.argv[2] if len(sys.argv) > 2 else "https://YOUR-SITE.vercel.app").rstrip("/")
NAME = "AI Marketing Playbook"
TAG = "Practical AI and digital marketing tips for beginners"

POSTS = [
 ("what-is-seo-beginners-guide", "What Is SEO? A Beginner's Guide for 2026",
  "Learn what SEO is, how search engines rank pages, and the first steps to get your website found on Google.",
  ["SEO (Search Engine Optimization) is the practice of making your website easy for search engines to find, understand and rank. When someone searches for something, Google picks the pages it believes are most helpful. SEO is how you earn that spot without paying for ads.",
   "Search engines work in three steps: crawling (bots discover your pages), indexing (they store and understand the content) and ranking (they order results by relevance and quality). If any step fails, your page will not show up.",
   "Start with the basics: a clear page title, a helpful meta description, headings that describe your content, fast loading, and original writing that answers a real question."]),
 ("keyword-research-for-beginners", "Keyword Research for Beginners: Find What People Search",
  "A simple process to find keywords your audience actually searches, using free tools.",
  ["Keywords are the words people type into Google. Keyword research means finding the ones that match your topic and that you realistically have a chance of ranking for.",
   "Begin with a seed topic, then use Google autocomplete, the People Also Ask box and free tools like Google Keyword Planner and Google Trends to collect related phrases. Prefer long-tail phrases such as 'best AI tools for small business' over broad ones such as 'AI'.",
   "For each keyword, check the search intent. Is the person trying to learn, compare or buy? Match your page to that intent and you will beat many bigger sites."]),
 ("on-page-seo-checklist", "On-Page SEO Checklist: 10 Things to Fix on Every Page",
  "A practical on-page SEO checklist covering titles, headings, images, links and more.",
  ["On-page SEO is everything you control inside your page. A short checklist applied to every post builds steady results.",
   "Check these: one H1 that contains your main keyword, a title under 60 characters, a meta description under 160, descriptive image alt text, short readable paragraphs, internal links to related posts, a clean URL, and a mobile-friendly layout.",
   "Finish by reading the page out loud. If it does not answer the visitor's question quickly, rewrite the opening paragraph."]),
 ("how-ai-is-changing-digital-marketing", "How AI Is Changing Digital Marketing",
  "See how AI tools are changing content creation, ads, analytics and customer support for marketers.",
  ["AI has moved from buzzword to daily tool. Marketers use it to draft content, generate ad variations, analyse customer data and automate repetitive replies.",
   "The biggest gain is speed. A task that took a day, such as researching a topic and drafting an outline, now takes minutes. The human job shifts to strategy, taste and fact-checking.",
   "Treat AI as an assistant, not an author. Always review output, add your own experience and keep your brand voice consistent."]),
 ("best-free-ai-tools-for-content-creators", "Best Free AI Tools for Content Creators",
  "A shortlist of free AI tools for writing, design, video and research that save hours every week.",
  ["You do not need a big budget to use AI well. Many strong tools have free plans that are enough for a student or a small brand.",
   "For writing and research, use a general AI assistant. For design, try Canva's free tier. For video, look at free editors with auto-captions. For code and websites, AI studio tools can generate a full page from a prompt.",
   "Pick two or three tools and learn them properly instead of collecting dozens. Consistency beats variety."]),
 ("how-to-write-blog-posts-that-rank", "How to Write Blog Posts That Rank on Google",
  "A step by step method for writing blog posts that satisfy readers and search engines.",
  ["Great ranking posts start with a clear question. Decide who the reader is and what they want to know before you write a single line.",
   "Structure matters: a strong title, a short intro that gives the answer early, subheadings for each point, and a short conclusion with a next step. Use simple words and short sentences.",
   "After publishing, update the post every few months with fresh examples. Search engines reward pages that stay accurate."]),
 ("social-media-marketing-basics", "Social Media Marketing Basics for Small Businesses",
  "Learn how to choose platforms, plan content and measure results in social media marketing.",
  ["Social media marketing means using platforms to build awareness and trust. You do not need to be everywhere. Pick the one or two platforms where your customers already spend time.",
   "Plan content around three pillars: educate, entertain and sell. A simple weekly calendar of three to five posts is enough to start.",
   "Track reach, saves, shares and profile visits. Double down on the formats that perform and drop the ones that do not."]),
 ("google-search-console-guide", "Google Search Console: A Simple Setup Guide",
  "Step by step guide to adding your website to Google Search Console and submitting your sitemap.",
  ["Google Search Console is a free tool that shows how Google sees your site: which queries bring visitors, which pages are indexed and what errors exist.",
   "To set it up, add your site as a URL prefix property, verify ownership (an HTML tag or file works well on Vercel), then submit your sitemap.xml under the Sitemaps section.",
   "Check the Pages report for indexing problems and the Performance report for clicks and impressions. New sites can take days or weeks to appear, so be patient."]),
 ("website-speed-and-core-web-vitals", "Website Speed and Core Web Vitals Explained",
  "Understand Core Web Vitals and simple ways to make your website load faster.",
  ["Speed is a ranking and user experience factor. Core Web Vitals measure loading (LCP), interactivity (INP) and visual stability (CLS).",
   "Quick wins: compress images, use modern formats like WebP, avoid heavy scripts, set image width and height, and host on a fast network. Static sites on Vercel are fast by default.",
   "Test your pages with PageSpeed Insights and fix the biggest issue first. Small improvements add up."]),
 ("build-and-host-a-free-website-with-vercel", "Build and Host a Free Website with Vercel",
  "How to build a website with AI, push it to GitHub and publish it free on Vercel.",
  ["You can launch a real website in an afternoon at no cost. Generate the code with an AI tool, upload it to a GitHub repository and connect that repository to Vercel.",
   "Every time you push a change to GitHub, Vercel redeploys automatically. You also get a free HTTPS address ending in .vercel.app that you can submit to Google Search Console.",
   "If a deployment fails, open the build log, copy the error and paste it into an AI assistant. Most errors are small typos or missing files."]),
]

PALETTE = [("#7c5cff", "#00d4ff"), ("#ff5c8a", "#ffb35c"), ("#00e0a4", "#2f7bff"), ("#ffd35c", "#ff5c5c"), ("#5cf0ff", "#7c5cff")]

CSS = """:root{--bg:#0b0b12;--card:#14141f;--text:#e8e8f0;--mute:#9a9ab0;--acc:#7c5cff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;line-height:1.7}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
header,footer{max-width:1100px;margin:auto;padding:24px 20px}
header a.logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.4rem;color:var(--text)}
main{max-width:1100px;margin:auto;padding:0 20px 40px}
h1,h2{font-family:'Syne',sans-serif;line-height:1.2}
.hero h1{font-size:clamp(2rem,5vw,3.2rem);margin:20px 0 8px}.hero p{color:var(--mute);max-width:600px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;margin-top:30px}
.card{background:var(--card);border-radius:16px;overflow:hidden;border:1px solid #23233a;transition:.2s}
.card:hover{transform:translateY(-4px);border-color:var(--acc)}
.card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.card div{padding:16px 18px 20px}.card h2{font-size:1.1rem;margin:0 0 8px}.card h2 a{color:var(--text)}
.card p{color:var(--mute);font-size:.92rem;margin:0}
article{max-width:740px;margin:auto}article h1{font-size:clamp(1.8rem,4vw,2.6rem)}
article img{width:100%;border-radius:16px;margin:16px 0}article p{font-size:1.05rem}
.meta{color:var(--mute);font-size:.9rem}.more{margin-top:40px}.more li{margin:6px 0}
footer{color:var(--mute);font-size:.9rem;border-top:1px solid #23233a}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Syne:wght@700;800&display=swap" rel="stylesheet">'

def page(title, desc, path, body, og_img, extra=""):
    e = html.escape
    url = f"{SITE}/{path}"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}<link rel="stylesheet" href="/style.css">{extra}</head><body>
<header><a class="logo" href="/">{NAME}</a></header>
{body}
<footer>&copy; 2026 {NAME}. Built for an SEO learning project.</footer></body></html>"""

def svg(i, title):
    a, b = PALETTE[i % len(PALETTE)]
    words, lines, cur = title.split(), [], ""
    for w in words:
        if len(cur) + len(w) > 24: lines.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    lines.append(cur)
    t = "".join(f'<tspan x="60" dy="{0 if k == 0 else 62}">{html.escape(l)}</tspan>' for k, l in enumerate(lines[:4]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs><rect width="1200" height="675" fill="url(#g)"/><circle cx="1050" cy="120" r="220" fill="#fff" opacity=".1"/><text x="60" y="300" font-family="Arial,sans-serif" font-weight="800" font-size="54" fill="#fff">{t}</text></svg>'''



open("style.css", "w").write(CSS)

cards = ""
for i, (slug, title, desc, paras) in enumerate(POSTS, 1):
    img = f"post-{i}.{EXT}"
    if EXT == "svg": open(img, "w").write(svg(i - 1, title))
    cards += f'<div class="card"><a href="/{slug}.html"><img src="/{img}" alt="{html.escape(title)}" loading="lazy"></a><div><h2><a href="/{slug}.html">{html.escape(title)}</a></h2><p>{html.escape(desc)}</p></div></div>'
    others = "".join(f'<li><a href="/{s}.html">{html.escape(t)}</a></li>' for j, (s, t, _, _) in enumerate(POSTS) if j != i - 1 and abs(j - (i - 1)) <= 2)
    body = f'<main><article><p class="meta"><a href="/">Home</a> / Blog</p><h1>{html.escape(title)}</h1><img src="/{img}" alt="{html.escape(title)}">' + "".join(f"<p>{html.escape(p)}</p>" for p in paras) + f'<div class="more"><h2>Keep reading</h2><ul>{others}</ul></div></article></main>'
    ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{title}","description":"{desc}","image":"{SITE}/{img}","author":{{"@type":"Person","name":"{NAME}"}}}}</script>'
    open(f"{slug}.html", "w").write(page(f"{title} | {NAME}", desc, f"{slug}.html", body, img, ld))

home = f'<main><section class="hero"><h1>{NAME}</h1><p>{TAG}. Ten guides on SEO, content and AI tools.</p></section><div class="grid">{cards}</div></main>'
open("index.html", "w").write(page(f"{NAME} | {TAG}", f"{TAG}. Read 10 beginner friendly guides on SEO, content creation and AI tools.", "", home, f"post-1.{EXT}"))

urls = [""] + [f"{p[0]}.html" for p in POSTS]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"<url><loc>{SITE}/{u}</loc></url>" for u in urls) + "\n</urlset>")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("Built", len(POSTS), "posts")
