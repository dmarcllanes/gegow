"""
Navigation — sidebar (desktop) + mobile top header + floating bottom nav.
"""

from fasthtml.common import Div, Header, Nav, A, Span, Button

NAV_ITEMS = [
    ('🧭', 'Explore',   'Explore',  '/dashboard'),
    ('✈️', 'Book',      'Book',     '/book'),
    ('🧳', 'Suitcase',  'Suitcase', '/suitcase'),
    ('🛍️', 'Shop',      'Shop',     '/gear'),
    ('🏢', 'B2B',       'B2B',      '/b2b'),
]

NAV_CSS = """
/* ════════════════════════════════════════════════════════════
   SIDEBAR  (desktop ≥ 768px)
════════════════════════════════════════════════════════════ */
.sidebar { display: none; }

@media (min-width: 768px) {
  .sidebar {
    display: flex;
    flex-direction: column;
    width: var(--sidebar, 240px);
    flex-shrink: 0;
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
    scrollbar-width: none;
    background: #070f1a;
    border-right: 1px solid rgba(255,255,255,.06);
    box-shadow: 2px 0 20px rgba(0,0,0,.3);
  }
  .sidebar::-webkit-scrollbar { display: none; }

  .sidebar::after {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 220px;
    background: radial-gradient(ellipse 180% 100% at 50% 0%,
      rgba(0,201,177,.12) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
  }

  /* ── Brand ── */
  .sidebar-brand {
    position: relative; z-index: 1;
    display: flex; align-items: center; gap: 11px;
    padding: 22px 18px 18px;
  }
  .sidebar-brand-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #00C9B1, #007a6e);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; flex-shrink: 0;
    box-shadow: 0 2px 14px rgba(0,201,177,.4);
  }
  .sidebar-brand-name {
    font-size: 16px; font-weight: 800; color: #fff; letter-spacing: -.3px;
  }
  .sidebar-brand-sub {
    font-size: 10px; color: rgba(255,255,255,.3); margin-top: 2px;
  }

  .sidebar-rule {
    height: 1px; margin: 0 18px;
    background: linear-gradient(90deg, rgba(0,201,177,.35), rgba(0,201,177,.06) 60%, transparent);
    position: relative; z-index: 1;
  }

  /* ── Profile card ── */
  .sidebar-profile {
    position: relative; z-index: 1;
    display: flex; align-items: center; gap: 10px;
    margin: 14px 12px 6px;
    padding: 11px 13px;
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 12px;
    text-decoration: none;
    transition: background .2s, border-color .2s;
  }
  .sidebar-profile:hover {
    background: rgba(0,201,177,.07);
    border-color: rgba(0,201,177,.22);
  }
  .sidebar-avatar {
    width: 30px; height: 30px;
    background: linear-gradient(135deg, #00C9B1, #007a6e);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 12px; font-weight: 800; color: #04111a;
    flex-shrink: 0;
  }
  .sidebar-profile-info { flex: 1; min-width: 0; }
  .sidebar-profile-name {
    font-size: 12px; font-weight: 700; color: rgba(255,255,255,.85);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .sidebar-profile-role { font-size: 10px; color: rgba(255,255,255,.3); margin-top: 1px; }
  .sidebar-profile-arrow { font-size: 11px; color: rgba(255,255,255,.2); flex-shrink: 0; }

  /* ── Section label ── */
  .sidebar-section-label {
    position: relative; z-index: 1;
    font-size: 9px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: rgba(255,255,255,.2);
    padding: 14px 20px 4px;
  }

  /* ── Nav items ── */
  .sidebar .nav-item {
    position: relative; z-index: 1;
    display: flex; align-items: center; gap: 10px;
    padding: 10px 14px;
    margin: 1px 10px;
    border-radius: 10px;
    color: rgba(255,255,255,.42);
    font-size: 13px; font-weight: 500;
    text-decoration: none;
    transition: background .15s, color .15s;
  }
  .sidebar .nav-item:hover {
    background: rgba(255,255,255,.06);
    color: rgba(255,255,255,.82);
  }
  .sidebar .nav-item.active {
    background: rgba(0,201,177,.09);
    color: #e0fff9;
    font-weight: 600;
  }
  .sidebar .nav-item.active::before {
    content: '';
    position: absolute; left: 0; top: 22%; bottom: 22%;
    width: 3px;
    background: linear-gradient(180deg, #00C9B1, #00a08f);
    border-radius: 0 3px 3px 0;
    box-shadow: 0 0 8px rgba(0,201,177,.65);
  }
  .sidebar .nav-icon {
    font-size: 15px; width: 20px; text-align: center; flex-shrink: 0;
    opacity: .6; transition: opacity .15s;
  }
  .sidebar .nav-item:hover .nav-icon,
  .sidebar .nav-item.active .nav-icon { opacity: 1; }

  /* ── Divider ── */
  .sidebar-divider {
    position: relative; z-index: 1;
    height: 1px; margin: 10px 18px;
    background: rgba(255,255,255,.07);
  }

  /* ── Footer ── */
  .sidebar-footer {
    position: relative; z-index: 1;
    margin-top: auto; padding: 10px 10px 22px;
  }
  .sidebar-logout {
    display: flex; align-items: center; gap: 9px;
    padding: 10px 14px; border-radius: 10px;
    background: transparent;
    color: rgba(252,165,165,.55);
    font-size: 12px; font-weight: 500;
    cursor: pointer; border: 1px solid transparent;
    transition: all .15s; width: 100%; text-decoration: none;
  }
  .sidebar-logout:hover {
    background: rgba(239,68,68,.09);
    color: #fca5a5;
    border-color: rgba(239,68,68,.2);
  }
  .sidebar-footer-text {
    font-size: 10px; color: rgba(255,255,255,.13);
    padding: 8px 14px 0; line-height: 1.6;
  }
}

@media (min-width: 1200px) {
  .sidebar { width: 260px; }
}

/* ════════════════════════════════════════════════════════════
   MOBILE TOP HEADER  (< 768px)
════════════════════════════════════════════════════════════ */
.gegow-header {
  background: rgba(5, 12, 22, 0.95);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  height: 58px;
  padding: 0 16px;
  position: sticky; top: 0; z-index: 300;
  display: flex; align-items: center; justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,.06);
  box-shadow: 0 1px 0 rgba(255,255,255,.04), 0 4px 24px rgba(0,0,0,.4);
  transform: translateY(0);
  transition: transform 0.3s ease;
}
.gegow-header.nav-hidden {
  transform: translateY(-100%);
}
/* teal accent line at very bottom of header */
.gegow-header::after {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent 0%, rgba(0,201,177,.5) 40%, rgba(0,201,177,.5) 60%, transparent 100%);
}
@media (min-width: 768px) { .gegow-header { display: none; } }

.gegow-header-left  { display: flex; align-items: center; gap: 10px; }
.gegow-header-right { display: flex; align-items: center; gap: 8px; }

.gh-logo-icon {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, #00C9B1, #007a6e);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 17px; flex-shrink: 0;
  box-shadow: 0 0 16px rgba(0,201,177,.35);
}
.gh-brand-name {
  font-size: 18px; font-weight: 900; letter-spacing: -.5px; color: #fff;
}
.gh-brand-sub { font-size: 9px; color: rgba(255,255,255,.3); margin-top: 1px; }

.gh-avatar {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, #00C9B1, #007a6e);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; font-weight: 800; color: #04111a;
  text-decoration: none;
  box-shadow: 0 0 0 2px rgba(0,201,177,.4);
  transition: box-shadow .15s, transform .15s;
}
.gh-avatar:hover { box-shadow: 0 0 0 3px rgba(0,201,177,.65); transform: scale(1.05); }

.gh-icon-btn {
  width: 34px; height: 34px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 15px; color: rgba(255,255,255,.55);
  text-decoration: none; cursor: pointer;
  transition: all .15s;
  position: relative;
}
.gh-icon-btn:hover {
  background: rgba(0,201,177,.12);
  border-color: rgba(0,201,177,.3);
  color: #00C9B1;
}

/* ════════════════════════════════════════════════════════════
   FLOATING BOTTOM NAV  (< 768px)
════════════════════════════════════════════════════════════ */
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  z-index: 300;
  padding: 0 12px calc(env(safe-area-inset-bottom, 8px) + 8px);
  pointer-events: none;
  display: flex;
  transform: translateY(0);
  transition: transform 0.3s ease;
}
.bottom-nav.nav-hidden {
  transform: translateY(120%);
}
@media (min-width: 768px) { .bottom-nav { display: none; } }
@media (orientation: landscape) and (max-width: 767px) {
  .bottom-nav { padding: 0 12px calc(env(safe-area-inset-bottom, 4px) + 4px); }
}

.bn-inner {
  flex: 1;
  display: flex; align-items: stretch;
  background: rgba(5, 12, 22, 0.92);
  backdrop-filter: blur(28px) saturate(200%);
  -webkit-backdrop-filter: blur(28px) saturate(200%);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 22px;
  padding: 5px 6px;
  box-shadow:
    0 -1px 0 rgba(255,255,255,.05) inset,
    0 16px 48px rgba(0,0,0,.5),
    0 4px 16px rgba(0,0,0,.3);
  pointer-events: auto;
  overflow: hidden;
}
/* teal shimmer line at top of nav pill */
.bn-inner::before {
  content: '';
  position: absolute; top: 0; left: 15%; right: 15%; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,201,177,.6), transparent);
}

.bottom-nav .nav-item {
  flex: 1;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 3px;
  padding: 8px 4px 6px;
  border-radius: 16px;
  color: rgba(255,255,255,.32);
  font-size: 10px; font-weight: 600;
  text-decoration: none;
  position: relative;
  transition: color .2s ease, background .2s ease, transform .18s ease;
  -webkit-tap-highlight-color: transparent;
  min-height: 50px;
}
@media (max-width: 359px) {
  .bottom-nav .nav-item { padding: 6px 2px 5px; font-size: 9px; min-height: 46px; }
}
@media (orientation: landscape) and (max-width: 767px) {
  .bottom-nav .nav-item { padding: 5px 4px 4px; min-height: 40px; }
}

/* Active state — teal bubble background */
.bottom-nav .nav-item.active {
  color: #00C9B1;
  background: linear-gradient(160deg, rgba(0,201,177,.18) 0%, rgba(0,109,119,.12) 100%);
}

/* Hover */
.bottom-nav .nav-item:not(.active):hover {
  color: rgba(255,255,255,.65);
  background: rgba(255,255,255,.05);
}

/* Active top glow */
.bottom-nav .nav-item.active::before {
  content: '';
  position: absolute; top: 0; left: 20%; right: 20%; height: 2px;
  border-radius: 0 0 4px 4px;
  background: linear-gradient(90deg, transparent, #00C9B1, transparent);
  box-shadow: 0 0 10px rgba(0,201,177,.9);
}

/* Icon */
.bottom-nav .nav-icon {
  font-size: 20px; line-height: 1;
  transition: transform .2s cubic-bezier(.34,1.56,.64,1);
  display: block;
}
@media (max-width: 359px) { .bottom-nav .nav-icon { font-size: 18px; } }
@media (orientation: landscape) and (max-width: 767px) { .bottom-nav .nav-icon { font-size: 17px; } }

.bottom-nav .nav-item.active .nav-icon {
  transform: scale(1.18) translateY(-1px);
  filter: drop-shadow(0 0 6px rgba(0,201,177,.7));
}
.bottom-nav .nav-item:active .nav-icon { transform: scale(0.9); }

/* Label */
.bottom-nav .nav-label {
  line-height: 1;
  transition: opacity .2s, color .2s;
  white-space: nowrap;
}
.bottom-nav .nav-item:not(.active) .nav-label { opacity: 0.6; }
.bottom-nav .nav-item.active .nav-label { opacity: 1; font-weight: 700; }
"""


def sidebar(active: str = '/') -> Div:
    items = []
    for icon, label, _short, href in NAV_ITEMS:
        cls = 'nav-item' + (' active' if href == active else '')
        items.append(A(Span(icon, cls='nav-icon'), Span(label), href=href, cls=cls))

    return Div(
        Div(
            Div('✈', cls='sidebar-brand-icon'),
            Div(
                Div('Gegow', cls='sidebar-brand-name'),
                Div('Digital Travel Agency', cls='sidebar-brand-sub'),
            ),
            cls='sidebar-brand',
        ),
        Div(cls='sidebar-rule'),
        A(
            Div('G', cls='sidebar-avatar'),
            Div(
                Div('My Account', cls='sidebar-profile-name'),
                Div('Traveller', cls='sidebar-profile-role'),
                cls='sidebar-profile-info',
            ),
            Span('›', cls='sidebar-profile-arrow'),
            href='/profile', cls='sidebar-profile',
        ),
        Div('Menu', cls='sidebar-section-label'),
        *items,
        Div(cls='sidebar-divider'),
        Div(
            A('🚪  Log out', href='/auth/logout', cls='sidebar-logout'),
            Div('© 2026 Gegow · 🇵🇭 Philippines', cls='sidebar-footer-text'),
            cls='sidebar-footer',
        ),
        cls='sidebar',
    )


def app_header() -> Header:
    return Header(
        Div(
            Div('✈', cls='gh-logo-icon'),
            Div(
                Div('Gegow', cls='gh-brand-name'),
                Div('Digital Travel Agency', cls='gh-brand-sub'),
            ),
            cls='gegow-header-left',
        ),
        Div(
            A('G', href='/profile', cls='gh-avatar', title='My Profile'),
            A('🚪', href='/auth/logout', cls='gh-icon-btn', title='Log out'),
            cls='gegow-header-right',
        ),
        cls='gegow-header',
    )


def bottom_nav(active: str = '/') -> Nav:
    items = []
    for icon, _label, short, href in NAV_ITEMS:
        cls = 'nav-item' + (' active' if href == active else '')
        items.append(
            A(
                Span(icon, cls='nav-icon'),
                Span(short, cls='nav-label'),
                href=href, cls=cls,
            )
        )
    return Nav(
        Div(*items, cls='bn-inner'),
        cls='bottom-nav',
    )
