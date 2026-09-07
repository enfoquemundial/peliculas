(function () {
  var AEP = window.AEP || {};
  var BASE = document.documentElement.getAttribute("data-base") || "";
  var header = document.querySelector("[data-header]");
  var menuBtn = document.querySelector("[data-menu]");
  var navMobile = document.getElementById("mobile-nav");
  var open = false;

  function assetUrl(url) {
    url = (url || "").trim();
    if (!url) return url;
    if (/^(https?:)?\/\//i.test(url) || url.indexOf("data:") === 0) return url;
    return BASE + url.replace(/^\//, "");
  }

  var headerBase =
    "fixed inset-x-0 top-0 z-header transition-[background-color,border-color,backdrop-filter] duration-250 ";
  var headerIdle = "border-b border-transparent bg-linear-to-b from-bg/80 to-transparent";
  var headerOn = "border-b border-border bg-bg/92 backdrop-blur-md";

  function paintHeader() {
    if (!header) return;
    header.className = headerBase + (open || window.scrollY > 12 ? headerOn : headerIdle);
  }
  paintHeader();
  window.addEventListener("scroll", paintHeader, { passive: true });

  if (menuBtn && header && navMobile) {
    menuBtn.addEventListener("click", function () {
      open = !open;
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      menuBtn.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
      navMobile.classList.toggle("hidden", !open);
      navMobile.classList.toggle("flex", open);
      document.body.style.overflow = open ? "hidden" : "";
      menuBtn.innerHTML = open
        ? '<svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>'
        : '<svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 5h16M4 12h16M4 19h16"/></svg>';
      paintHeader();
    });
    navMobile.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        open = false;
        navMobile.classList.add("hidden");
        navMobile.classList.remove("flex");
        document.body.style.overflow = "";
        paintHeader();
      });
    });
  }

  if (AEP.googleAnalyticsId) {
    var ga = document.createElement("script");
    ga.async = true;
    ga.src = "https://www.googletagmanager.com/gtag/js?id=" + AEP.googleAnalyticsId;
    document.head.appendChild(ga);
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag("js", new Date());
    gtag("config", AEP.googleAnalyticsId);
  }
  if (AEP.googleSiteVerification) {
    var meta = document.createElement("meta");
    meta.name = "google-site-verification";
    meta.content = AEP.googleSiteVerification;
    document.head.appendChild(meta);
  }

  var ads = AEP.adsterra || {};
  if (ads.siteHead) {
    var hold = document.createElement("div");
    hold.innerHTML = ads.siteHead;
    Array.from(hold.childNodes).forEach(function (n) { document.head.appendChild(n); });
  }
  document.querySelectorAll("[data-ad-slot]").forEach(function (el) {
    var html = ads[el.getAttribute("data-ad-slot")];
    if (html && String(html).trim()) {
      el.className = "mx-auto w-full max-w-5xl overflow-hidden px-4 py-6";
      el.innerHTML = '<div class="flex min-h-0 items-center justify-center">' + html + "</div>";
    }
  });

  var overlay = document.querySelector("[data-dialog-overlay]");
  var dialog = document.querySelector("[data-dialog]");
  var dialogTitle = document.querySelector("[data-dialog-title]");
  var form = document.querySelector("[data-notify-form]");
  var success = document.querySelector("[data-success]");

  function openDialog(title) {
    if (!dialog || !overlay) return;
    if (dialogTitle) dialogTitle.textContent = title || "Amor en Prisión — Parte 2";
    overlay.classList.remove("hidden");
    dialog.classList.remove("hidden");
    var email = dialog.querySelector("#notify-email");
    if (email) email.focus();
  }
  function closeDialog() {
    if (!dialog || !overlay) return;
    overlay.classList.add("hidden");
    dialog.classList.add("hidden");
  }
  document.querySelectorAll("[data-notify]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      openDialog(btn.getAttribute("data-notify") || "");
    });
  });
  if (overlay) overlay.addEventListener("click", closeDialog);
  document.querySelectorAll("[data-close]").forEach(function (b) {
    b.addEventListener("click", closeDialog);
  });
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = form.querySelector("#notify-email");
      var err = form.querySelector("[data-error]");
      var value = ((input && input.value) || "").trim().toLowerCase();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        if (err) err.textContent = "Introduce un correo válido.";
        return;
      }
      try {
        var list = JSON.parse(localStorage.getItem("aep-notify") || "[]");
        if (list.indexOf(value) === -1) list.push(value);
        localStorage.setItem("aep-notify", JSON.stringify(list));
      } catch (x) {}
      form.classList.add("hidden");
      if (success) success.classList.remove("hidden");
    });
  }

  var contact = document.querySelector("[data-contact]");
  if (contact) {
    contact.addEventListener("submit", function (e) {
      e.preventDefault();
      var payload = {
        name: (contact.querySelector("#name") || {}).value || "",
        email: (contact.querySelector("#email") || {}).value || "",
        message: (contact.querySelector("#message") || {}).value || "",
        at: new Date().toISOString(),
      };
      try {
        var prev = JSON.parse(localStorage.getItem("aep-contact") || "[]");
        prev.push(payload);
        localStorage.setItem("aep-contact", JSON.stringify(prev));
      } catch (x) {}
      contact.classList.add("hidden");
      var done = document.querySelector("[data-contact-ok]");
      if (done) {
        done.classList.remove("hidden");
        var thanks = done.querySelector("[data-contact-name]");
        if (thanks) thanks.textContent = payload.name || "por escribir";
      }
    });
  }

  function youtubeId(url) {
    try {
      var u = new URL(url);
      if (u.hostname.indexOf("youtu.be") !== -1) return u.pathname.replace("/", "") || null;
      if (u.hostname.indexOf("youtube.com") !== -1) {
        if (u.pathname.indexOf("/embed/") === 0) return u.pathname.split("/")[2] || null;
        return u.searchParams.get("v");
      }
    } catch (e) { return null; }
    return null;
  }
  function vimeoId(url) {
    try {
      var u = new URL(url);
      if (u.hostname.indexOf("vimeo.com") === -1) return null;
      return u.pathname.split("/").filter(Boolean)[0] || null;
    } catch (e) { return null; }
  }
  function resolvePlayer(url) {
    url = (url || "").trim();
    if (!url) return { kind: "none", src: "" };
    var yt = youtubeId(url);
    if (yt) return { kind: "embed", src: "https://www.youtube-nocookie.com/embed/" + yt + "?rel=0&modestbranding=1&autoplay=1" };
    var vm = vimeoId(url);
    if (vm) return { kind: "embed", src: "https://player.vimeo.com/video/" + vm + "?autoplay=1" };
    if (/\.(mp4|webm|ogg)(\?|$)/i.test(url)) return { kind: "html5", src: assetUrl(url) };
    if (url.indexOf("http") === 0) return { kind: "embed", src: url };
    return { kind: "html5", src: assetUrl(url) };
  }

  var stage = document.querySelector("[data-player]");
  if (stage) {
    var slug = stage.getAttribute("data-player");
    var status = stage.getAttribute("data-status") || "available";
    var poster = assetUrl(stage.getAttribute("data-poster") || "");
    var source = resolvePlayer((AEP.videos && AEP.videos[slug]) || "");
    if (status !== "coming-soon" && (source.kind === "html5" || source.kind === "embed")) {
      stage.addEventListener("click", function playOnce() {
        stage.removeEventListener("click", playOnce);
        if (source.kind === "html5") {
          var video = document.createElement("video");
          video.className = "player-reel";
          video.controls = true;
          video.autoplay = true;
          video.playsInline = true;
          video.poster = poster;
          video.preload = "metadata";
          video.setAttribute("controlslist", "nodownload");
          var src = document.createElement("source");
          src.src = source.src;
          src.type = "video/mp4";
          video.appendChild(src);
          stage.replaceWith(video);
        } else {
          var wrap = document.createElement("div");
          wrap.className = "aspect-video overflow-hidden rounded-xl bg-player";
          wrap.innerHTML =
            '<iframe title="Reproductor" src="' + source.src +
            '" class="size-full" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
          stage.replaceWith(wrap);
        }
      });
    }
  }
})();
