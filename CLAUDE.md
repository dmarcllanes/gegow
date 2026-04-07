# Gegow: Digital Travel Agency PWA

## Project Overview
Gegow is a "digital-in-pocket" travel agency built using FastHTML and Polars. It connects to the Bakasyonista backend to offer flights, hotels, tours, and dropshipped travel gear with custom markup logic.

## Tech Stack
- **Backend/Frontend**: FastHTML (Python-based)
- **Data Engine**: Polars (for high-speed catalog processing and markup calcs)
- **Database**: Supabase (User profiles, "My Suitcase" itineraries, B2B leads)
- **Deployment**: Docker on Hugging Face or Vercel
- **PWA**: Manifest.json + Service Workers for offline itinerary access

## Business Logic & Markups
- **Domestic Flights**: +₱250 - ₱400 profit per way
- **International Flights**: +₱1,000 - ₱3,000+ profit per way
- **Hotel Stays**: +₱300 - ₱1,000 profit per night
- **Joiner/Domestic Tours**: +₱400 - ₱900 profit per person
- **International Tours**: +₱500 - ₱2,000+ profit per person

## Core Features
1. **Gegow Path (Wizard)**: 5-step booking flow to prevent information overload.
2. **My Suitcase**: Offline-ready storage for vouchers and schedules.
3. **Gegow-Gear**: Dropshipping store for travel items.
4. **B2B Portal**: Specialized entry for Manning Agencies and Corporate clients.

## Coding Guidelines
- Use **FastHTML** components for modular UI (Cards, Wizards, Modals).
- Use **Polars DataFrames** for all heavy filtering of the Bakasyonista CSV/API data.
- Maintain a **Teal and Beige** color palette for a modern "Philippine Sea" aesthetic.
- Ensure all forms use the **Wizard pattern** to maintain simplicity.

---

## Design System

### Color Tokens (`app/main.py` — CSS `:root`)
| Token | Value | Usage |
|---|---|---|
| `--teal` | `#006D77` | Primary brand color |
| `--teal-dk` | `#005760` | Darker teal for gradients |
| `--teal-lt` | `#B2DFDB` | Light teal accents |
| `--teal-xl` | `#E0F2F1` | Very light teal backgrounds |
| `--beige` | `#F1F1E6` | Page background |
| `--border` | `#DDD9CE` | Default borders |
| `--border-dk` | `#C8C4B8` | Darker borders on hover |
| `--text` | `#0F172A` | Primary text |
| `--muted` | `#5F6B72` | Secondary/muted text |
| `--muted-lt` | `#94A3B8` | Lightest muted text |
| `--amber` | `#FF7043` | CTA / confirm accent |

### Hero Gradient (consistent across all pages)
All page heroes use the same gradient for visual consistency:
```css
background: linear-gradient(160deg, #04111a 0%, #005760 55%, #0a9aa8 100%);
```
With a grid pattern overlay:
```css
::before {
  background-image:
    linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
  background-size: 48px 48px;
}
```
And a curved beige bottom edge:
```css
::after {
  height: 28px; background: var(--beige);
  border-radius: 20px 20px 0 0;
  position: absolute; bottom: -1px; left: 0; right: 0;
}
```
Pages using this pattern: **Dashboard search banner**, **My Suitcase**, **Shop/Gear**.

---

## UI Components & Patterns

### Bottom Navigation (`app/components/navigation.py`)
- Floating pill-style glassmorphism bottom nav on mobile
- Container uses `pointer-events: none`; inner `.bn-inner` pill uses `pointer-events: auto` to prevent blocking page content
- `NAV_ITEMS` is a 4-tuple: `(icon, label, short_label, href)`
- Active item: teal gradient bubble + top glow `::before` + icon `scale(1.18) translateY(-1px)` + `drop-shadow`
- Safe area padding: `padding: 0 12px calc(env(safe-area-inset-bottom, 8px) + 8px)`
- Top header height: 58px with teal `::after` accent line

### Wizard / Gegow Path (`app/components/wizard.py`)
5-step booking flow: Type → Where → Dates → Who → Review

**Progress header**: Label + step dots + step labels. No back button in the header (removed).

**Step 1**: Animated card-row layout (`type-card-new`) with SVG icons (paper plane, hotel building with blinking windows, compass with spinning needle). "← Back to Explore" button at the bottom.

**Button styles**:
- `.btn-next` — teal gradient (`#00c9b1 → #005c66`), shimmer sweep `::before` on hover, lifts 2px
- `.btn-confirm` — amber gradient (`#FF7043 → #d44020`), same shimmer treatment
- `.btn-back` — white background, 1.5px border, subtle shadow; hover shifts to beige + lifts 1px
- `.btn-suitcase` — teal gradient (same as `btn-next`), shimmer sweep; used on confirmation screen
- `.btn-again` — white background, bordered (same style as `btn-back`)

All action buttons use `display: flex; align-items: center; justify-content: center` and `position: relative; overflow: hidden` for the shimmer effect.

### Dashboard / Explore (`app/main.py` — `/dashboard` route)

**Search Banner** (`.dash-search-banner`):
- Uses the standard hero gradient + grid pattern + curved bottom edge
- Glassmorphism search row: `background: rgba(255,255,255,.1)`, `backdrop-filter: blur(16px)`, unified pill container (no separate border on input)
- Teal gradient search button flush inside the pill
- No destination chips in the hero — those live in the filter bar

**Filter Bar** (`.filter-bar`):
- Background: `var(--beige)` — consistent with the rest of the page
- **Category tabs** (`.cat-pill`): white background, 1.5px border, rounded card-pills; active = solid teal fill + shadow
- **Sub-rows** (dynamic, toggled by `filterCat` JS):
  - `#sub-all` — Popular Destinations row (Cebu, Boracay, Siargao, Baguio, Tokyo, Singapore, Abroad); visible when "All" is active
  - `#sub-flights` / `#sub-hotels` / `#sub-tours` — Domestic / International chips; visible only for the active category
- **Sub-pills** (`.sub-pill`): white background, 1.5px border, 20px border-radius; active = teal fill

**`filterCat(pill, cat)` logic**:
- Hides all `.sub-tabs`
- If `cat === 'all'`: shows `#sub-all` (destinations)
- If specific category: hides `#sub-all`, shows `#sub-{cat}`, resets sub-pill to "all", fires HTMX reload

### My Suitcase (`app/components/suitcase.py`)
- Hero: same standard gradient + grid + curved bottom edge
- Stats grid: 3-column glassmorphism cards (`rgba(255,255,255,.08)` background)
- Eyebrow label with pulsing dot animation (`sc-dot-pulse`)
- Offline-ready: data stored/read from `localStorage`

### Shop / Gegow-Gear (`app/routes/shop.py` + `app/main.py`)
- Hero: dark teal gradient (`#006D77 → #004d55 → #0a1628`) with grid pattern
- Sticky category tabs (`.category-tabs`) on white background; `.cat-tab` active = teal pill
- Gear grid: 2-col mobile → 3-col at 520px → 4-col at 900px+

### B2B Portal (`app/routes/b2b.py`)
- Tab-pills to switch between Manning Agency and Corporate
- Benefit icon cards + labeled form fields
- Form grid: 1-col mobile, 2-col at 400px+
- Body layout: sidebar at 280px (768px+), 300px (1024px+), 340px (1200px+)

### Splash Screen (`app/main.py` + `static/app.js`)
- Overlay `#app-splash` injected at top of `<body>` via `_splash_overlay()`
- Shows once per browser session using `sessionStorage.getItem('gegow_splashed')`
- Auto-dismisses after 3 seconds; click to dismiss early
- Displays promo package cards from `_SPLASH_PROMOS` list
- Exit animation: `.splash-exit` class → `opacity: 0` + `scale(.96)` over 520ms

---

## Responsive Breakpoints
All components use mobile-first design with these breakpoints:
| Breakpoint | Usage |
|---|---|
| `< 360px` | Tiny phones — 1-col grids, compact padding |
| `480px` | Small phones — standard mobile layout |
| `768px` | Tablet — sidebar appears, larger padding |
| `1024px` | Small desktop |
| `1200px` | Large desktop — max sidebar width, larger padding |

---

## File Structure
```
app/
├── main.py              # App entry, CSS, page_shell(), all route handlers
├── components/
│   ├── navigation.py    # Header, sidebar, bottom nav (NAV_CSS)
│   ├── wizard.py        # 5-step booking wizard (WIZARD_CSS)
│   ├── suitcase.py      # My Suitcase page (SUITCASE_CSS)
│   └── cards.py         # flight_card, hotel_card, tour_card, quick-book modal
├── routes/
│   ├── explore.py       # /search, /dashboard/page/{section}
│   ├── booking.py       # /book/step1–5, /book/confirm
│   ├── shop.py          # /gear/cart, shop catalog
│   ├── b2b.py           # /b2b, /b2b/submit (B2B_CSS)
│   └── monitoring.py    # /monitoring (MONITORING_CSS)
└── logic/
    ├── polars_engine.py  # CSV loading, filtering, markup calc, pagination
    └── supabase_db.py    # Auth, itinerary storage, B2B leads
static/
├── app.js               # Splash dismiss, filterCat/filterSub, search enter key
├── manifest.json        # PWA manifest
└── sw.js                # Service worker for offline support
```

---

## Known Patterns & Decisions
- **`main-area` padding-bottom**: `calc(82px + env(safe-area-inset-bottom, 0px))` — accounts for floating bottom nav height
- **Cart drawer width**: `width: min(340px, 100vw)` — reliable on all screen sizes
- **Wizard back button removed from header**: The `← Back` button was removed from `.wizard-progress` header; back navigation is handled by the `btn-back` button at the bottom of each step body
- **Shimmer on primary buttons**: All `.btn-next`, `.btn-confirm`, `.btn-suitcase` use a `::before` pseudo-element that sweeps left-to-right on hover (`left: -100%` → `left: 150%`)
- **Destination chips vs sub-filters**: Destination chips (`#sub-all`) and category sub-filters (`#sub-flights` etc.) are mutually exclusive — only one row is visible at a time, controlled by `filterCat()`
