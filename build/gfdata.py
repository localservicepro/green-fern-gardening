# -*- coding: utf-8 -*-
"""Shared data and layout for the Green Fern Gardening Services site."""

import json

SITE_URL = "https://www.greenfern.au"
BUSINESS = "Green Fern Gardening Services"
OWNER = "Marty Searle"
PHONE = "0420 462 848"
PHONE_E164 = "+61420462848"
EMAIL = "marty@greenfern.au"
ABN = "29 279 087 766"
STREET = "101 Dianne Ave"
SUBURB = "Craigieburn"
STATE = "VIC"
POSTCODE = "3064"
# Shown on the page. The full street address stays in the LocalBusiness JSON-LD
# below so crawlers and AI answer engines still get the complete NAP.
ADDRESS_PUBLIC = "Craigieburn VIC 3064"

LAT = "-37.5991"
LON = "144.9407"

# Google Ads account tag. Conversion *labels* are runtime values and live in
# assets/js/config.js; only the account id is needed to emit the tag itself.
GOOGLE_ADS_ID = "AW-18361639983"

# GoHighLevel external tracking snippet (supplied by the client).
GHL_TRACKING_ID = "tk_eae768369958426d9896d163c30864d9"
GHL_TRACKING_SRC = "https://link.msgsndr.com/js/external-tracking.js"

# The four suburbs the client leads with — spread across the corridor so the
# in-between suburbs read as covered. The full list still drives areaServed,
# the footer and the service-areas section.
MAIN_SUBURBS = ["Craigieburn", "Glenroy", "Thomastown", "Preston"]

SUBURBS = [
    "Craigieburn", "Lalor", "Epping", "Glenroy", "Campbellfield", "Broadmeadows",
    "Thomastown", "Reservoir", "Tullamarine", "Preston", "Northcote",
]

# Client photography, hosted in the shared Drive folder.
# Each photo carries the alt text from the client's own site, so a photo can never be
# placed against content it doesn't show. Add the file id and the alt text together.
LOGO_ID = "128MwkIZAvXBUfivoRjAQiTCWY2RhpRu7"

PHOTOS = {
    "laid-turf": {
        "id": "1OG7YM-IvY3b_L3RS4n8fKYlZId7zZGSi",
        "alt": "Freshly laid turf with a crisp cut edge, maintained by Green Fern Gardening Services",
    },
    "formal-hedge": {
        "id": "1I0l-Zc-htytko8ecPI0U5LP8hC_QUeLc",
        "alt": "Formal hedge trimmed level to a resort-style finish by Green Fern Gardening Services",
    },
    "turf-renovation": {
        "id": "1KnbrCKUAK70fJG729PIBQNgdufbISAQ6",
        "alt": "Backyard turf renovation by Green Fern Gardening Services, ground preparation through to finished lawn",
    },
    "childcare-beds": {
        "id": "1nEsEhs1Vq7T6WKl1X0SfloCJ1BlreFVd",
        "alt": "Garden beds and play area maintained at a childcare centre in Melbourne’s north",
    },
    "strata-driveway": {
        "id": "1IOOutPrtXJsHV9L9VycOwobuRl2C6PIs",
        "alt": "Strata driveway with maintained hedges and topiary kept on a scheduled round",
    },
    "hedge-reduction": {
        "id": "1tUGvHhkgm6XaFEPHWrAJwMAx7JrIH1Vv",
        "alt": "Hedge reduction before and after, cut back to a level resort-style finish",
    },
}


def img(key, width=1200):
    """Public CDN URL for a client photo at a given render width."""
    file_id = LOGO_ID if key == "logo" else PHOTOS[key]["id"]
    return "https://lh3.googleusercontent.com/d/%s=w%d" % (file_id, width)


def alt(key):
    """The verified alt text for a photo. Never write alt text inline."""
    return PHOTOS[key]["alt"]


SERVICES = [
    {
        "slug": "lawn-mowing",
        "nav": "Lawn Mowing",
        "dd_desc": "Fortnightly Sept–April, four-weekly May–Aug.",
        "h1": "Lawn Mowing Services Melbourne — Scheduled Residential &amp; Commercial",
        "title": "Lawn Mowing Services Melbourne | Green Fern",
        "keyword": "Lawn Mowing Services Melbourne",
        "description": "Scheduled lawn mowing across Melbourne’s north — fortnightly September to April, four-weekly May to August. Homes, schools, childcare and strata. Call 0420 462 848.",
        "card": "Mowing on a set cycle you never have to chase — fortnightly through the growing season, four-weekly over winter.",
        "photo": "laid-turf",
        "audience": "Homeowners and facility managers wanting a set schedule, not a one-off",
    },
    {
        "slug": "hedge-trimming",
        "nav": "Hedge Trimming",
        "dd_desc": "Regular hedging, pruning and garden bed care.",
        "h1": "Hedge Trimming Melbourne — Regular Hedging, Pruning &amp; Garden Beds",
        "title": "Hedge Trimming Melbourne | Preston, Reservoir &amp; North",
        "keyword": "Hedge Trimming Melbourne",
        "description": "Hedge trimming in Melbourne’s north — scheduled hedging, shaping and restoration cuts in Preston, Reservoir, Northcote and Glenroy. Call 0420 462 848.",
        "card": "Shaped, level hedges kept on a cycle — plus restoration cuts for hedges that have got away.",
        "photo": "formal-hedge",
        "audience": "Established gardens around Preston, Glenroy and Northcote",
    },
    {
        "slug": "garden-maintenance",
        "nav": "Garden Maintenance",
        "dd_desc": "Grounds care, weed control, seasonal clean-ups.",
        "h1": "Garden Maintenance Melbourne — Scheduled Grounds Care &amp; Weed Control",
        "title": "Garden Maintenance Melbourne | Schools &amp; Strata",
        "keyword": "Garden Maintenance Melbourne",
        "description": "Scheduled garden maintenance and weed control across Melbourne’s north for childcare centres, schools, strata and commercial grounds. Call 0420 462 848.",
        "card": "Whole-of-grounds care on a fixed cycle — beds, weeds, mulch, leaf litter and playground surfaces.",
        "photo": "childcare-beds",
        "audience": "Childcare centres, schools, strata managers, owners’ corporations",
    },
    {
        "slug": "soft-landscaping",
        "nav": "Soft Landscaping",
        "dd_desc": "Garden renovations, beds, mulch and turf.",
        "h1": "Landscaping Craigieburn — Soft Landscaping &amp; Garden Renovations",
        "title": "Landscaping Craigieburn | Soft Landscaping &amp; Garden Beds",
        "keyword": "Landscaping Craigieburn",
        "description": "Soft landscaping in Craigieburn — garden bed renovations, planting, mulching and turf laying across Melbourne’s northern suburbs. Call 0420 462 848.",
        "card": "Tired beds rebuilt: soil prep, planting, mulch and turf that still looks right in three years.",
        "photo": "turf-renovation",
        "audience": "Homeowners renovating a tired garden or laying new turf",
    },
    {
        "slug": "tree-removal",
        "nav": "Other Services",
        "dd_desc": "Tree removal, slashing, hedge reductions, one-off works.",
        "h1": "Other Services — Tree Removal, Block Slashing &amp; One-Off Works",
        "title": "Tree Removal Craigieburn | Block Slashing &amp; Clean-Ups",
        "keyword": "Tree Removal Craigieburn",
        "description": "Tree removal up to 8 metres in Craigieburn, plus block slashing, hedge reductions and one-off garden works across Melbourne’s north. Call 0420 462 848.",
        "card": "Tree removal up to 8 metres, block slashing, hedge reductions and one-off project work, quoted separately.",
        "photo": "hedge-reduction",
        "audience": "One-off and project work, quoted separately from regular service",
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

# Verbatim from greenfern.au. Do not edit the wording and never add to this list
# without the client supplying the review.
TESTIMONIALS = [
    {
        "quote": "Marty works his magic every visit, especially when it comes to returning the sand to the sandpits, ready for the children to enthusiastically spread it far and wide all over again. The service always looks fresh, tidy and beautifully maintained after he has been, and the children genuinely love watching him in action. With Marty and Green Fern Gardening, it is one thing we never have to think twice about.",
        "name": "Liz",
        "role": "Service Manager, Where We Grow",
    },
    {
        "quote": "We have found Green Fern to be such a positive experience. They are always reliable, communicate clearly, and take real pride in how everything looks every time they visit our service. It makes a big difference when we have our garden cared for by Green Fern always to a high standard without needing to follow anything up.",
        "name": "Sena",
        "role": "Centre Director, Busy Bees",
    },
    {
        "quote": "We have been incredibly impressed with Green Fern from start to finish. Not only do they do a fantastic job with the garden itself, but the way they leave the property afterwards is outstanding, everything is always neat, tidy and beautifully presented. Their reliability has also been a huge plus.",
        "name": "Meghan",
        "role": "Centre Director, Busy Bees",
    },
    {
        "quote": "Working with Marty has been an excellent experience for our school. The service provided is consistently efficient, reliable, and highly productive. Marty is responsive to our needs, ensures tasks are completed promptly, and maintains a high standard of work, making a valuable contribution to the smooth running of our school operations.",
        "name": "Ameera",
        "role": "Primary School Principal",
    },
]

# Final FAQ copy from the approved SEO strategy.
FAQS_HOME = [
    ("Do you do lawn mowing in Craigieburn and Epping?",
     "Yes. Green Fern Gardening Services is based in Craigieburn and services Craigieburn, Glenroy, Thomastown, Preston and the surrounding northern suburbs. Mowing runs fortnightly from September to April and four-weekly from May to August."),
    ("How much does hedge trimming cost in Melbourne’s north?",
     "Hedge trimming is priced on hedge length, height and how overgrown it is. Regular scheduled trimming costs considerably less per visit than a one-off restoration cut. Call 0420 462 848 for a site walkthrough and a fixed quote."),
    ("Are your gardeners Working With Children checked?",
     "Yes. Every Green Fern crew member holds a current Working With Children Check, and we operate under a JSEA and SWMS on every childcare, school and commercial site, backed by $10M public liability insurance."),
    ("How often should I have my lawn mowed in Melbourne?",
     "Green Fern mows fortnightly from September to April while grass is growing, and four-weekly from May to August when growth slows. The cycle is agreed at the walkthrough, so you never have to re-book or chase a visit."),
    ("Do you maintain childcare centre and school grounds in Melbourne’s north?",
     "Yes. Childcare centres, schools and strata properties are Green Fern’s core work, including softfall and sandpit top-ups, levelling and playground surface inspection, scheduled around active sites and access windows."),
    ("Which Melbourne suburbs does Green Fern service?",
     "Craigieburn, Lalor, Epping, Glenroy, Campbellfield, Broadmeadows, Thomastown, Reservoir, Tullamarine, Preston and Northcote."),
]


def jsonld(obj):
    return ('<script type="application/ld+json">\n'
            + json.dumps(obj, indent=2, ensure_ascii=False)
            + "\n</script>")


def local_business_node():
    """Shared LocalBusiness entity, referenced by @id from every page."""
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": SITE_URL + "/#business",
        "name": BUSINESS,
        "url": SITE_URL + "/",
        "telephone": PHONE_E164,
        "email": EMAIL,
        "founder": {"@type": "Person", "name": OWNER},
        "description": ("Scheduled lawn mowing, hedge trimming and garden maintenance for homes, "
                        "childcare centres, schools, strata and commercial properties across "
                        "Craigieburn and Melbourne’s northern suburbs."),
        "image": img("logo", 1024),
        "logo": img("logo", 512),
        "priceRange": "$$",
        "identifier": {"@type": "PropertyValue", "name": "ABN", "value": ABN},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": SUBURB,
            "addressRegion": STATE,
            "postalCode": POSTCODE,
            "addressCountry": "AU",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
        "areaServed": [{"@type": "City", "name": s} for s in SUBURBS],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "07:00", "closes": "17:00",
        }, {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Saturday"], "opens": "08:00", "closes": "13:00",
        }],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Gardening and grounds maintenance services",
            "itemListElement": [{
                "@type": "Offer",
                "itemOffered": {"@type": "Service", "name": s["keyword"],
                                "url": "%s/services/%s/" % (SITE_URL, s["slug"])},
            } for s in SERVICES],
        },
    }
