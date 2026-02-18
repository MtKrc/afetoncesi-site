#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert TR card content to EN and fix internal links to /en/ for EN E-E-A-T pages."""

import os

BASE = os.path.join(os.path.dirname(__file__), "..")

PAGES = {
    "en/kaynak-politikasi/index.html": {
        "card": """<div class="card">
  <h1>Source policy</h1>
  <div class="info-box" role="note">
    <p><strong>Important:</strong> afetoncesi.com is not an official body. In an emergency, call <strong>112</strong>. Information on this site is based on official sources; verify the source for critical decisions.</p>
  </div>
  <h2>Which sources do we use?</h2>
  <p>Preparedness claims (what to do, what to avoid, what to have) are based on official or widely recognised institutions. Preferred sources include AFAD, MGM, Kızılay, e-Devlet, 112, DASK and similar public bodies. All official links are listed on the <a href="/en/kaynaklar/">Sources</a> page; each page has a relevant "Official sources" block.</p>
  <h2>Attribution</h2>
  <p>We do not present content summarised or adapted from an official source as our own. We use phrases like "According to AFAD…", "As stated on e-Devlet…" and link to the source.</p>
  <h2>Update policy</h2>
  <ul>
    <li><strong>Trigger-based updates:</strong> We update content when official guidance changes, when an error is reported, or during a planned review.</li>
    <li><strong>Annual review:</strong> High-impact pages (e.g. earthquake, emergency kit, assembly point) are reviewed at least yearly or after a major disaster or policy change; links and text are kept in line with official guidance.</li>
    <li><strong>Last updated date:</strong> Pages may show a "Last updated" date for trust; this is updated when content or sources change.</li>
  </ul>
  <h2>Corrections</h2>
  <p>Errors reported by users or partners are corrected by priority. Obvious errors (wrong number, broken link, wrong agency name) are updated as soon as possible. Use the <a href="/en/iletisim/">Contact</a> page to report corrections.</p>
  <h2>Related pages</h2>
  <p><a href="/en/hakkimizda/">About us</a> · <a href="/en/editorial-ilkeler/">Editorial principles</a> · <a href="/en/kaynaklar/">Official sources</a> · <a href="/en/sss/">FAQ</a> · <a href="/en/iletisim/">Contact</a></p>
</div>""",
    },
    "en/iletisim/index.html": {
        "card": """<div class="card">
  <h1>Contact</h1>
  <div class="info-box" role="alert">
    <p><strong>In an emergency:</strong> This site does not provide emergency services. For life-threatening or emergency help, call <strong>112</strong> and follow official instructions.</p>
  </div>
  <p>You can contact afetoncesi.com about:</p>
  <ul>
    <li><strong>Error or currency report:</strong> Tell us about wrong information, broken links or outdated content on the site. We will review and update as soon as possible. The process is summarised on our <a href="/en/kaynak-politikasi/">Source policy</a> page.</li>
    <li><strong>Suggestion or partnership:</strong> Content ideas, institution/school/NGO partnerships or technical matters.</li>
  </ul>
  <p>We currently use email for contact. The address is set by site management; the current address will be shared on this page or the <a href="/en/hakkimizda/">About us</a> page in due course.</p>
  <p class="small">For general questions see <a href="/en/sss/">FAQ</a>; for the official source list see <a href="/en/kaynaklar/">Sources</a>.</p>
  <h2>Related pages</h2>
  <p><a href="/en/hakkimizda/">About us</a> · <a href="/en/editorial-ilkeler/">Editorial principles</a> · <a href="/en/kaynak-politikasi/">Source policy</a> · <a href="/en/kaynaklar/">Official sources</a> · <a href="/en/sss/">FAQ</a> · <a href="/en/gizlilik/">Privacy</a></p>
</div>""",
    },
    "en/gizlilik/index.html": {
        "card": """<div class="card">
  <h1>Privacy</h1>
  <div class="info-box" role="note">
    <p><strong>Important:</strong> afetoncesi.com is not an official body. This page summarises the site's data practices. In an emergency, call <strong>112</strong>.</p>
  </div>
  <p>afetoncesi.com respects user privacy and aims to collect only the minimum data needed to run or improve the site.</p>
  <h2>Data we collect</h2>
  <ul>
    <li><strong>Visit data:</strong> Server logs (IP, date/time, page URL, browser info) may be generated. These may be kept for a limited time for security and technical analysis; they are not used for advertising or targeting on sensitive topics such as disaster or health.</li>
    <li><strong>Form or contact:</strong> Information you send via a contact form or email is used only to respond to your request and, if needed, to correct content; we do not use it for marketing or share it with third parties.</li>
    <li><strong>Cookies:</strong> The site may use minimal functional cookies (e.g. language preference). We do not use third-party advertising or tracking cookies. If we add advertising, the policy will be updated and noted on the <a href="/en/nasil-finanse-ediliyoruz/">How we are funded</a> page.</li>
  </ul>
  <h2>Data sharing</h2>
  <p>We do not share your personal data with ad networks or data brokers. It is not sold or transferred to third parties except where required by law.</p>
  <h2>Your rights</h2>
  <p>You can contact us via the <a href="/en/iletisim/">Contact</a> page to request access, correction or deletion of your data. Requests are answered within a reasonable time.</p>
  <h2>Policy updates</h2>
  <p>When this page is updated, the Last updated date is changed. Significant changes are noted briefly on the page.</p>
  <h2>Related pages</h2>
  <p><a href="/en/hakkimizda/">About us</a> · <a href="/en/nasil-finanse-ediliyoruz/">How we are funded</a> · <a href="/en/iletisim/">Contact</a> · <a href="/en/kaynaklar/">Official sources</a> · <a href="/en/sss/">FAQ</a></p>
</div>""",
    },
    "en/nasil-finanse-ediliyoruz/index.html": {
        "card": """<div class="card">
  <h1>How we are funded</h1>
  <div class="info-box" role="note">
    <p><strong>Important:</strong> afetoncesi.com is not an official body. In an emergency, call <strong>112</strong>. This page explains the site's funding and commercial content policy.</p>
  </div>
  <p>afetoncesi.com is an independent, public-benefit information platform. Core preparedness information will always remain free and accessible.</p>
  <h2>Current situation</h2>
  <p><strong>There are currently no ads, affiliate links or product sales on the site.</strong> There is no revenue; the project is sustained by volunteer/personal resources. Information pages contain no commercial elements.</p>
  <h2>Separation of information and commerce</h2>
  <p>In future, we may consider ethical advertising, affiliate or donation models for sustainability. If we do:</p>
  <ul>
    <li>Information pages (what to do, lists, official sources) will remain separate from commercial messaging; ads will not be mixed with content.</li>
    <li>Areas such as "Shop" or "Product suggestions" will have separate URLs and information architecture; "how to choose" guides will remain product-agnostic.</li>
    <li>Sensitive data (disaster, health) will not be used for ad targeting.</li>
    <li>This page and <a href="/en/editorial-ilkeler/">Editorial principles</a> will be updated so users can see clearly how we are funded.</li>
  </ul>
  <h2>Transparency</h2>
  <p>Any change to the funding model will be announced on this page. Use the <a href="/en/iletisim/">Contact</a> page for questions.</p>
  <h2>Related pages</h2>
  <p><a href="/en/hakkimizda/">About us</a> · <a href="/en/editorial-ilkeler/">Editorial principles</a> · <a href="/en/kaynaklar/">Official sources</a> · <a href="/en/sss/">FAQ</a> · <a href="/en/gizlilik/">Privacy</a> · <a href="/en/iletisim/">Contact</a></p>
</div>""",
    },
}

def main():
    for path, data in PAGES.items():
        full = os.path.join(BASE, path)
        with open(full, "r", encoding="utf-8") as f:
            s = f.read()
        start = s.find("<div class=\"card\">")
        if start == -1:
            print("Card not found in", path)
            continue
        # Find matching </div> (count nested divs)
        depth = 1
        i = start + len("<div class=\"card\">")
        end = -1
        while i < len(s) - 6:
            if s[i:i+5] == "<div " or s[i:i+4] == "<div>":
                depth += 1
            elif s[i:i+6] == "</div>":
                depth -= 1
                if depth == 0:
                    end = i + 6
                    break
            i += 1
        if end == -1:
            print("Card end not found in", path)
            continue
        new_s = s[:start] + data["card"] + s[end:]
        with open(full, "w", encoding="utf-8") as f:
            f.write(new_s)
        print("Updated", path)

if __name__ == "__main__":
    main()
