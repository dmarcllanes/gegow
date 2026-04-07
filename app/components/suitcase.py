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
  padding: 28px 18px 26px;
  position: relative; overflow: hidden;
}
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
  font-size: 28px; font-weight: 900; letter-spacing: -.5px;
  line-height: 1.1; color: #fff; margin-bottom: 4px;
}
.sc-hero-sub { font-size: 12px; color: rgba(255,255,255,.45); }

/* ── Stats ── */
.sc-stats {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 10px; margin-top: 22px; position: relative; z-index: 1;
}
.sc-stat {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 14px; padding: 13px 10px 11px;
  text-align: center;
  transition: background .2s;
}
.sc-stat:hover { background: rgba(255,255,255,.14); }
.sc-stat-val {
  font-size: 20px; font-weight: 900; color: #fff; line-height: 1;
}
.sc-stat-lbl {
  font-size: 9px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1px; color: rgba(255,255,255,.4); margin-top: 4px;
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
  flex: 1; padding: 13px 6px 12px;
  text-align: center;
  font-size: 12px; font-weight: 600;
  color: var(--muted);
  border-bottom: 2px solid transparent;
  margin-bottom: -1.5px;
  cursor: pointer; white-space: nowrap;
  transition: color .15s, border-color .15s;
  min-width: 72px; user-select: none;
}
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
  padding: 16px 16px 110px;
  background: var(--beige);
  min-height: 60vh;
}

/* ── Trip card ── */
.sc-card {
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 14px;
  position: relative;
  box-shadow: var(--shadow-sm);
  transition: transform .15s, box-shadow .15s, border-color .15s;
}
.sc-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--teal-lt);
}
/* top accent per type */
.sc-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  border-radius: 20px 20px 0 0;
}
.sc-card[data-type="flight"]::before { background: linear-gradient(90deg, #0D9488, #0891b2); }
.sc-card[data-type="hotel"]::before  { background: linear-gradient(90deg, #f59e0b, #ef4444); }
.sc-card[data-type="tour"]::before   { background: linear-gradient(90deg, #8b5cf6, #06b6d4); }

/* ── Card head ── */
.sc-card-head {
  display: flex; align-items: flex-start; gap: 13px;
  padding: 18px 16px 14px; position: relative;
}
.sc-type-icon {
  width: 48px; height: 48px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 26px; flex-shrink: 0;
}
.sc-type-icon-flight { background: var(--teal-xl); }
.sc-type-icon-hotel  { background: #FEF3C7; }
.sc-type-icon-tour   { background: #EDE9FE; }

.sc-head-body { flex: 1; min-width: 0; }
.sc-type-label {
  font-size: 9px; font-weight: 800; letter-spacing: 1.8px;
  text-transform: uppercase; color: var(--muted-lt); margin-bottom: 4px;
}
.sc-trip-name {
  font-size: 15px; font-weight: 800; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  line-height: 1.25;
}
.sc-ref-id {
  font-size: 10px; color: var(--muted-lt);
  letter-spacing: .3px; margin-top: 4px;
}

/* ── Status pill ── */
.sc-status-pill {
  position: absolute; top: 16px; right: 14px;
  padding: 4px 10px; border-radius: 20px;
  font-size: 10px; font-weight: 800; letter-spacing: .3px;
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

/* ── Date row ── */
.sc-date-row {
  display: flex; align-items: center; gap: 10px;
  padding: 11px 16px;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  background: var(--beige);
}
.sc-date-block { flex: 1; min-width: 0; }
.sc-date-lbl {
  font-size: 8px; font-weight: 800; text-transform: uppercase;
  letter-spacing: .8px; color: var(--muted-lt); margin-bottom: 3px;
}
.sc-date-val { font-size: 13px; font-weight: 700; color: var(--text); }
.sc-date-arrow { font-size: 14px; color: var(--teal); flex-shrink: 0; }
.sc-duration-chip {
  background: var(--teal-xl); color: var(--teal-dk);
  border: 1px solid var(--teal-lt);
  font-size: 10px; font-weight: 700; white-space: nowrap;
  padding: 4px 10px; border-radius: 10px; flex-shrink: 0;
}
.sc-countdown-chip {
  background: #DBEAFE; color: #1E40AF;
  border: 1px solid #BFDBFE;
  font-size: 10px; font-weight: 700; white-space: nowrap;
  padding: 4px 10px; border-radius: 10px; flex-shrink: 0;
}

/* ── Card footer ── */
.sc-card-foot {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px 14px; background: #fff;
}
.sc-price { font-size: 22px; font-weight: 900; color: var(--teal); line-height: 1; }
.sc-price-sub { font-size: 10px; color: var(--muted); margin-top: 3px; }
.sc-foot-actions { display: flex; gap: 8px; align-items: center; }
.sc-btn-rebook {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 8px 16px;
  background: var(--teal); color: #fff;
  font-size: 12px; font-weight: 800;
  border-radius: 10px; text-decoration: none; border: none; cursor: pointer;
  transition: background .15s, transform .15s;
}
.sc-btn-rebook:hover { background: var(--teal-dk); transform: translateY(-1px); }
.sc-btn-delete {
  width: 34px; height: 34px;
  display: flex; align-items: center; justify-content: center;
  background: transparent; border: 1.5px solid var(--border);
  border-radius: 9px; color: var(--muted-lt);
  font-size: 12px; cursor: pointer; transition: all .15s;
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

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); }
    catch(e) { return []; }
  }

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
    var from  = new Date(dateFrom);
    var diff  = Math.round((from - today) / 86400000);
    if (diff < 0)   return null;
    if (diff === 0) return 'TODAY';
    if (diff === 1) return 'TOMORROW';
    return 'IN ' + diff + ' DAYS';
  }

  var TYPE_ICON = { flight: '\u2708\ufe0f', hotel: '\ud83c\udfe8', tour: '\ud83d\uddfa\ufe0f' };
  var TYPE_LABEL = { flight: 'Flight', hotel: 'Hotel Stay', tour: 'Tour Package' };
  var DATE_LABEL = {
    flight: ['Departure', 'Return'],
    hotel:  ['Check-in',  'Check-out'],
    tour:   ['Start',     'End'],
  };
  var STATUS_MAP = {
    upcoming:  { cls: 'sc-status-upcoming',  txt: '\ud83d\uddd3 Upcoming'  },
    active:    { cls: 'sc-status-active',     txt: '\u2708\ufe0f On Trip'   },
    completed: { cls: 'sc-status-completed',  txt: '\u2713 Completed'       },
  };

  function cardHTML(b) {
    var st   = getStatus(b.date_from, b.date_to);
    var sp   = STATUS_MAP[st] || STATUS_MAP.completed;
    var typ  = (b.trip_type || 'flight').toLowerCase();
    var icon = TYPE_ICON[typ] || '\ud83e\uddf3';
    var n    = nights(b.date_from, b.date_to);
    var pax  = (parseInt(b.adults) || 1) + (parseInt(b.children) || 0);
    var label = b.label || ((typ.charAt(0).toUpperCase() + typ.slice(1)) + ' Booking');
    var ref   = b.ref || '\u2014';
    var dl    = DATE_LABEL[typ] || ['From', 'To'];
    var durationTxt = n + (typ === 'flight' ? ' day' : ' night') + (n !== 1 ? 's' : '');
    var countdown = (st === 'upcoming') ? daysUntil(b.date_from) : null;
    var chipHTML = countdown
      ? '<span class="sc-countdown-chip">\u23f0 ' + countdown + '</span>'
      : '<span class="sc-duration-chip">' + durationTxt + '</span>';
    var iconClass = 'sc-type-icon sc-type-icon-' + typ;

    return '<div class="sc-card" data-status="' + st + '" data-type="' + typ + '">'
      + '<div class="sc-card-head">'
        + '<div class="' + iconClass + '">' + icon + '</div>'
        + '<div class="sc-head-body">'
          + '<div class="sc-type-label">' + (TYPE_LABEL[typ] || typ) + '</div>'
          + '<div class="sc-trip-name">' + label + '</div>'
          + '<div class="sc-ref-id">ID: GGW-' + ref + '</div>'
        + '</div>'
        + '<span class="sc-status-pill ' + sp.cls + '">' + sp.txt + '</span>'
      + '</div>'
      + '<div class="sc-date-row">'
        + '<div class="sc-date-block">'
          + '<div class="sc-date-lbl">' + dl[0] + '</div>'
          + '<div class="sc-date-val">' + fmtDate(b.date_from) + '</div>'
        + '</div>'
        + '<div class="sc-date-arrow">\u2192</div>'
        + '<div class="sc-date-block">'
          + '<div class="sc-date-lbl">' + dl[1] + '</div>'
          + '<div class="sc-date-val">' + (fmtDate(b.date_to) || '\u2014') + '</div>'
        + '</div>'
        + chipHTML
      + '</div>'
      + '<div class="sc-card-foot">'
        + '<div class="sc-price-block">'
          + '<div class="sc-price">' + peso(b.total) + '</div>'
          + '<div class="sc-price-sub">' + pax + ' traveler' + (pax !== 1 ? 's' : '') + '</div>'
        + '</div>'
        + '<div class="sc-foot-actions">'
          + '<a href="/book" class="sc-btn-rebook">\u21ba Rebook</a>'
          + '<button class="sc-btn-delete" onclick="scDeleteTrip(\'' + ref + '\')" title="Remove">\u2715</button>'
        + '</div>'
      + '</div>'
    + '</div>';
  }

  function emptyHTML(filter) {
    var cfg = {
      all:       { icon: '\ud83e\uddf3', title: 'Your suitcase is empty',    sub: 'Complete a booking to see your trips here — stored offline, always available.' },
      upcoming:  { icon: '\ud83d\uddd3\ufe0f', title: 'No upcoming trips',   sub: 'Nothing booked ahead yet. Start planning your next adventure!' },
      active:    { icon: '\u2708\ufe0f', title: "You're not traveling now",  sub: "No active trips at the moment. Book one today!" },
      completed: { icon: '\ud83c\udfc1', title: 'No completed trips yet',    sub: 'Past trips will appear here once your travel dates pass.' },
    };
    var c = cfg[filter] || cfg.all;
    var cta = (filter === 'all')
      ? '<a href="/book" class="sc-empty-cta">Book a Trip \u2192</a>'
      : '';
    return '<div class="sc-empty">'
      + '<div class="sc-empty-icon">' + c.icon + '</div>'
      + '<div class="sc-empty-title">' + c.title + '</div>'
      + '<div class="sc-empty-sub">' + c.sub + '</div>'
      + cta
    + '</div>';
  }

  function updateStats(trips) {
    var upcoming = trips.filter(function(t){ return getStatus(t.date_from, t.date_to) === 'upcoming'; }).length;
    var total = trips.reduce(function(s, t){ return s + (parseInt(t.total) || 0); }, 0);
    function el(id) { return document.getElementById(id); }
    if (el('sc-s-trips'))    el('sc-s-trips').textContent    = trips.length;
    if (el('sc-s-upcoming')) el('sc-s-upcoming').textContent = upcoming;
    if (el('sc-s-spent'))    el('sc-s-spent').textContent    = '\u20b1' + total.toLocaleString();
  }

  function updateBadges(trips) {
    var counts = { all: trips.length, upcoming: 0, active: 0, completed: 0 };
    trips.forEach(function(t) {
      var s = getStatus(t.date_from, t.date_to);
      counts[s] = (counts[s] || 0) + 1;
    });
    ['all','upcoming','active','completed'].forEach(function(s) {
      var el = document.getElementById('sc-badge-' + s);
      if (el) el.textContent = counts[s];
    });
  }

  function updateTicker(trips) {
    var ticker = document.getElementById('sc-ticker');
    if (!ticker) return;
    var active = trips.find(function(t){ return getStatus(t.date_from, t.date_to) === 'active'; });
    if (!active) { ticker.classList.remove('show'); return; }
    ticker.classList.add('show');
    var typ  = (active.trip_type || 'flight').toLowerCase();
    var icon = TYPE_ICON[typ] || '\u2708\ufe0f';
    var n    = nights(active.date_from, active.date_to);
    var pax  = (parseInt(active.adults) || 1) + (parseInt(active.children) || 0);
    var titleEl = document.getElementById('sc-ticker-title');
    var metaEl  = document.getElementById('sc-ticker-meta');
    var iconEl  = document.getElementById('sc-ticker-icon');
    if (titleEl) titleEl.textContent = active.label || (typ + ' Booking');
    if (iconEl)  iconEl.textContent  = icon;
    if (metaEl)  metaEl.textContent  =
      fmtDate(active.date_from) + ' \u2013 ' + fmtDate(active.date_to)
      + '  \u00b7  ' + pax + ' pax  \u00b7  ' + n + ' night' + (n !== 1 ? 's' : '');
  }

  function render(filter) {
    var list = document.getElementById('sc-list');
    if (!list) return;
    var trips = load();
    updateStats(trips);
    updateBadges(trips);
    updateTicker(trips);
    var filtered = (filter === 'all') ? trips : trips.filter(function(t){
      return getStatus(t.date_from, t.date_to) === filter;
    });
    list.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : emptyHTML(filter);
  }

  /* Public API */
  window.scSwitchTab = function(el, filter) {
    document.querySelectorAll('.sc-tab').forEach(function(t){ t.classList.remove('active'); });
    el.classList.add('active');
    render(filter);
  };

  window.scDeleteTrip = function(ref) {
    var trips = load().filter(function(t){ return String(t.ref) !== String(ref); });
    localStorage.setItem(KEY, JSON.stringify(trips));
    var active = document.querySelector('.sc-tab.active');
    render(active ? active.dataset.filter : 'all');
  };

  window.saveToSuitcase = function(booking) {
    var trips = load();
    trips.unshift(booking);
    localStorage.setItem(KEY, JSON.stringify(trips));
  };

  /* Init */
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

        # ── JS ────────────────────────────────────────────────────────
        Script(_SUITCASE_JS),
    )
