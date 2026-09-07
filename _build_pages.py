#!/usr/bin/env python3
"""Páginas HTML con las mismas clases Tailwind que el sitio en vivo.

Las rutas internas son relativas (index.html, ../css/site.css, …)
para que el sitio abra con doble clic, no solo en un servidor.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANON = "https://www.amorenprision.com"

BTN = (
    "inline-flex items-center justify-center gap-2 whitespace-nowrap font-sans font-semibold "
    "tracking-wide uppercase transition-[transform,background-color,color,border-color,opacity] "
    "duration-150 ease-out focus-visible:outline-2 focus-visible:outline-offset-2 "
    "focus-visible:outline-accent disabled:pointer-events-none disabled:opacity-40 "
    "active:not-disabled:scale-[0.96] select-none"
)
BTN_P = (
    "bg-accent text-accent-fg hover:bg-[color-mix(in_oklab,var(--color-accent)_88%,black)] "
    "shadow-[0_10px_24px_-12px_var(--color-accent)]"
)
BTN_O = "border border-border-strong bg-transparent text-fg hover:bg-elevated hover:border-fg"
BTN_G = "bg-transparent text-fg hover:bg-elevated"
SZ_LG = "h-12 px-4 text-xs rounded-xl sm:h-14 sm:min-w-44 sm:px-6 sm:text-sm"
SZ_MD = "h-12 px-5 text-xs rounded-lg"
SZ_SM = "h-10 px-4 text-xs rounded-md"

PLAY = '<svg class="size-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 5v14l14-7z"/></svg>'
PLAY4 = '<svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 5v14l14-7z"/></svg>'
PLAY7 = '<svg class="size-7 translate-x-0.5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 5v14l14-7z"/></svg>'
INFO = '<svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>'
BELL = '<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>'
MENU = '<svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 5h16M4 12h16M4 19h16"/></svg>'
XICO = '<svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>'
X5 = '<svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>'
CHECK = '<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
CLOCK = '<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
BACK = '<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m12 19-7-7 7-7M19 12H5"/></svg>'

NAV = [("/", "Inicio"), ("/peliculas", "Películas"), ("/miniseries", "Miniseries"), ("/proximamente", "Próximamente"), ("/contacto", "Contacto")]

TITLES = [
    {
        "id": "amor-en-prision", "slug": "amor-en-prision", "title": "Amor en Prisión",
        "kind": "miniseries", "kind_label": "Miniserie",
        "tagline": "Dos mundos. Un mismo corazón.",
        "synopsis": "Él está preso. Ella es una oficial de correcciones. Lo que comenzó como una simple conversación terminará convirtiéndose en un sentimiento capaz de desafiar las reglas de la prisión.",
        "poster": "/images/amor-en-prision.jpg", "backdrop": "/images/amor-en-prision.png",
        "year": 2026, "producer": "Esfrailin Quezada", "status": "available",
        "episodes": [
            {"part": 1, "watch": "amor-en-prision-parte-1", "title": "Amor en Prisión — Parte 1", "status": "available",
             "description": "Él está preso. Ella es una oficial de correcciones. Lo que comenzó como una simple conversación terminará convirtiéndose en un sentimiento capaz de desafiar las reglas de la prisión."},
            {"part": 2, "watch": "amor-en-prision-parte-2", "title": "Amor en Prisión — Parte 2", "status": "available",
             "description": "La historia continúa. Descubre qué sucede después, completamente gratis."},
        ],
    },
    {
        "id": "celdas-del-silencio", "slug": "celdas-del-silencio", "title": "Celdas del Silencio",
        "kind": "miniseries", "kind_label": "Miniserie",
        "tagline": "Algunos secretos no caben detrás de una reja.",
        "synopsis": "Una nueva miniserie de suspenso y romance dentro del sistema penitenciario. Muy pronto.",
        "poster": "/images/celdas-del-silencio.jpg", "backdrop": "/images/celdas-del-silencio.jpg",
        "year": 2026, "producer": "", "status": "coming-soon",
        "episodes": [{"part": 1, "watch": "celdas-del-silencio-parte-1", "title": "Celdas del Silencio — Parte 1", "status": "coming-soon", "description": "El primer capítulo se publicará próximamente."}],
    },
    {
        "id": "la-ultima-visita", "slug": "la-ultima-visita", "title": "La Última Visita",
        "kind": "movie", "kind_label": "Película",
        "tagline": "Un cristal. Dos vidas. Una conversación que lo cambia todo.",
        "synopsis": "En la sala de visitas, una conversación de veinte minutos decide el resto de una vida. Próximamente.",
        "poster": "/images/la-ultima-visita.jpg", "backdrop": "/images/la-ultima-visita.jpg",
        "year": 2026, "producer": "", "status": "coming-soon",
        "episodes": [{"part": 1, "watch": "la-ultima-visita", "title": "La Última Visita", "status": "coming-soon", "description": "Película completa. Se publicará próximamente."}],
    },
    {
        "id": "corazon-condenado", "slug": "corazon-condenado", "title": "Corazón Condenado",
        "kind": "movie", "kind_label": "Película",
        "tagline": "El amor no pide permiso para entrar.",
        "synopsis": "Una historia de redención y deseo a la sombra de las rejas. Próximamente en la plataforma.",
        "poster": "/images/corazon-condenado.jpg", "backdrop": "/images/corazon-condenado.jpg",
        "year": 2026, "producer": "", "status": "coming-soon",
        "episodes": [{"part": 1, "watch": "corazon-condenado", "title": "Corazón Condenado", "status": "coming-soon", "description": "Película completa. Se publicará próximamente."}],
    },
]


def page_depth(path: str) -> int:
    p = path.strip("/")
    if not p:
        return 0
    if p.endswith(".html"):
        parent = p.rsplit("/", 1)
        if len(parent) == 1:
            return 0
        p = parent[0]
    return len([x for x in p.split("/") if x])


def page_base(path: str) -> str:
    d = page_depth(path)
    return "" if d == 0 else "../" * d


def to_relative(url: str, base: str, is_href: bool) -> str:
    if not url or url.startswith(("#", "http://", "https://", "mailto:", "data:", "//", "javascript:")):
        return url
    if not url.startswith("/"):
        return url
    path = url[1:]
    if is_href:
        if path == "":
            return (base + "index.html") if base else "index.html"
        last = path.split("/")[-1]
        if "." in last:
            return base + path
        return base + path.rstrip("/") + "/index.html"
    return base + path


def relativize(html: str, path: str) -> str:
    base = page_base(path)

    def href_sub(m):
        q, url = m.group(1), m.group(2)
        return f"href={q}{to_relative(url, base, True)}{q}"

    def src_sub(m):
        q, url = m.group(1), m.group(2)
        return f"src={q}{to_relative(url, base, False)}{q}"

    def poster_sub(m):
        q, url = m.group(1), m.group(2)
        return f"data-poster={q}{to_relative(url, base, False)}{q}"

    html = re.sub(r'href=(["\'])([^"\']*)\1', href_sub, html)
    html = re.sub(r'src=(["\'])([^"\']*)\1', src_sub, html)
    html = re.sub(r'data-poster=(["\'])([^"\']*)\1', poster_sub, html)
    html = html.replace(
        '<html lang="es" class="antialiased">',
        f'<html lang="es" class="antialiased" data-base="{base}">',
    )
    return html


def badge(status):
    if status == "available":
        return (
            '<span class="inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-[0.68rem] font-semibold tracking-[0.16em] uppercase border-success/40 bg-success/15 text-success">'
            f"{CHECK} Disponible ahora</span>"
        )
    return (
        '<span class="inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-[0.68rem] font-semibold tracking-[0.16em] uppercase border-accent/50 bg-accent/10 text-accent">'
        f"{CLOCK} Próximamente</span>"
    )


def card(t, priority=False):
    href = f"/ver/{t['episodes'][0]['watch']}" if t["status"] == "available" else f"/pelicula/{t['slug']}"
    loading = "eager" if priority else "lazy"
    sat = " saturate-75" if t["status"] != "available" else ""
    if t["status"] == "coming-soon":
        overlay = '<div class="absolute inset-0 grid place-items-center"><span class="stamp">Próximamente</span></div>'
    else:
        overlay = (
            '<div class="absolute inset-0 grid place-items-center opacity-0 transition-opacity duration-250 group-hover:opacity-100">'
            f'<span class="grid size-16 place-items-center rounded-full bg-accent text-accent-fg shadow-card">{PLAY7}</span></div>'
        )
    cta = "Ver" if t["status"] == "available" else "Próximamente"
    return f"""
    <article class="group relative">
      <a href="{href}" class="block rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-accent">
        <div class="relative overflow-hidden rounded-2xl border border-border bg-surface shadow-card transition-[transform,border-color,box-shadow] duration-250 ease-out group-hover:-translate-y-1 group-hover:border-accent/50">
          <div class="poster-frame relative overflow-hidden">
            <img src="{t['poster']}" alt="Póster de {t['title']}" width="600" height="900" loading="{loading}" decoding="async" class="transition-transform duration-500 ease-out group-hover:scale-[1.04]{sat}">
            <div class="absolute inset-0 bg-linear-to-t from-bg via-bg/20 to-transparent"></div>
            {overlay}
            <div class="absolute left-3 top-3">{badge(t['status'])}</div>
          </div>
          <div class="space-y-1.5 p-4">
            <p class="text-xs font-semibold uppercase tracking-[0.22em] text-subtle">{t['kind_label']} · {t['year']}</p>
            <h3 class="font-display text-lg leading-snug text-fg">{t['title']}</h3>
            <p class="line-clamp-2 text-sm text-muted">{t['tagline']}</p>
            <p class="pt-2 text-xs font-semibold uppercase tracking-[0.18em] text-accent">{cta}</p>
          </div>
        </div>
      </a>
    </article>"""


def notify_btn(title, size="lg"):
    sz = SZ_LG if size == "lg" else SZ_MD
    return (
        f'<button type="button" data-notify="{title}" class="{BTN} {BTN_O} {sz}">'
        f"{BELL} Avísame cuando esté disponible</button>"
    )


def head(title, desc, path, extra=""):
    url = CANON + (path if path != "/" else "/")
    img = CANON + "/images/amor-en-prision.jpg"
    return f"""<!DOCTYPE html>
<html lang="es" class="antialiased">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#070607">
  <meta name="robots" content="index,follow">
  <meta name="author" content="Esfrailin Quezada">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img}">
  <meta property="og:locale" content="es_LA">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{img}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Outfit:wght@300;400;500;600;700&display=swap">
  <link rel="stylesheet" href="/css/site.css">
  {extra}
</head>"""


def chrome(active):
    links = []
    mobile = []
    for href, label in NAV:
        on = href == "/" and active == "/" or (href != "/" and (active == href or active.startswith(href + "/")))
        cls = "text-sm font-medium tracking-wide transition-colors duration-150 " + ("text-fg" if on else "text-muted hover:text-fg")
        bar = '<span class="mt-1 block h-px w-full bg-accent"></span>' if on else ""
        links.append(f'<a href="{href}" class="{cls}">{label}{bar}</a>')
        mobile.append(f'<a href="{href}" class="border-b border-border py-4 font-display text-2xl text-fg">{label}</a>')
    return f"""
  <a href="#contenido" class="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-modal focus:rounded-md focus:bg-accent focus:px-3 focus:py-2 focus:text-accent-fg">Saltar al contenido</a>
  <header class="fixed inset-x-0 top-0 z-header transition-[background-color,border-color,backdrop-filter] duration-250 border-b border-transparent bg-linear-to-b from-bg/80 to-transparent" data-header>
    <div class="mx-auto flex h-16 max-w-6xl items-center justify-between gap-4 px-4 sm:h-[4.25rem] sm:px-6">
      <a href="/" class="font-display text-[0.95rem] font-semibold tracking-[0.18em] text-fg sm:text-base">AMOR EN PRISIÓN</a>
      <nav class="hidden items-center gap-7 md:flex" aria-label="Principal">{''.join(links)}</nav>
      <button type="button" class="grid size-11 place-items-center rounded-md text-fg md:hidden" data-menu aria-expanded="false" aria-controls="mobile-nav" aria-label="Abrir menú">{MENU}</button>
    </div>
    <nav id="mobile-nav" class="hidden min-h-[100svh] flex-col gap-2 bg-bg px-6 pb-16 pt-4 md:hidden" aria-label="Móvil">{''.join(mobile)}</nav>
  </header>"""


def footer():
    return f"""
  <footer class="mt-auto border-t border-border bg-surface">
    <div class="barbed" aria-hidden="true"></div>
    <div class="mx-auto max-w-6xl px-4 py-12 sm:px-6">
      <p class="font-display text-lg tracking-[0.2em] text-fg">AMOR EN PRISIÓN</p>
      <p class="mt-2 max-w-md text-sm text-muted">“Historias que merecen ser vistas.”</p>
      <nav class="mt-8 flex flex-wrap gap-x-6 gap-y-3 text-sm text-muted" aria-label="Pie de página">
        <a href="/" class="hover:text-fg">Inicio</a>
        <a href="/peliculas" class="hover:text-fg">Películas</a>
        <a href="/proximamente" class="hover:text-fg">Próximamente</a>
        <a href="/contacto" class="hover:text-fg">Contacto</a>
        <a href="/privacidad" class="hover:text-fg">Política de Privacidad</a>
        <a href="/terminos" class="hover:text-fg">Términos y Condiciones</a>
      </nav>
      <p class="mt-10 text-xs text-subtle">© 2026 AMOR EN PRISIÓN. Todos los derechos reservados. Producida por Esfrailin Quezada.</p>
    </div>
  </footer>
  <div class="fixed inset-0 z-modal bg-bg/80 hidden" data-dialog-overlay></div>
  <div class="fixed left-1/2 top-1/2 z-modal w-[min(92vw,28rem)] -translate-x-1/2 -translate-y-1/2 rounded-2xl border border-border bg-surface p-6 shadow-card focus:outline-none hidden" data-dialog role="dialog" aria-labelledby="dlg-title">
    <button class="absolute right-3 top-3 grid size-11 place-items-center rounded-md text-muted hover:text-fg" type="button" data-close aria-label="Cerrar">{X5}</button>
    <form data-notify-form class="pr-8">
      <h2 id="dlg-title" class="font-display text-xl text-fg">Avísame</h2>
      <p class="mt-2 text-sm text-muted">Déjanos tu correo y te avisamos el día que <span data-dialog-title>Amor en Prisión — Parte 2</span> esté lista para ver gratis.</p>
      <div class="mt-5 space-y-2">
        <label class="text-xs font-medium uppercase tracking-[0.16em] text-muted" for="notify-email">Correo electrónico</label>
        <input id="notify-email" type="email" autocomplete="email" required placeholder="tu@correo.com" class="flex h-12 w-full rounded-lg border border-border bg-elevated px-4 text-base text-fg placeholder:text-subtle transition-[border-color,box-shadow] duration-150 focus-visible:outline-none focus-visible:border-accent focus-visible:ring-2 focus-visible:ring-accent/40">
        <p data-error class="text-sm text-accent"></p>
      </div>
      <button type="submit" class="{BTN} {BTN_P} {SZ_MD} mt-5 w-full">Quiero que me avisen</button>
      <p class="mt-3 text-xs text-subtle">No enviamos spam. Puedes dejar de recibir avisos cuando quieras.</p>
    </form>
    <div data-success class="pr-8 hidden">
      <h2 class="font-display text-xl text-fg">Te avisaremos</h2>
      <p class="mt-2 text-sm text-muted">Guardamos tu correo en este dispositivo. Cuando se publique, serás de los primeros en saberlo.</p>
      <button type="button" data-close class="{BTN} {BTN_P} {SZ_MD} mt-6 w-full">Cerrar</button>
    </div>
  </div>
  <script src="/js/config.js"></script>
  <script src="/js/site.js"></script>
</body>
</html>"""


def page(path, title, desc, active, body, extra=""):
    html = (
        head(title, desc, path, extra)
        + f"""
<body class="bg-bg text-fg">
  <div class="grain" aria-hidden="true"></div>
  <div class="ad-rail ad-rail-left" data-ad-slot="railLeft"></div>
  <div class="ad-rail ad-rail-right" data-ad-slot="railRight"></div>
  <div class="flex min-h-svh flex-col bg-bg text-fg">
{chrome(active)}
    <main id="contenido" class="flex-1">
{body}
    </main>
    <div data-ad-slot="betweenSections"></div>
{footer()}
"""
    )
    html = relativize(html, path)
    dest = ROOT / path.lstrip("/")
    if path.endswith("/") or path == "/":
        dest = (ROOT if path == "/" else dest) / "index.html"
    elif not path.endswith(".html"):
        dest = dest / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT))


featured = TITLES[0]
p1, p2 = featured["episodes"]

ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TVSeries","name":"Amor en Prisión","description":"{featured["synopsis"]}","image":"{CANON}{featured["poster"]}","inLanguage":"es","url":"{CANON}/pelicula/amor-en-prision"}}</script>'

page(
    "/",
    "AMOR EN PRISIÓN — Dos mundos. Un mismo corazón.",
    "Amor en Prisión es una plataforma de cine y miniseries. Mira gratis la Parte 1 de la historia de un preso y una oficial de correcciones. La Parte 2 llega pronto.",
    "/",
    f"""
      <section class="relative isolate min-h-[100svh] overflow-hidden bg-bg">
        <img src="{featured['backdrop']}" alt="Amor en Prisión: un preso y una oficial de correcciones frente a frente" width="1000" height="1500" fetchpriority="high" decoding="async" class="absolute inset-0 size-full object-cover object-[62%_18%] sm:object-[58%_12%]">
        <div class="absolute inset-0 bg-linear-to-t from-bg via-bg/55 to-bg/25" aria-hidden="true"></div>
        <div class="absolute inset-0 bg-linear-to-r from-bg via-bg/40 to-transparent" aria-hidden="true"></div>
        <div class="absolute inset-x-0 top-0 h-28 bg-linear-to-b from-bg/80 to-transparent" aria-hidden="true"></div>
        <div class="relative mx-auto flex min-h-[100svh] max-w-6xl flex-col justify-end px-4 pb-10 pt-24 sm:px-6 sm:pb-20 lg:pb-24">
          <p class="kicker">Disponible ahora · Parte 1</p>
          <h1 class="mt-3 max-w-xl font-display text-[clamp(2.1rem,7.2vw,5.4rem)] leading-[0.95] tracking-[0.04em] text-fg sm:mt-4">AMOR EN<span class="block text-accent">PRISIÓN</span></h1>
          <p class="mt-3 max-w-lg font-display text-base italic text-fg sm:mt-5 sm:text-xl">“Dos mundos. Un mismo corazón.”</p>
          <p class="mt-2 max-w-lg text-sm text-muted sm:mt-3 sm:text-lg">Una historia de amor que nació donde nadie esperaba encontrarlo.</p>
          <div class="mt-5 flex flex-row flex-wrap gap-3 sm:mt-8 sm:items-center">
            <a href="/ver/amor-en-prision-parte-1" class="{BTN} {BTN_P} {SZ_LG} min-w-0 flex-1 sm:flex-none">{PLAY} Ver parte 1</a>
            <a href="/pelicula/amor-en-prision" class="{BTN} {BTN_O} {SZ_LG} min-w-0 flex-1 sm:flex-none">{INFO} Más información</a>
          </div>
          <p class="mt-5 text-xs uppercase tracking-[0.22em] text-subtle sm:mt-8">Productor: Esfrailin Quezada</p>
        </div>
      </section>
      <div data-ad-slot="heroBelow"></div>
      <section class="mx-auto w-full max-w-6xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="kicker">La película</p>
        <h2 class="mt-3 font-display text-3xl text-fg sm:text-4xl">Amor en Prisión</h2>
        <div class="mt-8 flex flex-col items-start gap-8 sm:flex-row sm:items-center sm:gap-12">
          <a href="/pelicula/amor-en-prision" class="poster-frame relative block w-full max-w-72 shrink-0 overflow-hidden rounded-2xl border border-border shadow-card">
            <img src="{featured['poster']}" alt="Póster de Amor en Prisión, Parte 1" width="600" height="900">
          </a>
          <div>
            <p class="font-display text-2xl text-fg">Parte 1</p>
            <div class="mt-3">{badge('available')}</div>
            <p class="mt-5 max-w-xl text-base leading-relaxed text-muted">“{p1['description']}”</p>
            <a href="/ver/amor-en-prision-parte-1" class="{BTN} {BTN_P} {SZ_LG} mt-8 inline-flex">{PLAY} Ver parte 1</a>
          </div>
        </div>
      </section>
      <div data-ad-slot="playerBefore"></div>
      <section class="relative overflow-hidden border-y border-border bg-surface">
        <img src="/images/manos-entre-rejas.jpg" alt="" class="absolute inset-0 size-full object-cover opacity-25" loading="lazy">
        <div class="absolute inset-0 bg-bg/70"></div>
        <div class="relative mx-auto grid max-w-6xl items-center gap-10 px-4 py-20 sm:px-6 lg:grid-cols-2">
          <div>
            <p class="kicker">{'Ya disponible' if p2['status'] == 'available' else 'Próxima entrega'}</p>
            <h2 class="mt-4 font-display text-4xl leading-tight text-fg sm:text-5xl">LA HISTORIA CONTINÚA…</h2>
            <p class="mt-6 font-display text-xl tracking-wide text-accent">AMOR EN PRISIÓN — PARTE 2</p>
            {f'''<p class="mt-3 max-w-md text-base text-muted">Ya puedes ver qué sucede después, completamente gratis.</p>
            <a href="/ver/amor-en-prision-parte-2" class="{BTN} {BTN_P} {SZ_LG} mt-8 inline-flex">{PLAY} Ver parte 2</a>''' if p2['status'] == 'available' else f'''<p class="mt-3 max-w-md text-base text-muted">Muy pronto podrás descubrir qué sucederá después.</p>
            <p class="mt-4 max-w-md text-sm text-subtle">La segunda parte de Amor en Prisión será publicada próximamente. Cuando esté disponible podrás verla aquí completamente gratis.</p>
            <div class="mt-8">{notify_btn(p2['title'])}</div>'''}
          </div>
          <a href="/ver/amor-en-prision-parte-2" class="poster-frame relative mx-auto block w-full max-w-xs overflow-hidden rounded-2xl border border-border">
            <img src="/images/amor-en-prision-parte-2.jpg" alt="Póster de Amor en Prisión Parte 2{'' if p2['status'] == 'available' else ', próximamente'}" width="600" height="900" loading="lazy" class="{'' if p2['status'] == 'available' else 'saturate-50'}">
            {'' if p2['status'] == 'available' else '<div class="absolute inset-0 grid place-items-center bg-bg/25"><span class="stamp">Próximamente</span></div>'}
          </a>
        </div>
      </section>
      <div data-ad-slot="betweenSections"></div>
      <section class="mx-auto w-full max-w-6xl px-4 py-16 sm:px-6 sm:py-20">
        <div class="flex items-end justify-between gap-4">
          <div>
            <p class="kicker">Catálogo</p>
            <h2 class="mt-3 font-display text-3xl text-fg">El catálogo</h2>
          </div>
          <a href="/proximamente" class="hidden text-sm font-medium text-muted hover:text-fg sm:inline">Ver todo</a>
        </div>
        <div class="mt-10 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">
          {''.join(card(t, priority=i<2) for i,t in enumerate(TITLES))}
        </div>
      </section>
    """,
    ld,
)

page("/peliculas", "Películas · AMOR EN PRISIÓN", "Todas las películas de Amor en Prisión. Drama y romance listos para ver, y títulos que llegan pronto.", "/peliculas", f"""
      <div class="mx-auto max-w-6xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Catálogo</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Películas</h1>
        <p class="mt-3 max-w-xl text-muted">Historias completas, pensadas para verse de una sentada.</p>
        <div class="mt-8"><div data-ad-slot="heroBelow"></div></div>
        <div class="mt-10 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">{''.join(card(t) for t in TITLES if t['kind']=='movie')}</div>
        <div class="mt-12"><div data-ad-slot="playerBefore"></div></div>
        <div class="mt-16">
          <p class="kicker">También disponibles</p>
          <h2 class="mt-3 font-display text-2xl text-fg">Miniseries para ver ahora</h2>
          <div class="mt-8 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">{''.join(card(t) for t in TITLES if t['status']=='available')}</div>
        </div>
      </div>""")

page("/miniseries", "Miniseries · AMOR EN PRISIÓN", "Miniseries de Amor en Prisión. Mira la Parte 1 ahora y espera las siguientes entregas.", "/miniseries", f"""
      <div class="mx-auto max-w-6xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Catálogo</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Miniseries</h1>
        <p class="mt-3 max-w-xl text-muted">Historias en partes. Entra cuando quieras; la siguiente entrega llega aquí.</p>
        <div class="mt-8"><div data-ad-slot="heroBelow"></div></div>
        <div class="mt-10 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">{''.join(card(t, priority=i==0) for i,t in enumerate(t for t in TITLES if t['kind']=='miniseries'))}</div>
        <div class="mt-12"><div data-ad-slot="playerBefore"></div></div>
      </div>""")

page("/proximamente", "Próximamente · AMOR EN PRISIÓN", "Lo que llega a Amor en Prisión: Parte 2, nuevas películas y miniseries.", "/proximamente", f"""
      <div class="mx-auto max-w-6xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Calendario</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Próximamente</h1>
        <p class="mt-3 max-w-xl text-muted">Nuevas películas, miniseries y capítulos.</p>
        <div class="mt-8"><div data-ad-slot="heroBelow"></div></div>
        <div class="mt-12 overflow-hidden rounded-2xl border border-border bg-surface">
          <div class="grid items-center gap-6 p-5 sm:grid-cols-[180px_1fr] sm:p-8">
            <img src="/images/amor-en-prision-parte-2.jpg" alt="Amor en Prisión Parte 2" width="360" height="540" class="aspect-2/3 w-full rounded-xl object-cover">
            <div>
              <p class="kicker">La historia continúa…</p>
              <h2 class="mt-3 font-display text-2xl text-fg sm:text-3xl">Amor en Prisión — Parte 2</h2>
              <p class="mt-3 text-muted">Muy pronto podrás descubrir qué sucederá después.</p>
              <div class="mt-6">{notify_btn('Amor en Prisión — Parte 2', 'md')}</div>
            </div>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-2 gap-4 sm:gap-6 lg:grid-cols-4">{''.join(card(t) for t in TITLES if t['status']!='available')}</div>
        <div class="mt-12"><div data-ad-slot="playerBefore"></div></div>
      </div>""")

page("/contacto", "Contacto · AMOR EN PRISIÓN", "Escríbenos. Prensa, colaboraciones y consultas sobre Amor en Prisión.", "/contacto", f"""
      <div class="mx-auto max-w-xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Hablemos</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Contacto</h1>
        <p class="mt-3 text-muted">Prensa, colaboraciones o preguntas sobre la plataforma. Te leemos.</p>
        <form data-contact class="mt-10 space-y-5">
          <div class="space-y-2">
            <label class="text-xs font-medium uppercase tracking-[0.16em] text-muted" for="name">Nombre</label>
            <input id="name" name="name" required autocomplete="name" class="flex h-12 w-full rounded-lg border border-border bg-elevated px-4 text-base text-fg placeholder:text-subtle transition-[border-color,box-shadow] duration-150 focus-visible:outline-none focus-visible:border-accent focus-visible:ring-2 focus-visible:ring-accent/40">
          </div>
          <div class="space-y-2">
            <label class="text-xs font-medium uppercase tracking-[0.16em] text-muted" for="email">Correo</label>
            <input id="email" name="email" type="email" required autocomplete="email" class="flex h-12 w-full rounded-lg border border-border bg-elevated px-4 text-base text-fg placeholder:text-subtle transition-[border-color,box-shadow] duration-150 focus-visible:outline-none focus-visible:border-accent focus-visible:ring-2 focus-visible:ring-accent/40">
          </div>
          <div class="space-y-2">
            <label class="text-xs font-medium uppercase tracking-[0.16em] text-muted" for="message">Mensaje</label>
            <textarea id="message" name="message" required rows="6" class="w-full rounded-lg border border-border bg-elevated px-4 py-3 text-base text-fg placeholder:text-subtle focus-visible:border-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40"></textarea>
          </div>
          <button type="submit" class="{BTN} {BTN_P} {SZ_LG} w-full">Enviar</button>
        </form>
        <div data-contact-ok class="mt-10 rounded-2xl border border-border bg-surface p-6 hidden">
          <h2 class="font-display text-2xl text-fg">Mensaje recibido</h2>
          <p class="mt-2 text-sm text-muted">Gracias, <span data-contact-name></span>. Guardamos tu mensaje en este dispositivo.</p>
        </div>
        <div class="mt-10"><div data-ad-slot="playerBefore"></div></div>
      </div>""")

page("/privacidad", "Política de Privacidad · AMOR EN PRISIÓN", "Política de privacidad de AMOR EN PRISIÓN. Cómo tratamos datos, cookies y avisos.", "/", """
      <article class="mx-auto max-w-2xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Legal</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Política de Privacidad</h1>
        <div class="mt-6"><div data-ad-slot="playerBefore"></div></div>
        <div class="mt-8 space-y-6 text-sm leading-relaxed text-muted">
          <p>AMOR EN PRISIÓN respeta tu privacidad. Esta página explica qué datos se pueden recoger al usar el sitio y con qué fin.</p>
          <h2 class="font-display text-xl text-fg">Datos que nos das</h2>
          <p>Si dejas tu correo para que te avisemos de un estreno, o envías el formulario de contacto, esa información se guarda en tu propio navegador (almacenamiento local) hasta que conectemos un servicio de correo. No la vendemos.</p>
          <h2 class="font-display text-xl text-fg">Analítica</h2>
          <p>Si el propietario activa Google Analytics, ese servicio puede registrar visitas de forma agregada. El identificador se configura en js/config.js.</p>
          <h2 class="font-display text-xl text-fg">Publicidad</h2>
          <p>El sitio está preparado para anuncios de Adsterra. Cuando esos códigos estén activos, Adsterra puede usar cookies o identificadores según su propia política. Los anuncios no cubren el reproductor ni los controles principales.</p>
          <h2 class="font-display text-xl text-fg">Contacto</h2>
          <p>Para ejercer derechos sobre tus datos, usa la página de Contacto.</p>
        </div>
      </article>""")

page("/terminos", "Términos y Condiciones · AMOR EN PRISIÓN", "Términos de uso de AMOR EN PRISIÓN. Visualización personal del catálogo.", "/", """
      <article class="mx-auto max-w-2xl px-4 pb-20 pt-24 sm:px-6">
        <p class="kicker">Legal</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Términos y Condiciones</h1>
        <div class="mt-6"><div data-ad-slot="playerBefore"></div></div>
        <div class="mt-8 space-y-6 text-sm leading-relaxed text-muted">
          <p>Al entrar a AMOR EN PRISIÓN aceptas estos términos. Si no estás de acuerdo, no uses el sitio.</p>
          <h2 class="font-display text-xl text-fg">Uso del contenido</h2>
          <p>Las películas y miniseries se ofrecen para visionado personal y no comercial. Queda prohibido copiar, redistribuir, retransmitir o explotar el material sin autorización del productor.</p>
          <h2 class="font-display text-xl text-fg">Disponibilidad</h2>
          <p>La Parte 1 de Amor en Prisión está publicada. Títulos marcados como “Próximamente” pueden cambiar de fecha o de ficha.</p>
          <h2 class="font-display text-xl text-fg">Cuentas y menores</h2>
          <p>El sitio no exige cuenta. El contenido es drama romántico para público adulto. Quien permita el acceso a menores es responsable de esa supervisión.</p>
          <h2 class="font-display text-xl text-fg">Limitación</h2>
          <p>El servicio se ofrece “tal cual”. No respondemos por interrupciones de red, bloqueos de anuncios o fallos de terceros (alojamiento de video, redes publicitarias).</p>
        </div>
      </article>""")

page("/404.html", "Página no encontrada · AMOR EN PRISIÓN", "Esta ruta no existe.", "/", f"""
      <div class="mx-auto flex min-h-[70svh] max-w-xl flex-col items-center justify-center px-4 pb-20 pt-24 text-center sm:px-6">
        <p class="kicker">Error 404</p>
        <h1 class="mt-3 font-display text-4xl text-fg">Página no encontrada</h1>
        <p class="mt-3 text-muted">Esta ruta no existe. Vuelve al inicio para seguir viendo.</p>
        <a href="/" class="{BTN} {BTN_P} {SZ_LG} mt-8">Ir al inicio</a>
      </div>""")

for t in TITLES:
    eps = ""
    for ep in t["episodes"]:
        if ep["status"] == "available":
            action = f'<a href="/ver/{ep["watch"]}" class="{BTN} {BTN_P} {SZ_MD} mt-5 inline-flex">{PLAY4} Ver parte {ep["part"]}</a>'
        else:
            action = f'<div class="mt-5">{notify_btn(ep["title"], "md")}</div>'
        eps += f"""
              <li class="rounded-2xl border border-border bg-surface/80 p-5">
                <div class="flex flex-wrap items-center justify-between gap-3">
                  <h2 class="font-display text-xl text-fg">{ep['title']}</h2>
                  {badge(ep['status'])}
                </div>
                <p class="mt-3 text-sm text-muted">{ep['description']}</p>
                {action}
              </li>"""
    producer = f'<p class="mt-4 text-xs uppercase tracking-[0.2em] text-subtle">Productor: {t["producer"]}</p>' if t["producer"] else ""
    schema = "TVSeries" if t["kind"] == "miniseries" else "Movie"
    extra = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"{schema}","name":"{t["title"]}","description":"{t["synopsis"]}","image":"{CANON}{t["poster"]}","url":"{CANON}/pelicula/{t["slug"]}"}}</script>'
    page(
        f"/pelicula/{t['slug']}",
        f"{t['title']} · AMOR EN PRISIÓN",
        t["synopsis"],
        "/peliculas" if t["kind"] == "movie" else "/miniseries",
        f"""
      <article class="relative">
        <div class="absolute inset-x-0 top-0 h-96 overflow-hidden">
          <img src="{t['backdrop']}" alt="" class="hero-still size-full opacity-40">
          <div class="absolute inset-0 bg-linear-to-t from-bg via-bg/80 to-bg/40"></div>
        </div>
        <div class="relative mx-auto flex max-w-6xl flex-col gap-10 px-4 pb-20 pt-28 sm:flex-row sm:px-6">
          <div class="poster-frame w-full max-w-72 shrink-0 overflow-hidden rounded-2xl border border-border shadow-card">
            <img src="{t['poster']}" alt="Póster de {t['title']}" width="560" height="840">
          </div>
          <div>
            <p class="kicker">{t['kind_label']} · {t['year']}</p>
            <h1 class="mt-3 font-display text-4xl text-fg sm:text-5xl">{t['title']}</h1>
            <p class="mt-3 font-display text-lg italic text-muted">“{t['tagline']}”</p>
            <p class="mt-5 max-w-xl text-base leading-relaxed text-muted">{t['synopsis']}</p>
            <div class="mt-6"><div data-ad-slot="heroBelow"></div></div>
            {producer}
            <ul class="mt-10 space-y-4">{eps}</ul>
            <div class="mt-6"><div data-ad-slot="playerBefore"></div></div>
          </div>
        </div>
      </article>""",
        extra,
    )

for t in TITLES:
    for ep in t["episodes"]:
        if ep["status"] == "coming-soon":
            player = f"""
        <div class="stage-frame relative rounded-xl" data-player="{ep['watch']}" data-status="coming-soon" data-poster="{t['poster']}">
          <img src="{t['poster']}" alt="">
          <div class="absolute inset-0 grid place-items-center bg-bg/45 p-6 text-center">
            <div>
              <p class="kicker">Próximamente</p>
              <p class="mt-3 font-display text-2xl text-fg">{ep['title']}</p>
              <p class="mt-2 text-sm text-muted">Este capítulo aún no está publicado.</p>
            </div>
          </div>
        </div>"""
            extra_btn = f'<div class="mt-6">{notify_btn(ep["title"])}</div>'
        else:
            player = f"""
        <button type="button" class="stage-frame relative block w-full rounded-xl" data-player="{ep['watch']}" data-status="available" data-poster="{t['poster']}" aria-label="Reproducir {ep['title']}">
          <img src="{t['poster']}" alt="">
          <span class="absolute inset-0 bg-bg/35"></span>
          <span class="absolute inset-0 grid place-items-center">
            <span class="grid size-16 place-items-center rounded-full bg-accent text-accent-fg">{PLAY7}</span>
          </span>
        </button>"""
            extra_btn = ""
        extra = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"VideoObject","name":"{ep["title"]}","description":"{ep["description"]}","thumbnailUrl":"{CANON}{t["poster"]}","potentialAction":{{"@type":"WatchAction","target":"{CANON}/ver/{ep["watch"]}"}}}}</script>'
        page(
            f"/ver/{ep['watch']}",
            f"{ep['title']} · AMOR EN PRISIÓN",
            ep["description"],
            "/",
            f"""
      <div class="mx-auto w-full max-w-5xl px-4 pb-20 pt-24 sm:px-6">
        <a href="/pelicula/{t['slug']}" class="{BTN} {BTN_G} {SZ_SM} mb-6 -ml-2 uppercase">{BACK} Volver</a>
        <div data-ad-slot="playerBefore"></div>
        {player}
        <div data-ad-slot="playerAfter"></div>
        <div class="mt-8">
          <div class="flex flex-wrap items-center gap-3">
            {badge(ep['status'])}
            <p class="text-xs uppercase tracking-[0.2em] text-subtle">Parte {ep['part']}</p>
          </div>
          <h1 class="mt-3 font-display text-3xl text-fg sm:text-4xl">{ep['title']}</h1>
          <p class="mt-2 font-display text-base italic text-muted">{t['tagline']}</p>
          <p class="mt-4 max-w-2xl text-base leading-relaxed text-muted">{ep['description']}</p>
          {extra_btn}
        </div>
        <div class="mt-10"><div data-ad-slot="heroBelow"></div></div>
      </div>""",
            extra,
        )

print("done")
