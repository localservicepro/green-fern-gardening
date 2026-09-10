#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the static site into the repository root.

    python3 build/build.py

Edit the templates in build/ and re-run; the emitted HTML is committed so the
site can be deployed as plain static files with no build step on the host.
"""

import os
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from gfdata import SITE_URL, SERVICES  # noqa: E402
import page_home, page_services, page_static, service_content  # noqa: E402


def write(rel_path, content):
    path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("  %-42s %6.1f KB" % (rel_path, len(content.encode("utf-8")) / 1024.0))


def main():
    print("Building Green Fern Gardening Services…")

    write("index.html", page_home.build())
    write("services/index.html", page_services.build_hub())
    for s in SERVICES:
        write("services/%s/index.html" % s["slug"],
              page_services.build_service(s, service_content.CONTENT[s["slug"]]))
    write("about/index.html", page_static.build_about())
    write("contact/index.html", page_static.build_contact())
    write("thank-you/index.html", page_static.build_thank_you())
    write("404.html", page_static.build_404())

    # ---- robots.txt ----
    write("robots.txt", """User-agent: *
Allow: /
Disallow: /thank-you/

Sitemap: {site}/sitemap.xml
""".format(site=SITE_URL))

    # ---- sitemap.xml ----
    today = datetime.date.today().isoformat()
    urls = [("/", "1.0", "weekly"), ("/services/", "0.9", "monthly")]
    urls += [("/services/%s/" % s["slug"], "0.8", "monthly") for s in SERVICES]
    urls += [("/about/", "0.6", "yearly"), ("/contact/", "0.7", "monthly")]

    entries = "\n".join(
        """  <url>
    <loc>{site}{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""".format(site=SITE_URL, path=p, today=today, freq=f, pri=pri)
        for p, pri, f in urls)

    write("sitemap.xml", """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.w3.org/1999/xhtml/sitemap-placeholder">
{entries}
</urlset>
""".format(entries=entries).replace(
        "http://www.w3.org/1999/xhtml/sitemap-placeholder",
        "http://www.sitemaps.org/schemas/sitemap/0.9"))

    print("Done. %d pages." % (9,))


if __name__ == "__main__":
    main()
