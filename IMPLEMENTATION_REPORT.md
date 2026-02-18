# Hub pages icon UI – implementation report

## Scope
Icon UI patterns from TR `index.html` were applied **only** to these 6 hub pages (TR + EN), without changing any SEO/head content.

## Files changed (6)

| File | Changes |
|------|--------|
| `genel-hazirlik/index.html` | Quick access grid, H2 icons, guide card icons |
| `en/genel-hazirlik/index.html` | Same (EN labels, `/en/` links) |
| `afet-turleri/index.html` | Quick access grid, H2 “Kontrol listeleri” icon, disaster card icons |
| `en/afet-turleri/index.html` | Same (EN labels, `/en/afet-turleri/` links) |
| `acil-canta/index.html` | Quick access grid, H2 icon, info-box H4 icons |
| `en/acil-canta/index.html` | Quick access grid, H2 “Checklist” icon, H3 “Official sources” icon |

## Blocks added (by type)

### 1. Quick access section (all 6 files)
- **Location:** Below intro/progress, above the first `<hr/>`.
- **Pattern:** `<h2>` with icon + “Hızlı erişim” / “Quick access” + `<div class="grid quick-access">` with card links.
- **Content:**
  - **genel-hazirlik:** 5 cards → acil-canta, aile-plani, ev-guvenligi, toplanma-alani, sigorta.
  - **afet-turleri:** 5 cards → deprem, yangin, sel, firtina-hortum, tsunami (subpages under `/afet-turleri/` or `/en/afet-turleri/`).
  - **acil-canta:** 4 cards → deprem-cantasi-listesi, deprem-hazirlik, toplanma-alani-nasil-ogrenilir, genel-hazirlik (with `/en/` for EN).

### 2. H2 heading icons
- **genel-hazirlik (TR/EN):** Icons on “Bugün 15 dakikada” / “In 15 minutes today” and “Rehberler” / “Guides”.
- **afet-turleri (TR/EN):** Icon on “Kontrol listeleri” / “Checklists” (above search).
- **acil-canta (TR):** Icon on “Afet çantasında olması gerekenler (AFAD listesi)”.
- **acil-canta (EN):** Icon on “Checklist” H2.

### 3. Card / list icons
- **genel-hazirlik:** All 6 guide cards (Aile Planı, Acil Çanta, Ev Güvenliği, Toplanma Alanı, Sigorta, Afet Türleri) have an icon in `<h3>`.
- **afet-turleri:** All 8 disaster-type cards have an icon in the card heading.
- **acil-canta (TR):** Both info-box `<h4>`s (“Neden 72 saat?”, “Çantayı nerede tutmalı?”) have the bag/kit icon.
- **acil-canta (EN):** H3 “Official sources” has link icon.

### 4. Icon markup (unchanged pattern)
- All icons: `<span class="icon" aria-hidden="true"><svg>...</svg></span>`.
- Inline SVGs reused from TR `index.html` (clipboard, bag, book, map pin, link, phone, lightning, cloud, etc.).
- No new assets or external dependencies.

## Accessibility
- Icons use `aria-hidden="true"`.
- Card links have clear text labels (e.g. “Aç”, “Open”, card titles).

## SEO / head – confirmation
- **No changes** were made to any of the following in any of the 6 files:
  - `<title>`
  - `<meta name="description">`
  - `<link rel="canonical">`
  - `<link rel="alternate" hreflang="...">`
  - `og:*` and `twitter:*` meta tags
  - JSON-LD scripts (`BreadcrumbList`, `ItemList`, etc.)
- **No URL or internal link targets** were changed; only new blocks and icon markup were added to the body.

---

# Footer E-E-A-T links – implementation report

## Goal
Connect existing E-E-A-T pages (About, Contact, Privacy, Source policy, Editorial principles, How we are funded) across the site by adding a single footer links row on **all** HTML pages (TR + EN). No navbar changes; no head/SEO changes.

## What was added

- **Location:** Inside `<footer class="footer">`, immediately after the “Son güncelleme” / “Last updated” paragraph and before the Organization JSON-LD `<script>`.
- **TR:** One line:  
  `Kurumsal: Hakkımızda · İletişim · Gizlilik · Kaynak Politikası · Editöryal İlkeler · Nasıl finanse ediliyoruz?`  
  Links: `/hakkimizda/`, `/iletisim/`, `/gizlilik/`, `/kaynak-politikasi/`, `/editorial-ilkeler/`, `/nasil-finanse-ediliyoruz/`.
- **EN:** One line:  
  `About: About us · Contact · Privacy · Source policy · Editorial principles · How we are funded`  
  Links: `/en/hakkimizda/`, `/en/iletisim/`, `/en/gizlilik/`, `/en/kaynak-politikasi/`, `/en/editorial-ilkeler/`, `/en/nasil-finanse-ediliyoruz/`.
- **Markup:** `<p class="small footer-links">…</p>` with links separated by ` · `.

## Files changed

- **62 HTML files:** Every `index.html` in the repo (root, TR sections, `en/`, `en/afet-turleri/*`, `afet-turleri/*`, etc.) — footer block updated to include the new paragraph.
- **assets/styles.css:** Added `.footer-links { margin-top: 8px; }`.
- **sitemap.xml:** Not changed (all E-E-A-T URLs were already present).

## Verification

- `hakkimizda/index.html`: contains “Kurumsal:” and footer link list.
- `en/hakkimizda/index.html`: contains “About:” and EN footer link list.
- `deprem-hazirlik/index.html`: contains “Kurumsal:” and footer link list.

## SEO / head – confirmation

- **No changes** were made to any `<head>` content: no `<title>`, meta, canonical, hreflang, OG/Twitter, or JSON-LD in any file. Footer notice text, “Son güncelleme” / “Last updated” line, and Organization schema are unchanged.

---

# Language toggle (flag + badge) – implementation report

## Goal
Update the language toggle across Afetoncesi.com to show **flag + small TR/EN badge** (option 2). Only the toggle UI and site CSS were changed; SEO/head and URL targets were left untouched.

## What was changed

### 1. Toggle markup (header)
- **TR pages (toggle = “go to EN”):** Button content replaced with UK flag emoji (🇬🇧) + badge “EN” + screen-reader “English”. `aria-label="English"`, `class="langbtn lang-toggle"`.
- **EN pages (toggle = “go to TR”):** Button content replaced with Turkey flag emoji (🇹🇷) + badge “TR” + screen-reader “Türkçe”. `aria-label="Türkçe"`, `class="langbtn lang-toggle"`.
- Structure inside the existing `<button id="langToggle">`: `<span class="lang-flag" aria-hidden="true">…</span><span class="lang-badge" aria-hidden="true">TR|EN</span><span class="sr-only">…</span>`.

### 2. CSS (assets/styles.css)
- **.sr-only:** Visually hidden helper (position absolute, clip, overflow hidden, etc.) for screen-reader-only text.
- **.lang-toggle:** `display: inline-flex; align-items: center; gap: 8px;`
- **.lang-flag:** `font-size: 18px; line-height: 1;`
- **.lang-badge:** Small pill (font-size 12px, font-weight 700, padding 2px 6px, border-radius 999px, border and background).

## Files changed
- **62 HTML files:** Every page that contains the language toggle (root and TR section `index.html` files, all `en/**/index.html`).
- **1 CSS file:** `assets/styles.css` (sr-only, lang-toggle, lang-flag, lang-badge).

## SEO / head – confirmation
- **No head/SEO changes.** No changes were made to `<title>`, meta description, canonical, hreflang, OG/Twitter, or JSON-LD in any file. URL targets and trailing slashes were not modified.

---

# EN homepage structure alignment – implementation report

## Goal
Make `/en/index.html` use the same page structure and UI blocks as the TR homepage `/index.html`: hero, 3 CTA buttons, “Get ready — 3 steps” step-cards with icons, “Where to start?” grid, quick info box, and quick-access cards. EN text, EN links, and existing SEO/head were kept; no new CSS or dependencies.

## What was done

### Source of truth
- TR `index.html` body (hero, steps-block, grid sections, info-box, quick-access) was used as the structural template. All blocks were copied and strings translated to English.

### Blocks applied to `en/index.html`

| Block | TR (reference) | EN (implemented) |
|-------|-----------------|-------------------|
| **Hero** | `section.hero` with kicker, h1, p, 3 buttons | Same; “Disaster preparedness”, CTAs → /en/genel-hazirlik/, /en/afet-turleri/, /en/sss/ |
| **3 steps** | `section.steps-block` with `.steps-grid`, 3 `.step-card` (step-num + icon + h3 + p + btn) | Same; “Get ready — 3 steps”, step cards: Make a plan → /en/genel-hazirlik/, Prepare a kit → /en/acil-canta/, Learn more → /en/afet-turleri/ |
| **Where to start?** | H2 with clipboard icon + `.grid` of 3 cards (icon in h3, small p, “Başla”) | Same; General Preparedness, Disaster Types, Official Sources → /en/genel-hazirlik/, /en/afet-turleri/, /en/kaynaklar/ |
| **Quick info** | H2 “Kısa bilgiler” + `.info-box` (h4 + icon, 72hr kit text, link to /acil-canta/) | H2 “Quick info” + same box; link → /en/acil-canta/ |
| **Quick access** | H2 with phone icon + `.grid.quick-access` with 4 cards (112, toplanma, MeteoUyarı, AFAD) | Same; labels in EN (Assembly point, AFAD Latest Earthquakes); external URLs unchanged |

### Icon and accessibility
- All icon markup copied from TR: `<span class="icon" aria-hidden="true"><svg>…</svg></span>` (clipboard, kit, book, link, phone, map-pin, cloud, lightning). No new assets.
- Skiplink, alert banner (EN text), header/nav/footer unchanged. Buttons and links have clear labels.

### EN links (internal)
- Hero: /en/genel-hazirlik/, /en/afet-turleri/, /en/sss/
- Step cards: /en/genel-hazirlik/, /en/acil-canta/, /en/afet-turleri/
- “Where to start?” cards: /en/genel-hazirlik/, /en/afet-turleri/, /en/kaynaklar/
- Quick info: /en/acil-canta/
- Footer: existing /en/… links kept (hakkimizda, iletisim, gizlilik, kaynak-politikasi, editorial-ilkeler, nasil-finanse-ediliyoruz, kaynaklar).

### Files changed
- **en/index.html** only. Body content from `<main id="icerik">` through `</main>` replaced to match TR layout; head, header, footer left intact. Footer “Last updated” margin set to 12px to match TR.

## Checks
- EN homepage now has the same sections and spacing as TR: hero, steps grid, “Where to start?” grid, quick info box, quick-access grid.
- All internal links use /en/…; nav and language toggle unchanged; no new CSS files or dependencies.
- **No head/SEO changes** except keeping existing EN title, description, canonical, hreflang, OG/Twitter, JSON-LD.

---

*Report generated after adding footer E-E-A-T links site-wide.*
