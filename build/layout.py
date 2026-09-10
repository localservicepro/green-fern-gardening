# -*- coding: utf-8 -*-
"""Page shell: <head>, header (with the services hover dropdown), footer."""

from forms import quote_modal
from gfdata import (SITE_URL, BUSINESS, PHONE, PHONE_E164, EMAIL, ABN, ADDRESS_PUBLIC,
                    SUBURBS, SERVICES, GHL_TRACKING_ID, GHL_TRACKING_SRC,
                    img, jsonld)

# Critical CSS: everything needed to paint the header and hero without waiting
# for the stylesheet. The full sheet loads asynchronously below it.
CRITICAL_CSS = """
:root{--fern-900:#0d2b1d;--fern-800:#153c28;--fern-700:#1c5137;--fern-600:#24694a;--fern-500:#2f855a;--fern-400:#4da47a;--fern-300:#8fd0b0;--fern-100:#e3f2ea;--fern-50:#f2f9f5;--ink:#12211a;--ink-2:#3d5147;--ink-3:#6b7f75;--line:#dfe8e3;--line-2:#c9d8d1;--sun:#f4b942;--radius-lg:22px;--radius-pill:999px;--wrap:1160px;--gutter:20px;--font:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:var(--font);font-size:17px;line-height:1.65;color:var(--ink-2);background:#fff;-webkit-font-smoothing:antialiased}
img,svg{max-width:100%;height:auto;display:block}
a{color:var(--fern-600);text-decoration:none}
h1,h2{color:var(--ink);line-height:1.15;letter-spacing:-.03em;margin:0 0 .5em;font-weight:800;text-wrap:balance}
h1{font-size:clamp(2rem,6.2vw,3.5rem)}
p{margin:0 0 1.1em}
.wrap{width:100%;max-width:var(--wrap);margin-inline:auto;padding-inline:var(--gutter)}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--fern-700);color:#fff;padding:12px 18px;z-index:200}
.skip-link:focus{left:0}
.site-header{position:sticky;top:0;z-index:100;border-bottom:1px solid var(--line)}
.site-header::before{content:"";position:absolute;inset:0;z-index:-1;background:rgba(255,255,255,.94)}
.header-inner{position:relative;display:flex;align-items:center;gap:14px;min-height:70px}
.brand{display:flex;align-items:center;gap:10px;flex:1 1 auto;min-width:0}
.brand img,.brand svg{height:44px;width:auto;flex:0 0 auto}
.brand-mark{color:var(--fern-600)}
.brand-text{display:flex;flex-direction:column;line-height:1.05;min-width:0}
.brand-name{font-weight:800;font-size:1.02rem;color:var(--fern-800);letter-spacing:-.02em;white-space:nowrap}
.brand-tag{font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}
.nav-toggle{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border:1px solid var(--line-2);background:#fff;border-radius:12px;cursor:pointer;flex:0 0 auto}
.nav-toggle span{display:block;width:20px;height:2px;background:var(--ink);border-radius:2px;position:relative}
.nav-toggle span::before,.nav-toggle span::after{content:"";position:absolute;left:0;width:20px;height:2px;background:var(--ink);border-radius:2px}
.nav-toggle span::before{top:-6px}.nav-toggle span::after{top:6px}
.site-nav{position:fixed;inset:70px 0 0;background:#fff;padding:8px var(--gutter) 32px;overflow-y:auto;opacity:0;visibility:hidden}
.site-nav ul{list-style:none;margin:0;padding:0}
.nav-header-cta{display:inline-flex;flex:0 0 auto;padding:13px 18px;min-height:46px;font-size:.94rem}
.nav-cta-full{display:none}.nav-cta-short{display:inline}
.btn-row--split{display:flex;gap:10px;margin-top:22px}
.btn-row--split .btn{flex:1 1 0;min-width:0;padding-inline:14px;font-size:.95rem;white-space:nowrap}
.ticker{position:relative;z-index:2;overflow:hidden;background:rgba(255,255,255,.04);border-top:1px solid rgba(255,255,255,.12);border-bottom:1px solid rgba(255,255,255,.12)}
.ticker-track{display:flex;width:max-content}.ticker-run{display:flex;flex:0 0 auto}
.ticker-item{display:inline-flex;align-items:center;gap:9px;flex:0 0 auto;padding:14px 26px;font-size:.9rem;font-weight:600;color:#d7e9df;white-space:nowrap}
.page-head.has-bg{background-size:cover;background-position:center}
.page-head.has-bg::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,43,29,.93),rgba(13,43,29,.95))}
.page-head-inner{display:grid;gap:30px}
[hidden]{display:none!important}
.hero{position:relative;overflow:hidden;background:var(--fern-900);color:#cfe3d8}
.hero-inner{position:relative;z-index:2;display:grid;gap:32px;padding-block:clamp(2.5rem,8vw,4.75rem)}
.hero h1{color:#fff}
.hero-media{border-radius:var(--radius-lg);overflow:hidden;aspect-ratio:4/3;background:var(--fern-800)}
.hero-media img{width:100%;height:100%;object-fit:cover}
.page-head{background:var(--fern-900);color:#c3dacd;position:relative;overflow:hidden}
.page-head-inner{padding-block:clamp(2.25rem,6vw,3.75rem)}
.page-head h1{color:#fff;margin-bottom:.35em}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;font-weight:650;font-size:1rem;line-height:1;padding:16px 26px;border-radius:var(--radius-pill);border:1.5px solid transparent;cursor:pointer;min-height:52px}
.btn--primary{background:var(--fern-600);color:#fff}
.btn--call{background:var(--sun);color:var(--fern-900)}
.btn--ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.32)}
.btn-row{display:flex;flex-wrap:wrap;gap:12px}
[data-reveal]{opacity:0}
.no-js [data-reveal]{opacity:1}
@media (max-width:899px){.hero-inner{gap:20px;padding-block:1.7rem 1.5rem}.hero h1{font-size:clamp(1.8rem,7.4vw,2.4rem)}.hero-media{aspect-ratio:16/10}.hero-copy{display:flex;flex-direction:column}.hero-copy .btn-row--split{order:4;margin-top:4px}.hero-copy .lede{order:5;margin:18px 0 0}}
@media (max-width:479px){.header-inner{gap:9px}.brand{gap:8px}.brand-mark{height:34px}.brand-name{font-size:.95rem}.brand-tag{display:none}.nav-toggle{width:44px;height:44px}.nav-header-cta{padding:12px 15px;min-height:44px;font-size:.9rem}}
@media (max-width:359px){.brand-text{display:none}}
@media (min-width:900px){.hero-inner{grid-template-columns:1.05fr .95fr;align-items:center;gap:52px;padding-block:clamp(3.5rem,7vw,6rem)}}
@media (min-width:960px){.page-head-inner{grid-template-columns:1.02fr .98fr;align-items:center;gap:48px}}
@media (min-width:1000px){.nav-toggle{display:none}.site-nav{position:static;inset:auto;padding:0;overflow:visible;opacity:1;visibility:visible;flex:0 0 auto}.site-nav>ul{display:flex;align-items:center;gap:4px}.site-nav .nav-cta{display:none}.nav-header-cta{margin-left:10px;padding:16px 26px;min-height:52px;font-size:1rem}.nav-cta-full{display:inline}.nav-cta-short{display:none}}
@media (prefers-reduced-motion:reduce){[data-reveal]{opacity:1}}
"""


BRAND_MARK = """<svg class="brand-mark" viewBox="0 0 56 64" width="41" height="47" aria-hidden="true" focusable="false">
  <path d="M15 59C20 41 27 27 39 15" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M39 15c1.7-3.6 4.6-5.5 7.1-4.5 2.7 1 3.3 4.5 1 6.4-1.9 1.6-4.5.7-4.8-1.7" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="currentColor">
    <path d="M15.77 56.33C21.69 59.95 28.89 56.89 32.83 53.29C27.63 51.79 19.56 51.92 15.77 56.33Z"/>
    <path d="M17.29 51.48C16.97 45.02 10.83 41.21 5.99 40.17C7.56 44.93 11.89 50.99 17.29 51.48Z"/>
    <path d="M18.94 46.83C23.73 50.44 29.98 48.23 33.51 45.32C29.21 43.63 22.39 43.19 18.94 46.83Z"/>
    <path d="M20.74 42.36C21.07 36.84 16.18 33.32 12.13 32.21C13.03 36.34 16.17 41.7 20.74 42.36Z"/>
    <path d="M22.69 38.06C26.32 41.58 31.57 40.16 34.65 37.91C31.27 36.1 25.76 35.17 22.69 38.06Z"/>
    <path d="M24.81 33.94C25.72 29.44 22.03 26.31 18.77 25.21C19.05 28.64 21.07 33.18 24.81 33.94Z"/>
    <path d="M27.13 29.97C29.62 33.25 33.79 32.47 36.36 30.81C33.92 28.99 29.75 27.76 27.13 29.97Z"/>
    <path d="M29.64 26.14C30.96 22.72 28.36 20.16 25.86 19.18C25.64 21.82 26.7 25.4 29.64 26.14Z"/>
    <path d="M32.38 22.46C33.8 25.33 36.83 24.97 38.83 23.78C37.29 22.12 34.46 20.82 32.38 22.46Z"/>
  </g>
</svg>"""


def head(page):
    """Build the <head> for a page dict."""
    canonical = SITE_URL + page["path"]
    og_image = img(page.get("og_photo", "photo1"), 1200)
    robots = ('<meta name="robots" content="noindex, follow">'
              if page.get("noindex") else
              '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">')

    schema_blocks = "\n".join(jsonld(b) for b in page.get("schema", []))

    return """<!doctype html>
<html lang="en-AU" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{business}">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<meta name="theme-color" content="#0d2b1d">
<meta name="geo.region" content="AU-VIC">
<meta name="geo.placename" content="Craigieburn">
<meta name="geo.position" content="-37.5991;144.9407">
<meta name="ICBM" content="-37.5991, 144.9407">

<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="mask-icon" href="/favicon.svg" color="#0d2b1d">
<link rel="preconnect" href="https://lh3.googleusercontent.com" crossorigin>
<link rel="dns-prefetch" href="https://link.msgsndr.com">

<style>{critical}</style>
<link rel="preload" href="/assets/css/site.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/assets/css/site.css"></noscript>

<!-- GoHighLevel external tracking -->
<script src="{ghl_src}" data-tracking-id="{ghl_id}" defer></script>

{schema}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
""".format(
        title=page["title"],
        description=page["description"],
        robots=robots,
        canonical=canonical,
        business=BUSINESS,
        og_title=page.get("og_title", page["title"]),
        og_image=og_image,
        og_alt=page.get("og_alt", BUSINESS + " grounds maintenance crew in Melbourne's north"),
        critical=CRITICAL_CSS.strip(),
        ghl_src=GHL_TRACKING_SRC,
        ghl_id=GHL_TRACKING_ID,
        schema=schema_blocks,
    )


def _nav_link(label, href, current, extra=""):
    aria = ' aria-current="page"' if current == href else ""
    return '<li%s><a href="%s"%s>%s</a></li>' % (extra, href, aria, label)


def header(current=""):
    dd_items = "\n".join(
        '<li><a href="/services/{slug}/">{nav}<span class="dd-desc">{desc}</span></a></li>'.format(
            slug=s["slug"], nav=s["nav"], desc=s["dd_desc"]) for s in SERVICES)

    services_current = ' aria-current="page"' if current.startswith("/services/") else ""

    return """<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="{business} home">
      {mark}
      <span class="brand-text">
        <span class="brand-name">Green Fern</span>
        <span class="brand-tag">Garden Services</span>
      </span>
    </a>

    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
      <span></span>
    </button>

    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>
        {home}
        <li class="has-dropdown" data-open="false">
          <button class="dropdown-trigger" type="button" aria-expanded="false" aria-controls="services-menu"{services_current}>
            Services <span class="chev" aria-hidden="true"></span>
          </button>
          <div class="dropdown" id="services-menu">
            <div class="dropdown-inner">
              <ul>
                {dd_items}
                <li class="dd-all"><a href="/services/">All gardening services in Melbourne’s north</a></li>
              </ul>
            </div>
          </div>
        </li>
        {about}
        {contact}
        <li class="nav-cta"><a class="btn btn--call btn--block" href="tel:{phone_e164}">Call {phone}</a></li>
      </ul>
    </nav>

    <button class="btn btn--primary nav-header-cta" type="button" data-modal-open="quote-modal">
      <span class="nav-cta-full">Get a free quote</span><span class="nav-cta-short">Free quote</span>
    </button>
  </div>
</header>
""".format(
        business=BUSINESS,
        mark=BRAND_MARK,
        home=_nav_link("Home", "/", current),
        services_current=services_current,
        dd_items=dd_items,
        about=_nav_link("About", "/about/", current),
        contact=_nav_link("Contact", "/contact/", current),
        phone_e164=PHONE_E164,
        phone=PHONE,
    )



def footer():
    service_links = "\n".join(
        '<li><a href="/services/%s/">%s</a></li>' % (s["slug"], s["nav"]) for s in SERVICES)
    areas = " · ".join(SUBURBS)

    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" aria-label="{business} home">
          {mark}
          <span class="brand-text">
            <span class="brand-name">Green Fern</span>
            <span class="brand-tag">Garden Services</span>
          </span>
        </a>
        <p>Scheduled lawn mowing and garden maintenance for homes, childcare centres, schools, strata and commercial grounds across Craigieburn and Melbourne’s northern suburbs. Owner-operated by {owner}.</p>
      </div>

      <div>
        <h3>Services</h3>
        <ul>
          {service_links}
          <li><a href="/services/">All services</a></li>
        </ul>
      </div>

      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About Green Fern</a></li>
          <li><a href="/contact/">Contact &amp; quotes</a></li>
        </ul>
      </div>

      <div>
        <h3>Get in touch</h3>
        <ul>
          <li><a href="tel:{e164}">{phone}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li>{address}</li>
          <li>Mon–Fri 7am–5pm · Sat 8am–1pm</li>
        </ul>
      </div>
    </div>

    <div class="footer-areas" style="margin-top:34px">
      <h3>Service areas</h3>
      <p>{areas}</p>
    </div>

    <div class="footer-bottom">
      <p>© <span data-year>2026</span> {business}. ABN {abn}.</p>
      <p>$10M public liability · Working With Children Checks · JSEA &amp; SWMS on every commercial site</p>
    </div>
  </div>
</footer>
""".format(
        business=BUSINESS, owner="Marty Searle", mark=BRAND_MARK,
        service_links=service_links, e164=PHONE_E164, phone=PHONE, email=EMAIL,
        address=ADDRESS_PUBLIC, areas=areas, abn=ABN,
    )


def tail():
    return quote_modal() + """<script src="/assets/js/config.js" defer></script>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def page_head(trail, eyebrow, h1, lede, buttons, bg_photo=None, extra=""):
    """Dark page header. bg_photo lays the client's photography behind the overlay."""
    bg = ""
    style = ""
    if bg_photo:
        bg = ' has-bg'
        style = ' style="background-image:url(\'%s\')"' % img(bg_photo, 1600)
    return """<div class="page-head{bg}"{style}>
  {crumbs}
  <div class="wrap page-head-inner">
    <div class="page-head-copy">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <div class="btn-row" style="margin-top:24px">{buttons}</div>
    </div>
    {extra}
  </div>
</div>
""".format(bg=bg, style=style, crumbs=breadcrumbs(trail), eyebrow=eyebrow, h1=h1,
           lede=lede, buttons=buttons, extra=extra)


def breadcrumbs(trail):
    """trail: list of (label, href) — last item is the current page."""
    items = []
    for i, (label, href) in enumerate(trail):
        if i == len(trail) - 1:
            items.append('<li><span aria-current="page">%s</span></li>' % label)
        else:
            items.append('<li><a href="%s">%s</a></li>' % (href, label))
    return ('<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>'
            + "".join(items) + "</ol></div></nav>")


def breadcrumb_schema(trail):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": i + 1,
            "name": label,
            "item": SITE_URL + href,
        } for i, (label, href) in enumerate(trail)],
    }


def faq_section(faqs, heading="Frequently asked questions", lede=None):
    items = "\n".join(
        """      <details class="faq-item" data-reveal>
        <summary>{q}</summary>
        <div class="faq-a"><p>{a}</p></div>
      </details>""".format(q=q, a=a) for q, a in faqs)
    lede_html = '<p class="lede">%s</p>' % lede if lede else ""
    return """<section class="section section--tint" id="faq">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Answers</span>
    <h2 data-reveal>{heading}</h2>
    {lede}
    <div class="faq-list" style="margin-top:28px">
{items}
    </div>
  </div>
</section>
""".format(heading=heading, lede=lede_html, items=items)


def faq_schema(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        } for q, a in faqs],
    }


def cta_band(heading, body, service=None):
    q = "/contact/" + ("?service=" + service if service else "")
    return """<section class="section">
  <div class="wrap">
    <div class="cta-band" data-reveal>
      <h2>{heading}</h2>
      <p class="lede">{body}</p>
      <div class="btn-row">
        <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
        <a class="btn btn--ghost" href="{q}">Request a free quote</a>
      </div>
    </div>
  </div>
</section>
""".format(heading=heading, body=body, e164=PHONE_E164, phone=PHONE, q=q)


def areas_section(intro, deep=True):
    lis = "\n".join('      <li><span>%s</span></li>' % s for s in SUBURBS)
    cls = "section section--deep" if deep else "section section--tint"
    return """<section class="{cls}" id="service-areas">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Service areas</span>
    <h2 data-reveal>Gardening services across Melbourne’s northern suburbs</h2>
    <p class="lede" data-reveal>{intro}</p>
    <ul class="area-list" style="margin-top:26px" data-reveal>
{lis}
    </ul>
  </div>
</section>
""".format(cls=cls, intro=intro, lis=lis)
