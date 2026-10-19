# -*- coding: utf-8 -*-
"""Terms pages.

Linked from quotes and invoices only: no nav or footer link anywhere on the site,
noindex, and excluded from sitemap.xml. The wording comes verbatim from
terms_content.py — never edit copy here.
"""

import html

from gfdata import BUSINESS, PHONE, PHONE_E164, EMAIL
from terms_content import TERMS, LAST_UPDATED
import layout as L

# Sentence-case description per page; these pages are noindex, so this only ever
# shows if someone shares the link in an app that unfurls it.
DESCRIPTIONS = {
    "once-off": "The terms that apply to once-off residential work quoted by Green Fern Gardening Services.",
    "maintenance": "The terms that apply to ongoing residential maintenance quoted by Green Fern Gardening Services.",
    "commercial": "The terms that apply to recurring commercial maintenance arranged with Green Fern Gardening Services.",
}


def _render(blocks):
    out = []
    for kind, text in blocks:
        safe = html.escape(text, quote=False)
        if kind == "h2":
            out.append('        <h2>%s</h2>' % safe)
        elif kind == "subtitle":
            out.append('        <p class="terms-subtitle">%s</p>' % safe)
        else:
            out.append('        <p>%s</p>' % safe)
    return "\n".join(out)


def build(slug):
    doc = TERMS[slug]
    title = doc["title"]
    page = {
        "path": "/terms/%s/" % slug,
        "title": "%s | %s" % (title, BUSINESS),
        "description": DESCRIPTIONS[slug],
        "noindex": True,
        "og_photo": "formal-hedge",
        "og_alt": BUSINESS,
        "schema": [],
    }

    html_parts = [L.head(page), L.header("")]
    html_parts.append('<main id="main">\n')
    html_parts.append("""<div class="page-head">
  <div class="wrap page-head-inner">
    <div class="page-head-copy">
      <span class="eyebrow">{business}</span>
      <h1>{title}</h1>
    </div>
  </div>
</div>

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="prose terms">
{body}
        <p class="terms-updated">Last updated: {updated}</p>
    </div>

    <aside class="terms-contact">
      <h2>Questions about these terms?</h2>
      <p>Call <a href="tel:{e164}">{phone}</a> or email <a href="mailto:{email}">{email}</a>.</p>
    </aside>
  </div>
</section>
""".format(business=BUSINESS, title=html.escape(title, quote=False),
           body=_render(doc["blocks"]), updated=LAST_UPDATED,
           e164=PHONE_E164, phone=PHONE, email=EMAIL))
    html_parts.append("</main>\n")
    html_parts.append(L.footer())
    html_parts.append(L.tail())
    return "".join(html_parts)
