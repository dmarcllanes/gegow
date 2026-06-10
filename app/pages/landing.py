"""
Gegow — Landing page. Modern, animated, scroll-driven.
"""
import json as _json

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Style, Script, Link,
    Div, Nav, Footer, Section, Span, A, Button, P, H1, H2, H3,
)

IMGS = {
    "palawan":   "https://images.unsplash.com/photo-1518391846015-55a9cc003b25?w=800&q=80&fit=crop",
    "boracay":   "https://images.unsplash.com/photo-1537953773345-d172ccf13cf4?w=800&q=80&fit=crop",
    "siargao":   "https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?w=800&q=80&fit=crop",
    "singapore": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&q=80&fit=crop",
    "tokyo":     "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80&fit=crop",
    "bali":      "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80&fit=crop",
    "av1":       "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80&fit=crop&crop=face",
    "av2":       "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&q=80&fit=crop&crop=face",
    "av3":       "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=80&q=80&fit=crop&crop=face",
}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  background:var(--bg-body);color:var(--txt);-webkit-font-smoothing:antialiased;overflow-x:hidden;
  transition:background .3s,color .3s}
a{text-decoration:none;color:inherit}
img{display:block;width:100%;height:100%;object-fit:cover}

/* ── LIGHT (default) — Tropical Aqua ── */
:root{
  --g:#006D77;--gdk:#005060;--acc:#FF9100;--r:16px;
  --bg-body:#F0FAFA;--bg-2:#E0F5F5;--bg-3:#CBF0F0;
  --txt:#0A1D20;--txt-2:#1B3A3D;--muted:#4A7070;
  --border:rgba(0,140,153,.12);--border-md:rgba(0,140,153,.22);
  --card-bg:#ffffff;--card-bg-hover:rgba(0,140,153,.07);
  --nav-scrolled:rgba(240,250,250,.95);
  --hero-bg:#BDEAEC;
  --hero-bg-2:
    radial-gradient(ellipse 90% 60% at 50% 0%,rgba(0,170,180,.3) 0%,transparent 58%),
    radial-gradient(ellipse 55% 70% at 0% 90%,rgba(0,100,170,.15) 0%,transparent 55%),
    radial-gradient(ellipse 55% 55% at 100% 90%,rgba(0,170,180,.18) 0%,transparent 52%),
    radial-gradient(ellipse 40% 40% at 88% 10%,rgba(255,145,0,.14) 0%,transparent 52%),
    #BDEAEC;
  --hero-txt:#0A1D20;--hero-txt-2:#1B3A3D;--hero-muted:rgba(10,29,32,.42);
  --hero-pill-bg:rgba(0,140,153,.12);--hero-pill-border:rgba(0,140,153,.3);
  --hero-pill-txt:#006D77;
  --hero-grid:rgba(0,0,0,.04);
  --stats-bg:#E0F5F5;
  --shadow-card:0 4px 20px rgba(0,0,0,.09),0 0 0 1px rgba(0,140,153,.1);
  --search-card-bg:rgba(255,255,255,.9);--search-card-border:rgba(0,140,153,.18);
  --search-field-bg:#ffffff;--search-field-border:rgba(0,0,0,.12);
  --search-txt:#0A1D20;--search-ph:#4A7070;
  --step-bg:#ffffff;
  --marquee-bg:#E0F5F5;
  --reviews-bg:#E0F5F5;
  --cta-banner:linear-gradient(160deg,#A8E4E8 0%,#70C8D4 50%,#90D8E0 100%);
  --footer-bg:#CBF0F0;
  --toggle-bg:rgba(0,140,153,.08);
  --glow-teal:0 0 28px rgba(0,140,153,.22);
  --glow-acc:0 0 28px rgba(255,145,0,.2);
  --nav-pre-txt:#0A1D20;
  --nav-pre-muted:#1B3A3D;
  --nav-pre-btn-bg:rgba(0,0,0,.06);
  --nav-pre-btn-border:rgba(0,0,0,.16);
  --nav-pre-logo-color:#0A1D20;
}

/* ── DARK — Philippine Midnight Sea ── */
[data-theme="dark"]{
  --g:#00E8D4;--gdk:#00C4B2;
  --bg-body:#020C18;--bg-2:#07182C;--bg-3:#0D2545;
  --txt:#ffffff;--txt-2:rgba(255,255,255,.78);--muted:rgba(255,255,255,.48);
  --border:rgba(0,232,212,.12);--border-md:rgba(0,232,212,.22);
  --card-bg:rgba(255,255,255,.025);--card-bg-hover:rgba(0,232,212,.08);
  --nav-scrolled:rgba(2,12,24,.94);
  --hero-bg:#020C18;
  --hero-bg-2:
    radial-gradient(ellipse 110% 65% at 50% -5%,rgba(0,232,212,.2) 0%,transparent 55%),
    radial-gradient(ellipse 70% 90% at -5% 88%,rgba(0,60,200,.24) 0%,transparent 55%),
    radial-gradient(ellipse 70% 70% at 105% 95%,rgba(120,0,220,.18) 0%,transparent 52%),
    radial-gradient(ellipse 50% 50% at 92% 5%,rgba(255,145,0,.12) 0%,transparent 52%),
    #020C18;
  --hero-txt:#ffffff;--hero-txt-2:rgba(255,255,255,.78);--hero-muted:rgba(255,255,255,.42);
  --hero-pill-bg:rgba(0,232,212,.1);--hero-pill-border:rgba(0,232,212,.32);
  --hero-pill-txt:#00E8D4;
  --hero-grid:rgba(0,232,212,.05);
  --stats-bg:#07182C;
  --shadow-card:0 4px 28px rgba(0,0,0,.5),0 0 0 1px rgba(0,232,212,.08);
  --search-card-bg:rgba(255,255,255,.06);--search-card-border:rgba(0,232,212,.2);
  --search-field-bg:rgba(255,255,255,.07);--search-field-border:rgba(0,232,212,.14);
  --search-txt:#fff;--search-ph:rgba(255,255,255,.38);
  --step-bg:rgba(0,232,212,.04);
  --marquee-bg:#07182C;
  --reviews-bg:#07182C;
  --cta-banner:linear-gradient(160deg,#020C18 0%,#0A1E40 50%,#061830 100%);
  --footer-bg:#020C18;
  --toggle-bg:rgba(0,232,212,.08);
  --glow-teal:0 0 32px rgba(0,232,212,.3);
  --glow-acc:0 0 28px rgba(255,145,0,.3);
  --nav-pre-txt:#ffffff;
  --nav-pre-muted:rgba(255,255,255,.72);
  --nav-pre-btn-bg:rgba(255,255,255,.08);
  --nav-pre-btn-border:rgba(255,255,255,.2);
  --nav-pre-logo-color:#ffffff;
}

/* ── Scrollbar ── */
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--g);border-radius:4px}

/* ═══════════════════════════════════════════════════════════
   NAV
═══════════════════════════════════════════════════════════ */
.nav{
  position:fixed;inset:0 0 auto 0;z-index:300;height:64px;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 20px;gap:12px;
  background:transparent;
  transition:background .4s,backdrop-filter .4s,border-color .4s;
  border-bottom:1px solid transparent;
}
@media(min-width:768px){.nav{padding:0 40px}}
.nav.scrolled{
  background:var(--nav-scrolled);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-color:var(--border);
}

/* logo */
.nav-logo{
  display:flex;align-items:center;gap:9px;
  font-size:18px;font-weight:900;letter-spacing:-.4px;
  color:var(--nav-pre-logo-color);flex-shrink:0;
  transition:color .3s;
}
.nav.scrolled .nav-logo{color:var(--txt)}
.nav-logo-icon{
  width:34px;height:34px;border-radius:9px;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  display:flex;align-items:center;justify-content:center;font-size:16px;
  box-shadow:0 0 22px rgba(0,232,212,.5);flex-shrink:0;
}

/* desktop links */
.nav-links{display:none;align-items:center;gap:6px;flex:1;justify-content:center}
@media(min-width:900px){.nav-links{display:flex}}
.nav-links a{
  font-size:13px;font-weight:600;padding:6px 12px;border-radius:8px;
  color:var(--nav-pre-muted);transition:color .15s,background .15s;
}
.nav.scrolled .nav-links a{color:var(--muted)}
.nav-links a:hover{color:var(--g);background:rgba(0,201,177,.1)}

/* right cluster */
.nav-right{display:flex;align-items:center;gap:8px;flex-shrink:0}

/* theme toggle */
.theme-toggle{
  width:36px;height:36px;border-radius:9px;
  border:1.5px solid var(--nav-pre-btn-border);
  background:var(--nav-pre-btn-bg);
  backdrop-filter:blur(8px);
  cursor:pointer;font-size:16px;
  display:flex;align-items:center;justify-content:center;
  transition:border-color .25s,background .25s,color .25s,transform .2s;
  flex-shrink:0;color:var(--nav-pre-txt);
}
.nav.scrolled .theme-toggle{
  border-color:var(--border-md);background:var(--toggle-bg);color:var(--txt);
}
.theme-toggle:hover{border-color:var(--g);transform:rotate(20deg);background:rgba(0,201,177,.15);color:var(--g)}

/* PWA install button */
.btn-install{
  display:inline-flex;align-items:center;gap:6px;
  padding:7px 14px;border-radius:9px;
  border:1.5px solid var(--nav-pre-btn-border);
  background:var(--nav-pre-btn-bg);
  backdrop-filter:blur(8px);
  font-size:12px;font-weight:700;color:var(--nav-pre-txt);
  cursor:pointer;transition:all .2s;white-space:nowrap;
  display:none;
}
@media(min-width:600px){.btn-install{display:inline-flex}}
.nav.scrolled .btn-install{
  border-color:var(--g);background:rgba(0,201,177,.1);color:var(--g);
}
.btn-install:hover{background:rgba(0,201,177,.2);border-color:var(--g);color:var(--g);transform:translateY(-1px)}
.btn-install.hide{display:none!important}

/* auth buttons — desktop */
.btn-nav-ghost{
  display:none;padding:7px 16px;border-radius:9px;
  border:1.5px solid var(--nav-pre-btn-border);
  font-size:13px;font-weight:700;color:var(--nav-pre-txt);background:transparent;
  cursor:pointer;transition:all .15s;white-space:nowrap;
}
@media(min-width:768px){.btn-nav-ghost{display:inline-flex;align-items:center}}
.nav.scrolled .btn-nav-ghost{border-color:var(--border-md);color:var(--txt)}
.btn-nav-ghost:hover{border-color:var(--g);color:var(--g)}
.btn-nav-solid{
  display:none;padding:8px 18px;border-radius:9px;
  font-size:13px;font-weight:700;color:#fff;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  border:none;cursor:pointer;white-space:nowrap;
  box-shadow:0 0 20px rgba(0,232,212,.32);transition:all .15s;
}
@media(min-width:768px){.btn-nav-solid{display:inline-flex;align-items:center}}
.btn-nav-solid:hover{box-shadow:0 0 32px rgba(0,232,212,.52);transform:translateY(-1px)}

/* hamburger — mobile only */
.nav-hamburger{
  display:flex;flex-direction:column;justify-content:center;align-items:center;
  gap:5px;width:36px;height:36px;border-radius:9px;
  border:1.5px solid var(--nav-pre-btn-border);
  background:var(--nav-pre-btn-bg);
  cursor:pointer;flex-shrink:0;transition:all .2s;padding:0;
}
@media(min-width:900px){.nav-hamburger{display:none}}
.nav.scrolled .nav-hamburger{border-color:var(--border-md);background:var(--toggle-bg)}
.nav-hamburger span{
  display:block;width:16px;height:2px;border-radius:2px;
  background:var(--nav-pre-txt);transition:background .25s,transform .25s,opacity .25s;
}
.nav.scrolled .nav-hamburger span{background:var(--txt)}
.nav-hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.nav-hamburger.open span:nth-child(2){opacity:0}
.nav-hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}

/* mobile drawer */
.nav-drawer{
  display:none;position:fixed;top:64px;left:0;right:0;z-index:299;
  background:var(--nav-scrolled);
  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);
  padding:16px 20px 24px;flex-direction:column;gap:4px;
  animation:drawerDown .2s ease both;
}
.nav-drawer.open{display:flex}
@media(min-width:900px){.nav-drawer{display:none!important}}
@keyframes drawerDown{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
.drawer-link{
  display:flex;align-items:center;gap:12px;
  padding:12px 14px;border-radius:10px;
  font-size:14px;font-weight:600;color:var(--txt);
  transition:background .15s,color .15s;
}
.drawer-link:hover{background:rgba(0,201,177,.1);color:var(--g)}
.drawer-divider{height:1px;background:var(--border);margin:10px 0}
.drawer-install{
  display:flex;align-items:center;justify-content:center;gap:8px;
  width:100%;padding:12px;border-radius:10px;margin-bottom:10px;
  border:1.5px solid var(--g);background:rgba(0,201,177,.1);
  font-size:14px;font-weight:700;color:var(--g);cursor:pointer;
  transition:background .15s;
}
.drawer-install:hover{background:rgba(0,201,177,.2)}
.drawer-install.hide{display:none!important}
.drawer-auth{display:flex;gap:10px;padding:4px 0}
.drawer-auth .btn-ghost-full{
  flex:1;padding:11px;border-radius:10px;text-align:center;
  border:1.5px solid var(--border-md);font-size:14px;font-weight:700;
  color:var(--txt);background:transparent;cursor:pointer;transition:all .15s;
}
.drawer-auth .btn-ghost-full:hover{border-color:var(--g);color:var(--g)}
.drawer-auth .btn-solid-full{
  flex:1;padding:11px;border-radius:10px;text-align:center;
  font-size:14px;font-weight:700;color:#fff;
  background:linear-gradient(135deg,var(--g),#00a896);
  border:none;cursor:pointer;
  box-shadow:0 4px 16px rgba(0,201,177,.35);transition:all .15s;
}

/* ── Footer Install Strip ────────────────────────────────── */
.footer-install{
  display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:20px 0;margin-bottom:28px;
  border-bottom:1px solid var(--border);
  flex-wrap:wrap;gap:16px;
}
.footer-install-left{display:flex;align-items:center;gap:14px}
.footer-install-icon{
  width:44px;height:44px;border-radius:12px;flex-shrink:0;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  display:flex;align-items:center;justify-content:center;font-size:20px;
  box-shadow:0 0 18px rgba(0,232,212,.35);
}
.footer-install-title{font-size:14px;font-weight:800;color:var(--txt);margin-bottom:2px}
.footer-install-sub{font-size:12px;color:var(--muted)}
.footer-install-btns{display:flex;gap:8px;flex-shrink:0;flex-wrap:wrap}
.btn-install-cta{
  display:inline-flex;align-items:center;gap:6px;
  padding:9px 18px;border-radius:10px;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  border:none;font-size:13px;font-weight:700;color:#fff;
  cursor:pointer;white-space:nowrap;
  box-shadow:0 4px 14px rgba(0,232,212,.38);
  transition:all .18s;position:relative;overflow:hidden;
}
.btn-install-cta::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);transform:translateX(-100%);transition:transform .5s ease}
.btn-install-cta:hover{transform:translateY(-1px);box-shadow:0 6px 22px rgba(0,232,212,.5)}
.btn-install-cta:hover::before{transform:translateX(100%)}
.btn-install-cta:active{transform:scale(.96)}
.btn-install-cta.installed{opacity:.5;cursor:default;pointer-events:none;box-shadow:none}
.btn-ios-install{
  display:inline-flex;align-items:center;gap:6px;
  padding:9px 18px;border-radius:10px;
  background:transparent;border:1.5px solid var(--border-md);
  font-size:13px;font-weight:700;color:var(--txt);
  cursor:pointer;white-space:nowrap;transition:all .18s;
}
.btn-ios-install:hover{border-color:var(--g);color:var(--g)}
/* iOS modal */
.ios-modal{
  display:none;position:fixed;inset:0;z-index:999;
  background:rgba(0,0,0,.7);backdrop-filter:blur(8px);
  align-items:flex-end;justify-content:center;padding:16px;
}
.ios-modal.open{display:flex}
.ios-sheet{
  background:var(--bg-2,#071d29);border:1px solid var(--border);
  border-radius:24px;padding:28px 24px;max-width:420px;width:100%;
  animation:slideUp .35s ease both;
}
@keyframes slideUp{from{transform:translateY(60px);opacity:0}to{transform:translateY(0);opacity:1}}
.ios-sheet-title{font-size:18px;font-weight:900;color:var(--txt,#fff);margin-bottom:6px}
.ios-sheet-sub{font-size:13px;color:var(--muted);margin-bottom:20px}
.ios-steps{display:flex;flex-direction:column;gap:12px;margin-bottom:24px}
.ios-step{display:flex;align-items:center;gap:12px;font-size:14px;color:var(--txt,#fff)}
.ios-step-num{
  width:28px;height:28px;border-radius:8px;
  background:rgba(0,201,177,.15);border:1px solid rgba(0,201,177,.3);
  font-size:13px;font-weight:800;color:var(--g);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.ios-close{
  width:100%;padding:13px;border-radius:12px;
  background:var(--g);border:none;
  font-size:15px;font-weight:800;color:#fff;cursor:pointer;
}
.ios-close:hover{background:var(--gdk)}

/* ── Generic Install Guide Modal ─────────────────────────── */
.install-guide-modal{
  display:none;position:fixed;inset:0;z-index:999;
  background:rgba(0,0,0,.72);backdrop-filter:blur(8px);
  align-items:flex-end;justify-content:center;padding:16px;
}
.install-guide-modal.open{display:flex}
.ig-sheet{
  background:var(--bg-2,#071d29);border:1px solid var(--border);
  border-radius:24px;padding:28px 24px 24px;max-width:440px;width:100%;
  animation:slideUp .35s ease both;
}
.ig-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.ig-title{font-size:18px;font-weight:900;color:var(--txt,#fff)}
.ig-close-btn{
  width:32px;height:32px;border-radius:8px;border:none;
  background:rgba(255,255,255,.1);color:var(--muted,#9ca3af);
  font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:background .15s;
}
.ig-close-btn:hover{background:rgba(255,255,255,.18)}
.ig-sub{font-size:13px;color:var(--muted);margin-bottom:18px}
.ig-tabs{display:flex;gap:6px;margin-bottom:18px}
.ig-tab-btn{
  flex:1;padding:8px 6px;border-radius:10px;border:1.5px solid rgba(255,255,255,.1);
  background:transparent;font-size:12px;font-weight:700;color:var(--muted,#9ca3af);
  cursor:pointer;transition:all .15s;
}
.ig-tab-btn.active{
  background:rgba(0,201,177,.15);border-color:rgba(0,201,177,.4);color:var(--g,#00c9b1);
}
.ig-panel{display:none}
.ig-panel.active{display:flex;flex-direction:column;gap:12px;margin-bottom:24px}
.ig-step{display:flex;align-items:flex-start;gap:12px;font-size:14px;color:var(--txt,#fff)}
.ig-step-num{
  width:28px;height:28px;border-radius:8px;flex-shrink:0;
  background:rgba(0,201,177,.15);border:1px solid rgba(0,201,177,.3);
  font-size:13px;font-weight:800;color:var(--g,#00c9b1);
  display:flex;align-items:center;justify-content:center;margin-top:1px;
}
.ig-step-text{line-height:1.45}
.ig-step-hint{display:block;font-size:11px;color:var(--muted,#9ca3af);margin-top:2px}
.ig-got-it{
  width:100%;padding:13px;border-radius:12px;
  background:var(--g,#00c9b1);border:none;
  font-size:15px;font-weight:800;color:#fff;cursor:pointer;
}
.ig-got-it:hover{background:var(--gdk,#00a896)}

.btn-nav-solid{
  padding:8px 20px;border-radius:10px;
  font-size:13px;font-weight:700;color:#fff;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  border:none;cursor:pointer;
  box-shadow:0 0 20px rgba(0,232,212,.32);
  transition:all .15s;
}
.btn-nav-solid:hover{box-shadow:0 0 32px rgba(0,232,212,.52);transform:translateY(-1px)}

/* ═══════════════════════════════════════════════════════════
   HERO
═══════════════════════════════════════════════════════════ */
.hero{
  position:relative;min-height:100svh;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:calc(64px + 40px) 24px 60px;
  overflow:hidden;text-align:center;
  background:var(--hero-bg);
  color:var(--hero-txt);
  transition:background .3s,color .3s;
}
@media(min-width:768px){.hero{padding:calc(64px + 60px) 64px 80px}}

/* ── Daytime Island Sky (default / light) ────────────────── */
.hero-bg{
  position:absolute;inset:0;z-index:0;
  background:linear-gradient(
    to bottom,
    #0A2A4A 0%,
    #0E4060 15%,
    #1A6080 30%,
    #3D9AB8 48%,
    #7AC8DC 62%,
    #A8E0E8 72%,
    #C8EEF3 80%,
    #8EC8D8 90%,
    #4A9AB5 100%
  );
  transition:background .35s;
}
[data-theme="dark"] .hero-bg{
  background:linear-gradient(
    to bottom,
    #080318 0%,
    #160730 12%,
    #2E0E50 24%,
    #5C1A40 36%,
    #A83210 46%,
    #D95F08 54%,
    #F0A030 62%,
    #D96818 70%,
    #185A78 80%,
    #0A4060 90%,
    #061828 100%
  );
}

/* Remove scan beam (replaced by silhouette aesthetic) */
.hero::after{ display:none; }
@keyframes starTwinkle{
  0%,100%{opacity:.15}
  50%{opacity:.38}
}

/* floating orb — sun glow (light: bright midday; dark: sunset amber) */
.orb{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none}
.orb-1{
  width:320px;height:320px;
  background:radial-gradient(circle,rgba(255,245,180,.52) 0%,rgba(200,235,255,.22) 50%,transparent 72%);
  top:10%;left:68%;
  animation:sunPulse 8s ease-in-out infinite alternate;
}
.orb-2{ display:none; }
.orb-3{ display:none; }
@keyframes sunPulse{
  0%{opacity:.8;transform:scale(1)}
  100%{opacity:1;transform:scale(1.08)}
}
[data-theme="dark"] .orb-1{
  width:380px;height:380px;
  background:radial-gradient(circle,rgba(255,185,60,.32) 0%,rgba(255,100,20,.16) 45%,transparent 72%);
  top:42%;left:36%;
}

/* star field — only visible in dark (night) mode */
.hero-grid{
  display:block;position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    radial-gradient(circle,rgba(255,255,255,.9) 1px,transparent 1px),
    radial-gradient(circle,rgba(255,255,255,.6) 1px,transparent 1px),
    radial-gradient(circle,rgba(220,180,255,.85) 1.5px,transparent 1.5px),
    radial-gradient(circle,rgba(255,255,255,.45) 1px,transparent 1px),
    radial-gradient(circle,rgba(180,220,255,.7) 1px,transparent 1px),
    radial-gradient(circle,rgba(255,255,255,.35) 1px,transparent 1px);
  background-size:265px 175px,180px 270px,135px 135px,90px 90px,220px 160px,60px 60px;
  background-position:15px 20px,92px 62px,48px 108px,28px 68px,155px 38px,35px 42px;
  animation:starTwinkle 7s ease-in-out infinite alternate;
  opacity:.05;
  mask-image:linear-gradient(to bottom,black 0%,black 38%,transparent 58%);
  -webkit-mask-image:linear-gradient(to bottom,black 0%,black 38%,transparent 58%);
}
[data-theme="dark"] .hero-grid{ opacity:.3; }

/* ══════════════════════════════════════════════════════════
   ISLAND & MOUNTAIN SILHOUETTE LAYERS
══════════════════════════════════════════════════════════ */

/* ── Far mountains — daytime (default): blue-tinted ── */
.sil-far{
  position:absolute;bottom:0;left:0;right:0;height:42%;
  z-index:1;pointer-events:none;
  background:linear-gradient(to bottom,rgba(20,80,120,.22),rgba(10,50,90,.44));
  clip-path:polygon(
    0% 100%,0% 44%,4% 34%,9% 41%,14% 25%,20% 33%,26% 17%,32% 27%,
    38% 12%,44% 22%,51% 8%,57% 18%,63% 5%,69% 14%,75% 9%,82% 18%,
    88% 4%,94% 13%,100% 8%,100% 100%
  );
}
[data-theme="dark"] .sil-far{
  background:linear-gradient(to bottom,rgba(55,18,90,.22),rgba(28,8,55,.52));
}

/* ── Mid mountains — daytime: darker teal-blue ── */
.sil-mid{
  position:absolute;bottom:0;left:0;right:0;height:34%;
  z-index:2;pointer-events:none;
  background:linear-gradient(to bottom,rgba(10,55,88,.48),rgba(5,32,62,.78));
  clip-path:polygon(
    0% 100%,0% 56%,4% 46%,9% 53%,14% 38%,20% 47%,26% 31%,32% 41%,
    38% 25%,44% 35%,50% 20%,56% 30%,62% 15%,68% 25%,74% 19%,80% 29%,
    86% 23%,92% 31%,97% 25%,100% 28%,100% 100%
  );
}
[data-theme="dark"] .sil-mid{
  background:linear-gradient(to bottom,rgba(0,50,80,.58),rgba(0,28,52,.88));
}

/* ── Near islands / volcanic peaks — dark foreground ── */
.sil-near{
  position:absolute;bottom:0;left:0;right:0;height:26%;
  z-index:3;pointer-events:none;
  background:linear-gradient(to bottom,rgba(4,18,38,.86),rgba(2,10,22,.96));
  clip-path:polygon(
    0% 100%,0% 68%,3% 57%,7% 66%,11% 49%,16% 59%,21% 43%,27% 55%,
    33% 38%,39% 50%,45% 34%,51% 46%,57% 32%,63% 44%,69% 36%,75% 48%,
    81% 40%,87% 50%,93% 43%,100% 48%,100% 100%
  );
}
[data-theme="dark"] .sil-near{
  background:linear-gradient(to bottom,rgba(3,12,28,.93),rgba(2,7,16,1));
}

/* ── Ocean / sea layer — daytime: vivid teal ── */
.sil-ocean{
  position:absolute;bottom:0;left:0;right:0;height:14%;
  z-index:4;pointer-events:none;
  background:linear-gradient(to bottom,rgba(20,130,175,.82),rgba(8,88,130,.97));
}
[data-theme="dark"] .sil-ocean{
  background:linear-gradient(to bottom,rgba(0,95,135,.78),rgba(0,55,88,.97));
}

/* water shimmer line at the horizon */
.sil-ocean::after{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent 5%,rgba(255,255,220,.4) 30%,rgba(255,255,255,.75) 50%,rgba(255,255,220,.4) 70%,transparent 95%);
  animation:waterShimmer 4s ease-in-out infinite;
}
[data-theme="dark"] .sil-ocean::after{
  background:linear-gradient(90deg,transparent 5%,rgba(255,195,75,.28) 30%,rgba(255,220,120,.65) 50%,rgba(255,195,75,.28) 70%,transparent 95%);
}
@keyframes waterShimmer{
  0%,100%{opacity:.5;transform:scaleX(.85)}
  50%{opacity:1;transform:scaleX(1.08)}
}

/* ── Atmospheric haze / mist at horizon ── */
.sil-mist{
  position:absolute;bottom:12%;left:0;right:0;height:7%;
  z-index:5;pointer-events:none;
  background:linear-gradient(to bottom,transparent,rgba(200,240,255,.07),transparent);
  filter:blur(14px);
}
[data-theme="dark"] .sil-mist{
  background:linear-gradient(to bottom,transparent,rgba(255,170,90,.06),transparent);
}

/* ── Palm tree silhouettes ── */
.sil-palm-l{
  position:absolute;bottom:12%;left:-1%;
  width:16%;max-width:195px;height:54%;
  z-index:6;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;
  background-repeat:no-repeat;
  background-position:bottom left;
}
.sil-palm-r{
  position:absolute;bottom:10%;right:-1%;
  width:13%;max-width:160px;height:47%;
  z-index:6;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;
  background-repeat:no-repeat;
  background-position:bottom right;
  transform:scaleX(-1);
}

.hero-content{
  position:relative;z-index:10;
  max-width:780px;width:100%;
  display:flex;flex-direction:column;align-items:center;
  color:var(--hero-txt);
}
/* scroll hint */
.scroll-hint{ color:var(--hero-muted) }

/* pill badge */
.hero-pill{
  display:inline-flex;align-items:center;gap:8px;
  background:var(--hero-pill-bg);border:1px solid var(--hero-pill-border);
  border-radius:24px;padding:6px 16px;
  font-size:12px;font-weight:700;color:var(--hero-pill-txt);letter-spacing:.5px;
  margin-bottom:24px;
  animation:fadeUp .8s ease both;
}
.pulse{
  width:8px;height:8px;border-radius:50%;background:var(--g);flex-shrink:0;
  box-shadow:0 0 0 0 rgba(0,232,212,.7);
  animation:pulseRing 2s ease-out infinite;
}
@keyframes pulseRing{
  0%{box-shadow:0 0 0 0 rgba(0,232,212,.7)}
  70%{box-shadow:0 0 0 12px rgba(0,232,212,0)}
  100%{box-shadow:0 0 0 0 rgba(0,232,212,0)}
}

.hero-h1{
  font-size:clamp(38px,7.5vw,80px);
  font-weight:900;line-height:1.05;letter-spacing:-1.5px;
  margin-bottom:20px;
  color:var(--hero-txt);
  animation:fadeUp .8s .15s ease both;
}
.hero-h1 em{font-style:normal;color:var(--g);text-shadow:0 0 20px rgba(0,140,153,.28)}
[data-theme="dark"] .hero-h1 em{text-shadow:0 0 40px rgba(0,232,212,.5),0 0 80px rgba(0,232,212,.2)}
.hero-h1 .outline{
  -webkit-text-stroke:2px var(--hero-txt);
  color:transparent;opacity:.45;
}

.hero-sub{
  font-size:clamp(15px,2vw,18px);color:var(--hero-txt-2);line-height:1.7;
  max-width:540px;margin-bottom:36px;text-align:center;
  animation:fadeUp .8s .3s ease both;
}

/* ── Hero Image Viewer ─────────────────────────────────── */
.hero-visual{
  position:relative;width:100%;max-width:680px;
  border-radius:40px;overflow:hidden;
  aspect-ratio:16/9;
  box-shadow:0 40px 100px rgba(0,0,0,.35),0 0 0 1px rgba(255,255,255,.05);
  animation:fadeUp .8s .45s ease both;
  cursor:pointer;
}
@media(max-width:480px){.hero-visual{aspect-ratio:4/3;border-radius:24px}}

/* slides */
.hv-slide{
  position:absolute;inset:0;
  background-size:cover;background-position:center;
  opacity:0;
  transition:opacity 1s ease;
  transform:scale(1.06);
  transition:opacity 1s ease,transform 7s linear;
}
.hv-slide.active{opacity:1;transform:scale(1)}

/* dark vignette so glass text always readable */
.hv-vignette{
  position:absolute;inset:0;z-index:1;
  background:linear-gradient(
    to bottom,
    rgba(0,0,0,.1) 0%,
    transparent 35%,
    transparent 50%,
    rgba(0,0,0,.55) 100%
  );
}

/* top-left floating badge */
.hv-badge{
  position:absolute;top:14px;left:14px;z-index:3;
  display:flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.18);
  border:1px solid rgba(255,255,255,.3);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-radius:20px;padding:5px 12px;
  font-size:11px;font-weight:700;color:#fff;
  opacity:0;transform:translateY(-6px);
  transition:opacity .5s ease .3s,transform .5s ease .3s;
}
.hv-slide.active ~ .hv-badge,
.hv-badge.visible{opacity:1;transform:translateY(0)}

/* dots — top right */
.hv-dots{
  position:absolute;top:14px;right:14px;z-index:3;
  display:flex;gap:6px;align-items:center;
}
.hv-dot{
  width:6px;height:6px;border-radius:3px;
  background:rgba(255,255,255,.45);border:none;cursor:pointer;padding:0;
  transition:all .35s cubic-bezier(.4,0,.2,1);
}
.hv-dot.active{width:22px;background:#fff}

/* arrow buttons */
.hv-arrow{
  position:absolute;top:50%;z-index:3;
  transform:translateY(-50%);
  width:38px;height:38px;border-radius:50%;
  background:rgba(255,255,255,.15);
  border:1px solid rgba(255,255,255,.28);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  color:#fff;font-size:17px;font-weight:700;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  opacity:0;transition:opacity .25s,background .2s,transform .2s;
  user-select:none;
}
.hero-visual:hover .hv-arrow{opacity:1}
.hv-arrow.prev{left:12px}
.hv-arrow.next{right:12px}
.hv-arrow:hover{background:rgba(255,255,255,.28);transform:translateY(-50%) scale(1.1)}
.hv-arrow:active{transform:translateY(-50%) scale(.95)}

/* glassmorphism info card — bottom */
.hv-glass{
  position:absolute;bottom:14px;left:14px;right:14px;z-index:3;
  background:rgba(10,20,30,.45);
  border:1px solid rgba(255,255,255,.18);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-radius:16px;padding:14px 16px;
  display:flex;align-items:center;justify-content:space-between;gap:12px;
  transform:translateY(8px);opacity:0;
  transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease;
}
.hv-glass.visible{transform:translateY(0);opacity:1}
.hv-info{flex:1;min-width:0}
.hv-name{
  font-size:17px;font-weight:900;color:#fff;
  line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
@media(max-width:400px){.hv-name{font-size:14px}}
.hv-tag{font-size:11px;color:rgba(255,255,255,.65);margin-top:2px}
.hv-from{
  font-size:11px;color:rgba(255,255,255,.5);margin-top:6px;
  display:flex;align-items:baseline;gap:5px;
}
.hv-from strong{font-size:15px;font-weight:800;color:var(--g)}
.hv-cta{
  padding:10px 20px;border-radius:11px;flex-shrink:0;
  background:linear-gradient(135deg,var(--acc),#d96800);
  border:none;color:#fff;font-size:13px;font-weight:800;
  cursor:pointer;white-space:nowrap;
  box-shadow:0 4px 18px rgba(255,145,0,.42);
  transition:all .18s;text-decoration:none;
  display:inline-flex;align-items:center;
}
@media(max-width:400px){.hv-cta{padding:8px 14px;font-size:12px}}
.hv-cta:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,145,0,.58)}

/* trust pills */
.hero-trust{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px;justify-content:center;animation:fadeUp .8s .6s ease both}
.t-pill{
  display:flex;align-items:center;gap:6px;
  background:var(--hero-pill-bg);border:1px solid var(--hero-pill-border);
  border-radius:24px;padding:6px 14px;
  font-size:12px;color:var(--hero-txt);font-weight:600;opacity:.85;
}

/* scroll indicator */
.scroll-hint{
  display:flex;flex-direction:column;align-items:center;gap:8px;
  font-size:10px;color:var(--hero-muted);letter-spacing:.8px;text-transform:uppercase;
  animation:fadeUp 1s 1.2s ease both;pointer-events:none;
  margin-top:28px;
}
.scroll-arrow{
  width:24px;height:40px;border:2px solid var(--hero-muted);border-radius:12px;
  display:flex;justify-content:center;padding-top:6px;
}
.scroll-dot{
  width:4px;height:8px;border-radius:2px;background:var(--g);
  animation:scrollDot 2s ease-in-out infinite;
}
@keyframes scrollDot{0%,100%{transform:translateY(0);opacity:1}50%{transform:translateY(12px);opacity:.3}}

@keyframes fadeUp{
  from{opacity:0;transform:translateY(24px)}
  to{opacity:1;transform:translateY(0)}
}

/* ═══════════════════════════════════════════════════════════
   STATS BAR
═══════════════════════════════════════════════════════════ */
.stats-bar{
  background:var(--stats-bg);border-top:1px solid var(--border);border-bottom:1px solid var(--border);
  padding:0 24px;
  display:grid;grid-template-columns:repeat(2,1fr);
  transition:background .3s;
}
@media(min-width:640px){.stats-bar{grid-template-columns:repeat(4,1fr);padding:0 64px}}
.stat-item{
  padding:28px 16px;text-align:center;
  border-right:1px solid var(--border);
}
.stat-item:last-child,.stat-item:nth-child(2){border-right:none}
@media(min-width:640px){
  .stat-item{border-right:1px solid var(--border)}
  .stat-item:last-child{border-right:none}
  .stat-item:nth-child(2){border-right:1px solid var(--border)}
}
.stat-num{font-size:28px;font-weight:900;color:var(--txt);letter-spacing:-1px;line-height:1}
.stat-num span{color:var(--g)}
.stat-label{font-size:12px;color:var(--muted);margin-top:4px;letter-spacing:.3px}

/* ═══════════════════════════════════════════════════════════
   SECTIONS COMMON
═══════════════════════════════════════════════════════════ */
.sec{padding:72px 24px}
@media(min-width:768px){.sec{padding:96px 64px;max-width:1280px;margin:0 auto}}
.sec-eyebrow{
  display:block;
  font-size:11px;font-weight:800;color:var(--g);letter-spacing:1.5px;text-transform:uppercase;
  margin-bottom:12px;text-align:center;
}
.sec-title{
  font-size:clamp(26px,4vw,44px);font-weight:900;letter-spacing:-.8px;line-height:1.1;
  margin-bottom:12px;color:var(--txt);text-align:center;
}
.sec-sub{
  font-size:16px;color:var(--muted);line-height:1.7;max-width:540px;
  text-align:center;margin-left:auto;margin-right:auto;
}

/* reveal on scroll */
.reveal{opacity:0;transform:translateY(32px);transition:opacity .7s ease,transform .7s ease}
.reveal.in{opacity:1;transform:none}
.reveal-l{opacity:0;transform:translateX(-32px);transition:opacity .7s ease,transform .7s ease}
.reveal-l.in{opacity:1;transform:none}
.reveal-r{opacity:0;transform:translateX(32px);transition:opacity .7s ease,transform .7s ease}
.reveal-r.in{opacity:1;transform:none}
.d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}.d4{transition-delay:.4s}

/* ═══════════════════════════════════════════════════════════
   HOW IT WORKS
═══════════════════════════════════════════════════════════ */
.steps-wrap{background:var(--bg-2);transition:background .3s}
.steps{display:grid;gap:24px;margin-top:48px}
@media(min-width:640px){.steps{grid-template-columns:repeat(3,1fr)}}
.step{
  background:var(--step-bg);border:1px solid var(--border);
  border-radius:20px;padding:28px 24px;
  transition:border-color .25s,transform .25s,background .3s;
  box-shadow:var(--shadow-card);text-align:left;
}
.step:hover{border-color:var(--g);transform:translateY(-6px);box-shadow:var(--glow-teal),0 10px 32px rgba(0,0,0,.14)}
.step-num{
  width:44px;height:44px;border-radius:12px;
  background:linear-gradient(135deg,var(--card-bg-hover),transparent);
  border:1px solid var(--border-md);
  display:flex;align-items:center;justify-content:center;
  font-size:18px;font-weight:900;color:var(--g);margin-bottom:16px;
  box-shadow:var(--glow-teal);
}
.step-title{font-size:17px;font-weight:800;margin-bottom:8px;color:var(--txt)}
.step-body{font-size:14px;color:var(--muted);line-height:1.7}

/* ═══════════════════════════════════════════════════════════
   DESTINATIONS
═══════════════════════════════════════════════════════════ */
.dest-grid{
  display:grid;
  grid-template-columns:repeat(2,1fr);
  gap:12px;margin-top:32px;
}
@media(min-width:640px){.dest-grid{grid-template-columns:repeat(3,1fr)}}
@media(min-width:1024px){.dest-grid{grid-template-columns:repeat(6,1fr)}}
.dest-card{
  position:relative;border-radius:var(--r);overflow:hidden;
  aspect-ratio:2/3;cursor:pointer;
  transition:transform .3s ease,box-shadow .3s ease;
}
.dest-card:hover{transform:scale(1.03);box-shadow:0 20px 60px rgba(0,0,0,.55),0 0 0 2px rgba(0,232,212,.35)}
.dest-card:hover .dest-img{transform:scale(1.08)}
.dest-img{
  position:absolute;inset:0;transition:transform .6s ease;
  background:var(--bg-3);
}
.dest-img img{object-position:center}
.dest-overlay{
  position:absolute;inset:0;
  background:linear-gradient(to top,rgba(0,0,0,.85) 0%,rgba(0,0,0,.1) 60%,transparent 100%);
}
.dest-body{position:absolute;bottom:0;left:0;right:0;padding:14px 12px}
.dest-name{font-size:14px;font-weight:800}
.dest-from{font-size:11px;color:rgba(255,255,255,.6);margin-top:2px}
.dest-hot{
  position:absolute;top:10px;left:10px;
  background:var(--acc);font-size:9px;font-weight:800;
  padding:3px 8px;border-radius:6px;letter-spacing:.5px;
}

/* ═══════════════════════════════════════════════════════════
   SERVICES / FEATURES
═══════════════════════════════════════════════════════════ */
.feats{display:grid;gap:16px;margin-top:48px}
@media(min-width:640px){.feats{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.feats{grid-template-columns:repeat(4,1fr)}}
.feat{
  background:var(--card-bg);border:1px solid var(--border);
  border-radius:20px;padding:28px 22px;
  transition:all .25s;cursor:default;box-shadow:var(--shadow-card);text-align:left;
}
.feat:hover{background:var(--card-bg-hover);border-color:var(--g);transform:translateY(-4px);box-shadow:var(--glow-teal),0 8px 28px rgba(0,0,0,.12)}
.feat-icon{
  font-size:28px;margin-bottom:16px;
  width:52px;height:52px;border-radius:14px;
  background:var(--card-bg-hover);display:flex;align-items:center;justify-content:center;
  border:1px solid var(--border);transition:box-shadow .25s;
}
.feat:hover .feat-icon{box-shadow:var(--glow-teal)}
.feat-title{font-size:16px;font-weight:800;margin-bottom:8px;color:var(--txt)}
.feat-body{font-size:13px;color:var(--muted);line-height:1.7}

/* ═══════════════════════════════════════════════════════════
   MARQUEE
═══════════════════════════════════════════════════════════ */
.marquee-wrap{
  overflow:hidden;border-top:1px solid var(--border);border-bottom:1px solid var(--border);
  background:var(--marquee-bg);padding:16px 0;transition:background .3s;
}
.marquee-track{
  display:flex;gap:0;white-space:nowrap;
  animation:marquee 24s linear infinite;
}
.marquee-track:hover{animation-play-state:paused}
.m-item{
  display:inline-flex;align-items:center;gap:10px;
  padding:0 32px;font-size:13px;font-weight:700;color:var(--muted);letter-spacing:.3px;
  border-right:1px solid var(--border);
}
.m-item span{color:var(--g);font-size:16px}
@keyframes marquee{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ═══════════════════════════════════════════════════════════
   TESTIMONIALS
═══════════════════════════════════════════════════════════ */
.reviews-wrap{background:var(--reviews-bg);transition:background .3s}
.reviews{display:grid;gap:16px;margin-top:48px}
@media(min-width:640px){.reviews{grid-template-columns:repeat(3,1fr)}}
.review{
  background:var(--card-bg);border:1px solid var(--border);
  border-radius:20px;padding:24px;
  border-left:3px solid var(--border-md);
  transition:border-color .25s,background .3s,box-shadow .25s;box-shadow:var(--shadow-card);
  text-align:left;
}
.review:hover{border-color:var(--g);border-left-color:var(--g);box-shadow:var(--glow-teal),0 6px 20px rgba(0,0,0,.1)}
.review-stars{color:#FFB800;font-size:14px;margin-bottom:12px;letter-spacing:2px}
.review-body{font-size:14px;color:var(--txt-2);line-height:1.7;margin-bottom:16px}
.review-author{display:flex;align-items:center;gap:10px}
.review-av{
  width:38px;height:38px;border-radius:50%;overflow:hidden;flex-shrink:0;
  border:2px solid var(--border-md);background:var(--bg-3);
  box-shadow:var(--glow-teal);
}
.review-name{font-size:13px;font-weight:700;color:var(--txt)}
.review-loc{font-size:11px;color:var(--muted);margin-top:1px}

/* ═══════════════════════════════════════════════════════════
   CTA BANNER
═══════════════════════════════════════════════════════════ */
.cta-banner{
  position:relative;overflow:hidden;
  padding:72px 24px;text-align:center;
  background:var(--cta-banner);
  border-top:1px solid rgba(0,201,177,.2);border-bottom:1px solid rgba(0,201,177,.2);
  transition:background .3s;
}
@media(min-width:768px){.cta-banner{padding:96px 64px}}
.cta-bg-orb1{
  position:absolute;width:700px;height:700px;border-radius:50%;
  background:radial-gradient(circle,rgba(0,232,212,.18) 0%,transparent 65%);
  top:-250px;left:-150px;pointer-events:none;filter:blur(80px);
  animation:orbFloat1 14s ease-in-out infinite alternate;
}
.cta-bg-orb2{
  position:absolute;width:500px;height:500px;border-radius:50%;
  background:radial-gradient(circle,rgba(130,0,240,.15) 0%,transparent 65%);
  bottom:-120px;right:-80px;pointer-events:none;filter:blur(80px);
  animation:orbFloat2 18s ease-in-out infinite alternate-reverse;
}
.cta-content{position:relative;z-index:1}
.cta-title{font-size:clamp(28px,5vw,52px);font-weight:900;letter-spacing:-1px;margin-bottom:16px;color:var(--txt)}
.cta-title em{font-style:normal;color:var(--g)}
.cta-sub{font-size:16px;color:var(--txt-2);margin-bottom:32px}
.cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-cta-main{
  padding:16px 36px;border-radius:14px;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  font-size:16px;font-weight:800;color:#fff;border:none;cursor:pointer;
  box-shadow:0 8px 32px rgba(0,232,212,.38),0 0 0 1px rgba(0,232,212,.22);
  transition:all .22s;position:relative;overflow:hidden;
}
.btn-cta-main::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent 0%,rgba(255,255,255,.22) 50%,transparent 100%);
  transform:translateX(-100%);transition:transform .52s ease;
}
.btn-cta-main:hover{transform:translateY(-3px);box-shadow:0 16px 48px rgba(0,232,212,.48),0 0 0 1px rgba(0,232,212,.35)}
.btn-cta-main:hover::before{transform:translateX(100%)}
.btn-cta-ghost{
  padding:16px 36px;border-radius:14px;
  border:1.5px solid var(--border-md);
  font-size:16px;font-weight:800;color:var(--txt);background:transparent;cursor:pointer;
  transition:all .2s;
}
.btn-cta-ghost:hover{border-color:var(--g);background:var(--card-bg-hover)}
[data-theme="dark"] .btn-cta-ghost{color:#fff;border-color:rgba(255,255,255,.22)}
[data-theme="dark"] .btn-cta-ghost:hover{border-color:#fff;background:rgba(255,255,255,.08)}

/* ═══════════════════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════════════════ */
.footer{
  background:var(--footer-bg);border-top:1px solid var(--border);
  padding:48px 24px 32px;transition:background .3s;
}
@media(min-width:768px){.footer{padding:64px 64px 40px}}
.footer-top{
  display:grid;gap:40px;margin-bottom:48px;
}
@media(min-width:768px){.footer-top{grid-template-columns:2fr 1fr 1fr 1fr}}
.footer-brand{max-width:280px}
.footer-logo{display:flex;align-items:center;gap:10px;font-size:18px;font-weight:900;margin-bottom:12px}
.footer-logo-icon{
  width:32px;height:32px;border-radius:8px;
  background:linear-gradient(135deg,var(--g),var(--gdk));
  display:flex;align-items:center;justify-content:center;font-size:14px;
  box-shadow:0 0 16px rgba(0,232,212,.3);
}
.footer-desc{font-size:14px;color:var(--muted);line-height:1.7}
.footer-col-title{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--g);margin-bottom:16px}
.footer-links{display:flex;flex-direction:column;gap:10px}
.footer-links a{font-size:14px;color:var(--muted);transition:color .15s}
.footer-links a:hover{color:var(--txt)}
.footer-bottom{
  display:flex;flex-direction:column;gap:12px;
  padding-top:24px;border-top:1px solid var(--border);
  font-size:12px;color:var(--muted);
}
@media(min-width:640px){.footer-bottom{flex-direction:row;justify-content:space-between}}
.footer-socials{display:flex;gap:12px}
.social-btn{
  width:34px;height:34px;border-radius:8px;
  border:1px solid var(--border);background:rgba(255,255,255,.04);
  display:flex;align-items:center;justify-content:center;font-size:15px;
  transition:all .15s;cursor:pointer;
}
.social-btn:hover{border-color:var(--g);background:var(--card-bg-hover)}

/* ═══════════════════════════════════════════════════════════
   TROPICAL SECTION TRANSITIONS & ISLAND EFFECTS
═══════════════════════════════════════════════════════════ */

/* ── Stats Bar: shimmer accent line at bottom ── */
.stats-bar{position:relative}
.stats-bar::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent 5%,var(--g) 35%,var(--gdk) 65%,transparent 95%);
  opacity:.45;
}

/* ── Marquee Band: wave-cut top & bottom ── */
.marquee-wrap{position:relative;overflow:hidden}
.marquee-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:32px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 0%,100% 0%,100% 40%,
    93% 58%,86% 36%,79% 56%,72% 34%,65% 52%,58% 32%,51% 50%,
    44% 30%,37% 48%,30% 28%,23% 46%,15% 28%,7% 44%,0% 30%
  );
}
.marquee-wrap::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:32px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 100%,100% 100%,100% 60%,
    93% 42%,86% 64%,79% 44%,72% 66%,65% 48%,58% 68%,51% 50%,
    44% 70%,37% 52%,30% 72%,23% 54%,15% 72%,7% 56%,0% 70%
  );
}

/* ── Steps Section: sky-blue gradient bg + island-wave dividers ── */
.steps-wrap{
  position:relative;overflow:hidden;
  background:linear-gradient(180deg,var(--bg-2) 0%,var(--bg-3) 100%);
}
.steps-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:56px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 0%,100% 0%,100% 36%,
    95% 55%,88% 35%,80% 57%,72% 36%,64% 58%,56% 38%,48% 60%,
    40% 40%,32% 62%,24% 42%,16% 60%,8% 38%,0% 54%
  );
}
.steps-wrap::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:52px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 100%,100% 100%,100% 64%,
    94% 44%,87% 64%,80% 46%,72% 66%,65% 46%,57% 68%,50% 48%,
    42% 68%,34% 50%,26% 68%,18% 50%,10% 66%,2% 48%,0% 62%
  );
}
.steps-wrap .step{position:relative;z-index:3}

/* ── Destinations Wrap: wave from steps bottom ── */
.dest-wrap{position:relative;overflow:hidden;background:var(--bg-body)}
.dest-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:52px;z-index:2;pointer-events:none;
  background:var(--bg-3);
  clip-path:polygon(
    0% 0%,100% 0%,100% 38%,
    94% 56%,86% 38%,78% 58%,70% 40%,62% 60%,54% 42%,46% 62%,
    38% 44%,30% 64%,22% 46%,14% 62%,6% 44%,0% 58%
  );
}

/* ── Features Wrap: alternating teal bg ── */
.feats-wrap{position:relative;overflow:hidden;background:var(--bg-2)}
.feats-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:52px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 0%,100% 0%,100% 38%,
    94% 56%,87% 38%,79% 58%,71% 40%,63% 60%,55% 42%,47% 62%,
    39% 44%,31% 62%,23% 44%,15% 60%,7% 44%,0% 56%
  );
}
.feats-wrap::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:48px;z-index:2;pointer-events:none;
  background:var(--reviews-bg);
  clip-path:polygon(
    0% 100%,100% 100%,100% 62%,
    93% 44%,86% 62%,79% 44%,72% 64%,64% 46%,56% 66%,48% 48%,
    40% 66%,32% 48%,24% 66%,16% 50%,8% 64%,0% 48%
  );
}
.feats-wrap .feat{position:relative;z-index:3}

/* ── Reviews Section: tropical evening gradient ── */
.reviews-wrap{
  position:relative;overflow:hidden;
  background:linear-gradient(180deg,var(--bg-3) 0%,var(--bg-2) 100%);
}
.reviews-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:52px;z-index:2;pointer-events:none;
  background:var(--bg-2);
  clip-path:polygon(
    0% 0%,100% 0%,100% 40%,
    94% 58%,86% 40%,78% 60%,70% 42%,62% 62%,54% 44%,46% 64%,
    38% 46%,30% 66%,22% 48%,14% 64%,6% 46%,0% 60%
  );
}
.reviews-wrap::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:48px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 100%,100% 100%,100% 62%,
    94% 44%,87% 62%,80% 44%,72% 64%,64% 46%,56% 66%,48% 48%,
    40% 66%,32% 48%,24% 64%,16% 48%,8% 62%,0% 46%
  );
}
.reviews-wrap .review{position:relative;z-index:3}

/* ── CTA Banner: mini island panorama ── */
.cta-banner{
  position:relative;overflow:hidden;
  border-top:none;border-bottom:none;
}
/* mountain silhouette ridgeline */
.cta-banner::before{
  content:'';position:absolute;bottom:0;left:0;right:0;height:44%;
  z-index:0;pointer-events:none;
  background:linear-gradient(to bottom,rgba(0,70,95,.1),rgba(0,50,80,.24));
  clip-path:polygon(
    0% 100%,0% 48%,4% 36%,9% 48%,14% 29%,20% 42%,26% 24%,33% 38%,
    40% 20%,47% 34%,54% 16%,61% 30%,68% 14%,76% 28%,83% 18%,91% 32%,
    96% 22%,100% 28%,100% 100%
  );
}
/* ocean layer */
.cta-banner::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:14%;
  z-index:0;pointer-events:none;
  background:linear-gradient(to bottom,rgba(0,120,165,.18),rgba(0,90,138,.32));
}
/* ocean shimmer */
.cta-ocean-shimmer{
  position:absolute;bottom:13%;left:0;right:0;height:2px;
  z-index:1;pointer-events:none;
  background:linear-gradient(90deg,transparent 5%,rgba(255,255,220,.32) 28%,rgba(255,255,255,.62) 50%,rgba(255,255,220,.32) 72%,transparent 95%);
  animation:waterShimmer 4s ease-in-out infinite;
}
/* palm trees in CTA */
.cta-palm-l,.cta-palm-r{
  position:absolute;bottom:13%;z-index:1;pointer-events:none;opacity:.2;
}
.cta-palm-l{
  left:-1%;width:14%;max-width:160px;height:56%;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23005060' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;background-repeat:no-repeat;background-position:bottom left;
}
.cta-palm-r{
  right:-1%;width:11%;max-width:135px;height:48%;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23005060' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;background-repeat:no-repeat;background-position:bottom right;
  transform:scaleX(-1);
}
[data-theme="dark"] .cta-palm-l,[data-theme="dark"] .cta-palm-r{opacity:.14}
.cta-content{position:relative;z-index:5}
/* CTA orbs — theme-aware */
.cta-bg-orb1{background:radial-gradient(circle,rgba(0,140,153,.18) 0%,transparent 65%)}
.cta-bg-orb2{background:radial-gradient(circle,rgba(0,100,130,.14) 0%,transparent 65%)}
[data-theme="dark"] .cta-bg-orb1{background:radial-gradient(circle,rgba(0,232,212,.18) 0%,transparent 65%)}
[data-theme="dark"] .cta-bg-orb2{background:radial-gradient(circle,rgba(130,0,240,.15) 0%,transparent 65%)}
/* Fix CTA banner border */
.cta-banner{border-top:none;border-bottom:none}
/* Raise the banner border to use a shimmer wave top */
.cta-banner .cta-wave-top{
  position:absolute;top:0;left:0;right:0;height:52px;z-index:1;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 0%,100% 0%,100% 36%,
    94% 56%,86% 38%,78% 56%,70% 38%,62% 58%,54% 40%,46% 60%,
    38% 42%,30% 60%,22% 42%,14% 58%,6% 40%,0% 54%
  );
}

/* ── Footer: wave top + ocean gradient ── */
.footer{position:relative;overflow:hidden}
.footer::before{
  content:'';position:absolute;top:0;left:0;right:0;height:52px;z-index:2;pointer-events:none;
  background:var(--bg-body);
  clip-path:polygon(
    0% 0%,100% 0%,100% 38%,
    94% 56%,86% 38%,78% 58%,70% 40%,62% 58%,54% 40%,46% 60%,
    38% 40%,30% 58%,22% 40%,14% 56%,6% 40%,0% 54%
  );
}
.footer-logo-icon{box-shadow:var(--glow-teal)}

/* ── Button CTA main: use CSS var glow ── */
.btn-cta-main{
  box-shadow:var(--glow-teal),0 0 0 1px var(--border-md);
}
.btn-cta-main:hover{
  transform:translateY(-3px);
  box-shadow:var(--glow-teal),0 10px 36px rgba(0,0,0,.18),0 0 0 1px var(--border-md);
}

/* ── Destination card glow hover: theme-aware ── */
.dest-card:hover{
  transform:scale(1.03);
  box-shadow:0 16px 48px rgba(0,0,0,.32),0 0 0 2px var(--g);
}
"""

JS = """
// ── Theme (runs before DOMContentLoaded to prevent flash) ──
(function() {
  const saved = localStorage.getItem('gegow-theme');
  document.documentElement.setAttribute('data-theme', saved || 'light');
})();

document.addEventListener('DOMContentLoaded', () => {
  // Theme toggle
  const html   = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  function syncToggle() {
    const isDark = html.getAttribute('data-theme') === 'dark';
    if (toggle) toggle.textContent = isDark ? '☀️' : '🌙';
  }
  syncToggle();
  if (toggle) {
    toggle.addEventListener('click', () => {
      const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('gegow-theme', next);
      syncToggle();
    });
  }

  // Navbar scroll state
  const nav = document.querySelector('.nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hamburger / mobile drawer
  const hamburger = document.getElementById('nav-hamburger');
  const drawer    = document.getElementById('nav-drawer');
  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => {
      const isOpen = drawer.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
    // Close on link click
    drawer.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        drawer.classList.remove('open');
        hamburger.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
    // Close on outside click
    document.addEventListener('click', e => {
      if (!nav.contains(e.target) && !drawer.contains(e.target)) {
        drawer.classList.remove('open');
        hamburger.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  // Scroll reveal
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal,.reveal-l,.reveal-r').forEach(el => io.observe(el));

  // ── Hero Image Viewer ────────────────────────────────────
  const slides   = document.querySelectorAll('.hv-slide');
  const dots     = document.querySelectorAll('.hv-dot');
  const glass    = document.querySelector('.hv-glass');
  const badge    = document.querySelector('.hv-badge');
  const nameEl   = document.querySelector('.hv-name');
  const tagEl    = document.querySelector('.hv-tag');
  const fromEl   = document.querySelector('.hv-from h3,.hv-from strong');
  const ctaEl    = document.querySelector('.hv-cta');

  const SLIDES_DATA = JSON.parse(document.getElementById('hv-data').textContent);
  let current = 0, timer = null;

  function showSlide(idx, instant) {
    slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
    const d = SLIDES_DATA[idx];
    // animate glass card out then in
    if (!instant) {
      if (glass) { glass.classList.remove('visible'); }
      if (badge) { badge.classList.remove('visible'); }
    }
    setTimeout(() => {
      if (nameEl) nameEl.textContent = d.name;
      if (tagEl)  tagEl.textContent  = d.tag;
      if (fromEl) fromEl.textContent = d.price;
      if (badge)  badge.textContent  = d.badge;
      if (glass)  glass.classList.add('visible');
      if (badge)  badge.classList.add('visible');
    }, instant ? 0 : 300);
    current = idx;
  }

  function next() { showSlide((current + 1) % slides.length); }
  function prev() { showSlide((current - 1 + slides.length) % slides.length); }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(next, 4500);
  }

  // dot clicks
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => { showSlide(i); startTimer(); });
  });

  // arrow clicks
  const btnPrev = document.querySelector('.hv-arrow.prev');
  const btnNext = document.querySelector('.hv-arrow.next');
  if (btnPrev) btnPrev.addEventListener('click', (e) => { e.stopPropagation(); prev(); startTimer(); });
  if (btnNext) btnNext.addEventListener('click', (e) => { e.stopPropagation(); next(); startTimer(); });

  // pause on hover
  const heroVisual = document.querySelector('.hero-visual');
  if (heroVisual) {
    heroVisual.addEventListener('mouseenter', () => clearInterval(timer));
    heroVisual.addEventListener('mouseleave', startTimer);
    // swipe support
    let touchX = 0;
    heroVisual.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, { passive: true });
    heroVisual.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 40) { dx < 0 ? next() : prev(); startTimer(); }
    });
  }

  showSlide(0, true);
  startTimer();

  // Stat counter
  const statEls = document.querySelectorAll('[data-count]');
  const statIO = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target, end = +el.dataset.count, suf = el.dataset.suf || '';
      let start = 0;
      const step = end / 60;
      const timer = setInterval(() => {
        start = Math.min(start + step, end);
        el.textContent = (start >= 1000 ? (start / 1000).toFixed(1) + 'K' : Math.round(start)) + suf;
        if (start >= end) clearInterval(timer);
      }, 16);
      statIO.unobserve(el);
    });
  }, { threshold: 0.5 });
  statEls.forEach(el => statIO.observe(el));

  // ── PWA Install ──────────────────────────────────────────
  const btnNav    = document.getElementById('btn-install-nav');
  const btnDrawer = document.getElementById('btn-install-drawer');
  const btnHero   = document.getElementById('btn-install-hero');
  const btnIos    = document.getElementById('btn-install-ios');
  const iosModal  = document.getElementById('ios-modal');
  const iosClose  = document.getElementById('ios-close');

  const isIOS        = /iphone|ipad|ipod/i.test(navigator.userAgent);
  const isStandalone = window.navigator.standalone || window.matchMedia('(display-mode: standalone)').matches;

  // Platform visibility
  if (!isIOS && btnIos)  btnIos.style.display  = 'none';
  if (isIOS  && btnHero) btnHero.style.display = 'none';

  // Already installed — update UI immediately
  if (isStandalone) {
    if (btnHero) { btnHero.textContent = '✓ Installed'; btnHero.classList.add('installed'); }
    [btnNav, btnDrawer].forEach(b => b && b.classList.add('hide'));
  }

  const guideModal = document.getElementById('install-guide-modal');
  const guideClose = document.getElementById('install-guide-close');

  function showInstallGuide() {
    if (!guideModal) return;
    const isAndroid = /android/i.test(navigator.userAgent);
    guideModal.querySelectorAll('.ig-tab-btn').forEach(b => b.classList.remove('active'));
    guideModal.querySelectorAll('.ig-panel').forEach(p => p.classList.remove('active'));
    const tab = isIOS ? 'ios' : isAndroid ? 'android' : 'desktop';
    const btn = guideModal.querySelector('[data-tab="' + tab + '"]');
    const panel = document.getElementById('ig-' + tab);
    if (btn)   btn.classList.add('active');
    if (panel) panel.classList.add('active');
    guideModal.classList.add('open');
  }

  function onInstallAccepted(outcome) {
    if (outcome === 'accepted') {
      if (btnHero) { btnHero.textContent = '✓ Installing…'; btnHero.classList.add('installed'); }
      [btnNav, btnDrawer].forEach(b => b && b.classList.add('hide'));
    }
  }

  function triggerAndroidInstall() {
    // Use the global handler from sw-register.js
    const triggered = window.triggerPWAInstall && window.triggerPWAInstall(onInstallAccepted);
    if (!triggered) showInstallGuide();  // fallback: show manual guide
  }

  function triggerIOSInstall() {
    if (iosModal) iosModal.classList.add('open');
    else showInstallGuide();
  }

  // When sw-register.js fires pwa-install-ready, enable the Android button
  window.addEventListener('pwa-install-ready', () => {
    if (btnHero && !isIOS) {
      btnHero.textContent = '📲 Install App';
      btnHero.classList.remove('installed');
    }
    [btnNav, btnDrawer].forEach(b => b && b.classList.remove('hide'));
  });

  if (btnHero)   btnHero.addEventListener('click',   triggerAndroidInstall);
  if (btnIos)    btnIos.addEventListener('click',    triggerIOSInstall);
  if (btnNav)    btnNav.addEventListener('click',    triggerAndroidInstall);
  if (btnDrawer) btnDrawer.addEventListener('click', triggerAndroidInstall);
  if (iosClose)  iosClose.addEventListener('click',  () => iosModal && iosModal.classList.remove('open'));
  if (iosModal)  iosModal.addEventListener('click',  (e) => { if (e.target === iosModal) iosModal.classList.remove('open'); });

  const closeGuide = () => guideModal && guideModal.classList.remove('open');
  if (guideClose) guideClose.addEventListener('click', closeGuide);
  const guideCloseBottom = document.getElementById('install-guide-close-bottom');
  if (guideCloseBottom) guideCloseBottom.addEventListener('click', closeGuide);
  if (guideModal) guideModal.addEventListener('click', (e) => { if (e.target === guideModal) closeGuide(); });
  guideModal && guideModal.querySelectorAll('.ig-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      guideModal.querySelectorAll('.ig-tab-btn').forEach(b => b.classList.remove('active'));
      guideModal.querySelectorAll('.ig-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const panel = document.getElementById('ig-' + btn.dataset.tab);
      if (panel) panel.classList.add('active');
    });
  });

  window.addEventListener('pwa-installed', () => {
    if (btnHero) { btnHero.textContent = '✓ Installed'; btnHero.classList.add('installed'); }
    [btnNav, btnDrawer].forEach(b => b && b.classList.add('hide'));
  });
});
"""


_DRAWER_LINKS = [
    ("✈️", "Flights",    "/book?type=flight"),
    ("🏨", "Hotels",     "/book?type=hotel"),
    ("🗺️", "Tours",      "/book?type=tour"),
    ("🛍️", "Gear Shop",  "/gear"),
    ("🏢", "B2B Portal", "/b2b"),
]

def _nav():
    drawer_links = [
        A(Span(icon), Span(label), href=href, cls="drawer-link")
        for icon, label, href in _DRAWER_LINKS
    ]
    return Nav(
        # Logo
        A(
            Div("✈", cls="nav-logo-icon"),
            Span("Gegow"),
            href="/", cls="nav-logo",
        ),
        # Desktop center links
        Div(
            A("Flights", href="/book?type=flight"),
            A("Hotels",  href="/book?type=hotel"),
            A("Tours",   href="/book?type=tour"),
            A("Gear",    href="/gear"),
            A("B2B",     href="/b2b"),
            cls="nav-links",
        ),
        # Right side
        Div(
            Button("📲 Install", cls="btn-install", id="btn-install-nav", title="Install Gegow"),
            Button("☀️", cls="theme-toggle", id="theme-toggle", title="Toggle light/dark"),
            A("Sign in",     href="/login", cls="btn-nav-ghost"),
            A("Get started", href="/login", cls="btn-nav-solid"),
            # Hamburger (mobile)
            Button(
                Span(), Span(), Span(),
                cls="nav-hamburger", id="nav-hamburger",
                **{"aria-label": "Menu"},
            ),
            cls="nav-right",
        ),
        cls="nav",
        id="navbar",
    ), Div(
        *drawer_links,
        Div(cls="drawer-divider"),
        Button("📲  Install App", cls="btn-install drawer-install", id="btn-install-drawer"),
        Div(
            A("Sign in",     href="/login", cls="btn-ghost-full"),
            A("Get started", href="/login", cls="btn-solid-full"),
            cls="drawer-auth",
        ),
        cls="nav-drawer",
        id="nav-drawer",
    )


_HV_SLIDES = [
    {"name": "El Nido, Palawan",  "tag": "Island Paradise",       "price": "₱4,850",  "badge": "🇵🇭 Local Favorite", "href": "/book?type=tour&tour_dest=Palawan",   "img": IMGS["palawan"]},
    {"name": "Boracay",           "tag": "White Beach Escape",    "price": "₱3,290",  "badge": "🔥 Trending",        "href": "/book?type=tour&tour_dest=Boracay",   "img": IMGS["boracay"]},
    {"name": "Siargao",           "tag": "Surfing Capital of PH", "price": "₱3,990",  "badge": "🌊 Adventure",       "href": "/book?type=tour&tour_dest=Siargao",   "img": IMGS["siargao"]},
    {"name": "Singapore",         "tag": "City of Gardens",       "price": "₱8,500",  "badge": "✈️ International",   "href": "/book?type=tour&tour_dest=Singapore", "img": IMGS["singapore"]},
    {"name": "Tokyo, Japan",      "tag": "Culture & Street Food", "price": "₱18,900", "badge": "🌸 Asia's Best",     "href": "/book?type=tour&tour_dest=Tokyo",     "img": IMGS["tokyo"]},
    {"name": "Bali, Indonesia",   "tag": "Spiritual & Scenic",    "price": "₱12,400", "badge": "🌺 Relaxation",      "href": "/book",                               "img": IMGS["bali"]},
]


def _hero():
    first = _HV_SLIDES[0]
    slides = [
        Div(cls=f"hv-slide{'  active' if i == 0 else ''}",
            style=f"background-image:url('{s['img']}')")
        for i, s in enumerate(_HV_SLIDES)
    ]
    dots = [Div(cls=f"hv-dot{'  active' if i == 0 else ''}", role="button") for i in range(len(_HV_SLIDES))]

    return Section(
        Div(cls="hero-bg"),
        Div(cls="hero-grid"),
        Div(cls="orb orb-1"),
        Div(cls="orb orb-2"),
        Div(cls="orb orb-3"),
        Div(cls="sil-far"),
        Div(cls="sil-mid"),
        Div(cls="sil-near"),
        Div(cls="sil-ocean"),
        Div(cls="sil-mist"),
        Div(cls="sil-palm-l"),
        Div(cls="sil-palm-r"),
        Div(
            Div(Div(cls="pulse"), "🇵🇭  Philippines' #1 Digital Travel Agency", cls="hero-pill"),
            H1(
                Span("Your Next", cls="outline"), " Adventure",
                Span(" Starts Here", style="display:block;color:var(--g)"),
                cls="hero-h1",
            ),
            P("Flights, hotels & tours — handpicked for the best value. Book in minutes, travel in style.", cls="hero-sub"),
            # ── Image Viewer ──────────────────────────────────
            Div(
                *slides,
                Div(cls="hv-vignette"),
                # badge top-left
                Div(first["badge"], cls="hv-badge visible"),
                # dot nav top-right
                Div(*dots, cls="hv-dots"),
                # arrows
                Button("‹", cls="hv-arrow prev"),
                Button("›", cls="hv-arrow next"),
                # glassmorphism card bottom
                Div(
                    Div(
                        Div(first["name"], cls="hv-name"),
                        Div(first["tag"],  cls="hv-tag"),
                        Div("From ", H3(first["price"], cls="", style="display:inline;font-size:15px;font-weight:800;color:var(--g)"), cls="hv-from"),
                        cls="hv-info",
                    ),
                    A("Login →", href="/login", cls="hv-cta"),
                    cls="hv-glass visible",
                ),
                # data island for JS
                Div(_json.dumps(_HV_SLIDES), id="hv-data", style="display:none"),
                cls="hero-visual",
            ),
            Div(
                Div(Span("✅"), "Best Price Guarantee", cls="t-pill"),
                Div(Span("🔒"), "Secure Booking",       cls="t-pill"),
                Div(Span("💬"), "24/7 Support",         cls="t-pill"),
                cls="hero-trust",
            ),
            Div(
                Div(Div(cls="scroll-dot"), cls="scroll-arrow"),
                "scroll",
                cls="scroll-hint",
            ),
            cls="hero-content",
        ),
        cls="hero",
    )


def _stats():
    return Div(
        Div(Span("50K", **{"data-count": "50000", "data-suf": "+"}), cls="stat-num"),
        Div("Happy Travelers", cls="stat-label"),
        cls="stat-item",
    ), Div(
        Div(Span("200", **{"data-count": "200", "data-suf": "+"}), cls="stat-num"),
        Div("Destinations", cls="stat-label"),
        cls="stat-item",
    ), Div(
        Div(Span("₱0", **{"data-count": "0", "data-suf": ""}), Span(" fees", style="font-size:16px;color:var(--muted)"), cls="stat-num"),
        Div("Hidden Charges", cls="stat-label"),
        cls="stat-item",
    ), Div(
        Div(Span("4.9", **{"data-count": "5", "data-suf": "★"}), cls="stat-num"),
        Div("Average Rating", cls="stat-label"),
        cls="stat-item",
    )


def _marquee():
    items = [
        ("✈️", "Domestic Flights from ₱999"),
        ("🏨", "Hotel Deals up to 40% off"),
        ("🗺️", "Palawan Group Tours"),
        ("🛍️", "Travel Gear Essentials"),
        ("🌏", "International Packages"),
        ("🎫", "Instant E-Vouchers"),
        ("💳", "Flexible Payment"),
        ("🔔", "Price Drop Alerts"),
    ]
    # Double for infinite scroll
    all_items = items * 2
    return Div(
        Div(
            *[Div(Span(icon), text, cls="m-item") for icon, text in all_items],
            cls="marquee-track",
        ),
        cls="marquee-wrap",
    )


def _steps():
    return Div(
        Div(
            Span("How it works", cls="sec-eyebrow"),
            H2("Book in 3 Simple Steps", cls="sec-title reveal"),
            P("No agent visits. No lengthy phone calls. Plan and book your trip entirely online.", cls="sec-sub reveal d1"),
            Div(
                Div(Div("01", cls="step-num"), H3("Choose Your Trip", cls="step-title"),
                    P("Select from flights, hotels, tours, or build a full itinerary with our 5-step wizard.", cls="step-body"), cls="step reveal d1"),
                Div(Div("02", cls="step-num"), H3("Review & Pay",     cls="step-title"),
                    P("Transparent pricing with our markup shown. Secure checkout with multiple payment options.", cls="step-body"), cls="step reveal d2"),
                Div(Div("03", cls="step-num"), H3("Travel & Enjoy",   cls="step-title"),
                    P("Get your e-vouchers instantly. Store them in My Suitcase for offline access anytime.", cls="step-body"), cls="step reveal d3"),
                cls="steps",
            ),
            cls="sec",
        ),
        cls="steps-wrap",
    )


def _destinations():
    dests = [
        ("palawan",   "Palawan",   "from ₱2,499", True),
        ("boracay",   "Boracay",   "from ₱1,899", False),
        ("siargao",   "Siargao",   "from ₱2,199", True),
        ("singapore", "Singapore", "from ₱8,500", False),
        ("tokyo",     "Tokyo",     "from ₱14,999", False),
        ("bali",      "Bali",      "from ₱9,800",  True),
    ]
    cards = []
    for i, (key, name, price, hot) in enumerate(dests):
        card = A(
            Div(Div(style=f"position:absolute;inset:0;background-image:url({IMGS[key]});background-size:cover;background-position:center", cls="dest-img")),
            Div(cls="dest-overlay"),
            Div(Div(name, cls="dest-name"), Div(price, cls="dest-from"), cls="dest-body"),
            *([ Div("HOT", cls="dest-hot") ] if hot else []),
            href=f"/book?type=flight&dest={name.lower()}",
            cls=f"dest-card reveal d{min(i+1,4)}",
        )
        cards.append(card)

    return Div(
        Div(
            Span("Destinations", cls="sec-eyebrow"),
            H2("Popular in the Philippines & Asia", cls="sec-title reveal"),
            Div(*cards, cls="dest-grid"),
            cls="sec",
        ),
        cls="dest-wrap",
    )


def _features():
    feats = [
        ("✈️", "Flights",      "Domestic & international fares with ₱250–₱3,000+ profit markup built in."),
        ("🏨", "Hotels",       "Handpicked stays from budget hostels to 5-star resorts. Up to ₱1,000 markup/night."),
        ("🗺️", "Tours",        "Joiner & private tours across PH and Asia. ₱400–₱2,000+ markup per person."),
        ("🧳", "My Suitcase",  "Offline-ready storage for all your vouchers, schedules, and itineraries."),
        ("🛍️", "Gear Shop",    "Curated dropshipped travel essentials — luggage, adapters, organizers."),
        ("🏢", "B2B Portal",   "Dedicated portal for Manning Agencies and Corporate travel accounts."),
        ("🔒", "Secure Pay",   "SSL-encrypted checkout. Multiple payment methods supported."),
        ("📲", "PWA Ready",    "Install like an app. Works offline. Push notifications for deals."),
    ]
    return Div(
        Div(
            Span("Services", cls="sec-eyebrow"),
            H2("Everything a Traveler Needs", cls="sec-title reveal"),
            P("One platform for flights, stays, tours, and gear — built for Filipinos, priced right.", cls="sec-sub reveal d1"),
            Div(
                *[Div(Div(icon, cls="feat-icon"), H3(title, cls="feat-title"), P(body, cls="feat-body"), cls=f"feat reveal d{min(i%4+1,4)}")
                  for i, (icon, title, body) in enumerate(feats)],
                cls="feats",
            ),
            cls="sec",
        ),
        cls="feats-wrap",
    )


def _reviews():
    revs = [
        (IMGS["av1"], "Maria Santos",   "Cebu City",      "⭐⭐⭐⭐⭐", "Booked Palawan in 5 minutes. The price was way better than what I saw on other sites. My Suitcase saved my life when there was no signal!"),
        (IMGS["av2"], "Carlo Reyes",    "Manila",         "⭐⭐⭐⭐⭐", "Used the B2B portal for our company team outing. Setup was smooth and the markup is transparent. Will definitely use again."),
        (IMGS["av3"], "Ana Villanueva", "Davao City",     "⭐⭐⭐⭐⭐", "Siargao tour booked in one go. The 5-step wizard made it so easy. Got my e-voucher instantly on my phone."),
    ]
    cards = []
    for i, (av, name, loc, stars, body) in enumerate(revs):
        cards.append(Div(
            Div(stars, cls="review-stars"),
            P(f'"{body}"', cls="review-body"),
            Div(
                Div(style=f"width:38px;height:38px;border-radius:50%;overflow:hidden;background-image:url({av});background-size:cover;flex-shrink:0", cls="review-av"),
                Div(Div(name, cls="review-name"), Div(loc, cls="review-loc")),
                cls="review-author",
            ),
            cls=f"review reveal d{i+1}",
        ))
    return Div(
        Div(
            Span("Testimonials", cls="sec-eyebrow"),
            H2("Loved by Filipino Travelers", cls="sec-title reveal"),
            Div(*cards, cls="reviews"),
            cls="sec",
        ),
        cls="reviews-wrap",
    )


def _cta():
    return Section(
        Div(cls="cta-wave-top"),
        Div(cls="cta-bg-orb1"),
        Div(cls="cta-bg-orb2"),
        Div(cls="cta-palm-l"),
        Div(cls="cta-palm-r"),
        Div(cls="cta-ocean-shimmer"),
        Div(
            H2(Span("Plan Your Next Trip", cls="reveal"), Span(" with Gegow", style="display:block;color:var(--g)", cls="reveal d1"), cls="cta-title"),
            P("Join 50,000+ travelers who book smarter. Sign up free today.", cls="cta-sub reveal d2"),
            Div(
                A("Start Planning →", href="/login", cls="btn-cta-main reveal d2"),
                A("Explore Deals",    href="/dashboard", cls="btn-cta-ghost reveal d3"),
                cls="cta-btns",
            ),
            cls="cta-content",
        ),
        cls="cta-banner",
    )


def _footer():
    return Footer(
        # Install strip
        Div(
            Div(
                Div("📲", cls="footer-install-icon"),
                Div(
                    Div("Add Gegow to your Home Screen", cls="footer-install-title"),
                    Div("Works offline · No app store · Free", cls="footer-install-sub"),
                ),
                cls="footer-install-left",
            ),
            Div(
                Button("📲 Install App", cls="btn-install-cta", id="btn-install-hero"),
                Button("🍎 Add on iPhone", cls="btn-ios-install", id="btn-install-ios"),
                cls="footer-install-btns",
            ),
            id="install-card",
            cls="footer-install",
        ),
        Div(
            Div(
                Div(Div("✈", cls="footer-logo-icon"), Span("Gegow"), cls="footer-logo"),
                P("Philippines' digital-in-pocket travel agency. Flights, hotels, tours, and gear — all in one app.", cls="footer-desc"),
                cls="footer-brand",
            ),
            Div(
                Div("Product", cls="footer-col-title"),
                Div(A("Flights", href="/book?type=flight"), A("Hotels", href="/book?type=hotel"),
                    A("Tours", href="/book?type=tour"), A("Gear Shop", href="/gear"), cls="footer-links"),
            ),
            Div(
                Div("Company", cls="footer-col-title"),
                Div(A("About", href="#"), A("B2B Portal", href="/b2b"),
                    A("Careers", href="#"), A("Blog", href="#"), cls="footer-links"),
            ),
            Div(
                Div("Support", cls="footer-col-title"),
                Div(A("Help Center", href="#"), A("Contact Us", href="#"),
                    A("Privacy Policy", href="#"), A("Terms of Service", href="#"), cls="footer-links"),
            ),
            cls="footer-top",
        ),
        Div(
            Span("© 2026 Gegow Travel · Made with ❤️ in the Philippines"),
            Div(
                Div("𝕏", cls="social-btn"),
                Div("f", cls="social-btn"),
                Div("in", cls="social-btn", style="font-size:11px;font-weight:700"),
                cls="footer-socials",
            ),
            cls="footer-bottom",
        ),
        cls="footer",
    )


def landing_page():
    return Html(
        Head(
            Title("Gegow — Your Digital Travel Agency"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            Meta(name="description", content="Book flights, hotels and tours in the Philippines and Asia. Best prices, instant vouchers, offline access."),
            Meta(name="theme-color", content="#006D77"),
            Meta(name="apple-mobile-web-app-capable", content="yes"),
            Meta(name="apple-mobile-web-app-status-bar-style", content="black-translucent"),
            Meta(name="apple-mobile-web-app-title", content="Gegow"),
            Link(rel="manifest", href="/static/manifest.json"),
            Link(rel="apple-touch-icon", href="/static/icons/icon-192.png"),
            Link(rel="icon", type="image/png", sizes="192x192", href="/static/icons/icon-192.png"),
            Style(CSS),
            Script(src="/static/sw-register.js", defer=True),
        ),
        Body(
            *_nav(),
            _hero(),
            Div(*_stats(), cls="stats-bar"),
            _marquee(),
            _steps(),
            _destinations(),
            _features(),
            _reviews(),
            _cta(),
            _footer(),
            # iOS install modal
            Div(
                Div(
                    Div("Install Gegow on iPhone", cls="ios-sheet-title"),
                    Div("Add Gegow to your home screen for the best experience — works offline too.", cls="ios-sheet-sub"),
                    Div(
                        Div(Div("1", cls="ios-step-num"), Span("Tap the Share button (□↑) at the bottom of Safari"), cls="ios-step"),
                        Div(Div("2", cls="ios-step-num"), Span('Scroll down and tap "Add to Home Screen"'), cls="ios-step"),
                        Div(Div("3", cls="ios-step-num"), Span('Tap "Add" — Gegow appears on your home screen!'), cls="ios-step"),
                        cls="ios-steps",
                    ),
                    Button("Got it!", cls="ios-close", id="ios-close"),
                    cls="ios-sheet",
                ),
                cls="ios-modal",
                id="ios-modal",
            ),
            # Generic Install Guide modal (Android / Desktop fallback)
            Div(
                Div(
                    Div(
                        Div("Install Gegow", cls="ig-title"),
                        Button("✕", cls="ig-close-btn", id="install-guide-close"),
                        cls="ig-header",
                    ),
                    Div("Add Gegow to your home screen — no app store needed.", cls="ig-sub"),
                    Div(
                        Button("📱 Android", cls="ig-tab-btn active", **{"data-tab": "android"}),
                        Button("🍎 iPhone", cls="ig-tab-btn", **{"data-tab": "ios"}),
                        Button("💻 Desktop", cls="ig-tab-btn", **{"data-tab": "desktop"}),
                        cls="ig-tabs",
                    ),
                    # Android panel
                    Div(
                        Div(Div("1", cls="ig-step-num"), Div(Span("Open Gegow in Chrome"), Span("(this browser)", cls="ig-step-hint"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("2", cls="ig-step-num"), Div(Span("Tap the 3-dot menu ⋮ at the top right"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("3", cls="ig-step-num"), Div(Span('"Add to Home Screen" or "Install app"'), Span("Then tap Add/Install to confirm", cls="ig-step-hint"), cls="ig-step-text"), cls="ig-step"),
                        id="ig-android", cls="ig-panel active",
                    ),
                    # iOS panel
                    Div(
                        Div(Div("1", cls="ig-step-num"), Div(Span("Open Gegow in Safari"), Span("Must use Safari on iPhone/iPad", cls="ig-step-hint"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("2", cls="ig-step-num"), Div(Span("Tap the Share button □↑ at the bottom"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("3", cls="ig-step-num"), Div(Span('"Add to Home Screen" then tap "Add"'), cls="ig-step-text"), cls="ig-step"),
                        id="ig-ios", cls="ig-panel",
                    ),
                    # Desktop panel
                    Div(
                        Div(Div("1", cls="ig-step-num"), Div(Span("Open Gegow in Chrome or Edge"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("2", cls="ig-step-num"), Div(Span("Look for the install icon ⊕ in the address bar"), Span("Or click ⋮ menu → Cast, save, share → Install", cls="ig-step-hint"), cls="ig-step-text"), cls="ig-step"),
                        Div(Div("3", cls="ig-step-num"), Div(Span("Click Install — Gegow opens like a native app!"), cls="ig-step-text"), cls="ig-step"),
                        id="ig-desktop", cls="ig-panel",
                    ),
                    Button("Got it!", cls="ig-got-it", id="install-guide-close-bottom"),
                    cls="ig-sheet",
                ),
                cls="install-guide-modal",
                id="install-guide-modal",
            ),
            Script(JS),
        ),
    )
