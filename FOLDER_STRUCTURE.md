# Gegow Project Structure

gegow/
├── app/
│   ├── main.py              # Entry point for FastHTML app
│   ├── components/          # Reusable UI elements
│   │   ├── wizard.py        # The "Gegow Path" multi-step logic
│   │   ├── cards.py         # Travel package & gear display cards
│   │   ├── navigation.py    # PWA Bottom Nav & Header
│   │   └── suitcase.py      # Itinerary display components
│   ├── routes/              # Page definitions
│   │   ├── explore.py       # "Gegow Now" Discovery feed
│   │   ├── booking.py       # Flight/Hotel/Ferry engines
│   │   ├── shop.py          # Dropshipping Gear store
│   │   └── b2b.py           # Corporate & Manning Agency portal
│   └── logic/
│       ├── polars_engine.py # Catalog processing & markup calculations
│       └── supabase_db.py   # User data & booking persistence
├── static/                  # PWA Assets
│   ├── icons/               # Gegow branded icons
│   ├── images/              # Hero shots and tour previews
│   ├── manifest.json        # PWA configuration
│   └── sw.js                # Service Worker for offline "Suitcase"
├── data/                    # Local cache/CSV from supplier
│   ├── flights_cache.csv
│   ├── hotels_cache.csv
│   └── tours_catalog.csv
├── tests/                   # Unit tests for markup logic
├── Dockerfile               # Containerization for deployment
├── requirements.txt         # fasthtml, polars, pydantic, supabase
└── README.md                # Project setup and branding info