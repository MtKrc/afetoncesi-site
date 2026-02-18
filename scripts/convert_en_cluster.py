#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert TR deprem cluster pages to EN: head, nav, footer, card content."""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..")

# Common replacements for all 4 pages
COMMON = [
    ('<html lang="tr">', '<html lang="en">'),
    ('<a class="skiplink" href="#icerik">İçeriğe atla</a>', '<a class="skiplink" href="#icerik">Skip to content</a>'),
    ('<span>Afet öncesi hazırlık rehberi</span>', '<span>Preparedness guide (Türkiye)</span>'),
    ('aria-label="Menüyü aç/kapat"', 'aria-label="Open/close menu"'),
    ('<nav aria-label="Ana menü">', '<nav aria-label="Main menu">'),
    ('<a href="/" class="">Anasayfa</a>\n<a href="/genel-hazirlik/" class="active">Genel Hazırlık</a>\n<a href="/afet-turleri/" class="">Afet Türleri</a>\n<a href="/kaynaklar/" class="">Kaynaklar</a>\n<a href="/sss/" class="">SSS</a>',
     '<a href="/en/" class="">Home</a>\n<a href="/en/genel-hazirlik/" class="active">General Preparedness</a>\n<a href="/en/afet-turleri/" class="">Disaster Types</a>\n<a href="/en/kaynaklar/" class="">Sources</a>\n<a href="/en/sss/" class="">FAQ</a>'),
    ('aria-label="Dili değiştir">EN</button>', 'aria-label="Change language">TR</button>'),
    ('<strong>Not:</strong> Bu sitedeki içerik, resmi kaynaklara dayanır. Acil durumda <strong>112</strong>\'yi arayın ve resmi duyuruları takip edin.',
     '<strong>Note:</strong> Content on this site is based on official sources. In an emergency, call <strong>112</strong> and follow official announcements.'),
    ('Son güncelleme: 2026-02-14 · <a href="/kaynaklar/">Resmi kaynaklar</a>',
     'Last updated: 2026-02-14 · <a href="/en/kaynaklar/">Official sources</a>'),
    ('"name":"Anasayfa","item":"https://afetoncesi.com/"},{"@type":"ListItem","position":2,"name":"Genel Hazırlık","item":"https://afetoncesi.com/genel-hazirlik/"},{"@type":"ListItem","position":3,"name":"Deprem Hazırlığı","item":"https://afetoncesi.com/deprem-hazirlik/"},{"@type":"ListItem","position":4,"name":',
     '"name":"Home","item":"https://afetoncesi.com/en/"},{"@type":"ListItem","position":2,"name":"General Preparedness","item":"https://afetoncesi.com/en/genel-hazirlik/"},{"@type":"ListItem","position":3,"name":"Earthquake Preparedness","item":"https://afetoncesi.com/en/deprem-hazirlik/"},{"@type":"ListItem","position":4,"name":'),
    ('<meta property="og:locale" content="tr_TR"/>', '<meta property="og:locale" content="en_US"/>'),
]

# Per-page: (path, list of (old, new) for title/description/og/breadcrumb name, then card content (start marker, end marker, new card inner HTML)
PAGES = {
    "en/toplanma-alani-nasil-ogrenilir/index.html": {
        "url_slug": "toplanma-alani-nasil-ogrenilir",
        "title": "How to Find Your Assembly Point? – Query Guide | afetoncesi.com",
        "description": "How to find your assembly point? e-Devlet and AFAD assembly point query. Step-by-step guide and official links.",
        "og_title": "How to Find Your Assembly Point? | afetoncesi.com",
        "og_desc": "Assembly point query via e-Devlet and AFAD. Step-by-step guide.",
        "breadcrumb_name": "How to find your assembly point",
        "card": """  <h1>How to find your assembly point</h1>
  <p>Knowing in advance where you will meet your family after an earthquake or other disaster is important. You can find assembly point information via e-Devlet and AFAD.</p>
  <p><strong>How to find your assembly point? Short steps:</strong></p>
  <ul>
    <li>Log in to the e-Devlet portal (turkiye.gov.tr).</li>
    <li>Search for the "Disaster and emergency management assembly point query" service or go to the relevant page.</li>
    <li>Your nearest assembly points are listed according to your address.</li>
    <li>AFAD disaster maps and local municipalities can also provide assembly point information.</li>
  </ul>
  <h2>Query via e-Devlet</h2>
  <p>After logging in with your ID, select the "Disaster and Emergency Management Authority – Assembly Point Query" service. You can see the nearest assembly points by province, district and neighbourhood/address. Write the address in your family plan and, if possible, visit the area together in advance.</p>
  <h2>Assembly point in the family plan</h2>
  <p>Once you have identified your assembly point, add it to your family communication plan. Explain it to children and elderly family members. See our <a href="/en/aile-plani/">Family plan</a> and <a href="/en/toplanma-alani/">Assembly point</a> pages for more.</p>
  <div class="actions">
    <a class="btn primary" href="/en/deprem-hazirlik/">Earthquake preparedness</a>
    <a class="btn" href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a>
    <a class="btn" href="/en/toplanma-alani/">Assembly point guide</a>
  </div>
  <hr/>
  <h3>Official sources</h3>
  <ul class="small">
    <li><a href="https://www.turkiye.gov.tr/afet-ve-acil-durum-yonetimi-toplanma-alani-sorgulama" target="_blank" rel="noopener">e-Devlet – Assembly point query</a></li>
    <li><a href="https://www.afad.gov.tr/afet-haritalari" target="_blank" rel="noopener">AFAD – Disaster maps</a></li>
    <li><a href="https://www.112.gov.tr/" target="_blank" rel="noopener">112 Emergency</a></li>
  </ul>
  <p class="small">Last updated: 2026-02-14</p>""",
    },
    "en/deprem-sigortasi-dask/index.html": {
        "url_slug": "deprem-sigortasi-dask",
        "title": "Earthquake Insurance DASK – Compulsory Earthquake Insurance Guide | afetoncesi.com",
        "description": "Earthquake insurance DASK: what is compulsory earthquake insurance, how to get it? DASK policy and official sources.",
        "og_title": "Earthquake Insurance DASK | afetoncesi.com",
        "og_desc": "Compulsory earthquake insurance DASK: what it is, how to get it. Official guide.",
        "breadcrumb_name": "Earthquake insurance DASK",
        "card": """  <h1>Earthquake insurance DASK</h1>
  <p>In Türkiye, compulsory earthquake insurance for homes (DASK) is regulated by law. This insurance covers part of the material damage caused by earthquakes; it is a legal requirement.</p>
  <p><strong>What is DASK earthquake insurance? Short facts:</strong></p>
  <ul>
    <li>DASK (Natural Disaster Insurance Institution) provides compulsory earthquake insurance.</li>
    <li>DASK policy may be required for title deeds and electricity–water subscriptions.</li>
    <li>The policy covers damage to the building from an earthquake; separate policy may be needed for contents.</li>
    <li>You can get the policy through insurance companies and agents; it must be renewed when it expires.</li>
  </ul>
  <h2>How to get it</h2>
  <p>DASK policies are obtained through participating insurance companies and agents. Premiums are calculated using information such as province/district, year of construction and building type. The policy is usually valid for one year; remember to renew. See the official <a href="https://www.dask.gov.tr/" target="_blank" rel="noopener">DASK</a> site for conditions and the current list.</p>
  <h2>Policy in your emergency kit</h2>
  <p>Put a copy of the policy or a summary in your emergency kit; it may be needed when claiming after damage. See our <a href="/en/deprem-cantasi-listesi/">Earthquake kit list</a> and <a href="/en/sigorta/">Insurance</a> pages.</p>
  <div class="actions">
    <a class="btn primary" href="/en/deprem-hazirlik/">Earthquake preparedness</a>
    <a class="btn" href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a>
    <a class="btn" href="/en/sigorta/">Insurance guide</a>
  </div>
  <hr/>
  <h3>Official sources</h3>
  <ul class="small">
    <li><a href="https://www.dask.gov.tr/" target="_blank" rel="noopener">DASK – Natural Disaster Insurance Institution</a></li>
    <li><a href="https://www.afad.gov.tr/" target="_blank" rel="noopener">AFAD</a></li>
    <li><a href="https://www.112.gov.tr/" target="_blank" rel="noopener">112 Emergency</a></li>
  </ul>
  <p class="small">Last updated: 2026-02-14</p>""",
    },
    "en/cocuklarla-deprem/index.html": {
        "url_slug": "cocuklarla-deprem",
        "title": "Earthquake with Children – Talking to Kids About Earthquakes and Preparedness | afetoncesi.com",
        "description": "Earthquake with children: how to talk to kids about earthquakes, what to do at home? Calm language and simple steps. AFAD-based.",
        "og_title": "Earthquake with Children | afetoncesi.com",
        "og_desc": "Talking to kids about earthquakes and preparedness. Calm language, simple steps. Official guide.",
        "breadcrumb_name": "Earthquake with children",
        "card": """  <h1>Earthquake with children</h1>
  <p>Explaining earthquakes to children in a calm, age-appropriate way and including them in simple preparedness steps at home builds confidence and reduces fear. The suggestions below are based on AFAD and child-focused official sources.</p>
  <p><strong>Short tips on earthquake with children:</strong></p>
  <ul>
    <li>Avoid fear-based language; describe earthquakes as a natural event and focus on what to do.</li>
    <li>Practise steps like drop–cover–hold together; do a short drill at home.</li>
    <li>Explain the assembly point and communication plan to children; teach emergency contact numbers.</li>
    <li>Prepare the emergency kit together; a small toy or blanket for the child can go in the kit.</li>
  </ul>
  <h2>What to do at home</h2>
  <p>Identify safe spots (under a table, by an inner wall) with your child. Practise drop–cover–hold during a shake like a game. Teach 112 and family contact numbers for emergencies. Our <a href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a> page summarises steps for adults.</p>
  <h2>School and nursery</h2>
  <p>Ask about the disaster plan and assembly arrangement at school and nursery. Tell your child that similar rules apply at school.</p>
  <div class="actions">
    <a class="btn primary" href="/en/deprem-hazirlik/">Earthquake preparedness</a>
    <a class="btn" href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a>
    <a class="btn" href="/en/aile-plani/">Family plan</a>
  </div>
  <hr/>
  <h3>Official sources</h3>
  <ul class="small">
    <li><a href="https://www.afad.gov.tr/afadem" target="_blank" rel="noopener">AFAD AFADEM</a></li>
    <li><a href="https://www.afad.gov.tr/deprem-oncesi-ani-ve-sonrasi-alinacak-onlemler" target="_blank" rel="noopener">AFAD – Before/during/after earthquake</a></li>
    <li><a href="https://www.112.gov.tr/" target="_blank" rel="noopener">112 Emergency</a></li>
  </ul>
  <p class="small">Last updated: 2026-02-14</p>""",
    },
    "en/deprem-sonrasi-ilk-10-dakika/index.html": {
        "url_slug": "deprem-sonrasi-ilk-10-dakika",
        "title": "First 10 Minutes After an Earthquake – What to Do? | afetoncesi.com",
        "description": "First 10 minutes after an earthquake: what to do when the shaking stops? Safety, family, gas and electricity. Short AFAD-based guide.",
        "og_title": "First 10 Minutes After an Earthquake | afetoncesi.com",
        "og_desc": "What to do in the first minutes after an earthquake? Safety, family, gas and electricity. Official guide.",
        "breadcrumb_name": "First 10 minutes after an earthquake",
        "card": """  <h1>First 10 minutes after an earthquake</h1>
  <p>The minutes immediately after the shaking stops can be life-saving. Your own safety first, then family contact and gas–electricity–water safety matter. The steps below are based on AFAD guidance.</p>
  <p><strong>What to do in the first 10 minutes after an earthquake? Short list:</strong></p>
  <ul>
    <li>Stay in drop–cover–hold until the shaking stops; then check around you and put on shoes.</li>
    <li>If you smell gas, turn off the valve, do not use matches or lighters, open windows and leave, and call 112 or the gas company.</li>
    <li>Turn off the mains at the electrical panel; turn off the water valve if you suspect damage.</li>
    <li>Check on those around you; if anyone is injured call 112 and apply first aid if needed.</li>
    <li>If the building is unsafe, go to the assembly point; use stairs, do not use the lift.</li>
  </ul>
  <h2>Gas and electricity</h2>
  <p>If you suspect a gas leak, turn off the valve, ventilate the area and call 112 or the gas company. Turning off the electricity reduces fire risk. If you suspect pipe damage, turn off the main water valve.</p>
  <h2>Moving to the assembly point</h2>
  <p>If the building is damaged or at risk, go to your pre-arranged assembly point. Follow your family communication plan. See our <a href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a> and <a href="/en/toplanma-alani-nasil-ogrenilir/">How to find your assembly point</a> pages for details.</p>
  <div class="actions">
    <a class="btn primary" href="/en/deprem-hazirlik/">Earthquake preparedness</a>
    <a class="btn" href="/en/deprem-aninda-ne-yapmali/">What to do during an earthquake</a>
    <a class="btn" href="/en/toplanma-alani-nasil-ogrenilir/">Assembly point query</a>
  </div>
  <hr/>
  <h3>Official sources</h3>
  <ul class="small">
    <li><a href="https://www.afad.gov.tr/deprem-oncesi-ani-ve-sonrasi-alinacak-onlemler" target="_blank" rel="noopener">AFAD – Before/during/after earthquake</a></li>
    <li><a href="https://www.afad.gov.tr/afadem" target="_blank" rel="noopener">AFAD AFADEM</a></li>
    <li><a href="https://www.112.gov.tr/" target="_blank" rel="noopener">112 Emergency</a></li>
  </ul>
  <p class="small">Last updated: 2026-02-14</p>""",
    },
}

def main():
    for path, data in PAGES.items():
        full = os.path.join(BASE, path)
        with open(full, "r", encoding="utf-8") as f:
            s = f.read()
        slug = data["url_slug"]
        base_url = "https://afetoncesi.com"
        en_url = f"{base_url}/en/{slug}/"
        tr_url = f"{base_url}/{slug}/"

        for old, new in COMMON:
            s = s.replace(old, new)

        # Canonical and hreflang and og:url
        s = s.replace(f'href="{tr_url}"', f'href="{en_url}"')
        s = s.replace(f'content="{tr_url}"', f'content="{en_url}"')
        s = s.replace(f'"item":"{tr_url}"', f'"item":"{en_url}"')

        # Title and descriptions
        s = re.sub(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{data["description"]}"/>', s, count=1)
        s = re.sub(r'<title>[^<]*</title>', f'<title>{data["title"]}</title>', s, count=1)
        s = re.sub(r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{data["og_title"]}"/>', s, count=1)
        s = re.sub(r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{data["og_desc"]}"/>', s, count=1)
        s = re.sub(r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{data["og_title"]}"/>', s, count=1)
        s = re.sub(r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{data["og_desc"]}"/>', s, count=1)

        # Breadcrumb last item name (after position 4)
        s = re.sub(r'"position":4,"name":"[^"]*","item":"https://afetoncesi\.com/en/' + re.escape(slug) + r'/"',
                   f'"position":4,"name":"{data["breadcrumb_name"]}","item":"{en_url}"', s, count=1)

        # Card content: replace content between <div class="card"> and </div> (first matching close)
        start = s.find("<div class=\"card\">")
        if start == -1:
            print("Card not found in", path)
            continue
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
        s = s[:start] + "<div class=\"card\">\n" + data["card"] + "\n</div>" + s[end:]

        with open(full, "w", encoding="utf-8") as f:
            f.write(s)
        print("Updated", path)

if __name__ == "__main__":
    main()
