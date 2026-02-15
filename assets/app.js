(function () {
  function byId(id) { return document.getElementById(id); }

  // Print
  var printBtn = byId("printBtn");
  if (printBtn) {
    printBtn.addEventListener("click", function () { window.print(); });
  }

  // Language toggle: mirrors the same path under /en
  var langBtn = byId("langToggle");
  if (langBtn) {
    langBtn.addEventListener("click", function () {
      var p = window.location.pathname || "/";
      // Normalize: / -> /index.html (for predictable mapping)
      if (p === "/") p = "/index.html";
      if (p.startsWith("/en/")) {
        var tr = p.replace(/^\/en/, "");
        window.location.pathname = tr;
      } else {
        window.location.pathname = ("/en" + p).replace(/\/{2,}/g, "/");
      }
    });
  }

  // Search filter (cards with data-filter-text)
  var search = byId("searchInput");
  if (search) {
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-filter-text]"));
    var apply = function () {
      var q = (search.value || "").trim().toLowerCase();
      cards.forEach(function (el) {
        var hay = (el.getAttribute("data-filter-text") || "").toLowerCase();
        el.style.display = (!q || hay.indexOf(q) !== -1) ? "" : "none";
      });
    };
    search.addEventListener("input", apply);
    apply();
  }

  
  // Tabs (hazard pages)
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".tabs"));
  if (tabs.length) {
    tabs.forEach(function (wrap) {
      var buttons = Array.prototype.slice.call(wrap.querySelectorAll("[data-tab-target]"));
      var panels = Array.prototype.slice.call(document.querySelectorAll("[data-tab-panel]"));
      var activate = function (key) {
        buttons.forEach(function (b) { b.classList.toggle("active", b.getAttribute("data-tab-target") === key); });
        panels.forEach(function (p) { p.classList.toggle("active", p.getAttribute("data-tab-panel") === key); });
      };
      buttons.forEach(function (b) {
        b.addEventListener("click", function () { activate(b.getAttribute("data-tab-target")); });
      });
      // default: first active button
      var first = buttons.find(function (b) { return b.classList.contains("active"); }) || buttons[0];
      if (first) activate(first.getAttribute("data-tab-target"));
    });
  }

// Checklist persistence
  var checks = Array.prototype.slice.call(document.querySelectorAll('input[type="checkbox"][data-check-id]'));
  if (checks.length) {
    var storageKey = "afo:checks:" + (window.location.pathname || "/");
    var state = {};
    try { state = JSON.parse(localStorage.getItem(storageKey) || "{}"); } catch (e) { state = {}; }

    var updateProgress = function () {
      var total = checks.length;
      var done = checks.filter(function (c) { return c.checked; }).length;
      var el = document.querySelector("[data-progress]");
      if (!el) return;
      el.textContent = (done + " / " + total) + " " + (document.documentElement.lang === "tr" ? "tamamlandı" : "completed");
    };

    checks.forEach(function (cb) {
      var id = cb.getAttribute("data-check-id");
      cb.checked = !!state[id];
      cb.addEventListener("change", function () {
        state[id] = cb.checked;
        try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (e) {}
        updateProgress();
      });
    });
    updateProgress();

    var reset = document.querySelector("[data-reset-checks]");
    if (reset) {
      reset.addEventListener("click", function () {
        try { localStorage.removeItem(storageKey); } catch (e) {}
        window.location.reload();
      });
    }
  }
})();
