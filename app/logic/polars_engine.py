"""
Polars-based data engine for Gegow.
Handles loading, filtering, and markup application for flights, hotels, and tours.

Markup rules (per CLAUDE.md):
  Domestic flights:     +₱250–400  per way   → midpoint ₱325
  International flights:+₱1,000–3,000 per way → midpoint ₱2,000
  Hotels:               +₱300–1,000 per night → midpoint ₱650
  Domestic tours:       +₱400–900  per person → midpoint ₱650
  International tours:  +₱500–2,000 per person → midpoint ₱1,250
"""

import polars as pl
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"

# ---------------------------------------------------------------------------
# Markup constants (midpoints of the ranges in CLAUDE.md)
# ---------------------------------------------------------------------------
MARKUP = {
    "domestic_flight": 325,
    "international_flight": 2000,
    "hotel": 650,
    "domestic_tour": 650,
    "international_tour": 1250,
}


# ---------------------------------------------------------------------------
# Flights
# ---------------------------------------------------------------------------

def load_flights() -> pl.DataFrame:
    return pl.read_csv(DATA_DIR / "flights_cache.csv")


def _add_flight_markup(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("type") == "domestic")
        .then(pl.col("base_price") + MARKUP["domestic_flight"])
        .otherwise(pl.col("base_price") + MARKUP["international_flight"])
        .alias("selling_price")
    )


def search_flights(origin: str, destination: str) -> list[dict]:
    df = load_flights()
    results = df.filter(
        (pl.col("origin") == origin.upper()) &
        (pl.col("destination") == destination.upper())
    )
    return _add_flight_markup(results).to_dicts()


def get_featured_flights(limit: int = 6) -> list[dict]:
    df = load_flights()
    featured = pl.concat([
        df.filter(pl.col("type") == "domestic").head(4),
        df.filter(pl.col("type") == "international").head(4),
    ])
    return _add_flight_markup(featured).to_dicts()


def get_all_origins() -> list[str]:
    df = load_flights()
    return sorted(df.select("origin").unique().to_series().to_list())


def get_destinations_for_origin(origin: str) -> list[str]:
    df = load_flights()
    return sorted(
        df.filter(pl.col("origin") == origin.upper())
        .select("destination")
        .unique()
        .to_series()
        .to_list()
    )


# ---------------------------------------------------------------------------
# Hotels
# ---------------------------------------------------------------------------

def load_hotels() -> pl.DataFrame:
    return pl.read_csv(DATA_DIR / "hotels_cache.csv")


def _add_hotel_markup(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (pl.col("base_price_per_night") + MARKUP["hotel"]).alias("selling_price")
    )


def search_hotels(city: str) -> list[dict]:
    df = load_hotels()
    results = df.filter(
        pl.col("city").str.to_lowercase() == city.lower()
    )
    return _add_hotel_markup(results).to_dicts()


def get_featured_hotels(limit: int = 6) -> list[dict]:
    df = load_hotels()
    featured = pl.concat([
        df.filter(pl.col("type") == "domestic").head(4),
        df.filter(pl.col("type") == "international").head(3),
    ])
    return _add_hotel_markup(featured).to_dicts()


def get_hotel_cities() -> list[str]:
    df = load_hotels()
    return sorted(df.select("city").unique().to_series().to_list())


# ---------------------------------------------------------------------------
# Tours
# ---------------------------------------------------------------------------

def load_tours() -> pl.DataFrame:
    return pl.read_csv(DATA_DIR / "tours_catalog.csv")


def _add_tour_markup(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("type") == "domestic")
        .then(pl.col("base_price") + MARKUP["domestic_tour"])
        .otherwise(pl.col("base_price") + MARKUP["international_tour"])
        .alias("selling_price")
    )


def search_tours(destination: str = "", tour_type: str = "") -> list[dict]:
    df = load_tours()
    if destination:
        df = df.filter(
            pl.col("destination").str.to_lowercase().str.contains(destination.lower())
        )
    if tour_type and tour_type in ("domestic", "international"):
        df = df.filter(pl.col("type") == tour_type)
    return _add_tour_markup(df).to_dicts()


def get_featured_tours(limit: int = 6) -> list[dict]:
    df = load_tours()
    featured = pl.concat([
        df.filter(pl.col("type") == "domestic").head(4),
        df.filter(pl.col("type") == "international").head(4),
    ])
    return _add_tour_markup(featured).to_dicts()


# ---------------------------------------------------------------------------
# Explore feed — mixed featured deals
# ---------------------------------------------------------------------------

def get_explore_feed() -> dict:
    return {
        "flights": get_featured_flights(),
        "hotels": get_featured_hotels(),
        "tours": get_featured_tours(),
    }


# ---------------------------------------------------------------------------
# Paginated loaders (8 per page, optional sub filter)
# ---------------------------------------------------------------------------

PAGE_SIZE = 8


def _paginate(df: pl.DataFrame, page: int, sub: str) -> dict:
    if sub and sub != "all":
        df = df.filter(pl.col("type") == sub)
    total = len(df)
    pages = max(1, (total + PAGE_SIZE - 1) // PAGE_SIZE)
    page = max(1, min(page, pages))
    offset = (page - 1) * PAGE_SIZE
    items = df.slice(offset, PAGE_SIZE).to_dicts()
    return {"items": items, "page": page, "pages": pages, "total": total}


def get_flights_page(page: int = 1, sub: str = "all") -> dict:
    df = _add_flight_markup(load_flights())
    return _paginate(df, page, sub)


def get_hotels_page(page: int = 1, sub: str = "all") -> dict:
    df = _add_hotel_markup(load_hotels())
    return _paginate(df, page, sub)


def get_tours_page(page: int = 1, sub: str = "all") -> dict:
    df = _add_tour_markup(load_tours())
    return _paginate(df, page, sub)
