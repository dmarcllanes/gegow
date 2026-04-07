// ── Service Worker registration + PWA install prompt ─────────

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/sw.js', { scope: '/' })
      .then((reg) => {
        console.log('[Gegow SW] Registered, scope:', reg.scope);
        setInterval(() => reg.update(), 60000);
      })
      .catch((err) => {
        console.warn('[Gegow SW] Registration failed:', err);
      });
  });
}

// ── beforeinstallprompt — single global handler ───────────────
let _installPrompt = null;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  _installPrompt = e;

  // Show any element with data-pwa-install attribute
  document.querySelectorAll('[data-pwa-install]').forEach((el) => {
    el.style.display = '';
  });

  // Dispatch a custom event so any page can react
  window.dispatchEvent(new CustomEvent('pwa-install-ready'));

  console.log('[Gegow PWA] Install prompt ready.');
});

// ── Global install trigger (call from any page/button) ────────
// onAccepted(outcome) — optional callback with 'accepted'|'dismissed'
window.triggerPWAInstall = function (onAccepted) {
  if (!_installPrompt) return false;
  _installPrompt.prompt();
  _installPrompt.userChoice.then((result) => {
    console.log('[Gegow PWA] User choice:', result.outcome);
    _installPrompt = null;
    document.querySelectorAll('[data-pwa-install]').forEach((el) => {
      el.style.display = 'none';
    });
    if (typeof onAccepted === 'function') onAccepted(result.outcome);
  });
  return true;
};

// Check if a native install prompt is available
window.hasPWAPrompt = function () { return _installPrompt !== null; };

// ── appinstalled ──────────────────────────────────────────────
window.addEventListener('appinstalled', () => {
  console.log('[Gegow PWA] App installed successfully.');
  _installPrompt = null;
  window.dispatchEvent(new CustomEvent('pwa-installed'));
});
