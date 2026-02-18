# 72-hour wizard – personalization and UX update (implementation report)

## Scope
Changes apply only to **/72-saat/** (TR) and **/en/72-saat/** (EN). No head/SEO changes; no new dependencies; localStorage behavior unchanged.

---

## A) UX fixes

### 1) Radio options as full-row clickable labels
- **Before:** Radio + text inside `<label>`, but layout used `.kit` (flex) and options could feel disconnected.
- **After:** Each option is `<label class="wizard-option">` containing `<input type="radio">` and `<span class="wizard-option-text">text</span>`. The entire row is clickable.

### 2) Text next to radio
- Option text is immediately next to the radio circle (no separate numbers or detached labels). Achieved by flex layout inside `.wizard-option` with `gap: 12px`.

### 3) Responsive grid
- **Mobile (default):** 1 column.
- **Tablet (min-width: 640px):** 2 columns.
- **Desktop (min-width: 1024px):** 3 columns.
- Class: `.wizard-options-grid` with `display: grid` and `grid-template-columns` set per breakpoint.

### 4) Selected state
- `.wizard-option:has(input:checked)` gets `border-color: var(--primary)` and `background: var(--primary-lighter)` so the chosen option is clearly highlighted.

**Files:** `72-saat/index.html`, `en/72-saat/index.html` (form markup), `assets/styles.css` (wizard-options-grid, wizard-option, selected state).

---

## B) Personalization (plan generator, not generic checklist)

### 1) “Your inputs” summary at top of plan
- After “Planı oluştur” / “Generate plan”, the plan output now starts with:
  - **TR:** “Sizin cevaplarınız” — Hane, Çocuk, 65+ / özel ihtiyaç, Evcil hayvan, Konut, Araç, Çanta durumu (human-readable labels).
  - **EN:** “Your inputs” — Household, Children, 65+ / special needs, Pets, Home type, Car, Kit status.
- Rendered in a `.plan-summary-box` (definition list) for quick scanning.

### 2) Computed quantities (water and meals)
- **Water target (L):** `householdSize × 9` (3 L/person/day × 3 days). Shown in a prominent card: e.g. “27 L — Su hedefi (72 saat)”.
- **Meals target:** `householdSize × 9` (3 meals/person/day × 3 days). Shown as e.g. “27 öğün — Gıda hedefi”.
- Both values are also used in the Top 10 and in the “Su ve gıda” / “Water & food” section text.

### 3) Sections tagged by answers
- **Children = Yes:** Section “Çocuk” / “Children” with badge “Eklenme nedeni: çocuk” / “Added because: children” and short line “Bu bölüm cevaplarınıza göre eklendi.”
- **Elderly/special needs = Yes:** Section “Tıbbi / özel ihtiyaçlar” / “Medical / special needs” with “Eklenme nedeni: 65+ veya özel ihtiyaç” / “Added because: 65+ or special needs”.
- **Pets = Yes:** Section “Evcil hayvan” / “Pets” with “Eklenme nedeni: evcil hayvan” / “Added because: pets”.
- Core sections (water/food, first aid, light/power, documents, clothing, family plan) are always present; optional sections only when the corresponding answer is “yes”.

### 4) Explanation line
- At the very top of the plan output:
  - **TR:** “Bu plan cevaplarınıza göre hesaplanır; kişisel veriler sunucuya gönderilmez.”
  - **EN:** “This plan is computed from your answers; no personal data is sent to any server.”

**Files:** `72-saat/index.html`, `en/72-saat/index.html` (script: `buildChecklist`, `renderPlan`, `answerLabels`, summary/targets/explanation HTML).

---

## C) Constraints respected

- No backend; no new external dependencies.
- Existing `<head>`, canonical, hreflang, OG/Twitter, JSON-LD unchanged.
- localStorage key `afeto_72h_v1` and Save/Reset/Print behavior unchanged. Saved payload now includes `answerLabels`, `waterL`, `meals` so restored plans render the summary and targets correctly.

---

## D) Deliverables

| Deliverable | Status |
|-------------|--------|
| UX: full-row label, text next to radio, responsive grid, selected state | Done (TR + EN) |
| Plan: “Your inputs” summary, water/meals targets, tagged optional sections, explanation line | Done (TR + EN) |
| **docs/72-saat.md** | Created: formulas (water = hh×9, meals = hh×9), personalization rules, privacy note, UX note |
| **72_SAAT_PERSONALIZATION_REPORT.md** | This file |

---

## Files changed

- **72-saat/index.html** — Form: all radio groups use `.wizard-options-grid` and `.wizard-option`. Script: `answerLabels`, `buildChecklist` (waterL, meals, separate children/elderly/pets sections with `addedBecause`), `renderPlan` (explanation, summary box, target cards, section badges).
- **en/72-saat/index.html** — Same structure and script changes with EN copy.
- **assets/styles.css** — `.wizard-options-grid`, `.wizard-option`, `:has(input:checked)` selected state; `.plan-summary-box`, `.plan-targets`, `.plan-target-card`, `.plan-badge`, `.plan-explanation`.
- **docs/72-saat.md** — New: formulas and personalization rules documentation.
