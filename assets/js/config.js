/* Site configuration — edit this file, nothing else, to set the Google Ads
 * conversions. Nothing here is secret; it ships to the browser.
 */
window.GF_CONFIG = {

  /* Quote forms post to Sales Brain (the form's action attribute, set in
   * build/gfdata.py as LEAD_ACTION), which puts each lead into GoHighLevel.
   * There is nothing to configure here for leads. */
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

    /* Phone-number taps. Fires on any tel: link on the site — header button,
     * hero, CTA bands and footer. Label and value supplied by the client from
     * Google Ads > Goals > Conversions. */
    call: {
      label: '_prRCKGs-qIdEK_IwbNE',
      value: 1.0,
      currency: 'AUD'
    },

    /* Quote form. Deliberately empty: the form conversion is configured in
     * Google Ads as a page-load conversion on /thank-you/. Putting a label here
     * as well would fire a second conversion on submit and count every enquiry
     * twice. Only fill this in if that Ads conversion is switched to an event. */
    form: {
      label: ''
    }
  }
};
