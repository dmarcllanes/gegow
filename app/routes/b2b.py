"""
B2B Portal — specialized entry for Manning Agencies and Corporate clients.
Captures leads and optionally persists them to Supabase.
"""

from fasthtml.common import (
    Div, H2, H3, P, Span, A, Form, Input, Select, Option,
    Label, Button, Textarea, NotStr
)

from app.logic.supabase_db import save_b2b_lead


B2B_CSS = """
/* ── B2B Hero ─────────────────────────────────────────────── */
.b2b-hero {
  background: linear-gradient(to bottom, #0A2A4A 0%, #0E4060 22%, #1A6080 48%, #3D9AB8 75%, #7AC8DC 100%);
  padding: 22px 16px 20px;
  color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 480px) { .b2b-hero { padding: 28px 20px 24px; } }
@media (min-width: 768px) { .b2b-hero { padding: 40px 32px 36px; } }
@media (min-width: 1200px){ .b2b-hero { padding: 52px 48px 44px; } }
.b2b-hero-inner { position: relative; z-index: 7; }
.b2b-hero-eyebrow {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(255,255,255,.12);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,.2);
  color: rgba(255,255,255,.9);
  font-size: 11px; font-weight: 700;
  padding: 5px 12px; border-radius: 20px;
  margin-bottom: 14px; letter-spacing: .5px;
}
.b2b-hero-title {
  font-size: clamp(20px, 5vw, 32px);
  font-weight: 900; color: #fff;
  line-height: 1.15; letter-spacing: -.4px;
  margin-bottom: 8px;
}
.b2b-hero-sub {
  font-size: 14px; color: rgba(255,255,255,.72);
  line-height: 1.6; max-width: 480px; margin-bottom: 22px;
}
.b2b-stats {
  display: flex; gap: 8px; flex-wrap: wrap;
}
@media (min-width: 480px) { .b2b-stats { gap: 10px; } }
@media (min-width: 768px) {
  .b2b-stats { gap: 12px; flex-wrap: nowrap; }
}
.b2b-stat {
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 12px; padding: 10px 16px;
  display: flex; align-items: center; gap: 8px;
}
.b2b-stat-icon { font-size: 18px; }
.b2b-stat-val {
  font-size: 15px; font-weight: 900; color: #fff; line-height: 1;
}
.b2b-stat-lbl {
  font-size: 10px; color: rgba(255,255,255,.55);
  margin-top: 2px; letter-spacing: .4px;
}

/* ── Tab switcher ─────────────────────────────────────────── */
.b2b-tabs-wrap {
  background: #fff;
  border-bottom: 1px solid var(--border);
  padding: 0 20px;
  display: flex; gap: 0;
}
.b2b-tab-pill {
  padding: 14px 18px;
  font-size: 14px; font-weight: 700;
  color: var(--muted);
  text-decoration: none;
  border-bottom: 2.5px solid transparent;
  margin-bottom: -1px;
  display: flex; align-items: center; gap: 6px;
  transition: color .15s, border-color .15s;
  white-space: nowrap;
}
.b2b-tab-pill.active {
  color: var(--teal);
  border-bottom-color: var(--teal);
}
.b2b-tab-pill:hover { color: var(--teal-dk); }

/* ── Layout ───────────────────────────────────────────────── */
.b2b-body { padding: 16px 14px 32px; }
@media (min-width: 480px) { .b2b-body { padding: 20px 16px 32px; } }
@media (min-width: 768px) {
  .b2b-body {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 20px;
    padding: 28px 24px 40px;
    max-width: 900px;
  }
}
@media (min-width: 1024px) {
  .b2b-body {
    grid-template-columns: 300px 1fr;
    gap: 28px;
    padding: 32px 32px 48px;
    max-width: 980px;
  }
}
@media (min-width: 1200px) {
  .b2b-body {
    grid-template-columns: 340px 1fr;
    padding: 36px 48px 56px;
    max-width: 1100px;
  }
}

/* ── Benefits panel ───────────────────────────────────────── */
.b2b-benefits { margin-bottom: 20px; }
@media (min-width: 768px) { .b2b-benefits { margin-bottom: 0; } }

.b2b-benefits-title {
  font-size: 11px; font-weight: 800;
  text-transform: uppercase; letter-spacing: 1.4px;
  color: var(--teal); margin-bottom: 14px;
}
.b2b-benefit {
  display: flex; align-items: flex-start; gap: 14px;
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 14px 16px;
  margin-bottom: 10px;
  transition: border-color .15s, box-shadow .15s;
}
.b2b-benefit:hover {
  border-color: var(--teal-lt);
  box-shadow: 0 4px 16px rgba(0,109,119,.08);
}
.b2b-benefit-icon {
  width: 44px; height: 44px; border-radius: 14px;
  background: var(--teal-xl);
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; flex-shrink: 0;
}
.b2b-benefit-text { flex: 1; min-width: 0; }
.b2b-benefit-title {
  font-size: 14px; font-weight: 800; color: var(--text);
  margin-bottom: 3px; line-height: 1.3;
}
.b2b-benefit-desc { font-size: 12px; color: var(--muted); line-height: 1.5; }

/* ── Inquiry card ─────────────────────────────────────────── */
.b2b-form-card {
  background: #fff;
  border-radius: 24px;
  border: 1.5px solid var(--border);
  box-shadow: 0 2px 12px rgba(15,23,42,.05), 0 8px 32px rgba(15,23,42,.06);
  overflow: hidden;
}
.b2b-form-header {
  padding: 20px 22px 16px;
  border-bottom: 1px solid var(--border);
  background: var(--beige);
}
.b2b-form-header-title {
  font-size: 16px; font-weight: 900; color: var(--text);
  margin-bottom: 3px;
}
.b2b-form-header-sub {
  font-size: 12px; color: var(--muted);
}
.b2b-form-body { padding: 20px 22px 24px; }

/* Form inputs (consistent with wizard) */
.b2b-form-group { margin-bottom: 14px; }
.b2b-label {
  display: block; font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .8px;
  color: var(--muted); margin-bottom: 6px;
}
.b2b-input {
  width: 100%; padding: 13px 14px;
  border: 1.5px solid var(--border); border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none;
  box-shadow: 0 1px 3px rgba(15,23,42,.04);
  transition: border-color .18s, box-shadow .18s;
}
.b2b-input:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}
.b2b-select {
  width: 100%; padding: 13px 36px 13px 14px;
  border: 1.5px solid var(--border); border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none; appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%235F6B72' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
  background-repeat: no-repeat; background-position: right 14px center;
  box-shadow: 0 1px 3px rgba(15,23,42,.04);
  transition: border-color .18s;
  cursor: pointer;
}
.b2b-select:focus { border-color: var(--teal); }
.b2b-textarea {
  width: 100%; padding: 13px 14px;
  border: 1.5px solid var(--border); border-radius: 12px;
  font-size: 15px; background: #fff; color: var(--text);
  outline: none; resize: vertical; min-height: 88px;
  transition: border-color .18s, box-shadow .18s;
}
.b2b-textarea:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}
.b2b-row {
  display: grid; grid-template-columns: 1fr; gap: 0;
}
@media (min-width: 400px) { .b2b-row { grid-template-columns: 1fr 1fr; gap: 12px; } }

.b2b-submit {
  display: block; width: 100%; padding: 15px;
  background: linear-gradient(135deg, var(--teal) 0%, var(--teal-dk) 100%);
  border: none; border-radius: 14px;
  color: #fff; font-size: 16px; font-weight: 700;
  cursor: pointer; margin-top: 6px; text-align: center;
  box-shadow: 0 6px 20px rgba(0,109,119,.25);
  transition: transform .15s, box-shadow .15s;
}
.b2b-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(0,109,119,.35);
}

/* ── Success state ────────────────────────────────────────── */
.b2b-success {
  text-align: center; padding: 40px 24px 36px;
}
.b2b-success-icon { font-size: 60px; margin-bottom: 14px; }
.b2b-success-title {
  font-size: 22px; font-weight: 900; color: var(--text); margin-bottom: 8px;
}
.b2b-success-sub {
  font-size: 14px; color: var(--muted); line-height: 1.6; margin-bottom: 20px;
}
.b2b-success-ref {
  display: inline-block;
  background: var(--teal-xl); border: 1.5px solid var(--teal-lt);
  border-radius: 14px; padding: 12px 24px; margin-bottom: 24px;
  font-size: 13px; font-weight: 800; color: var(--teal);
  letter-spacing: .5px;
}
.b2b-back-link {
  display: inline-flex; align-items: center; gap: 6px;
  color: var(--teal); font-weight: 700; font-size: 14px;
  text-decoration: none;
  padding: 10px 20px; border-radius: 12px;
  border: 1.5px solid var(--teal-lt);
  transition: background .15s;
}
.b2b-back-link:hover { background: var(--teal-xl); }
"""


def _benefit(icon: str, title: str, desc: str) -> Div:
    return Div(
        Div(icon, cls="b2b-benefit-icon"),
        Div(
            Div(title, cls="b2b-benefit-title"),
            Div(desc, cls="b2b-benefit-desc"),
            cls="b2b-benefit-text",
        ),
        cls="b2b-benefit",
    )


def _field(label: str, inp, required_star: bool = False) -> Div:
    lbl_text = label + (" *" if required_star else "")
    return Div(Label(lbl_text, cls="b2b-label"), inp, cls="b2b-form-group")


def setup(rt):

    @rt('/b2b/submit')
    def post(
        lead_type: str = "",
        company_name: str = "",
        contact_person: str = "",
        email: str = "",
        phone: str = "",
        pax_count: str = "",
        destination: str = "",
        travel_date: str = "",
        services: str = "",
        notes: str = "",
    ):
        lead = {
            "lead_type": lead_type, "company_name": company_name,
            "contact_person": contact_person, "email": email,
            "phone": phone, "pax_count": pax_count,
            "destination": destination, "travel_date": travel_date,
            "services": services, "notes": notes,
        }
        save_b2b_lead(lead)
        ref = f"B2B-{email[:3].upper()}-{len(company_name):02d}"

        return Div(
            Div("🎉", cls="b2b-success-icon"),
            Div("Inquiry Received!", cls="b2b-success-title"),
            P(
                f"Thank you, {contact_person or company_name}! "
                "Our B2B team will contact you within 24 hours with a custom quote.",
                cls="b2b-success-sub",
            ),
            Div(f"Reference: {ref}", cls="b2b-success-ref"),
            A("← Back to B2B Portal", href="/b2b", cls="b2b-back-link"),
            cls="b2b-success",
        )


# ── Manning form ─────────────────────────────────────────────

def _manning_benefits() -> Div:
    return Div(
        Div("Why Manning Agencies Choose Gegow", cls="b2b-benefits-title"),
        _benefit("✈️", "Group Flight Blocks",
                 "Reserve seats on domestic & international routes at preferential rates."),
        _benefit("🏨", "Hotel Accommodation Packages",
                 "Pre-booked blocks near ports of embarkation."),
        _benefit("📋", "Document & Visa Assistance",
                 "Streamlined support for seafarer travel documentation."),
        _benefit("🔄", "Flexible Rebooking",
                 "No-hassle date changes for last-minute deployment updates."),
        cls="b2b-benefits",
    )


def _manning_form() -> Div:
    return Div(
        _manning_benefits(),
        Div(
            Div(
                Div("Submit an Inquiry", cls="b2b-form-header-title"),
                Div("We'll respond with a custom group quote within 24 h.", cls="b2b-form-header-sub"),
                cls="b2b-form-header",
            ),
            Div(
                Form(
                    Input(type="hidden", name="lead_type", value="manning"),
                    _field("Manning Agency Name", Input(
                        type="text", name="company_name", cls="b2b-input",
                        placeholder="e.g. Pacific Manning Corp.", required=True,
                    ), required_star=True),
                    Div(
                        _field("Contact Person", Input(
                            type="text", name="contact_person", cls="b2b-input",
                            placeholder="Full name", required=True,
                        ), required_star=True),
                        _field("Email", Input(
                            type="email", name="email", cls="b2b-input",
                            placeholder="ops@manning.com", required=True,
                        ), required_star=True),
                        cls="b2b-row",
                    ),
                    Div(
                        _field("Mobile / Viber", Input(
                            type="tel", name="phone", cls="b2b-input",
                            placeholder="+63 9XX XXX XXXX",
                        )),
                        _field("No. of Seafarers", Input(
                            type="number", name="pax_count", cls="b2b-input",
                            placeholder="e.g. 25", min="1",
                        )),
                        cls="b2b-row",
                    ),
                    Div(
                        _field("Destination / Port", Input(
                            type="text", name="destination", cls="b2b-input",
                            placeholder="e.g. Dubai, Rotterdam, Singapore",
                        )),
                        _field("Preferred Travel Date", Input(
                            type="date", name="travel_date", cls="b2b-input",
                        )),
                        cls="b2b-row",
                    ),
                    _field("Services Required", Select(
                        Option("Flights Only", value="flights"),
                        Option("Flights + Hotel", value="flights_hotel"),
                        Option("Complete Package (Flights + Hotel + Transfers)", value="full"),
                        Option("Hotel Accommodation Only", value="hotel"),
                        name="services", cls="b2b-select",
                    )),
                    _field("Additional Notes", Textarea(
                        placeholder="Special requirements, visa needs, layover preferences...",
                        name="notes", cls="b2b-textarea",
                    )),
                    Button("Submit Inquiry →", type="submit", cls="b2b-submit"),
                    hx_post="/b2b/submit",
                    hx_target="#b2b-response",
                    hx_swap="innerHTML",
                ),
                Div(id="b2b-response"),
                cls="b2b-form-body",
            ),
            cls="b2b-form-card",
        ),
        cls="b2b-body",
    )


# ── Corporate form ───────────────────────────────────────────

def _corporate_benefits() -> Div:
    return Div(
        Div("Why Corporates Partner With Gegow", cls="b2b-benefits-title"),
        _benefit("💼", "Corporate Rate Discounts",
                 "Exclusive markup waivers for volume bookings and retainer accounts."),
        _benefit("📊", "Travel Reporting Dashboard",
                 "Monthly consolidated travel reports for your finance team."),
        _benefit("🎯", "Dedicated Account Manager",
                 "A personal Gegow agent handles all bookings end-to-end."),
        _benefit("🔒", "Policy Compliance",
                 "Bookings enforced against your internal travel policy rules."),
        cls="b2b-benefits",
    )


def _corporate_form() -> Div:
    return Div(
        _corporate_benefits(),
        Div(
            Div(
                Div("Submit a Corporate Inquiry", cls="b2b-form-header-title"),
                Div("Our corporate team will reach out within 24 h.", cls="b2b-form-header-sub"),
                cls="b2b-form-header",
            ),
            Div(
                Form(
                    Input(type="hidden", name="lead_type", value="corporate"),
                    _field("Company Name", Input(
                        type="text", name="company_name", cls="b2b-input",
                        placeholder="e.g. Acme Corporation", required=True,
                    ), required_star=True),
                    Div(
                        _field("Contact Person", Input(
                            type="text", name="contact_person", cls="b2b-input",
                            placeholder="Full name & designation", required=True,
                        ), required_star=True),
                        _field("Work Email", Input(
                            type="email", name="email", cls="b2b-input",
                            placeholder="yourname@company.com", required=True,
                        ), required_star=True),
                        cls="b2b-row",
                    ),
                    Div(
                        _field("Contact Number", Input(
                            type="tel", name="phone", cls="b2b-input",
                            placeholder="+63 2 XXXX XXXX",
                        )),
                        _field("Monthly Travelers", Select(
                            Option("1–10 pax",   value="1-10"),
                            Option("11–30 pax",  value="11-30"),
                            Option("31–100 pax", value="31-100"),
                            Option("100+ pax",   value="100+"),
                            name="pax_count", cls="b2b-select",
                        )),
                        cls="b2b-row",
                    ),
                    _field("Primary Destinations", Input(
                        type="text", name="destination", cls="b2b-input",
                        placeholder="e.g. Singapore, Japan, domestic provinces",
                    )),
                    _field("Services Required", Select(
                        Option("Domestic Flights",           value="domestic_flights"),
                        Option("International Flights",      value="intl_flights"),
                        Option("Hotel Accommodations",       value="hotel"),
                        Option("Full Corporate Travel Mgmt", value="full"),
                        name="services", cls="b2b-select",
                    )),
                    _field("Additional Requirements", Textarea(
                        placeholder="Travel policy needs, preferred airlines, budget range...",
                        name="notes", cls="b2b-textarea",
                    )),
                    Button("Submit Inquiry →", type="submit", cls="b2b-submit"),
                    hx_post="/b2b/submit",
                    hx_target="#b2b-response",
                    hx_swap="innerHTML",
                ),
                Div(id="b2b-response"),
                cls="b2b-form-body",
            ),
            cls="b2b-form-card",
        ),
        cls="b2b-body",
    )
