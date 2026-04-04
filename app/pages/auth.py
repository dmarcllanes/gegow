"""
Gegow — Login page. Styled to match landing page aesthetic.
"""

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Style, Script,
    Div, A, Span, P, H1, H2, Button, NotStr,
)

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing:antialiased;overflow:hidden}
a{text-decoration:none;color:inherit}

/* ── Full-page dark background (mirrors landing hero) ─────── */
.login-page{
  min-height:100dvh;
  display:flex;align-items:center;justify-content:center;
  position:relative;overflow:hidden;
  background:#04111a;
  padding:20px;
}

/* Mesh gradient bg */
.lp-bg{
  position:absolute;inset:0;z-index:0;
  background:
    radial-gradient(ellipse 80% 70% at 20% 40%,rgba(0,201,177,.18) 0%,transparent 60%),
    radial-gradient(ellipse 60% 60% at 80% 60%,rgba(255,107,53,.13) 0%,transparent 55%),
    radial-gradient(ellipse 100% 80% at 50% 100%,rgba(0,150,200,.12) 0%,transparent 60%),
    #04111a;
  animation:meshShift 14s ease-in-out infinite alternate;
}
@keyframes meshShift{
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}

/* Grid overlay */
.lp-grid{
  position:absolute;inset:0;z-index:1;
  background-image:
    linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);
  background-size:60px 60px;
  mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 30%,transparent 100%);
}

/* Floating orbs */
.lp-orb{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none}
.lp-orb-1{width:500px;height:500px;background:rgba(0,201,177,.12);top:-15%;left:-10%;
  animation:orbFloat 10s ease-in-out infinite alternate}
.lp-orb-2{width:400px;height:400px;background:rgba(255,107,53,.1);bottom:5%;right:-8%;
  animation:orbFloat 14s ease-in-out infinite alternate;animation-delay:-4s}
.lp-orb-3{width:280px;height:280px;background:rgba(0,150,200,.1);top:45%;left:55%;
  animation:orbFloat 12s ease-in-out infinite alternate;animation-delay:-2s}
@keyframes orbFloat{
  0%{transform:translate(0,0) scale(1)}
  50%{transform:translate(30px,-20px) scale(1.05)}
  100%{transform:translate(-20px,30px) scale(.95)}
}

/* ── Glassmorphism card ───────────────────────────────────── */
.login-card{
  position:relative;z-index:2;
  width:100%;max-width:420px;
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.1);
  backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);
  border-radius:28px;
  padding:40px 36px 36px;
  box-shadow:0 32px 80px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.08);
  animation:cardUp .7s cubic-bezier(.4,0,.2,1) both;
  display:flex;flex-direction:column;align-items:center;
  text-align:center;
}
@media(max-width:480px){.login-card{padding:32px 24px 28px;border-radius:22px}}
@keyframes cardUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* Back link — top-left corner */
.lp-back{
  position:absolute;top:20px;left:20px;z-index:3;
  display:inline-flex;align-items:center;gap:6px;
  font-size:13px;font-weight:600;color:rgba(255,255,255,.5);
  padding:7px 14px;border-radius:10px;
  background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);
  transition:all .18s;backdrop-filter:blur(8px);
}
.lp-back:hover{color:#fff;background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.2)}

/* Brand mark */
.login-brand{
  display:flex;flex-direction:column;align-items:center;gap:10px;
  margin-bottom:28px;
}
.login-logo-icon{
  width:56px;height:56px;border-radius:16px;
  background:linear-gradient(135deg,#00C9B1,#009e8c);
  display:flex;align-items:center;justify-content:center;
  font-size:26px;
  box-shadow:0 0 32px rgba(0,201,177,.4),0 8px 24px rgba(0,0,0,.3);
}
.login-brand-name{
  font-size:22px;font-weight:900;color:#fff;letter-spacing:-.4px;
}
.login-brand-sub{font-size:11px;color:rgba(255,255,255,.45);margin-top:-4px}

/* Divider line in brand */
.login-divider-line{
  width:40px;height:2px;border-radius:2px;
  background:linear-gradient(90deg,#00C9B1,transparent);
  margin:4px auto 0;
}

/* Headline */
.login-title{
  font-size:22px;font-weight:900;color:#fff;
  letter-spacing:-.3px;margin-bottom:8px;line-height:1.2;
}
.login-sub{
  font-size:13px;color:rgba(255,255,255,.5);
  line-height:1.65;margin-bottom:32px;max-width:280px;
}

/* Destination pills row */
.login-dest-pills{
  display:flex;gap:8px;flex-wrap:wrap;justify-content:center;
  margin-bottom:28px;
}
.login-dest-pill{
  font-size:11px;font-weight:600;color:rgba(255,255,255,.6);
  background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.1);
  border-radius:20px;padding:4px 12px;
}

/* Warning box */
.warn-box{
  width:100%;padding:12px 14px;border-radius:12px;margin-bottom:20px;
  background:rgba(250,200,60,.08);border:1px solid rgba(250,200,60,.25);
  font-size:12px;color:rgba(250,200,150,.85);text-align:left;line-height:1.55;
}

/* Google button */
.btn-google{
  display:flex;align-items:center;justify-content:center;gap:12px;
  width:100%;padding:15px 20px;border-radius:14px;
  background:#fff;border:none;
  font-size:15px;font-weight:700;color:#1f2937;
  box-shadow:0 4px 20px rgba(0,0,0,.25),0 1px 0 rgba(0,0,0,.05);
  transition:all .2s;cursor:pointer;min-height:54px;
}
.btn-google:hover{
  transform:translateY(-2px);
  box-shadow:0 8px 32px rgba(0,0,0,.35);
  background:#f9fafb;
}
.btn-google:active{transform:scale(.97)}
.btn-google svg{width:20px;height:20px;flex-shrink:0}

/* OR divider */
.login-or{
  display:flex;align-items:center;gap:12px;
  width:100%;margin:22px 0;
  font-size:11px;color:rgba(255,255,255,.25);font-weight:600;letter-spacing:.5px;
}
.login-or::before,.login-or::after{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.1),transparent);
}

/* Trust chips */
.login-trust{
  display:flex;gap:8px;justify-content:center;flex-wrap:wrap;
  margin-top:24px;
}
.login-trust-chip{
  display:flex;align-items:center;gap:5px;
  font-size:11px;font-weight:600;color:rgba(255,255,255,.4);
}

/* Terms */
.login-terms{
  margin-top:20px;font-size:11px;color:rgba(255,255,255,.25);line-height:1.6;
}
.login-terms a{color:rgba(255,255,255,.4);text-decoration:underline;transition:color .15s}
.login-terms a:hover{color:rgba(255,255,255,.7)}

/* Sign-up nudge */
.login-signup{
  margin-top:16px;font-size:13px;color:rgba(255,255,255,.4);
}
.login-signup a{
  color:#00C9B1;font-weight:700;transition:color .15s;
}
.login-signup a:hover{color:#00e8cc}
"""

_GOOGLE_SVG = """<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
<path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
<path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
</svg>"""


def login_page(supabase_ok: bool = True) -> Html:
    return Html(
        Head(
            Title("Sign in · Gegow"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width,initial-scale=1,viewport-fit=cover"),
            Meta(name="theme-color", content="#04111a"),
            Style(CSS),
        ),
        Body(
            Div(
                # Background layers
                Div(cls="lp-bg"),
                Div(cls="lp-grid"),
                Div(cls="lp-orb lp-orb-1"),
                Div(cls="lp-orb lp-orb-2"),
                Div(cls="lp-orb lp-orb-3"),

                # Back link
                A("← Back to Gegow", href="/", cls="lp-back"),

                # Glass card
                Div(
                    # Brand
                    Div(
                        Div("✈", cls="login-logo-icon"),
                        Div("Gegow", cls="login-brand-name"),
                        Div("Digital Travel Agency", cls="login-brand-sub"),
                        cls="login-brand",
                    ),

                    # Headline
                    H1("Welcome back", cls="login-title"),
                    P("Sign in to access your trips, bookings, and suitcase.", cls="login-sub"),

                    # Destination pills
                    Div(
                        Span("🇵🇭 Palawan", cls="login-dest-pill"),
                        Span("🇯🇵 Tokyo", cls="login-dest-pill"),
                        Span("🇸🇬 Singapore", cls="login-dest-pill"),
                        Span("🏄 Siargao", cls="login-dest-pill"),
                        cls="login-dest-pills",
                    ),

                    # Warning if Supabase not configured
                    *([ Div(
                        "⚠️  Google Sign In is not yet configured. "
                        "Add SUPABASE_URL and SUPABASE_ANON_KEY to your .env file.",
                        cls="warn-box"
                    ) ] if not supabase_ok else []),

                    # Google button
                    A(
                        NotStr(_GOOGLE_SVG),
                        Span("Continue with Google"),
                        href="/auth/google",
                        cls="btn-google",
                    ),

                    # OR divider
                    Div("or", cls="login-or"),

                    # Trust chips
                    Div(
                        Span("🔒  Secure login", cls="login-trust-chip"),
                        Span("·", style="color:rgba(255,255,255,.2)"),
                        Span("✅  No password needed", cls="login-trust-chip"),
                        Span("·", style="color:rgba(255,255,255,.2)"),
                        Span("⚡  Instant access", cls="login-trust-chip"),
                        cls="login-trust",
                    ),

                    # Sign-up nudge
                    P(
                        "New to Gegow? ",
                        A("Create a free account →", href="/auth/google"),
                        cls="login-signup",
                    ),

                    # Terms
                    P(
                        "By continuing you agree to our ",
                        A("Terms of Service", href="#"), " and ",
                        A("Privacy Policy", href="#"), ".",
                        cls="login-terms",
                    ),

                    cls="login-card",
                ),

                cls="login-page",
            ),
        ),
        lang="en",
    )


def signup_page() -> Html:
    return login_page()
