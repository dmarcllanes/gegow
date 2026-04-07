// ── Service Worker registration + PWA install prompt ─────────

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/sw.js', { scope: '/' })
      .then((reg) => {
        console.log('[Gegow SW] Registered, scope:', reg.scope);

        // Check for updates every 60s while app is open
        setInterval(() => reg.update(), 60000);
      })
      .catch((err) => {
        console.warn('[Gegow SW] Registration failed:', err);
      });
  });
}

// ── beforeinstallprompt — capture & expose install trigger ───
let _installPrompt = null;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  _installPrompt = e;

  // Show any install button/banner that has data-pwa-install
  document.querySelectorAll('[data-pwa-install]').forEach((el) => {
    el.style.display = '';
  });

  console.log('[Gegow PWA] Install prompt ready.');
});

// Call this from any "Install App" button
window.triggerPWAInstall = function () {
  if (!_installPrompt) return;
  _installPrompt.prompt();
  _installPrompt.userChoice.then((result) => {
    console.log('[Gegow PWA] User choice:', result.outcome);
    _installPrompt = null;
    // Hide install buttons after choice
    document.querySelectorAll('[data-pwa-install]').forEach((el) => {
      el.style.display = 'none';
    });
  });
};

// ── appinstalled event ────────────────────────────────────────
window.addEventListener('appinstalled', () => {
  console.log('[Gegow PWA] App installed successfully.');
  _installPrompt = null;
});
