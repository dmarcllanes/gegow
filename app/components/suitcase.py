"""
My Suitcase — redesigned travel history & upcoming trips dashboard.
Data is read from localStorage (saved by the booking wizard confirm step).
"""

from fasthtml.common import Div, Span, A, Script, H2, P

SUITCASE_CSS = """
/* ══════════════════════════════════════════════════
   SUITCASE HERO
══════════════════════════════════════════════════ */
.sc-hero {
  background: #070f1a;
  padding: 28px 20px 24px;
  color: #fff;
  position: relative;
  overflow: hidden;
}
.sc-hero::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 200px;
  background: radial-gradient(ellipse 200% 100% at 50% 0%,
    rgba(0,201,177,.16) 0%, transparent 70%);
  pointer-events: none;
}
.sc-hero-eyebrow {
  position: relative; z-index: 1;
  font-size: 10px; font-weight: 800; letter-spacing: 1.8px;
  text-transform: uppercase; color: #00C9B1; margin-bottom: 6px;
}
.sc-hero-title {
  position: relative; z-index: 1;
  font-size: 28px; font-weight: 900; letter-spacing: -.5px;
  line-height: 1.15; margin-bottom: 4px;
}
.sc-hero-sub {
  position: relative; z-index: 1;
  font-size: 13px; color: rgba(255,255,255,.45); line-height: 1.5;
}
.sc-stats {
  position: relative; z-index: 1;
  display: flex; gap: 10px; margin-top: 22px;
}
.sc-stat {
  flex: 1;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.10);
  border-radius: 14px; padding: 13px 10px 11px;
  text-align: center;
  transition: background .2s, border-color .2s;
}
.sc-stat:hover {
  background: rgba(0,201,177,.08);
  border-color: rgba(0,201,177,.22);
}
.sc-stat-val {
  font-size: 20px; font-weight: 900;
  color: #00C9B1; line-height: 1;
}
.sc-stat-lbl {
  font-size: 9px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 1px;
  color: rgba(255,255,255,.3); margin-top: 4px;
}

/* ══════════════════════════════════════════════════
   STATUS TABS
══════════════════════════════════════════════════ */
.sc-tabs {
  display: flex;
  background: #fff;
  border-bottom: 1.5px solid var(--border);
  overflow-x: auto; scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.sc-tabs::-webkit-scrollbar { display: none; }
.sc-tab {
  flex: 1; padding: 13px 6px 12px;
  text-align: center;
  font-size: 12px; font-weight: 600;
  color: var(--muted);
  border-bottom: 2px solid transparent;
  margin-bottom: -1.5px;
  cursor: pointer; white-space: nowrap;
  transition: color .15s, border-color .15s;
  min-width: 72px;
  user-select: none;
}
.sc-tab:hover { color: var(--text); }
.sc-tab.active {
  color: var(--teal);
  border-bottom-color: var(--teal);
  font-weight: 700;
}
.sc-count-badge {
  display: inline-flex; align-items: center; justify-content: center;
  background: rgba(0,109,119,.1); color: var(--teal);
  font-size: 10px; font-weight: 700;
  padding: 1px 6px; border-radius: 10px; margin-left: 4px;
  min-width: 18px;
}
.sc-tab.active .sc-count-badge {
  background: var(--teal); color: #fff;
}

/* ══════════════════════════════════════════════════
   LIST AREA
══════════════════════════════════════════════════ */
.sc-list-wrap {
  padding: 16px 16px 100px;
  background: var(--beige);
  min-height: 60vh;
}

/* ══════════════════════════════════════════════════
   TRIP CARD
══════════════════════════════════════════════════ */
.sc-card {
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(15,23,42,.07), 0 1px 2px rgba(15,23,42,.04);
  overflow: hidden;
  margin-bottom: 14px;
  border: 1px solid rgba(15,23,42,.06);
  transition: transform .15s, box-shadow .15s;
}
.sc-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(15,23,42,.12), 0 2px 4px rgba(15,23,42,.06);
}

/* ── Gradient header (replaces photo background) ── */
.sc-card-header {
  padding: 20px 16px 18px;
  display: flex; align-items: flex-start; gap: 14px;
  position: relative; overflow: hidden;
}
.sc-card-header::after {
  content: '';
  position: absolute; bottom: -1px; left: 0; right: 0; height: 20px;
  background: #fff; border-radius: 18px 18px 0 0;
}
.flight-header { background: linear-gradient(135deg, #0f766e 0%, #1d4ed8 100%); }
.hotel-header  { background: linear-gradient(135deg, #d97706 0%, #92400e 100%); }
.tour-header   { background: linear-gradient(135deg, #0284c7 0%, #075985 100%); }

.sc-icon-bubble {
  width: 56px; height: 56px; border-radius: 16px;
  background: rgba(255,255,255,.2);
  border: 1.5px solid rgba(255,255,255,.25);
  display: flex; align-items: center; justify-content: center;
  font-size: 30px; flex-shrink: 0;
}
.sc-header-content { flex: 1; min-width: 0; padding-right: 64px; }
.sc-header-type {
  font-size: 9px; font-weight: 800; letter-spacing: 1.8px;
  text-transform: uppercase; color: rgba(255,255,255,.6); margin-bottom: 4px;
}
.sc-header-title {
  font-size: 16px; font-weight: 900; color: #fff;
  line-height: 1.25; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.sc-header-ref {
  font-size: 11px; color: rgba(255,255,255,.45); margin-top: 5px;
  letter-spacing: .3px;
}

/* Status pill */
.sc-status-pill {
  position: absolute; top: 16px; right: 14px;
  padding: 4px 10px; border-radius: 20px;
  font-size: 10px; font-weight: 800; letter-spacing: .4px;
  text-transform: uppercase; white-space: nowrap;
}
.sc-status-upcoming {
  background: rgba(59,130,246,.22); color: #bfdbfe;
  border: 1px solid rgba(59,130,246,.35);
}
.sc-status-active {
  background: rgba(0,201,177,.22); color: #6ee7df;
  border: 1px solid rgba(0,201,177,.4);
  animation: pulse-active 2s infinite;
}
@keyframes pulse-active {
  0%,100% { box-shadow: 0 0 0 0 rgba(0,201,177,.4); }
  50%      { box-shadow: 0 0 0 4px rgba(0,201,177,.0); }
}
.sc-status-completed {
  background: rgba(255,255,255,.14); color: rgba(255,255,255,.6);
  border: 1px solid rgba(255,255,255,.2);
}

/* ── Date strip ────────────────────────────────── */
.sc-date-strip {
  padding: 14px 16px 13px;
  display: flex; align-items: center; gap: 10px;
  border-bottom: 1px solid var(--border);
  background: #fff;
}
.sc-date-block { flex: 1; min-width: 0; }
.sc-date-lbl {
  font-size: 9px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .8px; color: var(--muted-lt); margin-bottom: 3px;
}
.sc-date-val { font-size: 14px; font-weight: 700; color: var(--text); }
.sc-date-sep { font-size: 18px; color: var(--teal); flex-shrink: 0; }
.sc-duration-chip {
  background: var(--teal-xl); color: var(--teal-dk);
  font-size: 11px; font-weight: 700; white-space: nowrap;
  padding: 5px 11px; border-radius: 10px; flex-shrink: 0;
}
.sc-countdown-chip {
  background: rgba(59,130,246,.1); color: #2563EB;
  border: 1px solid rgba(59,130,246,.18);
  font-size: 11px; font-weight: 700; white-space: nowrap;
  padding: 5px 11px; border-radius: 10px; flex-shrink: 0;
}

/* ── Card footer ───────────────────────────────── */
.sc-footer {
  padding: 12px 16px 14px;
  display: flex; align-items: center; justify-content: space-between;
  background: #fff;
}
.sc-foot-price { font-size: 20px; font-weight: 900; color: var(--teal); line-height: 1; }
.sc-foot-pax   { font-size: 11px; color: var(--muted); margin-top: 2px; }
.sc-foot-actions { display: flex; gap: 8px; align-items: center; }
.sc-btn-book {
  padding: 9px 18px;
  background: var(--teal);
  color: #fff; font-size: 12px; font-weight: 700;
  border-radius: 10px; text-decoration: none;
  transition: background .15s, transform .15s;
}
.sc-btn-book:hover { background: var(--teal-dk); transform: translateY(-1px); }
.sc-delete-btn {
  width: 34px; height: 34px;
  display: flex; align-items: center; justify-content: center;
  background: transparent; border: 1.5px solid var(--border);
  border-radius: 9px; color: var(--muted-lt);
  font-size: 12px; cursor: pointer;
  transition: all .15s;
}
.sc-delete-btn:hover {
  background: rgba(239,68,68,.08); border-color: rgba(239,68,68,.3);
  color: #EF4444;
}

/* ══════════════════════════════════════════════════
   EMPTY STATE
══════════════════════════════════════════════════ */
.sc-empty {
  text-align: center; padding: 64px 24px 40px;
}
.sc-empty-icon { font-size: 72px; margin-bottom: 18px; line-height: 1; }
.sc-empty-title {
  font-size: 20px; font-weight: 800; color: var(--text);
  margin-bottom: 8px;
}
.sc-empty-sub {
  font-size: 14px; color: var(--muted); line-height: 1.65;
  max-width: 280px; margin: 0 auto 28px;
}
.sc-empty-cta {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--teal); color: #fff;
  padding: 12px 24px; border-radius: 12px;
  font-size: 14px; font-weight: 700;
  text-decoration: none;
  transition: background .15s;
}
.sc-empty-cta:hover { background: var(--teal-dk); }

/* ══════════════════════════════════════════════════
   OFFLINE BANNER
══════════════════════════════════════════════════ */
.sc-offline-banner {
  display: none;
  background: #FFF7ED; border: 1px solid #FED7AA;
  border-radius: 10px; padding: 10px 14px;
  margin-bottom: 14px;
  font-size: 12px; color: #92400E; font-weight: 600;
  align-items: center; gap: 8px;
}

/* ══════════════════════════════════════════════════
   NOW TRAVELING STRIP  (mobile only, JS-injected)
══════════════════════════════════════════════════ */
.sc-now-strip {
  display: none; /* shown by JS when active trip exists */
  position: relative; overflow: hidden;
  background: #070f1a;
  border-bottom: 1px solid rgba(0,201,177,.18);
}
.sc-now-strip-bg {
  position: absolute; inset: 0;
  background-size: cover; background-position: center;
  opacity: .35;
}
.sc-now-strip-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(90deg, rgba(7,15,26,.95) 35%, rgba(7,15,26,.5) 100%);
}
.sc-now-strip-body {
  position: relative; z-index: 1;
  display: flex; align-items: center; gap: 12px;
  padding: 14px 16px;
}
.sc-now-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: #00C9B1; flex-shrink: 0;
  box-shadow: 0 0 0 3px rgba(0,201,177,.25);
  animation: sc-dot-pulse 1.6s ease-in-out infinite;
}
@keyframes sc-dot-pulse {
  0%,100% { box-shadow: 0 0 0 3px rgba(0,201,177,.25); }
  50%      { box-shadow: 0 0 0 7px rgba(0,201,177,.0); }
}
.sc-now-info { flex: 1; min-width: 0; }
.sc-now-label {
  font-size: 9px; font-weight: 800; letter-spacing: 1.5px;
  text-transform: uppercase; color: #00C9B1; margin-bottom: 2px;
}
.sc-now-title {
  font-size: 14px; font-weight: 800; color: #fff;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.sc-now-meta {
  font-size: 11px; color: rgba(255,255,255,.45); margin-top: 1px;
}
.sc-now-icon {
  font-size: 30px; flex-shrink: 0;
  filter: drop-shadow(0 0 6px rgba(0,201,177,.4));
}

/* ══════════════════════════════════════════════════
   MOBILE-ONLY OVERRIDES  (< 768px)
══════════════════════════════════════════════════ */
@media (max-width: 767px) {
  /* Show the now-strip */
  .sc-now-strip { display: block; }

  /* Hero tighter on small screens */
  .sc-hero { padding: 22px 16px 20px; }
  .sc-hero-title { font-size: 24px; }
  .sc-stats { gap: 8px; margin-top: 18px; }
  .sc-stat { padding: 11px 8px 9px; border-radius: 12px; }
  .sc-stat-val { font-size: 18px; }

  /* Full-bleed list — no side padding */
  .sc-list-wrap { padding: 0 0 110px; background: #f0ede8; }

  /* Cards: edge-to-edge, flat sides, grouped with tiny gap */
  .sc-card {
    border-radius: 0;
    border-left: none;
    border-right: none;
    margin-bottom: 6px;
    box-shadow: 0 1px 0 rgba(15,23,42,.06);
  }
  .sc-card:last-child { margin-bottom: 0; }

  /* Card padding adjustments for mobile */
  .sc-card-header { padding: 16px 14px 16px; }
  .sc-header-content { padding-right: 60px; }
  .sc-date-strip  { padding: 12px 14px; }
  .sc-footer      { padding: 10px 14px 12px; }

  /* Disable desktop hover lift — avoid sticky on touch */
  .sc-card:hover { transform: none; box-shadow: 0 1px 0 rgba(15,23,42,.06); }

  /* Touch press feedback instead */
  .sc-card:active { background: #f8f8f6; }

  /* Empty state full-bleed */
  .sc-empty { padding: 56px 20px 32px; }

  /* ── Floating Book FAB ─────────────────────── */
  .sc-fab {
    display: flex;
  }
}

/* FAB — hidden on desktop */
.sc-fab {
  display: none;
  position: fixed; bottom: 82px; right: 18px;
  z-index: 300;
  align-items: center; gap: 8px;
  background: linear-gradient(135deg, #00C9B1, #007a6e);
  color: #fff;
  padding: 13px 18px 13px 14px;
  border-radius: 50px;
  box-shadow: 0 6px 24px rgba(0,201,177,.45), 0 2px 6px rgba(0,0,0,.18);
  font-size: 14px; font-weight: 800;
  text-decoration: none;
  transition: transform .15s, box-shadow .15s;
  -webkit-tap-highlight-color: transparent;
}
.sc-fab:active {
  transform: scale(.95);
  box-shadow: 0 3px 12px rgba(0,201,177,.35);
}
.sc-fab-icon { font-size: 18px; line-height: 1; }
"""


_SUITCASE_JS = """
(function() {
  const KEY  = 'gegow_suitcase';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch(e) { return []; }
  }

  function getStatus(dateFrom, dateTo) {
    const today = new Date(); today.setHours(0,0,0,0);
    const from  = new Date(dateFrom || '9999-01-01');
    const to    = new Date(dateTo   || dateFrom || '9999-01-01');
    if (from > today) return 'upcoming';
    if (to >= today)  return 'active';
    return 'completed';
  }

  function fmtDate(d) {
    if (!d) return '—';
    const dt = new Date(d);
    if (isNaN(dt)) return d;
    return dt.toLocaleDateString('en-PH', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  function peso(n) {
    const v = parseInt(n) || 0;
    return '\\u20b1' + v.toLocaleString();
  }

  function nights(from, to) {
    if (!from || !to) return 1;
    const n = Math.round((new Date(to) - new Date(from)) / 86400000);
    return Math.max(1, n);
  }

  const TYPE_ICON = { flight:'\\u2708\\ufe0f', hotel:'\\ud83c\\udfe8', tour:'\\ud83d\\uddfa\\ufe0f' };
  const TYPE_GRAD = {
    flight: 'linear-gradient(135deg,#0D9488 0%,#1E40AF 100%)',
    hotel:  'linear-gradient(135deg,#F59E0B 0%,#B45309 100%)',
    tour:   'linear-gradient(135deg,#06B6D4 0%,#0E7490 100%)',
  };
  const TYPE_IMG = {
    flight: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=75&auto=format&fit=crop',
    hotel:  'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=600&q=75&auto=format&fit=crop',
    tour:   'https://images.unsplash.com/photo-1501854140801-50d01698950b?w=600&q=75&auto=format&fit=crop',
  };
  const STATUS_MAP = {
    upcoming:  { cls: 'sc-status-upcoming',  txt: '\\ud83d\\uddd3 Upcoming' },
    active:    { cls: 'sc-status-active',    txt: '\\u2708\\ufe0f On Trip'  },
    completed: { cls: 'sc-status-completed', txt: '\\u2713 Completed'       },
  };

  function daysUntil(dateFrom) {
    if (!dateFrom) return null;
    const today = new Date(); today.setHours(0,0,0,0);
    const from  = new Date(dateFrom);
    const diff  = Math.round((from - today) / 86400000);
    if (diff < 0)   return null;
    if (diff === 0) return 'Today!';
    if (diff === 1) return 'Tomorrow';
    return 'in ' + diff + ' days';
  }

  function cardHTML(b) {
    const st   = getStatus(b.date_from, b.date_to);
    const sp   = STATUS_MAP[st] || STATUS_MAP.completed;
    const typ  = b.trip_type || 'flight';
    const icon = TYPE_ICON[typ] || '\ud83e\uddf3';
    const n    = nights(b.date_from, b.date_to);
    const pax  = (parseInt(b.adults)||1) + (parseInt(b.children)||0);
    const label = b.label || (typ.charAt(0).toUpperCase() + typ.slice(1) + ' Booking');
    const ref  = b.ref || '\u2014';
    const typLabels = { flight: 'Flight', hotel: 'Hotel Stay', tour: 'Tour Package' };
    const typLabel  = typLabels[typ] || typ;
    const dateLbl1  = typ === 'hotel' ? 'Check-in' : 'Departure';
    const dateLbl2  = typ === 'hotel' ? 'Check-out' : 'Return';
    let durationTxt = n + (typ === 'flight' ? ' day' : ' night') + (n !== 1 ? 's' : '');
    const countdown = st === 'upcoming' ? daysUntil(b.date_from) : null;
    const chipHTML  = countdown
      ? `<span class="sc-countdown-chip">\u23f0 ${countdown}</span>`
      : `<span class="sc-duration-chip">${durationTxt}</span>`;

    return `<div class="sc-card" data-status="${st}">
      <div class="sc-card-header ${typ}-header">
        <div class="sc-icon-bubble">${icon}</div>
        <div class="sc-header-content">
          <div class="sc-header-type">${typLabel}</div>
          <div class="sc-header-title">${label}</div>
          <div class="sc-header-ref">REF \u00b7 ${ref}</div>
        </div>
        <span class="sc-status-pill ${sp.cls}">${sp.txt}</span>
      </div>
      <div class="sc-date-strip">
        <div class="sc-date-block">
          <div class="sc-date-lbl">${dateLbl1}</div>
          <div class="sc-date-val">${fmtDate(b.date_from)}</div>
        </div>
        <div class="sc-date-sep">\u2192</div>
        <div class="sc-date-block">
          <div class="sc-date-lbl">${dateLbl2}</div>
          <div class="sc-date-val">${fmtDate(b.date_to) || '\u2014'}</div>
        </div>
        ${chipHTML}
      </div>
      <div class="sc-footer">
        <div>
          <div class="sc-foot-price">${peso(b.total)}</div>
          <div class="sc-foot-pax">${pax} traveler${pax !== 1 ? 's' : ''}</div>
        </div>
        <div class="sc-foot-actions">
          <a href="/book" class="sc-btn-book">Book Again</a>
          <button class="sc-delete-btn" onclick="scDeleteTrip('${ref}')" title="Remove">\u2715</button>
        </div>
      </div>
    </div>`;
  }

  function emptyHTML(filter) {
    const cfg = {
      all:       { icon: '\\ud83e\\uddf3', title: 'Your suitcase is empty',    sub: 'Complete a booking to see your trips here. Your itineraries are stored offline and always available.' },
      upcoming:  { icon: '\\ud83d\\uddd3', title: 'No upcoming trips',        sub: 'Nothing booked ahead yet. Start planning your next adventure!' },
      active:    { icon: '\\u2708\\ufe0f', title: "You're not traveling now", sub: 'No active trips at the moment. Book one today!' },
      completed: { icon: '\\ud83c\\udfc1', title: 'No completed trips yet',   sub: 'Past trips will appear here once your travel dates pass.' },
    };
    const c = cfg[filter] || cfg.all;
    const cta = filter === 'all'
      ? `<a href="/book" class="sc-empty-cta">Book a Trip &#x2192;</a>`
      : '';
    return `<div class="sc-empty">
      <div class="sc-empty-icon">${c.icon}</div>
      <div class="sc-empty-title">${c.title}</div>
      <div class="sc-empty-sub">${c.sub}</div>
      ${cta}
    </div>`;
  }

  function updateStats(trips) {
    const up    = trips.filter(t => getStatus(t.date_from, t.date_to) === 'upcoming').length;
    const total = trips.reduce((s, t) => s + (parseInt(t.total)||0), 0);
    const el = id => document.getElementById(id);
    if (el('sc-s-trips'))    el('sc-s-trips').textContent    = trips.length;
    if (el('sc-s-upcoming')) el('sc-s-upcoming').textContent = up;
    if (el('sc-s-spent'))    el('sc-s-spent').textContent    = '\\u20b1' + total.toLocaleString();
  }

  function updateBadges(trips) {
    const counts = { all: trips.length, upcoming: 0, active: 0, completed: 0 };
    trips.forEach(t => { const s = getStatus(t.date_from, t.date_to); counts[s] = (counts[s]||0)+1; });
    ['all','upcoming','active','completed'].forEach(s => {
      const el = document.getElementById('sc-badge-' + s);
      if (el) el.textContent = counts[s];
    });
  }

  function renderNowStrip(trips) {
    const strip = document.getElementById('sc-now-strip');
    if (!strip) return;
    const active = trips.find(t => getStatus(t.date_from, t.date_to) === 'active');
    if (!active) { strip.style.display = 'none'; return; }

    strip.style.display = 'block';
    const typ = active.trip_type || 'flight';
    const bg  = document.getElementById('sc-now-bg');
    const img = TYPE_IMG[typ] || TYPE_IMG.flight;
    if (bg) bg.style.backgroundImage = "url('" + img + "')";

    const el = id => document.getElementById(id);
    if (el('sc-now-title')) el('sc-now-title').textContent = active.label || (typ + ' Booking');
    if (el('sc-now-icon'))  el('sc-now-icon').textContent  = TYPE_ICON[typ] || '\\u2708\\ufe0f';
    if (el('sc-now-meta')) {
      const n = nights(active.date_from, active.date_to);
      const pax = (parseInt(active.adults)||1) + (parseInt(active.children)||0);
      el('sc-now-meta').textContent = fmtDate(active.date_from) + ' – ' + fmtDate(active.date_to) + '  ·  ' + pax + ' pax';
    }
  }

  function render(filter) {
    const list  = document.getElementById('sc-list');
    if (!list) return;
    const trips = load();
    updateStats(trips);
    updateBadges(trips);
    renderNowStrip(trips);
    const filtered = filter === 'all' ? trips : trips.filter(t => getStatus(t.date_from, t.date_to) === filter);
    list.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : emptyHTML(filter);
  }

  // Public API
  window.scSwitchTab = function(el, filter) {
    document.querySelectorAll('.sc-tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
    render(filter);
  };

  window.scDeleteTrip = function(ref) {
    if (!confirm('Remove this trip from your suitcase?')) return;
    const trips = load().filter(t => String(t.ref) !== String(ref));
    localStorage.setItem(KEY, JSON.stringify(trips));
    const active = document.querySelector('.sc-tab.active');
    render(active ? active.dataset.filter : 'all');
  };

  // Also expose saveToSuitcase globally (called by booking confirm)
  window.saveToSuitcase = function(booking) {
    const trips = load();
    trips.unshift(booking);
    localStorage.setItem(KEY, JSON.stringify(trips));
  };

  // Init
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => render('all'));
  } else {
    render('all');
  }
})();
"""


def suitcase_page() -> Div:
    return Div(
        # ── FAB: mobile only "Book a Trip" floating button ────────────
        A(
            Span("✈", cls="sc-fab-icon"),
            "Book a Trip",
            href="/book",
            cls="sc-fab",
            title="Book a new trip",
        ),

        # ── Hero ──────────────────────────────────────────────────────
        Div(
            Div("My Suitcase", cls="sc-hero-eyebrow"),
            Div("All My Travels", cls="sc-hero-title"),
            Div(
                "Upcoming trips, active journeys & completed adventures —",
                Span(" available offline.", style="color:rgba(255,255,255,.55)"),
                cls="sc-hero-sub",
            ),
            Div(
                Div(
                    Div("0", cls="sc-stat-val", id="sc-s-trips"),
                    Div("Total Trips", cls="sc-stat-lbl"),
                    cls="sc-stat",
                ),
                Div(
                    Div("0", cls="sc-stat-val", id="sc-s-upcoming"),
                    Div("Upcoming", cls="sc-stat-lbl"),
                    cls="sc-stat",
                ),
                Div(
                    Div("₱0", cls="sc-stat-val", id="sc-s-spent"),
                    Div("Total Spent", cls="sc-stat-lbl"),
                    cls="sc-stat",
                ),
                cls="sc-stats",
            ),
            cls="sc-hero",
        ),

        # ── Now Traveling strip (mobile only, shown by JS if active trip)
        Div(
            Div(cls="sc-now-strip-bg", id="sc-now-bg"),
            Div(cls="sc-now-strip-overlay"),
            Div(
                Div(cls="sc-now-dot"),
                Div(
                    Div("Now Traveling", cls="sc-now-label"),
                    Div("—", cls="sc-now-title", id="sc-now-title"),
                    Div("", cls="sc-now-meta", id="sc-now-meta"),
                    cls="sc-now-info",
                ),
                Div("✈️", cls="sc-now-icon", id="sc-now-icon"),
                cls="sc-now-strip-body",
            ),
            cls="sc-now-strip", id="sc-now-strip",
        ),

        # ── Status tabs ───────────────────────────────────────────────
        Div(
            Div(
                "All",
                Span("0", cls="sc-count-badge", id="sc-badge-all"),
                cls="sc-tab active",
                data_filter="all",
                onclick="scSwitchTab(this,'all')",
            ),
            Div(
                "Upcoming",
                Span("0", cls="sc-count-badge", id="sc-badge-upcoming"),
                cls="sc-tab",
                data_filter="upcoming",
                onclick="scSwitchTab(this,'upcoming')",
            ),
            Div(
                "Active",
                Span("0", cls="sc-count-badge", id="sc-badge-active"),
                cls="sc-tab",
                data_filter="active",
                onclick="scSwitchTab(this,'active')",
            ),
            Div(
                "Completed",
                Span("0", cls="sc-count-badge", id="sc-badge-completed"),
                cls="sc-tab",
                data_filter="completed",
                onclick="scSwitchTab(this,'completed')",
            ),
            cls="sc-tabs",
        ),

        # ── List ──────────────────────────────────────────────────────
        Div(
            Div(id="sc-list", style="min-height:300px"),
            cls="sc-list-wrap",
        ),

        # ── JS ────────────────────────────────────────────────────────
        Script(_SUITCASE_JS),
    )
