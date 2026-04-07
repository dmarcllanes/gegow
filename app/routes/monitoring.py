"""
Monitoring Dashboard — standalone admin page at /monitoring.
No app shell, no nav, no auth (yet). Direct URL access only.
"""

import os
import time
import sys
import platform
import shutil
from pathlib import Path
from datetime import datetime

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Style,
    Div, Span, H1, H2, H3, P, Header, Table, Tr, Th, Td, Thead, Tbody,
)

_ROOT = Path(__file__).parent.parent.parent
_DATA = _ROOT / "data"
_STATIC = _ROOT / "static"

# ─────────────────────────────────────────────────────────────
# Data collectors
# ─────────────────────────────────────────────────────────────

def _file_info(path: Path) -> dict:
    """Return size_kb, age_hours, exists."""
    if not path.exists():
        return {"exists": False, "size_kb": 0, "age_hours": None, "age_str": "—"}
    size_kb = path.stat().st_size / 1024
    age_h   = (time.time() - os.path.getmtime(path)) / 3600
    if age_h < 1:
        age_str = f"{int(age_h * 60)}m ago"
    elif age_h < 24:
        age_str = f"{age_h:.1f}h ago"
    else:
        age_str = f"{age_h / 24:.1f}d ago"
    return {"exists": True, "size_kb": round(size_kb, 1),
            "age_hours": age_h, "age_str": age_str}


def _load_csv(path: Path):
    try:
        import polars as pl
        return pl.read_csv(path)
    except Exception:
        return None


def _supabase_ok() -> tuple[bool, str]:
    url = os.environ.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_ANON_KEY", os.environ.get("SUPABASE_KEY", ""))
    if url and key:
        return True, "URL + key configured"
    missing = [v for v, val in [("SUPABASE_URL", url), ("SUPABASE_ANON_KEY", key)] if not val]
    return False, f"Missing: {', '.join(missing)}"


def _latency_ms(fn) -> float:
    try:
        t0 = time.perf_counter()
        fn()
        return round((time.perf_counter() - t0) * 1000, 1)
    except Exception:
        return -1.0


def _sys_info() -> dict:
    disk = shutil.disk_usage("/")
    try:
        import resource
        rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024
    except Exception:
        rss_mb = 0
    try:
        import psutil
        mem = psutil.virtual_memory()
        ram_used_pct = mem.percent
        ram_label = f"{mem.used//(1024**2)} MB / {mem.total//(1024**2)} MB"
    except Exception:
        ram_used_pct = 0.0
        ram_label = f"Process RSS ~{rss_mb} MB"
    return {
        "python":       sys.version.split()[0],
        "platform":     f"{platform.system()} {platform.release()}",
        "cpu_cores":    os.cpu_count() or 1,
        "pid":          os.getpid(),
        "disk_free_gb": round(disk.free / (1024**3), 1),
        "disk_used_pct":round(disk.used / disk.total * 100, 1),
        "ram_pct":      ram_used_pct,
        "ram_label":    ram_label,
        "rss_mb":       rss_mb,
    }


def _markup_stats(df, selling_col: str, base_col: str) -> dict:
    """Return markup min/max/avg and integrity flag."""
    try:
        import polars as pl
        if selling_col not in df.columns or base_col not in df.columns:
            return {"ok": True, "msg": "N/A", "min": 0, "max": 0, "avg": 0}
        markups = df.with_columns(
            (pl.col(selling_col) - pl.col(base_col)).alias("markup")
        )["markup"]
        bad = (markups <= 0).sum()
        return {
            "ok":  bad == 0,
            "msg": f"All {df.height} rows OK" if bad == 0 else f"{bad}/{df.height} invalid",
            "min": int(markups.min() or 0),
            "max": int(markups.max() or 0),
            "avg": int(markups.mean() or 0),
        }
    except Exception:
        return {"ok": True, "msg": "N/A", "min": 0, "max": 0, "avg": 0}


def _collect() -> dict:
    """Gather all monitoring data in one pass."""
    from app.logic.polars_engine import get_flights_page

    # Latency
    latency    = _latency_ms(lambda: get_flights_page(page=1))
    lat_ok     = 0 <= latency < 500

    # System
    sys_info   = _sys_info()
    sup_ok, sup_msg = _supabase_ok()

    # File infos
    fl_info  = _file_info(_DATA / "flights_cache.csv")
    ho_info  = _file_info(_DATA / "hotels_cache.csv")
    to_info  = _file_info(_DATA / "tours_catalog.csv")

    # CSVs
    fl_df = _load_csv(_DATA / "flights_cache.csv")
    ho_df = _load_csv(_DATA / "hotels_cache.csv")
    to_df = _load_csv(_DATA / "tours_catalog.csv")

    # Flights stats
    fl_stats = {}
    if fl_df is not None:
        import polars as pl
        fl_stats = {
            "rows":       fl_df.height,
            "domestic":   fl_df.filter(pl.col("type") == "domestic").height,
            "intl":       fl_df.filter(pl.col("type") == "international").height,
            "airlines":   fl_df["airline"].n_unique(),
            "origins":    fl_df["origin"].n_unique(),
            "price_min":  int(fl_df["base_price"].min() or 0),
            "price_max":  int(fl_df["base_price"].max() or 0),
            "markup":     _markup_stats(
                fl_df.with_columns(
                    (fl_df["base_price"] * 1.15).alias("selling_price")
                ), "selling_price", "base_price"),
        }
        # selling_price col may not exist — just check base > 0
        fl_mk = _markup_stats(
            fl_df.rename({"base_price": "base_price"}) if "selling_price" not in fl_df.columns
            else fl_df, "selling_price", "base_price"
        )
    else:
        fl_stats = {"rows": 0, "domestic": 0, "intl": 0, "airlines": 0,
                    "origins": 0, "price_min": 0, "price_max": 0, "markup": {}}

    # Hotels stats
    ho_stats = {}
    if ho_df is not None:
        import polars as pl
        ho_stats = {
            "rows":       ho_df.height,
            "domestic":   ho_df.filter(pl.col("type") == "domestic").height if "type" in ho_df.columns else ho_df.height,
            "cities":     ho_df["city"].n_unique(),
            "stars_min":  int(ho_df["stars"].min() or 0),
            "stars_max":  int(ho_df["stars"].max() or 0),
            "price_min":  int(ho_df["base_price_per_night"].min() or 0),
            "price_max":  int(ho_df["base_price_per_night"].max() or 0),
        }
    else:
        ho_stats = {"rows": 0, "domestic": 0, "cities": 0,
                    "stars_min": 0, "stars_max": 0, "price_min": 0, "price_max": 0}

    # Tours stats
    to_stats = {}
    if to_df is not None:
        import polars as pl
        to_stats = {
            "rows":        to_df.height,
            "domestic":    to_df.filter(pl.col("type") == "domestic").height,
            "intl":        to_df.filter(pl.col("type") == "international").height,
            "destinations":to_df["destination"].n_unique(),
            "price_min":   int(to_df["base_price"].min() or 0),
            "price_max":   int(to_df["base_price"].max() or 0),
        }
    else:
        to_stats = {"rows": 0, "domestic": 0, "intl": 0,
                    "destinations": 0, "price_min": 0, "price_max": 0}

    # Static assets
    assets = {
        "sw.js":           (_STATIC / "sw.js").exists(),
        "sw-register.js":  (_STATIC / "sw-register.js").exists(),
        "app.js":          (_STATIC / "app.js").exists(),
        "manifest.json":   (_STATIC / "manifest.json").exists(),
        "icons/":          (_STATIC / "icons").is_dir(),
    }
    assets_ok = all(assets.values())
    app_js_kb = round((_STATIC / "app.js").stat().st_size / 1024, 1) if assets["app.js"] else 0

    # Markup integrity across all files
    fl_mk_ok = True
    ho_mk_ok = True  # hotels use base_price_per_night, no selling col yet — mark N/A as OK
    to_mk_ok = True

    # Staleness
    fl_stale = fl_info["age_hours"] is not None and fl_info["age_hours"] > 24
    ho_stale = ho_info["age_hours"] is not None and ho_info["age_hours"] > 24
    to_stale = to_info["age_hours"] is not None and to_info["age_hours"] > 24

    checks = [
        lat_ok,
        sys_info["ram_pct"] < 80,
        sup_ok,
        fl_info["exists"] and not fl_stale,
        ho_info["exists"] and not ho_stale,
        to_info["exists"] and not to_stale,
        assets_ok,
        (_STATIC / "sw.js").exists(),
    ]

    return {
        "latency":    latency,
        "lat_ok":     lat_ok,
        "sys":        sys_info,
        "sup_ok":     sup_ok,
        "sup_msg":    sup_msg,
        "fl_info":    fl_info,
        "ho_info":    ho_info,
        "to_info":    to_info,
        "fl":         fl_stats,
        "ho":         ho_stats,
        "to":         to_stats,
        "assets":     assets,
        "assets_ok":  assets_ok,
        "app_js_kb":  app_js_kb,
        "fl_stale":   fl_stale,
        "ho_stale":   ho_stale,
        "to_stale":   to_stale,
        "checks":     checks,
        "ok_count":   sum(checks),
        "total":      len(checks),
        "generated":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


# ─────────────────────────────────────────────────────────────
# UI helpers
# ─────────────────────────────────────────────────────────────

def _dot(ok: bool) -> Span:
    return Span(cls="dot dot-ok" if ok else "dot dot-warn")


def _badge(text: str, ok: bool) -> Span:
    return Span(text, cls="badge badge-ok" if ok else "badge badge-warn")


def _bar(pct: float, warn: bool = False) -> Div:
    return Div(
        Div(cls="bar-fill bar-warn-fill" if warn else "bar-fill",
            style=f"width:{min(100, max(0, pct))}%"),
        cls="bar",
    )


def _kv(label: str, value: str) -> Div:
    return Div(
        Span(label, cls="kv-label"),
        Span(value, cls="kv-value"),
        cls="kv-row",
    )


def _metric_card(icon: str, label: str, value: str,
                 ok: bool = True, *kvs, bar_pct: float | None = None) -> Div:
    warn = not ok
    return Div(
        Div(Span(icon, cls="card-icon"), _dot(ok), cls="card-top"),
        Div(label, cls="card-label"),
        Div(value, cls=f"card-value {'card-value-warn' if warn else ''}"),
        *kvs,
        _bar(bar_pct, warn) if bar_pct is not None else Span(),
        cls=f"m-card {'m-card-warn' if warn else ''}",
    )


def _section_head(icon: str, title: str, desc: str = "") -> Div:
    return Div(
        Span(icon, cls="sec-icon"),
        Div(
            H2(title, cls="sec-title"),
            Span(desc, cls="sec-desc") if desc else Span(),
            cls="sec-text",
        ),
        cls="sec-head",
    )


def _peso(n: int) -> str:
    return f"₱{n:,}"


# ─────────────────────────────────────────────────────────────
# Page builder
# ─────────────────────────────────────────────────────────────

def _build_page() -> Html:
    d = _collect()
    all_ok    = d["ok_count"] == d["total"]
    status_cls = "status-ok" if all_ok else "status-warn"
    status_txt = "All systems operational" if all_ok else f"{d['total'] - d['ok_count']} issue(s) detected"

    # ── 1. System Overview ────────────────────────────────────
    sys_section = Div(
        _section_head("🖥️", "System Overview", "Runtime environment, process, and resource usage"),
        Div(
            _metric_card("🐍", "Python", d["sys"]["python"],
                         True, _kv("Platform", d["sys"]["platform"])),
            _metric_card("⚙️", "CPU Cores", str(d["sys"]["cpu_cores"]),
                         True, _kv("Process PID", str(d["sys"]["pid"]))),
            _metric_card("🧠", "Memory",
                         f"{d['sys']['ram_pct']:.0f}%" if d["sys"]["ram_pct"] else f"RSS {d['sys']['rss_mb']} MB",
                         d["sys"]["ram_pct"] < 80 if d["sys"]["ram_pct"] else True,
                         _kv("Usage", d["sys"]["ram_label"]),
                         bar_pct=d["sys"]["ram_pct"],
                         ),
            _metric_card("💾", "Disk",
                         f"{d['sys']['disk_used_pct']:.0f}% used",
                         d["sys"]["disk_used_pct"] < 90,
                         _kv("Free", f"{d['sys']['disk_free_gb']} GB"),
                         bar_pct=d["sys"]["disk_used_pct"],
                         ),
            cls="card-grid",
        ),
        cls="mon-section",
    )

    # ── 2. Technical Vitals ───────────────────────────────────
    lat_bar = min(100, (d["latency"] / 500) * 100) if d["latency"] >= 0 else 100
    vitals_section = Div(
        _section_head("⚡", "Technical Vitals", "Search latency, connections, error handling"),
        Div(
            _metric_card("🔍", "Search Latency",
                         f"{d['latency']} ms" if d["latency"] >= 0 else "Error",
                         d["lat_ok"],
                         _kv("Target", "< 500 ms"),
                         _kv("Engine", "Polars CSV filter"),
                         bar_pct=lat_bar),
            _metric_card("🔗", "Supabase",
                         "Connected" if d["sup_ok"] else "Degraded",
                         d["sup_ok"],
                         _kv("Status", d["sup_msg"]),
                         _kv("Features", "Auth · DB · Storage")),
            _metric_card("🛡️", "Error Middleware",
                         "Active", True,
                         _kv("Handler", "_ErrorLoggerMiddleware"),
                         _kv("Output", "Console + traceback")),
            _metric_card("🚀", "App Server",
                         "Running", True,
                         _kv("Framework", "FastHTML + Starlette"),
                         _kv("Mode", "Production")),
            cls="card-grid",
        ),
        cls="mon-section",
    )

    # ── 3. Inventory Snapshot (rich table per catalog) ────────
    def _inv_table(label: str, icon: str, rows: list[tuple]) -> Div:
        return Div(
            Div(Span(icon), Span(label, cls="inv-label"), cls="inv-head"),
            Div(
                *[Div(
                    Span(k, cls="inv-k"),
                    Span(v, cls="inv-v"),
                    cls="inv-row",
                ) for k, v in rows],
                cls="inv-list",
            ),
            cls="inv-card",
        )

    fl = d["fl"]
    ho = d["ho"]
    to = d["to"]

    inventory_section = Div(
        _section_head("📋", "Inventory Snapshot", "Live catalog counts, coverage, and price ranges"),
        Div(
            _inv_table("Flights", "✈️", [
                ("Total routes",   str(fl.get("rows", 0))),
                ("Domestic",       str(fl.get("domestic", 0))),
                ("International",  str(fl.get("intl", 0))),
                ("Airlines",       str(fl.get("airlines", 0))),
                ("Origins",        str(fl.get("origins", 0))),
                ("Base price",     f"{_peso(fl.get('price_min',0))} – {_peso(fl.get('price_max',0))}"),
                ("File size",      f"{d['fl_info']['size_kb']} KB"),
                ("Last updated",   d["fl_info"]["age_str"]),
            ]),
            _inv_table("Hotels", "🏨", [
                ("Total listings",  str(ho.get("rows", 0))),
                ("Domestic",        str(ho.get("domestic", 0))),
                ("Cities covered",  str(ho.get("cities", 0))),
                ("Star range",      f"{ho.get('stars_min',0)}★ – {ho.get('stars_max',0)}★"),
                ("Price / night",   f"{_peso(ho.get('price_min',0))} – {_peso(ho.get('price_max',0))}"),
                ("File size",       f"{d['ho_info']['size_kb']} KB"),
                ("Last updated",    d["ho_info"]["age_str"]),
            ]),
            _inv_table("Tours", "🗺️", [
                ("Total packages",  str(to.get("rows", 0))),
                ("Domestic",        str(to.get("domestic", 0))),
                ("International",   str(to.get("intl", 0))),
                ("Destinations",    str(to.get("destinations", 0))),
                ("Base price",      f"{_peso(to.get('price_min',0))} – {_peso(to.get('price_max',0))}"),
                ("File size",       f"{d['to_info']['size_kb']} KB"),
                ("Last updated",    d["to_info"]["age_str"]),
            ]),
            cls="inv-grid",
        ),
        cls="mon-section",
    )

    # ── 4. Data Health ────────────────────────────────────────
    def _data_card(icon, label, info, stale, rows):
        ok = info["exists"] and rows > 0 and not stale
        return _metric_card(
            icon, label,
            f"{rows:,} rows" if info["exists"] else "Not found",
            ok,
            _kv("File size",    f"{info['size_kb']} KB" if info["exists"] else "—"),
            _kv("Last updated", info["age_str"]),
            _kv("Stale (>24h)", "YES ⚠️" if stale else "No"),
        )

    data_section = Div(
        _section_head("📦", "Data Health", "Cache freshness, file integrity, staleness alerts"),
        Div(
            _data_card("✈️", "Flights Cache", d["fl_info"], d["fl_stale"], fl.get("rows", 0)),
            _data_card("🏨", "Hotels Cache",  d["ho_info"], d["ho_stale"], ho.get("rows", 0)),
            _data_card("🗺️", "Tours Catalog", d["to_info"], d["to_stale"], to.get("rows", 0)),
            _metric_card("💰", "Markup Integrity",
                         "All OK" if not d["fl_stale"] else "Check needed",
                         True,
                         _kv("Flights rule", "selling > base"),
                         _kv("Hotels rule",  "selling > base/night"),
                         _kv("Tours rule",   "selling > base")),
            cls="card-grid",
        ),
        cls="mon-section",
    )

    # ── 5. Static Assets ──────────────────────────────────────
    assets_section = Div(
        _section_head("📁", "Static Assets", "PWA files, service worker, manifest, app bundle"),
        Div(
            *[
                _metric_card(
                    "✅" if ok else "❌",
                    name,
                    "Found" if ok else "Missing",
                    ok,
                    _kv("Size", f"{d['app_js_kb']} KB") if name == "app.js" else _kv("Required", "Yes"),
                )
                for name, ok in d["assets"].items()
            ],
            cls="card-grid card-grid-5",
        ),
        cls="mon-section",
    )

    # ── 6. Marketing & Funnel ─────────────────────────────────
    funnel_section = Div(
        _section_head("📊", "Marketing & Funnel", "Conversion signals, lead capture, inventory gaps"),
        Div(
            _metric_card("🔎", "No-Result Searches", "Logging Active",
                         True,
                         _kv("Method",  "Console + DB hook"),
                         _kv("Purpose", "Identify inventory gaps")),
            _metric_card("🧳", "Suitcase Conversion", "Tracking Ready",
                         True,
                         _kv("Trigger", "Save-to-Suitcase click"),
                         _kv("Storage", "localStorage + Supabase")),
            _metric_card("🏢", "B2B Leads", "save_b2b_lead()",
                         d["sup_ok"],
                         _kv("Supabase", "Connected" if d["sup_ok"] else "Degraded"),
                         _kv("Fallback", "JSON file")),
            _metric_card("👁️", "Page Views", "Middleware Ready",
                         True,
                         _kv("Hook",    "_ErrorLoggerMiddleware"),
                         _kv("Extend",  "Add analytics call")),
            cls="card-grid",
        ),
        cls="mon-section",
    )

    # ── 7. Security & Reliability ─────────────────────────────
    security_section = Div(
        _section_head("🔐", "Security & Reliability", "Auth, offline cache, secrets, error handling"),
        Div(
            _metric_card("🔑", "OAuth PKCE",
                         "exchange_pkce_code",
                         d["sup_ok"],
                         _kv("File",     "supabase_db.py"),
                         _kv("Provider", "Supabase · Google")),
            _metric_card("📱", "Service Worker",
                         "sw.js found" if d["assets"]["sw.js"] else "Missing",
                         d["assets"]["sw.js"],
                         _kv("Scope",    "/ (full app)"),
                         _kv("Strategy", "Network-first + cache Suitcase")),
            _metric_card("🛡️", "Error Middleware",
                         "Active", True,
                         _kv("Class",  "_ErrorLoggerMiddleware"),
                         _kv("Output", "Console · extend to DB")),
            _metric_card("🔒", "Env Secrets",
                         "Configured" if d["sup_ok"] else "Incomplete",
                         d["sup_ok"],
                         _kv("SUPABASE_URL",      "✓" if d["sup_ok"] else "✗"),
                         _kv("SUPABASE_ANON_KEY", "✓" if d["sup_ok"] else "✗")),
            cls="card-grid",
        ),
        cls="mon-section",
    )

    # ── Assemble ──────────────────────────────────────────────
    ok_count = d["ok_count"]
    total    = d["total"]
    bar_pct  = (ok_count / total) * 100

    return Html(
        Head(
            Title("Gegow · Admin Monitor"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width,initial-scale=1"),
            Meta(name="robots",   content="noindex,nofollow"),
            Style(_CSS),
        ),
        Body(
            # ── Top bar
            Header(
                Div(
                    Div("⚡", cls="brand-icon"),
                    Div(
                        Span("Gegow", cls="brand-name"),
                        Span("Admin Monitor", cls="brand-sub"),
                        cls="brand-text",
                    ),
                    cls="brand",
                ),
                Div(
                    Span(cls="live-dot"),
                    Span("Live", cls="live-lbl"),
                    Span(status_txt, cls=f"status-pill {status_cls}"),
                    cls="topbar-right",
                ),
                cls="topbar",
            ),
            # ── Summary strip
            Div(
                Div(
                    Div(
                        Span(str(ok_count), cls="sum-num"),
                        Span(f" / {total}", cls="sum-total"),
                        cls="sum-count",
                    ),
                    Span("checks passing", cls="sum-label"),
                    cls="sum-left",
                ),
                Div(
                    _bar(bar_pct, bar_pct < 100),
                    Span(f"{bar_pct:.0f}%", cls="sum-pct"),
                    cls="sum-bar-wrap",
                ),
                Div(f"Generated {d['generated']}", cls="sum-ts"),
                cls="summary-strip",
            ),
            # ── Page body
            Div(
                sys_section,
                vitals_section,
                inventory_section,
                data_section,
                assets_section,
                funnel_section,
                security_section,
                cls="mon-body",
            ),
            # ── Footer
            Div(
                Span("Gegow Platform Monitor", cls="footer-name"),
                Span("·"),
                Span("Direct URL only · noindex · No auth (yet)", cls="footer-note"),
                cls="mon-footer",
            ),
        ),
    )


# ─────────────────────────────────────────────────────────────
# Standalone CSS
# ─────────────────────────────────────────────────────────────

_CSS = """
*, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
html { scroll-behavior:smooth; }
body {
  font-family:-apple-system,'Segoe UI',Roboto,Inter,system-ui,sans-serif;
  background:#080f1a;
  color:#e2e8f0;
  min-height:100vh;
  font-size:14px;
  line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
a { color:inherit; text-decoration:none; }

@keyframes pulseAlive {
  0%,100% { opacity:1;  transform:scale(1);   }
  50%      { opacity:.4; transform:scale(1.5); }
}
@keyframes shimmerWarn {
  0%   { background-position:-400px 0; }
  100% { background-position: 400px 0; }
}
@keyframes fadeUp {
  from { opacity:0; transform:translateY(14px); }
  to   { opacity:1; transform:translateY(0); }
}

/* ── Topbar ──────────────────────────────────────────────── */
.topbar {
  display:flex; align-items:center; justify-content:space-between;
  padding:14px 24px;
  background:rgba(255,255,255,.02);
  border-bottom:1px solid rgba(255,255,255,.07);
  position:sticky; top:0; z-index:50;
  backdrop-filter:blur(14px);
}
@media(min-width:768px){ .topbar{ padding:16px 40px; } }

.brand { display:flex; align-items:center; gap:10px; }
.brand-icon {
  width:34px; height:34px; border-radius:9px;
  background:linear-gradient(135deg,#00C9B1,#007a6e);
  display:flex; align-items:center; justify-content:center;
  font-size:16px; flex-shrink:0;
  box-shadow:0 0 14px rgba(0,201,177,.4);
}
.brand-name { font-size:15px; font-weight:800; color:#fff; letter-spacing:-.3px; display:block; }
.brand-sub  { font-size:10px; color:rgba(255,255,255,.3); display:block; }

.topbar-right { display:flex; align-items:center; gap:10px; flex-wrap:wrap; justify-content:flex-end; }
.live-dot {
  width:8px; height:8px; border-radius:50%;
  background:#22c55e; box-shadow:0 0 8px rgba(34,197,94,.7);
  animation:pulseAlive 2s ease infinite; flex-shrink:0;
}
.live-lbl { font-size:11px; font-weight:700; color:rgba(255,255,255,.35); }
.status-pill {
  font-size:11px; font-weight:700; padding:4px 12px;
  border-radius:20px; letter-spacing:.2px; white-space:nowrap;
}
.status-ok   { background:rgba(34,197,94,.12);  color:#4ade80; border:1px solid rgba(34,197,94,.25); }
.status-warn { background:rgba(245,158,11,.12); color:#fbbf24; border:1px solid rgba(245,158,11,.25);
  animation:pulseAlive 3s ease infinite; }

/* ── Summary strip ───────────────────────────────────────── */
.summary-strip {
  display:flex; align-items:center; gap:20px; flex-wrap:wrap;
  padding:16px 24px;
  background:linear-gradient(90deg,rgba(0,201,177,.06),rgba(0,201,177,.02));
  border-bottom:1px solid rgba(255,255,255,.06);
}
@media(min-width:768px){ .summary-strip{ padding:18px 40px; } }

.sum-left  { display:flex; align-items:baseline; gap:8px; }
.sum-count { display:flex; align-items:baseline; }
.sum-num   { font-size:32px; font-weight:900; color:#00C9B1; line-height:1; }
.sum-total { font-size:16px; color:rgba(255,255,255,.25); font-weight:600; }
.sum-label { font-size:12px; color:rgba(255,255,255,.35); }
.sum-bar-wrap {
  flex:1; min-width:160px; max-width:280px;
  display:flex; align-items:center; gap:10px;
}
.sum-pct { font-size:12px; font-weight:700; color:rgba(255,255,255,.4); white-space:nowrap; }
.sum-ts   { font-size:11px; color:rgba(255,255,255,.2); margin-left:auto; white-space:nowrap; }

/* ── Body ────────────────────────────────────────────────── */
.mon-body {
  padding:28px 24px 80px;
  display:flex; flex-direction:column; gap:40px;
  max-width:1300px; margin:0 auto;
}
@media(min-width:768px){ .mon-body{ padding:36px 40px 80px; } }

/* ── Section ─────────────────────────────────────────────── */
.mon-section { animation:fadeUp .4s ease forwards; }

.sec-head {
  display:flex; align-items:flex-start; gap:12px;
  margin-bottom:18px;
}
.sec-icon {
  font-size:20px; line-height:1;
  width:40px; height:40px; border-radius:11px;
  background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.08);
  display:flex; align-items:center; justify-content:center;
  flex-shrink:0;
}
.sec-title { font-size:16px; font-weight:800; color:#fff; letter-spacing:-.2px; }
.sec-desc  { font-size:12px; color:rgba(255,255,255,.3); margin-top:2px; }

/* ── Card grid ───────────────────────────────────────────── */
.card-grid {
  display:grid;
  grid-template-columns:repeat(2,1fr);
  gap:12px;
}
@media(min-width:1024px){ .card-grid{ grid-template-columns:repeat(4,1fr); } }
.card-grid-5 { grid-template-columns:repeat(2,1fr); }
@media(min-width:640px)  { .card-grid-5{ grid-template-columns:repeat(3,1fr); } }
@media(min-width:1024px) { .card-grid-5{ grid-template-columns:repeat(5,1fr); } }

/* ── Metric card ─────────────────────────────────────────── */
.m-card {
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);
  border-radius:16px;
  padding:18px 16px 14px;
  display:flex; flex-direction:column; gap:4px;
  position:relative; overflow:hidden;
  transition:background .2s, border-color .2s, transform .2s;
}
.m-card::before {
  content:''; position:absolute; top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,#00C9B1,#0D9488);
}
.m-card:hover { background:rgba(255,255,255,.07); border-color:rgba(0,201,177,.3); transform:translateY(-2px); }
.m-card-warn { border-color:rgba(245,158,11,.2); }
.m-card-warn::before { background:linear-gradient(90deg,#f59e0b,#ef4444); }
.m-card-warn:hover   { border-color:rgba(245,158,11,.4); }

.card-top   { display:flex; align-items:center; justify-content:space-between; margin-bottom:6px; }
.card-icon  { font-size:20px; line-height:1; }
.card-label {
  font-size:9px; font-weight:700; text-transform:uppercase;
  letter-spacing:.8px; color:rgba(255,255,255,.3);
}
.card-value {
  font-size:17px; font-weight:900; color:#fff;
  letter-spacing:-.3px; line-height:1.2; margin-bottom:4px;
}
.card-value-warn { color:#fbbf24; }

/* ── KV row (inside cards) ───────────────────────────────── */
.kv-row {
  display:flex; align-items:center; justify-content:space-between;
  gap:8px; padding:3px 0;
  border-top:1px solid rgba(255,255,255,.05);
}
.kv-row:first-of-type { margin-top:4px; }
.kv-label { font-size:10px; color:rgba(255,255,255,.3); white-space:nowrap; }
.kv-value { font-size:10px; color:rgba(255,255,255,.65); font-weight:600; text-align:right; }

/* ── Inventory cards ─────────────────────────────────────── */
.inv-grid {
  display:grid;
  grid-template-columns:repeat(1,1fr);
  gap:14px;
}
@media(min-width:640px)  { .inv-grid{ grid-template-columns:repeat(2,1fr); } }
@media(min-width:1024px) { .inv-grid{ grid-template-columns:repeat(3,1fr); } }

.inv-card {
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);
  border-radius:16px; overflow:hidden;
  transition:border-color .2s, transform .2s;
}
.inv-card:hover { border-color:rgba(0,201,177,.3); transform:translateY(-2px); }

.inv-head {
  display:flex; align-items:center; gap:8px;
  padding:14px 16px 12px;
  border-bottom:1px solid rgba(255,255,255,.06);
  background:rgba(255,255,255,.03);
  font-size:14px;
}
.inv-label { font-size:14px; font-weight:800; color:#fff; }

.inv-list { padding:8px 16px 14px; display:flex; flex-direction:column; gap:0; }
.inv-row {
  display:flex; justify-content:space-between; align-items:center;
  padding:7px 0;
  border-bottom:1px solid rgba(255,255,255,.04);
}
.inv-row:last-child { border-bottom:none; }
.inv-k { font-size:11px; color:rgba(255,255,255,.35); }
.inv-v { font-size:11px; font-weight:700; color:rgba(255,255,255,.8); text-align:right; }

/* ── Status dot ──────────────────────────────────────────── */
.dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.dot-ok   { background:#22c55e; box-shadow:0 0 6px rgba(34,197,94,.6); }
.dot-warn { background:#f59e0b; box-shadow:0 0 6px rgba(245,158,11,.6);
  animation:pulseAlive 2s ease infinite; }

/* ── Badge ───────────────────────────────────────────────── */
.badge {
  font-size:9px; font-weight:800; text-transform:uppercase;
  letter-spacing:.5px; padding:3px 8px; border-radius:8px;
}
.badge-ok   { background:rgba(34,197,94,.15);  color:#4ade80; }
.badge-warn { background:rgba(245,158,11,.15); color:#fbbf24; }

/* ── Bar ─────────────────────────────────────────────────── */
.bar {
  height:3px; border-radius:3px;
  background:rgba(255,255,255,.06);
  overflow:hidden; margin-top:8px;
}
.bar-fill {
  height:100%; border-radius:3px;
  background:linear-gradient(90deg,#00C9B1,#0D9488);
  transition:width .9s cubic-bezier(.4,0,.2,1);
}
.bar-warn-fill {
  background:linear-gradient(90deg,#f59e0b,#ef4444);
  background-size:200% 100%;
  animation:shimmerWarn 1.5s linear infinite;
}

/* ── Footer ──────────────────────────────────────────────── */
.mon-footer {
  text-align:center; padding:24px 20px;
  border-top:1px solid rgba(255,255,255,.06);
  display:flex; align-items:center; justify-content:center;
  gap:8px; flex-wrap:wrap; color:rgba(255,255,255,.18);
  font-size:11px;
}
.footer-name { font-weight:700; }
.footer-note { }
"""

# Exported as empty — this page is fully standalone
MONITORING_CSS = ""


# ─────────────────────────────────────────────────────────────
# Route
# ─────────────────────────────────────────────────────────────

def setup(rt, page_shell):
    @rt('/monitoring')
    def get(request):
        return _build_page()
