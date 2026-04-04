"""
B2B Portal — specialized entry for Manning Agencies and Corporate clients.
Captures leads and optionally persists them to Supabase.
"""

from fasthtml.common import (
    Div, H2, H3, P, Span, A, Form, Input, Select, Option,
    Label, Button, Textarea, Hr
)

from app.logic.supabase_db import save_b2b_lead


B2B_CSS = """
.b2b-banner {
    background: linear-gradient(135deg, #1C1917 0%, #292524 100%);
    padding: 24px 16px;
    color: #fff;
}
.b2b-banner-title { font-size: 22px; font-weight: 800; margin-bottom: 6px; }
.b2b-banner-sub { font-size: 13px; opacity: 0.8; line-height: 1.5; }
.b2b-tabs {
    display: flex;
    border-bottom: 2px solid #E8E0D0;
    background: #fff;
}
.b2b-tab {
    flex: 1;
    padding: 14px 8px;
    text-align: center;
    font-size: 14px;
    font-weight: 600;
    color: #78716C;
    text-decoration: none;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
}
.b2b-tab.active { color: #0D9488; border-bottom-color: #0D9488; }
.b2b-form-wrap { padding: 20px 16px; }
.b2b-section-title { font-size: 16px; font-weight: 700; color: #1C1917; margin-bottom: 14px; }
.form-group { margin-bottom: 14px; }
.form-label { display: block; font-size: 13px; font-weight: 600; color: #44403C; margin-bottom: 5px; }
.form-input {
    width: 100%;
    padding: 11px 12px;
    border: 1.5px solid #E8E0D0;
    border-radius: 8px;
    font-size: 15px;
    background: #fff;
    color: #1C1917;
    outline: none;
}
.form-input:focus { border-color: #0D9488; }
.form-select {
    width: 100%;
    padding: 11px 12px;
    border: 1.5px solid #E8E0D0;
    border-radius: 8px;
    font-size: 15px;
    background: #fff;
    color: #1C1917;
    outline: none;
}
.form-textarea {
    width: 100%;
    padding: 11px 12px;
    border: 1.5px solid #E8E0D0;
    border-radius: 8px;
    font-size: 15px;
    background: #fff;
    color: #1C1917;
    outline: none;
    resize: vertical;
    min-height: 90px;
}
.btn-submit {
    width: 100%;
    background: #0D9488;
    color: #fff;
    border: none;
    padding: 14px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    margin-top: 8px;
}
.btn-submit:hover { background: #0F766E; }
.benefit-card {
    background: #F0FDFB;
    border: 1px solid #CCFBF1;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 10px;
}
.benefit-title { font-weight: 700; font-size: 14px; color: #0F766E; margin-bottom: 3px; }
.benefit-desc { font-size: 13px; color: #44403C; }
.success-banner {
    text-align: center;
    padding: 40px 24px;
}
.success-icon { font-size: 56px; margin-bottom: 12px; }
"""


def _benefit(icon: str, title: str, desc: str) -> Div:
    return Div(
        Div(f"{icon} {title}", cls="benefit-title"),
        Div(desc, cls="benefit-desc"),
        cls="benefit-card",
    )


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
            "lead_type": lead_type,
            "company_name": company_name,
            "contact_person": contact_person,
            "email": email,
            "phone": phone,
            "pax_count": pax_count,
            "destination": destination,
            "travel_date": travel_date,
            "services": services,
            "notes": notes,
        }
        save_b2b_lead(lead)

        return Div(
            Div(
                Div("✅", cls="success-icon"),
                H3("Inquiry Received!",
                   style="font-size:20px;font-weight:800;color:#1C1917;margin-bottom:8px"),
                P(
                    f"Thank you, {contact_person or company_name}! "
                    "Our B2B team will contact you within 24 hours with a custom quote.",
                    style="font-size:14px;color:#78716C;margin-bottom:20px;line-height:1.6",
                ),
                Div(
                    Span("Reference: ", style="font-weight:600"),
                    Span(f"B2B-{email[:3].upper()}-{len(company_name):02d}"),
                    style="font-size:14px;color:#44403C;margin-bottom:20px",
                ),
                A("← Back to B2B Portal", href="/b2b",
                  style="color:#0D9488;font-weight:700;text-decoration:none;font-size:14px"),
                cls="success-banner",
            ),
            style="padding:16px",
        )


# ---------------------------------------------------------------------------
# Form helpers
# ---------------------------------------------------------------------------

def _manning_form() -> Div:
    return Div(
        Div(
            Div("Manning Agency Benefits", cls="b2b-section-title"),
            _benefit("✈️", "Group Flight Blocks",
                     "Reserve seats on domestic & international routes at preferential rates."),
            _benefit("🏨", "Hotel Accommodation Packages",
                     "Pre-booked hotel blocks near ports of embarkation."),
            _benefit("📋", "Document & Visa Assistance",
                     "Streamlined support for seafarer travel documentation."),
            cls="b2b-benefits",
        ),
        Div(
            Div("Submit an Inquiry", cls="b2b-section-title"),
            Form(
                Input(type="hidden", name="lead_type", value="manning"),
                Div(
                    Label("Manning Agency Name *", cls="form-label"),
                    Input(type="text", name="company_name", cls="form-input",
                          placeholder="e.g. Pacific Manning Corp.", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Contact Person *", cls="form-label"),
                    Input(type="text", name="contact_person", cls="form-input",
                          placeholder="Full name", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Email *", cls="form-label"),
                    Input(type="email", name="email", cls="form-input",
                          placeholder="operations@manning.com", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Mobile / Viber", cls="form-label"),
                    Input(type="tel", name="phone", cls="form-input",
                          placeholder="+63 9XX XXX XXXX"),
                    cls="form-group",
                ),
                Div(
                    Label("Number of Seafarers", cls="form-label"),
                    Input(type="number", name="pax_count", cls="form-input",
                          placeholder="e.g. 25", min="1"),
                    cls="form-group",
                ),
                Div(
                    Label("Destination / Port", cls="form-label"),
                    Input(type="text", name="destination", cls="form-input",
                          placeholder="e.g. Dubai, Rotterdam, Singapore"),
                    cls="form-group",
                ),
                Div(
                    Label("Preferred Travel Date", cls="form-label"),
                    Input(type="date", name="travel_date", cls="form-input"),
                    cls="form-group",
                ),
                Div(
                    Label("Services Required", cls="form-label"),
                    Select(
                        Option("Flights Only", value="flights"),
                        Option("Flights + Hotel", value="flights_hotel"),
                        Option("Complete Package (Flights + Hotel + Transfers)", value="full"),
                        Option("Hotel Accommodation Only", value="hotel"),
                        name="services", cls="form-select",
                    ),
                    cls="form-group",
                ),
                Div(
                    Label("Additional Notes", cls="form-label"),
                    Textarea(
                        placeholder="Special requirements, visa needs, layover preferences...",
                        name="notes", cls="form-textarea",
                    ),
                    cls="form-group",
                ),
                Button("Submit Inquiry", type="submit", cls="btn-submit"),
                hx_post="/b2b/submit",
                hx_target="#b2b-response",
                hx_swap="innerHTML",
            ),
            Div(id="b2b-response"),
            cls="b2b-form-wrap",
        ),
        cls="b2b-layout",
    )


def _corporate_form() -> Div:
    return Div(
        Div(
            Div("Corporate Travel Benefits", cls="b2b-section-title"),
            _benefit("💼", "Corporate Rate Discounts",
                     "Exclusive markup waivers for volume bookings and retainer accounts."),
            _benefit("📊", "Travel Reporting Dashboard",
                     "Monthly consolidated travel reports for your finance team."),
            _benefit("🎯", "Dedicated Account Manager",
                     "A personal Gegow agent handles all your bookings end-to-end."),
            cls="b2b-benefits",
        ),
        Div(
            Div("Submit a Corporate Inquiry", cls="b2b-section-title"),
            Form(
                Input(type="hidden", name="lead_type", value="corporate"),
                Div(
                    Label("Company Name *", cls="form-label"),
                    Input(type="text", name="company_name", cls="form-input",
                          placeholder="e.g. Acme Corporation", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Contact Person *", cls="form-label"),
                    Input(type="text", name="contact_person", cls="form-input",
                          placeholder="Full name & designation", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Work Email *", cls="form-label"),
                    Input(type="email", name="email", cls="form-input",
                          placeholder="yourname@company.com", required=True),
                    cls="form-group",
                ),
                Div(
                    Label("Contact Number", cls="form-label"),
                    Input(type="tel", name="phone", cls="form-input",
                          placeholder="+63 2 XXXX XXXX"),
                    cls="form-group",
                ),
                Div(
                    Label("Estimated Monthly Travelers", cls="form-label"),
                    Select(
                        Option("1–10 pax", value="1-10"),
                        Option("11–30 pax", value="11-30"),
                        Option("31–100 pax", value="31-100"),
                        Option("100+ pax", value="100+"),
                        name="pax_count", cls="form-select",
                    ),
                    cls="form-group",
                ),
                Div(
                    Label("Primary Destinations", cls="form-label"),
                    Input(type="text", name="destination", cls="form-input",
                          placeholder="e.g. Singapore, Japan, domestic provinces"),
                    cls="form-group",
                ),
                Div(
                    Label("Services Required", cls="form-label"),
                    Select(
                        Option("Domestic Flights", value="domestic_flights"),
                        Option("International Flights", value="intl_flights"),
                        Option("Hotel Accommodations", value="hotel"),
                        Option("Full Corporate Travel Management", value="full"),
                        name="services", cls="form-select",
                    ),
                    cls="form-group",
                ),
                Div(
                    Label("Additional Requirements", cls="form-label"),
                    Textarea(
                        placeholder="Travel policy needs, preferred airlines, budget range...",
                        name="notes", cls="form-textarea",
                    ),
                    cls="form-group",
                ),
                Button("Submit Inquiry", type="submit", cls="btn-submit"),
                hx_post="/b2b/submit",
                hx_target="#b2b-response",
                hx_swap="innerHTML",
            ),
            Div(id="b2b-response"),
            cls="b2b-form-wrap",
        ),
        cls="b2b-layout",
    )
