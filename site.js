// The footer's year: always the current one.
document.querySelectorAll('[data-year]').forEach(function (el) {
  el.textContent = String(new Date().getFullYear());
});
