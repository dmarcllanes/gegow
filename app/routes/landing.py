"""
Gegow — Landing page. Mobile-first, PWA-ready.
Designed to look and feel like a real travel app on any screen.
"""

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Link, Style, Script,
    Div, Nav, Footer, Span, A, Button, Input, P, H1, H2, H3,
)

# ─────────────────────────────────────────────────────────────
# CSS — mobile-first, then tablet/desktop via min-width queries
# ─────────────────────────────────────────────────────────────
LANDING_CSS = """
/* ── Base reset ──────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Inter, sans-serif;
  background: #ffffff;
  color: #1a1a2e;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}
a { text-decoration: none; color: inherit; }
img { display: block; max-width: 100%; }
/* Prevent 300ms tap delay */
a, button { -webkit-tap-highlight-color: transparent; touch-action: manipulation; }

/* ── Tokens ───────────────────────────────────────────────── */
:root {
  --primary:    #006D77;
  --primary-dk: #005760;
  --primary-lt: #e0f2f1;
  --accent:     #FF7043;
  --accent-dk:  #e64a19;
  --text:       #1a1a2e;
  --text-2:     #4a5568;
  --text-3:     #94a3b8;
  --border:     #e8ecf0;
  --bg:         #f8fafc;
  --white:      #ffffff;
  --radius:     16px;
  --radius-sm:  10px;
  --safe-top:   env(safe-area-inset-top, 0px);
  --safe-bot:   env(safe-area-inset-bottom, 0px);
}

/* ── Navbar ───────────────────────────────────────────────── */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 0 20px;
  height: 56px;
  display: flex; align-items: center; justify-content: space-between;
  padding-top: var(--safe-top);
}
.nav-logo {
  display: flex; align-items: center; gap: 8px;
  font-size: 18px; font-weight: 800; color: var(--primary);
  letter-spacing: -.4px;
}
.nav-logo-mark {
  width: 32px; height: 32px; border-radius: 9px;
  background: var(--primary);
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; flex-shrink: 0;
}
.nav-links {
  display: none;
  gap: 28px; align-items: center;
}
@media (min-width: 768px) { .nav-links { display: flex; } }
.nav-links a {
  font-size: 14px; font-weight: 500; color: var(--text-2);
  transition: color .15s;
}
.nav-links a:hover { color: var(--primary); }
.nav-actions { display: flex; align-items: center; gap: 8px; }
.btn-nav-ghost {
  padding: 7px 16px; border-radius: 8px;
  font-size: 13px; font-weight: 600; color: var(--text-2);
  border: 1px solid var(--border); background: transparent;
  cursor: pointer; transition: all .15s;
}
.btn-nav-ghost:hover { border-color: var(--primary); color: var(--primary); }
.btn-nav-fill {
  padding: 7px 18px; border-radius: 8px;
  font-size: 13px; font-weight: 700; color: var(--white);
  background: var(--primary); border: none;
  cursor: pointer; transition: background .15s;
}
.btn-nav-fill:hover { background: var(--primary-dk); }
/* hide login on mobile, show only Get started */
.btn-nav-ghost { display: none; }
@media (min-width: 480px) { .btn-nav-ghost { display: inline-flex; } }

/* ── Hero ─────────────────────────────────────────────────── */
.hero {
  background: linear-gradient(160deg, var(--primary-dk) 0%, var(--primary) 60%, #0a9396 100%);
  padding: 40px 20px 0;
  overflow: hidden;
  position: relative;
  min-height: 520px;
  display: flex; flex-direction: column;
}
@media (min-width: 768px) {
  .hero { padding: 64px 48px 0; min-height: 580px; }
}
/* subtle wave bottom */
.hero::after {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0; height: 40px;
  background: var(--white);
  clip-path: ellipse(54% 100% at 50% 100%);
}
.hero-tag {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(255,255,255,.15);
  border: 1px solid rgba(255,255,255,.25);
  border-radius: 20px; padding: 5px 12px;
  font-size: 12px; font-weight: 700; color: rgba(255,255,255,.95);
  letter-spacing: .3px; margin-bottom: 20px; width: fit-content;
}
.hero-tag-dot { width: 6px; height: 6px; border-radius: 50%; background: #5eead4; }
.hero-title {
  font-size: clamp(28px, 8vw, 52px);
  font-weight: 900; color: #fff;
  line-height: 1.1; letter-spacing: -.5px;
  margin-bottom: 14px;
}
.hero-title em {
  font-style: normal;
  background: linear-gradient(90deg, #a7f3d0, #67e8f9);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero-sub {
  font-size: 15px; color: rgba(255,255,255,.75);
  line-height: 1.6; max-width: 420px; margin-bottom: 32px;
}
@media (min-width: 768px) { .hero-sub { font-size: 17px; } }
.hero-btns { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 40px; }
.btn-hero-main {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 14px 28px; border-radius: 12px;
  font-size: 15px; font-weight: 700; color: #fff;
  background: var(--accent); border: none; cursor: pointer;
  box-shadow: 0 4px 20px rgba(255,112,67,.45);
  transition: transform .15s, box-shadow .15s;
  min-height: 50px;
}
.btn-hero-main:active { transform: scale(.97); }
.btn-hero-ghost {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 14px 22px; border-radius: 12px;
  font-size: 15px; font-weight: 600; color: rgba(255,255,255,.9);
  background: rgba(255,255,255,.15);
  border: 1px solid rgba(255,255,255,.25); cursor: pointer;
  transition: background .15s;
  min-height: 50px;
}
.btn-hero-ghost:active { background: rgba(255,255,255,.25); }

/* ── Search bar (hero bottom) ─────────────────────────────── */
.hero-search {
  background: #fff;
  border-radius: 14px;
  padding: 6px 6px 6px 16px;
  display: flex; align-items: center; gap: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,.15);
  margin-bottom: 48px;
  max-width: 560px;
}
.hero-search input {
  flex: 1; border: none; outline: none; background: transparent;
  font-size: 15px; color: var(--text); font-family: inherit;
  min-width: 0; padding: 8px 0;
}
.hero-search input::placeholder { color: var(--text-3); }
.btn-search {
  padding: 10px 20px; border-radius: 10px;
  font-size: 14px; font-weight: 700; color: #fff;
  background: var(--primary); border: none; cursor: pointer;
  white-space: nowrap; min-height: 42px;
  transition: background .15s;
}
.btn-search:active { background: var(--primary-dk); }

/* ── Category tabs ────────────────────────────────────────── */
.categories {
  background: #fff; padding: 20px 0 4px;
  border-bottom: 1px solid var(--border);
  position: sticky; top: 56px; z-index: 50;
}
.cat-scroll {
  display: flex; gap: 8px; padding: 0 20px;
  overflow-x: auto; scrollbar-width: none;
}
.cat-scroll::-webkit-scrollbar { display: none; }
.cat-btn {
  display: flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: 20px;
  font-size: 13px; font-weight: 600;
  border: 1.5px solid var(--border); background: #fff;
  color: var(--text-2); white-space: nowrap; cursor: pointer;
  transition: all .15s; min-height: 38px;
  flex-shrink: 0;
}
.cat-btn.active {
  background: var(--primary); border-color: var(--primary);
  color: #fff; box-shadow: 0 2px 10px rgba(0,109,119,.3);
}
.cat-btn:active { transform: scale(.96); }

/* ── Section ─────────────────────────────────────────────── */
.section { padding: 32px 20px; }
@media (min-width: 768px) { .section { padding: 48px 32px; max-width: 1100px; margin: 0 auto; } }
.section-hd {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 18px;
}
.section-title { font-size: 18px; font-weight: 800; color: var(--text); letter-spacing: -.3px; }
@media (min-width: 768px) { .section-title { font-size: 22px; } }
.section-more {
  font-size: 13px; font-weight: 700; color: var(--primary);
  display: flex; align-items: center; gap: 2px;
  white-space: nowrap;
}

/* ── Destination cards (horizontal scroll) ────────────────── */
.dest-row {
  display: flex; gap: 12px;
  overflow-x: auto; scrollbar-width: none;
  padding-bottom: 8px; margin: 0 -20px; padding: 0 20px 8px;
}
.dest-row::-webkit-scrollbar { display: none; }
.dest-card {
  flex-shrink: 0;
  width: 160px; height: 200px;
  border-radius: var(--radius); overflow: hidden;
  position: relative; cursor: pointer;
  transition: transform .2s;
}
@media (min-width: 480px) { .dest-card { width: 180px; height: 220px; } }
.dest-card:active { transform: scale(.97); }
.dest-card-bg {
  position: absolute; inset: 0;
  transition: transform .3s;
}
.dest-card-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.75) 0%, rgba(0,0,0,.1) 50%, transparent 100%);
}
.dest-card-body { position: absolute; bottom: 0; left: 0; right: 0; padding: 12px; }
.dest-name  { font-size: 14px; font-weight: 800; color: #fff; }
.dest-price { font-size: 11px; color: rgba(255,255,255,.7); margin-top: 2px; }
.dest-hot   {
  position: absolute; top: 10px; left: 10px;
  background: var(--accent); color: #fff;
  font-size: 9px; font-weight: 800; padding: 3px 7px; border-radius: 6px;
  letter-spacing: .3px;
}

/* ── Feature cards (vertical stack mobile, grid desktop) ─── */
.feature-grid {
  display: flex; flex-direction: column; gap: 12px;
}
@media (min-width: 640px) {
  .feature-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
}
@media (min-width: 1024px) {
  .feature-grid { grid-template-columns: repeat(3, 1fr); }
}
.feature-card {
  display: flex; align-items: flex-start; gap: 14px;
  padding: 18px; border-radius: var(--radius);
  border: 1.5px solid var(--border); background: var(--white);
  transition: border-color .2s, box-shadow .2s;
}
.feature-card:hover { border-color: var(--primary); box-shadow: 0 4px 20px rgba(0,109,119,.08); }
.feature-icon-wrap {
  width: 44px; height: 44px; border-radius: 12px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-size: 20px; background: var(--primary-lt);
}
.feature-text-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
.feature-text-desc  { font-size: 13px; color: var(--text-2); line-height: 1.55; }

/* ── Deal cards (vertical) ───────────────────────────────── */
.deal-row {
  display: flex; flex-direction: column; gap: 12px;
}
@media (min-width: 640px) {
  .deal-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
}
@media (min-width: 1024px) {
  .deal-row { grid-template-columns: repeat(3, 1fr); }
}
.deal-card {
  border-radius: var(--radius); border: 1.5px solid var(--border);
  overflow: hidden; background: #fff;
  transition: box-shadow .2s, transform .15s; cursor: pointer;
}
.deal-card:hover { box-shadow: 0 8px 28px rgba(0,0,0,.08); transform: translateY(-2px); }
.deal-card:active { transform: scale(.98); }
.deal-card-img {
  height: 140px;
  background-size: 100%; background-position: center;
  position: relative;
}
@media (min-width: 640px) { .deal-card-img { height: 160px; } }
.deal-card-badge {
  position: absolute; top: 10px; left: 10px;
  padding: 4px 10px; border-radius: 6px;
  font-size: 10px; font-weight: 800; letter-spacing: .3px;
}
.badge-dom  { background: rgba(0,109,119,.9); color: #fff; }
.badge-intl { background: rgba(99,102,241,.9); color: #fff; }
.badge-hot  { background: rgba(255,112,67,.9); color: #fff; }
.deal-card-body { padding: 14px; }
.deal-card-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 4px; line-height: 1.3; }
.deal-card-meta  { font-size: 12px; color: var(--text-3); margin-bottom: 10px; }
.deal-card-foot  { display: flex; align-items: center; justify-content: space-between; }
.deal-price      { font-size: 16px; font-weight: 800; color: var(--primary); }
.deal-price-unit { font-size: 11px; color: var(--text-3); font-weight: 500; }
.btn-deal {
  padding: 7px 14px; border-radius: 8px;
  font-size: 12px; font-weight: 700; color: #fff;
  background: var(--primary); border: none; cursor: pointer;
  transition: background .15s; min-height: 34px;
}
.btn-deal:active { background: var(--primary-dk); }

/* ── Trust strip ──────────────────────────────────────────── */
.trust-strip {
  background: var(--bg); padding: 28px 20px;
  display: flex; flex-direction: column; gap: 16px; align-items: center;
}
@media (min-width: 640px) {
  .trust-strip { flex-direction: row; justify-content: center; gap: 40px; padding: 28px 32px; }
}
.trust-item {
  display: flex; align-items: center; gap: 10px;
}
.trust-icon {
  width: 40px; height: 40px; border-radius: 10px;
  background: var(--primary-lt);
  display: flex; align-items: center; justify-content: center; font-size: 18px;
}
.trust-label { font-size: 12px; color: var(--text-3); }
.trust-value { font-size: 15px; font-weight: 800; color: var(--text); }

/* ── Stats bar ────────────────────────────────────────────── */
.stats-bar {
  background: var(--primary);
  display: grid; grid-template-columns: repeat(2, 1fr);
  gap: 1px;
}
@media (min-width: 640px) { .stats-bar { grid-template-columns: repeat(4, 1fr); } }
.stat-item {
  padding: 24px 20px; text-align: center;
  background: var(--primary);
}
.stat-item:nth-child(odd)  { background: var(--primary); }
.stat-item:nth-child(even) { background: var(--primary-dk); }
.stat-num   { font-size: 28px; font-weight: 900; color: #fff; letter-spacing: -.5px; }
.stat-label { font-size: 12px; color: rgba(255,255,255,.65); margin-top: 4px; }

/* ── Testimonials ─────────────────────────────────────────── */
.testi-scroll {
  display: flex; gap: 12px;
  overflow-x: auto; scrollbar-width: none;
  margin: 0 -20px; padding: 0 20px 8px;
}
.testi-scroll::-webkit-scrollbar { display: none; }
.testi-card {
  flex-shrink: 0; width: 280px;
  padding: 20px; border-radius: var(--radius);
  border: 1.5px solid var(--border); background: #fff;
}
@media (min-width: 768px) { .testi-card { width: 320px; } }
.testi-stars  { color: #f59e0b; font-size: 12px; letter-spacing: 2px; margin-bottom: 10px; }
.testi-quote  { font-size: 13px; color: var(--text-2); line-height: 1.65; margin-bottom: 16px; }
.testi-author { display: flex; align-items: center; gap: 10px; }
.testi-av     { width: 34px; height: 34px; border-radius: 50%; background: var(--primary-lt); display: flex; align-items: center; justify-content: center; font-size: 16px; }
.testi-name   { font-size: 13px; font-weight: 700; color: var(--text); }
.testi-role   { font-size: 11px; color: var(--text-3); }

/* ── App download strip ───────────────────────────────────── */
.app-strip {
  background: linear-gradient(135deg, var(--primary-dk), var(--primary));
  padding: 36px 20px; text-align: center;
}
@media (min-width: 768px) { .app-strip { padding: 48px 40px; } }
.app-strip-title {
  font-size: 20px; font-weight: 900; color: #fff;
  letter-spacing: -.3px; margin-bottom: 8px;
}
@media (min-width: 768px) { .app-strip-title { font-size: 26px; } }
.app-strip-sub   { font-size: 14px; color: rgba(255,255,255,.65); margin-bottom: 24px; }
.app-strip-btns  { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.btn-app {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 22px; border-radius: 12px;
  background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2);
  color: #fff; font-size: 14px; font-weight: 600; cursor: pointer;
  transition: background .15s; min-height: 48px;
}
.btn-app:active { background: rgba(255,255,255,.22); }
.btn-app-icon  { font-size: 22px; line-height: 1; }
.btn-app-text  { text-align: left; }
.btn-app-sub   { display: block; font-size: 10px; opacity: .7; font-weight: 400; }
.btn-app-label { display: block; font-size: 14px; font-weight: 700; }

/* ── Footer ───────────────────────────────────────────────── */
.footer { background: #0f172a; padding: 40px 20px 32px; }
.footer-top {
  display: grid; gap: 32px;
  grid-template-columns: 1fr;
  margin-bottom: 32px;
}
@media (min-width: 640px) { .footer-top { grid-template-columns: 1.5fr 1fr 1fr; } }
@media (min-width: 900px) { .footer-top { grid-template-columns: 2fr 1fr 1fr 1fr; } }
.footer-brand-logo { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
.footer-brand-logo-mark {
  width: 28px; height: 28px; border-radius: 7px;
  background: var(--primary);
  display: flex; align-items: center; justify-content: center; font-size: 14px;
}
.footer-brand-name { font-size: 16px; font-weight: 800; color: #fff; }
.footer-brand-desc { font-size: 13px; color: #64748b; line-height: 1.6; max-width: 240px; }
.footer-col-title  { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #475569; margin-bottom: 14px; }
.footer-col a      { display: block; font-size: 13px; color: #64748b; margin-bottom: 9px; transition: color .15s; }
.footer-col a:hover { color: #cbd5e1; }
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,.06); padding-top: 20px;
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;
}
.footer-copy { font-size: 12px; color: #475569; }

/* ── Utility ──────────────────────────────────────────────── */
.w-full { width: 100%; }
"""

LANDING_JS = """
// Active category tab
document.querySelectorAll('.cat-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});
"""

# ── Data ──────────────────────────────────────────────────────
DESTS = [
    {"name": "Palawan",   "emoji": "🏝", "price": "from ₱2,499", "grad": "linear-gradient(160deg,#0ea5e9,#0369a1)", "hot": True},
    {"name": "Boracay",   "emoji": "🌊", "price": "from ₱1,899", "grad": "linear-gradient(160deg,#38bdf8,#0d9488)", "hot": True},
    {"name": "Siargao",   "emoji": "🏄", "price": "from ₱2,199", "grad": "linear-gradient(160deg,#14b8a6,#0ea5e9)", "hot": False},
    {"name": "Cebu",      "emoji": "🌺", "price": "from ₱899",   "grad": "linear-gradient(160deg,#0ea5e9,#1e40af)", "hot": False},
    {"name": "Davao",     "emoji": "🦅", "price": "from ₱1,199", "grad": "linear-gradient(160deg,#10b981,#15803d)", "hot": False},
    {"name": "Singapore", "emoji": "🌆", "price": "from ₱4,599", "grad": "linear-gradient(160deg,#8b5cf6,#4f46e5)", "hot": True},
    {"name": "Tokyo",     "emoji": "🗼", "price": "from ₱7,999", "grad": "linear-gradient(160deg,#f472b6,#e11d48)", "hot": False},
    {"name": "Bangkok",   "emoji": "🛕", "price": "from ₱3,299", "grad": "linear-gradient(160deg,#f97316,#9333ea)", "hot": False},
]

DEALS = [
    {"title": "Manila → Cebu",            "meta": "Cebu Pacific · 55 min", "price": "₱1,224", "unit": "/way", "badge": "🔥 Popular", "cls": "badge-hot",  "grad": "linear-gradient(135deg,#0ea5e9,#1e40af)"},
    {"title": "Henann Resort Boracay",     "meta": "5★ · Beach front",      "price": "₱5,200", "unit": "/night","badge": "🏨 Hotel",  "cls": "badge-dom",  "grad": "linear-gradient(135deg,#38bdf8,#0d9488)"},
    {"title": "Coron Palawan 4D3N",        "meta": "Tour · 4 days 3 nights", "price": "₱9,900", "unit": "/pax", "badge": "🗺 Tour",   "cls": "badge-intl", "grad": "linear-gradient(135deg,#06b6d4,#0369a1)"},
    {"title": "Manila → Singapore",        "meta": "SIA · 3h 45m",          "price": "₱6,500", "unit": "/way", "badge": "🌏 Intl",   "cls": "badge-intl", "grad": "linear-gradient(135deg,#8b5cf6,#4f46e5)"},
    {"title": "Discovery Shores Boracay",  "meta": "4★ · Beachfront",        "price": "₱4,800", "unit": "/night","badge": "🏨 Hotel",  "cls": "badge-dom",  "grad": "linear-gradient(135deg,#f59e0b,#ef4444)"},
    {"title": "El Nido Island Hopping 3D", "meta": "Tour · 3 days 2 nights", "price": "₱6,500", "unit": "/pax", "badge": "🗺 Tour",   "cls": "badge-hot",  "grad": "linear-gradient(135deg,#10b981,#0d9488)"},
]

FEATURES = [
    ("✈️", "Smart Booking Wizard",   "5-step guided flow — pick your trip, we handle the rest. No tab-switching."),
    ("💼", "My Suitcase",            "Offline-ready itineraries saved to your phone. Works without internet."),
    ("💰", "No Hidden Fees",         "Transparent markup. What you see is what you pay — always."),
    ("🗺️", "Local + International", "PH adventures to world tours. One platform, one checkout."),
    ("🛍️", "Travel Gear Shop",      "Packing cubes to noise-cancelling earbuds. Delivered to your door."),
    ("🏢", "B2B / Manning Portal",   "Group rates and custom packages for agencies and corporate clients."),
]

TESTIMONIALS = [
    ("★★★★★", "Booked Palawan for 4 in under 3 minutes. The wizard actually works — no confusion, no tabs.", "Maria Santos", "Frequent Traveler", "🌴"),
    ("★★★★★", "Used the B2B portal for our company trip. Got group hotel rates and a tour package in one go.", "Carlo Reyes", "HR Manager", "🏢"),
    ("★★★★★", "Suitcase saved us when we had zero signal at the airport. All booking details right there offline.", "Jess Lim", "Digital Nomad", "🎒"),
]


def _dest_card(d):
    return Div(
        Div(cls="dest-card-bg", style=f"background:{d['grad']};height:100%"),
        Div(cls="dest-card-overlay"),
        Div(Div(d["name"], cls="dest-name"), Div(d["price"], cls="dest-price"), cls="dest-card-body"),
        *([ Div("🔥 HOT", cls="dest-hot") ] if d["hot"] else []),
        cls="dest-card",
    )


def _deal_card(d):
    return Div(
        Div(
            Div(d["badge"], cls=f"deal-card-badge {d['cls']}"),
            cls="deal-card-img", style=f"background:{d['grad']}",
        ),
        Div(
            Div(d["title"], cls="deal-card-title"),
            Div(d["meta"],  cls="deal-card-meta"),
            Div(
                Div(Span(d["price"], cls="deal-price"), Span(d["unit"], cls="deal-price-unit")),
                A(Button("Book →", cls="btn-deal"), href="/book"),
                cls="deal-card-foot",
            ),
            cls="deal-card-body",
        ),
        cls="deal-card",
    )


def _feature_card(icon, title, desc):
    return Div(
        Div(icon, cls="feature-icon-wrap"),
        Div(
            Div(title, cls="feature-text-title"),
            Div(desc,  cls="feature-text-desc"),
        ),
        cls="feature-card",
    )


def _testi_card(stars, quote, name, role, emoji):
    return Div(
        Div(stars, cls="testi-stars"),
        P(f'"{quote}"', cls="testi-quote"),
        Div(
            Div(emoji, cls="testi-av"),
            Div(Div(name, cls="testi-name"), Div(role, cls="testi-role")),
            cls="testi-author",
        ),
        cls="testi-card",
    )


def landing_page() -> Html:
    return Html(
        Head(
            Title("Gegow — Your Digital Travel Agency"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            Meta(name="theme-color", content="#006D77"),
            Meta(name="description", content="Book flights, hotels and tours in the Philippines and beyond. No hidden fees, no agents."),
            Meta(name="mobile-web-app-capable", content="yes"),
            Meta(name="apple-mobile-web-app-capable", content="yes"),
            Meta(name="apple-mobile-web-app-status-bar-style", content="black-translucent"),
            Style(LANDING_CSS),
        ),
        Body(
            # ── Navbar ──────────────────────────────────────
            Nav(
                Div(
                    Div("✈", cls="nav-logo-mark"),
                    Span("Gegow"),
                    cls="nav-logo",
                ),
                Div(
                    A("Features",     href="#features"),
                    A("Destinations", href="#destinations"),
                    A("B2B",          href="/b2b"),
                    cls="nav-links",
                ),
                Div(
                    A(Button("Log in", cls="btn-nav-ghost"), href="/login"),
                    A(Button("Get started", cls="btn-nav-fill"), href="/"),
                    cls="nav-actions",
                ),
                cls="nav",
            ),

            # ── Hero ────────────────────────────────────────
            Div(
                Div(Div(cls="hero-tag-dot"), Span("🇵🇭 No.1 Digital Travel Agency"), cls="hero-tag"),
                H1(
                    Span("Book your next trip "),
                    Span("without the hassle.", style="background:linear-gradient(90deg,#a7f3d0,#67e8f9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text"),
                    cls="hero-title",
                ),
                P("Flights, hotels, tours and gear — all in one place. Transparent pricing, zero agent fees.", cls="hero-sub"),
                Div(
                    A(Button("Start booking ✈", cls="btn-hero-main"), href="/"),
                    A(Button("Learn more", cls="btn-hero-ghost"), href="#features"),
                    cls="hero-btns",
                ),
                Div(
                    Span("🔍", style="font-size:16px;color:#94a3b8"),
                    Input(type="text", placeholder="Where do you want to go?"),
                    A(Button("Search", cls="btn-search"), href="/book"),
                    cls="hero-search",
                ),
                cls="hero",
            ),

            # ── Category tabs ───────────────────────────────
            Div(
                Div(
                    Button("✈️  Flights", cls="cat-btn active"),
                    Button("🏨  Hotels",  cls="cat-btn"),
                    Button("🗺️  Tours",   cls="cat-btn"),
                    Button("🛍️  Gear",    cls="cat-btn"),
                    Button("🏢  B2B",     cls="cat-btn"),
                    cls="cat-scroll",
                ),
                cls="categories",
            ),

            # ── Featured deals ──────────────────────────────
            Div(
                Div(
                    Div("Today's best deals", cls="section-title"),
                    A("See all →", href="/book", cls="section-more"),
                    cls="section-hd",
                ),
                Div(*[_deal_card(d) for d in DEALS], cls="deal-row"),
                cls="section",
            ),

            # ── Destinations ────────────────────────────────
            Div(
                Div(
                    Div("Popular destinations", cls="section-title"),
                    A("View all →", href="/book", cls="section-more"),
                    cls="section-hd",
                ),
                Div(*[_dest_card(d) for d in DESTS], cls="dest-row"),
                cls="section",
                id="destinations",
            ),

            # ── Trust strip ─────────────────────────────────
            Div(
                Div(Div("⭐", cls="trust-icon"), Div(Div("4.9 / 5", cls="trust-value"), Div("Customer rating", cls="trust-label")), cls="trust-item"),
                Div(Div("📦", cls="trust-icon"), Div(Div("12,000+", cls="trust-value"),  Div("Bookings completed", cls="trust-label")), cls="trust-item"),
                Div(Div("🔒", cls="trust-icon"), Div(Div("SSL + PCI", cls="trust-value"),  Div("Secure payments", cls="trust-label")), cls="trust-item"),
                cls="trust-strip",
            ),

            # ── Features ────────────────────────────────────
            Div(
                Div(
                    Div("Why Gegow", cls="section-title"),
                    cls="section-hd",
                ),
                Div(*[_feature_card(i, t, d) for i, t, d in FEATURES], cls="feature-grid"),
                cls="section",
                id="features",
            ),

            # ── Stats ───────────────────────────────────────
            Div(
                Div(Div("12K+", cls="stat-num"),  Div("Trips booked",     cls="stat-label"), cls="stat-item"),
                Div(Div("98%",  cls="stat-num"),  Div("Happy travelers",   cls="stat-label"), cls="stat-item"),
                Div(Div("40+",  cls="stat-num"),  Div("Destinations",      cls="stat-label"), cls="stat-item"),
                Div(Div("24/7", cls="stat-num"),  Div("Support",           cls="stat-label"), cls="stat-item"),
                cls="stats-bar",
            ),

            # ── Testimonials ────────────────────────────────
            Div(
                Div(Div("What travelers say", cls="section-title"), cls="section-hd"),
                Div(*[_testi_card(*t) for t in TESTIMONIALS], cls="testi-scroll"),
                cls="section",
            ),

            # ── App strip ───────────────────────────────────
            Div(
                Div("Travel smarter, right from your phone", cls="app-strip-title"),
                P("Add Gegow to your home screen — works offline, no app store needed.", cls="app-strip-sub"),
                Div(
                    Button(
                        Span("🍎", cls="btn-app-icon"),
                        Div(Span("Download on the", cls="btn-app-sub"), Span("App Store", cls="btn-app-label"), cls="btn-app-text"),
                        cls="btn-app",
                    ),
                    Button(
                        Span("▶️", cls="btn-app-icon"),
                        Div(Span("Get it on", cls="btn-app-sub"), Span("Google Play", cls="btn-app-label"), cls="btn-app-text"),
                        cls="btn-app",
                    ),
                    cls="app-strip-btns",
                ),
                cls="app-strip",
            ),

            # ── Footer ──────────────────────────────────────
            Footer(
                Div(
                    Div(
                        Div(
                            Div("✈", cls="footer-brand-logo-mark"),
                            Span("Gegow", cls="footer-brand-name"),
                            cls="footer-brand-logo",
                        ),
                        P("Digital-in-pocket travel agency. Flights, hotels, tours and gear — from your phone.", cls="footer-brand-desc"),
                    ),
                    Div(
                        Div("Product", cls="footer-col-title"),
                        A("Explore", href="/"),
                        A("Book a Trip", href="/book"),
                        A("Gear Shop", href="/gear"),
                        A("B2B Portal", href="/b2b"),
                        cls="footer-col",
                    ),
                    Div(
                        Div("Company", cls="footer-col-title"),
                        A("About", href="#"),
                        A("Careers", href="#"),
                        A("Blog", href="#"),
                        A("Press", href="#"),
                        cls="footer-col",
                    ),
                    Div(
                        Div("Support", cls="footer-col-title"),
                        A("Help Center", href="#"),
                        A("Privacy", href="#"),
                        A("Terms", href="#"),
                        cls="footer-col",
                    ),
                    cls="footer-top",
                ),
                Div(
                    Span("🇵🇭 © 2026 Gegow Travel · All rights reserved"),
                    Span("Made with ❤️ in the Philippines"),
                    cls="footer-bottom",
                ),
                cls="footer",
            ),

            Script(LANDING_JS),
        ),
        lang="en",
    )
