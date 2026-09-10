# -*- coding: utf-8 -*-
"""Services hub and the five service pages."""

from gfdata import (SITE_URL, BUSINESS, PHONE, PHONE_E164, SERVICES, SUBURBS,
                    TESTIMONIALS, img, local_business_node)
import layout as L


def _service_node(s):
    return {
        "@type": "Service",
        "@id": "%s/services/%s/#service" % (SITE_URL, s["slug"]),
        "name": s["keyword"],
        "serviceType": s["nav"],
        "description": s["description"],
        "provider": {"@id": SITE_URL + "/#business"},
        "areaServed": [{"@type": "City", "name": x} for x in SUBURBS],
        "url": "%s/services/%s/" % (SITE_URL, s["slug"]),
        "image": img(s["photo"], 1200),
        "audience": {"@type": "Audience", "audienceType": s["audience"]},
    }


# ---------------------------------------------------------------- hub

def build_hub():
    trail = [("Home", "/"), ("Services", "/services/")]
    page = {
        "path": "/services/",
        "title": "Gardening Services Melbourne | Green Fern Craigieburn",
        "description": ("Gardening services across Melbourne’s north — lawn mowing, hedge trimming, "
                        "garden maintenance, landscaping and tree removal. Call 0420 462 848."),
        "og_photo": "photo3",
        "og_alt": "Green Fern Gardening Services grounds maintenance in Melbourne’s north",
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [
                local_business_node(),
                L.breadcrumb_schema(trail),
                {
                    "@type": "CollectionPage",
                    "@id": SITE_URL + "/services/#webpage",
                    "url": SITE_URL + "/services/",
                    "name": "Gardening Services Melbourne | Green Fern Craigieburn",
                    "about": {"@id": SITE_URL + "/#business"},
                    "inLanguage": "en-AU",
                    "mainEntity": {
                        "@type": "ItemList",
                        "itemListElement": [{
                            "@type": "ListItem",
                            "position": i + 1,
                            "name": s["keyword"],
                            "url": "%s/services/%s/" % (SITE_URL, s["slug"]),
                        } for i, s in enumerate(SERVICES)],
                    },
                },
                L.faq_schema(HUB_FAQS),
            ],
        }],
    }

    cards = "\n".join("""        <article class="card service-card" data-reveal data-reveal-delay="{d}">
          <div class="sc-media">
            <img src="{photo}" width="600" height="375" loading="lazy" decoding="async" alt="{alt}">
          </div>
          <div class="sc-body">
            <h3>{nav}</h3>
            <p>{card}</p>
            <p style="font-size:.88rem;color:var(--ink-3)"><strong>Best for:</strong> {audience}.</p>
            <a class="card-link" href="/services/{slug}/">See {nav_l} details</a>
          </div>
        </article>""".format(
        d=(i % 3) + 1, photo=img(s["photo"], 600), slug=s["slug"], nav=s["nav"],
        nav_l=s["nav"].lower(), card=s["card"], audience=s["audience"],
        alt="%s in Melbourne’s northern suburbs by %s" % (s["nav"], BUSINESS),
    ) for i, s in enumerate(SERVICES))

    html = [L.head(page), L.header("/services/")]
    html.append(L.page_head(
        trail,
        "Craigieburn · Melbourne’s north",
        "Gardening Services Melbourne — Lawn, Hedge &amp; Grounds Care",
        "Green Fern Gardening Services covers the full round: lawn mowing, hedge trimming, weed control, "
        "garden maintenance, soft landscaping and tree removal. One contractor, one schedule, one invoice — "
        "across Craigieburn, Epping, Reservoir, Preston and the rest of Melbourne’s northern suburbs.",
        '<button class="btn btn--call" type="button" data-modal-open="quote-modal">Get a free quote</button>'
        '<a class="btn btn--ghost" href="tel:%s">Call %s</a>' % (PHONE_E164, PHONE),
        bg_photo="photo6"))

    html.append('<main id="main">\n')
    html.append("""<section class="section">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Our services</span>
    <h2 data-reveal>Five services that keep a property looking maintained</h2>
    <p class="lede" data-reveal>Most clients start with one and end up on a full grounds schedule. Weed control is included in garden maintenance rather than billed separately.</p>
    <div class="grid grid--3" style="margin-top:34px">
{cards}
    </div>
  </div>
</section>
""".format(cards=cards))

    html.append("""<section class="section section--tint">
  <div class="wrap">
    <div class="split split--flip">
      <div class="split-media" data-reveal>
        <img src="{photo}" width="720" height="540" loading="lazy" decoding="async"
             alt="Green Fern Gardening Services crew working on a scheduled maintenance round in Melbourne’s north">
      </div>
      <div data-reveal data-reveal-delay="1">
        <span class="eyebrow">Bundled rounds</span>
        <h2>Why most clients bundle two or three</h2>
        <div class="prose">
          <p>A crew already on site for a mow can trim the hedge, clear the beds and top up mulch in the same visit. That is cheaper than three separate call-outs, and it is the reason our childcare, school and strata clients hand us the whole grounds contract rather than splitting it.</p>
          <ul>
            <li>One visit, one travel charge, one invoice</li>
            <li>The same crew who know where the taps, gates and access codes are</li>
            <li>Problems get flagged early — drainage, dieback, damaged softfall</li>
            <li>A single point of contact: {owner}, who answers his own phone</li>
          </ul>
        </div>
        <a class="btn btn--primary" href="/contact/">Ask for a bundled quote</a>
      </div>
    </div>
  </div>
</section>
""".format(photo=img("photo6", 720), owner="Marty Searle"))

    html.append(L.areas_section(
        "Every service on this page is available across all eleven suburbs we cover. "
        "Craigieburn, Epping, Lalor and Thomastown sit on the same round, so those "
        "properties usually get the earliest available start date."))

    html.append(L.faq_section(HUB_FAQS, heading="Questions about our gardening services"))
    html.append(L.cta_band(
        "Not sure which service you need?",
        "Tell us what the property looks like now and what you want it to look like. "
        "We will tell you which services actually get you there — and which you can skip."))
    html.append("</main>\n")
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)


HUB_FAQS = [
    ("What gardening services does Green Fern offer in Melbourne?",
     "Green Fern Gardening Services offers lawn mowing, hedge trimming, garden maintenance with weed control, soft landscaping and tree removal across Craigieburn, Epping, Lalor, Thomastown, Reservoir, Preston, Northcote, Glenroy, Broadmeadows, Campbellfield and Tullamarine."),
    ("Can I book more than one service on the same visit?",
     "Yes, and it costs less than booking them separately. A crew already on site for a mow can trim hedges, weed beds and top up mulch in the same visit, so you pay one travel charge and receive one invoice."),
    ("Do you offer one-off jobs or only regular schedules?",
     "Both. Tree removal, block slashing, garden renovations and seasonal clean-ups are commonly one-off. Lawn mowing, hedge trimming and garden maintenance are usually scheduled weekly, fortnightly or monthly, which lowers the per-visit price."),
    ("Do you service commercial and strata properties?",
     "Yes. Childcare centres, schools, strata common areas and commercial frontages are Green Fern’s core work, covered by $10M public liability, Working With Children Checks and a JSEA and SWMS on every site."),
]


# ---------------------------------------------------------------- service pages

def build_service(s, body_fn):
    trail = [("Home", "/"), ("Services", "/services/"), (s["nav"], "/services/%s/" % s["slug"])]
    faqs = body_fn.faqs
    page = {
        "path": "/services/%s/" % s["slug"],
        "title": s["title"],
        "description": s["description"],
        "og_photo": s["photo"],
        "og_alt": "%s by %s in Melbourne’s north" % (s["nav"], BUSINESS),
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [
                local_business_node(),
                L.breadcrumb_schema(trail),
                _service_node(s),
                {
                    "@type": "WebPage",
                    "@id": "%s/services/%s/#webpage" % (SITE_URL, s["slug"]),
                    "url": "%s/services/%s/" % (SITE_URL, s["slug"]),
                    "name": s["title"],
                    "primaryImageOfPage": img(s["photo"], 1200),
                    "inLanguage": "en-AU",
                },
                L.faq_schema(faqs),
            ],
        }],
    }

    others = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
    related = "\n".join("""        <article class="card" data-reveal data-reveal-delay="{d}">
          <h3>{nav}</h3>
          <p>{card}</p>
          <a class="card-link" href="/services/{slug}/">{nav} details</a>
        </article>""".format(d=i + 1, nav=o["nav"], card=o["card"], slug=o["slug"])
        for i, o in enumerate(others))

    html = [L.head(page), L.header("/services/%s/" % s["slug"])]
    html.append(L.page_head(
        trail, body_fn.eyebrow, s["h1"], body_fn.lede,
        '<button class="btn btn--call" type="button" data-modal-open="quote-modal">Get a free quote</button>'
        '<a class="btn btn--ghost" href="tel:%s">Call %s</a>' % (PHONE_E164, PHONE),
        bg_photo=s["photo"]))

    html.append('<main id="main">\n')
    html.append(body_fn.body)

    html.append(L.areas_section(body_fn.areas_intro))
    html.append(L.faq_section(faqs, heading=body_fn.faq_heading))

    html.append("""<section class="section">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Also available</span>
    <h2 data-reveal>Other services on the same round</h2>
    <p class="lede" data-reveal>Bundle these into the same visit and you pay one travel charge instead of three.</p>
    <div class="grid grid--3" style="margin-top:30px">
{related}
    </div>
  </div>
</section>
""".format(related=related))

    html.append(L.cta_band(body_fn.cta_heading, body_fn.cta_body, service=s["slug"]))
    html.append("</main>\n")
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)
