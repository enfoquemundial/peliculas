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
  googleAnalyticsId: "G-L26VFVKY25",

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
    "amor-en-prision-parte-2": "videos/amor-en-prision-parte-2.mp4",
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
    /* 1. Banner debajo del HERO (inicio). 300x250 */
    heroBelow:
      '<script>\n  atOptions = {\n    "key" : "7e914056e9d1944186973b5b82dcfbd5",\n    "format" : "iframe",\n    "height" : 250,\n    "width" : 300,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/7e914056e9d1944186973b5b82dcfbd5/invoke.js"></script>',
    /* 2. Banner entre secciones. 728x90 */
    betweenSections:
      '<script>\n  atOptions = {\n    "key" : "83799c21bf80a75aba6bdd2964a4c1d8",\n    "format" : "iframe",\n    "height" : 90,\n    "width" : 728,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/83799c21bf80a75aba6bdd2964a4c1d8/invoke.js"></script>',
    /* 3. Banner ANTES del reproductor. 320x50 */
    playerBefore:
      '<script>\n  atOptions = {\n    "key" : "0e97eacbf1d2fff572756221bee9dbea",\n    "format" : "iframe",\n    "height" : 50,\n    "width" : 320,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/0e97eacbf1d2fff572756221bee9dbea/invoke.js"></script>',
    /* 4. Banner DEBAJO del reproductor. 468x60 */
    playerAfter:
      '<script>\n  atOptions = {\n    "key" : "0707a3fdb6cac3f20c389bf2c4f9b3c8",\n    "format" : "iframe",\n    "height" : 60,\n    "width" : 468,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/0707a3fdb6cac3f20c389bf2c4f9b3c8/invoke.js"></script>',
    /* 5. Script global del sitio: Social Bar de Adsterra */
    siteHead:
      '<script src="https://pl31223554.profitableratecpmnetwork.com/e9/59/0f/e9590fcdd0c9ca9e688ca8a295202f52.js"></script>',
    /* 6. Riel izquierdo (pantallas anchas). 160x600 */
    railLeft:
      '<script>\n  atOptions = {\n    "key" : "0dec58ef9eaad2ac5e08e9acec928b12",\n    "format" : "iframe",\n    "height" : 600,\n    "width" : 160,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/0dec58ef9eaad2ac5e08e9acec928b12/invoke.js"></script>',
    /* 7. Riel derecho (pantallas anchas). 160x300 */
    railRight:
      '<script>\n  atOptions = {\n    "key" : "9dbab803944767c4407f1cab4a4d7d2e",\n    "format" : "iframe",\n    "height" : 300,\n    "width" : 160,\n    "params" : {}\n  };\n</script>\n<script src="https://www.highrevenueformat.com/9dbab803944767c4407f1cab4a4d7d2e/invoke.js"></script>',
  },
};
