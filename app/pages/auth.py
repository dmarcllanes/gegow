"""
Gegow — Login page. Aligned to tropical island light-mode theme.
"""

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Style, Script,
    Div, A, Span, P, H1, Button, NotStr,
)

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing:antialiased;overflow:hidden}
a{text-decoration:none;color:inherit}

/* ── Tropical daytime sky — mirrors landing hero ── */
.login-page{
  min-height:100dvh;
  display:flex;align-items:center;justify-content:center;
  position:relative;overflow:hidden;
  background:linear-gradient(
    to bottom,
    #0A2A4A 0%,
    #0E4060 15%,
    #1A6080 30%,
    #3D9AB8 48%,
    #7AC8DC 62%,
    #A8E0E8 72%,
    #C8EEF3 80%,
    #8EC8D8 90%,
    #4A9AB5 100%
  );
  padding:20px;
}

/* Sun glow */
.lp-orb{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none}
.lp-orb-1{
  width:320px;height:320px;
  background:radial-gradient(circle,rgba(255,245,180,.52) 0%,rgba(200,235,255,.22) 50%,transparent 72%);
  top:6%;right:8%;
  animation:sunPulse 8s ease-in-out infinite alternate;
}
.lp-orb-2,.lp-orb-3{display:none}
@keyframes sunPulse{
  0%{opacity:.8;transform:scale(1)}
  100%{opacity:1;transform:scale(1.08)}
}

/* Subtle stars in upper sky */
.lp-grid{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background-image:
    radial-gradient(circle,rgba(255,255,255,.8) 1px,transparent 1px),
    radial-gradient(circle,rgba(255,255,255,.5) 1px,transparent 1px);
  background-size:260px 180px,140px 130px;
  background-position:18px 22px,80px 55px;
  opacity:.07;
  mask-image:linear-gradient(to bottom,black 0%,black 32%,transparent 52%);
  -webkit-mask-image:linear-gradient(to bottom,black 0%,black 32%,transparent 52%);
}

/* ── Island silhouette layers ── */
.lp-sil-far{
  position:absolute;bottom:0;left:0;right:0;height:40%;
  z-index:1;pointer-events:none;
  background:linear-gradient(to bottom,rgba(20,80,120,.2),rgba(10,50,90,.42));
  clip-path:polygon(
    0% 100%,0% 44%,4% 34%,9% 41%,14% 25%,20% 33%,26% 17%,32% 27%,
    38% 12%,44% 22%,51% 8%,57% 18%,63% 5%,69% 14%,75% 9%,82% 18%,
    88% 4%,94% 13%,100% 8%,100% 100%
  );
}
.lp-sil-mid{
  position:absolute;bottom:0;left:0;right:0;height:32%;
  z-index:2;pointer-events:none;
  background:linear-gradient(to bottom,rgba(10,55,88,.46),rgba(5,32,62,.76));
  clip-path:polygon(
    0% 100%,0% 56%,4% 46%,9% 53%,14% 38%,20% 47%,26% 31%,32% 41%,
    38% 25%,44% 35%,50% 20%,56% 30%,62% 15%,68% 25%,74% 19%,80% 29%,
    86% 23%,92% 31%,97% 25%,100% 28%,100% 100%
  );
}
.lp-sil-near{
  position:absolute;bottom:0;left:0;right:0;height:24%;
  z-index:3;pointer-events:none;
  background:linear-gradient(to bottom,rgba(4,18,38,.84),rgba(2,10,22,.96));
  clip-path:polygon(
    0% 100%,0% 68%,3% 57%,7% 66%,11% 49%,16% 59%,21% 43%,27% 55%,
    33% 38%,39% 50%,45% 34%,51% 46%,57% 32%,63% 44%,69% 36%,75% 48%,
    81% 40%,87% 50%,93% 43%,100% 48%,100% 100%
  );
}
.lp-sil-ocean{
  position:absolute;bottom:0;left:0;right:0;height:13%;
  z-index:4;pointer-events:none;
  background:linear-gradient(to bottom,rgba(20,130,175,.8),rgba(8,88,130,.96));
}
.lp-sil-ocean::after{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent 5%,rgba(255,255,220,.35) 28%,rgba(255,255,255,.65) 50%,rgba(255,255,220,.35) 72%,transparent 95%);
  animation:waterShimmer 4s ease-in-out infinite;
}
@keyframes waterShimmer{
  0%,100%{opacity:.5;transform:scaleX(.85)}
  50%{opacity:1;transform:scaleX(1.08)}
}
.lp-sil-mist{
  position:absolute;bottom:11%;left:0;right:0;height:6%;
  z-index:4;pointer-events:none;
  background:linear-gradient(to bottom,transparent,rgba(200,240,255,.07),transparent);
  filter:blur(12px);
}

/* Palm tree silhouettes */
.lp-palm-l{
  position:absolute;bottom:12%;left:-1%;
  width:15%;max-width:180px;height:52%;
  z-index:5;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;background-repeat:no-repeat;background-position:bottom left;
}
.lp-palm-r{
  position:absolute;bottom:10%;right:-1%;
  width:12%;max-width:148px;height:45%;
  z-index:5;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 110 250'%3E%3Cpath fill='%23030c1c' d='M55 250 C53 214 50 176 53 146 C55 130 60 114 55 98 C38 84 18 91 5 79 C20 75 44 88 54 95 C53 87 54 78 56 70 C70 51 90 36 103 32 C94 48 73 62 57 76 C56 66 59 54 65 38 C60 54 55 70 55 81 C67 69 80 73 93 81 C84 85 65 88 56 97 C63 89 76 93 85 100 C76 100 62 98 56 105 C52 123 50 148 49 174 C47 200 49 226 53 250 Z'/%3E%3C/svg%3E");
  background-size:contain;background-repeat:no-repeat;background-position:bottom right;
  transform:scaleX(-1);
}

/* ── Login card: light glassmorphism ── */
.login-card{
  position:relative;z-index:6;
  width:100%;max-width:420px;
  background:rgba(255,255,255,.90);
  border:1px solid rgba(0,140,153,.18);
  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border-radius:28px;
  padding:40px 36px 36px;
  box-shadow:
    0 24px 60px rgba(0,0,0,.2),
    0 0 0 1px rgba(0,140,153,.1),
    inset 0 1px 0 rgba(255,255,255,.8);
  animation:cardUp .65s cubic-bezier(.4,0,.2,1) both;
  display:flex;flex-direction:column;align-items:center;
  text-align:center;
}
@media(max-width:480px){.login-card{padding:32px 24px 28px;border-radius:22px}}
@keyframes cardUp{
  from{opacity:0;transform:translateY(28px)}
  to{opacity:1;transform:translateY(0)}
}

/* Back link */
.lp-back{
  position:absolute;top:20px;left:20px;z-index:7;
  display:inline-flex;align-items:center;gap:6px;
  font-size:13px;font-weight:600;color:#0A1D20;
  padding:7px 14px;border-radius:10px;
  background:rgba(255,255,255,.82);border:1px solid rgba(0,140,153,.2);
  transition:all .18s;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
}
.lp-back:hover{
  background:rgba(255,255,255,.96);
  border-color:rgba(0,140,153,.42);
  color:#006D77;
  transform:translateX(-2px);
}

/* Brand */
.login-brand{
  display:flex;flex-direction:column;align-items:center;gap:10px;
  margin-bottom:28px;
}
.login-logo-icon{
  width:56px;height:56px;border-radius:16px;
  background:linear-gradient(135deg,#006D77,#005060);
  display:flex;align-items:center;justify-content:center;
  font-size:26px;
  box-shadow:0 0 28px rgba(0,140,153,.35),0 6px 18px rgba(0,0,0,.14);
}
.login-brand-name{
  font-size:22px;font-weight:900;color:#0A1D20;letter-spacing:-.4px;
}
.login-brand-sub{font-size:11px;color:#4A7070;margin-top:-4px}
.login-divider-line{
  width:40px;height:2px;border-radius:2px;
  background:linear-gradient(90deg,#006D77,rgba(0,109,119,.15));
  margin:4px auto 0;
}

/* Headline */
.login-title{
  font-size:22px;font-weight:900;color:#0A1D20;
  letter-spacing:-.3px;margin-bottom:8px;line-height:1.2;
}
.login-sub{
  font-size:13px;color:#4A7070;
  line-height:1.65;margin-bottom:28px;max-width:280px;
}

/* Destination pills */
.login-dest-pills{
  display:flex;gap:8px;flex-wrap:wrap;justify-content:center;
  margin-bottom:28px;
}
.login-dest-pill{
  font-size:11px;font-weight:600;color:#006D77;
  background:rgba(0,140,153,.08);
  border:1px solid rgba(0,140,153,.2);
  border-radius:20px;padding:4px 12px;
  transition:all .15s;
}
.login-dest-pill:hover{background:rgba(0,140,153,.15);border-color:rgba(0,140,153,.35)}

/* Warning box */
.warn-box{
  width:100%;padding:12px 14px;border-radius:12px;margin-bottom:20px;
  background:rgba(250,200,60,.08);border:1px solid rgba(250,180,40,.35);
  font-size:12px;color:#7A5500;text-align:left;line-height:1.55;
}

/* Google button */
.btn-google{
  display:flex;align-items:center;justify-content:center;gap:12px;
  width:100%;padding:15px 20px;border-radius:14px;
  background:#fff;border:1.5px solid rgba(0,140,153,.18);
  font-size:15px;font-weight:700;color:#1f2937;
  box-shadow:0 2px 12px rgba(0,0,0,.09),0 1px 0 rgba(0,0,0,.04);
  transition:all .2s;cursor:pointer;min-height:54px;
}
.btn-google:hover{
  transform:translateY(-2px);
  box-shadow:0 6px 24px rgba(0,140,153,.2),0 2px 8px rgba(0,0,0,.07);
  border-color:rgba(0,140,153,.38);
  background:#f5fffe;
}
.btn-google:active{transform:scale(.97)}
.btn-google svg{width:20px;height:20px;flex-shrink:0}

/* OR divider */
.login-or{
  display:flex;align-items:center;gap:12px;
  width:100%;margin:22px 0;
  font-size:11px;color:#4A7070;font-weight:600;letter-spacing:.5px;
}
.login-or::before,.login-or::after{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,140,153,.22),transparent);
}

/* Trust chips */
.login-trust{
  display:flex;gap:8px;justify-content:center;flex-wrap:wrap;
  margin-top:24px;
}
.login-trust-chip{
  display:flex;align-items:center;gap:5px;
  font-size:11px;font-weight:600;color:#4A7070;
}

/* Terms */
.login-terms{
  margin-top:20px;font-size:11px;color:#4A7070;line-height:1.6;
}
.login-terms a{color:#006D77;text-decoration:underline;transition:color .15s}
.login-terms a:hover{color:#005060}

/* Sign-up nudge */
.login-signup{
  margin-top:16px;font-size:13px;color:#4A7070;
}
.login-signup a{color:#006D77;font-weight:700;transition:color .15s}
.login-signup a:hover{color:#005060}
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
            Meta(name="theme-color", content="#1A6080"),
            Style(CSS),
        ),
        Body(
            Div(
                # Sky layers
                Div(cls="lp-grid"),
                Div(cls="lp-orb lp-orb-1"),
                Div(cls="lp-orb lp-orb-2"),
                Div(cls="lp-orb lp-orb-3"),

                # Island silhouettes
                Div(cls="lp-sil-far"),
                Div(cls="lp-sil-mid"),
                Div(cls="lp-sil-near"),
                Div(cls="lp-sil-ocean"),
                Div(cls="lp-sil-mist"),
                Div(cls="lp-palm-l"),
                Div(cls="lp-palm-r"),

                # Back link
                A("← Back to Gegow", href="/", cls="lp-back"),

                # Glass card
                Div(
                    # Brand
                    Div(
                        Div("✈", cls="login-logo-icon"),
                        Div("Gegow", cls="login-brand-name"),
                        Div("Digital Travel Agency", cls="login-brand-sub"),
                        Div(cls="login-divider-line"),
                        cls="login-brand",
                    ),

                    # Headline
                    H1("Welcome back", cls="login-title"),
                    P("Sign in to access your trips, bookings, and suitcase.", cls="login-sub"),

                    # Destination pills
                    Div(
                        Span("🇵🇭 Palawan",   cls="login-dest-pill"),
                        Span("🇯🇵 Tokyo",     cls="login-dest-pill"),
                        Span("🇸🇬 Singapore", cls="login-dest-pill"),
                        Span("🏄 Siargao",    cls="login-dest-pill"),
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
                        Span("🔒  Secure login",        cls="login-trust-chip"),
                        Span("·", style="color:rgba(0,0,0,.15)"),
                        Span("✅  No password needed",  cls="login-trust-chip"),
                        Span("·", style="color:rgba(0,0,0,.15)"),
                        Span("⚡  Instant access",      cls="login-trust-chip"),
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
