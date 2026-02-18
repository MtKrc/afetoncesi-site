# SEO Implementation Summary (afetoncesi.com)

**See also:** [MASTER_PRD.md](./MASTER_PRD.md) — North Star PRD and Phase 1 technical SEO scope.

---

This document summarizes the SEO fixes applied and provides templates/examples for reference.

---

## 1. URL standard (trailing slash)

- **Internal links:** All internal links use trailing slash (e.g. `/genel-hazirlik/`, `/acil-canta/`).
- **Canonical:** Every page uses **absolute** canonical: `https://afetoncesi.com/.../` (trailing slash).
- **Sitemap:** `sitemap.xml` lists all URLs with trailing slash and absolute `https://afetoncesi.com/...` format.
- **Redirects:**
  - **Apache:** `.htaccess` redirects `/*/index.html` → `/*/` and `/index.html` → `/` (301).
  - **Netlify:** `netlify.toml` defines the same redirects.

**Note:** Ensure the server serves `/path/` as `/path/index.html` (default on most hosts). Add `og-image.jpg` (1200×630 px) at site root for social previews.

---

## 2. Head template (per page)

Each page uses the following pattern. Replace `TITLE`, `DESCRIPTION`, `CANONICAL_PATH`, `OG_TITLE`, `TWITTER_TITLE` and locale as needed.

```html
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="description" content="DESCRIPTION"/>
<title>TITLE | afetoncesi.com</title>
<link rel="canonical" href="https://afetoncesi.com/CANONICAL_PATH"/>
<link rel="alternate" hreflang="x-default" href="https://afetoncesi.com/TR_VERSION_PATH"/>
<link rel="alternate" hreflang="tr" href="https://afetoncesi.com/TR_PATH"/>
<link rel="alternate" hreflang="en" href="https://afetoncesi.com/en/EN_PATH"/>
<meta property="og:type" content="website|article"/>
<meta property="og:url" content="https://afetoncesi.com/CANONICAL_PATH"/>
<meta property="og:title" content="OG_TITLE"/>
<meta property="og:description" content="DESCRIPTION"/>
<meta property="og:image" content="https://afetoncesi.com/og-image.jpg"/>
<meta property="og:locale" content="tr_TR|en_US"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="TWITTER_TITLE"/>
<meta name="twitter:description" content="DESCRIPTION"/>
<meta name="twitter:image" content="https://afetoncesi.com/og-image.jpg"/>
```

- **x-default:** Points to the Turkish version (default language).
- **TR pages:** `og:locale` = `tr_TR`. **EN pages:** `og:locale` = `en_US`.

---

## 3. Structured data examples

### Organization (footer, all pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "afetoncesi.com",
  "url": "https://afetoncesi.com/",
  "description": "Afet öncesi hazırlık rehberi. Resmi kaynaklı kontrol listeleri."
}
```

### FAQPage (SSS / FAQ only)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Bu site resmi mi?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hayır. Bu site, resmi kurumların yayımladığı rehber ve duyuruları sadeleştirerek bir araya getirir. Her sayfanın altında resmi kaynak linkleri vardır."
      }
    },
    {
      "@type": "Question",
      "name": "Acil durumda ne yapmalıyım?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "112'yi arayın ve AFAD, yerel yönetim, meteoroloji gibi resmi kanalları takip edin."
      }
    }
  ]
}
```

---

## 4. Sitemap (excerpt)

`sitemap.xml` uses only absolute URLs with trailing slash. New pages (e.g. deprem-aninda-ne-yapmali) are included:

```xml
<url>
  <loc>https://afetoncesi.com/</loc>
  <lastmod>2026-02-14</lastmod>
</url>
<url>
  <loc>https://afetoncesi.com/deprem-aninda-ne-yapmali/</loc>
  <lastmod>2026-02-14</lastmod>
</url>
<url>
  <loc>https://afetoncesi.com/en/deprem-aninda-ne-yapmali/</loc>
  <lastmod>2026-02-14</lastmod>
</url>
```

---

## 5. Modified HTML examples (summary)

- **index.html (TR):** Full head with OG, Twitter, x-default, absolute canonical; nav/links with trailing slash; Organization schema in footer.
- **acil-canta (TR):** New title “Deprem Çantası Listesi – Afet Çantası Nasıl Hazırlanır?”, longer meta description, same head/footer pattern.
- **deprem-hazirlik (TR):** New title “Deprem Öncesi Hazırlık Rehberi”, new meta, H2 “Deprem öncesi hazırlık rehberi”, link to “Deprem anında ne yapmalı?”.
- **sss (TR):** FAQ schema in head, H2 “Afet öncesi hazırlık hakkında”, Organization in footer.
- **afet-turleri/deprem (TR):** H2 “Deprem öncesi, sırasında ve sonrasında yapılacaklar”, two short intro paragraphs, H2 “Kontrol listesi” and “Resmi kaynaklar”, link to deprem-aninda-ne-yapmali.
- **deprem-aninda-ne-yapmali (TR + EN):** New page with 5-step list, “Çök–Kapan–Tutun” section, “Yapılmaması gerekenler”, official sources; minimal layout, mobile-first.

All other TR and EN pages received absolute canonical, x-default, OG, Twitter, and Organization schema in footer.

---

## 6. Design constraints (kept)

- No animation.
- No heavy JS (only existing menu toggle, print, lang switch, tabs, checklist persistence).
- Mobile-first (existing breakpoints and hamburger menu).
- High-trust tone (disclaimer, official sources, 112).
