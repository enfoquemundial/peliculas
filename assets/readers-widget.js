(function () {
  var scriptTag = document.currentScript;
  var DATA_URL = (scriptTag && scriptTag.getAttribute("data-src")) || "/data/readers.json";
  var REFRESH_MS = parseInt((scriptTag && scriptTag.getAttribute("data-refresh")) || "30000", 10);
  var TARGET_ID = (scriptTag && scriptTag.getAttribute("data-target")) || "aw-readers";

  function flagEmoji(cc) {
    if (!cc || cc.length !== 2) return "🏳️";
    var A = 0x1f1e6;
    var chars = cc.toUpperCase().split("");
    return chars.map(function (c) {
      return String.fromCodePoint(A + (c.charCodeAt(0) - 65));
    }).join("");
  }

  function sourceLabel(referrer, refClass) {
    var r = (referrer || "").toLowerCase();
    if (!r) return "DIRECTO";
    if (r.indexOf("facebook") !== -1 || r.indexOf("fb.me") !== -1) return "FACEBOOK";
    if (r.indexOf("instagram") !== -1) return "INSTAGRAM";
    if (r.indexOf("tiktok") !== -1) return "TIKTOK";
    if (r.indexOf("youtube") !== -1 || r.indexOf("youtu.be") !== -1) return "YOUTUBE";
    if (r.indexOf("t.co") !== -1 || r.indexOf("twitter") !== -1 || r.indexOf("x.com") !== -1) return "X (TWITTER)";
    if (r.indexOf("google") !== -1) return "GOOGLE";
    if (r.indexOf("whatsapp") !== -1) return "WHATSAPP";
    if (refClass && refClass.toLowerCase() === "search") return "BÚSQUEDA";
    return r.replace(/^www\./, "").toUpperCase();
  }

  function deviceIcon(row) {
    var os = (row.os || "").toLowerCase();
    if (os.indexOf("android") !== -1) return "🤖";
    if (os.indexOf("ios") !== -1 || os.indexOf("iphone") !== -1 || os.indexOf("ipad") !== -1 || os.indexOf("mac") !== -1) return "🍎";
    if (!row.desktop) return "📱";
    return "🖥️";
  }

  function placeLabel(row) {
    var parts = [];
    if (row.city) parts.push(row.city);
    if (row.country) parts.push(row.country);
    return parts.length ? parts.join(", ") : "Ubicación desconocida";
  }

  function timeAgo(fetchedAtIso) {
    var diffSec = Math.max(0, Math.round((Date.now() - new Date(fetchedAtIso).getTime()) / 1000));
    var m = Math.floor(diffSec / 60);
    var s = diffSec % 60;
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function render(container, data) {
    container.innerHTML = "";
    container.className = "aw-readers";

    var header = document.createElement("div");
    header.className = "aw-readers__header";
    header.innerHTML = '<span>Lectores</span><span class="aw-readers__count">' + (data.count || 0) + "</span>";
    container.appendChild(header);

    var rows = data.rows || [];
    if (!rows.length) {
      var empty = document.createElement("div");
      empty.className = "aw-readers__empty";
      empty.textContent = "Sin visitantes en este momento.";
      container.appendChild(empty);
      return;
    }

    rows.forEach(function (row) {
      var el = document.createElement("div");
      el.className = "aw-readers__row";
      el.innerHTML =
        '<span class="aw-readers__time">' + timeAgo(data.fetched_at) + "</span>" +
        '<span class="aw-readers__meta">' +
        '<span class="aw-readers__source">' + sourceLabel(row.referrer, row.ref_class) + "</span>" +
        '<span class="aw-readers__place"><span class="aw-readers__flag">' + flagEmoji(row.country_code) + "</span>" + placeLabel(row) + "</span>" +
        "</span>" +
        '<span class="aw-readers__device">' + deviceIcon(row) + "</span>";
      container.appendChild(el);
    });
  }

  function load() {
    var container = document.getElementById(TARGET_ID);
    if (!container) return;
    fetch(DATA_URL, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) { render(container, data); })
      .catch(function (err) { console.error("[readers-widget] failed to load data:", err); });
  }

  load();
  setInterval(load, REFRESH_MS);
})();
