# Gegow Monitoring Checklist

To "avoid crush" and ensure "preventive maintenance," here are the specific metrics you should monitor for the Gegow platform:

## 1. Technical Vitals (Preventive Maintenance)
*   **Search Latency**: Monitor how long `polars_engine.py` takes to load and filter your CSVs. Target: <500ms.
*   **Memory Usage**: Monitor `psutil.virtual_memory()` to prevent spikes from large CSVs.
*   **Supabase Connection**: Ensure `SUPABASE_URL` and `SUPABASE_ANON_KEY` are valid by checking `supabase_db.is_configured()`.

## 2. Data Health (Supply Chain)
*   **Empty Caches**: Alert if `flights_cache.csv` or `hotels_cache.csv` has 0 rows.
*   **Stale Data**: Monitor `os.path.getmtime()` of your data files. If >24h old, update is needed.
*   **Markup Integrity**: Sanity check: `selling_price > base_price` for all items.

## 3. Marketing & User Funnel
*   **"No Results" Searches**: Log failed searches to identify travel inventory gaps.
*   **Suitcase Conversion**: Track "Save to Suitcase" clicks vs. total visitors.
*   **B2B Lead Success**: Monitor `save_b2b_lead` successes to avoid losing partners.

## 4. Security & Reliability
*   **OAuth Health**: Monitor `exchange_pkce_code` failures in `supabase_db.py`.
*   **Service Worker Sync**: Ensure `sw.js` is successfully caching the "Suitcase" for offline use.

---

### Implementation Tip (DIY Middleware)
Add this to your `app/main.py` to catch "crush" events and log them:

```python
import traceback
from fasthtml.common import *

async def error_logger_middleware(app, request, next):
    try:
        return await next(request)
    except Exception as e:
        # In a real setup, log stack_trace to a database table or a file
        stack_trace = traceback.format_exc()
        # Log: f"ERROR: {str(e)}\n{stack_trace}"
        return Titled("Under Maintenance", P("We're fixing a minor issue. Please try again soon."))
```
