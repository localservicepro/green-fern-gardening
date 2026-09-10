# -*- coding: utf-8 -*-
"""The quote form. Rendered more than once per page (inline + modal), so every
instance takes a prefix to keep element ids unique."""

from gfdata import PHONE, PHONE_E164, SERVICES


def quote_form(prefix, heading="Request your free quote",
               intro="Tell us about the property and we will book a walkthrough. Most quotes go out within one business day.",
               classes="form-card", heading_level="h2"):
    def fid(name):
        return "%s-%s" % (prefix, name)

    service_options = "\n".join(
        '            <option value="%s">%s</option>' % (s["nav"], s["nav"]) for s in SERVICES)

    intro_html = '<p class="form-intro">%s</p>' % intro if intro else ""
    heading_html = ('<{hl} class="form-heading">{h}</{hl}>'.format(hl=heading_level, h=heading)
                    if heading else "")

    return """<form class="{classes} quote-form" data-thank-you="/thank-you/" novalidate>
  {heading}
  {intro}

  <!-- Honeypot: hidden from people, filled by bots. -->
  <div class="hp-field" aria-hidden="true">
    <label for="{f_hp}">Leave this field empty</label>
    <input type="text" id="{f_hp}" name="company_website" tabindex="-1" autocomplete="off">
  </div>

  <div class="field">
    <label for="{f_name}">Full name <span class="req" aria-hidden="true">*</span></label>
    <input type="text" id="{f_name}" name="full_name" autocomplete="name" required placeholder="Marty Searle">
    <span class="err" role="alert">This field is required.</span>
  </div>

  <div class="field-row">
    <div class="field">
      <label for="{f_email}">Email <span class="req" aria-hidden="true">*</span></label>
      <input type="email" id="{f_email}" name="email" autocomplete="email" inputmode="email" required placeholder="you@example.com.au">
      <span class="err" role="alert">This field is required.</span>
    </div>
    <div class="field">
      <label for="{f_phone}">Phone <span class="req" aria-hidden="true">*</span></label>
      <input type="tel" id="{f_phone}" name="phone" autocomplete="tel" inputmode="tel" required placeholder="0400 000 000">
      <span class="err" role="alert">This field is required.</span>
    </div>
  </div>

  <div class="field">
    <label for="{f_addr}">Property address <span class="req" aria-hidden="true">*</span></label>
    <input type="text" id="{f_addr}" name="property_address" autocomplete="street-address" required placeholder="12 Example Street, Craigieburn VIC 3064">
    <span class="err" role="alert">This field is required.</span>
  </div>

  <div class="field-row">
    <div class="field">
      <label for="{f_size}">Property size</label>
      <select id="{f_size}" name="property_size">
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
      <label for="{f_service}">Service needed <span class="req" aria-hidden="true">*</span></label>
      <select id="{f_service}" name="service_needed" required>
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
    <label for="{f_notes}">Job notes</label>
    <textarea id="{f_notes}" name="job_notes" rows="4" placeholder="How often you would like visits, gate or pet access, anything that has been left too long, and any site requirements."></textarea>
  </div>

  <button class="btn btn--primary btn--block" type="submit">Get my free quote</button>
  <div class="form-status" role="status" aria-live="polite"></div>
  <p class="form-note">We use your details to prepare your quote and contact you about it. No marketing lists. Prefer to talk? Call <a href="tel:{e164}">{phone}</a>.</p>
</form>""".format(
        classes=classes,
        heading=heading_html,
        intro=intro_html,
        f_hp=fid("company_website"), f_name=fid("full_name"), f_email=fid("email"),
        f_phone=fid("phone"), f_addr=fid("property_address"), f_size=fid("property_size"),
        f_service=fid("service_needed"), f_notes=fid("job_notes"),
        service_options=service_options, e164=PHONE_E164, phone=PHONE,
    )


def quote_modal():
    """Site-wide popup opened by the header CTA."""
    return """<div class="modal" id="quote-modal" hidden>
  <div class="modal-backdrop" data-modal-close></div>
  <div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="quote-modal-title">
    <button class="modal-close" type="button" data-modal-close aria-label="Close">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>
    </button>
    <div class="modal-body">
{form}
    </div>
  </div>
</div>
""".format(form=quote_form(
        "qf-modal",
        heading='<span id="quote-modal-title">Get a free quote</span>',
        intro="Free on-site walkthrough, a fixed price per visit, and a schedule locked in before we start.",
        classes="modal-form",
    ))
