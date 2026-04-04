"""
Auth callback error page — shown only when OAuth exchange fails.
"""

from fasthtml.common import Html, Head, Body, Title, Meta, Style, Div, H2, P, A, Span

_CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, 'Segoe UI', Inter, system-ui, sans-serif;
  background: #0a0a0f; color: #e8e8f0;
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  -webkit-font-smoothing: antialiased;
}
.card {
  background: #18181f; border: 1px solid rgba(255,255,255,.08);
  border-radius: 20px; padding: 48px 40px; text-align: center;
  max-width: 420px; width: 100%;
}
.icon { font-size: 48px; margin-bottom: 20px; }
h2   { font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 10px; }
p    { font-size: 14px; color: #8888a0; line-height: 1.65; margin-bottom: 28px; }
.btn {
  display: inline-block; padding: 12px 28px; border-radius: 10px;
  background: linear-gradient(135deg, #006D77, #0D9488);
  color: #fff; font-size: 14px; font-weight: 700;
  box-shadow: 0 4px 16px rgba(0,109,119,.35);
}
.err { font-size: 12px; color: #f87171; margin-top: 16px; opacity: .8; }
"""


def error_page(reason: str = "") -> Html:
    return Html(
        Head(
            Title("Sign-in failed — Gegow"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style(_CSS),
        ),
        Body(
            Div(
                Div("⚠️", cls="icon"),
                H2("Sign-in failed"),
                P("Something went wrong while connecting your Google account. "
                  "Please try again — if the problem persists, contact support."),
                A("← Back to login", href="/login", cls="btn"),
                Div(reason, cls="err") if reason else Span(),
                cls="card",
            ),
        ),
    )
