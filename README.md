# Green Fern Gardening Services — website

Static, mobile-first marketing site for Green Fern Gardening Services (Craigieburn VIC),
built to the approved SEO/AEO/GEO strategy. No framework, no build step on the host —
deploy the repository root as-is to any static host.

## Pages

| URL | Target keyword | Notes |
| --- | --- | --- |
| `/` | Lawn Mowing Craigieburn | H1, title, meta and body all target the primary term |
| `/services/` | Gardening Services Melbourne | Hub; hover mega-menu links every service page |
| `/services/lawn-mowing/` | Lawn Mowing Services Melbourne | Deliberately takes the wider term so it does not compete with the homepage |
| `/services/hedge-trimming/` | Hedge Trimming Melbourne | Highest-volume opportunity in the strategy (260/mo, 0.26 comp) |
| `/services/garden-maintenance/` | Garden Maintenance Melbourne | Weed control folds in here rather than getting its own page |
| `/services/soft-landscaping/` | Landscaping Craigieburn | |
| `/services/tree-removal/` | Tree Removal Craigieburn | |
| `/about/` | brand / trust | |
| `/contact/` | quote form | |
| `/thank-you/` | — | `noindex`; the form redirects here after a successful submit |
| `/404.html` | — | `noindex` |

No two pages share a primary target, so nothing cannibalises anything else.

## Editing content

Pages are generated so the header, footer, schema and meta stay consistent:

```
python3 build/build.py
```

- `build/gfdata.py` — business details (NAP, ABN, suburbs), the service list, testimonials, FAQ copy
- `build/layout.py` — `<head>`, header + services dropdown, footer, FAQ/CTA/areas blocks, schema helpers
- `build/service_content.py` — the long-form copy for each service page
- `build/page_*.py` — page assembly

The generated HTML is committed, so the site still deploys as plain static files.
Re-run the build after any edit under `build/` and commit the regenerated HTML.

## How a quote form submission reaches the CRM

Every quote form posts `multipart/form-data` to Sales Brain
(`https://app.salesbrain.com.au/api/lead/4889139c-7618-4b19-a821-81f6e8800df4`, set as
`LEAD_ACTION` in `build/gfdata.py`). Sales Brain saves the lead and puts it into the
client's GoHighLevel account through its own connection (fields mapped, Lead Source and
contact source set). There is **no GoHighLevel external tracking script and no GHL form
embed** on the site; do not add them back.

The fields are unchanged: `full_name`, `email`, `phone`, `property_address`,
`property_size`, `service_needed` and `job_notes`, plus hidden `source_page` (the page
path, filled in by `build/build.py`) and `redirect` (`https://www.greenfern.au/thank-you/`),
and the `_hp_url` honeypot (Sales Brain ignores leads that fill it).

The form is rendered twice on most pages: once in the header popup (opened by the
**Get a free quote** button, present on every page) and once inline in the hero on
`/contact/`. Both instances share one handler; element ids are prefixed per instance.

- **Without JavaScript** the browser posts the form and Sales Brain redirects to `/thank-you/`.
- **With JavaScript** (`assets/js/site.js`) the form validates with visible messages,
  sends the same `FormData` with `fetch()`, then goes to `/thank-you/?name=<first name>`.
  If the request fails it falls back to a normal post, so a lead is never lost.

## Tracking

> **This site is generated.** Anything injected straight into the built HTML — an
> analytics tag, a verification meta tag, a pixel — is wiped the next time
> `build/build.py` runs, which is every content change. Tags belong in `build/`.
> After adding one, run the build and confirm `git diff` on the HTML is empty: that
> proves the generated output matches what is deployed.

**Google Analytics 4 — `G-ZFKK470FL2`.** Injected by the Sales Brain client portal and
mirrored in `build/gfdata.py` as `PORTAL_ANALYTICS`, kept byte-identical to the portal's
block (markers included) so its marker-based injection stays idempotent. The block also
fires a `generate_lead` GA4 event on `/thank-you/`, deduplicated per visit via
`sessionStorage`. If the portal reissues the block, replace that constant rather than
hand-editing the built pages.



**Google Ads tag.** `AW-18361639983` is emitted as gtag.js high in `<head>` on every page,
including `/thank-you/` and the unlisted terms pages. The account id lives in
`build/gfdata.py` as `GOOGLE_ADS_ID`.

**Conversions** are wired in `assets/js/site.js` and configured in `assets/js/config.js`:

| Conversion | Fires | Config key | Status |
| --- | --- | --- | --- |
| Phone click | Any `a[href^="tel:"]` — header, hero, CTA bands, footer | `googleAds.call` | Live: `_prRCKGs-qIdEK_IwbNE`, value 1.0 AUD |
| Quote form | On a successful submit, just before the `/thank-you/` redirect | `googleAds.form` | **Intentionally empty** |

`googleAds.form.label` is empty **on purpose**. The form conversion is configured in Google
Ads as a page-load conversion on `/thank-you/`. Setting a label here as well would fire a
second conversion on submit and count every enquiry twice. Only fill it in if that Ads
conversion is switched from a page load to an event.

Each entry takes `{ label, value, currency }`; `value`/`currency` are optional and omitted
from the event when `value` isn't a number. The label is the part after the slash in
`AW-18361639983/AbC-D_efG…`. With a label empty that conversion silently does nothing; with
the tag blocked, `adsConversion()` falls through on a 1-second timeout. Neither can stop a
call being placed or a form being submitted.

**Don't paste Google's own tel: snippet into the pages.** `site.js` already has a delegated
`tel:` listener, so adding the snippet as well would fire two conversions per tap. Supply
the label here instead.

Also note that a `gtag/js` URL copied out of Gmail arrives wrapped in `https://www.google.com/url?q=…`
click tracking. The real src is `https://www.googletagmanager.com/gtag/js?id=AW-18361639983`.

## Thank-you page personalisation

`/thank-you/` greets the visitor by first name: *"Thanks, Jane — we've got your details"*.

The quote form puts the first name in `sessionStorage` under `gf-lead-name` and appends
`?name=` to the redirect, so the greeting survives both the fetch path and the native-post
fallback. `GREETING_SCRIPT` in `build/page_static.py` reads it inline, right after the
heading, so there is no flash of the generic text.

The value is **validated against a whitelist, not stripped**: anything with markup, digits
or an implausible length is discarded and the generic heading stands. It is written with
`textContent`, so markup could not execute even if it got through. The `name` parameter is
removed from the address bar on load, whether or not it was usable, so it is not carried
into a shared or bookmarked link. With no name — a direct visit, or JavaScript off — the
heading reads as it always did.

## Terms pages (unlisted)

Three pages carry the terms that go with quotes and invoices:

| URL | Page title | Source document |
| --- | --- | --- |
| `/terms/once-off/` | Residential Terms - Once-Off Work | `Green_Fern_Residential_Terms_Once_Off.docx` |
| `/terms/maintenance/` | Residential Terms - Ongoing Maintenance | `Green_Fern_Residential_Terms_Maintenance.docx` |
| `/terms/commercial/` | Commercial Terms - Ongoing Services | `Green_Fern_Commercial_Terms_Ongoing.docx` |

They are **unlisted on purpose**: no link from the nav, the footer or any other page,
excluded from `sitemap.xml`, and served `noindex, follow`. Only someone with the link
reaches them. They are deliberately *not* blocked in `robots.txt` — a disallowed page
can't be crawled, so Google would never see the `noindex` and could still list the URL.

**The wording is verbatim and must stay that way.** `build/terms_content.py` was generated
directly from the Word documents' XML, not retyped, and the build renders it unchanged.
The "Client: [CLIENT NAME] / Quote no:" line is omitted from the two residential
documents at the client's request — it belongs on the Word versions only.

To update the terms, get the new `.docx`, regenerate `build/terms_content.py` from it
rather than editing the file by hand, bump `LAST_UPDATED`, and re-run the build. A
paragraph-by-paragraph diff against the source document is the check that matters.

The pages also carry print styles, so a client can print or save one to PDF cleanly from
the browser.

## Content integrity

Two rules this repo enforces, both from client corrections:

- **Testimonials in `build/gfdata.py` are verbatim from greenfern.au**, with real names and
  roles. Never add, reword or invent a review — if a new one is needed, get the text from
  the client.
- **Photo alt text lives in the `PHOTOS` registry**, taken from the client's own site, and
  `img()`/`alt()` are always used together. Never write alt text inline at a call site —
  that's how photos end up next to content they don't show.

Service facts that were corrected and must not drift back:

| Claim | Correct version |
| --- | --- |
| Mowing frequency | Fortnightly Sept–April, four-weekly May–Aug. **No weekly mowing.** |
| Crew | Experienced and uniformed, but **not guaranteed the same crew** each visit |
| Timing | A cycle is agreed and a message goes out before the visit — **no guaranteed fixed day** |
| Tree removal | **Up to 8 metres.** Taller, near power lines, or needing climbing/crane = arborist |
| Slashing | **Waste is not removed** on slashing jobs; it is on removals and clean-ups |
| One-off work | Quoted **separately** from the ongoing maintenance price |

## Images — action needed before launch

Site egress in the build environment blocks Google Drive, so the client's photography could
not be committed to the repo. The six photos are currently referenced from Drive's public
CDN (`https://lh3.googleusercontent.com/d/<file-id>=w<width>`). They render for real
visitors, but they should be moved in-repo before launch for speed and reliability:

1. Download the six `.webp` files from the client's Drive folder into `assets/images/`.
2. In `build/gfdata.py`, change `img()` to return `/assets/images/<name>.webp`.
3. Re-run `python3 build/build.py`.

Two related follow-ups:

- **Alt text is now sourced from the client's own site**, recovered by parsing greenfern.au,
  so each photo sits with content that matches it. The mapping lives in `PHOTOS`.
- **`apple-touch-icon.png` is not present.** `/favicon.svg` covers everything except iOS
  home-screen icons; export a 180×180 PNG of the logo to `/apple-touch-icon.png` and add
  `<link rel="apple-touch-icon" href="/apple-touch-icon.png">` in `build/layout.py`.

The header/footer brand mark is an inline SVG fern, so the branding renders with no external
request. Swap it for the client's supplied logo file if preferred.

## Address masking

Only `Craigieburn VIC 3064` appears in the rendered page. The full street address stays in
the `LocalBusiness` JSON-LD, so crawlers, Google Business Profile matching and AI answer
engines still see the complete NAP. `build/gfdata.py` holds both: `ADDRESS_PUBLIC` for the
visible text and `STREET` for the schema.

If the client later wants the full address shown (it does help local pack consistency),
swap `ADDRESS_PUBLIC` for the full string in the footer, about and contact templates.

## Technical SEO in place

- Self-referencing `<link rel="canonical">` on every page
- Unique title (≤60 chars) and meta description (140–165 chars) per page
- `robots.txt` referencing `sitemap.xml`; `sitemap.xml` covering all 9 indexable pages
- JSON-LD: `LocalBusiness` (full NAP, ABN, geo, hours, all 11 suburbs in `areaServed`),
  `Service` on each service page, `FAQPage` on every page with an FAQ, `BreadcrumbList`,
  `WebSite`, `WebPage`/`CollectionPage`/`AboutPage`/`ContactPage`
- Open Graph + Twitter Card tags
- Critical CSS inlined; full stylesheet loaded async; JS deferred
- Every image has `alt`, explicit `width`/`height` and `loading="lazy"` below the fold
- All 11 service suburbs named as text on every page
- One `<h1>` per page, no heading-level skips

### One deviation worth flagging

The strategy asked for `Review` schema on the four testimonials. That is **not** included:
Google ignores self-serving review markup on `LocalBusiness` and it can trigger a structured
data manual action. The testimonials are still on the page as visible social proof. Review
rich results should come from Google Business Profile reviews instead.

## Local preview

```
python3 -m http.server 8000
```

Then open <http://127.0.0.1:8000/>. Clean URLs (`/services/lawn-mowing/`) work because each
page is an `index.html` in its own directory — no host rewrite rules needed.
