# 72 Saat Hazırlık Planı – Implementation Report

## Goal
Build a high-trust “72 Saat Hazırlık Planı” / “72-Hour Preparedness Plan” wizard at `/72-saat/` (TR) and `/en/72-saat/` (EN) that generates a personalized checklist and can be printed as a one-page plan.

## Files Changed / Added

| File | Change |
|------|--------|
| **72-saat/index.html** | **New.** TR wizard page: 8-step form, progress indicator, plan output with Top 10 + 7 sections, Save/Reset/Print, official sources, JSON-LD HowTo + BreadcrumbList, full SEO head. |
| **en/72-saat/index.html** | **New.** EN wizard page: same structure, English copy, `/en/` links. |
| **assets/styles.css** | Added `.wizard-progress`, `.wizard-step`, `.plan-output` styles for wizard and plan layout. |
| **assets/print.css** | Hide `.no-print`, `.wizard-form`, `.wizard-actions` when printing; `.plan-print-area .plan-actions` hidden; list styling for plan checklist in print. |
| **sitemap.xml** | Added `<url>` for `https://afetoncesi.com/72-saat/` and `https://afetoncesi.com/en/72-saat/` with `<lastmod>2026-02-17</lastmod>`. |
| **genel-hazirlik/index.html** | Added “72 Saat Planı” quick-access card (clock icon) linking to `/72-saat/`. |
| **en/genel-hazirlik/index.html** | Added “72-Hour Plan” quick-access card linking to `/en/72-saat/`. |

## What Was Added

### Wizard (client-side only)
- **Inputs (8 steps):** Household size (1–5+), children (yes/no), elderly or special needs (yes/no), pets (yes/no), home type (apartment/house/dorm/other), car available (yes/no), region optional dropdown (Marmara, Ege, İç Anadolu, Akdeniz, Karadeniz, Doğu, Güneydoğu), existing kit level (none/basic/partial/ready).
- **Output:** “Top 10 actions today” list + 7 checklist sections: (1) Water & food, (2) First aid & hygiene, (3) Light/power/communication, (4) Documents & money, (5) Clothing & shelter, (6) Family plan & meeting point, (7) Special needs (if children/elderly/pets). Internal links to acil-canta, deprem-hazirlik, toplanma-alani-nasil-ogrenilir, aile-plani (TR) or EN equivalents.
- **Save/Load:** localStorage key `afeto_72h_v1`. Buttons: “Planı Kaydet” / “Save plan”, “Sıfırla” / “Reset”, “PDF olarak yazdır” / “Print to PDF” (window.print). Note: “Veriler yalnızca cihazınızda saklanır.” / “Data is stored only on your device.”
- **Accessibility:** Labels/legends on inputs, `aria-live="polite"` on progress and plan output, keyboard-navigable form, no PII or precise address collection.

### SEO & structured data
- **Canonical / hreflang:** TR page canonical `https://afetoncesi.com/72-saat/`, x-default and tr same, en alternate `https://afetoncesi.com/en/72-saat/`. EN page canonical `https://afetoncesi.com/en/72-saat/`, x-default `https://afetoncesi.com/72-saat/`, hreflang tr/en. No other head/SEO tags changed on existing pages.
- **JSON-LD:** BreadcrumbList (Home → 72 Saat) and HowTo schema describing wizard steps on both TR and EN. Organization in footer left as-is.

### Navigation
- **72-saat and en/72-saat:** Nav includes “72 Saat” / “72 Hours” as active item.
- **Discovery:** “72 Saat Planı” / “72-Hour Plan” card added to Genel Hazırlık / General Preparedness quick-access grid only (no site-wide nav change).

### Print
- Wizard form and action buttons hidden when printing. Plan output (title, date, household summary, Top 10, sections, related guides, official sources) prints; official sources block (AFAD, Kızılay, 112, MGM) included in print.

## Rules Compliance
- No ads, affiliate links, or commerce CTAs.
- No precise address or PII collection.
- Calm, action-oriented tone.
- Existing SEO head pattern preserved; canonical and hreflang correct for TR/EN and x-default (TR).
- Design uses existing styles.css and app.js; no new external dependencies.

## Summary
- **New pages:** 2 (72-saat/index.html, en/72-saat/index.html).
- **Modified:** styles.css, print.css, sitemap.xml, genel-hazirlik/index.html, en/genel-hazirlik/index.html.
- **Head/SEO:** No changes on existing pages; new pages follow site pattern with HowTo and BreadcrumbList.
