"""Gegow — OAuth error page (pages folder)."""

from fasthtml.common import Html, Head, Body, Title, Meta, Style, Div, H2, P, A, Span

_CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #f9fafb; color: #111827; min-height: 100dvh;
  display: flex; align-items: center; justify-content: center;
  -webkit-font-smoothing: antialiased; padding: 20px;
}
.card {
  background: #fff; border: 1.5px solid #e5e7eb; border-radius: 20px;
  padding: 40px 32px; text-align: center; max-width: 400px; width: 100%;
  box-shadow: 0 4px 24px rgba(0,0,0,.06);
}
.icon { font-size: 44px; margin-bottom: 18px; }
h2   { font-size: 20px; font-weight: 800; color: #111827; margin-bottom: 8px; }
p    { font-size: 14px; color: #6b7280; line-height: 1.65; margin-bottom: 24px; }
.btn {
  display: inline-block; padding: 12px 28px; border-radius: 10px;
  background: #006D77; color: #fff; font-size: 14px; font-weight: 700;
  box-shadow: 0 4px 14px rgba(0,109,119,.3); transition: background .15s;
}
.btn:hover { background: #005760; }
.err { font-size: 11px; color: #ef4444; margin-top: 14px; opacity: .8; }
"""


def error_page(reason: str = "") -> Html:
    return Html(
        Head(
            Title("Sign-in failed · Gegow"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width,initial-scale=1"),
            Style(_CSS),
        ),
        Body(
            Div(
                Div("⚠️", cls="icon"),
                H2("Sign-in failed"),
                P("Something went wrong connecting your Google account. Please try again."),
                A("← Back to login", href="/login", cls="btn"),
                Div(reason, cls="err") if reason else Span(),
                cls="card",
            ),
        ),
    )
