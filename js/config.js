/**
 * =============================================================================
 *  AMOR EN PRISIÓN — Configuración (EDITA ESTE ARCHIVO)
 * =============================================================================
 *
 *  1. URL del video de cada parte
 *  2. Códigos oficiales de Adsterra
 *  3. Google Analytics y Search Console
 *  4. Dominio canónico (SEO)
 *
 *  Después de editar, sube de nuevo este archivo (js/config.js) a tu hosting.
 *  No hace falta tocar el resto de la web.
 * =============================================================================
 */
window.AEP = {
  /* CAMBIA ESTA URL cuando el sitio esté en tu dominio (sin barra al final). */
  canonicalUrl: "https://www.amorenprision.com",

  /* PEGA AQUÍ tu ID de Google Analytics 4. Ejemplo: "G-XXXXXXXXXX" */
  googleAnalyticsId: "",

  /* PEGA AQUÍ el código de verificación de Google Search Console. */
  googleSiteVerification: "",

  /**
   * URL DE CADA VIDEO
   * Acepta: enlace .mp4 / .webm, YouTube o Vimeo.
   * Ejemplos:
   *   "https://cdn.tudominio.com/videos/parte-1.mp4"
   *   "https://www.youtube.com/watch?v=XXXXXXXXXXX"
   * Déjalo vacío hasta tener el video. El reproductor no se rompe.
   */
  videos: {
    "amor-en-prision-parte-1": "videos/amor-en-prision-parte-1.mp4",
    "amor-en-prision-parte-2": "", // >>> PEGA AQUÍ la URL de la PARTE 2 cuando se publique
    "celdas-del-silencio-parte-1": "",
    "la-ultima-visita": "",
    "corazon-condenado": "",
  },

  /**
   * ESPACIOS ADSTERRA
   * Pega el HTML/JS oficial que te dé Adsterra. Vacío = no se muestra nada
   * (no hay anuncios falsos). Nunca cubren el reproductor ni los botones.
   */
  adsterra: {
    /* 1. Banner debajo del HERO (inicio) */
    heroBelow: "",
    /* 2. Banner entre secciones */
    betweenSections: "",
    /* 3. Banner ANTES del reproductor */
    playerBefore: "",
    /* 4. Banner DEBAJO del reproductor */
    playerAfter: "",
    /* 5. Script global del sitio (pegar el <script> de Adsterra para todo el sitio) */
    siteHead: "",
  },
};
