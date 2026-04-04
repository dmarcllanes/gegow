"""
Supabase integration for Gegow.
Handles user profiles, "My Suitcase" itineraries, and B2B leads.
Gracefully degrades if SUPABASE_URL / SUPABASE_KEY are not set.
"""

import os
import hashlib
import base64
import secrets
import httpx
from dotenv import load_dotenv

load_dotenv()

_client = None


def _sanitize(obj):
    """Recursively replace lone Unicode surrogates in all strings within a JSON object.

    Python's json.loads() can produce strings with lone surrogates (U+D800–U+DFFF)
    when the source JSON contains malformed \\uXXXX sequences.  These crash
    UTF-8 encoding later.  This helper replaces them with U+FFFD.
    """
    if isinstance(obj, str):
        return obj.encode("utf-8", errors="replace").decode("utf-8")
    if isinstance(obj, dict):
        return {k: _sanitize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_sanitize(v) for v in obj]
    return obj


def _get_client():
    global _client
    if _client is not None:
        return _client

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")
    if not url or not key:
        return None

    try:
        from supabase import create_client
        _client = create_client(url, key)
    except Exception:
        _client = None

    return _client


# ---------------------------------------------------------------------------
# Suitcase (saved itineraries)
# ---------------------------------------------------------------------------

def save_itinerary(user_id: str, itinerary: dict) -> dict | None:
    client = _get_client()
    if not client:
        return None
    try:
        result = client.table("suitcase").insert({
            "user_id": user_id,
            **itinerary,
        }).execute()
        return result.data[0] if result.data else None
    except Exception:
        return None


def get_itineraries(user_id: str) -> list[dict]:
    client = _get_client()
    if not client:
        return []
    try:
        result = (
            client.table("suitcase")
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )
        return _sanitize(result.data or [])
    except Exception:
        return []


def delete_itinerary(itinerary_id: str) -> bool:
    client = _get_client()
    if not client:
        return False
    try:
        client.table("suitcase").delete().eq("id", itinerary_id).execute()
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# B2B leads
# ---------------------------------------------------------------------------

def save_b2b_lead(lead: dict) -> dict | None:
    client = _get_client()
    if not client:
        return None
    try:
        result = client.table("b2b_leads").insert(lead).execute()
        return result.data[0] if result.data else None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# User profiles
# ---------------------------------------------------------------------------

def get_or_create_profile(user_id: str, email: str) -> dict | None:
    client = _get_client()
    if not client:
        return None
    try:
        result = (
            client.table("profiles")
            .select("*")
            .eq("id", user_id)
            .single()
            .execute()
        )
        if result.data:
            return result.data
        # Create profile
        created = client.table("profiles").insert({
            "id": user_id,
            "email": email,
        }).execute()
        return created.data[0] if created.data else None
    except Exception:
        return None


def is_configured() -> bool:
    return bool(os.getenv("SUPABASE_URL") and os.getenv("SUPABASE_ANON_KEY"))


# ---------------------------------------------------------------------------
# OAuth — Google sign-in via Supabase PKCE flow
# ---------------------------------------------------------------------------

def _pkce_pair() -> tuple[str, str]:
    """Return (code_verifier, code_challenge) for PKCE S256."""
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).rstrip(b"=").decode()
    return verifier, challenge


def get_google_oauth_url(app_url: str) -> tuple[str, str] | tuple[None, None]:
    """
    Build the Supabase Google OAuth redirect URL using PKCE.
    Returns (oauth_url, code_verifier). Store code_verifier in a short-lived cookie.
    """
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")
    if not url or not key:
        return None, None

    verifier, challenge = _pkce_pair()
    callback = f"{app_url.rstrip('/')}/auth/callback"
    oauth_url = (
        f"{url}/auth/v1/authorize"
        f"?provider=google"
        f"&redirect_to={callback}"
        f"&code_challenge={challenge}"
        f"&code_challenge_method=s256"
    )
    return oauth_url, verifier


def exchange_pkce_code(code: str, code_verifier: str) -> dict | None:
    """
    Exchange the PKCE auth code for a Supabase session.
    Returns the session dict with access_token, refresh_token, and user.
    """
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")
    if not url or not key:
        return None

    try:
        resp = httpx.post(
            f"{url}/auth/v1/token?grant_type=pkce",
            json={"auth_code": code, "code_verifier": code_verifier},
            headers={
                "apikey": key,
                "Content-Type": "application/json",
            },
            timeout=10.0,
        )
        resp.raise_for_status()
        return _sanitize(resp.json())
    except Exception:
        return None


def get_user_from_token(access_token: str) -> dict | None:
    """Verify an access token and return the Supabase user dict."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")
    if not url or not key or not access_token:
        return None
    try:
        resp = httpx.get(
            f"{url}/auth/v1/user",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {access_token}",
            },
            timeout=8.0,
        )
        if resp.status_code == 200:
            return _sanitize(resp.json())
        return None
    except Exception:
        return None
