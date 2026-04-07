"""
My Suitcase — Crypto/trading terminal style UI.
Data is read from localStorage (saved by the booking wizard confirm step).
"""

from fasthtml.common import Div, Span, A, Script

SUITCASE_CSS = """
/* ══════════════════════════════════════════════════════════════
   SUITCASE — aligned with Gegow teal/beige theme
══════════════════════════════════════════════════════════════ */

.sc-page { background: var(--beige); min-height: 100vh; }

/* ── Hero ── */
.sc-hero {
  background: linear-gradient(160deg, #04111a 0%, #005760 55%, #0a9aa8 100%);
  padding: 22px 16px 24px;
  position: relative; overflow: hidden;
}
@media (min-width: 480px) { .sc-hero { padding: 28px 18px 26px; } }
@media (min-width: 768px) { .sc-hero { padding: 36px 32px 32px; } }
@media (min-width: 1200px){ .sc-hero { padding: 44px 48px 40px; } }
.sc-hero::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
  background-size: 48px 48px;
}
.sc-hero::after {
  content: '';
  position: absolute; bottom: -1px; left: 0; right: 0;
  height: 28px; background: var(--beige);
  border-radius: 20px 20px 0 0;
}
.sc-hero-inner { position: relative; z-index: 1; }

.sc-hero-eyebrow {
  display: inline-flex; align-items: center; gap: 7px;
  font-size: 10px; font-weight: 800; letter-spacing: 2px;
  text-transform: uppercase; color: #5eead4;
  margin-bottom: 10px;
}
.sc-eyebrow-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: #5eead4;
  animation: sc-dot-pulse 1.8s ease-in-out infinite;
}
@keyframes sc-dot-pulse {
  0%,100% { opacity: 1; transform: scale(1); }
  50%      { opacity: .6; transform: scale(1.4); }
}
.sc-hero-title {
  font-size: clamp(22px, 5vw, 28px); font-weight: 900; letter-spacing: -.5px;
  line-height: 1.1; color: #fff; margin-bottom: 4px;
}
.sc-hero-sub { font-size: 12px; color: rgba(255,255,255,.45); }

/* ── Stats ── */
.sc-stats {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 8px; margin-top: 18px; position: relative; z-index: 1;
}
@media (min-width: 480px) { .sc-stats { gap: 10px; margin-top: 22px; } }
@media (max-width: 300px) { .sc-stats { grid-template-columns: 1fr; } }
.sc-stat {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 14px; padding: 13px 10px 11px;
  text-align: center;
  transition: background .2s;
}
.sc-stat:hover { background: rgba(255,255,255,.14); }
.sc-stat-val {
  font-size: clamp(16px, 4vw, 20px); font-weight: 900; color: #fff; line-height: 1;
}
.sc-stat-lbl {
  font-size: clamp(8px, 2vw, 9px); font-weight: 700; text-transform: uppercase;
  letter-spacing: .8px; color: rgba(255,255,255,.4); margin-top: 4px;
}

/* ── Active trip strip ── */
.sc-ticker {
  display: none;
  background: var(--teal-xl);
  border-left: 4px solid var(--teal);
  padding: 12px 16px;
  align-items: center; gap: 12px;
  border-bottom: 1px solid var(--teal-lt);
}
.sc-ticker.show { display: flex; }
.sc-ticker-dot {
  width: 9px; height: 9px; border-radius: 50%;
  background: var(--teal); flex-shrink: 0;
  box-shadow: 0 0 0 3px rgba(0,109,119,.2);
  animation: sc-dot-pulse 1.6s ease-in-out infinite;
}
.sc-ticker-badge {
  font-size: 9px; font-weight: 900; letter-spacing: 1.2px;
  text-transform: uppercase; color: var(--teal);
  background: rgba(0,109,119,.12); border: 1px solid var(--teal-lt);
  padding: 2px 7px; border-radius: 4px; flex-shrink: 0;
}
.sc-ticker-info { flex: 1; min-width: 0; }
.sc-ticker-title {
  font-size: 13px; font-weight: 800; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.sc-ticker-meta { font-size: 10px; color: var(--muted); margin-top: 2px; }
.sc-ticker-icon { font-size: 26px; flex-shrink: 0; }

/* ── Tabs ── */
.sc-tabs {
  display: flex;
  background: #fff;
  border-bottom: 1.5px solid var(--border);
  overflow-x: auto; scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.sc-tabs::-webkit-scrollbar { display: none; }
.sc-tab {
  flex: 1; padding: 11px 4px 10px;
  text-align: center;
  font-size: 11px; font-weight: 600;
  color: var(--muted);
  border-bottom: 2px solid transparent;
  margin-bottom: -1.5px;
  cursor: pointer; white-space: nowrap;
  transition: color .15s, border-color .15s;
  min-width: 60px; user-select: none;
}
@media (min-width: 380px) { .sc-tab { padding: 13px 6px 12px; font-size: 12px; min-width: 72px; } }
.sc-tab:hover { color: var(--text); }
.sc-tab.active { color: var(--teal); border-bottom-color: var(--teal); font-weight: 700; }
.sc-count-badge {
  display: inline-flex; align-items: center; justify-content: center;
  background: rgba(0,109,119,.1); color: var(--teal);
  font-size: 10px; font-weight: 700;
  padding: 1px 6px; border-radius: 10px; margin-left: 4px; min-width: 18px;
}
.sc-tab.active .sc-count-badge { background: var(--teal); color: #fff; }

/* ── List area ── */
.sc-list-wrap {
  padding: 14px 12px 100px;
  background: var(--beige);
  min-height: 60vh;
}
@media (min-width: 480px) { .sc-list-wrap { padding: 16px 16px 110px; } }
@media (min-width: 768px) { .sc-list-wrap { padding: 20px 28px 80px; } }
@media (min-width: 1200px){ .sc-list-wrap { padding: 24px 48px 60px; } }

/* ── Trip card (minimal) ── */
.sc-card {
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 18px;
  overflow: hidden;
  margin-bottom: 12px;
  position: relative;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: transform .18s, box-shadow .18s, border-color .18s;
  -webkit-tap-highlight-color: transparent;
}
.sc-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
  border-color: var(--teal-lt);
}
.sc-card:active { transform: scale(.98); }

/* left accent bar per type */
.sc-card::before {
  content: '';
  position: absolute; top: 0; left: 0; bottom: 0; width: 4px;
  border-radius: 18px 0 0 18px;
}
.sc-card[data-type="flight"]::before { background: linear-gradient(180deg, #0D9488, #0891b2); }
.sc-card[data-type="hotel"]::before  { background: linear-gradient(180deg, #f59e0b, #ef4444); }
.sc-card[data-type="tour"]::before   { background: linear-gradient(180deg, #8b5cf6, #06b6d4); }

/* ── Card inner row ── */
.sc-card-row {
  display: flex; align-items: center; gap: 10px;
  padding: 14px 14px 14px 18px;
}
@media (min-width: 480px) { .sc-card-row { gap: 14px; padding: 16px 16px 16px 20px; } }
.sc-type-icon {
  width: 46px; height: 46px; border-radius: 13px;
  display: flex; align-items: center; justify-content: center;
  font-size: 24px; flex-shrink: 0;
}
.sc-type-icon-flight { background: var(--teal-xl); }
.sc-type-icon-hotel  { background: #FEF3C7; }
.sc-type-icon-tour   { background: #EDE9FE; }

.sc-card-info { flex: 1; min-width: 0; }
.sc-type-label {
  font-size: 9px; font-weight: 800; letter-spacing: 1.6px;
  text-transform: uppercase; color: var(--muted-lt); margin-bottom: 3px;
}
.sc-trip-name {
  font-size: 14px; font-weight: 800; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  line-height: 1.3;
}
.sc-card-date {
  font-size: 11px; color: var(--muted); margin-top: 3px;
}

.sc-card-right {
  display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0;
}
.sc-price { font-size: 17px; font-weight: 900; color: var(--teal); line-height: 1; }
.sc-status-pill {
  padding: 3px 9px; border-radius: 20px;
  font-size: 9px; font-weight: 800; letter-spacing: .4px;
  text-transform: uppercase; white-space: nowrap;
}
.sc-status-upcoming  { background: #DBEAFE; color: #1E40AF; }
.sc-status-active    {
  background: var(--teal-xl); color: var(--teal-dk);
  animation: sc-pill-pulse 2.4s ease-in-out infinite;
}
@keyframes sc-pill-pulse {
  0%,100% { box-shadow: 0 0 0 0 rgba(0,109,119,.0); }
  50%      { box-shadow: 0 0 0 4px rgba(0,109,119,.15); }
}
.sc-status-completed { background: #F1F5F9; color: #64748B; }
.sc-chevron { font-size: 13px; color: var(--muted-lt); }

/* ── Modal overlay ── */
.sc-modal-overlay {
  display: none;
  position: fixed; inset: 0; z-index: 600;
  background: rgba(0,0,0,.5);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  align-items: flex-end;
  justify-content: center;
}
.sc-modal-overlay.open { display: flex; }

@media (min-width: 600px) {
  .sc-modal-overlay { align-items: center; }
}

/* ── Modal sheet ── */
.sc-modal {
  width: 100%; max-width: 520px;
  background: #fff;
  border-radius: 24px 24px 0 0;
  overflow: hidden;
  max-height: 92dvh;
  display: flex; flex-direction: column;
  transform: translateY(100%);
  transition: transform .35s cubic-bezier(.32,0,.67,0);
}
.sc-modal-overlay.open .sc-modal {
  transform: translateY(0);
  transition: transform .35s cubic-bezier(.33,1,.68,1);
}
@media (min-width: 600px) {
  .sc-modal {
    border-radius: 24px;
    max-height: 88dvh;
    transform: translateY(20px) scale(.96);
    opacity: 0;
    transition: transform .3s cubic-bezier(.33,1,.68,1), opacity .3s ease;
  }
  .sc-modal-overlay.open .sc-modal {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

/* drag handle */
.sc-modal-handle {
  width: 36px; height: 4px; border-radius: 2px;
  background: rgba(0,0,0,.12);
  margin: 10px auto 0;
  flex-shrink: 0;
}

/* ── Modal hero ── */
.sc-modal-hero {
  padding: 20px 20px 18px;
  display: flex; align-items: flex-start; gap: 14px;
  flex-shrink: 0;
}
.sc-modal-icon {
  width: 52px; height: 52px; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  font-size: 28px; flex-shrink: 0;
}
.sc-modal-hero-text { flex: 1; min-width: 0; }
.sc-modal-type { font-size: 9px; font-weight: 800; letter-spacing: 1.8px; text-transform: uppercase; color: var(--muted-lt); margin-bottom: 4px; }
.sc-modal-title { font-size: 18px; font-weight: 900; color: var(--text); line-height: 1.2; }
.sc-modal-ref { font-size: 11px; color: var(--muted-lt); margin-top: 5px; }
.sc-modal-close {
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--beige); border: none;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; color: var(--muted); cursor: pointer;
  flex-shrink: 0; margin-top: 2px;
  transition: background .15s, color .15s;
}
.sc-modal-close:hover { background: #FEE2E2; color: #DC2626; }

/* ── Modal body (scrollable) ── */
.sc-modal-body {
  flex: 1; overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 0 20px 8px;
}

/* Divider */
.sc-modal-divider {
  height: 1px; background: var(--border);
  margin: 0 -20px 16px;
}

/* Date strip */
.sc-modal-dates {
  display: flex; align-items: stretch; gap: 0;
  background: var(--beige); border-radius: 14px;
  overflow: hidden; margin-bottom: 16px;
  border: 1px solid var(--border);
}
.sc-modal-date-block {
  flex: 1; padding: 12px 14px; min-width: 0;
}
.sc-modal-date-block + .sc-modal-date-block {
  border-left: 1px solid var(--border);
}
.sc-modal-date-lbl {
  font-size: 9px; font-weight: 800; text-transform: uppercase;
  letter-spacing: .8px; color: var(--muted-lt); margin-bottom: 4px;
}
.sc-modal-date-val { font-size: 13px; font-weight: 800; color: var(--text); }
.sc-modal-date-sub { font-size: 10px; color: var(--muted); margin-top: 2px; }

/* Chips row */
.sc-modal-chips {
  display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;
}
.sc-chip {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 6px 12px; border-radius: 20px;
  font-size: 11px; font-weight: 700;
}
.sc-chip-teal      { background: var(--teal-xl); color: var(--teal-dk); border: 1px solid var(--teal-lt); }
.sc-chip-blue      { background: #DBEAFE; color: #1E40AF; border: 1px solid #BFDBFE; }
.sc-chip-amber     { background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
.sc-chip-violet    { background: #EDE9FE; color: #5B21B6; border: 1px solid #DDD6FE; }
.sc-chip-slate     { background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; }

/* Details list */
.sc-modal-details {
  display: flex; flex-direction: column; gap: 0;
  border: 1px solid var(--border); border-radius: 14px;
  overflow: hidden; margin-bottom: 16px;
}
.sc-detail-row {
  display: flex; align-items: center; justify-content: space-between;
  padding: 11px 14px; gap: 12px;
  border-bottom: 1px solid var(--border);
}
.sc-detail-row:last-child { border-bottom: none; }
.sc-detail-lbl { font-size: 12px; color: var(--muted); }
.sc-detail-val { font-size: 12px; font-weight: 700; color: var(--text); text-align: right; }

/* Price hero */
.sc-modal-price-row {
  display: flex; align-items: center; justify-content: space-between;
  background: linear-gradient(135deg, var(--teal-xl), #e0f7f5);
  border: 1px solid var(--teal-lt);
  border-radius: 14px; padding: 14px 16px;
  margin-bottom: 16px;
}
.sc-modal-price-big { font-size: 26px; font-weight: 900; color: var(--teal); line-height: 1; }
.sc-modal-price-sub { font-size: 11px; color: var(--muted); margin-top: 4px; }

/* ── Modal footer (actions) ── */
.sc-modal-foot {
  padding: 14px 20px calc(env(safe-area-inset-bottom, 0px) + 14px);
  border-top: 1px solid var(--border);
  display: flex; gap: 10px;
  flex-shrink: 0; background: #fff;
}
.sc-btn-rebook {
  flex: 1; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  padding: 13px 16px;
  background: linear-gradient(135deg, var(--teal), var(--teal-dk)); color: #fff;
  font-size: 14px; font-weight: 800;
  border-radius: 12px; text-decoration: none; border: none; cursor: pointer;
  box-shadow: 0 4px 14px rgba(0,109,119,.3);
  transition: opacity .15s, transform .1s;
}
.sc-btn-rebook:hover { opacity: .9; transform: translateY(-1px); }
.sc-btn-rebook:active { transform: scale(.97); }
.sc-btn-delete {
  width: 48px; height: 48px;
  display: flex; align-items: center; justify-content: center;
  background: transparent; border: 1.5px solid var(--border);
  border-radius: 12px; color: var(--muted-lt);
  font-size: 16px; cursor: pointer; transition: all .15s; flex-shrink: 0;
}
.sc-btn-delete:hover { background: #FEF2F2; border-color: #FECACA; color: #DC2626; }

/* ── Empty state ── */
.sc-empty { text-align: center; padding: 64px 24px 40px; }
.sc-empty-icon { font-size: 68px; margin-bottom: 16px; line-height: 1; opacity: .7; }
.sc-empty-title { font-size: 19px; font-weight: 800; color: var(--text); margin-bottom: 8px; }
.sc-empty-sub   { font-size: 13px; color: var(--muted); line-height: 1.65; max-width: 280px; margin: 0 auto 28px; }
.sc-empty-cta {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--teal); color: #fff;
  padding: 12px 26px; border-radius: 12px;
  font-size: 14px; font-weight: 800; text-decoration: none;
  box-shadow: 0 4px 16px rgba(0,109,119,.25);
  transition: background .15s, transform .15s;
}
.sc-empty-cta:hover { background: var(--teal-dk); transform: translateY(-1px); }

/* ── FAB ── */
.sc-fab {
  display: none;
  position: fixed; bottom: 80px; right: 16px; z-index: 300;
  align-items: center; gap: 8px;
  background: var(--teal); color: #fff;
  padding: 13px 18px 13px 14px; border-radius: 50px;
  box-shadow: 0 6px 20px rgba(0,109,119,.35);
  font-size: 14px; font-weight: 800; text-decoration: none;
  -webkit-tap-highlight-color: transparent;
  transition: transform .15s, box-shadow .15s;
}
.sc-fab:active { transform: scale(.95); }
.sc-fab-icon { font-size: 18px; line-height: 1; }

/* ── Mobile ── */
@media (max-width: 767px) {
  .sc-fab { display: flex; }
  .sc-hero { padding: 22px 16px 22px; }
  .sc-hero-title { font-size: 24px; }
  .sc-stats { gap: 8px; margin-top: 18px; }
  .sc-ticker.show { display: flex; }
  .sc-list-wrap { padding: 12px 12px 110px; }
  .sc-card { border-radius: 16px; }
  .sc-card:hover { transform: none; }
  .sc-card:active { background: #fafaf8; }
}
"""


_SUITCASE_JS = r"""
(function() {
  var KEY = 'gegow_suitcase';

  /* ── Helpers ── */
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch(e) { return []; }
  }
  function save(trips) { localStorage.setItem(KEY, JSON.stringify(trips)); }

  function getStatus(dateFrom, dateTo) {
    var today = new Date(); today.setHours(0,0,0,0);
    var from  = new Date(dateFrom || '9999-01-01');
    var to    = new Date(dateTo   || dateFrom || '9999-01-01');
    if (from > today) return 'upcoming';
    if (to   >= today) return 'active';
    return 'completed';
  }

  function fmtDate(d) {
    if (!d) return '\u2014';
    var dt = new Date(d);
    if (isNaN(dt)) return d;
    return dt.toLocaleDateString('en-PH', { month: 'short', day: 'numeric', year: 'numeric' });
  }

  function fmtDay(d) {
    if (!d) return '';
    var dt = new Date(d);
    if (isNaN(dt)) return '';
    return dt.toLocaleDateString('en-PH', { weekday: 'short' });
  }

  function peso(n) {
    var v = parseInt(n) || 0;
    return '\u20b1' + v.toLocaleString();
  }

  function nights(from, to) {
    if (!from || !to) return 1;
    var n = Math.round((new Date(to) - new Date(from)) / 86400000);
    return Math.max(1, n);
  }

  function daysUntil(dateFrom) {
    if (!dateFrom) return null;
    var today = new Date(); today.setHours(0,0,0,0);
    var diff  = Math.round((new Date(dateFrom) - today) / 86400000);
    if (diff < 0)   return null;
    if (diff === 0) return 'TODAY';
    if (diff === 1) return 'TOMORROW';
    return diff + ' days away';
  }

  var TYPE_ICON  = { flight: '\u2708\ufe0f', hotel: '\ud83c\udfe8', tour: '\ud83d\uddfa\ufe0f' };
  var TYPE_LABEL = { flight: 'Flight', hotel: 'Hotel Stay', tour: 'Tour Package' };
  var DATE_LABEL = {
    flight: ['Departure', 'Return'],
    hotel:  ['Check-in',  'Check-out'],
    tour:   ['Start Date','End Date'],
  };
  var STATUS_MAP = {
    upcoming:  { cls: 'sc-status-upcoming',  txt: '\ud83d\uddd3 Upcoming' },
    active:    { cls: 'sc-status-active',     txt: '\u2708 On Trip'        },
    completed: { cls: 'sc-status-completed',  txt: '\u2713 Completed'      },
  };

  /* ── Minimal card HTML ── */
  function cardHTML(b, idx) {
    var st   = getStatus(b.date_from, b.date_to);
    var sp   = STATUS_MAP[st] || STATUS_MAP.completed;
    var typ  = (b.trip_type || 'flight').toLowerCase();
    var icon = TYPE_ICON[typ] || '\ud83e\uddf3';
    var label = b.label || ((typ.charAt(0).toUpperCase() + typ.slice(1)) + ' Booking');
    var dl   = DATE_LABEL[typ] || ['From', 'To'];
    var dateLine = dl[0] + ': ' + fmtDate(b.date_from)
      + (b.date_to ? '  \u2192  ' + dl[1] + ': ' + fmtDate(b.date_to) : '');

    return '<div class="sc-card" data-status="' + st + '" data-type="' + typ + '" onclick="scOpenModal(' + idx + ')">'
      + '<div class="sc-card-row">'
        + '<div class="sc-type-icon sc-type-icon-' + typ + '">' + icon + '</div>'
        + '<div class="sc-card-info">'
          + '<div class="sc-type-label">' + (TYPE_LABEL[typ] || typ) + '</div>'
          + '<div class="sc-trip-name">' + label + '</div>'
          + '<div class="sc-card-date">' + dateLine + '</div>'
        + '</div>'
        + '<div class="sc-card-right">'
          + '<div class="sc-price">' + peso(b.total) + '</div>'
          + '<span class="sc-status-pill ' + sp.cls + '">' + sp.txt + '</span>'
          + '<span class="sc-chevron">\u203a</span>'
        + '</div>'
      + '</div>'
    + '</div>';
  }

  /* ── Modal content builder ── */
  function buildModal(b, idx) {
    var st   = getStatus(b.date_from, b.date_to);
    var sp   = STATUS_MAP[st] || STATUS_MAP.completed;
    var typ  = (b.trip_type || 'flight').toLowerCase();
    var icon = TYPE_ICON[typ] || '\ud83e\uddf3';
    var label = b.label || ((typ.charAt(0).toUpperCase() + typ.slice(1)) + ' Booking');
    var ref   = b.ref || '\u2014';
    var dl    = DATE_LABEL[typ] || ['From', 'To'];
    var n     = nights(b.date_from, b.date_to);
    var pax   = (parseInt(b.adults) || 1) + (parseInt(b.children) || 0);
    var adults   = parseInt(b.adults)   || 1;
    var children = parseInt(b.children) || 0;
    var durationTxt = n + (typ === 'hotel' ? ' night' : ' day') + (n !== 1 ? 's' : '');
    var countdown  = (st === 'upcoming') ? daysUntil(b.date_from) : null;
    var priceEach  = pax > 0 ? Math.round((parseInt(b.total) || 0) / pax) : (parseInt(b.total) || 0);

    /* chips */
    var chips = '<span class="sc-chip sc-chip-teal">' + durationTxt + '</span>';
    if (countdown) chips += '<span class="sc-chip sc-chip-blue">\u23f0 ' + countdown + '</span>';
    chips += '<span class="sc-chip sc-chip-' + (st==='completed'?'slate':st==='active'?'teal':'blue') + '">' + sp.txt + '</span>';
    if (typ === 'flight' && b.airline)  chips += '<span class="sc-chip sc-chip-amber">\u2708 ' + b.airline + '</span>';
    if (typ === 'hotel'  && b.stars)    chips += '<span class="sc-chip sc-chip-amber">' + '\u2605'.repeat(parseInt(b.stars)||3) + '</span>';
    if (typ === 'tour'   && b.includes) chips += '<span class="sc-chip sc-chip-violet">' + b.includes.split('|')[0] + '</span>';

    /* detail rows */
    var details = '';
    if (b.airline)       details += row('Airline',     b.airline);
    if (b.origin)        details += row('From',        b.origin);
    if (b.destination)   details += row('To',          b.destination);
    if (b.hotel_name)    details += row('Hotel',       b.hotel_name);
    if (b.city)          details += row('City',        b.city);
    if (b.location)      details += row('Location',    b.location);
    if (b.tour_name || b.name) details += row('Package', b.tour_name || b.name);
    details += row('Travelers', pax + ' (' + adults + ' adult' + (adults!==1?'s':'') + (children?' · '+children+' child'+( children!==1?'ren':''):'') + ')');
    if (b.class_type)    details += row('Class',       b.class_type);
    if (b.meal)          details += row('Meal',        b.meal);
    if (b.rooms)         details += row('Rooms',       b.rooms);
    details += row('Booking ID', 'GGW-' + ref);

    var m = document.getElementById('sc-modal');
    m.querySelector('.sc-modal-type').textContent  = TYPE_LABEL[typ] || typ;
    m.querySelector('.sc-modal-icon').textContent  = icon;
    m.querySelector('.sc-modal-icon').className    = 'sc-modal-icon sc-type-icon-' + typ;
    m.querySelector('.sc-modal-title').textContent = label;
    m.querySelector('.sc-modal-ref').textContent   = 'Booking ID: GGW-' + ref;

    /* dates */
    var datesEl = m.querySelector('.sc-modal-dates');
    datesEl.innerHTML =
      '<div class="sc-modal-date-block">'
        + '<div class="sc-modal-date-lbl">' + dl[0] + '</div>'
        + '<div class="sc-modal-date-val">' + fmtDate(b.date_from) + '</div>'
        + '<div class="sc-modal-date-sub">' + fmtDay(b.date_from) + '</div>'
      + '</div>'
      + (b.date_to
        ? '<div class="sc-modal-date-block">'
            + '<div class="sc-modal-date-lbl">' + dl[1] + '</div>'
            + '<div class="sc-modal-date-val">' + fmtDate(b.date_to) + '</div>'
            + '<div class="sc-modal-date-sub">' + fmtDay(b.date_to) + '</div>'
          + '</div>'
        : '');

    m.querySelector('.sc-modal-chips').innerHTML   = chips;
    m.querySelector('.sc-modal-details').innerHTML = details;

    m.querySelector('.sc-modal-price-big').textContent = peso(b.total);
    m.querySelector('.sc-modal-price-sub').textContent =
      pax + ' traveler' + (pax!==1?'s':'') + (pax>1 ? '  ·  ' + peso(priceEach) + ' each' : '');

    /* wire delete button */
    m.querySelector('.sc-btn-delete').onclick = function() {
      scDeleteTrip(ref);
      scCloseModal();
    };
  }

  function row(label, val) {
    return '<div class="sc-detail-row">'
      + '<span class="sc-detail-lbl">' + label + '</span>'
      + '<span class="sc-detail-val">' + val + '</span>'
    + '</div>';
  }

  /* ── Modal open / close ── */
  var _currentTrips = [];

  window.scOpenModal = function(idx) {
    var b = _currentTrips[idx];
    if (!b) return;
    buildModal(b, idx);
    document.getElementById('sc-modal-overlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.scCloseModal = function() {
    document.getElementById('sc-modal-overlay').classList.remove('open');
    document.body.style.overflow = '';
  };

  /* close on overlay click */
  document.addEventListener('DOMContentLoaded', function() {
    var overlay = document.getElementById('sc-modal-overlay');
    if (overlay) {
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) scCloseModal();
      });
    }
    /* close on Escape */
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') scCloseModal();
    });
  });

  /* ── Empty state ── */
  function emptyHTML(filter) {
    var cfg = {
      all:       { icon: '\ud83e\uddf3', title: 'Your suitcase is empty',   sub: 'Complete a booking to see your trips here — stored offline, always available.' },
      upcoming:  { icon: '\ud83d\uddd3\ufe0f', title: 'No upcoming trips',  sub: 'Nothing booked ahead yet. Start planning your next adventure!' },
      active:    { icon: '\u2708\ufe0f', title: "You're not traveling now", sub: 'No active trips at the moment. Book one today!' },
      completed: { icon: '\ud83c\udfc1', title: 'No completed trips yet',   sub: 'Past trips will appear here once your travel dates pass.' },
    };
    var c = cfg[filter] || cfg.all;
    return '<div class="sc-empty">'
      + '<div class="sc-empty-icon">' + c.icon + '</div>'
      + '<div class="sc-empty-title">' + c.title + '</div>'
      + '<div class="sc-empty-sub">' + c.sub + '</div>'
      + (filter === 'all' ? '<a href="/book" class="sc-empty-cta">Book a Trip \u2192</a>' : '')
    + '</div>';
  }

  /* ── Stats / badges / ticker ── */
  function updateStats(trips) {
    var upcoming = trips.filter(function(t){ return getStatus(t.date_from,t.date_to)==='upcoming'; }).length;
    var total    = trips.reduce(function(s,t){ return s+(parseInt(t.total)||0); }, 0);
    var el = function(id){ return document.getElementById(id); };
    if (el('sc-s-trips'))    el('sc-s-trips').textContent    = trips.length;
    if (el('sc-s-upcoming')) el('sc-s-upcoming').textContent = upcoming;
    if (el('sc-s-spent'))    el('sc-s-spent').textContent    = '\u20b1' + total.toLocaleString();
  }

  function updateBadges(trips) {
    var counts = { all: trips.length, upcoming:0, active:0, completed:0 };
    trips.forEach(function(t){ var s=getStatus(t.date_from,t.date_to); counts[s]=(counts[s]||0)+1; });
    ['all','upcoming','active','completed'].forEach(function(s){
      var el = document.getElementById('sc-badge-'+s);
      if (el) el.textContent = counts[s];
    });
  }

  function updateTicker(trips) {
    var ticker = document.getElementById('sc-ticker');
    if (!ticker) return;
    var active = trips.find(function(t){ return getStatus(t.date_from,t.date_to)==='active'; });
    if (!active) { ticker.classList.remove('show'); return; }
    ticker.classList.add('show');
    var typ = (active.trip_type||'flight').toLowerCase();
    var n   = nights(active.date_from, active.date_to);
    var pax = (parseInt(active.adults)||1)+(parseInt(active.children)||0);
    var te = document.getElementById('sc-ticker-title');
    var me = document.getElementById('sc-ticker-meta');
    var ie = document.getElementById('sc-ticker-icon');
    if (te) te.textContent = active.label || (typ + ' Booking');
    if (ie) ie.textContent = TYPE_ICON[typ] || '\u2708\ufe0f';
    if (me) me.textContent = fmtDate(active.date_from)+' \u2013 '+fmtDate(active.date_to)
      +'  \u00b7  '+pax+' pax  \u00b7  '+n+' night'+(n!==1?'s':'');
  }

  /* ── Render list ── */
  function render(filter) {
    var list = document.getElementById('sc-list');
    if (!list) return;
    var trips = load();
    updateStats(trips);
    updateBadges(trips);
    updateTicker(trips);
    var filtered = filter === 'all' ? trips : trips.filter(function(t){
      return getStatus(t.date_from,t.date_to) === filter;
    });
    /* store for modal lookups — filtered indices */
    _currentTrips = filtered;
    list.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : emptyHTML(filter);
  }

  /* ── Public API ── */
  window.scSwitchTab = function(el, filter) {
    document.querySelectorAll('.sc-tab').forEach(function(t){ t.classList.remove('active'); });
    el.classList.add('active');
    render(filter);
  };

  window.scDeleteTrip = function(ref) {
    var trips = load().filter(function(t){ return String(t.ref) !== String(ref); });
    save(trips);
    var active = document.querySelector('.sc-tab.active');
    render(active ? active.dataset.filter : 'all');
  };

  window.saveToSuitcase = function(booking) {
    var trips = load();
    trips.unshift(booking);
    save(trips);
  };

  /* ── Init ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function(){ render('all'); });
  } else {
    render('all');
  }
})();
"""


def suitcase_page() -> Div:
    return Div(
        # ── FAB ───────────────────────────────────────────────────────
        A(
            Span("✈", cls="sc-fab-icon"),
            "Book a Trip",
            href="/book",
            cls="sc-fab",
            title="Book a new trip",
        ),

        Div(
            # ── Hero ──────────────────────────────────────────────────
            Div(
                Div(
                    # eyebrow
                    Div(
                        Div(cls="sc-eyebrow-dot"),
                        "TRAVEL PORTFOLIO",
                        cls="sc-hero-eyebrow",
                    ),
                    Div("My Suitcase", cls="sc-hero-title"),
                    Div(
                        "Flights · Hotels · Tours  ·  offline-ready",
                        cls="sc-hero-sub",
                    ),
                    # Stats
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
                            Div("Portfolio Value", cls="sc-stat-lbl"),
                            cls="sc-stat",
                        ),
                        cls="sc-stats",
                    ),
                    cls="sc-hero-inner",
                ),
                cls="sc-hero",
            ),

            # ── Live ticker (active trip, shown by JS) ─────────────────
            Div(
                Div(cls="sc-ticker-dot"),
                Span("LIVE", cls="sc-ticker-badge"),
                Div(
                    Div("—", cls="sc-ticker-title", id="sc-ticker-title"),
                    Div("", cls="sc-ticker-meta", id="sc-ticker-meta"),
                    cls="sc-ticker-info",
                ),
                Div("✈️", cls="sc-ticker-icon", id="sc-ticker-icon"),
                cls="sc-ticker",
                id="sc-ticker",
            ),

            # ── Tabs ───────────────────────────────────────────────────
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

            # ── List ──────────────────────────────────────────────────
            Div(
                Div(id="sc-list", style="min-height:280px"),
                cls="sc-list-wrap",
            ),

            cls="sc-page",
        ),

        # ── Trip detail modal ─────────────────────────────────────────
        Div(
            Div(
                # drag handle
                Div(cls="sc-modal-handle"),
                # hero row
                Div(
                    Div("✈️", cls="sc-modal-icon sc-type-icon-flight"),
                    Div(
                        Div("Flight", cls="sc-modal-type"),
                        Div("Trip Details", cls="sc-modal-title"),
                        Div("Booking ID: GGW-—", cls="sc-modal-ref"),
                        cls="sc-modal-hero-text",
                    ),
                    Span("✕", cls="sc-modal-close", onclick="scCloseModal()"),
                    cls="sc-modal-hero",
                ),
                # scrollable body
                Div(
                    Div(cls="sc-modal-divider"),
                    # dates
                    Div(cls="sc-modal-dates"),
                    # chips
                    Div(cls="sc-modal-chips"),
                    # price
                    Div(
                        Div(
                            Div("₱0", cls="sc-modal-price-big"),
                            Div("1 traveler", cls="sc-modal-price-sub"),
                        ),
                        cls="sc-modal-price-row",
                    ),
                    # details
                    Div(cls="sc-modal-details"),
                    cls="sc-modal-body",
                ),
                # footer actions
                Div(
                    Span("↺ Rebook Similar", href="/book", cls="sc-btn-rebook",
                         onclick="scCloseModal(); window.location='/book'"),
                    Span("🗑", cls="sc-btn-delete"),
                    cls="sc-modal-foot",
                ),
                cls="sc-modal",
                id="sc-modal",
            ),
            cls="sc-modal-overlay",
            id="sc-modal-overlay",
        ),

        # ── JS ────────────────────────────────────────────────────────
        Script(_SUITCASE_JS),
    )
