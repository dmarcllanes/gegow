"""
Explore route — discovery feed showing featured flights, hotels, and tours.
"""

from fasthtml.common import Div, Form, Input, Button, Span, A, P

from app.logic.polars_engine import get_explore_feed, get_flights_page, get_hotels_page, get_tours_page
from app.components.cards import (
    flight_card, hotel_card, tour_card, section_header,
)


def _pagination_bar(section: str, page: int, pages: int, sub: str, total: int) -> Div:
    """Prev / page-info / Next pagination row."""
    prev_disabled = page <= 1
    next_disabled = page >= pages

    prev_btn = Span(
        "← Prev",
        cls="pg-btn" + (" pg-disabled" if prev_disabled else ""),
        **({"hx_get": f"/dashboard/page/{section}?page={page-1}&sub={sub}",
            "hx_target": f"#{section}-content",
            "hx_swap": "innerHTML"} if not prev_disabled else {}),
    )
    next_btn = Span(
        "Next →",
        cls="pg-btn" + (" pg-disabled" if next_disabled else ""),
        **({"hx_get": f"/dashboard/page/{section}?page={page+1}&sub={sub}",
            "hx_target": f"#{section}-content",
            "hx_swap": "innerHTML"} if not next_disabled else {}),
    )
    info = Span(f"Page {page} of {pages}", cls="pg-info")

    return Div(prev_btn, info, next_btn, cls="pagination-bar")


EXPLORE_CSS = """
.hero {
    background: linear-gradient(135deg, #0D9488 0%, #0F766E 60%, #134E4A 100%);
    padding: 24px 16px 28px;
    color: #fff;
}
.hero-title { font-size: 26px; font-weight: 800; margin-bottom: 4px; line-height: 1.2; }
.hero-sub { font-size: 14px; opacity: 0.85; margin-bottom: 18px; }
.search-bar {
    display: flex;
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}
.search-input {
    flex: 1;
    border: none;
    padding: 13px 14px;
    font-size: 15px;
    outline: none;
    color: #1C1917;
    background: transparent;
}
.search-btn {
    background: #F59E0B;
    border: none;
    padding: 13px 18px;
    font-size: 20px;
    cursor: pointer;
}
.quick-links {
    display: flex;
    gap: 10px;
    padding: 14px 16px;
    overflow-x: auto;
    scrollbar-width: none;
}
.quick-links::-webkit-scrollbar { display: none; }
.quick-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    background: #fff;
    border-radius: 12px;
    padding: 12px 14px;
    min-width: 72px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.07);
    text-decoration: none;
    color: #1C1917;
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
    border: 1px solid #F0EBE3;
}
.quick-link .ql-icon { font-size: 22px; }
.section-scroll {
    display: flex;
    gap: 10px;
    padding: 0 16px;
    overflow-x: auto;
    scrollbar-width: none;
}
.section-scroll::-webkit-scrollbar { display: none; }
.section-scroll .card { min-width: 240px; margin: 0; }
"""


def setup(rt):
    @rt('/search')
    def get(q: str = ""):
        if not q or len(q) < 2:
            return Div()
        from app.logic.polars_engine import load_flights, load_tours
        import polars as pl

        flights = load_flights().filter(
            pl.col("destination_city").str.to_lowercase().str.contains(q.lower()) |
            pl.col("origin_city").str.to_lowercase().str.contains(q.lower())
        ).head(3).to_dicts()

        tours = load_tours().filter(
            pl.col("destination").str.to_lowercase().str.contains(q.lower()) |
            pl.col("name").str.to_lowercase().str.contains(q.lower())
        ).head(3).to_dicts()

        if not flights and not tours:
            return Div(
                P(f'No results for "{q}". Try "Cebu", "Boracay", or "Tokyo".',
                  style="padding:16px;color:#78716C;font-size:14px"),
            )

        from app.logic.polars_engine import MARKUP
        import polars as pl

        items = []
        for f in flights:
            markup = MARKUP["domestic_flight"] if f["type"] == "domestic" else MARKUP["international_flight"]
            f["selling_price"] = f["base_price"] + markup
            items.append(flight_card(f))
        for t in tours:
            markup = MARKUP["domestic_tour"] if t["type"] == "domestic" else MARKUP["international_tour"]
            t["selling_price"] = t["base_price"] + markup
            items.append(tour_card(t))

        return Div(
            Div(f'Results for "{q}"',
                style="padding:12px 16px 4px;font-weight:700;font-size:15px;color:#1C1917"),
            *items,
            style="padding:0 16px 16px",
        )

    @rt('/dashboard/page/{section}')
    def get(section: str, page: int = 1, sub: str = "all"):
        loaders = {
            "flights": (get_flights_page, flight_card),
            "hotels":  (get_hotels_page,  hotel_card),
            "tours":   (get_tours_page,   tour_card),
        }
        if section not in loaders:
            return Div()
        loader, card_fn = loaders[section]
        result = loader(page=page, sub=sub)
        cards = [card_fn(item) for item in result["items"]]
        return Div(
            Div(*cards, cls="card-row stagger") if cards else Div(
                P("No results found.", style="padding:24px;color:var(--muted);text-align:center"),
            ),
            _pagination_bar(section, result["page"], result["pages"], sub, result["total"]),
        )
