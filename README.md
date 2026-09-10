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

## Images — action needed before launch

Site egress in the build environment blocks Google Drive, so the client's photography could
not be committed to the repo. The six photos are currently referenced from Drive's public
CDN (`https://lh3.googleusercontent.com/d/<file-id>=w<width>`). They render for real
visitors, but they should be moved in-repo before launch for speed and reliability:

1. Download the six `.webp` files from the client's Drive folder into `assets/images/`.
2. In `build/gfdata.py`, change `img()` to return `/assets/images/<name>.webp`.
3. Re-run `python3 build/build.py`.

Two related follow-ups:

- **Alt text needs a check.** The photos could not be viewed from the build environment, so
  alt text describes the service context rather than the specific photo. Confirm each one
  matches what is actually in the image.
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
