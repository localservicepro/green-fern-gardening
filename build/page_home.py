# -*- coding: utf-8 -*-
"""Homepage — target keyword: Lawn Mowing Craigieburn."""

from gfdata import (SITE_URL, BUSINESS, PHONE, PHONE_E164, SERVICES, SUBURBS,
                    TESTIMONIALS, FAQS_HOME, img, local_business_node)
import layout as L

ICONS = {
    "mow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18h6a3 3 0 0 0 3-3V7"/><circle cx="5" cy="18" r="2.5"/><circle cx="17" cy="18" r="2.5"/><path d="M12 7h4a3 3 0 0 1 3 3v5"/><path d="M12 4v3"/></svg>',
    "hedge": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m6 4 4 4"/><path d="m18 4-4 4"/><path d="M9 9a4 4 0 1 0-4 4"/><path d="M15 9a4 4 0 1 1 4 4"/><path d="M12 8v13"/></svg>',
    "garden": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21V9"/><path d="M12 12c0-3 2-6 6-6 0 4-3 6-6 6Z"/><path d="M12 15c0-2.5-1.7-5-5-5 0 3.4 2.5 5 5 5Z"/><path d="M4 21h16"/></svg>',
    "land": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3 18 5-6 4 4 3-3 6 5"/><path d="M3 21h18"/><circle cx="8" cy="7" r="2.5"/></svg>',
    "tree": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-6"/><path d="M12 16a6 6 0 0 0 6-6 6 6 0 0 0-1.2-3.6A5 5 0 0 0 12 2a5 5 0 0 0-4.8 4.4A6 6 0 0 0 6 10a6 6 0 0 0 6 6Z"/></svg>',
    "sms": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}

SERVICE_ICONS = ["mow", "hedge", "garden", "land", "tree"]


def build():
    trail = [("Home", "/")]

    page = {
        "path": "/",
        "title": "Lawn Mowing Craigieburn | Green Fern Gardening Services",
        "description": ("Scheduled lawn mowing and garden maintenance in Craigieburn, Epping and "
                        "across Melbourne’s north. Homes, schools, childcare and strata. "
                        "Call 0420 462 848."),
        "og_title": "Lawn Mowing Craigieburn | Green Fern Gardening Services",
        "og_photo": "photo1",
        "og_alt": "Green Fern Gardening Services mowing a lawn in Craigieburn",
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [
                local_business_node(),
                {
                    "@type": "WebSite",
                    "@id": SITE_URL + "/#website",
                    "url": SITE_URL + "/",
                    "name": BUSINESS,
                    "publisher": {"@id": SITE_URL + "/#business"},
                    "inLanguage": "en-AU",
                },
                {
                    "@type": "WebPage",
                    "@id": SITE_URL + "/#webpage",
                    "url": SITE_URL + "/",
                    "name": "Lawn Mowing Craigieburn | Green Fern Gardening Services",
                    "isPartOf": {"@id": SITE_URL + "/#website"},
                    "about": {"@id": SITE_URL + "/#business"},
                    "primaryImageOfPage": img("photo1", 1200),
                    "inLanguage": "en-AU",
                },
                L.faq_schema(FAQS_HOME),
            ],
        }],
    }

    service_cards = "\n".join("""        <article class="card service-card" data-reveal data-reveal-delay="{d}">
          <div class="sc-media">
            <img src="{photo}" width="600" height="375" loading="lazy" decoding="async"
                 alt="{alt}">
          </div>
          <div class="sc-body">
            <h3>{nav}</h3>
            <p>{card}</p>
            <a class="card-link" href="/services/{slug}/">{nav} in Melbourne’s north</a>
          </div>
        </article>""".format(
        d=(i % 3) + 1, photo=img(s["photo"], 600), slug=s["slug"], nav=s["nav"], card=s["card"],
        alt="%s by %s across Melbourne’s northern suburbs" % (s["nav"], BUSINESS),
    ) for i, s in enumerate(SERVICES))

    quotes = "\n".join("""        <figure class="quote-card" data-reveal data-reveal-delay="{d}">
          <div class="quote-stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote><p>{quote}</p></blockquote>
          <figcaption><cite><b>{name}</b>{role}</cite></figcaption>
        </figure>""".format(d=(i % 3) + 1, quote=t["quote"], name=t["name"], role=t["role"])
        for i, t in enumerate(TESTIMONIALS[:3]))

    html = []
    html.append(L.head(page))
    html.append(L.header("/"))
    html.append('<main id="main">\n')

    # ---- Hero ----
    html.append("""<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <span class="eyebrow">Craigieburn · Melbourne’s northern suburbs</span>
      <h1>Lawn Mowing &amp; Garden Maintenance Craigieburn</h1>
      <p class="hero-sub">Grounds care that shows up. Every time.</p>
      <p class="lede">Green Fern Gardening Services is the lawn mowing Craigieburn households, childcare centres, schools and strata book when they want it handled rather than chased. Scheduled visits across Craigieburn, Epping, Lalor and Melbourne’s north — a set visit day, a day-before SMS, and the same crew every time.</p>
      <div class="btn-row" style="margin-top:26px">
        <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
        <a class="btn btn--primary" href="/contact/">Get a free quote</a>
      </div>
      <ul class="hero-badges">
        <li>Day-before SMS reminders</li>
        <li>$10M public liability</li>
        <li>Working With Children Checks</li>
        <li>Owner-answered phone</li>
      </ul>
    </div>
    <div class="hero-media">
      <img src="{hero}" width="900" height="675" fetchpriority="high" decoding="async"
           alt="Green Fern Gardening Services mowing a residential lawn in Craigieburn, Melbourne">
    </div>
  </div>
</section>
""".format(e164=PHONE_E164, phone=PHONE, hero=img("photo1", 900)))

    # ---- Trust strip ----
    html.append("""<section class="trust-strip">
  <div class="wrap">
    <ul>
      <li><span class="t-num">11</span><span class="t-lab">Northern suburbs serviced</span></li>
      <li><span class="t-num">$10M</span><span class="t-lab">Public liability cover</span></li>
      <li><span class="t-num">100%</span><span class="t-lab">Crew hold WWC Checks</span></li>
      <li><span class="t-num">SMS</span><span class="t-lab">Reminder the day before</span></li>
    </ul>
  </div>
</section>
""")

    # ---- Primary keyword section ----
    html.append("""<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="prose" data-reveal>
        <span class="eyebrow">Our home ground</span>
        <h2>Lawn Mowing Craigieburn — on a schedule, not on request</h2>
        <p>Green Fern is based at Craigieburn, which means lawn mowing Craigieburn properties sits on our own doorstep rather than at the end of a cross-town run. Craigieburn, Epping, Lalor and Thomastown share a single round, so those properties get the earliest start dates and the lowest per-visit price on our books.</p>
        <p>Craigieburn lawns are hard on a mower. The soil compacts, summers run hot and dry, and spring growth from September through November is steep enough that a fortnightly cycle turns into twice the work at every visit. So we set the cycle to the season rather than selling one flat schedule: weekly through spring, fortnightly over summer, monthly through the winter slowdown.</p>
        <ul>
          <li>Mow, edge, line-trim and clippings removed — every visit, no extras billed after</li>
          <li>A fixed price per visit, quoted from a walkthrough rather than an hourly rate</li>
          <li>An automated SMS the day before so gates get unlocked and pets brought in</li>
          <li>The same crew each cycle, who already know the site and its access</li>
        </ul>
        <a class="btn btn--primary" href="/services/lawn-mowing/">Lawn mowing details and pricing</a>
      </div>
      <div data-reveal data-reveal-delay="1">
        <div class="split-media">
          <img src="{photo}" width="720" height="540" loading="lazy" decoding="async"
               alt="Green Fern Gardening Services completing a scheduled lawn mowing visit in Craigieburn">
        </div>
      </div>
    </div>
  </div>
</section>
""".format(photo=img("photo2", 720)))

    # ---- Services ----
    html.append("""<section class="section" id="services">
  <div class="wrap">
    <span class="eyebrow" data-reveal>What we do</span>
    <h2 data-reveal>Lawn and garden services across Melbourne’s north</h2>
    <p class="lede" data-reveal>Six services, one contractor, one invoice. Lawn mowing, hedge trimming, weed control, tree removal, soft landscaping and full garden maintenance — booked on a schedule so nothing gets away from you.</p>
    <div class="grid grid--3" style="margin-top:34px">
{cards}
    </div>
  </div>
</section>
""".format(cards=service_cards))

    # ---- Why Green Fern ----
    html.append("""<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Why Green Fern</span>
    <h2 data-reveal>Built around properties where presentation matters</h2>
    <p class="lede" data-reveal>Most of our work is on sites that cannot afford a missed visit — childcare centres, schools, strata common areas and commercial frontages. The systems that keeps those clients happy are the same ones your lawn gets.</p>
    <div class="grid grid--3" style="margin-top:34px">
      <article class="card" data-reveal data-reveal-delay="1">
        <div class="card-icon">{sms}</div>
        <h3>An automated SMS the day before</h3>
        <p>You know exactly when we are coming. Gates get unlocked, pets get brought in, and outdoor sessions get moved without anyone having to ring us.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="2">
        <div class="card-icon">{shield}</div>
        <h3>Compliance sorted before you ask</h3>
        <p>$10M public liability, current Working With Children Checks on every crew member, and a JSEA and SWMS filed for every childcare, school and commercial site.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="3">
        <div class="card-icon">{clock}</div>
        <h3>A schedule you never have to chase</h3>
        <p>Weekly, fortnightly or monthly, set at the first walkthrough. Same crew, same day, no re-booking and no call centre — you speak to {owner}.</p>
      </article>
    </div>
  </div>
</section>
""".format(sms=ICONS["sms"], shield=ICONS["shield"], clock=ICONS["clock"], owner="Marty"))

    # ---- How it works ----
    html.append("""<section class="section">
  <div class="wrap">
    <span class="eyebrow" data-reveal>How it works</span>
    <h2 data-reveal>Three steps to a lawn you stop thinking about</h2>
    <ol class="steps" style="margin-top:34px">
      <li data-reveal data-reveal-delay="1">
        <h3>Free walkthrough</h3>
        <p>Call {phone} or send the quote form. We walk the property, measure what actually needs doing, and give you a fixed price per visit — not an hourly guess.</p>
      </li>
      <li data-reveal data-reveal-delay="2">
        <h3>Your schedule gets set</h3>
        <p>Weekly through spring, fortnightly over summer, monthly through winter — or whatever cycle suits the site. Locked in up front, with your visit day confirmed.</p>
      </li>
      <li data-reveal data-reveal-delay="3">
        <h3>We just turn up</h3>
        <p>An SMS lands the day before. The crew mows, edges, trims and clears clippings, then sends through anything you should know about. That is the whole job.</p>
      </li>
    </ol>
  </div>
</section>
""".format(phone=PHONE))

    # ---- Who we work for ----
    html.append("""<section class="section section--tint">
  <div class="wrap">
    <div class="split">
      <div class="split-media" data-reveal>
        <img src="{photo}" width="720" height="540" loading="lazy" decoding="async"
             alt="Green Fern Gardening Services maintaining grounds at a childcare centre in Melbourne’s north">
      </div>
      <div data-reveal data-reveal-delay="1">
        <span class="eyebrow">Who we work for</span>
        <h2>Homes, childcare centres, schools, strata and commercial grounds</h2>
        <div class="prose">
          <ul>
            <li><strong>Homes</strong> — scheduled lawn mowing and garden maintenance in Craigieburn, Epping, Lalor, Thomastown, Reservoir and Preston.</li>
            <li><strong>Childcare centres</strong> — softfall top-ups, sandpit maintenance, playground surface checks, all scheduled around active sessions.</li>
            <li><strong>Schools</strong> — grounds care worked around timetables and access windows, with the compliance paperwork already in place.</li>
            <li><strong>Strata &amp; owners’ corporations</strong> — common areas, frontages and garden beds kept to a consistent standard on one contract.</li>
            <li><strong>Commercial properties</strong> — frontages and car park landscaping that reflect on the business behind them.</li>
          </ul>
        </div>
        <a class="btn btn--primary" href="/about/" style="margin-top:6px">More about Green Fern</a>
      </div>
    </div>
  </div>
</section>
""".format(photo=img("photo3", 720)))

    # ---- Testimonials ----
    html.append("""<section class="section" id="reviews">
  <div class="wrap">
    <span class="eyebrow" data-reveal>What clients say</span>
    <h2 data-reveal>Centre directors, principals and homeowners</h2>
    <div class="grid grid--3" style="margin-top:34px">
{quotes}
    </div>
  </div>
</section>
""".format(quotes=quotes))

    # ---- Gallery ----
    html.append("""<section class="section section--tint" id="our-work">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Our recent work</span>
    <h2 data-reveal>Lawns, hedges and grounds across Melbourne’s north</h2>
    <p class="lede" data-reveal>A sample of scheduled maintenance and one-off works completed for homes, centres and commercial sites around Craigieburn.</p>
    <div class="gallery" style="margin-top:30px">
      <figure data-reveal data-reveal-delay="1"><img src="{p1}" width="520" height="390" loading="lazy" decoding="async" alt="Freshly mown residential lawn maintained by Green Fern Gardening Services in Craigieburn"></figure>
      <figure data-reveal data-reveal-delay="2"><img src="{p2}" width="520" height="390" loading="lazy" decoding="async" alt="Hedge trimming and garden bed work completed in Melbourne’s northern suburbs"></figure>
      <figure data-reveal data-reveal-delay="3"><img src="{p3}" width="520" height="390" loading="lazy" decoding="async" alt="Scheduled grounds maintenance on a commercial property in Melbourne’s north"></figure>
      <figure data-reveal data-reveal-delay="1"><img src="{p4}" width="520" height="390" loading="lazy" decoding="async" alt="Soft landscaping and garden bed renovation completed in Craigieburn"></figure>
      <figure data-reveal data-reveal-delay="2"><img src="{p5}" width="520" height="390" loading="lazy" decoding="async" alt="Tree and shrub removal and site clean-up by Green Fern Gardening Services"></figure>
      <figure data-reveal data-reveal-delay="3"><img src="{p6}" width="520" height="390" loading="lazy" decoding="async" alt="Green Fern Gardening Services crew maintaining garden beds in Melbourne’s north"></figure>
    </div>
  </div>
</section>
""".format(p1=img("photo1", 520), p2=img("photo2", 520), p3=img("photo3", 520),
           p4=img("photo4", 520), p5=img("photo5", 520), p6=img("photo6", 520)))

    # ---- Service areas ----
    html.append(L.areas_section(
        "Green Fern Gardening Services is based at Craigieburn and runs scheduled rounds through "
        "Melbourne’s northern corridor. If your property is in one of these suburbs, we can usually "
        "add you to an existing round — which keeps the per-visit price down."))

    # ---- FAQ ----
    html.append(L.faq_section(
        FAQS_HOME,
        heading="Lawn mowing and garden maintenance questions",
        lede="The things people ask before booking. If yours is not here, call %s and ask Marty directly." % PHONE))

    # ---- CTA ----
    html.append(L.cta_band(
        "Ready for grounds care you don’t have to chase?",
        "Free on-site walkthrough, a fixed price per visit, and a schedule locked in before we start. "
        "Craigieburn, Epping, Lalor, Reservoir, Preston and across Melbourne’s north."))

    html.append("</main>\n")
    html.append(L.call_bar())
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)
