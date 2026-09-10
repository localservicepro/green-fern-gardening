/* Site configuration — edit this file, nothing else, to connect the CRM.
 *
 * ghlEndpoint: the URL the quote form POSTs to as JSON. Use either
 *   - a GoHighLevel inbound webhook trigger URL, or
 *   - your own endpoint that forwards to the GHL contacts API.
 * Leave it empty and the form tells visitors to call instead of failing silently.
 */
window.GF_CONFIG = {
  ghlEndpoint: '',
  thankYouPath: '/thank-you/'
};
