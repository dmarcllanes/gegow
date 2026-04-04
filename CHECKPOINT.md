# Gegow — Build Checkpoint

> Compact history of every change applied. Use this to resume context in future sessions.

---

## Stack
| Layer | Tech |
|---|---|
| Backend/Frontend | FastHTML (python-fasthtml) |
| Data Engine | Polars DataFrames |
| Database | Supabase (graceful degradation if unconfigured) |
| Package Manager | `uv` + `pyproject.toml` |
| Deployment | Docker (Hugging Face / Vercel) |
| PWA | `manifest.json` + `sw.js` service worker |

---

## Checkpoint 1 — Project Bootstrap
- Replaced `requirements.txt` with `pyproject.toml` (`uv` workflow)
- Dependencies: `python-fasthtml>=0.12.0`, `polars>=1.0.0`, `supabase>=2.0.0`, `python-dotenv>=1.0.0`, `uvicorn>=0.30.0`
- Added `Dockerfile` using `uv sync` + `uv run python -m app.main`
- Fixed `ModuleNotFoundError: No module named 'app'` → added `sys.path.insert(0, parent.parent)` in `app/main.py`

---

## Checkpoint 2 — Data Layer
**`data/flights_cache.csv`** — 20 rows (10 domestic PH, 10 international)
- Cols: `id, origin, destination, airline, departure, arrival, duration_min, base_price, type, origin_city, destination_city`

**`data/hotels_cache.csv`** — 15 rows (PH + international)
- Cols: `id, name, city, location, stars, base_price_per_night, amenities, type`

**`data/tours_catalog.csv`** — 14 rows (domestic + international)
- Cols: `id, name, destination, duration_days, duration_nights, type, base_price, includes, highlights`

---

## Checkpoint 3 — Polars Engine (`app/logic/polars_engine.py`)
Markup constants (midpoints per CLAUDE.md):
```python
MARKUP = {
  "domestic_flight": 325,    # +₱250–400/way
  "international_flight": 2000, # +₱1000–3000/way
  "hotel": 650,              # +₱300–1000/night
  "domestic_tour": 650,      # +₱400–900/person
  "international_tour": 1250,# +₱500–2000/person
}
```
Functions: `search_flights`, `search_hotels`, `search_tours`, `get_featured_flights/hotels/tours` (4+4 mix), `get_explore_feed`, `get_all_origins`, `get_destinations_for_origin`, `get_hotel_cities`

---

## Checkpoint 4 — Supabase (`app/logic/supabase_db.py`)
- Gracefully degrades when `SUPABASE_URL`/`SUPABASE_KEY` env vars are missing
- Functions: `is_configured()`, `save_itinerary`, `get_itineraries`, `save_b2b_lead`, `get_or_create_profile`

---

## Checkpoint 5 — UI Design System
Applied from `UI.md`:
```css
--gegow-primary: #006D77
--gegow-accent: #FF7043
--gegow-bg: #F1F1E6
--gegow-gradient-btn: linear-gradient(90deg, #FF7043, #F4511E)
--gegow-glass: rgba(255,255,255,0.7)
```
- `.btn-gegow` — coral gradient CTA, `border-radius: 12px`, `box-shadow` orange glow
- `.glass-nav` — `backdrop-filter: blur(10px)` + semi-transparent bg
- `.card-gradient-overlay` — dark overlay on card visuals
- `.wizard-step` — `transition: opacity 0.3s ease-in-out`
- Hero — `aurora` CSS keyframe animation on gradient background
- Cards — `repeat(auto-fill, minmax(280px, 1fr))` CSS Grid

---

## Checkpoint 6 — Navigation (`app/components/navigation.py`)
- **Sidebar** (desktop ≥768px): sticky, `#006D77` gradient, active item has white left-bar indicator + `translateX(2px)` hover
- **Mobile header**: teal gradient top bar, search icon button
- **Bottom nav**: glassmorphism (`var(--gegow-glass)` + blur), active item teal top-border, hidden on desktop

---

## Checkpoint 7 — Card Components (`app/components/cards.py`)
- `DEST_GRAD` — airport code → CSS gradient (16 destinations)
- `CITY_GRAD` — city name → CSS gradient (13 cities)
- `TOUR_GRAD` — domestic/international gradients
- `flight_card` — route codes, airline, time, selling price, Book Now CTA
- `hotel_card` — stars, amenities (first 3), price/night
- `tour_card` — duration badge, includes (first 3), price/person
- `gear_card` — emoji icon, HTMX add-to-cart (`hx-post=/gear/cart`)
- `section_header` — title + optional "See all →" link

---

## Checkpoint 8 — Booking Wizard (`app/components/wizard.py`)
5-step HTMX flow: **type → destination → dates → travelers → review → confirmed**
- Each step swaps `#wizard-body` via `hx-post` + `hx-target`
- `wizard_step1()` through `wizard_step5()`, `wizard_confirmed()`
- WIZARD_CSS includes `.wizard-step` fade transition

---

## Checkpoint 9 — Routes
| File | Routes |
|---|---|
| `app/routes/explore.py` | `GET /`, `GET /search` |
| `app/routes/booking.py` | `GET /book`, `POST /book/step1–5`, `POST /book/confirm` |
| `app/routes/shop.py` | `GET /gear`, `POST /gear/cart` — 12 gear items, category tabs |
| `app/routes/b2b.py` | `GET /b2b`, `POST /b2b/submit` — Manning + Corporate forms |

---

## Checkpoint 10 — Main App (`app/main.py`)
- `COMBINED_CSS` = base CSS + NAV_CSS + WIZARD_CSS in one `<style>` block
- `PWA_HEADERS` tuple passed to `fast_app(hdrs=...)` — includes Meta, Link, Style, **and both Scripts**
- `page_shell(content, active, title)` — returns full Html with sidebar + main-area + bottom_nav
- Number counters on explore page (IntersectionObserver-triggered)
- Suitcase page renders via `renderSuitcase()` JS on load

---

## Checkpoint 11 — Static Assets
**`static/app.js`**
- `document.body.classList.add('js-loaded')` — enables scroll animations (progressive enhancement)
- `IntersectionObserver` for `.fade-up → .in-view` scroll trigger
- Ripple effect on all `.btn-*` clicks
- Number counter animation (`data-count` attribute)
- `switchHeroTab(type)`, `adjustPax(type, delta)`
- `saveToSuitcase`, `renderSuitcase`, `removeItinerary` — localStorage suitcase
- `addToCart`, `updateCartBadge` — localStorage cart
- `seedDemoData()` — pre-fills 4 sample itineraries + 3 cart items on first load (skips if data exists)

**`static/sw.js`** — Network-first for dynamic, cache-first for `/suitcase` + `/explore`

**`static/manifest.json`** — PWA manifest, `theme_color: #0D9488`, shortcuts for flights/hotels/suitcase

---

## Checkpoint 12 — Bug Fixes
| Bug | Fix |
|---|---|
| `ModuleNotFoundError: app` | `sys.path.insert(0, parent.parent)` in main.py |
| `requirements.txt` instead of uv | Moved deps to `pyproject.toml`, deleted requirements.txt, updated Dockerfile |
| Desktop layout capped at 480px | Removed `max-width: 480px`, used flexbox `app-layout` + sticky sidebar |
| All content invisible at `/` | Scripts were only in `Body()` — FastHTML never rendered them. Fixed: moved both scripts into `PWA_HEADERS` so FastHTML always includes them in `<head>` |
| `.fade-up` stuck at `opacity:0` | Progressive enhancement: `.fade-up` defaults to `opacity:1`; only `.js-loaded .fade-up` starts hidden for animation |
| Hero text invisible | Removed `animation-fill-mode: both` → changed to `forwards` on all hero keyframe animations |

---

## File Map
```
gegow/
├── app/
│   ├── main.py               # Entry point, CSS, page_shell, all routes wired
│   ├── components/
│   │   ├── cards.py          # flight/hotel/tour/gear card FT components
│   │   ├── navigation.py     # sidebar, app_header, bottom_nav
│   │   ├── suitcase.py       # suitcase container (rendering via JS)
│   │   └── wizard.py         # 5-step booking wizard steps
│   ├── logic/
│   │   ├── polars_engine.py  # data loading, filtering, markup calc
│   │   └── supabase_db.py    # DB layer (graceful degradation)
│   └── routes/
│       ├── explore.py        # / and /search
│       ├── booking.py        # /book wizard
│       ├── shop.py           # /gear + cart
│       └── b2b.py            # /b2b forms
├── data/
│   ├── flights_cache.csv     # 20 flights (10 dom + 10 intl)
│   ├── hotels_cache.csv      # 15 hotels
│   └── tours_catalog.csv     # 14 tours
├── static/
│   ├── app.js                # All client-side logic + seed data
│   ├── sw.js                 # Service worker
│   ├── sw-register.js        # SW registration
│   └── manifest.json         # PWA manifest
├── pyproject.toml            # uv deps
├── Dockerfile                # uv-based container
├── CLAUDE.md                 # Project spec + markup rules
└── UI.md                     # Design tokens source of truth
```

---

## Checkpoint 13 — Landing, Auth & OAuth
**`/landing`** — dark-theme marketing page: glassmorphism nav, animated hero, features grid, destinations scroll, testimonials, footer

**`/login`** + **`/signup`** — mobile-first auth pages: Google OAuth button, show/hide password, password strength meter (signup), remember me

**Google OAuth (Supabase PKCE flow):**
- `GET /auth/google` → PKCE pair, `gegow_cv` cookie (5 min), redirect to Supabase
- `GET /auth/callback` → exchange code, set `gegow_token` (7d) + `gegow_refresh` (30d) cookies
- `GET /auth/logout` → clear cookies, redirect `/login`
- `supabase_db.py`: `_pkce_pair`, `get_google_oauth_url`, `exchange_pkce_code`, `get_user_from_token`
- **Required**: add `{APP_URL}/auth/callback` to Supabase Redirect URLs + Google Console Authorized URIs
- `APP_URL=http://localhost:8000` in `.env`

---

## Checkpoint 14 — Dashboard UX & Profile Page
**`/dashboard`** redesigned with user context:
- Welcome card (teal gradient): time-based greeting, avatar initial, name, 👤 profile link, 🚪 Log out button (always visible)
- Status strip: Saved Trips · Bookings · Rewards (tap to navigate)
- Guest state: sign-in strip with CTA
- Reads `gegow_token` cookie → `get_user_from_token` → name/initials

**`/profile`** — personal dashboard page:
- Hero: avatar, name, email, member badge, Log out button
- Stats row, saved itineraries list (Supabase `suitcase` table), quick actions grid, travel preferences

**Navigation fixes:**
- Bottom nav trimmed to 5 tabs (removed Profile — too cramped); Profile in sidebar + welcome card
- Sidebar: added 👤 My Profile item + 🚪 Log out button at footer
- Mobile header: added 🚪 logout icon button next to search

---

## Checkpoint 15 — Landing Page Redesign (`app/pages/landing.py`)

**Navbar (full rewrite):**
- CSS variables `--nav-pre-txt/muted/btn-bg/btn-border` per theme (white on dark hero, dark on light hero) — fixes invisible text in light mode on transparent nav
- Mobile (< 900px): logo + [theme-toggle + hamburger]; hamburger opens `.nav-drawer` with all 5 links + Install App + Sign in/Get started
- Desktop (≥ 900px): logo · centered links · [Install, theme-toggle, Sign in, Get started]
- Hamburger animates 3 bars → X; closes on link tap or outside click; `body.overflow:hidden` while open
- Install button in drawer (`id="btn-install-drawer"`) wired to same `triggerInstall()` — visible on all screen sizes

**Hero search widget → animated image viewer:**
- Removed: tabs (Flights/Hotels/Tours), all form fields, `_sel/_date/_counter` helpers, `Select/Option/Label` imports
- Added: `hero-visual` — 16:9 (4:3 on mobile) image slider, 6 destinations
- **Ken Burns**: active slide zooms `scale(1.06)→scale(1)` over 7s
- **Crossfade**: 1s opacity transition, auto-advances every 4.5s, pauses on hover
- **Glassmorphism card** (bottom): frosted dark glass, destination name + tag + "From ₱X" price + "Explore →" CTA linking to `/book?type=tour&tour_dest=X`
- **Badge** (top-left): "🔥 Trending", "🇵🇭 Local Favorite" etc., animates in per slide
- **Dots** (top-right): pill-shaped, active dot stretches wide; click to jump
- **Arrows**: prev/next, appear on hover, frosted glass
- **Touch swipe**: left/right swipe on mobile
- Slide data passed via `#hv-data` JSON island; JS reads it to update glass card on transition

**Light mode fixes:**
- `hero-content` now uses `var(--hero-txt)` instead of hardcoded `color:#fff`
- Select option backgrounds use `var(--search-card-bg)` (already removed with form)

**Hero CTA:** Changed "Explore →" button to `A("Login →", href="/login")` — directs visitors to sign in

**Install strip moved to footer:**
- Removed standalone install section between hero and features
- Embedded compact install strip at top of `_footer()` with platform-split buttons (Android / iOS)
- `.footer-install` CSS: dark gradient bg, `var(--txt)` / `var(--muted)` for light-mode compatibility

**Scroll hint:** Moved from `position:absolute;bottom:24px` into `hero-content` as in-flow element (`margin-top:28px`) to prevent overlap with trust pills

---

## Checkpoint 16 — Login Page Rewrite (`app/pages/auth.py`)

Full dark-glassmorphism redesign to match landing page aesthetic:
- **Background**: mesh radial gradient (`rgba(0,201,177,.18)` teal + `rgba(255,107,53,.13)` coral + `rgba(0,150,200,.12)` blue) on `#04111a` + animated orbs + dot grid overlay
- **Glass card**: `max-width:420px`, `backdrop-filter:blur(28px)`, `border-radius:28px`, `rgba(255,255,255,.07)` bg, `box-shadow:0 32px 80px rgba(0,0,0,.5)`
- **Brand**: teal gradient logo icon (`linear-gradient(135deg,#00C9B1,#009e8c)`) with `box-shadow:0 0 32px rgba(0,201,177,.4)`, brand name + sub
- **Destination pills**: Palawan · Tokyo · Singapore · Siargao (`.login-dest-pill`)
- **Google button**: white bg so SVG brand colors render correctly; hover lifts with shadow
- **"← Back to Gegow"** frosted glass link top-left (`.lp-back`)
- `theme-color` meta: `#04111a`
- Removed: show/hide password, strength meter (OAuth-only flow, no password inputs)

---

## Checkpoint 17 — Dashboard Cleanup (`app/main.py`)

Progressively removed clutter from `/dashboard`:
1. **Removed hero widget** (`_hero_widget()`) — search form redundant with `/book` page
2. **Removed trust bar** — unnecessary on authenticated dashboard
3. **Removed entire welcome banner** (`if user / else top_section` block with `time-based greeting, avatar, status-strip, guest-strip`) — sidebar already shows navigation and identity context
- Dashboard `content` now starts directly with quick-links grid
- Removed unused imports: `get_user_from_token`, `get_itineraries`, `datetime`

---

## Checkpoint 18 — Sidebar Redesign (`app/components/navigation.py`)

Full dark premium rewrite to match landing page theme:

**Sidebar (desktop ≥768px):**
- **Background**: `radial-gradient` teal + coral mesh on `#04111a` base + `::before` dot grid overlay (`28px × 28px`, `rgba(255,255,255,.03)`)
- **Logo icon**: `linear-gradient(135deg,#00C9B1,#009e8c)`, `border-radius:12px`, `box-shadow:0 0 20px rgba(0,201,177,.4)`
- **Nav items default**: `color:rgba(255,255,255,.5)`, hover `translateX(3px)` + `rgba(255,255,255,.07)` bg
- **Nav items active**: teal color `#00C9B1`, `rgba(0,201,177,.12)` bg, `border:1px solid rgba(0,201,177,.2)`, glowing left accent bar (`box-shadow:0 0 8px rgba(0,201,177,.6)`), icon `filter:drop-shadow(0 0 6px rgba(0,201,177,.5))`
- **Divider**: `linear-gradient(90deg,transparent,rgba(255,255,255,.08),transparent)`
- **Logout button**: `rgba(239,68,68,.1)` bg, red-tinted text, `border:1px solid rgba(239,68,68,.2)`

**Mobile header:**
- `linear-gradient(90deg,#04111a,#005760)` bg
- Logout icon button with red-tinted styling

**Bottom nav:**
- `rgba(4,17,26,.92)` frosted glass + `backdrop-filter:blur(20px)`
- Active item: `color:#00C9B1`, `::after` gradient top indicator (`linear-gradient(90deg,transparent,#00C9B1,transparent)`) with `box-shadow:0 0 8px rgba(0,201,177,.6)`

---

## Checkpoint 19 — Full UI/UX Overhaul (Previous Session)

### Navigation (`app/components/navigation.py`) — full rewrite
- **Sidebar**: `background:#070f1a`, teal radial glow via `::after`, profile card (`.sidebar-profile`), underline active indicator with teal left bar, clean footer with logout
- **Mobile header** (`.gegow-header`): `rgba(7,15,26,.96)` + `backdrop-filter:blur(18px)`, matching bottom nav — replaced search icon with teal gradient avatar `.gh-avatar` + red-on-hover logout `.gh-logout`
- **Bottom nav**: same dark frosted glass as header, teal active top-line with glow
- Removed "My Profile" from sidebar nav items list

### Explore / Dashboard (`app/main.py` — `/dashboard` route)
- Removed Gear and B2B category pills and card sections from explore
- Added unified `.filter-bar` holding both rows: `.cat-tabs` (underline-style, centered) + `.sub-tabs-wrap` (rectangular chip sub-filters)
- Sub-categories: Flights → Domestic/International · Hotels → Local/International · Tours → Local/International
- `data-subcat` attribute added to all `flight_card`, `hotel_card`, `tour_card` for client-side filtering
- `filterCat()` / `filterSub()` JS for show/hide logic
- All banners unified to `var(--beige)` background; `.dash-search-banner` centered via `.dsb-inner`
- `sec_head()` helper replaces old `section_header` in main.py

### Booking Wizard (`app/components/wizard.py`) — full artistic rewrite
- `_wrap(current, *children)` helper: returns `.wizard-page#wizard-content > .wizard-card` structure
- `_step_indicator(current)`: named step labels (Type / Where / Dates / Who / Review) below dots
- Step 1: three photo-backed `.type-card` elements (Unsplash, `aspect-ratio:2/3`, hover lift)
- All steps use `hx_swap="outerHTML"` targeting `#wizard-content` (the `.wizard-page` wrapper)
- Forms: uppercase labels, `border-radius:12px` inputs, 2-col `form-row` grid
- Pax: `.pax-card` beige cards with `.pax-stepper`
- Review: `.review-card` teal gradient header + coral confirm button
- Confirmation: teal gradient icon circle, reference box, two action buttons

### Routing fixes (`app/routes/booking.py`, `shop.py`, `b2b.py`)
- Removed `@rt('/book')`, `@rt('/gear')`, `@rt('/b2b')` root handlers from `setup()` files (Starlette first-match was shadowing `page_shell`-wrapped versions in `main.py`)
- `/book` route in `main.py` simplified: now just passes `wizard_step1()` directly to `page_shell()`

### Wizard HTMX fix
- `id="wizard-content"` moved from `.wizard-card` (inner) to `.wizard-page` (outer) in both `_wrap()` and `wizard_confirmed()` — prevents nested `.wizard-page` shells on each HTMX outerHTML swap

---

## Checkpoint 20 — Explore Pagination

### `app/logic/polars_engine.py`
- Added `PAGE_SIZE = 8`
- Added `_paginate(df, page, sub)` — filters by `sub` (domestic/international/all), slices 8 rows, returns `{items, page, pages, total}`
- Added `get_flights_page(page, sub)`, `get_hotels_page(page, sub)`, `get_tours_page(page, sub)`

### `app/routes/explore.py`
- Added `_pagination_bar(section, page, pages, sub, total)` — renders Prev / `Page X of Y` / Next with HTMX attributes
- Added `GET /dashboard/page/{section}?page=N&sub=X` route — returns card grid + pagination bar (inner content only, targeting `#{section}-content`)

### `app/main.py` — `/dashboard` route
- Dashboard now loads page 1 server-side via `get_flights_page(1)` etc.
- Each category section split into outer `#cat-{section}` (show/hide by filterCat) + inner `#{section}-content` (HTMX pagination target)
- `filterSub()` JS changed from client-side card hide/show → `htmx.ajax()` reload to page 1 with new sub filter
- `filterCat()` JS also calls `htmx.ajax()` to reset section to page 1 / sub=all when switching category
- Added `.pagination-bar`, `.pg-btn`, `.pg-info`, `.pg-btn.pg-disabled` CSS

---

## Checkpoint 21 — My Suitcase Redesign (`app/components/suitcase.py`)

Full rewrite — all rendering is client-side JS reading from `localStorage('gegow_suitcase')`.

### Hero
- Dark `#070f1a` background + teal radial glow (matches sidebar)
- Three live stat cards: **Total Trips** / **Upcoming** / **Total Spent** (computed on render)

### Status tabs
- All · Upcoming · Active · Completed
- Live count badge on each tab, teal underline on active
- Status computed from dates: `upcoming` (from > today), `active` (from ≤ today ≤ to), `completed` (to < today)

### Trip cards
- Unsplash photo header per type (flight/hotel/tour) + gradient overlay
- Status pill: blue "Upcoming" · pulsing teal "On Trip" · gray "Completed"
- Type icon, destination label, `REF #XXXXX` tag, delete button (with confirm)
- 2×2 info grid: Departure/Check-in · Return/Check-out · Duration · Travelers
- Total price + "Book Again" CTA

### Empty states
- Unique icon + message per tab; "Book a Trip →" CTA on the empty All state

### `static/app.js` updates
- `seedDemoData()` expanded to 6 trips covering all three statuses:
  - 3 upcoming (flight MNL→CEB, hotel Boracay, flight MNL→SIN)
  - 1 active (tour Siargao, overlapping today 2026-03-31)
  - 2 completed (tour Palawan Feb 2026, hotel Jan 2026)
- Removed `renderSuitcase()` call from `DOMContentLoaded` (new suitcase IIFE handles rendering)
- `SUITCASE_CSS` imported and added to `COMBINED_CSS` in `main.py`

---

## Run
```bash
uv run python -m app.main       # dev
docker build -t gegow . && docker run -p 8000:8000 gegow  # prod
```
