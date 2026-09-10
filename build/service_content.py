# -*- coding: utf-8 -*-
"""Long-form content for each service page. One target keyword each, no overlap."""

from gfdata import img, PHONE


class Content(object):
    def __init__(self, eyebrow, lede, body, faqs, faq_heading, areas_intro, cta_heading, cta_body):
        self.eyebrow = eyebrow
        self.lede = lede
        self.body = body
        self.faqs = faqs
        self.faq_heading = faq_heading
        self.areas_intro = areas_intro
        self.cta_heading = cta_heading
        self.cta_body = cta_body


def _prose(intro_html, photo_key, photo_alt, aside_html):
    return """<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="prose" data-reveal>
{intro}
      </div>
      <div data-reveal data-reveal-delay="1">
        <div class="split-media">
          <img src="{photo}" width="720" height="540" loading="lazy" decoding="async" alt="{alt}">
        </div>
        <div class="card" style="margin-top:20px">
{aside}
        </div>
      </div>
    </div>
  </div>
</section>
""".format(intro=intro_html, photo=img(photo_key, 720), alt=photo_alt, aside=aside_html)


def _detail(html):
    return """<section class="section section--tint">
  <div class="wrap wrap--narrow">
    <div class="prose" data-reveal>
{html}
    </div>
  </div>
</section>
""".format(html=html)


CONTENT = {}

# ------------------------------------------------------------------ lawn mowing
CONTENT["lawn-mowing"] = Content(
    eyebrow="Scheduled service · Melbourne north",
    lede="Lawn mowing services across Melbourne on a fixed schedule — weekly through spring, "
         "fortnightly over summer, monthly through winter. Residential, childcare, school, strata "
         "and commercial lawns, mowed by the same crew on the same day each cycle.",
    body=_prose(
        """<h2>Lawn mowing services in Melbourne, done on a schedule</h2>
<p>Most lawn mowing in Melbourne is sold as a one-off. You ring around, someone comes when they can, and six weeks later you are ringing around again. Green Fern Gardening Services works the other way: we set a cycle at the first walkthrough, lock in your visit day, and you stop thinking about it.</p>
<p>Every scheduled lawn mowing visit includes the mow, edging along paths, driveways and beds, line-trimming around obstacles, and clippings blown off hard surfaces and taken away. Nothing is billed as an extra afterwards — the price you agree is the price per visit.</p>
<h3>What a mowing visit actually covers</h3>
<ul>
  <li>Cut height set for the grass type and the season, not one blanket setting</li>
  <li>Edges cut along paths, driveways, fence lines and garden beds</li>
  <li>Line trimming around trees, posts, play equipment and air-conditioning units</li>
  <li>Clippings blown clear of paths and removed from site</li>
  <li>A quick look over the lawn — dry patches, drainage, pest damage — flagged to you</li>
</ul>""",
        "photo1",
        "Scheduled lawn mowing on a residential property in Melbourne’s northern suburbs",
        """<h4>Typical mowing cycles</h4>
<p style="font-size:.95rem"><strong>Spring (Sep–Nov):</strong> weekly — growth peaks and skipping a week doubles the work.<br>
<strong>Summer (Dec–Feb):</strong> fortnightly, with the cut height raised to hold moisture.<br>
<strong>Autumn (Mar–May):</strong> fortnightly, tapering as growth slows.<br>
<strong>Winter (Jun–Aug):</strong> monthly — mostly tidy-ups and leaf clearing.</p>""",
    ),
    faqs=[
        ("How much do lawn mowing services cost in Melbourne?",
         "Lawn mowing is priced per visit on lawn area, access and how much edging is involved — not by the hour. Properties on a regular weekly or fortnightly schedule pay noticeably less per visit than one-off cuts, because the grass never gets away. Call 0420 462 848 for a free walkthrough and a fixed per-visit price."),
        ("How often should a Melbourne lawn be mowed?",
         "Weekly through spring, fortnightly over summer and autumn, and monthly through winter when growth slows. Melbourne’s growth curve is steep in September and October, so a fortnightly cycle in spring usually means twice the work at each visit."),
        ("Do you mow commercial and strata lawns?",
         "Yes. Green Fern mows childcare centre, school, strata common area and commercial lawns across Melbourne’s north, with $10M public liability, Working With Children Checks and a JSEA and SWMS filed for every site."),
        ("Do I need to be home for the lawn mowing visit?",
         "No. Once we have gate access sorted, most clients are at work when we visit. You get an automated SMS the day before so gates can be unlocked and pets brought inside, and a note after the visit if anything needs your attention."),
        ("Do you take the grass clippings away?",
         "Yes. Clippings are blown off paths and driveways and removed from site as part of the standard visit — there is no extra green-waste charge on scheduled lawn mowing."),
    ],
    faq_heading="Lawn mowing questions",
    areas_intro="Scheduled lawn mowing runs across all eleven suburbs on our round. "
                "Craigieburn, Epping, Lalor and Thomastown share a route, so those properties "
                "usually get the earliest start date.",
    cta_heading="Get your lawn on a schedule",
    cta_body="A free walkthrough, a fixed price per visit, and a mowing day locked in before we start.",
)

# ------------------------------------------------------------------ hedge trimming
CONTENT["hedge-trimming"] = Content(
    eyebrow="Scheduled service · Melbourne north",
    lede="Hedge trimming in Melbourne — scheduled shaping to keep hedges level and dense, plus "
         "restoration cuts for hedges that have got away. Established gardens in Preston, "
         "Northcote, Reservoir and Glenroy are our most common hedging work.",
    body=_prose(
        """<h2>Hedge trimming in Melbourne, on a cycle that keeps hedges dense</h2>
<p>A hedge trimmed on a cycle stays thick, level and easy to maintain. A hedge left for two years goes woody in the middle, thins at the base, and needs a restoration cut that costs several times a regular visit — and takes a season to look right again.</p>
<p>Green Fern Gardening Services trims hedges across Melbourne’s northern suburbs on a schedule set to the species and its growth rate. Established-garden suburbs like Preston, Northcote and Reservoir are where most of our hedging work sits, alongside boundary and screening hedges on childcare, school and strata sites.</p>
<h3>Hedges we trim regularly</h3>
<ul>
  <li><strong>Box and English box</strong> — formal low hedging and borders, trimmed to hold a crisp line</li>
  <li><strong>Photinia and Viburnum</strong> — fast-growing screening hedges that need two to three cuts a year</li>
  <li><strong>Murraya and Lilly Pilly</strong> — dense screening, shaped so the base stays as wide as the top</li>
  <li><strong>Conifer and Cypress</strong> — trimmed inside the green growth, never back into bare wood</li>
  <li><strong>Boundary and screening hedges</strong> on strata, school and childcare sites</li>
</ul>
<p>Every trim includes shaping to a batter — slightly wider at the base than the top — so light reaches the bottom of the hedge and it does not go bare underneath. Clippings are collected and removed the same visit.</p>""",
        "photo2",
        "Hedge trimming and shaping on an established garden in Melbourne’s northern suburbs",
        """<h4>When to trim in Melbourne</h4>
<p style="font-size:.95rem"><strong>Late winter (Aug):</strong> the main structural cut, before the spring flush.<br>
<strong>Late spring (Nov):</strong> tidy the spring growth and reset the shape.<br>
<strong>Late summer (Feb):</strong> a light cut only — hard cuts in high heat scorch the exposed inner foliage.<br>
Avoid heavy cuts during heatwaves and while birds are nesting in dense screening hedges.</p>""",
    ),
    faqs=[
        ("How much does hedge trimming cost in Melbourne?",
         "Hedge trimming is priced on hedge length, height and how overgrown it is. Regular scheduled trimming costs considerably less per visit than a one-off restoration cut, because there is less material to cut and remove. Call 0420 462 848 for a site walkthrough and a fixed quote."),
        ("When should you trim hedges in Melbourne?",
         "The main structural cut is best in late winter, around August, before the spring growth flush. A second tidy in late spring resets the shape, and a light cut in late summer keeps it sharp. Avoid hard cuts during heatwaves — exposed inner foliage scorches."),
        ("How often does a hedge need to be trimmed?",
         "Fast growers like Photinia, Murraya and Lilly Pilly need two to three cuts a year to stay dense. Slower formal hedges such as box usually need two. Screening conifers are generally once or twice a year, always inside the green growth."),
        ("Can you fix a hedge that has been left too long?",
         "Usually, yes. An overgrown hedge is brought back over one or two seasons rather than in a single cut, so it is not taken back into bare wood all at once. We assess it on site and tell you honestly whether it can be restored or is better replaced."),
        ("Do you clean up and remove the hedge clippings?",
         "Yes. Clippings are collected, paths and beds are blown clear, and the green waste leaves with us at the end of the visit."),
    ],
    faq_heading="Hedge trimming questions",
    areas_intro="Hedge trimming is available across all eleven suburbs we service. "
                "The established gardens in Preston, Northcote, Reservoir and Glenroy carry "
                "most of our regular hedging rounds.",
    cta_heading="Book a hedge trim or a restoration cut",
    cta_body="We will tell you on site whether your hedge needs a regular trim or a staged "
             "restoration — and what each one costs.",
)

# ------------------------------------------------------------------ garden maintenance
CONTENT["garden-maintenance"] = Content(
    eyebrow="Scheduled service · Melbourne north",
    lede="Garden maintenance across Melbourne — scheduled grounds care and weed control for "
         "childcare centres, schools, strata common areas and commercial properties, plus homes "
         "that want the whole garden handled rather than just the lawn.",
    body=_prose(
        """<h2>Garden maintenance and weed control in Melbourne</h2>
<p>Garden maintenance is the whole-of-grounds contract: beds, weeds, mulch, pruning, leaf litter and playground surfaces, all on one schedule. It is the service most of our childcare, school and strata clients hold, because it means one contractor is accountable for how the site looks rather than four.</p>
<p>Weed control is included in every garden maintenance visit rather than billed as a separate call-out. On childcare and school sites we plan weed management around active areas and access windows, and use methods appropriate to grounds where children play.</p>
<h3>What a garden maintenance round covers</h3>
<ul>
  <li><strong>Weed control</strong> in beds, along fence lines, in paving joints and through gravel areas</li>
  <li><strong>Garden bed care</strong> — cultivating, edging beds back to a clean line, dead-heading and pruning</li>
  <li><strong>Mulch</strong> checked and topped up so beds hold moisture and suppress weed germination</li>
  <li><strong>Seasonal clean-ups</strong> — autumn leaf litter, spring growth flush, storm debris</li>
  <li><strong>Softfall and sandpit maintenance</strong> — levelling, top-ups and surface inspection on childcare and school sites</li>
  <li><strong>Reporting</strong> on anything that needs attention: drainage, dieback, damaged edging or play surfaces</li>
</ul>""",
        "photo3",
        "Scheduled garden maintenance and weed control on grounds in Melbourne’s northern suburbs",
        """<h4>Built for compliance sites</h4>
<p style="font-size:.95rem">Every crew member holds a current Working With Children Check. We operate under a JSEA and SWMS on every childcare, school and commercial site, and carry $10M public liability cover. Visits are scheduled around session times and access windows, and documentation is provided before the first visit rather than after you ask.</p>""",
    ),
    faqs=[
        ("What does garden maintenance include?",
         "Green Fern’s garden maintenance covers weed control, garden bed cultivation and edging, pruning and dead-heading, mulch top-ups, seasonal leaf and debris clean-ups, and softfall or sandpit maintenance on childcare and school sites. Lawn mowing can be added to the same visit."),
        ("Is weed control charged separately?",
         "No. Weed control is part of every scheduled garden maintenance visit, covering beds, fence lines, paving joints and gravel areas. Treating weeds on a cycle stops seed set, which is why regular sites need far less intervention over time."),
        ("Do you maintain childcare centre and school grounds in Melbourne’s north?",
         "Yes. Childcare centres, schools and strata properties are Green Fern’s core work, including softfall and sandpit top-ups, levelling and playground surface inspection, scheduled around active sites and access windows."),
        ("Is your weed control safe around children and pets?",
         "We select methods to suit the site. On childcare, school and family properties that means favouring mechanical removal and mulch suppression in play areas, and scheduling any treatment for times when the area is not in use, with re-entry periods observed."),
        ("Can strata committees get one contract for all common areas?",
         "Yes. Strata and owners’ corporation grounds are covered on a single scheduled contract with one invoice, one point of contact and a consistent standard across every common area and frontage."),
    ],
    faq_heading="Garden maintenance questions",
    areas_intro="Garden maintenance rounds cover all eleven suburbs. Childcare, school and strata "
                "sites across Melbourne’s northern corridor make up most of this work.",
    cta_heading="Put the whole grounds contract on one schedule",
    cta_body="One contractor, one invoice, and compliance paperwork in place before the first visit.",
)

# ------------------------------------------------------------------ soft landscaping
CONTENT["soft-landscaping"] = Content(
    eyebrow="Project work · Craigieburn",
    lede="Soft landscaping in Craigieburn — garden bed renovations, soil preparation, planting, "
         "mulching and turf laying. The planting side of landscaping, done so it still looks right "
         "in three years rather than three months.",
    body=_prose(
        """<h2>Soft landscaping and garden renovations in Craigieburn</h2>
<p>Soft landscaping is everything that grows: soil, plants, mulch and turf. Green Fern Gardening Services renovates tired garden beds and lays new turf across Craigieburn and Melbourne’s northern suburbs — and because we also maintain gardens, we plant things that survive a Craigieburn summer rather than things that look good on delivery day.</p>
<p>Most jobs start the same way: beds that were planted once, never mulched, and are now half weed. We strip them back, fix the soil, replant to a plan that suits the aspect, and mulch properly. The maintenance load afterwards drops sharply.</p>
<h3>What soft landscaping work covers</h3>
<ul>
  <li><strong>Garden bed renovation</strong> — clearing, reshaping and re-edging beds to a clean line</li>
  <li><strong>Soil preparation</strong> — decompacting, improving and conditioning before anything is planted</li>
  <li><strong>Planting</strong> selected for aspect, exposure and Craigieburn’s hot, dry summers</li>
  <li><strong>Mulching</strong> to the right depth to hold moisture and stop weed germination</li>
  <li><strong>Turf laying</strong> — ground preparation, levelling, laying and an establishment watering plan</li>
  <li><strong>Screening and hedging</strong> planted at correct spacing for the mature size, not the pot size</li>
</ul>
<p>We do not take on hard landscaping — paving, retaining walls, decking or structural work. If a job needs it, we will say so up front rather than take it on and sub it out.</p>""",
        "photo4",
        "Soft landscaping and garden bed renovation completed in Craigieburn",
        """<h4>Planted for a Craigieburn summer</h4>
<p style="font-size:.95rem">Craigieburn gets hot, dry and windy from December through February, on soils that compact hard. Plant choices that work in a sheltered inner-north garden often fail here. We plant to the actual site — aspect, wind exposure and soil — and mulch deep enough that the bed holds moisture between waterings.</p>""",
    ),
    faqs=[
        ("What is the difference between soft and hard landscaping?",
         "Soft landscaping is the living material — soil preparation, planting, mulch and turf. Hard landscaping is built structure such as paving, retaining walls and decking. Green Fern does soft landscaping only, and will tell you up front if a job needs a hard landscaping trade."),
        ("How much does landscaping cost in Craigieburn?",
         "Soft landscaping is quoted per project after a site visit, based on bed area, how much clearing and soil work is needed, plant numbers and mulch volume. Turf is quoted on area plus preparation. Call 0420 462 848 for a walkthrough and a written quote."),
        ("When is the best time to lay turf in Melbourne?",
         "Spring and early autumn are best — warm enough for roots to establish, without the heat stress of midsummer. Turf laid in January needs far more watering to survive. We set an establishment watering plan with every turf job."),
        ("Do you maintain the garden after the renovation?",
         "Most clients move onto a scheduled garden maintenance round once the new beds are in, which is when plantings are most vulnerable. It is not a requirement, but a renovated bed left unmaintained for a year usually undoes the work."),
        ("Can you replant a garden that keeps dying?",
         "Usually the problem is soil compaction, aspect or plant choice rather than neglect. We assess the site first and tell you which of the three it is before quoting anything — sometimes the fix is soil work rather than new plants."),
    ],
    faq_heading="Soft landscaping questions",
    areas_intro="Soft landscaping and turf projects run across all eleven suburbs, with most "
                "garden renovation work concentrated in Craigieburn and the surrounding "
                "northern growth corridor.",
    cta_heading="Get a soft landscaping quote",
    cta_body="A walkthrough, an honest read on what the site actually needs, and a written "
             "quote covering soil, plants, mulch and turf.",
)

# ------------------------------------------------------------------ tree removal
CONTENT["tree-removal"] = Content(
    eyebrow="One-off works · Craigieburn",
    lede="Tree removal in Craigieburn — small tree and shrub removal, overgrown block slashing and "
         "full site clean-ups across Melbourne’s northern suburbs, with all green waste taken away.",
    body=_prose(
        """<h2>Tree removal, block slashing and clean-ups in Craigieburn</h2>
<p>Green Fern Gardening Services handles the one-off jobs that scheduled maintenance does not cover: small trees and shrubs that have outgrown their spot, self-seeded growth along fence lines, and blocks that have not been touched in two seasons. Everything is cut, cleared and taken away in the same visit.</p>
<p>We remove small trees and shrubs within safe reach from the ground. Large trees, anything near power lines, and any removal needing climbing or a crane is work for a qualified arborist — we will tell you that on site and, where we can, point you to someone who does it. What we will not do is take on a removal that should not be done from the ground.</p>
<h3>One-off works we take on</h3>
<ul>
  <li><strong>Small tree and shrub removal</strong> — overgrown plantings, self-seeded growth, dead or failing shrubs</li>
  <li><strong>Block slashing</strong> — vacant blocks and overgrown yards cut back to manageable ground</li>
  <li><strong>Fence line clearing</strong> — blackberry, woody weeds and volunteer growth along boundaries</li>
  <li><strong>Site clean-ups</strong> — pre-sale tidy-ups, end-of-lease clears and post-storm debris</li>
  <li><strong>Green waste removal</strong> — everything cut leaves with us, no skip needed</li>
</ul>""",
        "photo5",
        "Tree and shrub removal and site clean-up completed in Craigieburn",
        """<h4>Before you book a removal</h4>
<p style="font-size:.95rem">Many Victorian councils protect trees over a certain height or trunk diameter, and some properties carry planning overlays that require a permit before removal. Check with your council first — we will flag it if a tree looks like it falls under local protection, but the permit is the property owner’s responsibility.</p>""",
    ),
    faqs=[
        ("How much does tree removal cost in Craigieburn?",
         "Tree removal is quoted per job after a site visit, based on size, access, what is underneath it and how much green waste comes out. Block slashing is quoted on area and how heavy the growth is. Call 0420 462 848 for a walkthrough and a fixed price."),
        ("Do I need a council permit to remove a tree in Craigieburn?",
         "Often yes. Hume City Council and most Victorian councils protect trees above a certain height or trunk circumference, and some properties sit under planning overlays. Check with your council before booking — we will flag a tree that looks protected, but the permit is the owner’s responsibility."),
        ("Do you remove large trees?",
         "No. Green Fern removes small trees and shrubs that can be taken down safely from the ground. Large trees, anything near power lines and any removal needing climbing or a crane is arborist work, and we will say so on site rather than take it on."),
        ("Do you slash overgrown blocks?",
         "Yes. Vacant blocks and overgrown yards across Craigieburn and Melbourne’s north are cut back to manageable ground, with fence lines cleared and all cut material removed."),
        ("Do you take the green waste away?",
         "Yes. Everything cut is removed as part of the job — there is no skip to hire and nothing left stacked on the nature strip."),
    ],
    faq_heading="Tree removal questions",
    areas_intro="One-off removals, block slashing and clean-ups are available across all eleven "
                "suburbs, with most work in Craigieburn and the surrounding growth corridor.",
    cta_heading="Book a removal or a block clean-up",
    cta_body="Tell us what is there and we will give you a fixed price, with all green waste taken away.",
)
