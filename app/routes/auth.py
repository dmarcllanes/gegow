"""
Gegow — Login & Sign-up pages.
Mobile-first, full-screen, PWA-quality auth flow.
"""

from fasthtml.common import (
    Html, Head, Body, Title, Meta, Style, Script,
    Div, Form, Input, Button, Label, A,
    Span, P, H1, H2,
)

# ─────────────────────────────────────────────────────────────
# Shared CSS (login + signup)
# ─────────────────────────────────────────────────────────────
AUTH_CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Inter, sans-serif;
  background: #f8fafc;
  color: #1a1a2e;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100%;
  /* Prevent iOS scroll bounce on auth pages */
  overscroll-behavior: none;
}
a { text-decoration: none; color: inherit; }
/* Prevent 300ms tap delay */
a, button { -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
/* Prevent iOS font size inflate */
input, select, textarea, button { font-family: inherit; font-size: 16px; }

:root {
  --primary:    #006D77;
  --primary-dk: #005760;
  --primary-lt: #e0f2f1;
  --accent:     #FF7043;
  --text:       #1a1a2e;
  --text-2:     #4a5568;
  --text-3:     #94a3b8;
  --border:     #e2e8f0;
  --border-foc: #006D77;
  --bg:         #f8fafc;
  --white:      #ffffff;
  --red:        #ef4444;
  --safe-top:   env(safe-area-inset-top, 0px);
  --safe-bot:   env(safe-area-inset-bottom, 16px);
}

/* ── Page wrapper ─────────────────────────────────────────── */
.auth-page {
  min-height: 100dvh;          /* dynamic viewport height — handles iOS browser chrome */
  display: flex;
  flex-direction: column;
  padding-top: var(--safe-top);
  padding-bottom: var(--safe-bot);
}

/* ── Top bar ──────────────────────────────────────────────── */
.auth-topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 20px 8px;
  flex-shrink: 0;
}
.auth-back {
  display: flex; align-items: center; gap: 4px;
  font-size: 14px; font-weight: 600; color: var(--text-2);
  background: none; border: none; cursor: pointer; padding: 6px 0;
  min-height: 44px;          /* touch target */
}
.auth-skip {
  font-size: 14px; font-weight: 600; color: var(--primary);
  padding: 6px 0; min-height: 44px; display: flex; align-items: center;
}

/* ── Scroll area ──────────────────────────────────────────── */
.auth-scroll {
  flex: 1; overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 0 20px 20px;
  display: flex; flex-direction: column;
}
@media (min-width: 540px) {
  .auth-scroll { align-items: center; justify-content: center; }
}

/* ── Card (wider screens) ─────────────────────────────────── */
.auth-card {
  width: 100%;
}
@media (min-width: 540px) {
  .auth-card {
    max-width: 420px;
    background: var(--white);
    border-radius: 24px;
    padding: 40px 36px;
    box-shadow: 0 8px 40px rgba(0,0,0,.08);
    border: 1px solid var(--border);
  }
}

/* ── Brand header ─────────────────────────────────────────── */
.auth-brand-mark {
  width: 56px; height: 56px; border-radius: 16px;
  background: var(--primary);
  display: flex; align-items: center; justify-content: center;
  font-size: 28px; margin-bottom: 20px;
  box-shadow: 0 4px 16px rgba(0,109,119,.3);
}
.auth-title    { font-size: 24px; font-weight: 900; color: var(--text); letter-spacing: -.4px; margin-bottom: 6px; }
.auth-subtitle { font-size: 14px; color: var(--text-2); line-height: 1.55; margin-bottom: 28px; }

/* ── Google button ────────────────────────────────────────── */
.btn-google {
  width: 100%; display: flex; align-items: center; justify-content: center; gap: 10px;
  padding: 13px 20px; border-radius: 12px;
  background: var(--white); border: 1.5px solid var(--border);
  font-size: 15px; font-weight: 600; color: var(--text);
  cursor: pointer; margin-bottom: 20px; min-height: 50px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
  transition: border-color .15s, box-shadow .15s;
  -webkit-tap-highlight-color: transparent;
}
.btn-google:hover  { border-color: #c0c0c0; box-shadow: 0 2px 8px rgba(0,0,0,.1); }
.btn-google:active { background: #f9f9f9; }
.btn-google svg    { width: 20px; height: 20px; flex-shrink: 0; }

/* ── Divider ─────────────────────────────────────────────── */
.divider {
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 20px; color: var(--text-3); font-size: 12px; font-weight: 500;
}
.divider::before, .divider::after {
  content: ''; flex: 1; height: 1px; background: var(--border);
}

/* ── Form fields ─────────────────────────────────────────── */
.field { margin-bottom: 16px; }
.field-label {
  display: block; font-size: 13px; font-weight: 600; color: var(--text-2);
  margin-bottom: 6px;
}
.field-wrap { position: relative; }
.field-input {
  width: 100%; padding: 13px 16px;
  background: var(--white); border: 1.5px solid var(--border);
  border-radius: 12px; font-size: 16px; color: var(--text);
  outline: none; transition: border-color .15s, box-shadow .15s;
  -webkit-appearance: none; appearance: none;
}
.field-input::placeholder { color: var(--text-3); font-size: 15px; }
.field-input:focus {
  border-color: var(--border-foc);
  box-shadow: 0 0 0 3px rgba(0,109,119,.1);
}
.field-input.has-icon  { padding-left: 44px; }
.field-input.has-right { padding-right: 50px; }
.field-icon {
  position: absolute; left: 14px; top: 50%; transform: translateY(-50%);
  font-size: 16px; pointer-events: none; line-height: 1;
  opacity: .45;
}
.field-right-btn {
  position: absolute; right: 12px; top: 50%; transform: translateY(-50%);
  font-size: 12px; font-weight: 700; color: var(--primary);
  background: none; border: none; cursor: pointer; padding: 4px 6px;
  min-height: 36px;
}

/* two column row */
.field-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }

/* ── Forgot password ─────────────────────────────────────── */
.row-between {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 24px;
}
.check-label {
  display: flex; align-items: center; gap: 8px;
  font-size: 14px; color: var(--text-2); cursor: pointer;
}
.check-label input[type=checkbox] {
  width: 18px; height: 18px; border-radius: 5px;
  accent-color: var(--primary); cursor: pointer; flex-shrink: 0;
}
.link-forgot { font-size: 14px; font-weight: 600; color: var(--primary); }
.link-forgot:hover { color: var(--primary-dk); }

/* ── Submit button ───────────────────────────────────────── */
.btn-submit {
  width: 100%; padding: 15px 20px; border-radius: 12px;
  background: var(--primary); border: none;
  color: #fff; font-size: 16px; font-weight: 700;
  cursor: pointer; min-height: 52px;
  box-shadow: 0 4px 16px rgba(0,109,119,.35);
  transition: background .15s, transform .1s;
  -webkit-tap-highlight-color: transparent;
}
.btn-submit:hover  { background: var(--primary-dk); }
.btn-submit:active { transform: scale(.98); background: var(--primary-dk); }

/* ── Bottom switch ───────────────────────────────────────── */
.auth-switch {
  margin-top: 20px; text-align: center;
  font-size: 14px; color: var(--text-2);
}
.auth-switch a { font-weight: 700; color: var(--primary); }

/* ── Password strength ───────────────────────────────────── */
.pw-meter { display: flex; gap: 4px; margin-top: 8px; }
.pw-bar   {
  flex: 1; height: 3px; border-radius: 2px;
  background: var(--border); transition: background .25s;
}
.pw-bar.weak   { background: #ef4444; }
.pw-bar.fair   { background: #f59e0b; }
.pw-bar.strong { background: #10b981; }
.pw-hint { font-size: 11px; color: var(--text-3); margin-top: 5px; }

/* ── Error banner ────────────────────────────────────────── */
.error-banner {
  display: none; align-items: center; gap: 8px;
  padding: 12px 14px; border-radius: 10px; margin-bottom: 16px;
  background: #fef2f2; border: 1.5px solid #fecaca;
  font-size: 13px; color: #dc2626;
}
.error-banner.show { display: flex; }

/* ── Terms ───────────────────────────────────────────────── */
.auth-terms {
  margin-top: 16px; text-align: center;
  font-size: 11px; color: var(--text-3); line-height: 1.65;
}
.auth-terms a { color: var(--text-2); text-decoration: underline; }
"""

AUTH_JS = """
function togglePw(inputId, btn) {
  const inp = document.getElementById(inputId);
  const show = inp.type === 'password';
  inp.type = show ? 'text' : 'password';
  btn.textContent = show ? 'Hide' : 'Show';
}

document.addEventListener('DOMContentLoaded', () => {
  // Password strength
  const pw = document.getElementById('password');
  if (!pw) return;
  const bars = document.querySelectorAll('.pw-bar');
  const hint = document.querySelector('.pw-hint');
  const levels = ['', 'Weak', 'Fair', 'Good', 'Strong'];
  const colors = ['', 'weak', 'fair', 'strong', 'strong'];
  pw.addEventListener('input', () => {
    const v = pw.value;
    const score = [/.{8,}/, /[A-Z]/, /[0-9]/, /[^A-Za-z0-9]/].filter(r => r.test(v)).length;
    bars.forEach((b, i) => {
      b.className = 'pw-bar';
      if (i < score) b.classList.add(colors[score]);
    });
    if (hint) hint.textContent = v.length ? levels[score] || '' : '';
  });
});
"""


def _google_icon():
    return """<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
  <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
  <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
  <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
</svg>"""


def login_page() -> Html:
    return Html(
        Head(
            Title("Log in · Gegow"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            Meta(name="theme-color", content="#f8fafc"),
            Meta(name="apple-mobile-web-app-capable", content="yes"),
            Style(AUTH_CSS),
        ),
        Body(
            Div(
                # Top bar
                Div(
                    A("← Back", href="/landing", cls="auth-back"),
                    A("Skip", href="/", cls="auth-skip"),
                    cls="auth-topbar",
                ),

                # Scrollable content
                Div(
                    Div(
                        # Brand mark
                        Div("✈", cls="auth-brand-mark"),
                        H1("Welcome back", cls="auth-title"),
                        P("Log in to your Gegow account.", cls="auth-subtitle"),

                        # Error banner
                        Div("⚠️  Incorrect email or password.", cls="error-banner", id="auth-error"),

                        # Google
                        A(
                            Span(_google_icon()),
                            Span("Continue with Google"),
                            href="/auth/google",
                            cls="btn-google",
                        ),

                        Div("or", cls="divider"),

                        # Form
                        Form(
                            Div(
                                Label("Email", cls="field-label", for_="email"),
                                Div(
                                    Span("✉️", cls="field-icon"),
                                    Input(type="email", id="email", name="email",
                                          placeholder="you@example.com",
                                          cls="field-input has-icon",
                                          autocomplete="email", required=True),
                                    cls="field-wrap",
                                ),
                                cls="field",
                            ),
                            Div(
                                Label("Password", cls="field-label", for_="password"),
                                Div(
                                    Span("🔒", cls="field-icon"),
                                    Input(type="password", id="password", name="password",
                                          placeholder="Enter your password",
                                          cls="field-input has-icon has-right",
                                          autocomplete="current-password", required=True),
                                    Button("Show", cls="field-right-btn",
                                           type="button", onclick="togglePw('password',this)"),
                                    cls="field-wrap",
                                ),
                                cls="field",
                            ),
                            Div(
                                Label(
                                    Input(type="checkbox", name="remember"),
                                    Span("Remember me"),
                                    cls="check-label",
                                ),
                                A("Forgot password?", href="#", cls="link-forgot"),
                                cls="row-between",
                            ),
                            Button("Log in", type="submit", cls="btn-submit"),
                            method="post", action="/login",
                        ),

                        P(
                            Span("Don't have an account? "),
                            A("Sign up free", href="/signup"),
                            cls="auth-switch",
                        ),
                        P(
                            Span("By continuing you agree to our "),
                            A("Terms", href="#"),
                            Span(" & "),
                            A("Privacy Policy", href="#"),
                            Span("."),
                            cls="auth-terms",
                        ),
                        cls="auth-card",
                    ),
                    cls="auth-scroll",
                ),

                cls="auth-page",
            ),
            Script(AUTH_JS),
        ),
        lang="en",
    )


def signup_page() -> Html:
    return Html(
        Head(
            Title("Create account · Gegow"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            Meta(name="theme-color", content="#f8fafc"),
            Meta(name="apple-mobile-web-app-capable", content="yes"),
            Style(AUTH_CSS),
        ),
        Body(
            Div(
                # Top bar
                Div(
                    A("← Back", href="/landing", cls="auth-back"),
                    A("Log in", href="/login", cls="auth-skip"),
                    cls="auth-topbar",
                ),

                # Scrollable content
                Div(
                    Div(
                        Div("✈", cls="auth-brand-mark"),
                        H1("Create account", cls="auth-title"),
                        P("Sign up free — no credit card needed.", cls="auth-subtitle"),

                        # Google
                        A(
                            Span(_google_icon()),
                            Span("Sign up with Google"),
                            href="/auth/google",
                            cls="btn-google",
                        ),

                        Div("or sign up with email", cls="divider"),

                        Form(
                            Div(
                                Div(
                                    Label("First name", cls="field-label", for_="first_name"),
                                    Div(
                                        Input(type="text", id="first_name", name="first_name",
                                              placeholder="Juan",
                                              cls="field-input",
                                              autocomplete="given-name", required=True),
                                        cls="field-wrap",
                                    ),
                                    cls="field",
                                ),
                                Div(
                                    Label("Last name", cls="field-label", for_="last_name"),
                                    Div(
                                        Input(type="text", id="last_name", name="last_name",
                                              placeholder="dela Cruz",
                                              cls="field-input",
                                              autocomplete="family-name", required=True),
                                        cls="field-wrap",
                                    ),
                                    cls="field",
                                ),
                                cls="field-row",
                            ),
                            Div(
                                Label("Email address", cls="field-label", for_="email"),
                                Div(
                                    Span("✉️", cls="field-icon"),
                                    Input(type="email", id="email", name="email",
                                          placeholder="you@example.com",
                                          cls="field-input has-icon",
                                          autocomplete="email", required=True),
                                    cls="field-wrap",
                                ),
                                cls="field",
                            ),
                            Div(
                                Label("Password", cls="field-label", for_="password"),
                                Div(
                                    Span("🔒", cls="field-icon"),
                                    Input(type="password", id="password", name="password",
                                          placeholder="Create a strong password",
                                          cls="field-input has-icon has-right",
                                          autocomplete="new-password", required=True),
                                    Button("Show", cls="field-right-btn",
                                           type="button", onclick="togglePw('password',this)"),
                                    cls="field-wrap",
                                ),
                                Div(
                                    Div(cls="pw-bar"), Div(cls="pw-bar"),
                                    Div(cls="pw-bar"), Div(cls="pw-bar"),
                                    cls="pw-meter",
                                ),
                                Span("", cls="pw-hint"),
                                cls="field",
                            ),
                            Button("Create account", type="submit", cls="btn-submit"),
                            method="post", action="/signup",
                        ),

                        P(
                            Span("Already have an account? "),
                            A("Log in", href="/login"),
                            cls="auth-switch",
                        ),
                        P(
                            Span("By signing up you agree to our "),
                            A("Terms", href="#"),
                            Span(" & "),
                            A("Privacy Policy", href="#"),
                            Span("."),
                            cls="auth-terms",
                        ),
                        cls="auth-card",
                    ),
                    cls="auth-scroll",
                ),

                cls="auth-page",
            ),
            Script(AUTH_JS),
        ),
        lang="en",
    )
