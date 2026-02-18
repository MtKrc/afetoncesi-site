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

*Report generated after adding footer E-E-A-T links site-wide.*
