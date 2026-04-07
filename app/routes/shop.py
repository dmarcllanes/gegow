"""
Gegow Shop — Souvenirs, Food & Pasalubong, Beach & Water Gear, Clothing, Travel Accessories.
"""

from fasthtml.common import Div, Span, A, Script, Button


# ─────────────────────────────────────────────────────────────
# CATALOG
# ─────────────────────────────────────────────────────────────

SHOP_CATALOG = [

    # ── 🎁 SOUVENIRS & PASALUBONG ──────────────────────────────
    {
        "id": "SV001",
        "name": "Pasalubong Gift Box (Assorted)",
        "description": "Dried mango, polvoron, choco, native snacks",
        "price": 485,
        "emoji": "🎁",
        "category": "souvenir",
        "badge": "Bestseller",
    },
    {
        "id": "SV002",
        "name": "Handwoven Bayong Bag",
        "description": "Eco-friendly woven native bag, great for beach",
        "price": 380,
        "emoji": "👜",
        "category": "souvenir",
    },
    {
        "id": "SV003",
        "name": "Philippine Islands Ref Magnet Set (6 pcs)",
        "description": "Cebu, Boracay, Palawan, Siargao, Manila, Davao",
        "price": 220,
        "emoji": "🧲",
        "category": "souvenir",
        "badge": "New",
    },
    {
        "id": "SV004",
        "name": "Jeepney Keychain (Handpainted)",
        "description": "Authentic Filipino jeepney miniature, vibrant colors",
        "price": 150,
        "emoji": "🚌",
        "category": "souvenir",
    },
    {
        "id": "SV005",
        "name": "Malong Fabric Wrap",
        "description": "Traditional Mindanao woven fabric, multipurpose",
        "price": 650,
        "emoji": "🪢",
        "category": "souvenir",
    },
    {
        "id": "SV006",
        "name": "Native Buri Hat (Salakot-style)",
        "description": "Sun protection, handwoven, one size fits most",
        "price": 295,
        "emoji": "👒",
        "category": "souvenir",
    },
    {
        "id": "SV007",
        "name": "Filipino Collectible Snow Globe",
        "description": "Intramuros & Jeepney design, perfect gift",
        "price": 420,
        "emoji": "🌐",
        "category": "souvenir",
    },
    {
        "id": "SV008",
        "name": "Philippine Map Tote Bag",
        "description": "Canvas tote with Pilipinas island map print",
        "price": 350,
        "emoji": "🗺️",
        "category": "souvenir",
        "badge": "New",
    },

    # ── 🍱 FOOD & LOCAL DELICACIES ─────────────────────────────
    {
        "id": "FD001",
        "name": "Dried Mango Chips – Cebu (200g)",
        "description": "Sweet & tangy, airport bestseller, no preservatives",
        "price": 280,
        "emoji": "🥭",
        "category": "food",
        "badge": "Bestseller",
    },
    {
        "id": "FD002",
        "name": "Malagos Craft Chocolate – Davao (3-pack)",
        "description": "Award-winning single-origin PH dark chocolate",
        "price": 495,
        "emoji": "🍫",
        "category": "food",
        "badge": "New",
    },
    {
        "id": "FD003",
        "name": "Polvoron Assorted Pack (24 pcs)",
        "description": "Classic, ube, pandan & strawberry flavors",
        "price": 320,
        "emoji": "🍪",
        "category": "food",
    },
    {
        "id": "FD004",
        "name": "Ube Jam Spread (220g)",
        "description": "Rich Benguet ube, perfect for pandesal & toast",
        "price": 195,
        "emoji": "🫙",
        "category": "food",
    },
    {
        "id": "FD005",
        "name": "Chicharon Bulaklak – Crispy Pack",
        "description": "Meaty, crunchy, with spiced vinegar sachet",
        "price": 180,
        "emoji": "🐷",
        "category": "food",
    },
    {
        "id": "FD006",
        "name": "Kapeng Barako Ground Coffee (200g)",
        "description": "Bold Batangas barako beans, strong & aromatic",
        "price": 245,
        "emoji": "☕",
        "category": "food",
    },
    {
        "id": "FD007",
        "name": "Otap & Broas Cookie Duo Pack",
        "description": "Cebuano puff pastry + ladyfingers, 2-in-1 box",
        "price": 165,
        "emoji": "🥐",
        "category": "food",
    },
    {
        "id": "FD008",
        "name": "Native Kakanin Assortment Box",
        "description": "Puto, kutsinta, sapin-sapin & palitaw selections",
        "price": 380,
        "emoji": "🍡",
        "category": "food",
        "badge": "New",
    },

    # ── 🏊 BEACH & WATER SPORTS ────────────────────────────────
    {
        "id": "BW001",
        "name": "Rash Guard – Long Sleeve UV50+",
        "description": "UPF 50+ sun protection, quick-dry, unisex S–XXL",
        "price": 899,
        "emoji": "🏄",
        "category": "beach",
        "badge": "Bestseller",
    },
    {
        "id": "BW002",
        "name": "Anti-Fog Swimming Goggles",
        "description": "Wide view, UV400, adjustable strap, adults & kids",
        "price": 420,
        "emoji": "🥽",
        "category": "beach",
    },
    {
        "id": "BW003",
        "name": "One-Piece Swimsuit (Women's)",
        "description": "High-waist, tummy control, S–XL, multiple colors",
        "price": 750,
        "emoji": "👙",
        "category": "beach",
        "badge": "New",
    },
    {
        "id": "BW004",
        "name": "Men's Board Shorts (Quick-dry)",
        "description": "4-way stretch, mesh lining, drawstring, S–XXL",
        "price": 580,
        "emoji": "🩱",
        "category": "beach",
    },
    {
        "id": "BW005",
        "name": "Full Snorkel Set (Mask + Tube + Fins)",
        "description": "Panoramic mask, dry-top tube, adjustable fins",
        "price": 1450,
        "emoji": "🤿",
        "category": "beach",
        "badge": "Bestseller",
    },
    {
        "id": "BW006",
        "name": "Waterproof Phone Dry Bag (2-pack)",
        "description": "IPX8 rated, fits up to 7\" screen, touch-sensitive",
        "price": 299,
        "emoji": "📱",
        "category": "beach",
    },
    {
        "id": "BW007",
        "name": "Rubber Slippers / Tsinelas (Unisex)",
        "description": "Anti-slip, lightweight, beach & reef-safe",
        "price": 350,
        "emoji": "🩴",
        "category": "beach",
    },
    {
        "id": "BW008",
        "name": "Aqua Water Shoes",
        "description": "Protects feet on reef, rocks & wet surfaces",
        "price": 680,
        "emoji": "👟",
        "category": "beach",
    },
    {
        "id": "BW009",
        "name": "XL Beach Tote Bag (Waterproof)",
        "description": "Holds towel, gear & change of clothes, zippered",
        "price": 495,
        "emoji": "🏖️",
        "category": "beach",
    },
    {
        "id": "BW010",
        "name": "Kids Floaties & Arm Bands Set",
        "description": "BPA-free, adjustable, for ages 3–8, bright colors",
        "price": 280,
        "emoji": "🦺",
        "category": "beach",
        "badge": "New",
    },

    # ── 👙 CLOTHING & APPAREL ──────────────────────────────────
    {
        "id": "CL001",
        "name": "Quick-Dry Travel Underwear 3-Pack (Men's)",
        "description": "Moisture-wicking, anti-odor, boxer brief style",
        "price": 750,
        "emoji": "🩲",
        "category": "clothing",
        "badge": "Bestseller",
    },
    {
        "id": "CL002",
        "name": "Quick-Dry Sports Bra 2-Pack (Women's)",
        "description": "Medium support, mesh panels, S–XL",
        "price": 680,
        "emoji": "👙",
        "category": "clothing",
    },
    {
        "id": "CL003",
        "name": "UV Protection Long-Sleeve Shirt",
        "description": "UPF 40+, breathable, fishing/outdoor style",
        "price": 950,
        "emoji": "👕",
        "category": "clothing",
    },
    {
        "id": "CL004",
        "name": "Compression Travel Socks 2-Pair",
        "description": "Reduces swelling on long flights, S/M & L/XL",
        "price": 450,
        "emoji": "🧦",
        "category": "clothing",
        "badge": "New",
    },
    {
        "id": "CL005",
        "name": "Men's Boxer Briefs 5-Pack (Quick-dry)",
        "description": "Anti-chafe, seamless waistband, breathable",
        "price": 1200,
        "emoji": "🩳",
        "category": "clothing",
    },
    {
        "id": "CL006",
        "name": "Packable Windbreaker Jacket",
        "description": "Folds into pocket, waterproof, unisex S–XXL",
        "price": 1850,
        "emoji": "🧥",
        "category": "clothing",
    },

    # ── 🎒 TRAVEL GEAR & ACCESSORIES ──────────────────────────
    {
        "id": "GR001",
        "name": "Hard-Shell Carry-On Spinner (20\")",
        "description": "TSA lock, lightweight, fits overhead bin",
        "price": 8500,
        "emoji": "🧳",
        "category": "gear",
        "badge": "Bestseller",
    },
    {
        "id": "GR002",
        "name": "Memory Foam Neck Pillow",
        "description": "Ergonomic support for long-haul flights",
        "price": 850,
        "emoji": "😴",
        "category": "gear",
    },
    {
        "id": "GR003",
        "name": "Universal Travel Adapter",
        "description": "Works in 150+ countries, 4 USB ports",
        "price": 650,
        "emoji": "🔌",
        "category": "gear",
    },
    {
        "id": "GR004",
        "name": "Compression Packing Cubes 6-set",
        "description": "Maximize luggage space, color-coded by size",
        "price": 1200,
        "emoji": "📦",
        "category": "gear",
    },
    {
        "id": "GR005",
        "name": "Portable Power Bank 20,000mAh",
        "description": "Fast-charge for phones, tablets & earbuds",
        "price": 1800,
        "emoji": "🔋",
        "category": "gear",
    },
    {
        "id": "GR006",
        "name": "RFID-Blocking Travel Wallet",
        "description": "Slim, holds cards + passport safely",
        "price": 950,
        "emoji": "💳",
        "category": "gear",
    },
    {
        "id": "GR007",
        "name": "Quick-Dry Microfiber Towel",
        "description": "Ultra-compact, dries in 20 minutes",
        "price": 750,
        "emoji": "🏊",
        "category": "gear",
    },
    {
        "id": "GR008",
        "name": "Wireless Noise-Cancelling Earbuds",
        "description": "30hr battery, active noise cancellation",
        "price": 3200,
        "emoji": "🎧",
        "category": "gear",
    },
    {
        "id": "GR009",
        "name": "Anti-Theft Backpack 30L",
        "description": "Hidden zippers, USB charging port, TSA-friendly",
        "price": 3500,
        "emoji": "🎒",
        "category": "gear",
    },
    {
        "id": "GR010",
        "name": "Digital Luggage Scale",
        "description": "Avoid excess baggage fees — up to 50kg",
        "price": 450,
        "emoji": "⚖️",
        "category": "gear",
    },
    {
        "id": "GR011",
        "name": "Travel Toiletry Set (TSA-Approved)",
        "description": "Leak-proof bottles + clear zip pouch",
        "price": 580,
        "emoji": "🪥",
        "category": "gear",
    },
    {
        "id": "GR012",
        "name": "First Aid Travel Kit",
        "description": "Plasters, antiseptic, meds, scissors, 42 items",
        "price": 680,
        "emoji": "🩹",
        "category": "gear",
        "badge": "New",
    },
    {
        "id": "GR013",
        "name": "Insect Repellent Bracelet (6-pack)",
        "description": "DEET-free, waterproof, 200 hrs protection",
        "price": 320,
        "emoji": "🦟",
        "category": "gear",
    },
    {
        "id": "GR014",
        "name": "SPF50 Mineral Sunscreen (Travel Size 4-pack)",
        "description": "50ml each, reef-safe, TSA-approved",
        "price": 480,
        "emoji": "🧴",
        "category": "gear",
    },
]

# Backward compat alias (used in app.js seedDemoData)
GEAR_CATALOG = SHOP_CATALOG


CATEGORIES = {
    "all":      "🛍️ All",
    "souvenir": "🎁 Souvenirs",
    "food":     "🍱 Food",
    "beach":    "🏊 Beach & Water",
    "clothing": "👙 Clothing",
    "gear":     "🎒 Gear",
}

SECTION_META = {
    "souvenir": ("🎁", "Souvenirs & Pasalubong", "Take a piece of the Philippines home"),
    "food":     ("🍱", "Food & Local Delicacies", "Authentic Filipino flavors & treats"),
    "beach":    ("🏊", "Beach & Water Sports",    "Everything you need for island life"),
    "clothing": ("👙", "Clothing & Apparel",       "Travel-ready threads that work harder"),
    "gear":     ("🎒", "Travel Gear",              "Smart accessories for every journey"),
}


def setup(rt):

    @rt('/gear/cart')
    def post():
        return Div()
