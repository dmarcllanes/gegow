"""
Gegow Path — redesigned 5-step booking wizard.
"""

from fasthtml.common import (
    Div, H2, H3, P, Span, Button, Form, Input, Select, Option,
    Label, A, Hr, Script, NotStr
)

_UNS = "https://images.unsplash.com/photo-"
_FLIGHT_IMG = _UNS + "1436491865332-7a61a109cc05?w=600&q=80&auto=format&fit=crop"
_HOTEL_IMG  = _UNS + "1631049307264-da0ec9d70304?w=600&q=80&auto=format&fit=crop"
_TOUR_IMG   = _UNS + "1501854140801-50d01698950b?w=600&q=80&auto=format&fit=crop"

STEP_LABELS = ["Type", "Where", "Dates", "Who", "Review"]

WIZARD_CSS = """
/* ── Wizard page shell ───────────────────────────────── */
.wizard-page {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 28px 16px 80px;
  background: var(--beige);
}

/* ── Wizard card ─────────────────────────────────────── */
.wizard-card {
  background: #fff;
  border-radius: 24px;
  box-shadow:
    0 2px 4px rgba(15,23,42,.04),
    0 8px 32px rgba(15,23,42,.08),
    0 24px 64px rgba(15,23,42,.06);
  width: 100%;
  max-width: 540px;
  overflow: hidden;
}

/* ── Progress header ─────────────────────────────────── */
.wizard-progress {
  padding: 22px 24px 18px;
  border-bottom: 1px solid var(--border);
  background: var(--beige);
}
.wizard-progress-label {
  font-size: 10px; font-weight: 800;
  text-transform: uppercase; letter-spacing: 1.6px;
  color: var(--muted-lt); margin-bottom: 14px;
}
.wizard-steps {
  display: flex; align-items: center; margin-bottom: 10px;
}
.step-dot {
  width: 30px; height: 30px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 800; flex-shrink: 0;
  background: var(--border); color: var(--muted-lt);
  transition: all .2s;
}
.step-dot.done {
  background: var(--teal); color: #fff;
  box-shadow: none;
}
.step-dot.active {
  background: var(--teal); color: #fff;
  box-shadow: 0 0 0 4px rgba(0,109,119,.15);
  transform: scale(1.1);
}
.step-line {
  flex: 1; height: 2px;
  background: var(--border); margin: 0 5px;
  border-radius: 2px; transition: background .3s;
}
.step-line.done { background: var(--teal); }
.step-labels-row {
  display: flex;
  padding: 0 2px;
}
.step-lbl {
  flex: 1; text-align: center;
  font-size: 10px; font-weight: 600;
  color: var(--muted-lt);
  white-space: nowrap;
}
.step-lbl.done  { color: var(--teal-dk); }
.step-lbl.active { color: var(--teal); font-weight: 800; }

/* ── Step body ───────────────────────────────────────── */
.wizard-body { padding: 28px 24px 24px; }
.wizard-eyebrow {
  font-size: 11px; font-weight: 800;
  text-transform: uppercase; letter-spacing: 1.4px;
  color: var(--teal); margin-bottom: 5px;
}
.wizard-title {
  font-size: 22px; font-weight: 900; color: var(--text);
  line-height: 1.2; margin-bottom: 4px; letter-spacing: -.3px;
}
.wizard-sub {
  font-size: 13px; color: var(--muted); margin-bottom: 24px;
  line-height: 1.5;
}

/* ── Trip type cards ─────────────────────────────────── */
.type-grid {
  display: grid; grid-template-columns: 1fr 1fr 1fr;
  gap: 10px; margin-bottom: 0;
}
.type-card {
  position: relative; overflow: hidden;
  border-radius: 16px; cursor: pointer;
  border: 2.5px solid transparent;
  aspect-ratio: 2/3;
  display: flex; flex-direction: column; justify-content: flex-end;
  transition: border-color .2s, transform .2s, box-shadow .2s;
  text-decoration: none;
}
.type-card:hover {
  border-color: var(--teal);
  transform: translateY(-4px);
  box-shadow: 0 16px 40px rgba(0,109,119,.18);
}
.type-card-bg {
  position: absolute; inset: 0;
  background-size: cover; background-position: center;
}
.type-card-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top,
    rgba(0,0,0,.8) 0%, rgba(0,0,0,.25) 50%, transparent 100%);
}
.type-card-body {
  position: relative; z-index: 1;
  padding: 10px 12px 14px;
}
.type-icon { font-size: 22px; display: block; margin-bottom: 4px; }
.type-label {
  font-size: 14px; font-weight: 800; color: #fff;
  display: block; line-height: 1.1;
}
.type-desc {
  font-size: 10px; color: rgba(255,255,255,.65);
  margin-top: 3px; line-height: 1.3;
}

/* ── Form elements ───────────────────────────────────── */
.form-group { margin-bottom: 16px; }
.form-row {
  display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
}
@media (max-width: 400px) { .form-row { grid-template-columns: 1fr; } }
.form-label {
  display: block; font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .8px;
  color: var(--muted); margin-bottom: 6px;
}
.form-input {
  width: 100%; padding: 13px 14px;
  border: 1.5px solid var(--border);
  border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none;
  box-shadow: 0 1px 3px rgba(15,23,42,.04);
  transition: border-color .18s, box-shadow .18s;
}
.form-input:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}
.form-select {
  width: 100%; padding: 13px 36px 13px 14px;
  border: 1.5px solid var(--border);
  border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none; appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%235F6B72' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  box-shadow: 0 1px 3px rgba(15,23,42,.04);
  transition: border-color .18s, box-shadow .18s;
  cursor: pointer;
}
.form-select:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}

/* ── Pax stepper ─────────────────────────────────────── */
.pax-card {
  display: flex; align-items: center; justify-content: space-between;
  background: var(--beige); border-radius: 14px;
  padding: 16px 18px; margin-bottom: 12px;
  border: 1.5px solid var(--border);
}
.pax-info {}
.pax-label { font-size: 14px; font-weight: 700; color: var(--text); }
.pax-sub   { font-size: 12px; color: var(--muted); margin-top: 1px; }
.pax-stepper { display: flex; align-items: center; gap: 14px; }
.pax-btn {
  width: 36px; height: 36px; border-radius: 50%;
  border: 2px solid var(--teal); background: #fff; color: var(--teal);
  font-size: 20px; font-weight: 700; line-height: 1;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background .15s, color .15s;
}
.pax-btn:hover { background: var(--teal); color: #fff; }
.pax-count {
  font-size: 22px; font-weight: 900; color: var(--text);
  min-width: 28px; text-align: center;
}

/* ── Review cards ────────────────────────────────────── */
.review-card {
  border: 1.5px solid var(--border);
  border-radius: 16px; overflow: hidden;
  margin-bottom: 12px;
  transition: border-color .15s, box-shadow .15s;
}
.review-card:hover {
  border-color: var(--teal-lt);
  box-shadow: 0 4px 16px rgba(0,109,119,.1);
}
.review-card-header {
  background: linear-gradient(135deg, var(--teal) 0%, var(--teal-dk) 100%);
  padding: 16px 18px;
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 12px;
}
.review-card-title { font-size: 14px; font-weight: 700; color: #fff; line-height: 1.3; }
.review-card-price { font-size: 20px; font-weight: 900; color: #fff; white-space: nowrap; }
.review-card-body { padding: 14px 18px; }
.review-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 7px 0; border-bottom: 1px solid #F5F0E8; font-size: 13px;
}
.review-row:last-child { border-bottom: none; }
.review-label { color: var(--muted); }
.review-value { font-weight: 600; color: var(--text); }

/* ── Action buttons ──────────────────────────────────── */
.btn-next {
  display: block; width: 100%; padding: 15px;
  background: linear-gradient(135deg, var(--teal) 0%, var(--teal-dk) 100%);
  border: none; border-radius: 14px;
  color: #fff; font-size: 16px; font-weight: 700;
  cursor: pointer; margin-top: 20px; text-align: center;
  text-decoration: none;
  box-shadow: 0 6px 20px rgba(0,109,119,.25);
  transition: transform .15s, box-shadow .15s;
}
.btn-next:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(0,109,119,.35);
}
.btn-next:active { transform: scale(.98); }
.btn-confirm {
  display: block; width: 100%; padding: 15px;
  background: linear-gradient(135deg, #FF7043 0%, #F4511E 100%);
  border: none; border-radius: 14px;
  color: #fff; font-size: 16px; font-weight: 700;
  cursor: pointer; margin-top: 14px; text-align: center;
  text-decoration: none;
  box-shadow: 0 6px 20px rgba(244,81,30,.3);
  transition: transform .15s, box-shadow .15s;
}
.btn-confirm:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(244,81,30,.4);
}
.btn-back {
  display: block; width: 100%; padding: 12px;
  background: transparent; border: none;
  color: var(--muted); font-size: 14px; font-weight: 600;
  cursor: pointer; margin-top: 6px; text-align: center;
  border-radius: 12px;
  transition: color .15s, background .15s;
}
.btn-back:hover { color: var(--text); background: rgba(0,0,0,.04); }

/* ── Confirmation ────────────────────────────────────── */
.confirm-wrap { padding: 40px 24px 32px; text-align: center; }
.confirm-icon-wrap {
  width: 80px; height: 80px; border-radius: 50%;
  background: linear-gradient(135deg, var(--teal), var(--teal-dk));
  display: flex; align-items: center; justify-content: center;
  font-size: 40px; margin: 0 auto 20px;
  box-shadow: 0 8px 28px rgba(0,109,119,.3);
}
.confirm-title { font-size: 26px; font-weight: 900; color: var(--text); margin-bottom: 6px; }
.confirm-sub   { font-size: 14px; color: var(--muted); margin-bottom: 28px; line-height: 1.6; }
.confirm-ref-box {
  display: inline-block;
  background: var(--teal-xl); border: 1.5px solid var(--teal-lt);
  border-radius: 14px; padding: 16px 28px; margin-bottom: 28px;
}
.confirm-ref-label {
  font-size: 10px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 1.4px; color: var(--teal); margin-bottom: 4px;
}
.confirm-ref-num { font-size: 24px; font-weight: 900; color: var(--text); }
.confirm-total  {
  font-size: 18px; font-weight: 800; color: var(--teal); margin-bottom: 24px;
}
.confirm-actions { display: flex; flex-direction: column; gap: 10px; }
.btn-suitcase {
  display: block; padding: 14px;
  background: var(--teal-xl); border: 1.5px solid var(--teal-lt);
  border-radius: 14px; color: var(--teal);
  font-size: 15px; font-weight: 700; text-decoration: none;
  transition: background .15s;
}
.btn-suitcase:hover { background: var(--teal-lt); }
.btn-again {
  display: block; padding: 12px;
  background: transparent; border: 1.5px solid var(--border);
  border-radius: 14px; color: var(--muted);
  font-size: 14px; font-weight: 600; text-decoration: none;
  transition: border-color .15s, color .15s;
}
.btn-again:hover { border-color: var(--text); color: var(--text); }

/* ── Step 1 — animated type selection cards ──────────── */
.type-grid-new {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.type-card-new {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 18px;
  border-radius: 20px;
  border: 2px solid var(--border);
  background: var(--beige);
  cursor: pointer;
  text-decoration: none;
  transition: border-color .2s, transform .18s, box-shadow .2s, background .2s;
}
.type-card-new:hover {
  border-color: var(--teal);
  background: #fff;
  transform: translateY(-3px);
  box-shadow: 0 14px 36px rgba(0,109,119,.16);
}
.type-icon-bubble {
  width: 72px; height: 72px;
  border-radius: 20px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.flight-bubble { background: linear-gradient(135deg, #0a9aa8 0%, #006d77 100%); }
.hotel-bubble  { background: linear-gradient(135deg, #2d9e8f 0%, #005f6b 100%); }
.tour-bubble   { background: linear-gradient(135deg, #1e8a9a 0%, #004a56 100%); }
.type-svg { width: 44px; height: 44px; }
.type-text  { flex: 1; min-width: 0; }
.type-label-new {
  display: block;
  font-size: 17px; font-weight: 800; color: var(--text);
  letter-spacing: -.2px; margin-bottom: 3px;
}
.type-desc-new {
  display: block;
  font-size: 12px; color: var(--muted); line-height: 1.4;
}
.type-arrow {
  font-size: 24px; color: #C8C4BE; flex-shrink: 0;
  transition: color .2s, transform .2s;
}
.type-card-new:hover .type-arrow { color: var(--teal); transform: translateX(4px); }

/* ── SVG keyframe animations ─────────────────────────── */
@keyframes plane-drift {
  0%,100% { transform: translate(0,0) rotate(-8deg); }
  33%     { transform: translate(3px,-3px) rotate(-5deg); }
  66%     { transform: translate(-2px, 2px) rotate(-10deg); }
}
@keyframes compass-rotate {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes win-on1 {
  0%,100%,45%  { fill: rgba(0,109,119,.35); }
  20%          { fill: rgba(255,215,80,.9); }
}
@keyframes win-on2 {
  0%,100%,65%  { fill: rgba(0,109,119,.35); }
  45%          { fill: rgba(255,215,80,.9); }
}
@keyframes win-on3 {
  0%,100%      { fill: rgba(0,109,119,.35); }
  65%          { fill: rgba(255,215,80,.9); }
}
@keyframes trail-fade {
  0%,100% { opacity: .18; }
  50%     { opacity: .42; }
}

/* Idle — always running, calm pace */
.plane-g  { animation: plane-drift 3.6s ease-in-out infinite; }
.trail-g  { animation: trail-fade  3.6s ease-in-out infinite; }
.needle-g { animation: compass-rotate 9s linear infinite; transform-origin: 24px 24px; }
.hw1 { animation: win-on1 3.5s ease-in-out infinite; }
.hw2 { animation: win-on2 3.5s ease-in-out infinite 0.6s; }
.hw3 { animation: win-on3 3.5s ease-in-out infinite 1.2s; }
.hw4 { animation: win-on1 3.5s ease-in-out infinite 1.8s; }
.hw5 { animation: win-on2 3.5s ease-in-out infinite 2.4s; }

/* Hover — speed everything up */
.type-card-new:hover .plane-g  { animation-duration: .9s; }
.type-card-new:hover .trail-g  { animation-duration: .9s; }
.type-card-new:hover .needle-g { animation-duration: 1.4s; }
.type-card-new:hover .hw1,
.type-card-new:hover .hw2,
.type-card-new:hover .hw3,
.type-card-new:hover .hw4,
.type-card-new:hover .hw5 { animation-duration: .9s; }
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _step_indicator(current: int) -> Div:
    dots, labels = [], []
    for i in range(1, 6):
        if i < current:
            dot_cls, lbl_cls, label = "step-dot done", "step-lbl done", "✓"
        elif i == current:
            dot_cls, lbl_cls, label = "step-dot active", "step-lbl active", str(i)
        else:
            dot_cls, lbl_cls, label = "step-dot", "step-lbl", str(i)
        dots.append(Span(label, cls=dot_cls))
        if i < 5:
            dots.append(Div(cls="step-line" + (" done" if i < current else "")))
        labels.append(Span(STEP_LABELS[i - 1], cls=lbl_cls))

    return Div(
        Div("Gegow Path — Book Your Trip", cls="wizard-progress-label"),
        Div(*dots, cls="wizard-steps"),
        Div(*labels, cls="step-labels-row"),
        cls="wizard-progress",
    )


def _hidden(name: str, value: str) -> Input:
    return Input(type="hidden", name=name, value=value)


def _wrap(current: int, *children) -> Div:
    return Div(
        Div(
            _step_indicator(current),
            Div(*children, cls="wizard-body"),
            cls="wizard-card",
        ),
        cls="wizard-page",
        id="wizard-content",
    )


# ---------------------------------------------------------------------------
# Step 1 — Choose trip type
# ---------------------------------------------------------------------------

def wizard_step1() -> Div:
    # ── Animated SVG: Paper plane with dotted trail ──────
    _flight_svg = NotStr("""
<svg class="type-svg" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g class="trail-g">
    <circle cx="8"  cy="30" r="1.8" fill="white" opacity=".5"/>
    <circle cx="13" cy="34" r="1.4" fill="white" opacity=".38"/>
    <circle cx="5"  cy="37" r="1.1" fill="white" opacity=".25"/>
  </g>
  <g class="plane-g">
    <path d="M10 26 L40 10 L32 42 L23 29 Z" fill="white" opacity=".95"/>
    <path d="M23 29 L21 41 L27 35 Z" fill="white" opacity=".62"/>
    <path d="M23 29 L40 10 L32 42 Z" fill="white" opacity=".15"/>
  </g>
</svg>""")

    # ── Animated SVG: Hotel building with blinking windows ─
    _hotel_svg = NotStr("""
<svg class="type-svg hotel-svg" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="8"  y="18" width="32" height="27" rx="2.5" fill="white" opacity=".92"/>
  <rect x="9"  y="10" width="20" height="10" rx="2"   fill="white" opacity=".68"/>
  <rect x="19" y="34" width="10" height="11" rx="1.5" fill="rgba(0,109,119,.42)"/>
  <rect class="hw1" x="12" y="22" width="6" height="5" rx="1" fill="rgba(0,109,119,.35)"/>
  <rect class="hw2" x="21" y="22" width="6" height="5" rx="1" fill="rgba(0,109,119,.35)"/>
  <rect class="hw3" x="30" y="22" width="6" height="5" rx="1" fill="rgba(0,109,119,.35)"/>
  <rect class="hw4" x="12" y="30" width="6" height="5" rx="1" fill="rgba(0,109,119,.35)"/>
  <rect class="hw5" x="30" y="30" width="6" height="5" rx="1" fill="rgba(0,109,119,.35)"/>
</svg>""")

    # ── Animated SVG: Compass with spinning needle ────────
    _tour_svg = NotStr("""
<svg class="type-svg" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="24" cy="24" r="18" stroke="white" stroke-width="2.5" opacity=".65"/>
  <line x1="24" y1="6"  x2="24" y2="9"  stroke="white" stroke-width="2" stroke-linecap="round" opacity=".7"/>
  <line x1="24" y1="39" x2="24" y2="42" stroke="white" stroke-width="2" stroke-linecap="round" opacity=".4"/>
  <line x1="6"  y1="24" x2="9"  y2="24" stroke="white" stroke-width="2" stroke-linecap="round" opacity=".4"/>
  <line x1="39" y1="24" x2="42" y2="24" stroke="white" stroke-width="2" stroke-linecap="round" opacity=".4"/>
  <g class="needle-g">
    <polygon points="24,10 21,24 24,22 27,24" fill="white"/>
    <polygon points="24,38 21,24 24,26 27,24" fill="white" opacity=".45"/>
  </g>
  <circle cx="24" cy="24" r="3.2" fill="white"/>
</svg>""")

    def _card(svg, bubble_cls, label, desc, trip_type):
        return A(
            Div(svg, cls=f"type-icon-bubble {bubble_cls}"),
            Div(
                Span(label, cls="type-label-new"),
                Span(desc,  cls="type-desc-new"),
                cls="type-text",
            ),
            Div("›", cls="type-arrow"),
            href=f"/book/step2?trip_type={trip_type}",
            hx_get=f"/book/step2?trip_type={trip_type}",
            hx_target="#wizard-content",
            hx_swap="outerHTML",
            cls="type-card-new",
        )

    return _wrap(
        1,
        Div("Step 1 of 5", cls="wizard-eyebrow"),
        Div("What are you booking?", cls="wizard-title"),
        Div("Tap a category to get started.", cls="wizard-sub"),
        Div(
            _card(_flight_svg, "flight-bubble", "Flight",
                  "Domestic & international", "flight"),
            _card(_hotel_svg,  "hotel-bubble",  "Hotel",
                  "Best stays, best prices",  "hotel"),
            _card(_tour_svg,   "tour-bubble",   "Tour",
                  "Guided local & abroad",    "tour"),
            cls="type-grid-new",
        ),
    )


# ---------------------------------------------------------------------------
# Step 2 — Destination
# ---------------------------------------------------------------------------

def wizard_step2_flight(origins: list[str]) -> Div:
    return _wrap(
        2,
        Div("Step 2 of 5", cls="wizard-eyebrow"),
        Div("Where are you flying?", cls="wizard-title"),
        Div("Pick your origin and destination.", cls="wizard-sub"),
        _hidden("trip_type", "flight"),
        Div(
            Div(
                Label("From", cls="form-label"),
                Select(*[Option(o, value=o) for o in origins],
                       name="origin", cls="form-select"),
                cls="form-group",
            ),
            Div(
                Label("To (IATA Code)", cls="form-label"),
                Input(type="text", name="destination",
                      placeholder="e.g. CEB, SIN, NRT",
                      cls="form-input", maxlength="3"),
                cls="form-group",
            ),
            cls="form-row",
        ),
        Button("Continue →", cls="btn-next",
               hx_get="/book/step3",
               hx_include="[name='trip_type'],[name='origin'],[name='destination']",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
        Button("← Back", cls="btn-back",
               hx_get="/book/step1",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


def wizard_step2_hotel(cities: list[str]) -> Div:
    return _wrap(
        2,
        Div("Step 2 of 5", cls="wizard-eyebrow"),
        Div("Where would you like to stay?", cls="wizard-title"),
        Div("Pick your destination city.", cls="wizard-sub"),
        _hidden("trip_type", "hotel"),
        Div(
            Label("City", cls="form-label"),
            Select(*[Option(c, value=c) for c in cities],
                   name="city", cls="form-select"),
            cls="form-group",
        ),
        Button("Continue →", cls="btn-next",
               hx_get="/book/step3",
               hx_include="[name='trip_type'],[name='city']",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
        Button("← Back", cls="btn-back",
               hx_get="/book/step1",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


def wizard_step2_tour() -> Div:
    return _wrap(
        2,
        Div("Step 2 of 5", cls="wizard-eyebrow"),
        Div("What tour are you after?", cls="wizard-title"),
        Div("Enter a destination or keyword.", cls="wizard-sub"),
        _hidden("trip_type", "tour"),
        Div(
            Div(
                Label("Destination / Keyword", cls="form-label"),
                Input(type="text", name="tour_dest",
                      placeholder="e.g. Palawan, Boracay, Tokyo",
                      cls="form-input"),
                cls="form-group",
            ),
            Div(
                Label("Tour Type", cls="form-label"),
                Select(
                    Option("All Types", value=""),
                    Option("🇵🇭 Local / Domestic", value="domestic"),
                    Option("🌍 International", value="international"),
                    name="tour_type", cls="form-select",
                ),
                cls="form-group",
            ),
            cls="form-row",
        ),
        Button("Continue →", cls="btn-next",
               hx_get="/book/step3",
               hx_include="[name='trip_type'],[name='tour_dest'],[name='tour_type']",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
        Button("← Back", cls="btn-back",
               hx_get="/book/step1",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


# ---------------------------------------------------------------------------
# Step 3 — Dates
# ---------------------------------------------------------------------------

def wizard_step3(params: dict) -> Div:
    trip_type = params.get("trip_type", "flight")
    is_hotel  = trip_type == "hotel"
    label1    = "Check-in Date"  if is_hotel else "Departure Date"
    label2    = "Check-out Date" if is_hotel else "Return Date (optional)"
    hidden    = [_hidden(k, v) for k, v in params.items()]

    return _wrap(
        3,
        Div("Step 3 of 5", cls="wizard-eyebrow"),
        Div("When are you going?", cls="wizard-title"),
        Div("Select your travel dates.", cls="wizard-sub"),
        *hidden,
        Div(
            Div(
                Label(label1, cls="form-label"),
                Input(type="date", name="date_from", cls="form-input", required=True),
                cls="form-group",
            ),
            Div(
                Label(label2, cls="form-label"),
                Input(type="date", name="date_to", cls="form-input"),
                cls="form-group",
            ),
            cls="form-row",
        ),
        Button("Continue →", cls="btn-next",
               hx_get="/book/step4",
               hx_include="[name]",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
        Button("← Back", cls="btn-back",
               hx_get="/book/step2",
               hx_include="[name='trip_type']",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


# ---------------------------------------------------------------------------
# Step 4 — Travelers
# ---------------------------------------------------------------------------

def wizard_step4(params: dict) -> Div:
    hidden = [_hidden(k, v) for k, v in params.items()]

    return _wrap(
        4,
        Div("Step 4 of 5", cls="wizard-eyebrow"),
        Div("Who's travelling?", cls="wizard-title"),
        Div("Select the number of travellers.", cls="wizard-sub"),
        *hidden,
        Div(
            Div(
                Div(
                    Div("Adults", cls="pax-label"),
                    Div("Age 12 and above", cls="pax-sub"),
                    cls="pax-info",
                ),
                Div(
                    Button("−", type="button", cls="pax-btn",
                           onclick="adjustPax('adults',-1)"),
                    Span("1", cls="pax-count", id="adults-count"),
                    Button("+", type="button", cls="pax-btn",
                           onclick="adjustPax('adults',1)"),
                    cls="pax-stepper",
                ),
                cls="pax-card",
            ),
            Div(
                Div(
                    Div("Children", cls="pax-label"),
                    Div("Ages 2 – 11", cls="pax-sub"),
                    cls="pax-info",
                ),
                Div(
                    Button("−", type="button", cls="pax-btn",
                           onclick="adjustPax('children',-1)"),
                    Span("0", cls="pax-count", id="children-count"),
                    Button("+", type="button", cls="pax-btn",
                           onclick="adjustPax('children',1)"),
                    cls="pax-stepper",
                ),
                cls="pax-card",
            ),
        ),
        Input(type="hidden", name="adults",   value="1", id="adults-input"),
        Input(type="hidden", name="children", value="0", id="children-input"),
        Button("Review Options →", cls="btn-next",
               hx_get="/book/step5",
               hx_include="[name]",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
        Button("← Back", cls="btn-back",
               hx_get="/book/step3",
               hx_include="[name='trip_type'],[name='origin'],[name='destination'],"
                           "[name='city'],[name='tour_dest'],[name='tour_type']",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


# ---------------------------------------------------------------------------
# Step 5 — Review & Confirm
# ---------------------------------------------------------------------------

def wizard_step5(params: dict, results: list[dict]) -> Div:
    trip_type = params.get("trip_type", "flight")
    adults    = int(params.get("adults", 1))
    children  = int(params.get("children", 0))
    date_from = params.get("date_from", "")
    date_to   = params.get("date_to", "")
    pax       = adults + children

    result_cards = []
    for item in results[:5]:
        price = item.get("selling_price", 0)

        if trip_type == "flight":
            title       = f"{item['origin_city']} → {item['destination_city']}"
            sub_line    = f"{item['airline']}  ·  {item['departure']} – {item['arrival']}"
            price_label = f"₱{int(price):,} / way × {pax} pax"
            total       = price * pax
        elif trip_type == "hotel":
            title = item["name"]
            sub_line = f"📍 {item.get('location', item.get('city', ''))}"
            nights = 1
            if date_from and date_to:
                from datetime import date as _date
                try:
                    nights = max(1, (_date.fromisoformat(date_to) - _date.fromisoformat(date_from)).days)
                except ValueError:
                    pass
            price_label = f"₱{int(price):,} / night × {nights} night(s)"
            total = price * nights
        else:
            title       = item["name"]
            sub_line    = f"📍 {item.get('destination', '')}"
            price_label = f"₱{int(price):,} / person × {pax} person(s)"
            total       = price * pax

        result_cards.append(
            Div(
                Div(
                    Div(
                        Div(title, cls="review-card-title"),
                        Div(sub_line,
                            style="font-size:11px;color:rgba(255,255,255,.7);margin-top:3px"),
                        cls="",
                    ),
                    Div(f"₱{int(total):,}", cls="review-card-price"),
                    cls="review-card-header",
                ),
                Div(
                    Div(
                        Div("Price breakdown", cls="review-label"),
                        Div(price_label, cls="review-value"),
                        cls="review-row",
                    ),
                    Div(
                        Div("Travel dates", cls="review-label"),
                        Div(date_from + (f" → {date_to}" if date_to else ""), cls="review-value"),
                        cls="review-row",
                    ),
                    Button(
                        "Confirm this Booking →",
                        cls="btn-confirm",
                        hx_post="/book/confirm",
                        hx_vals=str({
                            "trip_type": trip_type,
                            "item_id":   item.get("id", ""),
                            "adults":    adults,
                            "children":  children,
                            "date_from": date_from,
                            "date_to":   date_to,
                            "total":     int(total),
                        }).replace("'", '"'),
                        hx_target="#wizard-content",
                        hx_swap="outerHTML",
                    ),
                    cls="review-card-body",
                ),
                cls="review-card",
            )
        )

    if not result_cards:
        result_cards = [
            Div(
                Div("😕", style="font-size:40px;margin-bottom:10px"),
                Div("No results found", style="font-weight:700;font-size:16px;color:var(--text);margin-bottom:4px"),
                Div("Try adjusting your search criteria.", style="font-size:13px;color:var(--muted)"),
                style="text-align:center;padding:32px 20px",
            )
        ]

    return _wrap(
        5,
        Div("Step 5 of 5", cls="wizard-eyebrow"),
        Div("Pick your option", cls="wizard-title"),
        Div(f"{len(results)} result(s) found — select one to confirm.", cls="wizard-sub"),
        *result_cards,
        Button("← Start Over", cls="btn-back",
               hx_get="/book/step1",
               hx_target="#wizard-content",
               hx_swap="outerHTML"),
    )


# ---------------------------------------------------------------------------
# Confirmation
# ---------------------------------------------------------------------------

def wizard_confirmed(booking: dict) -> Div:
    return Div(
        Div(
            Div(
                Div("🎉", cls="confirm-icon-wrap"),
                Div("Booking Confirmed!", cls="confirm-title"),
                Div(
                    "Your trip has been saved to your Suitcase. "
                    "Check your itinerary anytime — even offline.",
                    cls="confirm-sub",
                ),
                Div(
                    Div("Booking Reference", cls="confirm-ref-label"),
                    Div(f"GGW-{booking.get('ref','00000')}", cls="confirm-ref-num"),
                    cls="confirm-ref-box",
                ),
                Div(
                    f"Total Charged: ₱{int(booking.get('total',0)):,}",
                    cls="confirm-total",
                ),
                Div(
                    A("🧳 View My Suitcase", href="/suitcase", cls="btn-suitcase"),
                    A("Book Another Trip", href="/book", cls="btn-again"),
                    cls="confirm-actions",
                ),
                cls="confirm-wrap",
            ),
            cls="wizard-card",
        ),
        cls="wizard-page",
        id="wizard-content",
    )
