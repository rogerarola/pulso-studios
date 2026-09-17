#!/usr/bin/env python3
"""Generates index.html (EN) and es/index.html (ES) from one template.

Run from the repo root:  python3 _build/build.py
GitHub Pages ignores folders starting with "_", so this file is never published.
Edit the copy in STRINGS, run the script, commit the generated HTML.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://pulso-studios.com"
EMAIL = "contact@pulso-studios.com"

STRINGS = {
    "en": {
        "path": "/",
        "locale": "en_US",
        "alt_locale": "es_ES",
        "title": "Pulso Studios — EDM Mixing, Mastering & Music Production Studio",
        "description": "Pulso Studios is a professional mixing, mastering and music production studio for EDM artists and labels. DSP-ready, club-ready sound through precise engineering.",
        "og_title": "Pulso Studios — EDM Mixing, Mastering & Music Production",
        "og_description": "Professional mixing, mastering and production for EDM artists and labels. Precise, DSP-ready sound engineering for electronic music.",
        "og_alt": "Pulso Studios. EDM mixing, mastering and music production",
        "skip": "Skip to content",
        "nav_label": "Main",
        "nav_work": "Selected work",
        "nav_services": "Services",
        "nav_faq": "FAQ",
        "cta": "Get in touch",
        "lang_label": "Language",
        "h1": "EDM mixing, mastering and music production for artists and labels.",
        "about": "Pulso Studios is a professional mixing, mastering and music production studio for EDM artists and labels. We turn raw ideas into polished, DSP-ready and club-ready records through precise sound engineering and meticulous attention to detail.",
        "marquee": ["DSP-ready", "club-ready"],
        "services_h2": "Services",
        "services": [
            ("Mixing", "Professional mixing for EDM and electronic music tracks."),
            ("Mastering", "DSP-ready and club-ready mastering for electronic music releases."),
            ("Music production", "Music production services tailored for EDM artists."),
        ],
        "work_h2": "Selected work",
        "proj1_service": "Mixing &amp; Mastering",
        "proj2_service": "Mixing",
        "proj1_alt": "Cover artwork of When I Close My Eyes (ARLA &amp; BAAT Remix)",
        "proj2_alt": "Cover artwork of the Dreamlight EP by BAAT",
        "faq_h2": "FAQ",
        "faq": [
            ("What does Pulso Studios do?", "Pulso Studios is a mixing, mastering and music production studio specialised in EDM, helping artists and labels turn their tracks into a polished, professional, release-ready sound."),
            ("What genres does Pulso Studios work with?", "Pulso Studios primarily works with EDM and related electronic music genres, mixing and mastering tracks for producers, artists and labels."),
            ("Do you offer mixing and mastering as separate services?", "Yes. Pulso Studios offers mixing and mastering as standalone services or combined together, depending on what the track needs."),
            ("How can I send my tracks to Pulso Studios?", "You can get in touch through the contact form on this page or email contact@pulso-studios.com with details about your project."),
        ],
        "contact_h2": "Get in touch",
        "or_email": "Or send an email to",
        "label_name": "Your name",
        "label_email": "Your email",
        "label_message": "Message",
        "submit": "Send",
        "mail_subject": "New message from",
        "mail_opening": "Opening your mail client...",
        "org_description": "Pulso Studios is a professional mixing, mastering and music production studio for EDM artists and labels.",
        "knows": ["EDM mixing", "Mastering", "Music production", "Electronic music"],
    },
    "es": {
        "path": "/es/",
        "locale": "es_ES",
        "alt_locale": "en_US",
        "title": "Pulso Studios — Estudio de mezcla, mastering y producción de EDM",
        "description": "Pulso Studios es un estudio profesional de mezcla, masterización y producción musical para artistas y sellos de EDM. Sonido listo para DSPs y para el club.",
        "og_title": "Pulso Studios — Mezcla, mastering y producción de EDM",
        "og_description": "Mezcla, masterización y producción profesional para artistas y sellos de EDM. Ingeniería de sonido precisa para música electrónica.",
        "og_alt": "Pulso Studios. Mezcla, mastering y producción musical de EDM",
        "skip": "Saltar al contenido",
        "nav_label": "Principal",
        "nav_work": "Trabajos",
        "nav_services": "Servicios",
        "nav_faq": "FAQ",
        "cta": "Contacto",
        "lang_label": "Idioma",
        "h1": "Mezcla, mastering y producción musical de EDM para artistas y sellos.",
        "about": "Pulso Studios es un estudio profesional de mezcla, masterización y producción musical para artistas y sellos de EDM. Convertimos ideas en bruto en grabaciones pulidas, listas para DSPs y listas para la pista de baile, mediante una ingeniería de sonido precisa y una atención meticulosa al detalle.",
        "marquee": ["listo para DSPs", "listo para el club"],
        "services_h2": "Servicios",
        "services": [
            ("Mezcla", "Mezcla profesional para temas de EDM y música electrónica."),
            ("Masterización", "Masterización lista para DSPs y para el club, para lanzamientos de música electrónica."),
            ("Producción musical", "Servicios de producción musical a medida para artistas de EDM."),
        ],
        "work_h2": "Trabajos seleccionados",
        "proj1_service": "Mezcla y Masterización",
        "proj2_service": "Mezcla",
        "proj1_alt": "Portada de When I Close My Eyes (ARLA &amp; BAAT Remix)",
        "proj2_alt": "Portada del EP Dreamlight de BAAT",
        "faq_h2": "Preguntas frecuentes",
        "faq": [
            ("¿Qué hace Pulso Studios?", "Pulso Studios es un estudio de mezcla, masterización y producción musical especializado en EDM, que ayuda a artistas y sellos a convertir sus pistas en un sonido pulido, profesional y listo para publicar."),
            ("¿Con qué géneros trabaja Pulso Studios?", "Pulso Studios trabaja principalmente con EDM y géneros de música electrónica relacionados, mezclando y masterizando pistas para productores, artistas y sellos."),
            ("¿Ofrecéis la mezcla y la masterización como servicios separados?", "Sí. Pulso Studios ofrece la mezcla y la masterización como servicios independientes o combinados, según lo que necesite la pista."),
            ("¿Cómo puedo enviar mis pistas a Pulso Studios?", "Puedes ponerte en contacto a través del formulario de esta página o escribir a contact@pulso-studios.com con los detalles de tu proyecto."),
        ],
        "contact_h2": "Contacto",
        "or_email": "O envía un email a",
        "label_name": "Tu nombre",
        "label_email": "Tu email",
        "label_message": "Mensaje",
        "submit": "Enviar",
        "mail_subject": "Nuevo mensaje de",
        "mail_opening": "Abriendo tu cliente de correo...",
        "org_description": "Pulso Studios es un estudio profesional de mezcla, masterización y producción musical para artistas y sellos de EDM.",
        "knows": ["Mezcla de EDM", "Masterización", "Producción musical", "Música electrónica"],
    },
}


def letters(word, start):
    return "".join(
        f'<span style="--i:{start + i}">{ch}</span>' for i, ch in enumerate(word)
    )


def json_ld(lang, t):
    url = SITE + t["path"]
    graph = [
        {
            "@type": "Organization",
            "@id": SITE + "/#organization",
            "name": "Pulso Studios",
            "url": SITE + "/",
            "logo": {
                "@type": "ImageObject",
                "url": SITE + "/assets/img/pulso-studios-logo-512.png",
                "width": 512,
                "height": 512,
            },
            "image": SITE + "/og-image.jpg",
            "description": t["org_description"],
            "email": EMAIL,
            "areaServed": "Worldwide",
            "knowsAbout": t["knows"],
            "knowsLanguage": ["en", "es"],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer service",
                "email": EMAIL,
                "availableLanguage": ["English", "Spanish"],
            },
            "makesOffer": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": name,
                        "description": desc,
                        "provider": {"@id": SITE + "/#organization"},
                        "areaServed": "Worldwide",
                    },
                }
                for name, desc in t["services"]
            ],
        },
        {
            "@type": "WebSite",
            "@id": SITE + "/#website",
            "url": SITE + "/",
            "name": "Pulso Studios",
            "publisher": {"@id": SITE + "/#organization"},
            "inLanguage": ["en", "es"],
        },
        {
            "@type": "WebPage",
            "@id": url + "#webpage",
            "url": url,
            "name": t["title"],
            "description": t["description"],
            "isPartOf": {"@id": SITE + "/#website"},
            "about": {"@id": SITE + "/#organization"},
            "inLanguage": lang,
            "primaryImageOfPage": SITE + "/og-image.jpg",
        },
        {
            "@type": "FAQPage",
            "@id": url + "#faq",
            "inLanguage": lang,
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in t["faq"]
            ],
        },
    ]
    data = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(data, ensure_ascii=False, indent=2)


def page(lang):
    t = STRINGS[lang]
    url = SITE + t["path"]
    en_cur = ' aria-current="true"' if lang == "en" else ""
    es_cur = ' aria-current="true"' if lang == "es" else ""

    services = "\n".join(
        f"""        <li>
          <a class="service" href="#contact" data-reveal style="--d:{i}">
            <h3 class="service-name">{name}</h3>
            <p class="service-desc">{desc}</p>
            <span class="service-go" aria-hidden="true">{t['cta']}</span>
          </a>
        </li>"""
        for i, (name, desc) in enumerate(t["services"])
    )

    faq = "\n".join(
        f"""          <div class="faq-item" data-reveal style="--d:{i}">
            <h3 class="faq-question">
              <button type="button" class="faq-trigger" id="faq-q{i + 1}" aria-controls="faq-a{i + 1}" aria-expanded="true">
                <span>{q}</span><span class="faq-icon" aria-hidden="true"></span>
              </button>
            </h3>
            <div class="faq-panel is-open" id="faq-a{i + 1}" role="region" aria-labelledby="faq-q{i + 1}">
              <div class="faq-panel-inner"><p class="faq-answer">{a}</p></div>
            </div>
          </div>"""
        for i, (q, a) in enumerate(t["faq"])
    )

    group = "".join(
        ('<span class="outline">' if i % 2 else "<span>") + w + "</span><i></i>"
        for i, w in enumerate(t["marquee"] * 2)
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title'].replace('&', '&amp;')}</title>
  <meta name="description" content="{t['description']}" />
  <meta name="author" content="Pulso Studios" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" hreflang="en" href="{SITE}/" />
  <link rel="alternate" hreflang="es" href="{SITE}/es/" />
  <link rel="alternate" hreflang="x-default" href="{SITE}/" />

  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

  <!-- Open Graph -->
  <meta property="og:site_name" content="Pulso Studios" />
  <meta property="og:title" content="{t['og_title'].replace('&', '&amp;')}" />
  <meta property="og:description" content="{t['og_description']}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="{t['locale']}" />
  <meta property="og:locale:alternate" content="{t['alt_locale']}" />
  <meta property="og:image" content="{SITE}/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{t['og_alt']}" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t['og_title'].replace('&', '&amp;')}" />
  <meta name="twitter:description" content="{t['og_description']}" />
  <meta name="twitter:image" content="{SITE}/og-image.jpg" />

  <link rel="preload" href="/assets/fonts/AlteHaasGrotesk-Bold.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/assets/fonts/AlteHaasGrotesk-Regular.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/assets/css/site.css" />
  <script>document.documentElement.classList.add('js');</script>

  <!-- Structured data: Organization, WebSite, WebPage, FAQPage -->
  <script type="application/ld+json">
{json_ld(lang, t)}
  </script>
</head>
<body>

  <a class="skip-link" href="#about">{t['skip']}</a>

  <header>
    <nav class="nav" aria-label="{t['nav_label']}">
      <a class="nav-brand" href="#hero">pulso studios</a>
      <ul class="nav-links">
        <li class="nav-section"><a href="#services">{t['nav_services']}</a></li>
        <li class="nav-section"><a href="#work">{t['nav_work']}</a></li>
        <li class="nav-section"><a href="#faq">{t['nav_faq']}</a></li>
        <li class="nav-lang" aria-label="{t['lang_label']}">
          <a href="/" lang="en" hreflang="en"{en_cur}>EN</a><span aria-hidden="true">/</span><a href="/es/" lang="es" hreflang="es"{es_cur}>ES</a>
        </li>
        <li><a class="nav-cta" href="#contact">{t['cta']}</a></li>
      </ul>
    </nav>
  </header>

  <main>

    <!-- HERO -->
    <section id="hero" aria-label="Pulso Studios">
      <div class="hero-mark">
        <div class="pulse" aria-hidden="true"><div class="pulse-scroll"><div class="pulse-ring"></div><div class="pulse-dot"></div></div></div>
        <div class="wordmark" role="img" aria-label="Pulso Studios">
          <span class="wordmark-line" aria-hidden="true">{letters('pulso', 0)}</span>
          <span class="wordmark-line" aria-hidden="true">{letters('studios', 4)}</span>
        </div>
      </div>
      <div class="hero-row">
        <h1 class="hero-sub">{t['h1']}</h1>
      </div>
    </section>

    <!-- ABOUT -->
    <section id="about" aria-label="Pulso Studios">
      <div class="wrap">
        <p class="about-text">{t['about']}</p>
      </div>
    </section>

    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <div class="marquee-group">{group}</div>
        <div class="marquee-group">{group}</div>
      </div>
    </div>

    <!-- SERVICES -->
    <section id="services" aria-labelledby="services-h">
      <div class="wrap">
        <h2 class="h2" id="services-h" data-reveal>{t['services_h2']}</h2>
        <ul class="services-list">
{services}
        </ul>
      </div>
    </section>

    <!-- WORK -->
    <section id="work" aria-labelledby="work-h">
      <div class="wrap">
        <h2 class="h2" id="work-h" data-reveal>{t['work_h2']}</h2>
        <div class="projects">

          <article class="project" data-wipe>
            <div class="project-media">
              <div class="project-media-inner">
                <picture>
                  <source type="image/webp" srcset="/assets/img/when-i-close-my-eyes-arla-baat-remix-800.webp 800w, /assets/img/when-i-close-my-eyes-arla-baat-remix-1400.webp 1400w" sizes="(max-width: 767px) 92vw, 56vw" />
                  <img class="project-img" src="/assets/img/when-i-close-my-eyes-arla-baat-remix-1400.jpg" alt="{t['proj1_alt']}" width="1400" height="1400" loading="lazy" decoding="async" />
                </picture>
              </div>
            </div>
            <div class="project-info" data-reveal>
              <h3 class="project-title">When I Close My Eyes (ARLA &amp; BAAT Remix)</h3>
              <p class="project-artist">DALEXO, Adrian Fyrla, Boix &amp; Breakloop, GIPX</p>
              <p class="project-service">{t['proj1_service']}</p>
            </div>
          </article>

          <article class="project" data-wipe>
            <div class="project-media">
              <div class="project-media-inner">
                <picture>
                  <source type="image/webp" srcset="/assets/img/dreamlight-ep-baat-800.webp 800w, /assets/img/dreamlight-ep-baat-1400.webp 1400w" sizes="(max-width: 767px) 92vw, 32vw" />
                  <img class="project-img" src="/assets/img/dreamlight-ep-baat-1400.jpg" alt="{t['proj2_alt']}" width="1400" height="1400" loading="lazy" decoding="async" />
                </picture>
              </div>
            </div>
            <div class="project-info" data-reveal>
              <h3 class="project-title">Dreamlight EP</h3>
              <p class="project-artist">BAAT</p>
              <p class="project-service">{t['proj2_service']}</p>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" aria-labelledby="faq-h">
      <div class="wrap faq-grid">
        <h2 class="h2" id="faq-h" data-reveal>{t['faq_h2']}</h2>
        <div class="faq-list">
{faq}
        </div>
      </div>
    </section>

    <!-- CONTACT -->
    <section id="contact" class="invert" aria-labelledby="contact-h">
      <div class="wrap">
        <div class="contact-grid">
          <div>
            <h2 class="h2 contact-heading" id="contact-h" data-reveal>{t['contact_h2']}</h2>
            <p class="contact-alt" data-reveal style="--d:1">{t['or_email']} <a class="link" href="mailto:{EMAIL}">{EMAIL}</a></p>
          </div>
          <form class="contact-form" id="contactForm" data-reveal style="--d:2" data-subject="{t['mail_subject']}" data-opening="{t['mail_opening']}">
            <div class="field">
              <label for="f-name">{t['label_name']}</label>
              <input type="text" class="contact-field" id="f-name" name="name" required autocomplete="name" />
            </div>
            <div class="field">
              <label for="f-email">{t['label_email']}</label>
              <input type="email" class="contact-field" id="f-email" name="email" required autocomplete="email" />
            </div>
            <div class="field">
              <label for="f-message">{t['label_message']}</label>
              <textarea class="contact-field" id="f-message" name="message" rows="4"></textarea>
            </div>
            <button type="submit" class="btn btn--solid contact-submit">{t['submit']}</button>
            <p class="contact-status" id="contactStatus" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>

  </main>

  <footer class="invert">
    <div class="wrap footer-inner">
      <span class="footer-brand">pulso studios</span>
      <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>
      <span>&copy; <span id="year">2026</span> Pulso Studios</span>
    </div>
  </footer>

  <script src="/assets/js/site.js" defer></script>
</body>
</html>
"""



# ─────────────────────────────────────────────────────────────────────────────
# Private showcase pages (not indexed, not in the sitemap, not linked from home)
# ─────────────────────────────────────────────────────────────────────────────

# Set enabled to True to ask for the password before showing the page.
# Note: this check runs in the browser, so it keeps casual visitors out but it
# is not real security (the password can be read in the page source).
GATE = {"enabled": False, "password": "pulso2026"}

AUDIO_BASE = "/versions-pel-directe/audio/"
TRACKS = [
    # (file, title, genre, duration in seconds)
    ("track-01.mp3", "Uptown Funk", "Tech House", 107.5),
    ("track-02.mp3", "L'Amour Toujours", "EDM", 68.6),
    ("track-03.mp3", "NUEVAYoL", "Afro House", 33.2),
    ("track-04.mp3", "Ja Dormiré", "Techno", 30.0),
    ("track-05.mp3", "Mediterrània", "Trap", 27.0),
]

VERSIONS = {
    "ca": {
        "dir": "versions-pel-directe",
        "home": "/",
        "page_title": "Pulso Studios — Versions pel directe",
        "share_description": "Una selecció de versions produïdes, mesclades i masteritzades a Pulso Studios.",
        "title_lines": ["versions", "pel directe"],
        "title_label": "Versions pel directe",
        "title_vw": ("15vw", "17vw"),
        "intro": "Una selecció de versions produïdes, mesclades i masteritzades a Pulso Studios perquè puguis escoltar com sonarà el teu proper directe.",
        "cta_listen": "Escolta-les",
        "cta_contact": "Contacte",
        "tracks_h2": "Les versions",
        "play": "Reprodueix",
        "pause": "Pausa",
        "seek": "Posició de",
        "audio_error": "No s'ha pogut carregar l'àudio. Torna-ho a provar.",
        "contact_h2": "Tens algun dubte?",
        "contact_note": "Escriu-nos i en parlem.",
        "skip": "Salta al contingut",
        "nav_label": "Principal",
        "lang_label": "Idioma",
        "gate_title": "Identifica't",
        "gate_label": "Contrasenya",
        "gate_submit": "Entrar",
        "gate_wrong": "Contrasenya incorrecta",
    },
    "es": {
        "dir": "versiones-para-el-directo",
        "home": "/es/",
        "page_title": "Pulso Studios — Versiones para el directo",
        "share_description": "Una selección de versiones producidas, mezcladas y masterizadas en Pulso Studios.",
        "title_lines": ["versiones", "para el directo"],
        "title_label": "Versiones para el directo",
        "title_vw": ("12vw", "13.2vw"),
        "intro": "Una selección de versiones producidas, mezcladas y masterizadas en Pulso Studios para que puedas escuchar cómo sonará tu próximo directo.",
        "cta_listen": "Escúchalas",
        "cta_contact": "Contacto",
        "tracks_h2": "Las versiones",
        "play": "Reproducir",
        "pause": "Pausar",
        "seek": "Posición de",
        "audio_error": "No se ha podido cargar el audio. Vuelve a intentarlo.",
        "contact_h2": "¿Tienes alguna duda?",
        "contact_note": "Escríbenos y lo hablamos.",
        "skip": "Saltar al contenido",
        "nav_label": "Principal",
        "lang_label": "Idioma",
        "gate_title": "Identifícate",
        "gate_label": "Contraseña",
        "gate_submit": "Entrar",
        "gate_wrong": "Contraseña incorrecta",
    },
}


def title_letters(lines):
    out, i = [], 0
    for line in lines:
        spans = []
        for ch in line:
            if ch == " ":
                spans.append(f'<span class="sp" style="--i:{i}"></span>')
            else:
                spans.append(f'<span style="--i:{i}">{ch}</span>')
            i += 1
        out.append(f'<span class="wordmark-line" aria-hidden="true">{"".join(spans)}</span>')
        i = max(0, i - 4)
    return "\n          ".join(out)


def clock(seconds):
    s = round(seconds)
    return f"{s // 60}:{s % 60:02d}"


def versions_page(lang):
    t = VERSIONS[lang]
    url = f"{SITE}/{t['dir']}/"
    ca_cur = ' aria-current="true"' if lang == "ca" else ""
    es_cur = ' aria-current="true"' if lang == "es" else ""
    genres = []
    for _, _, genre, _ in TRACKS:
        if genre not in genres:
            genres.append(genre)
    group = "".join(
        ('<span class="outline">' if i % 2 else "<span>") + g.lower() + "</span><i></i>"
        for i, g in enumerate(genres)
    )
    rows = "\n".join(
        f"""          <li class="track" data-duration="{dur}" data-reveal style="--d:{i}">
            <button type="button" class="track-play" aria-label="{t['play']} {title}"></button>
            <h3 class="track-title">{title}</h3>
            <p class="track-genre">{genre}</p>
            <p class="track-time"><span class="track-current">0:00</span><span class="track-sep"> / </span><span class="track-total">{clock(dur)}</span></p>
            <input type="range" class="track-seek" min="0" max="100" step="0.1" value="0" aria-label="{t['seek']} {title}" />
            <p class="track-error" role="alert"></p>
            <audio preload="none" src="{AUDIO_BASE}{f}"></audio>
          </li>"""
        for i, (f, title, genre, dur) in enumerate(TRACKS)
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['page_title']}</title>

  <!-- Private page: keep it out of search engines. Do not add it to sitemap.xml or robots.txt. -->
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex" />
  <meta name="googlebot" content="noindex, nofollow, noarchive, nosnippet, noimageindex" />
  <meta name="referrer" content="no-referrer" />

  <!-- Link preview when the URL is shared by WhatsApp or email (not SEO) -->
  <meta property="og:site_name" content="Pulso Studios" />
  <meta property="og:title" content="{t['page_title']}" />
  <meta property="og:description" content="{t['share_description']}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />

  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

  <link rel="preload" href="/assets/fonts/AlteHaasGrotesk-Bold.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/assets/fonts/AlteHaasGrotesk-Regular.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/assets/css/site.css" />
  <link rel="stylesheet" href="/assets/css/versions.css" />
  <script>
    // ---- PASSWORD GATE: change it in _build/build.py (GATE) or right here ----
    window.PULSO_GATE = {json.dumps(GATE)};
    (function () {{
      var d = document.documentElement, ok = false;
      d.classList.add('js');
      try {{ ok = sessionStorage.getItem('psv_ok') === '1'; }} catch (e) {{}}
      if (window.PULSO_GATE.enabled && !ok) d.classList.add('gated');
    }})();
  </script>
</head>
<body style="--title-vw:{t['title_vw'][0]};--title-vw-m:{t['title_vw'][1]}">

  <div id="gate">
    <h1 class="gate-title">{t['gate_title']}</h1>
    <form class="gate-form" id="gateForm" autocomplete="off" data-wrong="{t['gate_wrong']}">
      <div class="field">
        <label for="gatePass">{t['gate_label']}</label>
        <input type="password" class="contact-field" id="gatePass" autocomplete="off" required />
      </div>
      <button type="submit" class="btn btn--solid contact-submit">{t['gate_submit']}</button>
      <p class="gate-error" id="gateError" role="alert"></p>
    </form>
  </div>

  <a class="skip-link" href="#tracks">{t['skip']}</a>

  <header>
    <nav class="nav" aria-label="{t['nav_label']}">
      <a class="nav-brand" href="{t['home']}">pulso studios</a>
      <ul class="nav-links">
        <li class="nav-lang" aria-label="{t['lang_label']}">
          <a href="/versions-pel-directe/" lang="ca" hreflang="ca"{ca_cur}>CA</a><span aria-hidden="true">/</span><a href="/versiones-para-el-directo/" lang="es" hreflang="es"{es_cur}>ES</a>
        </li>
        <li><a class="nav-cta" href="#contact">{t['cta_contact']}</a></li>
      </ul>
    </nav>
  </header>

  <main>

    <section id="hero" class="v-hero">
      <div class="hero-mark">
        <div class="pulse" aria-hidden="true"><div class="pulse-scroll"><div class="pulse-ring"></div><div class="pulse-dot"></div></div></div>
        <h1 class="wordmark v-title" aria-label="{t['title_label']}">
          {title_letters(t['title_lines'])}
        </h1>
      </div>
      <div class="hero-row">
        <p class="hero-sub">{t['intro']}</p>
        <div class="hero-cta">
          <a class="btn btn--solid" href="#tracks">{t['cta_listen']}</a>
        </div>
      </div>
    </section>

    <section id="tracks" aria-labelledby="tracks-h">
      <div class="wrap">
        <h2 class="visually-hidden" id="tracks-h">{t['tracks_h2']}</h2>
        <ul class="tracks" data-play="{t['play']}" data-pause="{t['pause']}" data-error="{t['audio_error']}">
{rows}
        </ul>
      </div>
    </section>

    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <div class="marquee-group">{group}</div>
        <div class="marquee-group">{group}</div>
      </div>
    </div>

    <section id="contact" class="invert v-contact" aria-labelledby="contact-h">
      <div class="wrap">
        <h2 class="h2 contact-heading" id="contact-h" data-reveal>{t['contact_h2']}</h2>
        <p class="v-contact-note" data-reveal style="--d:1">{t['contact_note']}</p>
        <a class="link v-contact-mail" data-reveal style="--d:2" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </section>

  </main>

  <footer class="invert">
    <div class="wrap footer-inner">
      <a class="footer-brand" href="{t['home']}" style="text-decoration:none">pulso studios</a>
      <span>&copy; <span id="year">2026</span> Pulso Studios</span>
    </div>
  </footer>

  <script src="/assets/js/site.js" defer></script>
  <script src="/assets/js/versions.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page("en"), encoding="utf-8")
    (ROOT / "es").mkdir(exist_ok=True)
    (ROOT / "es" / "index.html").write_text(page("es"), encoding="utf-8")
    for lang, t in VERSIONS.items():
        (ROOT / t["dir"]).mkdir(exist_ok=True)
        (ROOT / t["dir"] / "index.html").write_text(versions_page(lang), encoding="utf-8")
    print("built index.html, es/index.html and the two private showcase pages")
