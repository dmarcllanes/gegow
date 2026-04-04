"""
Booking route — Gegow Path 5-step wizard.
All steps are HTMX partial swaps into #wizard-content.
"""

import random
from fasthtml.common import Div, H2, P, Script

from app.logic import polars_engine as pe
from app.components.wizard import (
    wizard_step1,
    wizard_step2_flight,
    wizard_step2_hotel,
    wizard_step2_tour,
    wizard_step3,
    wizard_step4,
    wizard_step5,
    wizard_confirmed,
)


def setup(rt):

    # Step 1 — trip type selection
    @rt('/book/step1')
    def get():
        return wizard_step1()

    # Step 2 — destination
    @rt('/book/step2')
    def get(trip_type: str = "flight"):
        return _render_step2(trip_type)

    # Step 3 — dates (receives all accumulated params as query strings)
    @rt('/book/step3')
    def get(
        trip_type: str = "flight",
        origin: str = "",
        destination: str = "",
        city: str = "",
        tour_dest: str = "",
        tour_type: str = "",
    ):
        params = {k: v for k, v in {
            "trip_type": trip_type,
            "origin": origin,
            "destination": destination,
            "city": city,
            "tour_dest": tour_dest,
            "tour_type": tour_type,
        }.items() if v}
        return wizard_step3(params)

    # Step 4 — travelers
    @rt('/book/step4')
    def get(
        trip_type: str = "flight",
        origin: str = "",
        destination: str = "",
        city: str = "",
        tour_dest: str = "",
        tour_type: str = "",
        date_from: str = "",
        date_to: str = "",
    ):
        params = {k: v for k, v in {
            "trip_type": trip_type,
            "origin": origin,
            "destination": destination,
            "city": city,
            "tour_dest": tour_dest,
            "tour_type": tour_type,
            "date_from": date_from,
            "date_to": date_to,
        }.items() if v}
        return wizard_step4(params)

    # Step 5 — review results
    @rt('/book/step5')
    def get(
        trip_type: str = "flight",
        origin: str = "",
        destination: str = "",
        city: str = "",
        tour_dest: str = "",
        tour_type: str = "",
        date_from: str = "",
        date_to: str = "",
        adults: str = "1",
        children: str = "0",
    ):
        params = {k: v for k, v in {
            "trip_type": trip_type,
            "origin": origin,
            "destination": destination,
            "city": city,
            "tour_dest": tour_dest,
            "tour_type": tour_type,
            "date_from": date_from,
            "date_to": date_to,
            "adults": adults,
            "children": children,
        }.items() if v}

        results = _search_results(trip_type, origin, destination, city, tour_dest, tour_type)
        return wizard_step5(params, results)

    # Confirm booking — saves to localStorage via JS injection
    @rt('/book/confirm')
    def post(
        trip_type: str = "flight",
        item_id: str = "",
        adults: str = "1",
        children: str = "0",
        date_from: str = "",
        date_to: str = "",
        total: str = "0",
    ):
        ref = f"{random.randint(10000, 99999)}"
        booking = {
            "ref": ref,
            "trip_type": trip_type,
            "item_id": item_id,
            "adults": int(adults),
            "children": int(children),
            "date_from": date_from,
            "date_to": date_to,
            "total": int(total),
            "label": _booking_label(trip_type, item_id),
        }
        # Inject JS to save to localStorage suitcase
        save_script = Script(f"""
            saveToSuitcase({str(booking).replace("'", '"')});
        """)
        return Div(
            wizard_confirmed(booking),
            save_script,
        )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _render_step2(trip_type: str):
    if trip_type == "flight":
        origins = pe.get_all_origins()
        return wizard_step2_flight(origins)
    elif trip_type == "hotel":
        cities = pe.get_hotel_cities()
        return wizard_step2_hotel(cities)
    else:
        return wizard_step2_tour()


def _search_results(
    trip_type: str,
    origin: str = "",
    destination: str = "",
    city: str = "",
    tour_dest: str = "",
    tour_type: str = "",
) -> list[dict]:
    if trip_type == "flight":
        if origin and destination:
            return pe.search_flights(origin, destination)
        return pe.get_featured_flights()
    elif trip_type == "hotel":
        if city:
            results = pe.search_hotels(city)
            return results if results else pe.get_featured_hotels()
        return pe.get_featured_hotels()
    else:
        return pe.search_tours(destination=tour_dest, tour_type=tour_type)


def _booking_label(trip_type: str, item_id: str) -> str:
    try:
        if trip_type == "flight":
            flights = pe.load_flights().filter(
                __import__("polars").col("id") == item_id
            ).to_dicts()
            if flights:
                f = flights[0]
                return f"{f['origin_city']} → {f['destination_city']} ({f['airline']})"
        elif trip_type == "hotel":
            hotels = pe.load_hotels().filter(
                __import__("polars").col("id") == item_id
            ).to_dicts()
            if hotels:
                return hotels[0]["name"]
        elif trip_type == "tour":
            tours = pe.load_tours().filter(
                __import__("polars").col("id") == item_id
            ).to_dicts()
            if tours:
                return tours[0]["name"]
    except Exception:
        pass
    return f"{trip_type.title()} Booking"
