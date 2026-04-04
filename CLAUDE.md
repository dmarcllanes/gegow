# Gegow: Digital Travel Agency PWA

## Project Overview
Gegow is a "digital-in-pocket" travel agency built using FastHTML and Polars. It connects to the Bakasyonista backend to offer flights, hotels, tours, and dropshipped travel gear with custom markup logic.

## Tech Stack
- **Backend/Frontend**: FastHTML (Python-based)
- **Data Engine**: Polars (for high-speed catalog processing and markup calcs)
- **Database**: Supabase (User profiles, "My Suitcase" itineraries, B2B leads)
- **Deployment**: Docker on Hugging Face or Vercel
- **PWA**: Manifest.json + Service Workers for offline itinerary access

## Business Logic & Markups
- [cite_start]**Domestic Flights**: +₱250 - ₱400 profit per way [cite: 23]
- [cite_start]**International Flights**: +₱1,000 - ₱3,000+ profit per way [cite: 24, 25]
- [cite_start]**Hotel Stays**: +₱300 - ₱1,000 profit per night [cite: 36]
- [cite_start]**Joiner/Domestic Tours**: +₱400 - ₱900 profit per person [cite: 39, 41]
- [cite_start]**International Tours**: +₱500 - ₱2,000+ profit per person [cite: 42]

## Core Features
1. **Gegow Path (Wizard)**: 5-step booking flow to prevent information overload.
2. **My Suitcase**: Offline-ready storage for vouchers and schedules.
3. [cite_start]**Gegow-Gear**: Dropshipping store for travel items[cite: 74].
4. [cite_start]**B2B Portal**: Specialized entry for Manning Agencies and Corporate clients[cite: 85, 86].

## Coding Guidelines
- Use **FastHTML** components for modular UI (Cards, Wizards, Modals).
- Use **Polars DataFrames** for all heavy filtering of the Bakasyonista CSV/API data.
- Maintain a **Teal and Beige** color palette for a modern "Philippine Sea" aesthetic.
- Ensure all forms use the **Wizard pattern** to maintain simplicity.