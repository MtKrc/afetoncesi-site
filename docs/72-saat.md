# 72 Saat Hazırlık Planı – Formulas and personalization rules

This document describes how the 72-hour wizard computes quantities and which plan sections are added based on user answers. All logic is client-side; no backend.

## Water target (liters)

- **Formula:** `waterL = householdSize × 9`
- **Rationale:** Official guidance (e.g. AFAD, Red Cross) often recommends about **3 L of water per person per day**. For 72 hours (3 days): 3 L × 3 days = **9 L per person**. Total household water target = 9 × number of people.
- **Cap:** If user selects “5+”, we use 5 for the calculation (waterL = 45 L). Display still shows “5+ kişi” in the summary.

## Meals target (count)

- **Formula:** `meals = householdSize × 9`
- **Rationale:** Plan for **3 meals per person per day** for 3 days: 3 × 3 = **9 meals per person**. Total meals = 9 × number of people.
- **Cap:** Same as water; “5+” is treated as 5 for the number (meals = 45).

## Personalization rules (which sections appear)

| User answer | Section added | Label (TR) | Label (EN) |
|-------------|----------------|------------|------------|
| Children = Yes | Extra section | “Çocuk” — *Eklenme nedeni: çocuk* | “Children” — *Added because: children* |
| Elderly/special needs = Yes | Extra section | “Tıbbi / özel ihtiyaçlar” — *Eklenme nedeni: 65+ veya özel ihtiyaç* | “Medical / special needs” — *Added because: 65+ or special needs* |
| Pets = Yes | Extra section | “Evcil hayvan” — *Eklenme nedeni: evcil hayvan* | “Pets” — *Added because: pets* |

- Core sections (Water & food, First aid, Light/power, Documents, Clothing, Family plan) are always shown.
- Optional sections are only added when the corresponding answer is “yes”. Each optional section is clearly tagged so the user sees that it was added because of their answers.

## Data and privacy

- No personal data (address, name, etc.) is collected.
- All answers and the generated plan are stored only in the browser (`localStorage` key: `afeto_72h_v1`). Nothing is sent to a server.
- The plan page shows a short explanation: “Bu plan cevaplarınıza göre hesaplanır; kişisel veriler sunucuya gönderilmez.” / “This plan is computed from your answers; no personal data is sent to any server.”

## Required answers and defaults

- **Required steps (must select an option to proceed):** Step 1 (household size), Step 2 (children yes/no), Step 3 (65+ or special needs yes/no), Step 4 (pets yes/no).
- **Enforcement:** The “Next” button is disabled until an option is selected on steps 1–4. If the user somehow tries to advance without selecting (e.g. via keyboard or a future UI change), an inline message is shown: *“Bu bilgi planı doğru hesaplamak için gerekli.”* (TR) / *“This information is required to calculate your plan correctly.”* (EN).
- **No skipping:** Skipping required steps is not supported. The wizard does not use defaults for household, children, elderly, or pets; the plan is only generated when all four required answers are provided.
- **Optional steps:** Steps 5–8 (home type, car, region, kit level) are optional in the sense that “Next” / “Generate plan” is not disabled for them. If we ever allowed skipping and applied defaults, they would be documented here. Current behaviour: no defaults; user must select to proceed only for steps 1–4.

## UX (radio options)

- Every radio choice is a full-row clickable label (input + text inside one `<label>`).
- Options are laid out in a responsive grid: 1 column on mobile, 2 on tablet (≥640px), 3 on desktop (≥1024px).
- The selected option has a clear visual state (border and background) via `.wizard-option:has(input:checked)`.
