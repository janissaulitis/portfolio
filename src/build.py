"""Builds the two front doors of the portfolio from one source.

    index.html           sports part first  (the original link)
    business/index.html  business part first

Run:  python3 src/build.py   (from the repo root)
"""
from pathlib import Path

SRC = Path(__file__).parent
ROOT = SRC.parent
read = lambda n: (SRC / n).read_text(encoding="utf-8")

SITE = "https://janis-saulitis-portfolio.netlify.app/"
GO = '<svg class="go" viewBox="0 0 14 14" aria-hidden="true"><path d="M5 2.5 9.5 7 5 11.5"/></svg>'
CARET = '<svg class="caret" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5"/></svg>'

PARTS = {
    "business": dict(
        title="For any business", short="Business", count="6 tools",
        lede="Office work that eats the week: books, customer emails, document checks, risk calls, and where AI is worth it in the first place.",
        door="Books, customer emails, loan checks, AI costs",
        groups=[("ai-plan", "Where AI pays", "2 tools"), ("back-office", "Back office", "2 tools"), ("lending", "Lending", "2 tools")],
        html=lambda: read("business.html")),
    "sports": dict(
        title="For live sports production", short="Sports", count="6 tools",
        lede="Built for the people who put tennis and basketball on screen: quotes, crew plans, finish times, captions and client reports.",
        door="Quotes, crew plans, finish times, captions, reports",
        groups=[("sales", "Sales", "1 tool"), ("planning", "Planning the day", "3 tools"), ("data", "Data & graphics", "2 tools")],
        html=lambda: read("sales.html") + "\n" + read("planning.html") + "\n" + read("data.html")),
}

INTRO = {
    "sports": dict(h1="Working tools for live sports production and everyday business, built by directing AI",
                   desc="Twelve working tools built by directing AI: six for live sports production (quotes, crew plans, finish times, captions, client reports) and six for any business (bookkeeping, customer emails, loan checks, AI costs). Each with a demo video and real test results."),
    "business": dict(h1="Working AI tools for everyday business, from the back office to lending",
                     desc="Twelve working tools built by directing AI: six for any business (bookkeeping, customer emails, loan checks, risk calls, AI costs) and six for live sports production. Each with a demo video and real test results."),
}

EXTRA_CSS = """
/* sticky top bar */
.bar { position: sticky; top: 0; z-index: 40; padding-block: 14px; border-bottom: 1px solid transparent; transition: border-color .2s }
.bar.stuck { border-bottom-color: var(--line) }
.group, .proj { scroll-margin-top: 84px }

/* two parts: business and sports */
.bar nav .links { align-items: center }
.dd { position: relative; display: inline-flex }
.dd > button { all: unset; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; color: var(--muted); font-size: 14px }
.dd > button:hover, .dd > button[aria-expanded="true"] { color: var(--fg) }
.dd > button:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; border-radius: 4px }
.caret { width: 12px; height: 12px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; transition: transform .15s }
.dd > button[aria-expanded="true"] .caret { transform: rotate(180deg) }
.dd-menu { position: absolute; top: calc(100% + 12px); left: -14px; min-width: 230px; display: grid; background: var(--surface); border: 1px solid var(--line); border-top: 3px solid var(--tag); border-radius: 4px 4px 10px 10px; padding: 6px 0; box-shadow: 0 18px 40px rgba(0,0,0,.25); z-index: 30 }
.dd-menu[hidden] { display: none }
.bar nav .dd-menu a { display: flex; justify-content: space-between; gap: 16px; padding: 10px 14px; color: var(--fg); font-weight: 500 }
.bar nav .dd-menu a:hover { background: var(--bg) }
.dd-menu a .c, .jump .sub .c { font: 500 11px/1.4 var(--mono); color: var(--muted); text-transform: uppercase; letter-spacing: .06em }
.dd-menu .all { border-bottom: 1px solid var(--line); margin-bottom: 4px }
.bar .jump .sub { padding-left: 56px; font-weight: 500; font-size: 14px; color: var(--muted) }
.bar .jump .sub + .sub { border-top: 0 }

.doors { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 12px; margin: 6px 0 4px }
.door { display: grid; gap: 6px; align-content: start; text-decoration: none; color: var(--fg); background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 6px; padding: 16px 18px; transition: border-color .15s, transform .15s }
.door + .door { border-left-color: var(--tag) }
.door:hover { border-color: var(--accent); transform: translateY(-1px) }
.door + .door:hover { border-color: var(--tag) }
.door .t { font: 700 24px/1.05 var(--display); text-transform: uppercase; letter-spacing: .02em }
.door .d { font-size: 14.5px; color: var(--muted); line-height: 1.4 }
.door .go2 { font: 600 13px/1 var(--body); color: var(--accent); margin-top: 6px }
.door + .door .go2 { color: var(--tag-ink) }
.door .n { font: 500 11px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }

.part { scroll-margin-top: 76px; padding-top: 34px }
.part-head { display: grid; gap: 8px; padding: 22px 24px; border-radius: 8px; background: var(--strap); color: var(--strap-fg); margin-bottom: 4px }
.part-head .n { font: 500 12px/1 var(--mono); letter-spacing: .1em; text-transform: uppercase; color: var(--tag) }
.part-head h2 { margin: 0; font: 700 clamp(30px, 3.6vw, 42px)/1 var(--display); text-transform: uppercase; letter-spacing: .02em }
.part-head p { margin: 0; max-width: 68ch; opacity: .85 }
.part-head .subnav { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px }
.part-head .subnav a { color: var(--strap-fg); text-decoration: none; border: 1px solid rgba(255,255,255,.28); border-radius: 999px; padding: 4px 12px; font-size: 13.5px }
.part-head .subnav a:hover { border-color: var(--tag); color: var(--tag) }
.part .group:first-of-type { border-top: 0 }
@media (max-width: 820px) { .doors { grid-template-columns: minmax(0,1fr) } .part-head { padding: 18px } }
"""

EXTRA_JS = """
  const bar = document.querySelector(".bar");
  const stick = () => bar.classList.toggle("stuck", scrollY > 8);
  addEventListener("scroll", stick, { passive: true }); stick();
  // top-bar dropdowns (Business / Sports)
  const dds = [...document.querySelectorAll(".dd")];
  const shut = except => dds.forEach(d => { if (d !== except) { d.querySelector("button").setAttribute("aria-expanded", "false"); d.querySelector(".dd-menu").hidden = true; } });
  dds.forEach(d => {
    const b = d.querySelector("button"), m = d.querySelector(".dd-menu");
    b.addEventListener("click", e => { e.stopPropagation(); const open = m.hidden; shut(d); m.hidden = !open; b.setAttribute("aria-expanded", String(open)); });
    m.addEventListener("click", e => { if (e.target.closest("a")) shut(); });
  });
  document.addEventListener("click", e => { if (!e.target.closest(".dd")) shut(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") shut(); });
"""


def dropdown(key):
    p = PARTS[key]
    items = f'<a class="all" href="#{key}">All {p["short"].lower()} tools <span class="c">{p["count"]}</span></a>' + "".join(
        f'<a href="#{gid}">{name.replace("&", "&amp;")} <span class="c">{c}</span></a>' for gid, name, c in p["groups"])
    return (f'<span class="dd"><button type="button" aria-expanded="false" aria-controls="dd-{key}">{p["short"]}{CARET}</button>'
            f'<span class="dd-menu" id="dd-{key}" hidden>{items}</span></span>')


def jump(order):
    rows, n = [], 0
    for key in order:
        n += 1; p = PARTS[key]
        rows.append(f'<a href="#{key}"><span class="n">{n:02d}</span><span>{p["title"]}</span><span class="c">{p["count"]}</span>{GO}</a>')
        rows += [f'<a class="sub" href="#{gid}"><span></span><span>{name.replace("&", "&amp;")}</span><span class="c">{c}</span>{GO}</a>'
                 for gid, name, c in p["groups"]]
    for href, label, c in [("#other", "Web design", "concept"), ("#how", "How I work", "8 steps"), ("#contact", "Contact", "")]:
        n += 1
        rows.append(f'<a href="{href}"><span class="n">{n:02d}</span><span>{label}</span><span class="c">{c}</span>{GO}</a>')
    return '<nav class="jump" id="jump" aria-label="Sections" hidden>' + "".join(rows) + "</nav>"


def part(key, n):
    p = PARTS[key]
    sub = "".join(f'<a href="#{gid}">{name.replace("&", "&amp;")}</a>' for gid, name, _ in p["groups"])
    return (f'  <section class="part" id="{key}">\n    <div class="part-head"><span class="n">Part {n} · {p["count"]}</span>'
            f'<h2>{p["title"]}</h2><p>{p["lede"]}</p><nav class="subnav" aria-label="{p["short"]} groups">{sub}</nav></div>\n'
            + p["html"]() + "  </section>\n")


def doors(order):
    out = []
    for key in order:
        p = PARTS[key]
        out.append(f'<a class="door" href="#{key}"><span class="n">{p["count"]}</span><span class="t">{p["title"]}</span>'
                   f'<span class="d">{p["door"]}</span><span class="go2">See them ↓</span></a>')
    return '    <div class="doors">' + "".join(out) + "</div>\n"


def page(first):
    order = [first] + [k for k in PARTS if k != first]
    M = "" if first == "sports" else "../"
    url = SITE if first == "sports" else SITE + "business/"
    intro = INTRO[first]
    css = read("head_css.css") + EXTRA_CSS
    js = read("script.js").rstrip().rstrip("})();").rstrip() + "\n" + EXTRA_JS + "})();\n"
    links = (dropdown(order[0]) + dropdown(order[1]) +
             '<a href="#other">Web design</a><a href="#how">How I work</a><a href="#contact">Contact</a>')
    body = f"""<div class="wrap" id="top">
  <header class="bar">
    <a class="name" href="#top" aria-label="Jānis Saulītis, back to top"><svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><path class="rays" d="M16 3v4M5.4 7.9l2.8 2.8M26.6 7.9l-2.8 2.8M1.5 18.5h4M26.5 18.5h4"/><path class="disc" d="M7.5 22.5a8.5 8.5 0 0 1 17 0z"/><path class="ground" d="M2.5 26.5h27"/></svg><span>Jānis Saulītis</span></a>
    <nav>
      <span class="links">{links}</span>
      <button class="icon-btn" id="theme" type="button" aria-label="Switch to dark mode"><svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg><svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/></svg></button>
      <button class="icon-btn menu-btn" id="menu" type="button" aria-label="Sections" aria-expanded="false" aria-controls="jump"><svg class="i-bars" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="i-x" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
    </nav>
    {jump(order)}
  </header>

  <section class="intro">
    <div class="kicker">Portfolio · Riga · November 2026</div>
    <h1>{intro["h1"]}</h1>
    <ul class="facts">
      <li><b>12</b><span>working tools, each with a demo video</span></li>
      <li><b>11</b><span>live to try, free</span></li>
      <li><b>6</b><span>different AI builders</span></li>
      <li><b>50+</b><span>AI mistakes caught in testing</span></li>
    </ul>
{doors(order)}    <p class="note">All companies, people, tournaments and figures in the demos are invented.</p>
  </section>

{part(order[0], 1)}
{part(order[1], 2)}
{read("other.html")}
{read("how.html")}
{read("contact.html")}
  <footer>All companies, people, loans, tournaments, crew, prices and audience figures in these demos are invented. Built by directing AI tools: Claude Code, v0, Lovable, Replit, n8n with OpenAI, Google Apps Script, with Google Gemini inside two of the tools.</footer>
</div>
"""
    body = body.replace("{M}", M)
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>Jānis Saulītis · AI Builds</title>
<meta name="description" content="{intro["desc"]}">
<link rel="canonical" href="{url}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230e1211'/%3E%3Cpath d='M16 4v3.5M7 8.5l2.4 2.4M25 8.5l-2.4 2.4M3.5 18.5h3.5M25 18.5h3.5' stroke='%23f2c230' stroke-width='2.4' stroke-linecap='round'/%3E%3Cpath d='M8.5 22.5a7.5 7.5 0 0 1 15 0z' fill='%23f2c230'/%3E%3Cpath d='M4 26.5h24' stroke='%2339c48f' stroke-width='2.4' stroke-linecap='round'/%3E%3C/svg%3E">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="Jānis Saulītis · Working tools built by directing AI">
<meta property="og:description" content="{intro["desc"]}">
<meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}og.png">
<meta name="darkreader-lock">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<style>
{css}</style>
</head>
<body>

"""
    return head + body + f"\n<script>\n{js}</script>\n\n</body>\n</html>\n"


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page("sports"), encoding="utf-8")
    (ROOT / "business").mkdir(exist_ok=True)
    (ROOT / "business" / "index.html").write_text(page("business"), encoding="utf-8")
    print("built index.html and business/index.html")
