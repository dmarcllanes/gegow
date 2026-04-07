/* Gegow — App interactions & animations */

/* ── Splash screen ───────────────────────────────────────── */
(function () {
  var splash = document.getElementById('app-splash');
  if (!splash) return;

  function dismiss() {
    splash.classList.add('splash-exit');
    setTimeout(function () { splash.style.display = 'none'; }, 520);
    sessionStorage.setItem('gegow_splashed', '1');
  }

  // Already seen this session — remove immediately (no flash)
  if (sessionStorage.getItem('gegow_splashed')) {
    splash.style.display = 'none';
    return;
  }

  // Auto-dismiss after 3 s, or on tap/click
  var timer = setTimeout(dismiss, 3000);
  splash.addEventListener('click', function () {
    clearTimeout(timer);
    dismiss();
  });
})();

/* ── Enable JS-driven animations ────────────────────────── */
document.documentElement.classList.add('js-loaded');
document.body.classList.add('js-loaded');

/* ── Scroll-triggered fade-up ────────────────────────────── */
(function () {
  const io = new IntersectionObserver(
    entries => entries.forEach(e => {
      if (!e.isIntersecting) return;
      const delay = parseInt(e.target.dataset.delay || 0);
      setTimeout(() => e.target.classList.add('in-view'), delay);
      io.unobserve(e.target);
    }),
    { threshold: 0.07, rootMargin: '0px 0px -32px 0px' }
  );

  function observe() {
    document.querySelectorAll('.fade-up:not(.in-view)').forEach(el => io.observe(el));
  }
  observe();
  document.addEventListener('htmx:afterSwap', observe);

  // Auto-stagger children of .stagger
  document.querySelectorAll('.stagger').forEach(parent => {
    Array.from(parent.children).forEach((child, i) => {
      child.classList.add('fade-up');
      child.dataset.delay = i * 70;
    });
  });
})();

/* ── Ripple effect ───────────────────────────────────────── */
document.addEventListener('click', e => {
  const btn = e.target.closest('[class*="btn-"],[class*="search-submit"]');
  if (!btn || btn.classList.contains('btn-back') || btn.classList.contains('btn-remove')) return;

  const ripple = document.createElement('span');
  ripple.className = 'ripple-wave';
  const rect = btn.getBoundingClientRect();
  const size = Math.max(rect.width, rect.height) * 2;
  Object.assign(ripple.style, {
    width: size + 'px',
    height: size + 'px',
    left: (e.clientX - rect.left - size / 2) + 'px',
    top: (e.clientY - rect.top - size / 2) + 'px',
  });
  btn.style.position = 'relative';
  btn.style.overflow = 'hidden';
  btn.appendChild(ripple);
  setTimeout(() => ripple.remove(), 700);
});

/* ── Number counter ──────────────────────────────────────── */
const counterIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const target = parseInt(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const t0 = performance.now();
    const dur = 1400;
    const tick = now => {
      const p = Math.min((now - t0) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.floor(eased * target).toLocaleString() + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
    counterIO.unobserve(el);
  });
}, { threshold: 0.5 });

function initCounters() {
  document.querySelectorAll('[data-count]').forEach(el => counterIO.observe(el));
}
initCounters();

/* ── Hero search tabs ────────────────────────────────────── */
function switchHeroTab(type) {
  document.querySelectorAll('.htab').forEach(t => t.classList.toggle('active', t.dataset.type === type));
}

/* ── Pax stepper (wizard) ────────────────────────────────── */
function adjustPax(type, delta) {
  const count = document.getElementById(type + '-count');
  const input = document.getElementById(type + '-input');
  if (!count || !input) return;
  let v = parseInt(count.textContent) + delta;
  v = Math.max(type === 'adults' ? 1 : 0, Math.min(10, v));
  count.textContent = v;
  input.value = v;
}

/* ── Suitcase (localStorage) ─────────────────────────────── */
function getSuitcase() {
  return JSON.parse(localStorage.getItem('gegow_suitcase') || '[]');
}
function saveToSuitcase(booking) {
  const items = getSuitcase();
  booking.saved_at = new Date().toISOString();
  items.unshift(booking);
  localStorage.setItem('gegow_suitcase', JSON.stringify(items));
}
function removeItinerary(idx) {
  const items = getSuitcase();
  items.splice(idx, 1);
  localStorage.setItem('gegow_suitcase', JSON.stringify(items));
  renderSuitcase();
}
function renderSuitcase() {
  const container = document.getElementById('suitcase-list');
  if (!container) return;
  const items = getSuitcase();

  if (!items.length) {
    container.innerHTML = `
      <div class="suitcase-empty">
        <div class="empty-icon">🧳</div>
        <div class="empty-title">Your suitcase is empty</div>
        <p style="font-size:14px;color:var(--muted);margin-bottom:24px">
          Book a trip and your itinerary will appear here — even offline!
        </p>
        <a href="/book" class="btn-primary" style="display:inline-block;width:auto;padding:12px 32px;border-radius:50px;text-decoration:none">
          Book a Trip ✈️
        </a>
      </div>`;
    return;
  }

  const icon = { flight: '✈️', hotel: '🏨', tour: '🗺️' };
  container.innerHTML = items.map((item, i) => `
    <div class="itinerary-card fade-up in-view" style="--i:${i}">
      <span class="itin-type-badge">${icon[item.trip_type] || '🌏'} ${item.trip_type}</span>
      <div class="itin-title">${item.label}</div>
      <div class="itin-meta">
        📅 ${item.date_from}${item.date_to ? ' → ' + item.date_to : ''}
        &nbsp;·&nbsp; 👤 ${item.adults} adult${item.adults > 1 ? 's' : ''}${item.children > 0 ? ', ' + item.children + ' child' : ''}
      </div>
      <div class="itin-price">₱${parseInt(item.total).toLocaleString()}</div>
      <div class="itin-ref">Ref: GGW-${item.ref}</div>
      <div class="itin-actions">
        <button class="btn-remove" onclick="removeItinerary(${i})">Remove</button>
        <div class="btn-view">View Details</div>
      </div>
    </div>
  `).join('');
}

/* ── Cart (localStorage) ─────────────────────────────────── */
function addToCart(btn) {
  try {
    const vals = JSON.parse(btn.getAttribute('hx-vals') || '{}');
    const cart = JSON.parse(localStorage.getItem('gegow_cart') || '[]');
    cart.push({ ...vals, qty: 1 });
    localStorage.setItem('gegow_cart', JSON.stringify(cart));
    btn.textContent = '✓ Added!';
    btn.style.background = 'var(--teal)';
    btn.style.color = '#fff';
    btn.style.borderColor = 'var(--teal)';
    updateCartBadge();
  } catch {}
}
function updateCartBadge() {
  const cart = JSON.parse(localStorage.getItem('gegow_cart') || '[]');
  const badge = document.getElementById('cart-badge');
  if (badge) {
    badge.textContent = cart.length;
    badge.style.display = cart.length > 0 ? 'flex' : 'none';
  }
}

/* ── Dev seed data (pre-fills suitcase + cart for UI testing) */
function seedDemoData() {
  const existing = getSuitcase();
  if (existing.length > 0) return; // don't overwrite real data

  const demoItineraries = [
    // ── Upcoming trips ──────────────────────────────────────
    {
      ref: '84721',
      trip_type: 'flight',
      item_id: 'FL001',
      label: 'Manila → Cebu (Cebu Pacific)',
      adults: 2, children: 0,
      date_from: '2026-04-15', date_to: '2026-04-15',
      total: 3048,
      saved_at: new Date().toISOString(),
    },
    {
      ref: '39204',
      trip_type: 'hotel',
      item_id: 'HT003',
      label: 'Henann Resort Boracay',
      adults: 2, children: 1,
      date_from: '2026-05-01', date_to: '2026-05-04',
      total: 23400,
      saved_at: new Date().toISOString(),
    },
    {
      ref: '72884',
      trip_type: 'flight',
      item_id: 'FL011',
      label: 'Manila → Singapore (Philippine Airlines)',
      adults: 1, children: 0,
      date_from: '2026-06-20', date_to: '2026-06-27',
      total: 14500,
      saved_at: new Date().toISOString(),
    },
    // ── Active trip (date_from ≤ today ≤ date_to) ───────────
    {
      ref: '55301',
      trip_type: 'tour',
      item_id: 'TR005',
      label: 'Siargao Surf & Island Hop 5D4N',
      adults: 2, children: 0,
      date_from: '2026-03-28', date_to: '2026-04-01',
      total: 28600,
      saved_at: new Date().toISOString(),
    },
    // ── Completed trips ─────────────────────────────────────
    {
      ref: '61539',
      trip_type: 'tour',
      item_id: 'TR002',
      label: 'El Nido Palawan Discovery 4D3N',
      adults: 2, children: 0,
      date_from: '2026-02-10', date_to: '2026-02-13',
      total: 38300,
      saved_at: new Date().toISOString(),
    },
    {
      ref: '30847',
      trip_type: 'hotel',
      item_id: 'HT009',
      label: 'Crimson Hotel Filinvest Alabang',
      adults: 2, children: 2,
      date_from: '2026-01-15', date_to: '2026-01-17',
      total: 9800,
      saved_at: new Date().toISOString(),
    },
  ];

  localStorage.setItem('gegow_suitcase', JSON.stringify(demoItineraries));

  const demoCart = [
    { item_id: 'GR004', name: 'Compression Packing Cubes (6-set)', price: 1200, qty: 1 },
    { item_id: 'GR003', name: 'Universal Travel Adapter', price: 650, qty: 1 },
    { item_id: 'GR008', name: 'Wireless Noise-Cancelling Earbuds', price: 3200, qty: 1 },
  ];
  if (!localStorage.getItem('gegow_cart')) {
    localStorage.setItem('gegow_cart', JSON.stringify(demoCart));
  }
}

/* ── Init on load ────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  seedDemoData();
  updateCartBadge();
  initCounters();
});
