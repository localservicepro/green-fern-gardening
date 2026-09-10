# -*- coding: utf-8 -*-
"""About, Contact and Thank You pages."""

from gfdata import (SITE_URL, BUSINESS, OWNER, PHONE, PHONE_E164, EMAIL, ABN, STREET,
                    SUBURB, STATE, POSTCODE, SUBURBS, SERVICES, TESTIMONIALS,
                    img, local_business_node)
import layout as L

ABOUT_FAQS = [
    ("Who owns Green Fern Gardening Services?",
     "Green Fern Gardening Services is owner-operated by Marty Searle from Craigieburn. Marty answers the phone himself — there is no call centre and no dispatcher between you and the person running the crew."),
    ("Is Green Fern insured?",
     "Yes. Green Fern carries $10M public liability insurance, every crew member holds a current Working With Children Check, and a JSEA and SWMS is filed for every childcare, school and commercial site before the first visit."),
    ("How long has Green Fern been operating in Melbourne’s north?",
     "Green Fern Gardening Services operates from Craigieburn under ABN 29 279 087 766, servicing eleven suburbs across Melbourne’s northern corridor for homes, childcare centres, schools, strata properties and commercial grounds."),
    ("What makes Green Fern different from other Melbourne gardeners?",
     "Scheduled visits with an automated SMS the day before, the same crew each time, compliance documentation supplied before you ask, and a fixed price per visit rather than an hourly rate that varies with how long the job takes."),
]

CONTACT_FAQS = [
    ("How do I get a quote from Green Fern?",
     "Call 0420 462 848 or send the quote form on this page. We book a free on-site walkthrough, measure what actually needs doing, and give you a fixed price per visit — usually within one business day of the walkthrough."),
    ("What areas do you quote in?",
     "Craigieburn, Lalor, Epping, Glenroy, Campbellfield, Broadmeadows, Thomastown, Reservoir, Tullamarine, Preston and Northcote. If you are just outside that list, call and ask — we can often fit a property in near an existing round."),
    ("How quickly can you start?",
     "Properties in Craigieburn, Epping, Lalor and Thomastown sit on an existing round and usually get the earliest start date. For other suburbs it depends on the current schedule — we will tell you a real date at the walkthrough, not a maybe."),
    ("Do you charge for quotes?",
     "No. The on-site walkthrough and the written quote are free, with no obligation to book."),
]


def build_about():
    trail = [("Home", "/"), ("About", "/about/")]
    page = {
        "path": "/about/",
        "title": "About Green Fern Gardening Services | Craigieburn",
        "description": ("Owner-operated grounds maintenance from Craigieburn. Green Fern services "
                        "homes, childcare centres, schools and strata across Melbourne’s north. "
                        "Call 0420 462 848."),
        "og_photo": "photo6",
        "og_alt": "The Green Fern Gardening Services crew working in Melbourne’s northern suburbs",
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [
                local_business_node(),
                L.breadcrumb_schema(trail),
                {
                    "@type": "AboutPage",
                    "@id": SITE_URL + "/about/#webpage",
                    "url": SITE_URL + "/about/",
                    "name": "About Green Fern Gardening Services",
                    "about": {"@id": SITE_URL + "/#business"},
                    "inLanguage": "en-AU",
                },
                L.faq_schema(ABOUT_FAQS),
            ],
        }],
    }

    quotes = "\n".join("""        <figure class="quote-card" data-reveal data-reveal-delay="{d}">
          <div class="quote-stars" aria-label="5 out of 5 stars">★★★★★</div>
          <blockquote><p>{quote}</p></blockquote>
          <figcaption><cite><b>{name}</b>{role}</cite></figcaption>
        </figure>""".format(d=(i % 2) + 1, quote=t["quote"], name=t["name"], role=t["role"])
        for i, t in enumerate(TESTIMONIALS))

    html = [L.head(page), L.header("/about/")]
    html.append("""<div class="page-head">
  {crumbs}
  <div class="wrap page-head-inner">
    <span class="eyebrow">Craigieburn VIC 3064</span>
    <h1>About Green Fern Gardening Services</h1>
    <p class="lede">Owner-operated grounds maintenance for Melbourne’s northern corridor. Founded and run by {owner} from Craigieburn, working for homes, childcare centres, schools, strata properties and commercial grounds across eleven suburbs.</p>
    <div class="btn-row" style="margin-top:24px">
      <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
      <a class="btn btn--ghost" href="/contact/">Get a free quote</a>
    </div>
  </div>
</div>
""".format(crumbs=L.breadcrumbs(trail), owner=OWNER, e164=PHONE_E164, phone=PHONE))

    html.append('<main id="main">\n')
    html.append("""<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-media" data-reveal>
        <img src="{photo}" width="720" height="540" loading="lazy" decoding="async"
             alt="{owner}, owner of Green Fern Gardening Services, working on a property in Craigieburn">
      </div>
      <div class="prose" data-reveal data-reveal-delay="1">
        <span class="eyebrow">The business</span>
        <h2>One contractor who actually turns up</h2>
        <p>Green Fern Gardening Services started because grounds maintenance in Melbourne’s north had a reliability problem, not a quality problem. Plenty of gardeners can cut a lawn well. Far fewer show up on the day they said they would, three months in a row.</p>
        <p>So the whole business is built around the schedule. Your visit day is set at the first walkthrough. An automated SMS lands the day before. The same crew arrives, does the same scope, and you get told about anything that needs attention. There is no dispatcher, no call centre and no rotating roster of subcontractors — you deal with {owner}.</p>
        <p>That approach is why most of our work now sits on sites where a missed visit is a real problem: childcare centres, schools, strata common areas and commercial frontages. Those clients cannot run on maybe.</p>
      </div>
    </div>
  </div>
</section>
""".format(photo=img("photo6", 720), owner=OWNER))

    html.append("""<section class="section section--tint">
  <div class="wrap">
    <span class="eyebrow" data-reveal>How we work</span>
    <h2 data-reveal>Standards that came from working on compliance sites</h2>
    <p class="lede" data-reveal>Childcare and school grounds set the bar. Every property we service gets the same systems, whether it is a primary school or a front lawn in Craigieburn.</p>
    <div class="grid grid--2" style="margin-top:34px">
      <article class="card" data-reveal data-reveal-delay="1">
        <h3>Insurance and checks in place first</h3>
        <p>$10M public liability cover, and a current Working With Children Check held by every crew member. Documentation is provided before the first visit, not produced after someone asks for it.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="2">
        <h3>JSEA and SWMS on every commercial site</h3>
        <p>A Job Safety and Environmental Analysis and Safe Work Method Statement is filed for every childcare, school, strata and commercial site before work starts, and reviewed when site conditions change.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="3">
        <h3>Scheduled around your site, not ours</h3>
        <p>Visits are planned around session times, timetables, access windows and gate codes. On childcare and school grounds that means working when children are not in the area, every time.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="4">
        <h3>Fixed price per visit</h3>
        <p>Quoted per visit after a walkthrough, not billed hourly. The price does not change because the job took longer than expected, and there are no green-waste surcharges on scheduled work.</p>
      </article>
    </div>
  </div>
</section>
""")

    html.append("""<section class="section">
  <div class="wrap">
    <span class="eyebrow" data-reveal>Business details</span>
    <h2 data-reveal>Green Fern Gardening Services</h2>
    <div class="grid grid--2" style="margin-top:30px">
      <div class="card" data-reveal>
        <ul class="contact-list">
          <li><div><span class="cl">Trading name</span><span class="cv">{business}</span></div></li>
          <li><div><span class="cl">Owner</span><span class="cv">{owner}</span></div></li>
          <li><div><span class="cl">ABN</span><span class="cv">{abn}</span></div></li>
          <li><div><span class="cl">Base</span><span class="cv">{street}, {suburb} {state} {postcode}</span></div></li>
        </ul>
      </div>
      <div class="card" data-reveal data-reveal-delay="1">
        <ul class="contact-list">
          <li><div><span class="cl">Phone</span><span class="cv"><a href="tel:{e164}">{phone}</a></span></div></li>
          <li><div><span class="cl">Email</span><span class="cv"><a href="mailto:{email}">{email}</a></span></div></li>
          <li><div><span class="cl">Hours</span><span class="cv">Mon–Fri 7am–5pm · Sat 8am–1pm</span></div></li>
          <li><div><span class="cl">Suburbs serviced</span><span class="cv">11 across Melbourne’s north</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
""".format(business=BUSINESS, owner=OWNER, abn=ABN, street=STREET, suburb=SUBURB,
           state=STATE, postcode=POSTCODE, e164=PHONE_E164, phone=PHONE, email=EMAIL))

    html.append("""<section class="section section--tint" id="reviews">
  <div class="wrap">
    <span class="eyebrow" data-reveal>What clients say</span>
    <h2 data-reveal>Centre directors, principals, strata managers and homeowners</h2>
    <div class="grid grid--2" style="margin-top:34px">
{quotes}
    </div>
  </div>
</section>
""".format(quotes=quotes))

    html.append(L.areas_section(
        "Green Fern runs scheduled rounds through Melbourne’s northern corridor from its "
        "Craigieburn base. These are the suburbs we service."))
    html.append(L.faq_section(ABOUT_FAQS, heading="About Green Fern"))
    html.append(L.cta_band(
        "Talk to Marty directly",
        "No call centre, no quote portal. Call and speak to the person who runs the crew."))
    html.append("</main>\n")
    html.append(L.call_bar())
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)


# ---------------------------------------------------------------- contact

QUOTE_FORM = """      <form class="form-card" id="quote-form" data-thank-you="/thank-you/" novalidate>
        <h2 style="font-size:1.5rem">Request your free quote</h2>
        <p style="font-size:.97rem">Tell us about the property and we will book a walkthrough. Most quotes go out within one business day.</p>

        <!-- Honeypot: hidden from people, filled by bots. -->
        <div class="hp-field" aria-hidden="true">
          <label for="company_website">Leave this field empty</label>
          <input type="text" id="company_website" name="company_website" tabindex="-1" autocomplete="off">
        </div>

        <div class="field">
          <label for="full_name">Full name <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="full_name" name="full_name" autocomplete="name" required
                 placeholder="Marty Searle">
          <span class="err" role="alert">This field is required.</span>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="email">Email <span class="req" aria-hidden="true">*</span></label>
            <input type="email" id="email" name="email" autocomplete="email" inputmode="email" required
                   placeholder="you@example.com.au">
            <span class="err" role="alert">This field is required.</span>
          </div>
          <div class="field">
            <label for="phone">Phone <span class="req" aria-hidden="true">*</span></label>
            <input type="tel" id="phone" name="phone" autocomplete="tel" inputmode="tel" required
                   placeholder="0400 000 000">
            <span class="err" role="alert">This field is required.</span>
          </div>
        </div>

        <div class="field">
          <label for="property_address">Property address <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="property_address" name="property_address" autocomplete="street-address" required
                 placeholder="12 Example Street, Craigieburn VIC 3064">
          <span class="hint">The address we would be attending, if it differs from your billing address.</span>
          <span class="err" role="alert">This field is required.</span>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="property_size">Property size</label>
            <select id="property_size" name="property_size">
              <option value="">Select a size</option>
              <option value="Small (under 300sqm)">Small — under 300sqm</option>
              <option value="Medium (300-700sqm)">Medium — 300–700sqm</option>
              <option value="Large (700sqm-1 acre)">Large — 700sqm to 1 acre</option>
              <option value="Acreage (1 acre+)">Acreage — 1 acre or more</option>
              <option value="Commercial or multi-site">Commercial or multi-site</option>
              <option value="Not sure">Not sure</option>
            </select>
          </div>
          <div class="field">
            <label for="service_needed">Service needed <span class="req" aria-hidden="true">*</span></label>
            <select id="service_needed" name="service_needed" required>
              <option value="">Select a service</option>
{service_options}
              <option value="Weed Control">Weed control</option>
              <option value="Multiple Services">Multiple services</option>
              <option value="Not sure">Not sure yet</option>
            </select>
            <span class="err" role="alert">This field is required.</span>
          </div>
        </div>

        <div class="field">
          <label for="job_notes">Job notes</label>
          <textarea id="job_notes" name="job_notes" rows="5"
                    placeholder="How often you would like visits, gate or pet access, anything that has been left too long, and any site requirements."></textarea>
          <span class="hint">The more detail here, the more accurate the quote.</span>
        </div>

        <button class="btn btn--primary btn--block" type="submit">Get my free quote</button>
        <div class="form-status" role="status" aria-live="polite"></div>
        <p class="form-note">We use your details to prepare your quote and contact you about it. No marketing lists, no sharing with third parties. Prefer to talk? Call <a href="tel:{e164}">{phone}</a>.</p>
      </form>"""


def build_contact():
    trail = [("Home", "/"), ("Contact", "/contact/")]
    page = {
        "path": "/contact/",
        "title": "Contact Green Fern Gardening Services | Craigieburn",
        "description": ("Get a free lawn mowing or garden maintenance quote in Craigieburn, Epping "
                        "and across Melbourne’s north. Call 0420 462 848 or send the quote form."),
        "og_photo": "photo2",
        "og_alt": "Contact Green Fern Gardening Services in Craigieburn",
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [
                local_business_node(),
                L.breadcrumb_schema(trail),
                {
                    "@type": "ContactPage",
                    "@id": SITE_URL + "/contact/#webpage",
                    "url": SITE_URL + "/contact/",
                    "name": "Contact Green Fern Gardening Services",
                    "about": {"@id": SITE_URL + "/#business"},
                    "inLanguage": "en-AU",
                },
                L.faq_schema(CONTACT_FAQS),
            ],
        }],
    }

    service_options = "\n".join(
        '              <option value="%s">%s</option>' % (s["nav"], s["nav"]) for s in SERVICES)
    form = QUOTE_FORM.format(service_options=service_options, e164=PHONE_E164, phone=PHONE)

    html = [L.head(page), L.header("/contact/")]
    html.append("""<div class="page-head">
  {crumbs}
  <div class="wrap page-head-inner">
    <span class="eyebrow">Free on-site walkthrough</span>
    <h1>Contact Green Fern Gardening Services</h1>
    <p class="lede">Lawn mowing and garden maintenance quotes across Craigieburn, Epping, Lalor, Reservoir, Preston and the rest of Melbourne’s north. Call {owner} directly, or send the form and we will come and look at the property.</p>
    <div class="btn-row" style="margin-top:24px">
      <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
      <a class="btn btn--ghost" href="mailto:{email}">Email {email}</a>
    </div>
  </div>
</div>
""".format(crumbs=L.breadcrumbs(trail), owner="Marty", e164=PHONE_E164, phone=PHONE, email=EMAIL))

    html.append('<main id="main">\n')
    html.append("""<section class="section">
  <div class="wrap">
    <div class="split">
{form}
      <div data-reveal data-reveal-delay="1">
        <span class="eyebrow">Direct contact</span>
        <h2>Speak to Marty, not a call centre</h2>
        <ul class="contact-list">
          <li>
            <span class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></span>
            <div><span class="cl">Phone</span><span class="cv"><a href="tel:{e164}">{phone}</a></span></div>
          </li>
          <li>
            <span class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
            <div><span class="cl">Email</span><span class="cv"><a href="mailto:{email}">{email}</a></span></div>
          </li>
          <li>
            <span class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <div><span class="cl">Based at</span><span class="cv">{street}, {suburb} {state} {postcode}</span></div>
          </li>
          <li>
            <span class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
            <div><span class="cl">Hours</span><span class="cv">Mon–Fri 7am–5pm · Sat 8am–1pm</span></div>
          </li>
        </ul>

        <div class="card" style="margin-top:24px">
          <h3>What happens after you send this</h3>
          <ol style="margin:0;padding-left:1.15em">
            <li>Marty calls to confirm the details and book a walkthrough time.</li>
            <li>We look at the property, measure the scope and check access.</li>
            <li>You get a fixed price per visit and a proposed schedule in writing.</li>
            <li>If you go ahead, your first visit date is locked in on the spot.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</section>
""".format(form=form, e164=PHONE_E164, phone=PHONE, email=EMAIL,
           street=STREET, suburb=SUBURB, state=STATE, postcode=POSTCODE))

    html.append(L.areas_section(
        "We quote across all eleven suburbs on our round. If your property sits just outside "
        "this list, call and ask — we can often fit it in alongside an existing route."))
    html.append(L.faq_section(CONTACT_FAQS, heading="Quote and booking questions"))
    html.append("</main>\n")
    html.append(L.call_bar())
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)


# ---------------------------------------------------------------- thank you

def build_thank_you():
    page = {
        "path": "/thank-you/",
        "title": "Thank you — your quote request is in | Green Fern Gardening Services",
        "description": "Your quote request has been received. Marty will call you shortly to book a free on-site walkthrough.",
        "noindex": True,
        "og_photo": "photo1",
        "og_alt": "Green Fern Gardening Services",
        "schema": [{
            "@context": "https://schema.org",
            "@graph": [local_business_node()],
        }],
    }

    service_links = "\n".join(
        '        <li><a href="/services/%s/">%s</a></li>' % (s["slug"], s["nav"]) for s in SERVICES)

    html = [L.head(page), L.header("")]
    html.append('<main id="main">\n')
    html.append("""<section class="hero">
  <div class="wrap" style="padding-block:clamp(3rem,9vw,5.5rem);text-align:center;position:relative;z-index:2">
    <div style="width:82px;height:82px;margin:0 auto 26px;border-radius:26px;background:rgba(143,208,176,.16);display:flex;align-items:center;justify-content:center">
      <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#8fd0b0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>
    </div>
    <span class="eyebrow">Quote request received</span>
    <h1>Thanks — we’ve got your details</h1>
    <p class="lede" style="margin-inline:auto">{owner} will call you shortly to confirm the details and book a free on-site walkthrough. If it is urgent, or you would rather sort it now, call <a href="tel:{e164}" style="color:#fff;text-decoration:underline">{phone}</a>.</p>
    <div class="btn-row" style="justify-content:center;margin-top:28px">
      <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
      <a class="btn btn--ghost" href="/">Back to the homepage</a>
    </div>
  </div>
</section>
""".format(owner="Marty", e164=PHONE_E164, phone=PHONE))

    html.append("""<section class="section">
  <div class="wrap wrap--narrow">
    <span class="eyebrow" data-reveal>Next steps</span>
    <h2 data-reveal>What happens from here</h2>
    <ol class="steps" style="margin-top:30px">
      <li data-reveal data-reveal-delay="1">
        <h3>We call you</h3>
        <p>Usually the same business day. Marty confirms the property details and finds a walkthrough time that suits.</p>
      </li>
      <li data-reveal data-reveal-delay="2">
        <h3>Free walkthrough</h3>
        <p>We measure the real scope, check access and gates, and talk through how often the site needs visiting.</p>
      </li>
      <li data-reveal data-reveal-delay="3">
        <h3>Fixed quote in writing</h3>
        <p>A price per visit and a proposed schedule. Go ahead and your first visit date is locked in on the spot.</p>
      </li>
    </ol>
  </div>
</section>
""")

    html.append("""<section class="section section--tint">
  <div class="wrap wrap--narrow">
    <h2 data-reveal>While you wait</h2>
    <p class="lede" data-reveal>Have a look at what else we can fold into the same visit — bundling services onto one round costs less than booking them separately.</p>
    <ul class="area-list" style="margin-top:24px" data-reveal>
{service_links}
        <li><a href="/about/">About Green Fern</a></li>
    </ul>
  </div>
</section>
""".format(service_links=service_links))

    html.append("</main>\n")
    html.append(L.call_bar())
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)


# ---------------------------------------------------------------- 404

def build_404():
    page = {
        "path": "/404.html",
        "title": "Page not found | Green Fern Gardening Services",
        "description": "That page could not be found. Browse our gardening services or call 0420 462 848.",
        "noindex": True,
        "og_photo": "photo1",
        "og_alt": "Green Fern Gardening Services",
        "schema": [],
    }
    service_links = "\n".join(
        '        <li><a href="/services/%s/">%s</a></li>' % (s["slug"], s["nav"]) for s in SERVICES)

    html = [L.head(page), L.header("")]
    html.append('<main id="main">\n')
    html.append("""<section class="hero">
  <div class="wrap" style="padding-block:clamp(3rem,9vw,5.5rem);text-align:center;position:relative;z-index:2">
    <span class="eyebrow">Error 404</span>
    <h1>That page has been mown down</h1>
    <p class="lede" style="margin-inline:auto">The page you were after does not exist. Try one of our services below, or call {phone} and we will point you the right way.</p>
    <div class="btn-row" style="justify-content:center;margin-top:26px">
      <a class="btn btn--call" href="tel:{e164}">Call {phone}</a>
      <a class="btn btn--ghost" href="/">Back to the homepage</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap wrap--narrow" style="text-align:center">
    <h2>Our gardening services</h2>
    <ul class="area-list" style="justify-content:center;margin-top:22px">
{service_links}
        <li><a href="/contact/">Get a free quote</a></li>
    </ul>
  </div>
</section>
""".format(phone=PHONE, e164=PHONE_E164, service_links=service_links))
    html.append("</main>\n")
    html.append(L.footer())
    html.append(L.tail())
    return "".join(html)
