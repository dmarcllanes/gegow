"""
Gegow-Gear — dropshipping store for travel accessories.
Products are statically defined (extend to a DB/API later).
Cart state is managed via localStorage on the client.
"""

from fasthtml.common import Div, H2, P, Span, A, Script, Button

from app.components.cards import gear_card, section_header


GEAR_CATALOG = [
    {
        "id": "GR001",
        "name": "Samsonite Carry-On Spinner",
        "description": "Lightweight hard-shell, fits overhead bin",
        "price": 8500,
        "emoji": "🧳",
        "category": "luggage",
    },
    {
        "id": "GR002",
        "name": "Memory Foam Neck Pillow",
        "description": "Ergonomic support for long-haul flights",
        "price": 850,
        "emoji": "😴",
        "category": "comfort",
    },
    {
        "id": "GR003",
        "name": "Universal Travel Adapter",
        "description": "Works in 150+ countries, 4 USB ports",
        "price": 650,
        "emoji": "🔌",
        "category": "electronics",
    },
    {
        "id": "GR004",
        "name": "Compression Packing Cubes (6-set)",
        "description": "Maximize luggage space, stays organized",
        "price": 1200,
        "emoji": "📦",
        "category": "luggage",
    },
    {
        "id": "GR005",
        "name": "Portable Power Bank 20,000mAh",
        "description": "Fast-charge for phones, tablets, earbuds",
        "price": 1800,
        "emoji": "🔋",
        "category": "electronics",
    },
    {
        "id": "GR006",
        "name": "RFID Blocking Travel Wallet",
        "description": "Slim, holds cards + passport safely",
        "price": 950,
        "emoji": "👜",
        "category": "security",
    },
    {
        "id": "GR007",
        "name": "Quick-Dry Microfiber Towel",
        "description": "Ultra-compact, dries in minutes",
        "price": 750,
        "emoji": "🏖️",
        "category": "comfort",
    },
    {
        "id": "GR008",
        "name": "Wireless Noise-Cancelling Earbuds",
        "description": "30hr battery, active noise cancellation",
        "price": 3200,
        "emoji": "🎧",
        "category": "electronics",
    },
    {
        "id": "GR009",
        "name": "Packable Rain Jacket",
        "description": "Waterproof, folds into its own pocket",
        "price": 2100,
        "emoji": "🧥",
        "category": "clothing",
    },
    {
        "id": "GR010",
        "name": "Anti-Theft Backpack 30L",
        "description": "Hidden zippers, USB charging port, TSA-friendly",
        "price": 3500,
        "emoji": "🎒",
        "category": "luggage",
    },
    {
        "id": "GR011",
        "name": "Luggage Scale (Digital)",
        "description": "Avoid excess baggage fees at check-in",
        "price": 450,
        "emoji": "⚖️",
        "category": "luggage",
    },
    {
        "id": "GR012",
        "name": "Travel Toiletry Set (TSA-Approved)",
        "description": "Leak-proof bottles + clear pouch",
        "price": 580,
        "emoji": "🪥",
        "category": "comfort",
    },
]

CATEGORIES = {
    "all": "All",
    "luggage": "🧳 Luggage",
    "electronics": "⚡ Electronics",
    "comfort": "😌 Comfort",
    "security": "🔒 Security",
    "clothing": "👗 Clothing",
}

SHOP_CSS = """
.shop-banner {
    background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
    padding: 20px 16px;
    color: #fff;
}
.shop-banner-title { font-size: 22px; font-weight: 800; margin-bottom: 4px; }
.shop-banner-sub { font-size: 13px; opacity: 0.9; }
.category-tabs {
    display: flex;
    gap: 8px;
    padding: 12px 16px;
    overflow-x: auto;
    scrollbar-width: none;
}
.category-tabs::-webkit-scrollbar { display: none; }
.cat-tab {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    white-space: nowrap;
    cursor: pointer;
    border: 1.5px solid #E8E0D0;
    background: #fff;
    color: #78716C;
    text-decoration: none;
}
.cat-tab.active { background: #0D9488; color: #fff; border-color: #0D9488; }
.cart-fab {
    position: fixed;
    bottom: 82px;
    right: 16px;
    background: #F59E0B;
    color: #fff;
    border: none;
    width: 52px; height: 52px;
    border-radius: 50%;
    font-size: 22px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    display: flex; align-items: center; justify-content: center;
    z-index: 150;
}
.cart-badge {
    position: absolute;
    top: -4px; right: -4px;
    background: #DC2626;
    color: #fff;
    border-radius: 50%;
    width: 20px; height: 20px;
    font-size: 11px; font-weight: 700;
    display: none; align-items: center; justify-content: center;
}
.gear-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    padding: 0 16px 16px;
}
.gear-grid .card { margin: 0; }
"""


def setup(rt):

    @rt('/gear/cart')
    def post():
        # Client-side only (localStorage); server just returns 204-equivalent
        return Div()
