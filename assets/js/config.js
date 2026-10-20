/* Site configuration — edit this file, nothing else, to connect the CRM and
 * Google Ads conversions. Nothing here is secret; it ships to the browser.
 */
window.GF_CONFIG = {

  /* How a quote form submission reaches the CRM.
   *
   *   'tracking-script' (current) — the GoHighLevel external tracking script
   *       loaded in <head> captures the submit event and creates the contact.
   *       Nothing else to configure. Confirmed working by test submission.
   *
   *   'webhook' — the form POSTs the fields as JSON to ghlEndpoint below.
   *       Only needed if the tracking script stops doing the capture.
   */
  leadCapture: 'tracking-script',

  /* Only read when leadCapture is 'webhook'. */
  ghlEndpoint: '',

  thankYouPath: '/thank-you/',

  /* Google Ads conversions.
   *
   * The account tag (AW-18361639983) is emitted in <head> on every page and
   * needs nothing here. These two labels are the per-conversion halves of a
   * send_to value — the part after the slash in
   *     AW-18361639983/AbC-D_efG-h12_34-567
   * Copy the label out of the conversion action's snippet in
   * Google Ads > Goals > Conversions, and paste it in. Leave a label empty and
   * that conversion simply doesn't fire; nothing else breaks.
   */
  googleAds: {
    id: 'AW-18361639983',

    /* Fires when a visitor taps any phone-number link or call button. */
    callConversionLabel: '',

    /* Fires the moment the quote form submits successfully, just before the
     * redirect to /thank-you/. Optional: if the conversion is set up in Ads as
     * a page-load on /thank-you/ instead, leave this empty. Don't use both, or
     * the conversion is counted twice. */
    formConversionLabel: ''
  }
};
