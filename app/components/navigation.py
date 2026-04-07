"""
Navigation — redesigned sidebar (desktop) + mobile top bar + bottom nav.
"""

from fasthtml.common import Div, Header, Nav, A, Span, P, Button

NAV_ITEMS = [
    ('🧭', 'Explore',     '/dashboard'),
    ('✈️', 'Book a Trip', '/book'),
    ('🧳', 'My Suitcase', '/suitcase'),
    ('🛍️', 'Shop',        '/gear'),
    ('🏢', 'B2B Portal',  '/b2b'),
]

NAV_CSS = """
/* ════════════════════════════════════════════════════════════
   SIDEBAR
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

  /* teal ambient glow at top */
  .sidebar::after {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 220px;
    background: radial-gradient(ellipse 180% 100% at 50% 0%,
      rgba(0,201,177,.12) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
  }

  /* ── Brand ───────────────────────────────────────────── */
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

  /* teal rule below brand */
  .sidebar-rule {
    height: 1px; margin: 0 18px;
    background: linear-gradient(90deg, rgba(0,201,177,.35), rgba(0,201,177,.06) 60%, transparent);
    position: relative; z-index: 1;
  }

  /* ── Profile card ─────────────────────────────────────── */
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

  /* ── Section label ────────────────────────────────────── */
  .sidebar-section-label {
    position: relative; z-index: 1;
    font-size: 9px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: rgba(255,255,255,.2);
    padding: 14px 20px 4px;
  }

  /* ── Nav items ────────────────────────────────────────── */
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
  /* left indicator */
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

  /* ── Divider ──────────────────────────────────────────── */
  .sidebar-divider {
    position: relative; z-index: 1;
    height: 1px; margin: 10px 18px;
    background: rgba(255,255,255,.07);
  }

  /* ── Footer ───────────────────────────────────────────── */
  .sidebar-footer {
    position: relative; z-index: 1;
    margin-top: auto; padding: 10px 10px 22px;
  }
}

@media (min-width: 1200px) {
  .sidebar { width: 260px; }
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

/* ════════════════════════════════════════════════════════════
   MOBILE TOP HEADER
════════════════════════════════════════════════════════════ */
.gegow-header {
  background: rgba(7,15,26,.96);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  height: 56px; padding: 0 16px;
  position: sticky; top: 0; z-index: 200;
  display: flex; align-items: center; justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,.07);
  box-shadow: 0 2px 16px rgba(0,0,0,.3);
}
@media (min-width: 768px) { .gegow-header { display: none; } }

.gegow-header-left  { display: flex; align-items: center; gap: 10px; }
.gegow-header-right { display: flex; align-items: center; gap: 8px; }

.gh-logo-icon {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, #00C9B1, #007a6e);
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; flex-shrink: 0;
  box-shadow: 0 2px 10px rgba(0,201,177,.3);
}
.gh-brand-name { font-size: 17px; font-weight: 800; letter-spacing: -.4px; color: #fff; }
.gh-brand-sub  { font-size: 9px; color: rgba(255,255,255,.35); margin-top: 1px; }

/* avatar circle — profile link */
.gh-avatar {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, #00C9B1, #007a6e);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #04111a;
  text-decoration: none;
  box-shadow: 0 0 0 2px rgba(0,201,177,.3);
  transition: box-shadow .15s;
}
.gh-avatar:hover { box-shadow: 0 0 0 3px rgba(0,201,177,.55); }

/* logout icon button */
.gh-logout {
  width: 34px; height: 34px;
  background: transparent;
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  font-size: 15px; color: rgba(255,255,255,.4);
  text-decoration: none;
  transition: all .15s;
}
.gh-logout:hover {
  background: rgba(239,68,68,.1);
  border-color: rgba(239,68,68,.3);
  color: #fca5a5;
}

/* ════════════════════════════════════════════════════════════
   BOTTOM NAV (mobile)
════════════════════════════════════════════════════════════ */
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  background: rgba(7,15,26,.96);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-top: 1px solid rgba(255,255,255,.07);
  display: flex; z-index: 200;
  padding-bottom: env(safe-area-inset-bottom, 0);
}
@media (min-width: 768px) { .bottom-nav { display: none; } }

.bottom-nav .nav-item {
  flex: 1;
  display: flex; flex-direction: column; align-items: center;
  padding: 8px 2px 6px; gap: 2px;
  color: rgba(255,255,255,.28);
  font-size: 9px; font-weight: 500;
  text-decoration: none; position: relative;
  transition: color .15s;
}
@media (min-width: 360px) { .bottom-nav .nav-item { padding: 9px 4px 7px; gap: 3px; font-size: 10px; } }
.bottom-nav .nav-item.active {
  color: #00C9B1; font-weight: 700;
}
.bottom-nav .nav-item.active::after {
  content: '';
  position: absolute; top: 0; left: 22%; right: 22%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #00C9B1, transparent);
  box-shadow: 0 0 6px rgba(0,201,177,.8);
}
.bottom-nav .nav-icon { font-size: 17px; line-height: 1; }
@media (min-width: 360px) { .bottom-nav .nav-icon { font-size: 18px; } }
@media (orientation: landscape) and (max-width: 767px) {
  .bottom-nav .nav-item { padding: 5px 2px 4px; }
  .bottom-nav .nav-icon { font-size: 15px; }
}
"""


def sidebar(active: str = '/') -> Div:
    items = []
    for icon, label, href in NAV_ITEMS:
        cls = 'nav-item' + (' active' if href == active else '')
        items.append(A(Span(icon, cls='nav-icon'), Span(label), href=href, cls=cls))

    return Div(
        # Brand
        Div(
            Div('✈', cls='sidebar-brand-icon'),
            Div(
                Div('Gegow', cls='sidebar-brand-name'),
                Div('Digital Travel Agency', cls='sidebar-brand-sub'),
            ),
            cls='sidebar-brand',
        ),
        Div(cls='sidebar-rule'),
        # Profile card
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
        # Nav
        Div('Menu', cls='sidebar-section-label'),
        *items,
        Div(cls='sidebar-divider'),
        # Footer
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
            A('🚪', href='/auth/logout', cls='gh-logout', title='Log out'),
            cls='gegow-header-right',
        ),
        cls='gegow-header',
    )


def bottom_nav(active: str = '/') -> Nav:
    short = {'Book a Trip': 'Book', 'My Suitcase': 'Suitcase', 'Shop': 'Shop', 'B2B Portal': 'B2B'}
    items = []
    for icon, label, href in NAV_ITEMS:
        cls = 'nav-item' + (' active' if href == active else '')
        items.append(A(Span(icon, cls='nav-icon'), Span(short.get(label, label)), href=href, cls=cls))
    return Nav(*items, cls='bottom-nav')
