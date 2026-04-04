"""
Premium card components — Airbnb/Agoda inspired.
Each card has a real destination photo header with gradient overlay,
deal badges, and polished price display.
"""

from fasthtml.common import Div, Span, A, Button

CARDS_CSS = ""  # All styles in main.py CSS block

# ── Destination photo map (Unsplash) ────────────────────────
_UNS = "https://images.unsplash.com/photo-"
DEST_IMG = {
    'MNL': _UNS + '1518509562904-e7ef99cdcc86?w=480&q=80&auto=format&fit=crop',   # Manila bay
    'CEB': _UNS + '1559128010-7c1ad6e1b6a5?w=480&q=80&auto=format&fit=crop',      # Cebu / turquoise sea
    'DVO': _UNS + '1504609813442-a8924e83f76e?w=480&q=80&auto=format&fit=crop',    # tropical jungle
    'KLO': _UNS + '1507525428034-b723cf961d3e?w=480&q=80&auto=format&fit=crop',    # Boracay white beach
    'MPH': _UNS + '1510414842594-a61c69b5ae57?w=480&q=80&auto=format&fit=crop',    # Boracay sunset
    'PPS': _UNS + '1501854140801-50d01698950b?w=480&q=80&auto=format&fit=crop',    # Palawan island
    'IAO': _UNS + '1455218873509-8097305ee378?w=480&q=80&auto=format&fit=crop',    # Siargao / surf
    'GES': _UNS + '1504609813442-a8924e83f76e?w=480&q=80&auto=format&fit=crop',    # General Santos
    'SIN': _UNS + '1565967511849-76a60a516170?w=480&q=80&auto=format&fit=crop',    # Singapore Marina
    'HKG': _UNS + '1474044159687-1ee9f3a51722?w=480&q=80&auto=format&fit=crop',    # Hong Kong skyline
    'NRT': _UNS + '1540959733332-eab4deabeeaf?w=480&q=80&auto=format&fit=crop',    # Tokyo night
    'KUL': _UNS + '1596422846543-75c6fc197f07?w=480&q=80&auto=format&fit=crop',    # Kuala Lumpur
    'DXB': _UNS + '1512453979798-5ea266f8880c?w=480&q=80&auto=format&fit=crop',    # Dubai
    'ICN': _UNS + '1517154421773-0529f29ea451?w=480&q=80&auto=format&fit=crop',    # Seoul
    'BKK': _UNS + '1508009603885-50cf7c579365?w=480&q=80&auto=format&fit=crop',    # Bangkok temple
    'SYD': _UNS + '1506973035872-a4ec16b8e8d9?w=480&q=80&auto=format&fit=crop',    # Sydney opera
}

CITY_IMG = {
    'Cebu':       _UNS + '1559128010-7c1ad6e1b6a5?w=480&q=80&auto=format&fit=crop',
    'Boracay':    _UNS + '1507525428034-b723cf961d3e?w=480&q=80&auto=format&fit=crop',
    'Palawan':    _UNS + '1501854140801-50d01698950b?w=480&q=80&auto=format&fit=crop',
    'Siargao':    _UNS + '1455218873509-8097305ee378?w=480&q=80&auto=format&fit=crop',
    'Davao':      _UNS + '1504609813442-a8924e83f76e?w=480&q=80&auto=format&fit=crop',
    'Manila':     _UNS + '1518509562904-e7ef99cdcc86?w=480&q=80&auto=format&fit=crop',
    'Singapore':  _UNS + '1565967511849-76a60a516170?w=480&q=80&auto=format&fit=crop',
    'Tokyo':      _UNS + '1540959733332-eab4deabeeaf?w=480&q=80&auto=format&fit=crop',
    'Bangkok':    _UNS + '1508009603885-50cf7c579365?w=480&q=80&auto=format&fit=crop',
    'Seoul':      _UNS + '1517154421773-0529f29ea451?w=480&q=80&auto=format&fit=crop',
    'Hong Kong':  _UNS + '1474044159687-1ee9f3a51722?w=480&q=80&auto=format&fit=crop',
    'Dubai':      _UNS + '1512453979798-5ea266f8880c?w=480&q=80&auto=format&fit=crop',
    'Sydney':     _UNS + '1506973035872-a4ec16b8e8d9?w=480&q=80&auto=format&fit=crop',
}

TOUR_IMG = {
    'domestic':      _UNS + '1501854140801-50d01698950b?w=480&q=80&auto=format&fit=crop',  # Palawan islands
    'international': _UNS + '1540959733332-eab4deabeeaf?w=480&q=80&auto=format&fit=crop',  # Tokyo
}

# ── Destination gradient palette (fallback) ─────────────────
DEST_GRAD = {
    'MNL': 'linear-gradient(135deg,#0D9488 0%,#0F766E 100%)',
    'CEB': 'linear-gradient(135deg,#0EA5E9 0%,#1E40AF 100%)',
    'DVO': 'linear-gradient(135deg,#10B981 0%,#065F46 100%)',
    'KLO': 'linear-gradient(135deg,#F59E0B 0%,#B45309 100%)',
    'MPH': 'linear-gradient(135deg,#38BDF8 0%,#0284C7 100%)',
    'PPS': 'linear-gradient(135deg,#06B6D4 0%,#0E7490 100%)',
    'IAO': 'linear-gradient(135deg,#14B8A6 0%,#0F766E 100%)',
    'GES': 'linear-gradient(135deg,#A78BFA 0%,#7C3AED 100%)',
    'SIN': 'linear-gradient(135deg,#8B5CF6 0%,#4F46E5 100%)',
    'HKG': 'linear-gradient(135deg,#EF4444 0%,#B91C1C 100%)',
    'NRT': 'linear-gradient(135deg,#F472B6 0%,#BE185D 100%)',
    'KUL': 'linear-gradient(135deg,#F97316 0%,#C2410C 100%)',
    'DXB': 'linear-gradient(135deg,#F59E0B 0%,#92400E 100%)',
    'ICN': 'linear-gradient(135deg,#3B82F6 0%,#1D4ED8 100%)',
    'BKK': 'linear-gradient(135deg,#A78BFA 0%,#9333EA 100%)',
    'SYD': 'linear-gradient(135deg,#34D399 0%,#059669 100%)',
}
CITY_GRAD = {
    'Cebu':       'linear-gradient(135deg,#0EA5E9 0%,#1E40AF 100%)',
    'Boracay':    'linear-gradient(135deg,#38BDF8 0%,#0D9488 100%)',
    'Palawan':    'linear-gradient(135deg,#06B6D4 0%,#0369A1 100%)',
    'Siargao':    'linear-gradient(135deg,#14B8A6 0%,#0EA5E9 100%)',
    'Davao':      'linear-gradient(135deg,#10B981 0%,#15803D 100%)',
    'Manila':     'linear-gradient(135deg,#0D9488 0%,#0F766E 100%)',
    'Singapore':  'linear-gradient(135deg,#8B5CF6 0%,#4F46E5 100%)',
    'Tokyo':      'linear-gradient(135deg,#F472B6 0%,#E11D48 100%)',
    'Bangkok':    'linear-gradient(135deg,#F97316 0%,#9333EA 100%)',
    'Seoul':      'linear-gradient(135deg,#3B82F6 0%,#06B6D4 100%)',
    'Hong Kong':  'linear-gradient(135deg,#EF4444 0%,#F97316 100%)',
    'Dubai':      'linear-gradient(135deg,#F59E0B 0%,#EF4444 100%)',
    'Sydney':     'linear-gradient(135deg,#34D399 0%,#0EA5E9 100%)',
}
TOUR_GRAD = {
    'domestic':      'linear-gradient(135deg,#0EA5E9 0%,#10B981 100%)',
    'international': 'linear-gradient(135deg,#8B5CF6 0%,#F59E0B 100%)',
}

POPULAR_ROUTES = {'MNL-CEB', 'MNL-DVO', 'MNL-KLO', 'MNL-MPH', 'MNL-PPS'}


def _peso(amount: float | int) -> str:
    return f"₱{int(amount):,}"


def _flight_badge(flight: dict) -> tuple[str, str]:
    if flight['type'] == 'international':
        return '🌏 International', 'badge-intl'
    route = f"{flight['origin']}-{flight['destination']}"
    if route in POPULAR_ROUTES:
        return '🔥 Popular', 'badge-hot'
    return '✈️ Domestic', 'badge-dom'


def _savings_label(selling: float, base: float) -> str:
    saved = int(selling - base)
    return f"+₱{saved:,} markup"   # shown as "from" price to agent


def flight_card(flight: dict, book_href: str = "") -> Div:
    grad = DEST_GRAD.get(flight['destination'], DEST_GRAD['MNL'])
    img  = DEST_IMG.get(flight['destination'], DEST_IMG.get('MNL', ''))
    badge_text, badge_cls = _flight_badge(flight)
    if not book_href:
        book_href = f"/book?type=flight&origin={flight['origin']}&destination={flight['destination']}"

    img_style = (
        f"background:linear-gradient(to bottom,rgba(0,0,0,.15) 0%,rgba(0,0,0,.65) 100%),"
        f"url('{img}') center/cover no-repeat,{grad}"
    )

    return Div(
        # Visual header with photo
        Div(
            # Badge overlaid top-left
            Span(badge_text, cls=f'vc-badge-img {badge_cls}'),
            # Route codes
            Div(
                Span(flight['origin'], cls='vc-code'),
                Div(cls='vc-line'),
                Span(flight['destination'], cls='vc-code'),
                cls='vc-route',
            ),
            Div(f"{flight['origin_city']} → {flight['destination_city']}", cls='vc-cities'),
            cls='card-visual', style=img_style,
        ),
        # Details
        Div(
            Div(
                Span(flight['airline'], cls='c-airline'),
                Span('·', cls='c-dot'),
                Span(f"{flight['departure']} – {flight['arrival']}", cls='c-time'),
                cls='c-meta',
            ),
            Div(
                Div(
                    Span('from', cls='from-label'),
                    Span(_peso(flight['selling_price']), cls='price-big'),
                    Span('/ way', cls='price-unit'),
                ),
                A('Book Now →', href=book_href, cls='btn-book'),
                cls='c-footer',
            ),
            cls='card-body',
        ),
        cls='card fade-up', data_subcat=flight['type'],
    )


def hotel_card(hotel: dict, book_href: str = "") -> Div:
    grad = CITY_GRAD.get(hotel['city'], 'linear-gradient(135deg,#0D9488,#0F766E)')
    img  = CITY_IMG.get(hotel['city'], '')
    stars_filled = '★' * hotel['stars']
    stars_empty  = '☆' * (5 - hotel['stars'])
    if not book_href:
        book_href = f"/book?type=hotel&city={hotel['city']}"
    amenities = hotel.get('amenities', '').split('|')[:3]

    img_style = (
        f"background:linear-gradient(to bottom,rgba(0,0,0,.1) 0%,rgba(0,0,0,.6) 100%),"
        f"url('{img}') center/cover no-repeat,{grad}" if img else f"background:{grad}"
    )

    return Div(
        Div(
            Span('🏨 Hotel', cls='vc-badge-img badge-dom'),
            Div(
                Span(f'{"★" * hotel["stars"]}', cls='vc-stars'),
                Div(hotel['name'], cls='vc-hotel-name'),
                Div(f'📍 {hotel["location"]}', cls='vc-cities'),
                cls='vc-hotel-info',
            ),
            cls='card-visual', style=img_style,
        ),
        Div(
            Div(
                Span(f'{stars_filled}{stars_empty}', cls='star-row'),
                Span(f'{hotel["stars"]}-star', cls='star-label'),
            ),
            Div(' · '.join(amenities), cls='c-meta', style='margin-top:4px'),
            Div(
                Div(
                    Span('from', cls='from-label'),
                    Span(_peso(hotel['selling_price']), cls='price-big'),
                    Span('/ night', cls='price-unit'),
                ),
                A('Book Now →', href=book_href, cls='btn-book'),
                cls='c-footer',
            ),
            cls='card-body',
        ),
        cls='card fade-up', data_subcat=hotel.get('type', 'domestic'),
    )


def tour_card(tour: dict, book_href: str = "") -> Div:
    grad = TOUR_GRAD.get(tour['type'], TOUR_GRAD['domestic'])
    img  = TOUR_IMG.get(tour['type'], TOUR_IMG['domestic'])
    badge_text = '🌴 Local Tour' if tour['type'] == 'domestic' else '🌍 International'
    badge_cls  = 'badge-dom' if tour['type'] == 'domestic' else 'badge-intl'
    if not book_href:
        book_href = f"/book?type=tour&id={tour['id']}"
    includes = tour.get('includes', '').split('|')[:3]

    img_style = (
        f"background:linear-gradient(to bottom,rgba(0,0,0,.1) 0%,rgba(0,0,0,.6) 100%),"
        f"url('{img}') center/cover no-repeat,{grad}"
    )

    return Div(
        Div(
            Span(badge_text, cls=f'vc-badge-img {badge_cls}'),
            Div(
                Span(f"{tour['duration_days']}D {tour['duration_nights']}N", cls='vc-duration'),
                Div(tour['name'], cls='vc-hotel-name'),
                Div(f'📍 {tour["destination"]}', cls='vc-cities'),
                cls='vc-hotel-info',
            ),
            cls='card-visual', style=img_style,
        ),
        Div(
            Div(' · '.join(includes), cls='c-meta'),
            Div(
                Div(
                    Span('from', cls='from-label'),
                    Span(_peso(tour['selling_price']), cls='price-big'),
                    Span('/ person', cls='price-unit'),
                ),
                A('Book Now →', href=book_href, cls='btn-book'),
                cls='c-footer',
            ),
            cls='card-body',
        ),
        cls='card fade-up', data_subcat=tour['type'],
    )


def gear_card(item: dict) -> Div:
    return Div(
        Div(
            Span(item.get('emoji', '🧳'), cls='gear-emoji'),
            cls='gear-visual',
        ),
        Div(
            Div(item['name'], cls='card-title'),
            Div(item.get('description', ''), cls='c-meta', style='margin-top:4px'),
            Div(
                Span(_peso(item['price']), cls='price-big'),
                cls='c-footer', style='margin-top:12px;justify-content:flex-start',
            ),
            A('Add to Cart', href='#', cls='btn-outline',
              hx_post='/gear/cart',
              hx_vals=f'{{"item_id":"{item["id"]}","name":"{item["name"]}","price":{item["price"]}}}',
              hx_swap='none',
              onclick='addToCart(this);return false;'),
            cls='card-body',
        ),
        cls='card fade-up',
    )


def section_header(title: str, see_all_href: str = "") -> Div:
    children = [Span(title, cls='section-hdr-title')]
    if see_all_href:
        children.append(A('See all →', href=see_all_href, cls='section-hdr-link'))
    return Div(*children, cls='section-hdr')
