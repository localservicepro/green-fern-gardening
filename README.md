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

## Connecting the quote form to GoHighLevel

The form posts JSON with field names that map 1:1 to the GHL contact fields:

| Form field | GHL merge field |
| --- | --- |
| `full_name` | `{{contact.full_name}}` |
| `email` | `{{contact.email}}` |
| `phone` | `{{contact.phone}}` |
| `property_address` | `{{contact.property_address}}` |
| `property_size` | `{{contact.property_size}}` |
| `service_needed` | `{{contact.service_needed}}` |
| `job_notes` | `{{contact.job_notes}}` |

`property_address`, `property_size`, `service_needed` and `job_notes` are custom fields —
create them in GHL under **Settings → Custom Fields** with exactly those keys before going live.

The form is rendered twice on most pages: once in the header popup (opened by the
**Get a free quote** button, present on every page) and once inline — in the hero on
`/contact/`. Both instances share one handler and one endpoint; element ids are prefixed
per instance so nothing collides.

**One thing is left to do:** set the endpoint in `assets/js/config.js`:

```js
window.GF_CONFIG = {
  ghlEndpoint: 'https://services.leadconnectorhq.com/hooks/…',  // GHL inbound webhook URL
  thankYouPath: '/thank-you/'
};
```

Until that is filled in, the form validates but tells visitors to call instead of failing
silently. On success it redirects to `/thank-you/`, which is where the conversion fires.

The GHL external tracking script (`tk_eae768369958426d9896d163c30864d9`) is already loaded
site-wide from `build/layout.py`, so attribution is captured on every page including the
thank-you redirect.

## Tracking

**Google Ads tag.** `AW-18361639983` is emitted as gtag.js high in `<head>` on every page,
including `/thank-you/` and the unlisted terms pages. The account id lives in
`build/gfdata.py` as `GOOGLE_ADS_ID`.

**Conversions** are wired in `assets/js/site.js` and configured in `assets/js/config.js`:

| Conversion | Fires | Config key |
| --- | --- | --- |
| Phone click | Any `a[href^="tel:"]` — header, hero, CTA bands, footer | `googleAds.callConversionLabel` |
| Quote form | On a successful submit, immediately before the `/thank-you/` redirect | `googleAds.formConversionLabel` |

Paste in only the label — the part after the slash in `AW-18361639983/AbC-D_efG…`. With a
label empty that conversion silently does nothing; with the tag blocked, `adsConversion()`
falls through on a 1-second timeout. Neither can stop a call being placed or a form being
submitted.

Use **either** `formConversionLabel` **or** a page-load conversion on `/thank-you/` in the
Ads UI — not both, or submissions are counted twice.

**The GoHighLevel tracking script and gtag.js do not conflict** — separate libraries, no
shared globals. But note that while `ghlEndpoint` is empty the form never submits and
nobody reaches `/thank-you/`, so there is nothing for either to record.

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
