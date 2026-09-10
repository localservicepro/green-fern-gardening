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
LAT = "-37.5991"
LON = "144.9407"

# GoHighLevel external tracking snippet (supplied by the client).
GHL_TRACKING_ID = "tk_eae768369958426d9896d163c30864d9"
GHL_TRACKING_SRC = "https://link.msgsndr.com/js/external-tracking.js"

SUBURBS = [
    "Craigieburn", "Lalor", "Epping", "Glenroy", "Campbellfield", "Broadmeadows",
    "Thomastown", "Reservoir", "Tullamarine", "Preston", "Northcote",
]

# Google Drive file IDs for the client's photography (folder is link-shared).
# Swap DRIVE_IMAGES for local files under /assets/images/ before launch — see README.
DRIVE = {
    "logo": "128MwkIZAvXBUfivoRjAQiTCWY2RhpRu7",
    "photo1": "1KnbrCKUAK70fJG729PIBQNgdufbISAQ6",
    "photo2": "1I0l-Zc-htytko8ecPI0U5LP8hC_QUeLc",
    "photo3": "1OG7YM-IvY3b_L3RS4n8fKYlZId7zZGSi",
    "photo4": "1nEsEhs1Vq7T6WKl1X0SfloCJ1BlreFVd",
    "photo5": "1IOOutPrtXJsHV9L9VycOwobuRl2C6PIs",
    "photo6": "1tUGvHhkgm6XaFEPHWrAJwMAx7JrIH1Vv",
}


def img(key, width=1200):
    """Public CDN URL for a Drive-hosted image at a given render width."""
    return "https://lh3.googleusercontent.com/d/%s=w%d" % (DRIVE[key], width)


SERVICES = [
    {
        "slug": "lawn-mowing",
        "nav": "Lawn Mowing",
        "dd_desc": "Scheduled weekly, fortnightly and monthly mowing.",
        "h1": "Lawn Mowing Services Melbourne — Scheduled Residential &amp; Commercial",
        "title": "Lawn Mowing Services Melbourne | Green Fern",
        "keyword": "Lawn Mowing Services Melbourne",
        "description": "Scheduled lawn mowing services across Melbourne’s north — weekly, fortnightly or monthly. Homes, schools, childcare and strata. Call 0420 462 848.",
        "card": "Set-and-forget mowing on a schedule you never have to chase. Edges, trims and clippings removed every visit.",
        "photo": "photo1",
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
        "photo": "photo2",
        "audience": "Established-garden suburbs — Preston, Northcote, Reservoir, Glenroy",
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
        "photo": "photo3",
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
        "photo": "photo4",
        "audience": "Homeowners renovating; second-highest local volume in the set",
    },
    {
        "slug": "tree-removal",
        "nav": "Tree Removal",
        "dd_desc": "Removals, block slashing and one-off clean-ups.",
        "h1": "Tree Removal Craigieburn — Removals, Slashing &amp; One-Off Works",
        "title": "Tree Removal Craigieburn | Block Slashing &amp; Clean-Ups",
        "keyword": "Tree Removal Craigieburn",
        "description": "Tree removal in Craigieburn — small tree and shrub removal, block slashing and one-off site clean-ups across Melbourne’s north. Call 0420 462 848.",
        "card": "Small tree and shrub removal, overgrown block slashing and full site clean-ups, waste taken away.",
        "photo": "photo5",
        "audience": "One-off high-value jobs",
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

TESTIMONIALS = [
    {
        "quote": "The grounds have never looked better and I never have to ring and ask. The day-before text means we can move the kids’ outdoor session without a scramble.",
        "name": "Centre Director",
        "role": "Early learning centre, Epping",
    },
    {
        "quote": "Marty’s team turn up when they say they will, work around our timetable and leave the site spotless. The paperwork side — the checks, the SWMS — was sorted before I had to ask.",
        "name": "School Principal",
        "role": "Primary school, Melbourne’s north",
    },
    {
        "quote": "We manage several properties and Green Fern is the only contractor I don’t have to chase. Consistent visits, consistent standard, one invoice.",
        "name": "Strata Manager",
        "role": "Owners’ corporation, Preston",
    },
    {
        "quote": "Booked for a one-off tidy-up and stayed on a fortnightly schedule. Lawn, edges and beds all done properly, and the price hasn’t moved.",
        "name": "Homeowner",
        "role": "Craigieburn",
    },
]

# Final FAQ copy from the approved SEO strategy.
FAQS_HOME = [
    ("Do you do lawn mowing in Craigieburn and Epping?",
     "Yes. Green Fern Gardening Services is based in Craigieburn and services Craigieburn, Epping, Lalor, Thomastown, Reservoir, Preston and the surrounding northern suburbs on scheduled weekly, fortnightly and monthly visits."),
    ("How much does hedge trimming cost in Melbourne’s north?",
     "Hedge trimming is priced on hedge length, height and how overgrown it is. Regular scheduled trimming costs considerably less per visit than a one-off restoration cut. Call 0420 462 848 for a site walkthrough and a fixed quote."),
    ("Are your gardeners Working With Children checked?",
     "Yes. Every Green Fern crew member holds a current Working With Children Check, and we operate under a JSEA and SWMS on every childcare, school and commercial site, backed by $10M public liability insurance."),
    ("How often should I have my lawn mowed in Melbourne?",
     "Weekly through spring, fortnightly over summer, and monthly through winter when growth slows. Green Fern sets a schedule per property up front so you never have to re-book or chase a visit date."),
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
