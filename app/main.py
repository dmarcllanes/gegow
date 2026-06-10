"""
Gegow — Digital-in-Pocket Travel Agency
FastHTML entry point — premium UI, Airbnb/Agoda/Kayak inspired.
"""

import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fasthtml.common import (
    fast_app, serve,
    Html, Head, Body, Title, Meta, Link, Script, Style,
    Div, Main, Span, A, Button, Input, Select, Option, H2, P, H1,
)
from starlette.responses import RedirectResponse as StarletteRedirect

from app.components.navigation import app_header, bottom_nav, sidebar, NAV_CSS
from app.components.wizard import WIZARD_CSS
from app.components.suitcase import SUITCASE_CSS
from app.routes.monitoring import MONITORING_CSS
from app.routes.b2b import B2B_CSS
from app.routes import explore, booking, shop, b2b, monitoring

# ─────────────────────────────────────────────────────────────
# DESIGN SYSTEM CSS
# ─────────────────────────────────────────────────────────────

CSS = """
/* ── 1. Tokens (UI.md) ───────────────────────────────────── */
:root {
  /* — Gegow tropical island palette — */
  --gegow-primary:      #006D77;
  --gegow-accent:       #FF7043;
  --gegow-bg:           #F0FAFA;
  --gegow-gradient-btn: linear-gradient(135deg, #FF7043, #d44020);
  --gegow-glass:        rgba(255,255,255,0.85);

  /* — Core tokens — */
  --teal:      #006D77;
  --teal-dk:   #005760;
  --teal-lt:   #B2DFDB;
  --teal-xl:   #E0F2F1;
  --beige:     #F0FAFA;
  --border:    #DDD9CE;
  --border-dk: #C8C4B8;
  --text:      #0A1D20;
  --muted:     #4A7070;
  --muted-lt:  #94A3B8;
  --amber:     #FF7043;
  --amber-lt:  #FFF3E0;
  --white:     #FFFFFF;
  --sidebar:   240px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
  --shadow-sm: 0 1px 3px rgba(15,23,42,.06), 0 1px 2px rgba(15,23,42,.04);
  --shadow-md: 0 4px 12px rgba(15,23,42,.08), 0 2px 4px rgba(15,23,42,.05);
  --shadow-lg: 0 12px 32px rgba(15,23,42,.10), 0 4px 8px rgba(15,23,42,.06);
  --shadow-xl: 0 24px 56px rgba(15,23,42,.14), 0 8px 16px rgba(15,23,42,.07);
}

/* ── 2. Reset ─────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, 'Segoe UI', Roboto, Inter, system-ui, sans-serif;
  background: var(--beige);
  color: var(--text);
  min-height: 100vh;
  font-size: 15px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
a { color: inherit; text-decoration: none; }
button, input, select, textarea { font-family: inherit; }
img { display: block; max-width: 100%; }

/* ── 3. App shell ─────────────────────────────────────────── */
.app-layout { display: flex; min-height: 100vh; }
.main-area  {
  flex: 1;
  min-width: 0;
  /* floating nav height ~70px + safe area + breathing room */
  padding-bottom: calc(82px + env(safe-area-inset-bottom, 0px));
}
@media (min-width: 768px) { .main-area { padding-bottom: 40px; } }
@media (min-width: 1200px) {
  .main-area { max-width: calc(100vw - var(--sidebar, 260px)); }
}
@media (orientation: landscape) and (max-width: 767px) {
  .main-area { padding-bottom: calc(60px + env(safe-area-inset-bottom, 0px)); }
}

/* ── 4. Animations ────────────────────────────────────────── */
@keyframes aurora {
  0%   { background-position: 0%   50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0%   50%; }
}
@keyframes fadeUpIn {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes rippleExpand {
  to { transform: scale(4); opacity: 0; }
}
@keyframes shimmer {
  from { background-position: -600px 0; }
  to   { background-position:  600px 0; }
}
@keyframes pulse-dot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50%       { transform: scale(1.3); opacity: .7; }
}

.js-loaded .fade-up { opacity: 0; transform: translateY(24px); transition: opacity .55s ease, transform .55s ease; }
.js-loaded .fade-up.in-view { opacity: 1; transform: none; }
/* fallback: visible without JS */
.fade-up { opacity: 1; transform: none; }

.ripple-wave {
  position: absolute;
  border-radius: 50%;
  background: rgba(255,255,255,.35);
  transform: scale(0);
  animation: rippleExpand .6s linear forwards;
  pointer-events: none;
}

/* ── 5. Hero ──────────────────────────────────────────────── */
.hero {
  background: linear-gradient(
    to bottom,
    #0A2A4A 0%, #0E4060 15%, #1A6080 30%,
    #3D9AB8 48%, #7AC8DC 62%, #A8E0E8 72%,
    #C8EEF3 82%, #8EC8D8 92%, #4A9AB5 100%
  );
  padding: 48px 20px 0;
  overflow: hidden;
  position: relative;
}
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 75% 12%, rgba(255,245,180,.3) 0%, transparent 50%),
    radial-gradient(ellipse at 20% 80%, rgba(0,109,119,.12) 0%, transparent 55%);
  pointer-events: none;
}
@media (min-width: 768px) { .hero { padding: 64px 48px 0; } }

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255,255,255,.15);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.25);
  color: rgba(255,255,255,.9);
  font-size: 12px;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 20px;
  margin-bottom: 16px;
  animation: fadeUpIn .5s ease forwards;
}
.hero-title {
  font-size: clamp(30px, 5vw, 56px);
  font-weight: 800;
  color: #fff;
  line-height: 1.1;
  letter-spacing: -.5px;
  margin-bottom: 12px;
  animation: fadeUpIn .55s .1s ease forwards;
}
.hero-sub {
  font-size: clamp(14px, 1.6vw, 18px);
  color: rgba(255,255,255,.8);
  max-width: 480px;
  margin-bottom: 32px;
  animation: fadeUpIn .55s .2s ease forwards;
}

/* ── 6. Hero search widget (Kayak/Expedia style) ─────────── */
.search-widget {
  background: rgba(255,255,255,.12);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,.25);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  padding: 20px 20px 0;
  max-width: 820px;
  animation: fadeUpIn .6s .25s ease forwards;
  position: relative;
  z-index: 2;
}
@media (min-width: 768px) { .search-widget { padding: 24px 28px 0; } }

.htabs {
  display: flex;
  gap: 4px;
  margin-bottom: 18px;
}
.htab {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.7);
  background: transparent;
  border: none;
  cursor: pointer;
  transition: background .2s, color .2s;
}
.htab.active {
  background: rgba(255,255,255,.2);
  color: #fff;
}
.htab:hover:not(.active) { background: rgba(255,255,255,.1); color: #fff; }

.search-form {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  padding-bottom: 20px;
}
@media (min-width: 600px) {
  .search-form { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 900px) {
  .search-form { grid-template-columns: 1fr 1fr 1fr auto; align-items: end; }
}

.sf-group { display: flex; flex-direction: column; gap: 4px; }
.sf-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .8px;
  color: rgba(255,255,255,.7);
}
.sf-input, .sf-select {
  background: rgba(255,255,255,.15);
  border: 1.5px solid rgba(255,255,255,.25);
  color: #fff;
  border-radius: var(--radius-md);
  padding: 11px 14px;
  font-size: 14px;
  font-weight: 500;
  outline: none;
  transition: border-color .2s, background .2s;
  width: 100%;
}
.sf-input::placeholder { color: rgba(255,255,255,.5); }
.sf-input:focus, .sf-select:focus {
  border-color: rgba(255,255,255,.6);
  background: rgba(255,255,255,.22);
}
.sf-select option { background: #006D77; color: #fff; }

.search-submit {
  background: var(--amber);
  color: #fff;
  border: none;
  padding: 12px 28px;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  transition: background .15s, transform .1s, box-shadow .15s;
  box-shadow: 0 4px 16px rgba(255,112,67,.35);
  position: relative;
  overflow: hidden;
}
.search-submit:hover {
  background: #d44020;
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(255,112,67,.5);
}

/* ── 7. Trust bar ─────────────────────────────────────────── */
.trust-bar {
  display: flex;
  gap: 0;
  padding: 0 20px;
  background: #fff;
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
  scrollbar-width: none;
}
.trust-bar::-webkit-scrollbar { display: none; }
.trust-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 14px 16px;
  white-space: nowrap;
  font-size: 13px;
  color: var(--muted);
  border-right: 1px solid var(--border);
  flex-shrink: 0;
}
.trust-item:last-child { border-right: none; }
.trust-icon { font-size: 18px; }
.trust-num  { font-size: 15px; font-weight: 800; color: var(--text); }
@media (min-width: 768px) {
  .trust-bar { padding: 0 32px; }
  .trust-item { padding: 16px 24px; font-size: 14px; }
}

/* ── 8. Section headings ──────────────────────────────────── */
.sec-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding: 20px 16px 12px;
}
@media (min-width: 480px) { .sec-head { padding: 28px 20px 14px; } }
@media (min-width: 768px) { .sec-head { padding: 36px 32px 18px; } }
@media (min-width: 1200px){ .sec-head { padding: 40px 48px 20px; } }

.sec-head-left {}
.sec-head-title {
  font-size: clamp(18px, 2vw, 24px);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.3px;
}
.sec-head-sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: 2px;
}
.sec-head-link {
  font-size: 13px;
  font-weight: 700;
  color: var(--teal);
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 6px 14px;
  border: 1.5px solid var(--teal-lt);
  border-radius: 20px;
  background: var(--teal-xl);
  transition: background .15s;
  white-space: nowrap;
  margin-left: 12px;
}
.sec-head-link:hover { background: var(--teal-lt); }

/* ── 9. Card grid ─────────────────────────────────────────── */
.card-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
  padding: 0 14px 8px;
}
@media (min-width: 480px) { .card-row { grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); padding: 0 16px 8px; gap: 16px; } }
@media (min-width: 768px) { .card-row { padding: 0 32px 8px; gap: 18px; } }
@media (min-width: 1200px){ .card-row { padding: 0 48px 8px; gap: 20px; } }

/* ── 10. Card base ────────────────────────────────────────── */
.card {
  background: #fff;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border);
  transition: transform .22s cubic-bezier(.34,1.56,.64,1), box-shadow .22s ease;
}
.card:hover {
  transform: translateY(-5px) scale(1.01);
  box-shadow: var(--shadow-xl);
  border-color: transparent;
}

/* ── 11. Card visual header ───────────────────────────────── */
.card-visual {
  position: relative;
  height: 148px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 10px 12px 12px;
  overflow: hidden;
  background-size: cover;
  background-position: center;
}
@media (min-width: 480px) { .card-visual { height: 160px; } }
@media (min-width: 768px) { .card-visual { height: 172px; padding: 12px 14px 14px; } }
@media (min-width: 1024px){ .card-visual { height: 180px; } }

/* Badge overlaid on image — top left */
.vc-badge-img {
  position: absolute;
  top: 10px; left: 10px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px; font-weight: 700;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  letter-spacing: .2px;
  z-index: 2;
}
.vc-badge-img.badge-hot {
  background: rgba(220,38,38,.82);
  color: #fff;
  box-shadow: 0 2px 8px rgba(220,38,38,.4);
}
.vc-badge-img.badge-dom  { background: rgba(13,148,136,.8); color: #fff; }
.vc-badge-img.badge-intl { background: rgba(109,40,217,.8); color: #fff; }
.vc-route {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 1;
}
.vc-code {
  font-size: clamp(20px, 4vw, 26px);
  font-weight: 900;
  color: #fff;
  text-shadow: 0 2px 8px rgba(0,0,0,.25);
  letter-spacing: -1px;
}
.vc-line {
  flex: 1;
  border-top: 1.5px dashed rgba(255,255,255,.6);
  position: relative;
}
.vc-line::after {
  content: '✈';
  position: absolute;
  top: -10px; left: 50%;
  transform: translateX(-50%);
  font-size: 14px;
  background: transparent;
  color: rgba(255,255,255,.9);
}
.vc-cities {
  font-size: 11px;
  color: rgba(255,255,255,.8);
  position: relative;
  z-index: 1;
  margin-top: 4px;
  font-weight: 500;
}
.vc-hotel-info { position: relative; z-index: 1; }
.vc-stars   { color: #FCD34D; font-size: 14px; }
.vc-hotel-name {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  text-shadow: 0 1px 6px rgba(0,0,0,.3);
  margin-top: 2px;
  line-height: 1.3;
}
.vc-duration {
  display: inline-block;
  background: rgba(255,255,255,.2);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 20px;
  margin-bottom: 6px;
}

/* ── 12. Card body ────────────────────────────────────────── */
.card-body { padding: 12px; }
@media (min-width: 480px) { .card-body { padding: 14px; } }
@media (min-width: 768px) { .card-body { padding: 16px; } }
.card-title { font-weight: 700; font-size: 15px; color: var(--text); line-height: 1.3; }

.c-meta {
  font-size: 12px;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 4px;
  flex-wrap: wrap;
}
.c-airline { font-size: 13px; font-weight: 600; color: var(--text); }
.c-time    { font-size: 12px; color: var(--muted); }
.c-dot     { color: var(--border); margin: 0 4px; font-size: 11px; }

.c-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 12px;
  gap: 10px;
}
.from-label { display: block; font-size: 10px; color: var(--muted-lt); text-transform: uppercase; letter-spacing: .5px; }
.price-big  { display: block; font-size: clamp(16px, 3.5vw, 20px); font-weight: 800; color: var(--teal); line-height: 1.1; }
.price-unit { font-size: 11px; color: var(--muted); font-weight: 400; }
.star-row   { color: var(--amber); font-size: 13px; letter-spacing: 1px; }
.star-label { font-size: 12px; color: var(--muted); margin-left: 4px; }

/* ── 13. Deal badges ──────────────────────────────────────── */
.deal-badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  margin-bottom: 8px;
}
.badge-hot  { background: #FFF7ED; color: #C2410C; }
.badge-dom  { background: var(--teal-xl); color: var(--teal-dk); }
.badge-intl { background: var(--amber-lt); color: #92400E; }

/* ── 14. Buttons (UI.md .btn-gegow applied to all CTAs) ───── */

/* Primary Gegow button — coral gradient from UI.md */
.btn-gegow {
  background: var(--gegow-gradient-btn);
  border-radius: var(--radius-md);
  color: #fff;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(255,112,67,0.3);
  transition: transform 0.2s ease, box-shadow .2s ease;
  border: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.btn-gegow:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255,112,67,0.45);
}
.btn-gegow:active { transform: scale(0.95); }

/* btn-book and btn-primary inherit the Gegow style */
.btn-book, .btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--gegow-gradient-btn);
  color: #fff;
  border: none;
  padding: 9px 18px;
  border-radius: var(--radius-md);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  box-shadow: 0 4px 15px rgba(255,112,67,0.3);
  transition: transform .2s ease, box-shadow .2s ease;
  text-decoration: none;
  position: relative;
  overflow: hidden;
}
.btn-book:hover, .btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255,112,67,0.45);
}
.btn-book:active, .btn-primary:active { transform: scale(0.95); }

/* Search submit */
.search-submit {
  background: var(--gegow-gradient-btn) !important;
  box-shadow: 0 4px 16px rgba(255,112,67,0.4) !important;
}
.search-submit:hover {
  box-shadow: 0 8px 28px rgba(255,112,67,0.55) !important;
  transform: translateY(-2px);
}

/* B2B submit */
.btn-submit {
  background: var(--gegow-gradient-btn);
  box-shadow: 0 4px 15px rgba(255,112,67,0.3);
  transition: transform .2s ease, box-shadow .2s ease;
}
.btn-submit:hover {
  background: var(--gegow-gradient-btn);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255,112,67,0.45);
}
.btn-submit:active { transform: scale(0.95); }

.btn-outline {
  display: block; width: 100%;
  background: transparent;
  color: var(--teal);
  border: 1.5px solid var(--teal-lt);
  padding: 9px;
  border-radius: var(--radius-md);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 8px;
  text-align: center;
  transition: background .15s, border-color .15s;
}
.btn-outline:hover { background: var(--teal-xl); border-color: var(--teal); }
.btn-back, .btn-remove {
  background: transparent;
  border: 1.5px solid var(--border);
  color: var(--muted);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  cursor: pointer;
  transition: border-color .15s;
}
.btn-back:hover   { border-color: var(--border-dk); }
.btn-remove { border-color: #FCA5A5; color: #DC2626; }
.btn-remove:hover { background: #FEF2F2; }

/* ── 14b. Shared page banner (Book / Gear / B2B) ──────────── */
.page-banner {
  background: var(--beige);
  padding: 36px 24px 28px;
  text-align: center;
}
@media (min-width: 768px) { .page-banner { padding: 44px 48px 32px; } }
.page-banner-badge {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--teal-xl); border: 1px solid var(--teal-lt);
  color: var(--teal); font-size: 11px; font-weight: 700;
  padding: 4px 12px; border-radius: 20px; margin-bottom: 10px;
}
.page-banner-title {
  font-size: clamp(20px, 3vw, 30px); font-weight: 800;
  color: var(--text); margin-bottom: 5px;
}
.page-banner-sub {
  font-size: 14px; color: var(--muted); line-height: 1.6;
  max-width: 520px; margin: 0 auto;
}

/* ── 15. Shop ─────────────────────────────────────────────── */

/* ── Hero banner ── */
.shop-hero {
  background: linear-gradient(to bottom, #0A2A4A 0%, #0E4060 20%, #1A6080 42%, #3D9AB8 65%, #7AC8DC 84%, #9ED4E4 100%);
  padding: 24px 16px 22px;
  position: relative; overflow: hidden;
}
@media (min-width: 480px) { .shop-hero { padding: 32px 20px 28px; } }
@media (min-width: 768px) { .shop-hero { padding: 40px 32px 36px; } }
@media (min-width: 1200px){ .shop-hero { padding: 48px 48px 40px; } }
.shop-hero::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 50% -20%, rgba(255,255,255,.1) 0%, transparent 70%);
}
.shop-hero-inner { position: relative; z-index: 1; }
.shop-hero-badge {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2);
  color: rgba(255,255,255,.9); font-size: 11px; font-weight: 700;
  padding: 4px 12px; border-radius: 20px; margin-bottom: 10px;
  letter-spacing: .3px;
}
.shop-hero-title {
  font-size: clamp(22px, 4vw, 32px); font-weight: 900;
  color: #fff; margin-bottom: 6px; letter-spacing: -.5px;
}
.shop-hero-sub { font-size: 13px; color: rgba(255,255,255,.6); margin-bottom: 20px; }

/* ── Shop search ── */
.shop-search-row {
  display: flex; gap: 8px; max-width: 520px;
}
.shop-search-input {
  flex: 1;
  background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.2);
  color: #fff; border-radius: 12px; padding: 11px 16px;
  font-size: 14px; outline: none;
  transition: border-color .2s, background .2s;
}
.shop-search-input::placeholder { color: rgba(255,255,255,.4); }
.shop-search-input:focus {
  border-color: rgba(0,109,119,.6); background: rgba(255,255,255,.14);
}
.shop-search-btn {
  background: linear-gradient(135deg, #006D77, #004d55);
  color: #fff; border: none; border-radius: 12px;
  padding: 11px 20px; font-size: 14px; font-weight: 700; cursor: pointer;
  white-space: nowrap; transition: opacity .15s;
}
.shop-search-btn:hover { opacity: .9; }

/* ── Category tabs ── */
.category-tabs {
  display: flex; gap: 8px; padding: 12px 16px;
  overflow-x: auto; scrollbar-width: none;
  background: #fff; border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 10;
  -webkit-overflow-scrolling: touch;
}
.category-tabs::-webkit-scrollbar { display: none; }
@media (min-width: 768px) { .category-tabs { padding: 12px 28px; } }
.cat-tab {
  padding: 7px 16px; border-radius: 20px;
  font-size: 13px; font-weight: 600; white-space: nowrap;
  cursor: pointer; border: 1.5px solid var(--border);
  background: transparent; color: var(--muted);
  text-decoration: none; transition: all .15s;
}
.cat-tab.active { background: var(--teal); color: #fff; border-color: var(--teal); }
.cat-tab:hover:not(.active) { border-color: var(--teal); color: var(--teal); }

/* ── Shop body ── */
.shop-body { padding: 0 0 100px; background: var(--beige); }

/* ── Section header ── */
.shop-section-head {
  display: flex; align-items: flex-start; justify-content: space-between;
  padding: 22px 16px 10px;
}
@media (min-width: 768px) { .shop-section-head { padding: 24px 28px 12px; } }
.shop-section-left { display: flex; flex-direction: column; gap: 2px; }
.shop-section-icon { font-size: 22px; margin-bottom: 4px; }
.shop-section-title {
  font-size: 18px; font-weight: 900; color: var(--text); letter-spacing: -.3px;
}
.shop-section-sub { font-size: 12px; color: var(--muted); }
.shop-section-see-all {
  font-size: 12px; font-weight: 700; color: var(--teal);
  text-decoration: none; white-space: nowrap; margin-top: 6px;
}

/* ── Product grid ── */
.gear-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px; padding: 0 12px 4px;
}
@media (min-width: 420px) { .gear-grid { gap: 12px; } }
@media (min-width: 520px) { .gear-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 768px) { .gear-grid { padding: 0 24px 4px; gap: 14px; grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 900px) { .gear-grid { grid-template-columns: repeat(4, 1fr); } }
@media (min-width: 1024px){ .gear-grid { grid-template-columns: repeat(4, 1fr); padding: 0 28px 4px; } }
@media (min-width: 1200px){ .gear-grid { grid-template-columns: repeat(5, 1fr); } }
@media (min-width: 1440px){ .gear-grid { grid-template-columns: repeat(6, 1fr); } }

.shop-divider {
  height: 1px; background: var(--border); margin: 6px 16px 0;
}

/* ── Product card ── */
.gear-card {
  background: #fff;
  border-radius: 16px;
  border: 1.5px solid var(--border);
  overflow: hidden;
  display: flex; flex-direction: column;
  transition: box-shadow .15s, transform .15s, border-color .15s;
}
.gear-card:hover {
  box-shadow: var(--shadow-md); transform: translateY(-3px);
  border-color: var(--teal-lt);
}

/* Visual header — category tinted */
.gear-visual {
  height: 90px;
  border-radius: 14px 14px 0 0;
  display: flex; align-items: center; justify-content: center;
  position: relative;
}
@media (min-width: 480px) { .gear-visual { height: 100px; } }
@media (min-width: 768px) { .gear-visual { height: 110px; } }
.gear-emoji { font-size: clamp(36px, 5vw, 48px); line-height: 1; }

/* Category color themes */
.gv-souvenir { background: linear-gradient(135deg, rgba(249,115,22,.12), rgba(234,88,12,.06)); }
.gv-food     { background: linear-gradient(135deg, rgba(245,158,11,.14), rgba(217,119,6,.06)); }
.gv-beach    { background: linear-gradient(135deg, rgba(14,165,233,.14), rgba(3,105,161,.06)); }
.gv-clothing { background: linear-gradient(135deg, rgba(168,85,247,.13), rgba(109,40,217,.06)); }
.gv-gear     { background: linear-gradient(135deg, rgba(13,148,136,.13), rgba(15,118,110,.06)); }

/* Badge */
.gear-badge {
  position: absolute; top: 8px; right: 8px;
  font-size: 9px; font-weight: 900; letter-spacing: .6px; text-transform: uppercase;
  padding: 3px 8px; border-radius: 6px;
}
.gb-bestseller { background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
.gb-new        { background: #DCFCE7; color: #166534; border: 1px solid #BBF7D0; }
.gb-sale       { background: #FEE2E2; color: #991B1B; border: 1px solid #FECACA; }

/* Card body */
.gear-body { padding: 12px 12px 14px; flex: 1; display: flex; flex-direction: column; }
.gear-name {
  font-size: 13px; font-weight: 700; color: var(--text);
  line-height: 1.35; margin-bottom: 4px;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.gear-desc {
  font-size: 11px; color: var(--muted); line-height: 1.45; flex: 1;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  margin-bottom: 10px;
}
.gear-foot {
  display: flex; align-items: center; justify-content: space-between; gap: 6px;
  margin-top: auto;
}
.gear-price { font-size: 16px; font-weight: 900; color: var(--teal); flex-shrink: 0; }
.gear-add-btn {
  display: inline-flex; align-items: center; gap: 4px;
  background: var(--teal); color: #fff;
  border: none; border-radius: 8px;
  padding: 7px 12px; font-size: 11px; font-weight: 700;
  cursor: pointer; text-decoration: none; white-space: nowrap;
  transition: background .15s, transform .15s;
}
.gear-add-btn:hover { background: var(--teal-dk); }
.gear-add-btn.added {
  background: #16a34a;
}

/* ── Cart FAB ── */
.cart-fab {
  position: fixed;
  bottom: calc(64px + env(safe-area-inset-bottom, 0px) + 12px);
  right: 16px;
  background: var(--amber);
  color: #fff;
  border: none;
  width: 52px; height: 52px;
  border-radius: 50%;
  font-size: 22px;
  cursor: pointer;
  box-shadow: var(--shadow-xl);
  display: flex; align-items: center; justify-content: center;
  z-index: 150;
  transition: transform .2s, box-shadow .2s;
}
.cart-fab:hover { transform: scale(1.08); }
@media (min-width: 480px) { .cart-fab { right: 20px; width: 54px; height: 54px; } }
@media (min-width: 768px) { .cart-fab { bottom: 28px; right: 28px; } }
@media (orientation: landscape) and (max-width: 767px) {
  .cart-fab { bottom: calc(56px + env(safe-area-inset-bottom, 0px) + 10px); }
}
.cart-badge {
  position: absolute;
  top: -4px; right: -4px;
  background: #DC2626; color: #fff;
  border-radius: 50%;
  width: 20px; height: 20px;
  font-size: 11px; font-weight: 700;
  display: none; align-items: center; justify-content: center;
  border: 2px solid #fff;
}

/* ── Cart Drawer ── */
.cart-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,.45); z-index: 400;
  backdrop-filter: blur(3px);
}
.cart-overlay.open { display: block; }

.cart-drawer {
  position: fixed; top: 0; right: -105%; bottom: 0;
  width: min(340px, 100vw);
  background: #fff; z-index: 401;
  display: flex; flex-direction: column;
  box-shadow: -8px 0 40px rgba(0,0,0,.18);
  transition: right .3s cubic-bezier(.4,0,.2,1);
}
.cart-drawer.open { right: 0; }

.cart-drawer-head {
  display: flex; align-items: center; justify-content: space-between;
  padding: 18px 18px 16px;
  border-bottom: 1px solid var(--border);
}
.cart-drawer-title { font-size: 16px; font-weight: 800; color: var(--text); }
.cart-drawer-count { font-size: 12px; color: var(--muted); margin-top: 1px; }
.cart-close-btn {
  width: 32px; height: 32px; border-radius: 8px;
  background: transparent; border: 1.5px solid var(--border);
  color: var(--muted); font-size: 16px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all .15s;
}
.cart-close-btn:hover { background: #FEE2E2; border-color: #FECACA; color: #DC2626; }

.cart-items { flex: 1; overflow-y: auto; padding: 12px 14px; }

.cart-row {
  display: flex; align-items: center; gap: 10px;
  padding: 12px 0; border-bottom: 1px solid var(--border);
}
.cart-row:last-child { border-bottom: none; }
.cart-row-icon {
  width: 46px; height: 46px; border-radius: 12px;
  background: var(--teal-xl); display: flex; align-items: center;
  justify-content: center; font-size: 24px; flex-shrink: 0;
}
.cart-row-info { flex: 1; min-width: 0; }
.cart-row-name { font-size: 13px; font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cart-row-price { font-size: 12px; color: var(--teal); font-weight: 700; margin-top: 1px; }
.cart-qty-row { display: flex; align-items: center; gap: 6px; margin-top: 4px; }
.cart-qty-btn {
  width: 22px; height: 22px; border-radius: 6px;
  background: var(--teal-xl); border: none; font-size: 14px; font-weight: 700;
  color: var(--teal); cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: background .15s;
}
.cart-qty-btn:hover { background: var(--teal-lt); }
.cart-qty-num { font-size: 12px; font-weight: 800; min-width: 16px; text-align: center; }
.cart-rm-btn {
  background: transparent; border: none; color: var(--muted-lt);
  font-size: 14px; cursor: pointer; padding: 4px;
  transition: color .15s;
  flex-shrink: 0;
}
.cart-rm-btn:hover { color: #DC2626; }

.cart-empty {
  padding: 48px 20px; text-align: center; color: var(--muted);
}
.cart-empty-icon { font-size: 52px; margin-bottom: 14px; opacity: .4; }
.cart-empty-txt { font-size: 14px; font-weight: 600; }

.cart-footer {
  border-top: 1px solid var(--border);
  padding: 16px 18px 20px;
}
.cart-total-row {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 14px;
}
.cart-total-lbl { font-size: 13px; font-weight: 700; color: var(--muted); }
.cart-total-val { font-size: 22px; font-weight: 900; color: var(--teal); }
.cart-checkout-btn {
  display: block; width: 100%; padding: 13px;
  background: linear-gradient(135deg, var(--teal), var(--teal-dk));
  color: #fff; font-size: 15px; font-weight: 800;
  border: none; border-radius: 14px; cursor: pointer;
  box-shadow: 0 4px 16px rgba(0,109,119,.35);
  transition: opacity .15s; margin-bottom: 8px;
}
.cart-checkout-btn:hover { opacity: .9; }
.cart-continue-btn {
  display: block; width: 100%; padding: 11px;
  background: transparent; border: 1.5px solid var(--border);
  color: var(--muted); font-size: 13px; font-weight: 700;
  border-radius: 12px; cursor: pointer;
  transition: border-color .15s, color .15s;
}
.cart-continue-btn:hover { border-color: var(--teal); color: var(--teal); }

/* ── 16. B2B portal ───────────────────────────────────────── */
.b2b-banner {
  background: var(--beige);
  padding: 36px 20px 28px;
  text-align: center;
}
@media (min-width: 768px) { .b2b-banner { padding: 44px 48px 32px; } }
.b2b-banner-title { font-size: clamp(20px,3vw,30px); font-weight: 800; color: var(--text); margin-bottom: 6px; }
.b2b-banner-sub   { font-size: 14px; color: var(--muted); line-height: 1.6; max-width: 520px; margin: 0 auto; }
.b2b-banner-badge {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--teal-xl); border: 1px solid var(--teal-lt);
  color: var(--teal); font-size: 11px; font-weight: 700;
  padding: 4px 12px; border-radius: 20px; margin-bottom: 10px;
}

.b2b-tabs {
  display: flex;
  background: #fff;
  border-bottom: 2px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 10;
}
.b2b-tab {
  flex: 1;
  padding: 15px 10px;
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: var(--muted);
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: color .15s;
}
.b2b-tab.active { color: var(--teal); border-bottom-color: var(--teal); }

.b2b-layout {
  display: grid;
  grid-template-columns: 1fr;
}
@media (min-width: 900px) {
  .b2b-layout { grid-template-columns: 1fr 1fr; align-items: start; }
}

.b2b-benefits  { padding: 32px 24px; background: var(--teal-xl); }
.b2b-form-wrap { padding: 32px 24px; }
@media (min-width: 768px) {
  .b2b-benefits  { padding: 40px 36px; }
  .b2b-form-wrap { padding: 40px 36px; }
}

.b2b-section-title { font-size: 16px; font-weight: 800; color: var(--text); margin-bottom: 18px; }
.form-group { margin-bottom: 16px; }
.form-label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .5px;
  color: var(--muted);
  margin-bottom: 6px;
}
.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: 11px 14px;
  border: 1.5px solid var(--border);
  border-radius: var(--radius-md);
  font-size: 14px;
  background: #fff;
  color: var(--text);
  outline: none;
  transition: border-color .15s, box-shadow .15s;
}
.form-input:focus, .form-select:focus, .form-textarea:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px var(--teal-lt);
}
.form-textarea { resize: vertical; min-height: 88px; }
.btn-submit {
  width: 100%;
  background: var(--teal);
  color: #fff;
  border: none;
  padding: 14px;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  margin-top: 8px;
  transition: background .15s, transform .1s;
  position: relative;
  overflow: hidden;
}
.btn-submit:hover { background: var(--teal-dk); transform: translateY(-1px); }

.benefit-card {
  background: #fff;
  border: 1px solid var(--teal-lt);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  margin-bottom: 12px;
  transition: box-shadow .15s, transform .15s;
}
.benefit-card:hover { box-shadow: var(--shadow-md); transform: translateX(3px); }
.benefit-title { font-weight: 700; font-size: 14px; color: var(--teal-dk); margin-bottom: 4px; }
.benefit-desc  { font-size: 13px; color: var(--muted); }

.success-banner { text-align: center; padding: 60px 28px; }
.success-icon   { font-size: 72px; margin-bottom: 16px; }

/* ── 17. Wizard ───────────────────────────────────────────── */
.wizard-page { max-width: 540px; margin: 0 auto; padding: 12px 0 32px; }

/* ── UI.md explicit classes ───────────────────────────────── */

/* Glass nav (UI.md) — applied to bottom nav */
.glass-nav {
  background: var(--gegow-glass);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255,255,255,0.3);
}

/* Card gradient overlay (UI.md) */
.card-gradient-overlay {
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 100%);
}

/* Wizard step transition (UI.md) */
.wizard-step {
  transition: opacity 0.3s ease-in-out;
}
#wizard-content > * {
  transition: opacity 0.3s ease-in-out;
}

/* ── 18. Suitcase ─────────────────────────────────────────── */
.suitcase-empty { text-align: center; padding: 80px 28px; }
.empty-icon  { font-size: 80px; margin-bottom: 16px; }
.empty-title { font-size: 22px; font-weight: 800; color: var(--text); margin-bottom: 8px; }

#suitcase-list { padding: 8px 20px 32px; }
@media (min-width: 768px) {
  #suitcase-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    padding: 16px 32px 40px;
    align-items: start;
  }
}

.itinerary-card {
  background: #fff;
  border-radius: var(--radius-lg);
  padding: 18px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border);
  transition: box-shadow .2s, transform .2s;
}
.itinerary-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
@media (min-width: 768px) { .itinerary-card { margin-bottom: 0; } }

.itin-type-badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  background: var(--teal-lt);
  color: var(--teal-dk);
  margin-bottom: 10px;
}
.itin-title  { font-size: 16px; font-weight: 700; margin-bottom: 6px; }
.itin-meta   { font-size: 13px; color: var(--muted); margin-bottom: 8px; line-height: 1.6; }
.itin-price  { font-size: 22px; font-weight: 800; color: var(--teal); }
.itin-ref    { font-size: 11px; color: var(--muted-lt); margin-top: 3px; }
.itin-actions{ display: flex; gap: 8px; margin-top: 14px; }
.btn-view    {
  flex: 1;
  background: var(--teal-xl);
  border: 1.5px solid var(--teal-lt);
  color: var(--teal);
  padding: 8px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  cursor: pointer;
  font-weight: 600;
  text-align: center;
  transition: background .15s;
}
.btn-view:hover { background: var(--teal-lt); }

/* ── 19. Search banner (hero) ─────────────────────────────── */
.dash-search-banner {
  background: linear-gradient(
    to bottom,
    #0A2A4A 0%, #0E4060 20%, #1A6080 42%,
    #3D9AB8 65%, #7AC8DC 84%, #9ED4E4 100%
  );
  padding: 28px 16px 36px;
  position: relative; overflow: hidden;
}
@media (min-width: 480px) { .dash-search-banner { padding: 36px 20px 42px; } }
@media (min-width: 768px) { .dash-search-banner { padding: 48px 32px 48px; } }
@media (min-width: 1200px){ .dash-search-banner { padding: 56px 48px 52px; } }
/* curved bottom edge into page */
.dash-search-banner::after {
  content: '';
  position: absolute; bottom: -1px; left: 0; right: 0;
  height: 28px; background: var(--beige);
  border-radius: 20px 20px 0 0;
  pointer-events: none; z-index: 6;
}
/* sun glow */
.dsb-sun {
  position: absolute; top: -20px; right: 8%; width: 260px; height: 260px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,245,180,.45) 0%, rgba(200,235,255,.18) 50%, transparent 72%);
  filter: blur(55px); pointer-events: none; z-index: 0;
}
/* island silhouettes */
.dsb-sil-far {
  position: absolute; bottom: 0; left: 0; right: 0; height: 42%;
  z-index: 1; pointer-events: none;
  background: linear-gradient(to bottom, rgba(20,80,120,.18), rgba(10,50,90,.4));
  clip-path: polygon(
    0% 100%,0% 44%,4% 34%,9% 41%,14% 25%,20% 33%,26% 17%,32% 27%,
    38% 12%,44% 22%,51% 8%,57% 18%,63% 5%,69% 14%,75% 9%,82% 18%,
    88% 4%,94% 13%,100% 8%,100% 100%
  );
}
.dsb-sil-mid {
  position: absolute; bottom: 0; left: 0; right: 0; height: 33%;
  z-index: 2; pointer-events: none;
  background: linear-gradient(to bottom, rgba(10,55,88,.44), rgba(5,32,62,.74));
  clip-path: polygon(
    0% 100%,0% 56%,4% 46%,9% 53%,14% 38%,20% 47%,26% 31%,32% 41%,
    38% 25%,44% 35%,50% 20%,56% 30%,62% 15%,68% 25%,74% 19%,80% 29%,
    86% 23%,92% 31%,97% 25%,100% 28%,100% 100%
  );
}
.dsb-sil-near {
  position: absolute; bottom: 0; left: 0; right: 0; height: 24%;
  z-index: 3; pointer-events: none;
  background: linear-gradient(to bottom, rgba(4,18,38,.82), rgba(2,10,22,.96));
  clip-path: polygon(
    0% 100%,0% 68%,3% 57%,7% 66%,11% 49%,16% 59%,21% 43%,27% 55%,
    33% 38%,39% 50%,45% 34%,51% 46%,57% 32%,63% 44%,69% 36%,75% 48%,
    81% 40%,87% 50%,93% 43%,100% 48%,100% 100%
  );
}
.dsb-sil-ocean {
  position: absolute; bottom: 0; left: 0; right: 0; height: 13%;
  z-index: 4; pointer-events: none;
  background: linear-gradient(to bottom, rgba(20,130,175,.78), rgba(8,88,130,.96));
}
.dsb-sil-ocean::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent 5%, rgba(255,255,220,.35) 28%, rgba(255,255,255,.65) 50%, rgba(255,255,220,.35) 72%, transparent 95%);
  animation: waterShimmer 4s ease-in-out infinite;
}
.dsb-palm-l {
  position: absolute; bottom: 12%; left: -1%; width: 13%; max-width: 160px; height: 55%;
  z-index: 5; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size: contain; background-repeat: no-repeat; background-position: bottom left;
}
.dsb-palm-r {
  position: absolute; bottom: 10%; right: -1%; width: 10%; max-width: 130px; height: 46%;
  z-index: 5; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size: contain; background-repeat: no-repeat; background-position: bottom right;
  transform: scaleX(-1);
}
@keyframes waterShimmer {
  0%,100%{opacity:.5;transform:scaleX(.85)}
  50%{opacity:1;transform:scaleX(1.08)}
}
.dsb-inner {
  max-width: 620px; margin: 0 auto;
  width: 100%; position: relative; z-index: 7;
}

/* headline */
.dsb-heading {
  font-size: clamp(20px, 4vw, 30px);
  font-weight: 900; color: #fff;
  letter-spacing: -.5px; line-height: 1.2;
  margin-bottom: 5px;
}
.dsb-sub {
  font-size: 13px; color: rgba(255,255,255,.72);
  margin-bottom: 18px;
}
@media (min-width: 480px) { .dsb-sub { font-size: 14px; margin-bottom: 20px; } }

/* search row — glassmorphism pill */
.dsb-search-row {
  display: flex; gap: 0; align-items: stretch;
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255,255,255,.2);
  border-radius: 16px; overflow: hidden;
  box-shadow: 0 8px 32px rgba(0,0,0,.25);
  margin-bottom: 16px;
}
.dsb-input-wrap {
  flex: 1; position: relative;
}
.dsb-icon {
  position: absolute; left: 14px; top: 50%; transform: translateY(-50%);
  font-size: 16px; color: rgba(255,255,255,.55); pointer-events: none; line-height: 1;
}
.dsb-input {
  width: 100%; height: 52px;
  background: transparent; border: none;
  color: #fff; font-size: 14px; font-weight: 500;
  padding: 0 14px 0 44px; outline: none;
}
@media (min-width: 480px) { .dsb-input { height: 54px; font-size: 15px; } }
.dsb-input::placeholder { color: rgba(255,255,255,.42); }
.dsb-btn {
  padding: 0 18px;
  background: linear-gradient(135deg, #006D77 0%, #004d55 100%);
  border: none; border-radius: 0;
  color: #fff; font-size: 13px; font-weight: 700;
  cursor: pointer; white-space: nowrap; flex-shrink: 0;
  transition: opacity .15s, transform .15s;
  display: flex; align-items: center; gap: 6px;
}
@media (min-width: 480px) { .dsb-btn { padding: 0 22px; font-size: 14px; } }
.dsb-btn:hover { opacity: .88; }
.dsb-btn:active { transform: scale(.97); }


/* ── 19b. Unified filter bar ──────────────────────────────── */
.filter-bar {
  background: var(--beige);
  border-bottom: 1px solid var(--border);
  padding: 14px 16px 0;
}
@media (min-width: 480px) { .filter-bar { padding: 16px 20px 0; } }
@media (min-width: 768px) { .filter-bar { padding: 18px 32px 0; } }
@media (min-width: 1200px){ .filter-bar { padding: 20px 48px 0; } }

/* Main category tabs — card-pill style */
.cat-tabs {
  display: flex; gap: 8px;
  overflow-x: auto; scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 14px;
}
@media (min-width: 480px) { .cat-tabs { gap: 10px; } }
.cat-tabs::-webkit-scrollbar { display: none; }

.cat-pill {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 14px;
  font-size: 12px; font-weight: 700;
  color: var(--muted);
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 10px;
  cursor: pointer; white-space: nowrap; flex-shrink: 0;
  transition: all .18s;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}
@media (min-width: 480px) { .cat-pill { padding: 9px 16px; font-size: 13px; border-radius: 11px; } }
.cat-pill:hover {
  border-color: var(--teal); color: var(--teal); background: var(--teal-xl);
}
.cat-pill.active {
  background: var(--teal); color: #fff;
  border-color: var(--teal);
  box-shadow: 0 4px 14px rgba(0,109,119,.28);
}

/* Sub-category chips */
.sub-tabs-wrap {
  background: var(--beige);
  border-bottom: 1px solid var(--border);
}
.sub-tabs {
  display: flex; gap: 8px;
  overflow-x: auto; scrollbar-width: none;
  padding: 10px 16px 12px;
  -webkit-overflow-scrolling: touch;
}
.sub-tabs::-webkit-scrollbar { display: none; }
@media (min-width: 480px) { .sub-tabs { padding: 10px 20px 12px; } }
@media (min-width: 768px) { .sub-tabs { padding: 10px 32px 12px; } }
@media (min-width: 1200px){ .sub-tabs { padding: 10px 48px 12px; } }

.dest-label {
  font-size: 10px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 1.2px; color: var(--muted-lt);
  white-space: nowrap; flex-shrink: 0;
  align-self: center; padding-right: 4px;
}
.sub-pill {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 6px 14px; border-radius: 20px; flex-shrink: 0;
  font-size: 12px; font-weight: 600;
  background: #fff;
  border: 1.5px solid var(--border);
  color: var(--muted);
  cursor: pointer; white-space: nowrap;
  transition: all .15s;
  box-shadow: 0 1px 3px rgba(0,0,0,.05);
  text-decoration: none;
}
.sub-pill:hover { border-color: var(--teal); color: var(--teal); background: var(--teal-xl); }
.sub-pill.active {
  background: var(--teal); border-color: var(--teal);
  color: #fff; font-weight: 700;
  box-shadow: 0 2px 10px rgba(0,109,119,.25);
}

/* ── Pagination bar ───────────────────────────────────────── */
.pagination-bar {
  display: flex; align-items: center; justify-content: center;
  gap: 12px; padding: 20px 16px 8px;
}
.pg-btn {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 7px 16px; border-radius: 8px;
  font-size: 13px; font-weight: 600;
  background: #fff; border: 1.5px solid var(--border);
  color: var(--teal); cursor: pointer;
  transition: all .15s;
}
.pg-btn:hover { background: var(--teal); color: #fff; border-color: var(--teal); }
.pg-btn.pg-disabled {
  color: var(--muted-lt); border-color: var(--border);
  pointer-events: none; opacity: .45; cursor: default;
}
.pg-info {
  font-size: 12px; font-weight: 600; color: var(--muted);
  min-width: 90px; text-align: center;
}

/* ── 19c. Quick links (kept for xs fallback, hidden via cat tabs) */
.quick-links { display: none; }

/* ── 20. Section header helper ────────────────────────────── */
.section-hdr { display: flex; justify-content: space-between; align-items: center; }
.section-hdr-title { font-weight: 700; font-size: 17px; color: var(--text); }
.section-hdr-link  { font-size: 13px; color: var(--teal); font-weight: 600; }

/* ── 22. Dashboard welcome banner ────────────────────────────── */
.welcome-banner {
  position: relative; overflow: hidden;
  background: linear-gradient(
    to bottom,
    #0A2A4A 0%, #0E4060 22%, #1A6080 48%,
    #3D9AB8 75%, #7AC8DC 100%
  );
  padding: 20px 16px 0;
}
@media (min-width: 480px) { .welcome-banner { padding: 28px 20px 0; } }
@media (min-width: 768px) { .welcome-banner { padding: 36px 32px 0; } }
@media (min-width: 1200px){ .welcome-banner { padding: 44px 48px 0; } }

/* sun glow orbs */
.wb-orb {
  position: absolute; border-radius: 50%; filter: blur(70px); pointer-events: none;
}
.wb-orb-1 { width: 320px; height: 320px;
  background: radial-gradient(circle, rgba(255,245,180,.32) 0%, rgba(200,235,255,.14) 50%, transparent 72%);
  top: -80px; right: -40px; }
.wb-orb-2 { width: 240px; height: 240px; background: rgba(0,109,119,.12);
  bottom: -60px; left: -40px; }

/* grid overlay */
.wb-grid {
  position: absolute; inset: 0; pointer-events: none;
  background-image:
    linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 90% 90% at 60% 30%, black 20%, transparent 100%);
}

/* top row: avatar + text + actions */
.welcome-card {
  position: relative; z-index: 1;
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 24px;
}
.welcome-avatar {
  width: 54px; height: 54px; border-radius: 50%; flex-shrink: 0;
  background: linear-gradient(135deg, #006D77, #004d55);
  border: 2.5px solid rgba(255,255,255,.3);
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; font-weight: 900; color: #fff;
  box-shadow: 0 0 20px rgba(0,109,119,.45);
}
.welcome-text { flex: 1; min-width: 0; }
.welcome-greeting {
  font-size: 11px; font-weight: 700; color: rgba(255,255,255,.5);
  text-transform: uppercase; letter-spacing: .8px; margin-bottom: 2px;
}
.welcome-name { font-size: clamp(16px, 4vw, 20px); font-weight: 900; color: #fff; letter-spacing: -.3px; line-height: 1.2; }
.welcome-sub  { font-size: 12px; color: rgba(255,255,255,.5); margin-top: 3px; }
.welcome-actions { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.btn-profile {
  width: 36px; height: 36px; border-radius: 10px;
  background: rgba(255,255,255,.1); border: 1.5px solid rgba(255,255,255,.18);
  color: #fff; font-size: 16px; text-decoration: none;
  display: flex; align-items: center; justify-content: center;
  transition: background .15s;
}
.btn-profile:hover { background: rgba(255,255,255,.2); }
.btn-logout {
  display: flex; align-items: center; gap: 6px;
  padding: 8px 14px; border-radius: 10px;
  background: rgba(239,68,68,.15); border: 1.5px solid rgba(239,68,68,.3);
  color: #fca5a5; font-size: 12px; font-weight: 700;
  text-decoration: none; white-space: nowrap;
  transition: all .15s;
}
.btn-logout:hover { background: rgba(239,68,68,.28); color: #fff; }

/* status cards row (3 glassmorphism tiles) */
.status-strip {
  position: relative; z-index: 1;
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
  padding-bottom: 20px;
}
@media (min-width: 480px) { .status-strip { gap: 10px; padding-bottom: 24px; } }
.status-item {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 14px 8px; border-radius: 16px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.1);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  text-decoration: none; transition: background .18s, transform .18s;
  gap: 2px;
}
.status-item:hover { background: rgba(0,109,119,.14); transform: translateY(-2px); }
.status-num   { font-size: clamp(18px, 4vw, 22px); font-weight: 900; color: #A8E0E8; line-height: 1; }
.status-label { font-size: clamp(8px, 2vw, 10px); color: rgba(255,255,255,.5); font-weight: 600;
  text-transform: uppercase; letter-spacing: .4px; margin-top: 2px; }
.status-link  { font-size: clamp(8px, 2vw, 10px); color: rgba(255,255,255,.35); font-weight: 600; margin-top: 1px; }

/* curved bottom edge of banner */
.welcome-banner::after {
  content: '';
  display: block;
  height: 20px;
  background: var(--gegow-bg);
  border-radius: 20px 20px 0 0;
  margin: 0 -1px;
  position: relative; z-index: 1;
}

/* guest strip */
.guest-strip {
  position: relative; overflow: hidden;
  background: linear-gradient(135deg, #0A2A4A 0%, #1A6080 55%, #3D9AB8 100%);
  padding: 24px 20px;
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
}
@media (min-width: 768px) { .guest-strip { padding: 28px 32px; } }
.guest-text { font-size: 15px; font-weight: 700; color: #fff; }
.guest-text span { color: #A8E0E8; }
.btn-signin {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 11px 22px; border-radius: 12px;
  background: linear-gradient(135deg, #006D77, #004d55); color: #fff;
  font-size: 14px; font-weight: 800; text-decoration: none; flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(0,109,119,.45);
  transition: all .18s;
}
.btn-signin:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,109,119,.55); }

/* ── 21. Profile / User Dashboard ────────────────────────── */
.profile-page { padding: 0 0 80px; background: var(--beige); }
@media (min-width: 768px) { .profile-page { padding: 0 0 60px; } }

/* ── Hero ── */
.profile-hero {
  background: linear-gradient(
    to bottom,
    #0A2A4A 0%, #0E4060 20%, #1A6080 45%,
    #3D9AB8 72%, #7AC8DC 100%
  );
  padding: 44px 20px 56px;
  text-align: center;
  position: relative; overflow: hidden;
}
.profile-hero::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
  background-size: 48px 48px;
}
.profile-hero::after {
  content: '';
  position: absolute; bottom: -1px; left: 0; right: 0;
  height: 36px; background: var(--beige);
  border-radius: 24px 24px 0 0;
}
.profile-avatar-wrap {
  position: relative; display: inline-flex;
  margin-bottom: 14px; z-index: 1;
}
.profile-avatar {
  width: 88px; height: 88px; border-radius: 50%;
  background: linear-gradient(135deg, #006D77, #004d55);
  display: flex; align-items: center; justify-content: center;
  font-size: 34px; font-weight: 900; color: #fff;
  border: 4px solid rgba(255,255,255,.2);
  box-shadow: 0 0 0 8px rgba(0,109,119,.18), 0 8px 32px rgba(0,0,0,.28);
  position: relative; z-index: 1;
}
.profile-avatar-ring {
  position: absolute; inset: -10px; border-radius: 50%;
  border: 2px solid rgba(0,109,119,.4);
  animation: profile-ring-pulse 2.8s ease-in-out infinite;
}
@keyframes profile-ring-pulse {
  0%,100% { opacity: .5; transform: scale(1); }
  50%      { opacity: 1;  transform: scale(1.06); }
}
.profile-name  {
  position: relative; z-index: 1;
  font-size: 22px; font-weight: 900; color: #fff; letter-spacing: -.4px;
  margin-bottom: 4px;
}
.profile-email {
  position: relative; z-index: 1;
  font-size: 13px; color: rgba(255,255,255,.55); margin-bottom: 12px;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  max-width: 280px; margin-left: auto; margin-right: auto;
}
.profile-badge {
  position: relative; z-index: 1;
  display: inline-flex; align-items: center; gap: 5px;
  background: rgba(255,255,255,.15); color: #d0f2f5;
  border: 1px solid rgba(255,255,255,.28);
  font-size: 11px; font-weight: 700; padding: 5px 14px; border-radius: 20px;
  margin-bottom: 16px;
}
.profile-logout-btn {
  position: relative; z-index: 1;
  display: inline-flex; align-items: center; gap: 6px;
  padding: 9px 18px; border-radius: 12px;
  background: rgba(255,255,255,.1); border: 1.5px solid rgba(255,255,255,.2);
  color: rgba(255,255,255,.82); font-size: 13px; font-weight: 700;
  text-decoration: none; transition: all .18s;
}
.profile-logout-btn:hover {
  background: rgba(239,68,68,.3); border-color: rgba(239,68,68,.4);
  color: #fca5a5;
}

.profile-section { padding: 16px 14px 0; }
@media (min-width: 480px) { .profile-section { padding: 18px 16px 0; } }
@media (min-width: 768px) { .profile-section { padding: 22px 28px 0; } }
@media (min-width: 1200px){ .profile-section { padding: 26px 48px 0; } }
.profile-section-title {
  font-size: 12px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 1px; color: var(--muted); margin-bottom: 12px;
}

/* ── Stats row ── */
.profile-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
@media (min-width: 480px) { .profile-stats { gap: 10px; } }
@media (min-width: 768px) { .profile-stats { gap: 14px; } }
.stat-card {
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 16px; padding: 16px 10px 14px; text-align: center;
  position: relative; overflow: hidden;
  transition: transform .15s, box-shadow .15s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,109,119,.1); }
.stat-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
}
.stat-card-trips::before  { background: linear-gradient(90deg, #0D9488, #06b6d4); }
.stat-card-dest::before   { background: linear-gradient(90deg, #f59e0b, #ef4444); }
.stat-card-spent::before  { background: linear-gradient(90deg, #8b5cf6, #ec4899); }
.stat-icon  { font-size: 20px; margin-bottom: 5px; display: block; }
.stat-num   { font-size: clamp(17px, 4vw, 22px); font-weight: 900; color: var(--text); line-height: 1; }
.stat-label { font-size: clamp(8px, 2vw, 10px); color: var(--muted); margin-top: 3px; font-weight: 600; text-transform: uppercase; letter-spacing: .4px; }

/* ── Booking list ── */
.booking-list { display: flex; flex-direction: column; gap: 10px; }
.booking-item {
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 16px; padding: 14px 16px;
  display: flex; align-items: center; gap: 12px;
  position: relative; overflow: hidden;
  transition: box-shadow .15s;
}
.booking-item:hover { box-shadow: 0 4px 16px rgba(0,0,0,.07); }
.booking-item::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px;
  border-radius: 4px 0 0 4px;
}
.booking-flight::before  { background: linear-gradient(to bottom, #0D9488, #1d4ed8); }
.booking-hotel::before   { background: linear-gradient(to bottom, #f59e0b, #92400e); }
.booking-tour::before    { background: linear-gradient(to bottom, #06b6d4, #0e7490); }
.booking-default::before { background: #e2e8f0; }
.booking-icon-wrap {
  width: 42px; height: 42px; border-radius: 12px;
  background: var(--teal-xl); display: flex; align-items: center;
  justify-content: center; font-size: 22px; flex-shrink: 0;
}
.booking-info { flex: 1; min-width: 0; }
.booking-title { font-size: 14px; font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.booking-sub   { font-size: 12px; color: var(--muted); margin-top: 2px; }
.booking-badge {
  font-size: 10px; font-weight: 700; padding: 4px 10px; border-radius: 20px;
  flex-shrink: 0; text-transform: uppercase; letter-spacing: .4px;
}
.badge-confirmed { background: #d1fae5; color: #065f46; }
.badge-pending   { background: #fef3c7; color: #92400e; }
.badge-upcoming  { background: #dbeafe; color: #1e40af; }
.badge-empty     { background: #f1f5f9; color: #64748b; }

/* ── Quick actions ── */
.quick-actions { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
.qa-card {
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 18px; padding: 18px 16px;
  display: flex; flex-direction: column; align-items: flex-start; gap: 10px;
  text-decoration: none; transition: box-shadow .15s, transform .15s, border-color .15s;
}
.qa-card:hover {
  box-shadow: 0 6px 20px rgba(0,0,0,.08);
  transform: translateY(-2px); border-color: var(--teal-lt);
}
.qa-icon-bubble {
  width: 46px; height: 46px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center; font-size: 24px;
}
.qa-flight  { background: rgba(13,148,136,.12); }
.qa-hotel   { background: rgba(245,158,11,.12); }
.qa-tour    { background: rgba(6,182,212,.12); }
.qa-suitcase{ background: rgba(139,92,246,.12); }
.qa-title { font-size: 14px; font-weight: 800; color: var(--text); }
.qa-sub   { font-size: 11px; color: var(--muted); margin-top: 1px; }

/* ── Preferences ── */
.pref-list { display: flex; flex-direction: column; gap: 8px; }
.pref-item {
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 14px; padding: 13px 16px;
  display: flex; align-items: center; justify-content: space-between;
  transition: border-color .15s;
}
.pref-item:hover { border-color: var(--teal-lt); }
.pref-left  { display: flex; align-items: center; gap: 10px; font-size: 14px; color: var(--text); font-weight: 500; }
.pref-icon  { font-size: 20px; }
.pref-right { font-size: 12px; color: var(--teal); font-weight: 700; background: var(--teal-xl); padding: 3px 10px; border-radius: 8px; }

/* ── Quick-Book Strip ──────────────────────────────────────── */
.quick-book-strip {
  padding: 0 16px;
  margin: -24px 0 0;
  position: relative; z-index: 2;
}
.quick-book-strip-title {
  font-size: 11px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 1px; color: var(--muted); margin-bottom: 10px;
}
.quick-book-row {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
  margin-bottom: 10px;
}
.qb-card {
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 16px; padding: 14px 10px;
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  text-decoration: none; text-align: center;
  transition: transform .15s, box-shadow .15s, border-color .15s;
  position: relative; overflow: hidden;
}
.qb-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  border-radius: 3px 3px 0 0;
}
.qb-flight::before  { background: linear-gradient(90deg, #0D9488, #0891b2); }
.qb-hotel::before   { background: linear-gradient(90deg, #f59e0b, #ef4444); }
.qb-tour::before    { background: linear-gradient(90deg, #06b6d4, #8b5cf6); }
.qb-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); border-color: var(--teal-lt); }
.qb-icon  { font-size: 26px; line-height: 1; }
.qb-label { font-size: 12px; font-weight: 800; color: var(--text); }
.qb-sub   { font-size: 10px; color: var(--muted); }

.suitcase-shortcut {
  display: flex; align-items: center; gap: 10px;
  background: linear-gradient(135deg, rgba(0,109,119,.07), rgba(0,109,119,.03));
  border: 1.5px solid rgba(0,109,119,.15);
  border-radius: 14px; padding: 13px 16px;
  text-decoration: none;
  transition: box-shadow .15s, border-color .15s;
}
.suitcase-shortcut:hover { box-shadow: var(--shadow-sm); border-color: var(--teal-lt); }
.suitcase-sc-icon { font-size: 22px; flex-shrink: 0; }
.suitcase-sc-info { flex: 1; min-width: 0; }
.suitcase-sc-title { font-size: 14px; font-weight: 800; color: var(--teal); }
.suitcase-sc-sub   { font-size: 11px; color: var(--muted); margin-top: 1px; }
.suitcase-sc-arrow { font-size: 18px; color: var(--teal); opacity: .6; }

/* ── PWA Install nudge ─────────────────────────────────────── */
.pwa-nudge {
  margin: 0 16px;
  background: linear-gradient(135deg, #0A2A4A 0%, #1A6080 60%, #3D9AB8 100%);
  border: 1.5px solid rgba(0,109,119,.28);
  border-radius: 16px; padding: 14px 16px;
  display: flex; align-items: center; gap: 12px;
  text-decoration: none;
  transition: box-shadow .15s;
}
.pwa-nudge:hover { box-shadow: 0 4px 20px rgba(0,109,119,.25); }
.pwa-nudge-icon { font-size: 26px; flex-shrink: 0; }
.pwa-nudge-info { flex: 1; min-width: 0; }
.pwa-nudge-title { font-size: 13px; font-weight: 800; color: #fff; }
.pwa-nudge-sub   { font-size: 11px; color: rgba(255,255,255,.55); margin-top: 2px; }
.pwa-nudge-btn {
  flex-shrink: 0; padding: 8px 14px; border-radius: 10px;
  background: linear-gradient(135deg, #006D77, #004d55);
  color: #fff; font-size: 12px; font-weight: 800; border: none;
  cursor: pointer; white-space: nowrap;
}

/* ── App Splash Screen ────────────────────────────────────── */
.app-splash {
  position: fixed; inset: 0; z-index: 99999;
  background: linear-gradient(
    to bottom,
    #0A2A4A 0%, #0E4060 18%, #1A6080 38%,
    #3D9AB8 60%, #7AC8DC 80%, #A8E0E8 100%
  );
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  overflow: hidden;
  transition: opacity .5s ease, transform .5s ease;
}
.app-splash.splash-exit {
  opacity: 0; pointer-events: none; transform: scale(1.05);
}
/* Expanding ring pulses */
.splash-rings {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  pointer-events: none;
}
.splash-ring {
  position: absolute; border-radius: 50%;
  border: 1px solid rgba(255,255,255,.07);
  animation: spl-ring 3.2s ease-out infinite;
}
.splash-ring:nth-child(1) { width: 160px; height: 160px; animation-delay: 0s; }
.splash-ring:nth-child(2) { width: 310px; height: 310px; animation-delay: .65s; }
.splash-ring:nth-child(3) { width: 480px; height: 480px; animation-delay: 1.3s; }
.splash-ring:nth-child(4) { width: 680px; height: 680px; animation-delay: 1.95s; }
@keyframes spl-ring {
  0%   { transform: scale(.75); opacity: 0; }
  15%  { opacity: 1; }
  100% { transform: scale(1.25); opacity: 0; }
}
/* Brand */
.splash-brand {
  position: relative; z-index: 1;
  text-align: center; margin-bottom: 36px;
}
.splash-logo-wrap {
  width: 90px; height: 90px; border-radius: 26px;
  background: rgba(255,255,255,.13);
  backdrop-filter: blur(20px);
  border: 1.5px solid rgba(255,255,255,.22);
  display: flex; align-items: center; justify-content: center;
  font-size: 46px; margin: 0 auto 16px;
  box-shadow: 0 12px 40px rgba(0,0,0,.28);
  animation: spl-logo .7s cubic-bezier(.34,1.56,.64,1) forwards;
}
@keyframes spl-logo {
  from { transform: scale(.55) rotate(-12deg); opacity: 0; }
  to   { transform: scale(1) rotate(0);        opacity: 1; }
}
.splash-wordmark {
  font-size: 38px; font-weight: 900; color: #fff;
  letter-spacing: -.8px;
  animation: spl-up .5s .18s ease both;
}
.splash-tagline {
  font-size: 11px; color: rgba(255,255,255,.55);
  letter-spacing: 2.5px; text-transform: uppercase; margin-top: 4px;
  animation: spl-up .5s .28s ease both;
}
@keyframes spl-up {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0); }
}
/* Promo strip */
.splash-promos-wrap {
  position: relative; z-index: 1;
  width: 100%; overflow: hidden; padding-bottom: 4px;
  margin-bottom: 32px;
  animation: spl-up .5s .38s ease both;
}
.splash-promos-track {
  display: flex; gap: 12px; padding: 4px 20px;
  width: max-content;
  animation: spl-scroll 16s linear infinite;
}
@keyframes spl-scroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.spl-promo {
  flex-shrink: 0; width: 168px; border-radius: 16px; overflow: hidden;
  background: rgba(255,255,255,.09);
  border: 1px solid rgba(255,255,255,.14);
  cursor: pointer;
  transition: transform .2s;
}
.spl-promo:hover { transform: translateY(-3px); }
.spl-promo-img {
  height: 92px; background-size: cover; background-position: center;
  position: relative;
}
.spl-promo-img::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.72) 0%, transparent 60%);
}
.spl-promo-dest {
  position: absolute; bottom: 8px; left: 10px; z-index: 1;
  font-size: 13px; font-weight: 800; color: #fff;
  text-shadow: 0 1px 4px rgba(0,0,0,.5);
}
.spl-promo-body { padding: 8px 10px 10px; }
.spl-promo-badge {
  font-size: 9px; font-weight: 800; color: #FF7043;
  text-transform: uppercase; letter-spacing: .8px; margin-bottom: 3px;
}
.spl-promo-title {
  font-size: 11px; font-weight: 700; color: rgba(255,255,255,.85);
  line-height: 1.35; margin-bottom: 5px;
}
.spl-promo-price {
  font-size: 16px; font-weight: 900;
  color: #A8E0E8;
}
.spl-promo-unit { font-size: 10px; color: rgba(255,255,255,.45); }
/* Loading dots */
.splash-dots {
  position: relative; z-index: 1; display: flex; gap: 8px;
  animation: spl-up .4s .5s ease both;
}
.spl-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: rgba(255,255,255,.35);
  animation: spl-dot 1.3s ease infinite;
}
.spl-dot:nth-child(2) { animation-delay: .22s; }
.spl-dot:nth-child(3) { animation-delay: .44s; }
@keyframes spl-dot {
  0%, 100% { background: rgba(255,255,255,.25); transform: scale(1); }
  50%       { background: #fff; transform: scale(1.4); }
}
/* Tap hint */
.splash-tap-hint {
  position: absolute; bottom: 32px; z-index: 1;
  font-size: 11px; color: rgba(255,255,255,.3);
  letter-spacing: 1px;
  animation: spl-up .4s .7s ease both;
}

/* ── Quick-Book Modal ─────────────────────────────────────── */
.qb-modal-overlay {
  position: fixed; inset: 0; z-index: 9000;
  background: rgba(0,0,0,.55);
  backdrop-filter: blur(3px);
  display: flex; align-items: flex-end;
}
.qb-modal-sheet {
  width: 100%; max-width: 540px;
  margin: 0 auto;
  background: #fff;
  border-radius: 28px 28px 0 0;
  padding: 12px 20px 32px;
  transform: translateY(100%);
  transition: transform .32s cubic-bezier(.32,0,.4,1);
  max-height: 92dvh;
  overflow-y: auto;
}
.qb-modal-sheet.open { transform: translateY(0); }
.qb-handle {
  width: 40px; height: 5px; border-radius: 3px;
  background: var(--border); margin: 0 auto 16px;
}
.qb-header {
  display: flex; align-items: flex-start;
  justify-content: space-between; gap: 12px;
  margin-bottom: 14px;
}
.qb-header-left { display: flex; align-items: center; gap: 12px; flex: 1; min-width: 0; }
.qb-icon { font-size: 32px; flex-shrink: 0; }
.qb-header-text { flex: 1; min-width: 0; }
.qb-name {
  font-size: 16px; font-weight: 800; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.qb-detail { font-size: 12px; color: var(--muted); margin-top: 2px; }
.qb-close {
  width: 32px; height: 32px; border-radius: 50%;
  border: 1.5px solid var(--border); background: transparent;
  color: var(--muted); font-size: 14px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  transition: background .15s, color .15s;
}
.qb-close:hover { background: var(--beige); color: var(--text); }
.qb-divider { height: 1px; background: var(--border); margin: 0 0 14px; }
.qb-price-strip {
  display: flex; justify-content: space-between; align-items: center;
  background: var(--beige); border-radius: 12px;
  padding: 10px 14px; margin-bottom: 16px;
  border: 1px solid var(--border);
}
.qb-price-label { font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .8px; color: var(--muted); }
.qb-price-value { font-size: 15px; font-weight: 900; color: var(--teal); }
.qb-field { margin-bottom: 14px; }
.qb-field-label {
  display: block; font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .8px;
  color: var(--muted); margin-bottom: 6px;
}
.qb-field-input {
  width: 100%; padding: 13px 14px;
  border: 1.5px solid var(--border); border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none;
  transition: border-color .18s, box-shadow .18s;
}
.qb-field-input:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}
.qb-pax-row {
  display: flex; align-items: center; gap: 18px;
  background: var(--beige); border-radius: 12px;
  padding: 10px 14px; border: 1.5px solid var(--border);
}
.qb-pax-btn {
  width: 38px; height: 38px; border-radius: 50%;
  border: 2px solid var(--teal); background: #fff; color: var(--teal);
  font-size: 22px; font-weight: 700; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background .15s, color .15s;
}
.qb-pax-btn:hover { background: var(--teal); color: #fff; }
.qb-pax-count {
  flex: 1; text-align: center;
  font-size: 24px; font-weight: 900; color: var(--text);
}
.qb-total-strip {
  display: flex; justify-content: space-between; align-items: center;
  background: linear-gradient(135deg, var(--teal-xl) 0%, #E8F7F5 100%);
  border: 1.5px solid var(--teal-lt); border-radius: 14px;
  padding: 12px 16px; margin-bottom: 18px;
}
.qb-total-label { font-size: 12px; font-weight: 700; color: var(--teal-dk); }
.qb-total-value { font-size: 20px; font-weight: 900; color: var(--teal); }
.qb-confirm-btn {
  display: block; width: 100%; padding: 15px;
  background: linear-gradient(135deg, var(--teal) 0%, var(--teal-dk) 100%);
  border: none; border-radius: 14px;
  color: #fff; font-size: 16px; font-weight: 700;
  cursor: pointer; text-align: center;
  box-shadow: 0 6px 20px rgba(0,109,119,.25);
  transition: transform .15s, box-shadow .15s;
}
.qb-confirm-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(0,109,119,.35);
}
/* Success view */
.qb-success-icon { font-size: 56px; text-align: center; margin: 16px 0 12px; }
.qb-success-title {
  font-size: 22px; font-weight: 900; color: var(--text);
  text-align: center; margin-bottom: 6px;
}
.qb-success-sub { font-size: 13px; color: var(--muted); text-align: center; margin-bottom: 12px; }
.qb-success-ref {
  font-size: 12px; font-weight: 800; color: var(--teal);
  text-align: center; letter-spacing: 1px;
  background: var(--teal-xl); border: 1px solid var(--teal-lt);
  border-radius: 10px; padding: 8px 16px; margin: 0 auto 20px;
  display: inline-block; width: 100%; box-sizing: border-box;
}
.qb-success-actions { display: flex; flex-direction: column; gap: 10px; }
.qb-suitcase-btn {
  display: block; width: 100%; padding: 14px;
  background: linear-gradient(135deg, var(--teal) 0%, var(--teal-dk) 100%);
  border: none; border-radius: 14px; color: #fff;
  font-size: 15px; font-weight: 700; cursor: pointer;
  transition: transform .15s;
}
.qb-suitcase-btn:hover { transform: translateY(-2px); }
.qb-again-btn {
  display: block; width: 100%; padding: 12px;
  background: transparent; border: 1.5px solid var(--border);
  border-radius: 14px; color: var(--muted);
  font-size: 14px; font-weight: 600; cursor: pointer;
  transition: border-color .15s, color .15s;
}
.qb-again-btn:hover { border-color: var(--text); color: var(--text); }
@media (min-width: 540px) {
  .qb-modal-overlay { align-items: center; }
  .qb-modal-sheet {
    border-radius: 28px; max-height: 85vh;
    margin-bottom: 0;
  }
}
"""

COMBINED_CSS = CSS + "\n" + NAV_CSS + "\n" + WIZARD_CSS + "\n" + SUITCASE_CSS + "\n" + MONITORING_CSS + "\n" + B2B_CSS

# ─────────────────────────────────────────────────────────────
# PWA headers
# ─────────────────────────────────────────────────────────────

PWA_HEADERS = (
    Meta(charset="utf-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
    # Theme
    Meta(name="theme-color", content="#006D77"),
    Meta(name="msapplication-TileColor", content="#006D77"),
    # Apple PWA
    Meta(name="apple-mobile-web-app-capable", content="yes"),
    Meta(name="apple-mobile-web-app-status-bar-style", content="black-translucent"),
    Meta(name="apple-mobile-web-app-title", content="Gegow"),
    # Apple touch icon (iOS "Add to Home Screen")
    Link(rel="apple-touch-icon", href="/static/icons/icon-192.png"),
    Link(rel="apple-touch-icon", sizes="192x192", href="/static/icons/icon-192.png"),
    Link(rel="apple-touch-icon", sizes="512x512", href="/static/icons/icon-512.png"),
    # Favicon fallback
    Link(rel="icon", type="image/png", sizes="192x192", href="/static/icons/icon-192.png"),
    Link(rel="icon", type="image/png", sizes="512x512", href="/static/icons/icon-512.png"),
    # Manifest
    Link(rel="manifest", href="/static/manifest.json"),
    Style(COMBINED_CSS),
    Script(src="/static/sw-register.js", defer=True),
    Script(src="/static/app.js", defer=True),
)

from starlette.staticfiles import StaticFiles

_STATIC_DIR = Path(__file__).parent.parent / "static"


def _safe(s) -> str:
    """Strip lone Unicode surrogates (U+D800–U+DFFF) that crash UTF-8 encoding.

    Python's json.loads() can produce strings containing lone surrogates when
    the source JSON has malformed \\uXXXX escape sequences (e.g. from Supabase
    user-metadata).  Starlette's HTMLResponse then raises UnicodeEncodeError
    when trying to encode the page as UTF-8.  This helper replaces any such
    characters with the Unicode replacement character (U+FFFD) so the page
    always renders safely.
    """
    if not isinstance(s, str):
        return str(s) if s is not None else ""
    return s.encode("utf-8", errors="replace").decode("utf-8")
import traceback as _tb
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import HTMLResponse as _HTMLResponse

class _ErrorLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            stack = _tb.format_exc()
            # In prod: persist stack to Supabase error_logs table or file
            print(f"[Gegow ERROR] {exc}\n{stack}")
            return _HTMLResponse(
                "<html><body style='font-family:sans-serif;padding:40px'>"
                "<h2>Under Maintenance</h2>"
                "<p>We're fixing a minor issue. Please try again soon.</p>"
                "</body></html>",
                status_code=500,
            )

app, rt = fast_app(hdrs=PWA_HEADERS, live=False)
app.add_middleware(_ErrorLoggerMiddleware)
app.mount("/static", StaticFiles(directory=str(_STATIC_DIR)), name="static")

from starlette.responses import FileResponse
@app.route("/sw.js")
async def service_worker(request):
    return FileResponse(str(_STATIC_DIR / "sw.js"), media_type="application/javascript", headers={"Service-Worker-Allowed": "/"})

@app.route("/favicon.ico")
async def favicon(request):
    return FileResponse(str(_STATIC_DIR / "favicon.ico"), media_type="image/x-icon")

# ─────────────────────────────────────────────────────────────
# Page shell
# ─────────────────────────────────────────────────────────────

_UNS = "https://images.unsplash.com/photo-"
_SPLASH_PROMOS = [
    {"dest": "Boracay",   "badge": "🔥 PROMO",    "title": "Boracay 3D2N Package", "price": "₱4,500", "unit": "/ person", "img": _UNS + "1507525428034-b723cf961d3e?w=360&q=75&fit=crop"},
    {"dest": "Singapore", "badge": "✈️ FLIGHTS",  "title": "Manila → Singapore",   "price": "₱7,800", "unit": "/ way",    "img": _UNS + "1565967511849-76a60a516170?w=360&q=75&fit=crop"},
    {"dest": "Siargao",   "badge": "🌊 SURF DEAL", "title": "Siargao Surf 5D4N",   "price": "₱9,500", "unit": "/ person", "img": _UNS + "1455218873509-8097305ee378?w=360&q=75&fit=crop"},
    {"dest": "Tokyo",     "badge": "🌸 LIMITED",   "title": "Tokyo Explorer 7D6N", "price": "₱28,000","unit": "/ person", "img": _UNS + "1540959733332-eab4deabeeaf?w=360&q=75&fit=crop"},
    {"dest": "Cebu",      "badge": "💸 CHEAP",     "title": "Manila → Cebu Flight", "price": "₱1,299", "unit": "/ way",   "img": _UNS + "1559128010-7c1ad6e1b6a5?w=360&q=75&fit=crop"},
    {"dest": "Palawan",   "badge": "🏝️ PARADISE",  "title": "El Nido Discovery 4D3N","price": "₱12,500","unit": "/ person","img": _UNS + "1501854140801-50d01698950b?w=360&q=75&fit=crop"},
]

def _splash_promo_card(p: dict) -> Div:
    return Div(
        Div(
            Span(p["dest"], cls="spl-promo-dest"),
            cls="spl-promo-img",
            style=f"background-image:url('{p['img']}')",
        ),
        Div(
            Div(p["badge"], cls="spl-promo-badge"),
            Div(p["title"], cls="spl-promo-title"),
            Div(
                Span(p["price"], cls="spl-promo-price"),
                Span(" " + p["unit"], cls="spl-promo-unit"),
            ),
            cls="spl-promo-body",
        ),
        cls="spl-promo",
    )

def _splash_overlay() -> Div:
    cards = [_splash_promo_card(p) for p in _SPLASH_PROMOS]
    # Duplicate for seamless infinite scroll
    cards_dup = [_splash_promo_card(p) for p in _SPLASH_PROMOS]
    return Div(
        # Expanding rings
        Div(
            Div(cls="splash-ring"),
            Div(cls="splash-ring"),
            Div(cls="splash-ring"),
            Div(cls="splash-ring"),
            cls="splash-rings",
        ),
        # Brand
        Div(
            Div("✈️", cls="splash-logo-wrap"),
            Div("Gegow", cls="splash-wordmark"),
            Div("Your Digital Travel Agency", cls="splash-tagline"),
            cls="splash-brand",
        ),
        # Promo strip
        Div(
            Div(*cards, *cards_dup, cls="splash-promos-track"),
            cls="splash-promos-wrap",
        ),
        # Loading dots
        Div(
            Div(cls="spl-dot"),
            Div(cls="spl-dot"),
            Div(cls="spl-dot"),
            cls="splash-dots",
        ),
        Div("Tap to skip", cls="splash-tap-hint"),
        id="app-splash", cls="app-splash",
    )


def page_shell(content, active: str = "/", title: str = "Gegow") -> Html:
    return Html(
        Head(Title(f"{title} · Gegow Travel"), *PWA_HEADERS),
        Body(
            _splash_overlay(),
            Div(
                sidebar(active=active),
                Div(
                    app_header(),
                    Main(content),
                    cls="main-area",
                ),
                cls="app-layout",
            ),
            bottom_nav(active=active),
        ),
    )

# ─────────────────────────────────────────────────────────────
# Hero search widget helpers
# ─────────────────────────────────────────────────────────────

def _flight_form(origins: list[str]) -> Div:
    opts = [Option(o, value=o) for o in origins]
    return Div(
        Div(
            Span("From", cls="sf-label"),
            Select(*opts, name="origin", cls="sf-select"),
            cls="sf-group",
        ),
        Div(
            Span("To (IATA)", cls="sf-label"),
            Input(type="text", name="destination", placeholder="e.g. CEB, SIN, NRT",
                  cls="sf-input", maxlength="3"),
            cls="sf-group",
        ),
        Div(
            Span("Departure", cls="sf-label"),
            Input(type="date", name="date_from", cls="sf-input"),
            cls="sf-group",
        ),
        Button("Search Flights 🔍", type="submit", cls="search-submit",
               formaction="/book", formmethod="get",
               onclick=f"this.form.trip_type.value='flight'"),
        cls="search-form",
    )


def _hotel_form(cities: list[str]) -> Div:
    opts = [Option(c, value=c) for c in cities]
    return Div(
        Div(
            Span("Destination", cls="sf-label"),
            Select(*opts, name="city", cls="sf-select"),
            cls="sf-group",
        ),
        Div(
            Span("Check-in", cls="sf-label"),
            Input(type="date", name="date_from", cls="sf-input"),
            cls="sf-group",
        ),
        Div(
            Span("Check-out", cls="sf-label"),
            Input(type="date", name="date_to", cls="sf-input"),
            cls="sf-group",
        ),
        Button("Search Hotels 🔍", type="submit", cls="search-submit",
               onclick="this.form.trip_type.value='hotel'"),
        cls="search-form",
    )


def _tour_form() -> Div:
    return Div(
        Div(
            Span("Destination", cls="sf-label"),
            Input(type="text", name="tour_dest", placeholder="e.g. Palawan, Tokyo...", cls="sf-input"),
            cls="sf-group",
        ),
        Div(
            Span("Type", cls="sf-label"),
            Select(
                Option("All Tours", value=""),
                Option("Local / Domestic", value="domestic"),
                Option("International", value="international"),
                name="tour_type", cls="sf-select",
            ),
            cls="sf-group",
        ),
        Div(
            Span("Travel Date", cls="sf-label"),
            Input(type="date", name="date_from", cls="sf-input"),
            cls="sf-group",
        ),
        Button("Search Tours 🔍", type="submit", cls="search-submit",
               onclick="this.form.trip_type.value='tour'"),
        cls="search-form",
    )


def _hero_widget() -> Div:
    from app.logic.polars_engine import get_all_origins, get_hotel_cities
    origins = get_all_origins()
    cities  = get_hotel_cities()

    return Div(
        # Tabs
        Div(
            Button("✈️ Flights", cls="htab active", data_type="flight",
                   hx_get="/hero-form/flight", hx_target="#hero-fields",
                   hx_swap="innerHTML",
                   onclick="switchHeroTab('flight')"),
            Button("🏨 Hotels", cls="htab", data_type="hotel",
                   hx_get="/hero-form/hotel", hx_target="#hero-fields",
                   hx_swap="innerHTML",
                   onclick="switchHeroTab('hotel')"),
            Button("🗺️ Tours", cls="htab", data_type="tour",
                   hx_get="/hero-form/tour", hx_target="#hero-fields",
                   hx_swap="innerHTML",
                   onclick="switchHeroTab('tour')"),
            cls="htabs",
        ),
        # Form with a hidden trip_type we set before submit
        Div(
            Input(type="hidden", name="trip_type", value="flight"),
            Div(_flight_form(origins), id="hero-fields"),
            action="/book", method="get",
            cls="",
            # FastHTML doesn't have a Form with custom attrs easily, use the Div approach
        ),
        cls="search-widget",
    )


# ─────────────────────────────────────────────────────────────
# Register sub-routes
# ─────────────────────────────────────────────────────────────

explore.setup(rt)
booking.setup(rt)
shop.setup(rt)
b2b.setup(rt)
monitoring.setup(rt, page_shell)


# Hero form tab endpoints
@rt('/hero-form/flight')
def get():
    from app.logic.polars_engine import get_all_origins
    return _flight_form(get_all_origins())

@rt('/hero-form/hotel')
def get():
    from app.logic.polars_engine import get_hotel_cities
    return _hotel_form(get_hotel_cities())

@rt('/hero-form/tour')
def get():
    return _tour_form()


# ─────────────────────────────────────────────────────────────
# Pages
# ─────────────────────────────────────────────────────────────

def sec_head(title: str, subtitle: str = "", href: str = "") -> Div:
    left = Div(
        Div(title, cls="sec-head-title"),
        Div(subtitle, cls="sec-head-sub") if subtitle else Span(),
        cls="sec-head-left",
    )
    link = A("See all →", href=href, cls="sec-head-link") if href else Span()
    return Div(left, link, cls="sec-head")


@rt('/dashboard')
def get(request):
    from app.logic.polars_engine import get_flights_page, get_hotels_page, get_tours_page
    from app.components.cards import flight_card, hotel_card, tour_card
    from app.routes.explore import _pagination_bar

    def _section_content(section, result, card_fn):
        cards = [card_fn(item) for item in result["items"]]
        return Div(
            Div(*cards, cls="card-row stagger") if cards else Div(),
            _pagination_bar(section, result["page"], result["pages"], "all", result["total"]),
            id=f"{section}-content",
        )

    fp = get_flights_page(page=1)
    hp = get_hotels_page(page=1)
    tp = get_tours_page(page=1)

    search_banner = Div(
        # Sky & atmosphere
        Div(cls="dsb-sun"),
        # Island silhouettes
        Div(cls="dsb-sil-far"),
        Div(cls="dsb-sil-mid"),
        Div(cls="dsb-sil-near"),
        Div(cls="dsb-sil-ocean"),
        Div(cls="dsb-palm-l"),
        Div(cls="dsb-palm-r"),
        # Content
        Div(
            Div("Where do you want to go?", cls="dsb-heading"),
            Div("Flights · Hotels · Tours — all in one place", cls="dsb-sub"),
            Div(
                Div(
                    Span("🔍", cls="dsb-icon"),
                    Input(
                        placeholder="Cebu, Boracay, Tokyo…",
                        cls="dsb-input", name="q", id="dash-search-input",
                        autocomplete="off",
                        onkeydown="if(event.key==='Enter'){var q=this.value.trim();if(q)window.location='/search?q='+encodeURIComponent(q);}",
                    ),
                    cls="dsb-input-wrap",
                ),
                Button("Search →", cls="dsb-btn", type="button",
                       onclick="var q=document.getElementById('dash-search-input').value.trim();"
                               "if(q)window.location='/search?q='+encodeURIComponent(q);"),
                cls="dsb-search-row",
            ),
            cls="dsb-inner",
        ),
        cls="dash-search-banner",
    )

    filter_bar = Div(
        # Main category tabs — card-pill style
        Div(
            Span("🌐 All",        cls="cat-pill active", data_cat="all",     onclick="filterCat(this,'all')"),
            Span("✈️ Flights",    cls="cat-pill",        data_cat="flights",  onclick="filterCat(this,'flights')"),
            Span("🏨 Hotels",     cls="cat-pill",        data_cat="hotels",   onclick="filterCat(this,'hotels')"),
            Span("🗺️ Tours",      cls="cat-pill",        data_cat="tours",    onclick="filterCat(this,'tours')"),
            cls="cat-tabs",
        ),
        # Sub-rows: destinations (all) + domestic/intl per category
        Div(
            # Popular destinations — visible when "All" is active
            Div(
                Span("Popular", cls="dest-label"),
                A("✈️ Cebu",        cls="sub-pill", href="/search?q=Cebu"),
                A("🏖️ Boracay",     cls="sub-pill", href="/search?q=Boracay"),
                A("🌊 Siargao",     cls="sub-pill", href="/search?q=Siargao"),
                A("🌸 Baguio",      cls="sub-pill", href="/search?q=Baguio"),
                A("🗼 Tokyo",       cls="sub-pill", href="/search?q=Tokyo"),
                A("🇸🇬 Singapore",  cls="sub-pill", href="/search?q=Singapore"),
                A("🌍 Abroad",      cls="sub-pill", href="/search?q=international"),
                cls="sub-tabs", id="sub-all",
            ),
            # Per-category sub-filters
            Div(
                Span("✈️ All Flights",    cls="sub-pill active", data_sub="all",           onclick="filterSub(this,'flights','all')"),
                Span("🇵🇭 Domestic",      cls="sub-pill",        data_sub="domestic",      onclick="filterSub(this,'flights','domestic')"),
                Span("🌏 International",  cls="sub-pill",        data_sub="international", onclick="filterSub(this,'flights','international')"),
                cls="sub-tabs", id="sub-flights", style="display:none",
            ),
            Div(
                Span("🏨 All Hotels",     cls="sub-pill active", data_sub="all",           onclick="filterSub(this,'hotels','all')"),
                Span("🇵🇭 Local",         cls="sub-pill",        data_sub="domestic",      onclick="filterSub(this,'hotels','domestic')"),
                Span("🌏 International",  cls="sub-pill",        data_sub="international", onclick="filterSub(this,'hotels','international')"),
                cls="sub-tabs", id="sub-hotels", style="display:none",
            ),
            Div(
                Span("🗺️ All Tours",      cls="sub-pill active", data_sub="all",           onclick="filterSub(this,'tours','all')"),
                Span("🌴 Domestic",       cls="sub-pill",        data_sub="domestic",      onclick="filterSub(this,'tours','domestic')"),
                Span("🌍 International",  cls="sub-pill",        data_sub="international", onclick="filterSub(this,'tours','international')"),
                cls="sub-tabs", id="sub-tours", style="display:none",
            ),
            cls="sub-tabs-wrap",
        ),
        cls="filter-bar",
    )

    content = Div(
        search_banner,
        filter_bar,
        Div(
            sec_head("✈️ Hot Flights", "Lowest fares across PH and beyond", "/book?type=flight"),
            _section_content("flights", fp, flight_card),
            id="cat-flights", data_section="flights",
        ),
        Div(
            sec_head("🏨 Top Hotels", "Handpicked stays for every budget", "/book?type=hotel"),
            _section_content("hotels", hp, hotel_card),
            id="cat-hotels", data_section="hotels",
        ),
        Div(
            sec_head("🗺️ Best Tours", "Curated adventures, local & international", "/book?type=tour"),
            _section_content("tours", tp, tour_card),
            id="cat-tours", data_section="tours",
        ),
        Div(style="height:40px"),
        # ── Quick-Book Modal ────────────────────────────────────
        Div(
            Div(
                # ── Sheet ────────────────────────────────────────
                Div(
                    # Drag handle
                    Div(cls="qb-handle"),
                    # Form view
                    Div(
                        # Header
                        Div(
                            Div(
                                Span("✈️", id="qb-icon", cls="qb-icon"),
                                Div(
                                    Div("", id="qb-name", cls="qb-name"),
                                    Div("", id="qb-detail", cls="qb-detail"),
                                    cls="qb-header-text",
                                ),
                                cls="qb-header-left",
                            ),
                            Button("✕", cls="qb-close", type="button", onclick="closeQuickBook()"),
                            cls="qb-header",
                        ),
                        Div(cls="qb-divider"),
                        # Price strip
                        Div(
                            Span("Price", cls="qb-price-label"),
                            Span("", id="qb-price", cls="qb-price-value"),
                            cls="qb-price-strip",
                        ),
                        # Date field
                        Div(
                            Div("", id="qb-date-label", cls="qb-field-label"),
                            Input(type="date", id="qb-date", cls="qb-field-input"),
                            cls="qb-field",
                        ),
                        # Travelers stepper
                        Div(
                            Div("", id="qb-pax-label", cls="qb-field-label"),
                            Div(
                                Button("−", type="button", cls="qb-pax-btn", onclick="qbPax(-1)"),
                                Span("1", id="qb-pax-count", cls="qb-pax-count"),
                                Button("+", type="button", cls="qb-pax-btn", onclick="qbPax(1)"),
                                cls="qb-pax-row",
                            ),
                            cls="qb-field",
                        ),
                        # Total
                        Div(
                            Span("Estimated Total", cls="qb-total-label"),
                            Span("", id="qb-total", cls="qb-total-value"),
                            cls="qb-total-strip",
                        ),
                        # Confirm
                        Button("Confirm Booking →", type="button", cls="qb-confirm-btn",
                               onclick="qbConfirm()"),
                        id="qb-form-view",
                    ),
                    # Success view (hidden initially)
                    Div(
                        Div("🎉", cls="qb-success-icon"),
                        Div("Added to Suitcase!", cls="qb-success-title"),
                        Div("Your booking is saved offline.", cls="qb-success-sub"),
                        Div("", id="qb-success-ref", cls="qb-success-ref"),
                        Div(
                            Button("View Suitcase", type="button", cls="qb-suitcase-btn",
                                   onclick="window.location='/suitcase'"),
                            Button("Book Another", type="button", cls="qb-again-btn",
                                   onclick="closeQuickBook()"),
                            cls="qb-success-actions",
                        ),
                        id="qb-success-view", style="display:none",
                    ),
                    id="qb-modal-sheet", cls="qb-modal-sheet",
                    onclick="event.stopPropagation()",
                ),
                id="qb-modal", cls="qb-modal-overlay",
                onclick="closeQuickBook()", style="display:none",
            ),
        ),
        Script("""
// ── Quick-Book Modal ────────────────────────────────────────
var _qbItem = null, _qbPax = 1;

function openQuickBook(item) {
  _qbItem = item;
  _qbPax = 1;
  document.getElementById('qb-icon').textContent   = item.icon;
  document.getElementById('qb-name').textContent   = item.name;
  document.getElementById('qb-detail').textContent = item.detail;
  document.getElementById('qb-price').textContent  = item.priceLabel;
  document.getElementById('qb-date-label').textContent = item.dateLabel;
  document.getElementById('qb-pax-label').textContent  = item.paxLabel;
  document.getElementById('qb-pax-count').textContent  = '1';
  document.getElementById('qb-total').textContent  = item.priceLabel;
  document.getElementById('qb-date').value = '';
  document.getElementById('qb-form-view').style.display    = '';
  document.getElementById('qb-success-view').style.display = 'none';
  var modal = document.getElementById('qb-modal');
  modal.style.display = '';
  document.body.style.overflow = 'hidden';
  setTimeout(function() {
    document.getElementById('qb-modal-sheet').classList.add('open');
  }, 10);
}

function closeQuickBook() {
  document.getElementById('qb-modal-sheet').classList.remove('open');
  document.body.style.overflow = '';
  setTimeout(function() {
    document.getElementById('qb-modal').style.display = 'none';
  }, 320);
}

function qbPax(delta) {
  _qbPax = Math.max(1, Math.min(9, _qbPax + delta));
  document.getElementById('qb-pax-count').textContent = _qbPax;
  var total = _qbItem.price * _qbPax;
  document.getElementById('qb-total').textContent = '₱' + total.toLocaleString();
}

function qbConfirm() {
  var date = document.getElementById('qb-date').value;
  if (!date) {
    var inp = document.getElementById('qb-date');
    inp.style.borderColor = '#ef4444';
    inp.focus();
    setTimeout(function() { inp.style.borderColor = ''; }, 1800);
    return;
  }
  var ref = 'GGW-' + Date.now().toString(36).toUpperCase().slice(-6);
  var booking = {
    ref: ref,
    type: _qbItem.type,
    name: _qbItem.name,
    date: date,
    pax: _qbPax,
    price: _qbItem.price * _qbPax,
    status: 'Pending',
    createdAt: new Date().toISOString(),
  };
  if (_qbItem.origin)      booking.origin      = _qbItem.origin;
  if (_qbItem.destination) booking.destination = _qbItem.destination;
  if (_qbItem.city)        booking.city        = _qbItem.city;

  var trips = JSON.parse(localStorage.getItem('gegow_trips') || '[]');
  trips.unshift(booking);
  localStorage.setItem('gegow_trips', JSON.stringify(trips));

  document.getElementById('qb-form-view').style.display    = 'none';
  document.getElementById('qb-success-view').style.display = '';
  document.getElementById('qb-success-ref').textContent    = 'Ref: ' + ref;
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeQuickBook();
});

// ── Filter / search ─────────────────────────────────────────
function filterCat(pill, cat) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  pill.classList.add('active');
  document.querySelectorAll('[data-section]').forEach(s => {
    s.style.display = (cat === 'all' || s.dataset.section === cat) ? '' : 'none';
  });
  document.querySelectorAll('.sub-tabs').forEach(t => t.style.display = 'none');
  const destRow = document.getElementById('sub-all');
  if (cat === 'all') {
    if (destRow) destRow.style.display = '';
  } else {
    if (destRow) destRow.style.display = 'none';
    const bar = document.getElementById('sub-' + cat);
    if (bar) {
      bar.style.display = '';
      bar.querySelectorAll('.sub-pill').forEach(p => p.classList.remove('active'));
      bar.querySelector('[data-sub="all"]').classList.add('active');
      htmx.ajax('GET', '/dashboard/page/' + cat + '?page=1&sub=all',
        {target: '#' + cat + '-content', swap: 'innerHTML'});
    }
  }
}
function filterSub(pill, cat, sub) {
  document.querySelectorAll('#sub-' + cat + ' .sub-pill').forEach(p => p.classList.remove('active'));
  pill.classList.add('active');
  htmx.ajax('GET', '/dashboard/page/' + cat + '?page=1&sub=' + sub,
    {target: '#' + cat + '-content', swap: 'innerHTML'});
}
document.getElementById('dash-search-input')?.addEventListener('keydown', e => {
  if (e.key === 'Enter') {
    const q = e.target.value.trim();
    if (q) window.location = '/search?q=' + encodeURIComponent(q);
  }
});
"""),
    )
    return page_shell(content, active="/dashboard", title="Explore")


# ─────────────────────────────────────────────────────────────
# User Profile / Personal Dashboard
# ─────────────────────────────────────────────────────────────

@rt('/profile')
def get(request):
    from app.logic.supabase_db import get_user_from_token, get_itineraries

    # Try to load user from session cookie
    token = request.cookies.get("gegow_token")
    user = get_user_from_token(token) if token else None

    name  = ""
    email = ""
    if user:
        meta  = user.get("user_metadata", {})
        name  = _safe(meta.get("full_name") or meta.get("name") or "")
        email = _safe(user.get("email", ""))

    initials = (name[:1] or email[:1] or "?").upper()

    # Saved itineraries as proxy for booking count
    itineraries = get_itineraries(user["id"]) if user else []
    booking_count = len(itineraries)

    # ── Hero ─────────────────────────────────────────────────
    hero = Div(
        # Avatar with animated ring
        Div(
            Div(initials, cls="profile-avatar"),
            Div(cls="profile-avatar-ring"),
            cls="profile-avatar-wrap",
        ),
        Div(name or "Traveler", cls="profile-name"),
        Div(email or "Not signed in", cls="profile-email"),
        Div("✈ Gegow Member", cls="profile-badge"),
        A("Log out", href="/auth/logout", cls="profile-logout-btn"),
        cls="profile-hero",
    )

    # ── Quick-Book Strip (always first — reduce booking friction) ─
    quick_book = Div(
        Div("Book a Trip", cls="quick-book-strip-title"),
        Div(
            A(
                Span("✈️", cls="qb-icon"),
                Div("Flights", cls="qb-label"),
                Div("Domestic & intl", cls="qb-sub"),
                href="/book?type=flight", cls="qb-card qb-flight fade-up",
            ),
            A(
                Span("🏨", cls="qb-icon"),
                Div("Hotels", cls="qb-label"),
                Div("Best rates", cls="qb-sub"),
                href="/book?type=hotel", cls="qb-card qb-hotel fade-up",
                **{"data-delay": "70"},
            ),
            A(
                Span("🗺️", cls="qb-icon"),
                Div("Tours", cls="qb-label"),
                Div("Curated trips", cls="qb-sub"),
                href="/book?type=tour", cls="qb-card qb-tour fade-up",
                **{"data-delay": "140"},
            ),
            cls="quick-book-row",
        ),
        A(
            Span("🧳", cls="suitcase-sc-icon"),
            Div(
                Div("My Suitcase", cls="suitcase-sc-title"),
                Div("Vouchers, itineraries & offline access", cls="suitcase-sc-sub"),
                cls="suitcase-sc-info",
            ),
            Span("›", cls="suitcase-sc-arrow"),
            href="/suitcase", cls="suitcase-shortcut fade-up",
            **{"data-delay": "210"},
        ),
        cls="quick-book-strip",
    )

    # ── Stats row ────────────────────────────────────────────
    stats = Div(
        Div(
            Span("🧳", cls="stat-icon"),
            Div(str(booking_count), cls="stat-num"),
            Div("Saved Trips", cls="stat-label"),
            cls="stat-card stat-card-trips",
        ),
        Div(
            Span("🗺️", cls="stat-icon"),
            Div("0", cls="stat-num"),
            Div("Destinations", cls="stat-label"),
            cls="stat-card stat-card-dest",
        ),
        Div(
            Span("💰", cls="stat-icon"),
            Div("₱0", cls="stat-num"),
            Div("Total Spent", cls="stat-label"),
            cls="stat-card stat-card-spent",
        ),
        cls="profile-stats",
    )

    # ── Recent bookings ──────────────────────────────────────
    TYPE_MAP = {"flight": ("✈️", "booking-flight"), "hotel": ("🏨", "booking-hotel"), "tour": ("🗺️", "booking-tour")}

    def _booking_row(it):
        typ   = it.get("type", "")
        dest  = _safe(it.get("destination") or it.get("hotel") or it.get("tour") or "Booking")
        date  = _safe((it.get("travel_date") or it.get("check_in") or ""))[:10]
        icon, item_cls = TYPE_MAP.get(typ, ("🧳", "booking-default"))
        return Div(
            Div(icon, cls="booking-icon-wrap"),
            Div(
                Div(dest, cls="booking-title"),
                Div(date or "Date TBD", cls="booking-sub"),
                cls="booking-info",
            ),
            Span("Saved", cls="booking-badge badge-upcoming"),
            cls=f"booking-item {item_cls}",
        )

    if itineraries:
        booking_items = [_booking_row(it) for it in itineraries[:5]]
    else:
        booking_items = [
            A(
                Div("✈️", cls="booking-icon-wrap"),
                Div(
                    Div("No trips yet", cls="booking-title"),
                    Div("Tap a booking button above to start planning!", cls="booking-sub"),
                    cls="booking-info",
                ),
                Span("Book now →", cls="booking-badge badge-empty"),
                href="/book", cls="booking-item booking-default",
                style="text-decoration:none;cursor:pointer;",
            )
        ]

    bookings_section = Div(
        Div("Saved Trips", cls="profile-section-title"),
        Div(*booking_items, cls="booking-list"),
        cls="profile-section",
    )

    # ── PWA install nudge — hidden until beforeinstallprompt fires ──
    pwa_nudge = Div(
        Span("📲", cls="pwa-nudge-icon"),
        Div(
            Div("Install Gegow App", cls="pwa-nudge-title"),
            Div("Works offline · No app store · Free", cls="pwa-nudge-sub"),
            cls="pwa-nudge-info",
        ),
        Button("Install", cls="pwa-nudge-btn",
               onclick="window.triggerPWAInstall && window.triggerPWAInstall()"),
        cls="pwa-nudge fade-up",
        id="profile-pwa-nudge",
        style="display:none",
        **{"data-pwa-install": "1"},
    )

    content = Div(
        hero,
        quick_book,
        Div(stats, cls="profile-section", style="padding-top:18px"),
        bookings_section,
        Div(style="height:16px"),
        pwa_nudge,
        Div(style="height:24px"),
        cls="profile-page",
        id="profile-page-root",
    )

    install_js = Script("""
(function(){
  // Hide nudge if already running as installed PWA
  const nudge = document.getElementById('profile-pwa-nudge');
  if (nudge && (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone)) {
    nudge.style.display = 'none';
  }
})();
""")

    return page_shell(
        Div(content, install_js),
        active="/profile", title="My Profile"
    )


@rt('/book')
def get(trip_type: str = ""):
    from app.components.wizard import wizard_step1
    from app.routes.booking import _render_step2

    content = _render_step2(trip_type) if trip_type else wizard_step1()
    return page_shell(content, active="/book", title="Book a Trip")


@rt('/gear')
def get(category: str = "all"):
    from app.routes.shop import SHOP_CATALOG, CATEGORIES, SECTION_META
    from app.components.cards import gear_card

    # ── Category tabs ─────────────────────────────────────────
    tabs = [
        A(label, href=f"/gear?category={cat}",
          cls=f"cat-tab {'active' if cat == category else ''}")
        for cat, label in CATEGORIES.items()
    ]

    # ── Hero banner ───────────────────────────────────────────
    hero = Div(
        Div(
            Div("🛍️ Gegow Shop", cls="shop-hero-badge"),
            Div("Souvenirs · Food · Gear · Clothing", cls="shop-hero-title"),
            Div("Philippine pasalubong, beach essentials & travel accessories — delivered.",
                cls="shop-hero-sub"),
            cls="shop-hero-inner",
        ),
        cls="shop-hero",
    )

    # ── Build sections ────────────────────────────────────────
    if category == "all":
        # Show all categories with section headers
        sections = []
        for cat_key, (icon, title, sub) in SECTION_META.items():
            cat_items = [i for i in SHOP_CATALOG if i["category"] == cat_key]
            if not cat_items:
                continue
            sections.append(
                Div(
                    Div(
                        Div(
                            Div(icon, cls="shop-section-icon"),
                            Div(title, cls="shop-section-title"),
                            Div(sub, cls="shop-section-sub"),
                            cls="shop-section-left",
                        ),
                        A("See all →", href=f"/gear?category={cat_key}", cls="shop-section-see-all"),
                        cls="shop-section-head",
                    ),
                    Div(*[gear_card(i) for i in cat_items], cls="gear-grid stagger"),
                    Div(cls="shop-divider"),
                )
            )
        body = Div(*sections, cls="shop-body")
    else:
        # Single category
        items = [i for i in SHOP_CATALOG if i["category"] == category]
        icon, title, sub = SECTION_META.get(category, ("🛍️", category.title(), ""))
        body = Div(
            Div(
                Div(
                    Div(icon, cls="shop-section-icon"),
                    Div(title, cls="shop-section-title"),
                    Div(sub, cls="shop-section-sub"),
                    cls="shop-section-left",
                ),
                cls="shop-section-head",
            ),
            Div(*[gear_card(i) for i in items], cls="gear-grid stagger"),
            Div(style="height:16px"),
            cls="shop-body",
        )

    # ── Cart FAB + Drawer ─────────────────────────────────────
    cart_fab = Button(
        "🛒", Span("0", cls="cart-badge", id="cart-badge"),
        cls="cart-fab", onclick="showCart()",
    )

    cart_drawer = Div(
        # Overlay
        Div(cls="cart-overlay", id="cart-overlay", onclick="closeCart()"),
        # Drawer
        Div(
            # Head
            Div(
                Div(
                    Div("My Cart", cls="cart-drawer-title"),
                    Div("0 items", cls="cart-drawer-count", id="cart-drawer-count"),
                ),
                Button("✕", cls="cart-close-btn", onclick="closeCart()"),
                cls="cart-drawer-head",
            ),
            # Items
            Div(id="cart-items-list", cls="cart-items"),
            # Footer
            Div(
                Div(
                    Span("Total", cls="cart-total-lbl"),
                    Span("₱0", cls="cart-total-val", id="cart-total-val"),
                    cls="cart-total-row",
                ),
                Button("Checkout (COD) →", cls="cart-checkout-btn", id="cart-checkout-btn"),
                Button("Continue Shopping", cls="cart-continue-btn", onclick="closeCart()"),
                cls="cart-footer",
            ),
            cls="cart-drawer", id="cart-drawer",
        ),
    )

    cart_js = Script(r"""
(function(){
  var KEY = 'gegow_cart';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch(e) { return []; }
  }
  function save(cart) { localStorage.setItem(KEY, JSON.stringify(cart)); }

  function peso(n) {
    return '\u20b1' + (parseInt(n)||0).toLocaleString();
  }

  function renderCart() {
    var cart  = load();
    var list  = document.getElementById('cart-items-list');
    var total = cart.reduce(function(s,i){ return s + (parseInt(i.price)||0) * (parseInt(i.qty)||1); }, 0);
    var count = cart.reduce(function(s,i){ return s + (parseInt(i.qty)||1); }, 0);

    var badge = document.getElementById('cart-badge');
    if (badge) { badge.textContent = count; badge.style.display = count > 0 ? 'flex' : 'none'; }

    var countEl = document.getElementById('cart-drawer-count');
    if (countEl) countEl.textContent = count + ' item' + (count !== 1 ? 's' : '');

    var totalEl = document.getElementById('cart-total-val');
    if (totalEl) totalEl.textContent = peso(total);

    if (!list) return;

    if (!cart.length) {
      list.innerHTML = '<div class="cart-empty"><div class="cart-empty-icon">🛒</div><div class="cart-empty-txt">Your cart is empty</div></div>';
      return;
    }

    list.innerHTML = cart.map(function(item, idx) {
      var subtotal = (parseInt(item.price)||0) * (parseInt(item.qty)||1);
      return '<div class="cart-row">'
        + '<div class="cart-row-icon">' + (item.emoji || '\ud83d\udecb') + '</div>'
        + '<div class="cart-row-info">'
          + '<div class="cart-row-name">' + item.name + '</div>'
          + '<div class="cart-row-price">' + peso(subtotal) + '</div>'
          + '<div class="cart-qty-row">'
            + '<button class="cart-qty-btn" onclick="cartQty(' + idx + ',-1)">\u2212</button>'
            + '<span class="cart-qty-num">' + (item.qty||1) + '</span>'
            + '<button class="cart-qty-btn" onclick="cartQty(' + idx + ',1)">+</button>'
          + '</div>'
        + '</div>'
        + '<button class="cart-rm-btn" onclick="cartRemove(' + idx + ')">\u2715</button>'
      + '</div>';
    }).join('');
  }

  window.showCart = function() {
    renderCart();
    document.getElementById('cart-overlay').classList.add('open');
    document.getElementById('cart-drawer').classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.closeCart = function() {
    document.getElementById('cart-overlay').classList.remove('open');
    document.getElementById('cart-drawer').classList.remove('open');
    document.body.style.overflow = '';
  };

  window.cartQty = function(idx, delta) {
    var cart = load();
    if (!cart[idx]) return;
    cart[idx].qty = Math.max(1, (parseInt(cart[idx].qty)||1) + delta);
    save(cart);
    renderCart();
  };

  window.cartRemove = function(idx) {
    var cart = load();
    cart.splice(idx, 1);
    save(cart);
    renderCart();
    updateCartBadge && updateCartBadge();
  };

  /* Override addToCart after app.js has loaded (deferred scripts run before DOMContentLoaded) */
  document.addEventListener('DOMContentLoaded', function() {
    window.addToCart = function(btn) {
      try {
        var vals = JSON.parse(btn.getAttribute('hx-vals') || '{}');
        var cart = load();
        var existing = cart.find(function(i){ return i.item_id === vals.item_id; });
        if (existing) {
          existing.qty = (parseInt(existing.qty)||1) + 1;
        } else {
          cart.push({ item_id: vals.item_id, name: vals.name, price: vals.price, emoji: vals.emoji||'', qty: 1 });
        }
        save(cart);
        /* Visual feedback */
        var orig = btn.textContent;
        btn.textContent = '\u2713 Added!';
        btn.classList.add('added');
        setTimeout(function(){ btn.textContent = orig; btn.classList.remove('added'); }, 1400);
        renderCart();
      } catch(e) { console.warn('addToCart error', e); }
    };

    document.getElementById('cart-checkout-btn')?.addEventListener('click', function(){
      var cart = load();
      if (!cart.length) { alert('Your cart is empty!'); return; }
      alert('Checkout coming soon!\nOur team will contact you via WhatsApp to confirm your order. \ud83d\udcf2');
    });
  });

  /* Init badge immediately (before DOMContentLoaded) */
  renderCart();
})();
""")

    content = Div(hero, Div(*tabs, cls="category-tabs"), body, cart_fab, cart_drawer, cart_js)
    return page_shell(content, active="/gear", title="Gegow Shop")


@rt('/b2b')
def get(tab: str = "manning"):
    from app.routes.b2b import _manning_form, _corporate_form

    content = Div(
        # ── Hero ─────────────────────────────────────────────────
        Div(
            Div(
                Div("🏢 Partnership Portal", cls="b2b-hero-eyebrow"),
                Div("Grow Your Business with Gegow", cls="b2b-hero-title"),
                Div(
                    "Exclusive group rates for Manning Agencies and Corporate accounts. "
                    "Flights · Hotels · Tours — all with dedicated support.",
                    cls="b2b-hero-sub",
                ),
                Div(
                    Div(
                        Div("🤝", cls="b2b-stat-icon"),
                        Div(
                            Div("500+", cls="b2b-stat-val"),
                            Div("Partner Companies", cls="b2b-stat-lbl"),
                        ),
                        cls="b2b-stat",
                    ),
                    Div(
                        Div("✈️", cls="b2b-stat-icon"),
                        Div(
                            Div("₱1M+", cls="b2b-stat-val"),
                            Div("Monthly Bookings", cls="b2b-stat-lbl"),
                        ),
                        cls="b2b-stat",
                    ),
                    Div(
                        Div("⚡", cls="b2b-stat-icon"),
                        Div(
                            Div("24h", cls="b2b-stat-val"),
                            Div("Response Time", cls="b2b-stat-lbl"),
                        ),
                        cls="b2b-stat",
                    ),
                    cls="b2b-stats",
                ),
                cls="b2b-hero-inner",
            ),
            cls="b2b-hero",
        ),
        # ── Tabs ─────────────────────────────────────────────────
        Div(
            A("🚢 Manning Agency",  href="/b2b?tab=manning",
              cls=f"b2b-tab-pill {'active' if tab == 'manning' else ''}"),
            A("🏢 Corporate Travel", href="/b2b?tab=corporate",
              cls=f"b2b-tab-pill {'active' if tab == 'corporate' else ''}"),
            cls="b2b-tabs-wrap",
        ),
        # ── Body ─────────────────────────────────────────────────
        _manning_form() if tab == "manning" else _corporate_form(),
    )
    return page_shell(content, active="/b2b", title="B2B Portal")


@rt('/suitcase')
def get():
    from app.components.suitcase import suitcase_page
    return page_shell(suitcase_page(), active="/suitcase", title="My Suitcase")


# ─────────────────────────────────────────────────────────────
# Landing & Auth pages (standalone — no app shell)
# ─────────────────────────────────────────────────────────────

@rt('/')
def get():
    from app.pages.landing import landing_page
    return landing_page()


@rt('/login')
def get():
    from app.pages.auth import login_page
    from app.logic.supabase_db import is_configured
    return login_page(supabase_ok=is_configured())


@rt('/signup')
def get():
    from app.pages.auth import login_page
    from app.logic.supabase_db import is_configured
    return login_page(supabase_ok=is_configured())


# ─────────────────────────────────────────────────────────────
# Google OAuth — PKCE flow via Supabase
# ─────────────────────────────────────────────────────────────

def _app_url() -> str:
    return os.getenv("APP_URL", "http://localhost:8000").rstrip("/")


def _set_session_cookies(response, access_token: str, refresh_token: str):
    response.set_cookie("gegow_token",   access_token,  httponly=True, samesite="lax", max_age=60*60*24*7)
    response.set_cookie("gegow_refresh", refresh_token, httponly=True, samesite="lax", max_age=60*60*24*30)


@rt('/auth/google')
def get():
    from app.logic.supabase_db import get_google_oauth_url, is_configured
    if not is_configured():
        return StarletteRedirect('/login?error=supabase_not_configured', status_code=303)

    oauth_url, code_verifier = get_google_oauth_url(_app_url())
    if not oauth_url:
        return StarletteRedirect('/login?error=oauth_failed', status_code=303)

    resp = StarletteRedirect(oauth_url, status_code=302)
    # Store verifier in short-lived httpOnly cookie (5 min)
    resp.set_cookie("gegow_cv", code_verifier, httponly=True, samesite="lax", max_age=300, path="/")
    return resp


@rt('/auth/callback')
def get(request):
    code = request.query_params.get("code")
    error = request.query_params.get("error")
    error_desc = _safe(request.query_params.get("error_description", ""))

    if error or not code:
        from app.pages.auth_callback import error_page
        return error_page(error_desc or _safe(error or "") or "No auth code received")

    code_verifier = request.cookies.get("gegow_cv")
    if not code_verifier:
        from app.pages.auth_callback import error_page
        return error_page("Session expired — please try signing in again.")

    from app.logic.supabase_db import exchange_pkce_code, get_or_create_profile
    session_data = exchange_pkce_code(code, code_verifier)

    if not session_data or "access_token" not in session_data:
        from app.pages.auth_callback import error_page
        return error_page("Token exchange failed. Please try again.")

    access_token  = session_data["access_token"]
    refresh_token = session_data.get("refresh_token", "")
    user          = session_data.get("user", {})

    # Ensure profile row exists in Supabase
    if user.get("id") and user.get("email"):
        get_or_create_profile(user["id"], user["email"])

    resp = StarletteRedirect('/dashboard', status_code=303)
    _set_session_cookies(resp, access_token, refresh_token)
    resp.delete_cookie("gegow_cv", path="/")
    return resp


@rt('/auth/logout')
def get():
    resp = StarletteRedirect('/login', status_code=303)
    resp.delete_cookie("gegow_token")
    resp.delete_cookie("gegow_refresh")
    return resp


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
