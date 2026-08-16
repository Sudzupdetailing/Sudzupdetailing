#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sudz Up Detailing — static site generator.

Emits plain HTML into the repo root. No build step is required to deploy:
GitHub Pages serves the committed output directly. Re-run this script after
editing content in _build/*.py, then commit the result.

    python3 _build/build.py
"""
import os, sys, json, html, datetime, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from cities import CITIES
from services import SERVICES
from guides import GUIDES

SITE  = "https://sudzupdetail.com"
BIZ   = "Sudz Up Detailing LLC"
TEL   = "414-286-1609"
TELE  = "+1-414-286-1609"
EMAIL = "SudzUpdetail2025@outlook.com"
ADDR  = "2948 WI-83"
CITY  = "Hartford"
REGION= "WI"
ZIP   = "53027"
LAT, LNG = 43.3219, -88.3762
TODAY = datetime.date.today().isoformat()
MEDIA_UPLOAD = "2026-06-25T03:10:29-04:00"

e = html.escape
PAGES = []   # (url_path, priority, changefreq, extra_xml)


# ────────────────────────────────────────────────────────────── schema helpers

def org_node():
    return {"@type": "Organization", "@id": f"{SITE}/#organization", "name": BIZ,
            "url": SITE + "/", "telephone": TELE, "email": EMAIL,
            "logo": {"@type": "ImageObject", "@id": f"{SITE}/#logo",
                     "url": f"{SITE}/img/opt/logo-512.png", "width": 512, "height": 512,
                     "caption": BIZ},
            "image": {"@id": f"{SITE}/#logo"}, "sameAs": []}


def business_node():
    return {
        "@type": ["LocalBusiness", "AutoWash"], "@id": f"{SITE}/#business", "name": BIZ,
        "parentOrganization": {"@id": f"{SITE}/#organization"},
        "description": ("Professional interior and exterior auto detailing in Hartford, Wisconsin. "
                        "Detail packages for cars, trucks and SUVs serving Hartford and the "
                        "surrounding Washington County area."),
        "url": SITE + "/", "telephone": TELE, "email": EMAIL,
        "image": {"@id": f"{SITE}/#logo"}, "logo": {"@id": f"{SITE}/#logo"},
        "address": {"@type": "PostalAddress", "streetAddress": ADDR, "addressLocality": CITY,
                    "addressRegion": REGION, "postalCode": ZIP, "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=2948+WI-83+Hartford+WI+53027",
        "areaServed": [{"@type": "City", "name": c["name"],
                        "containedInPlace": {"@type": "AdministrativeArea",
                                             "name": f'{c["county"]}, Wisconsin'}} for c in CITIES],
        "serviceArea": {"@type": "GeoCircle",
                        "geoMidpoint": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
                        "geoRadius": "40000"},
        "priceRange": "$135-$250", "currenciesAccepted": "USD",
        "paymentAccepted": "Cash, Credit Card, Debit Card",
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "08:00", "closes": "18:00"}],
        "knowsAbout": ["auto detailing", "interior car detailing", "exterior wash and polish",
                       "stain removal", "odor removal", "road salt corrosion", "vehicle cleaning"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Auto Detailing Services",
            "itemListElement": [
                {"@type": "Offer", "name": "Sudz Quick Clean", "priceCurrency": "USD", "price": "135",
                 "availability": "https://schema.org/InStock",
                 "itemOffered": {"@type": "Service", "name": "Sudz Quick Clean",
                                 "serviceType": "Interior Auto Detailing",
                                 "url": f"{SITE}/services/interior-car-detailing/",
                                 "provider": {"@id": f"{SITE}/#business"},
                                 "description": ("Interior vacuum, vinyl/rubber/plastic treatment, spot stain "
                                                 "removal, door jambs cleaned and windows cleaned. $135 for cars, "
                                                 "$150 for SUVs and trucks.")}},
                {"@type": "Offer", "name": "Sudz Up VIP Clean", "priceCurrency": "USD", "price": "200",
                 "availability": "https://schema.org/InStock",
                 "itemOffered": {"@type": "Service", "name": "Sudz Up VIP Clean",
                                 "serviceType": "Full Interior and Exterior Auto Detailing",
                                 "url": f"{SITE}/services/full-interior-exterior-detail/",
                                 "provider": {"@id": f"{SITE}/#business"},
                                 "description": ("Complete interior detail plus exterior wash and polish, wheels "
                                                 "cleaned and tires shined. $200 for cars, $250 for SUVs and "
                                                 "trucks.")}}]},
        "sameAs": []}


def website_node():
    return {"@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/", "name": BIZ,
            "publisher": {"@id": f"{SITE}/#organization"}, "inLanguage": "en-US"}


def crumb_node(url, trail):
    return {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": SITE + p} for i, (n, p) in enumerate(trail)]}


def faq_node(url, pairs):
    return {"@type": "FAQPage", "@id": f"{url}#faq", "isPartOf": {"@id": f"{url}#webpage"},
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


# ────────────────────────────────────────────────────────────── html fragments

NAV_LINKS = [("Services", "/services/"), ("Service Area", "/auto-detailing/"),
             ("Pricing", "/pricing/"), ("Guides", "/guides/"), ("About", "/about/")]


def nav(active=""):
    items = "".join(
        f'    <li><a href="{p}"{" aria-current=\"page\"" if p == active else ""}>{e(n)}</a></li>\n'
        for n, p in NAV_LINKS)
    return f'''<nav>
  <a href="/" aria-label="{e(BIZ)} home"><img src="/img/opt/logo-400.webp" alt="{e(BIZ)} — auto detailing in Hartford, Wisconsin" class="nav-logo" width="400" height="400" fetchpriority="high" decoding="async" /></a>
  <ul class="nav-links" id="navLinks">
{items}    <li><a href="/contact/" class="nav-cta">Book Now</a></li>
  </ul>
  <button class="nav-toggle" id="navToggle" aria-label="Open menu">
    <span></span><span></span><span></span>
  </button>
</nav>
'''


def crumbs_html(trail):
    out = ['<div class="crumbs"><nav aria-label="Breadcrumb"><ol>']
    for i, (n, p) in enumerate(trail):
        last = i == len(trail) - 1
        out.append(f'<li><span aria-current="page">{e(n)}</span></li>' if last
                   else f'<li><a href="{p}">{e(n)}</a></li>')
    out.append('</ol></nav></div>')
    return "".join(out)


def glance_html(pairs):
    cells = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in pairs)
    return f'<dl class="glance">{cells}</dl>'


def prose_html(sections):
    out = []
    for headline, paras in sections:
        out.append(f'<h2>{e(headline)}</h2>')
        out.extend(f'<p>{p}</p>' for p in paras)
    return "\n".join(out)


def faq_html(pairs):
    items = "".join(
        f'''      <div class="faq-item">
        <button type="button" class="faq-q" aria-expanded="false" aria-controls="fa{i}" id="fq{i}">{e(q)}</button>
        <div class="faq-a" id="fa{i}" role="region" aria-labelledby="fq{i}">{e(a)}</div>
      </div>\n''' for i, (q, a) in enumerate(pairs, 1))
    return f'''<section id="faq" aria-labelledby="faq-title" class="prose">
  <h2 id="faq-title">Frequently asked questions</h2>
  <div class="faq-wrap">
{items}  </div>
</section>'''


def cta_html(heading, body):
    return f'''<section class="ctastrip">
  <h2>{e(heading)}</h2>
  <p>{e(body)}</p>
  <div class="contact-btns">
    <a href="tel:+14142861609" class="btn-contact btn-contact-call">Call &mdash; {TEL}</a>
    <a href="sms:+14142861609" class="btn-contact btn-contact-text">Text &mdash; {TEL}</a>
  </div>
</section>'''


def related_html(heading, links):
    lis = "".join(f'<li><a href="{p}">{e(n)}</a></li>' for n, p in links)
    return f'<section class="related"><h2>{e(heading)}</h2><ul>{lis}</ul></section>'


FOOTER = f'''<footer>
  <div class="footer-inner">
    <div>
      <img src="/img/opt/logo-400.webp" alt="{e(BIZ)}" class="footer-logo" width="400" height="400" loading="lazy" decoding="async" />
      <div class="footer-meta">Hartford, Wisconsin &middot; {TEL}</div>
    </div>
    <div class="footer-social">
      <address class="footer-meta" style="font-style:normal;">
        <a href="tel:+14142861609">{TEL}</a><br />
        {ADDR}, {CITY}, {REGION} {ZIP}
      </address>
    </div>
  </div>
  <div class="footer-copy">&copy; 2026 {e(BIZ)} &middot; Hartford, WI &middot; All rights reserved.</div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, meta, graph, body, active="", extra_head=""):
    """Write a page to <path>/index.html (or root index.html when path == '/')."""
    url = SITE + path
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(meta)}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-video-preview:-1, max-snippet:-1" />
  <meta name="theme-color" content="#0A0A0A" />
  <meta name="author" content="{e(BIZ)}" />
  <meta name="geo.region" content="US-WI" />
  <meta name="geo.placename" content="Hartford, Wisconsin" />
  <meta name="geo.position" content="{LAT};{LNG}" />
  <meta name="ICBM" content="{LAT}, {LNG}" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="/img/opt/favicon-32.png" />
  <link rel="apple-touch-icon" href="/img/opt/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{e(BIZ)}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(meta)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/img/opt/logo-512.png" />
  <meta property="og:image:width" content="512" />
  <meta property="og:image:height" content="512" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(title)}" />
  <meta name="twitter:description" content="{e(meta)}" />
  <meta name="twitter:image" content="{SITE}/img/opt/logo-512.png" />
  <link rel="preload" href="/img/opt/logo-400.webp" as="image" type="image/webp" fetchpriority="high" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="/assets/site.css" />
  <link rel="stylesheet" media="print" onload="this.media='all';this.onload=null" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500&display=swap" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500&display=swap" /></noscript>
{extra_head}  <script type="application/ld+json">
{json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
{nav(active)}
{body}
{FOOTER}'''
    outdir = ROOT if path == "/" else os.path.join(ROOT, path.strip("/"))
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    return url


# ────────────────────────────────────────────────────────────────────── builds

def build_home():
    path = "/"
    url = SITE + "/"
    vids = [("01", "Interior Deep Clean in Progress — Hartford, WI",
             "Sudz Up Detailing performing an interior deep clean: vacuuming, vinyl/rubber/plastic treatment and spot stain removal on a customer vehicle in Hartford, Wisconsin.",
             "PT20S", 540, 960, "Interior deep clean in progress"),
            ("02", "Full VIP Detail Walkthrough — Washington County, WI",
             "A walkthrough of the Sudz Up VIP Clean: complete interior detail plus exterior wash, polish, wheel cleaning and tire shine.",
             "PT38S", 540, 960, "Full VIP detail walkthrough"),
            ("03", "Seat and Carpet Stain Removal — Hartford Auto Detailing",
             "Close-up of spot stain removal and carpet extraction during a Sudz Up Detailing interior service.",
             "PT20S", 540, 960, "Seat and carpet stain removal"),
            ("04", "Exterior Wash and Polish Finish — Sudz Up Detailing",
             "Exterior wash, polish and tire shine finish on a vehicle detailed by Sudz Up Detailing in Hartford, WI.",
             "PT10S", 1280, 720, "Exterior wash and polish finish")]
    photos = [("interior-dash", 1125, 844, 1125, "Dashboard and center console after an interior auto detail in Hartford, WI", "Interior Detail"),
              ("interior-seats-front", 1125, 844, 1125, "Front seats cleaned and conditioned by Sudz Up Detailing in Hartford, WI", "Front Seats"),
              ("interior-seats-rear", 1125, 844, 1125, "Rear seats vacuumed and shampooed during a Hartford, WI auto detail", "Rear Seats"),
              ("interior-rear-angle", 1126, 1500, 1126, "Rear interior cargo area detailed by Sudz Up Detailing, Hartford WI", "Interior Clean")]

    graph = [org_node(), business_node(), website_node(),
             {"@type": "WebPage", "@id": f"{url}#webpage", "url": url,
              "name": f"Auto Detailing in Hartford, WI | {BIZ}",
              "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#business"},
              "primaryImageOfPage": {"@id": f"{SITE}/#logo"}, "inLanguage": "en-US",
              "breadcrumb": {"@id": f"{url}#breadcrumb"}},
             crumb_node(url, [("Home", "/")])]
    for vid, name, desc, dur, w, h, _ in vids:
        graph.append({"@type": "VideoObject", "@id": f"{SITE}/#video-{vid}", "name": name,
                      "description": desc, "thumbnailUrl": [f"{SITE}/img/poster/detail-{vid}.jpg"],
                      "uploadDate": MEDIA_UPLOAD, "duration": dur,
                      "contentUrl": f"{SITE}/video/detail-{vid}.mp4", "embedUrl": f"{SITE}/#gallery",
                      "width": w, "height": h, "isFamilyFriendly": True, "inLanguage": "en-US",
                      "publisher": {"@id": f"{SITE}/#organization"}, "about": {"@id": f"{SITE}/#business"},
                      "contentLocation": {"@type": "Place", "name": "Hartford, Wisconsin"}})
    for slug, w, h, nat, cap, _ in photos:
        graph.append({"@type": "ImageObject", "@id": f"{SITE}/#img-{slug}",
                      "contentUrl": f"{SITE}/img/opt/{slug}-{nat}.jpg",
                      "url": f"{SITE}/img/opt/{slug}-{nat}.jpg", "width": w, "height": h,
                      "caption": cap, "creator": {"@id": f"{SITE}/#organization"},
                      "contentLocation": {"@type": "Place", "name": "Hartford, Wisconsin"}})
    home_faq = [
        ("How much does auto detailing cost in Hartford, WI?",
         "The Sudz Quick Clean is $135 for cars and $150 for SUVs and trucks. The Sudz Up VIP Clean is $200 for cars and $250 for SUVs and trucks. Final pricing depends on vehicle size and condition. Call or text 414-286-1609 for a no-obligation quote."),
        ("What is included in the VIP detail package?",
         "The Sudz Up VIP Clean includes an interior vacuum, vinyl/rubber/plastic treatment, spot stain removal, door jambs cleaned and windows cleaned, plus an exterior wash and polish, wheels cleaned and tires shined."),
        ("What areas does Sudz Up Detailing serve?",
         "Sudz Up Detailing is based in Hartford, Wisconsin and serves Hartford, Slinger, Richfield, West Bend, Jackson, Allenton, Germantown, Kewaskum, Colgate and Erin in Washington County, plus Rubicon and Neosho in Dodge County."),
        ("How long does an auto detail take?",
         "The Sudz Quick Clean typically takes about one to two hours. The Sudz Up VIP Clean is a full interior and exterior service and generally takes longer depending on vehicle size and condition."),
        ("Do you detail trucks and SUVs?",
         "Yes. Sudz Up Detailing details cars, trucks and SUVs. Pricing for SUVs and trucks is $150 for the Sudz Quick Clean and $250 for the Sudz Up VIP Clean."),
        ("How do I book an auto detail with Sudz Up Detailing?",
         "Call or text 414-286-1609, or email SudzUpdetail2025@outlook.com to schedule your appointment and get a no-obligation quote."),
    ]
    graph.append(faq_node(url, home_faq))

    photo_html = "\n".join(
        f'''    <button type="button" class="gallery-photo" onclick="openLightbox('/img/opt/{s}-{nat}.jpg','{e(cap)}')" aria-label="Enlarge photo: {e(lbl)}">
      <picture>
        <source type="image/webp" sizes="(max-width:768px) 50vw, 25vw" srcset="/img/opt/{s}-480.webp 480w, /img/opt/{s}-800.webp 800w, /img/opt/{s}-{nat}.webp {nat}w" />
        <img src="/img/opt/{s}-800.jpg" sizes="(max-width:768px) 50vw, 25vw" srcset="/img/opt/{s}-480.jpg 480w, /img/opt/{s}-800.jpg 800w, /img/opt/{s}-{nat}.jpg {nat}w" alt="{e(cap)}" width="{w}" height="{h}" loading="lazy" decoding="async" />
      </picture>
      <span class="gallery-photo-label">{e(lbl)}</span>
    </button>''' for s, w, h, nat, cap, lbl in photos)

    video_html = "\n".join(
        f'''    <div class="gallery-video" id="vid{i}wrap">
      <video id="vid{i}" src="/video/detail-{vid}.mp4" poster="/img/poster/detail-{vid}.jpg" width="{w}" height="{h}" playsinline preload="none" loop muted aria-label="{e(short)} — Sudz Up Detailing, Hartford WI"></video>
      <button type="button" class="video-play-hint" onclick="toggleVideo('vid{i}','vid{i}wrap')" aria-label="Play video: {e(short)}">
        <span class="play-icon"><svg width="13" height="15" viewBox="0 0 13 15" fill="black" aria-hidden="true"><path d="M0 0l13 7.5L0 15z"/></svg></span>
      </button>
    </div>''' for i, (vid, _, _, _, w, h, short) in enumerate(vids, 1))

    svc_cards = "\n".join(
        f'''  <a href="/services/{s["slug"]}/"><span class="card-eyebrow">{e(s["price"])}</span><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p></a>'''
        for s in SERVICES)
    area_cells = "\n".join(
        f'      <a class="area-cell" href="/auto-detailing/{c["slug"]}/" style="text-decoration:none;">{e(c["name"])}, WI<span>{e(c["county"])}</span></a>'
        for c in CITIES)
    guide_cards = "\n".join(
        f'''  <a href="/guides/{g["slug"]}/"><span class="card-eyebrow">Guide</span><h3>{e(g["h1"])}</h3><p>{e(g["card"])}</p></a>'''
        for g in GUIDES[:3])

    body = f'''<section id="hero" aria-label="Hero">
  <div class="hero-left">
    <p class="hero-eyebrow">Hartford, Wisconsin &middot; Auto Detailing</p>
    <h1 class="hero-headline">Your Ride.<br><span class="accent">Spotless.</span></h1>
    <p class="hero-sub">Professional interior and exterior detailing that restores, protects and elevates every vehicle we touch. Hartford, WI and the surrounding Washington County area.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Book an Appointment</a>
      <a href="/pricing/" class="btn-ghost">View Pricing</a>
    </div>
    <div class="hero-stats">
      <div><div class="stat-num">2</div><div class="stat-label">Detail Packages</div></div>
      <div><div class="stat-num">$135</div><div class="stat-label">Starting Price</div></div>
      <div><div class="stat-num">12</div><div class="stat-label">Communities Served</div></div>
    </div>
  </div>
  <div class="hero-right" aria-hidden="true">
    <div class="hero-logo-wrap"><img src="/img/opt/logo-400.webp" alt="" width="400" height="400" loading="lazy" decoding="async" /></div>
  </div>
</section>

<section id="services" aria-labelledby="services-title">
  <div class="services-header fade-up">
    <p class="section-eyebrow">What We Do</p>
    <h2 class="section-title" id="services-title">Pick Your Package</h2>
  </div>
  <div class="cardgrid fade-up">
{svc_cards}
  </div>
  <p class="pricing-note">* Prices may vary based on vehicle condition and service requirements.</p>
</section>

<section id="gallery" aria-labelledby="gallery-title">
  <div class="gallery-header fade-up">
    <p class="section-eyebrow">Our Work</p>
    <h2 class="section-title" id="gallery-title">The Proof Is<br>In The Polish</h2>
  </div>
  <div class="gallery-photos fade-up">
{photo_html}
  </div>
  <div class="gallery-videos fade-up">
{video_html}
  </div>
</section>

<section id="areas" aria-labelledby="areas-title">
  <div class="gallery-header fade-up">
    <p class="section-eyebrow">Service Area</p>
    <h2 class="section-title" id="areas-title">Detailing Across<br>Washington County</h2>
  </div>
  <div class="areas-grid fade-up">
{area_cells}
  </div>
  <p class="areas-note fade-up">Based on WI-83 in Hartford, working throughout Washington County and neighbouring Dodge County. Just outside the list? Call or text {TEL} and we will tell you straight away whether we can reach you.</p>
</section>

<section id="guides" aria-labelledby="guides-title">
  <div class="gallery-header fade-up">
    <p class="section-eyebrow">Owner Guides</p>
    <h2 class="section-title" id="guides-title">Worth Knowing<br>Before You Book</h2>
  </div>
  <div class="cardgrid fade-up">
{guide_cards}
  </div>
  <p class="areas-note fade-up"><a href="/guides/" style="color:var(--gold);text-decoration:none;">See all owner guides &rarr;</a></p>
</section>

{faq_html(home_faq)}

{cta_html("Ready To Book?", "Call or text for a no-obligation quote and we will schedule your detail. We take it from there.")}

<p class="areas-note" style="padding:2rem 1.25rem;">{ADDR}, {CITY}, {REGION} {ZIP} &middot; <a href="mailto:{EMAIL}" style="color:var(--gold);text-decoration:none;">{EMAIL}</a></p>

<div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
  <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close image">&#x2715;</button>
  <img id="lightboxImg" src="" alt="" />
</div>
'''
    page(path, f"Auto Detailing in Hartford, WI | {BIZ}",
         "Professional interior & exterior auto detailing in Hartford, WI. Packages from $135 for cars, $150 SUVs/trucks. Serving Washington County. Call or text 414-286-1609.",
         graph, body)
    PAGES.append(("/", "1.0", "monthly", home_media_xml(photos, vids)))


def home_media_xml(photos, vids):
    img = "\n".join(f"""    <image:image>
      <image:loc>{SITE}/img/opt/{s}-{nat}.jpg</image:loc>
      <image:caption>{e(cap)}</image:caption>
    </image:image>""" for s, w, h, nat, cap, lbl in photos)
    vid = "\n".join(f"""    <video:video>
      <video:thumbnail_loc>{SITE}/img/poster/detail-{v}.jpg</video:thumbnail_loc>
      <video:title>{e(name)}</video:title>
      <video:description>{e(desc)}</video:description>
      <video:content_loc>{SITE}/video/detail-{v}.mp4</video:content_loc>
      <video:duration>{int(dur[2:-1])}</video:duration>
      <video:family_friendly>yes</video:family_friendly>
      <video:live>no</video:live>
      <video:publication_date>{MEDIA_UPLOAD}</video:publication_date>
    </video:video>""" for v, name, desc, dur, w, h, short in vids)
    return img + "\n" + vid


def build_services():
    hub_url = SITE + "/services/"
    trail = [("Home", "/"), ("Services", "/services/")]
    cards = "\n".join(
        f'''  <a href="/services/{s["slug"]}/"><span class="card-eyebrow">{e(s["price"])}</span><h3>{e(s["name"])}</h3><p>{e(s["card"])}</p></a>'''
        for s in SERVICES)
    graph = [org_node(), business_node(), website_node(),
             {"@type": "CollectionPage", "@id": f"{hub_url}#webpage", "url": hub_url,
              "name": f"Auto Detailing Services | {BIZ}", "isPartOf": {"@id": f"{SITE}/#website"},
              "about": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US",
              "breadcrumb": {"@id": f"{hub_url}#breadcrumb"}},
             crumb_node(hub_url, trail),
             {"@type": "ItemList", "@id": f"{hub_url}#list",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"],
                                   "url": f'{SITE}/services/{s["slug"]}/'} for i, s in enumerate(SERVICES)]}]
    body = f'''{crumbs_html(trail)}
<div class="page-head">
  <p class="section-eyebrow">Services</p>
  <h1 class="section-title">Auto Detailing Services</h1>
  <p class="page-lede">Two packages, no upsell ladder. Below is what each service actually involves, written out properly rather than reduced to a bullet list.</p>
</div>
<div class="cardgrid">
{cards}
</div>
{cta_html("Not Sure Which You Need?", "Describe the vehicle and we will tell you honestly. We would rather point you at the cheaper package than sell you the wrong one.")}
{related_html("Service area", [(c["name"] + ", WI", f'/auto-detailing/{c["slug"]}/') for c in CITIES])}
'''
    page("/services/", f"Auto Detailing Services in Hartford, WI | {BIZ}",
         "Interior detailing, exterior wash and polish, full details, stain and odor removal, truck and SUV detailing in Hartford, WI. From $135. Call 414-286-1609.",
         graph, body, active="/services/")
    PAGES.append(("/services/", "0.9", "monthly", ""))

    for s in SERVICES:
        p = f'/services/{s["slug"]}/'
        url = SITE + p
        t = [("Home", "/"), ("Services", "/services/"), (s["name"], p)]
        graph = [org_node(), business_node(), website_node(),
                 {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": s["title"],
                  "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en-US",
                  "breadcrumb": {"@id": f"{url}#breadcrumb"}},
                 crumb_node(url, t),
                 {"@type": "Service", "@id": f"{url}#service", "name": s["name"],
                  "serviceType": s["name"], "url": url,
                  "provider": {"@id": f"{SITE}/#business"},
                  "areaServed": [{"@type": "City", "name": c["name"]} for c in CITIES],
                  "description": s["lede"],
                  "offers": {"@type": "Offer", "priceCurrency": "USD",
                             "availability": "https://schema.org/InStock",
                             "url": url}},
                 faq_node(url, s["faq"])]
        rel = [(x["name"], f'/services/{x["slug"]}/') for x in SERVICES if x["slug"] in s["related"]]
        body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">Service &middot; {e(s["price"])}</p>
  <h1 class="section-title">{e(s["h1"])}</h1>
  <p class="page-lede">{e(s["lede"])}</p>
</div>
<div class="prose"><div class="prose-col">
{glance_html(s["glance"])}
{prose_html(s["body"])}
</div></div>
{faq_html(s["faq"])}
{cta_html("Book This Service", f"Call or text {TEL} for a straight quote. No obligation, and we will tell you if you need less than you think.")}
{related_html("Related services", rel)}
{related_html("Where we work", [(c["name"] + ", WI", f'/auto-detailing/{c["slug"]}/') for c in CITIES])}
'''
        page(p, s["title"], s["meta"], graph, body, active="/services/")
        PAGES.append((p, "0.8", "monthly", ""))


def build_cities():
    hub = "/auto-detailing/"
    hub_url = SITE + hub
    trail = [("Home", "/"), ("Service Area", hub)]
    cards = "\n".join(
        f'''  <a href="/auto-detailing/{c["slug"]}/"><span class="card-eyebrow">{e(c["county"])}</span><h3>{e(c["name"])}, WI</h3><p>{e(c["lede"])}</p></a>'''
        for c in CITIES)
    graph = [org_node(), business_node(), website_node(),
             {"@type": "CollectionPage", "@id": f"{hub_url}#webpage", "url": hub_url,
              "name": f"Service Area | {BIZ}", "isPartOf": {"@id": f"{SITE}/#website"},
              "about": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US",
              "breadcrumb": {"@id": f"{hub_url}#breadcrumb"}},
             crumb_node(hub_url, trail),
             {"@type": "ItemList", "@id": f"{hub_url}#list",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f'{c["name"]}, WI',
                                   "url": f'{SITE}/auto-detailing/{c["slug"]}/'} for i, c in enumerate(CITIES)]}]
    body = f'''{crumbs_html(trail)}
<div class="page-head">
  <p class="section-eyebrow">Service Area</p>
  <h1 class="section-title">Where We Detail</h1>
  <p class="page-lede">Twelve communities across Washington and Dodge County. Each page below covers what we actually see in vehicles from that area &mdash; the roads, the seasons and the specific problems &mdash; rather than the same paragraph with the town name swapped.</p>
</div>
<div class="cardgrid">
{cards}
</div>
{cta_html("Outside The List?", f"Call or text {TEL}. If you are close we will say yes, and if you are too far we will tell you that instead of wasting your time.")}
{related_html("Our services", [(s["name"], f'/services/{s["slug"]}/') for s in SERVICES])}
'''
    page(hub, f"Auto Detailing Service Area | Washington County, WI | {BIZ}",
         "Auto detailing across Washington and Dodge County, WI — Hartford, West Bend, Slinger, Germantown, Richfield, Jackson and more. Call or text 414-286-1609.",
         graph, body, active=hub)
    PAGES.append((hub, "0.9", "monthly", ""))

    for c in CITIES:
        p = f'/auto-detailing/{c["slug"]}/'
        url = SITE + p
        t = [("Home", "/"), ("Service Area", hub), (c["name"], p)]
        graph = [org_node(), business_node(), website_node(),
                 {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": c["title"],
                  "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en-US",
                  "about": {"@id": f"{SITE}/#business"},
                  "breadcrumb": {"@id": f"{url}#breadcrumb"}},
                 crumb_node(url, t),
                 {"@type": "Service", "@id": f"{url}#service",
                  "name": f'Auto Detailing in {c["name"]}, WI', "serviceType": "Auto Detailing",
                  "url": url, "provider": {"@id": f"{SITE}/#business"},
                  "areaServed": {"@type": "City", "name": c["name"],
                                 "containedInPlace": {"@type": "AdministrativeArea",
                                                      "name": f'{c["county"]}, Wisconsin'}},
                  "description": c["lede"]},
                 {"@type": "Place", "@id": f"{url}#place", "name": f'{c["name"]}, Wisconsin',
                  "address": {"@type": "PostalAddress", "addressLocality": c["name"],
                              "addressRegion": "WI", "addressCountry": "US"},
                  "geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lng"]}},
                 faq_node(url, c["faq"])]
        others = [(x["name"] + ", WI", f'/auto-detailing/{x["slug"]}/') for x in CITIES if x["slug"] != c["slug"]]
        body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">{e(c["county"])} &middot; {e(c["drive"])}</p>
  <h1 class="section-title">{e(c["h1"])}</h1>
  <p class="page-lede">{e(c["lede"])}</p>
</div>
<div class="prose"><div class="prose-col">
{glance_html(c["glance"])}
{prose_html(c["body"])}
<div class="callout">
  <span class="callout-label">Pricing</span>
  <p>Sudz Quick Clean (interior) &mdash; $135 cars, $150 SUVs and trucks. Sudz Up VIP Clean (interior and exterior) &mdash; $200 cars, $250 SUVs and trucks. Prices may vary with vehicle condition, and we quote before starting rather than at collection.</p>
</div>
</div></div>
{faq_html(c["faq"])}
{cta_html(f'Book a Detail in {c["name"]}', f"Call or text {TEL} for a no-obligation quote. We will give you a straight price and a realistic turnaround.")}
{related_html("Services we offer", [(s["name"], f'/services/{s["slug"]}/') for s in SERVICES])}
{related_html("Other areas we serve", others)}
'''
        page(p, c["title"], c["meta"], graph, body, active=hub)
        PAGES.append((p, "0.8", "monthly", ""))


def build_guides():
    hub = "/guides/"
    hub_url = SITE + hub
    trail = [("Home", "/"), ("Guides", hub)]
    cards = "\n".join(
        f'''  <a href="/guides/{g["slug"]}/"><span class="card-eyebrow">Guide</span><h3>{e(g["h1"])}</h3><p>{e(g["card"])}</p></a>'''
        for g in GUIDES)
    graph = [org_node(), business_node(), website_node(),
             {"@type": "CollectionPage", "@id": f"{hub_url}#webpage", "url": hub_url,
              "name": f"Car Care Guides | {BIZ}", "isPartOf": {"@id": f"{SITE}/#website"},
              "inLanguage": "en-US", "breadcrumb": {"@id": f"{hub_url}#breadcrumb"}},
             crumb_node(hub_url, trail),
             {"@type": "ItemList", "@id": f"{hub_url}#list",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": g["h1"],
                                   "url": f'{SITE}/guides/{g["slug"]}/'} for i, g in enumerate(GUIDES)]}]
    body = f'''{crumbs_html(trail)}
<div class="page-head">
  <p class="section-eyebrow">Owner Guides</p>
  <h1 class="section-title">Car Care Guides<br>For Wisconsin Drivers</h1>
  <p class="page-lede">Written to be useful whether or not you ever book with us. Salt, stains, timing, resale and pets &mdash; the things people actually ask about.</p>
</div>
<div class="cardgrid">
{cards}
</div>
{cta_html("Questions We Have Not Covered?", f"Call or text {TEL}. We are happy to give you a straight answer even if it means telling you that you do not need us.")}
'''
    page(hub, f"Car Care Guides for Wisconsin Drivers | {BIZ}",
         "Practical car care guides for Wisconsin drivers — road salt, stain removal, detailing frequency, resale prep and pet odor. From a Hartford, WI detailer.",
         graph, body, active=hub)
    PAGES.append((hub, "0.7", "monthly", ""))

    for g in GUIDES:
        p = f'/guides/{g["slug"]}/'
        url = SITE + p
        t = [("Home", "/"), ("Guides", hub), (g["h1"], p)]
        graph = [org_node(), business_node(), website_node(),
                 {"@type": ["Article", "WebPage"], "@id": f"{url}#webpage", "url": url,
                  "headline": g["h1"], "name": g["title"], "description": g["meta"],
                  "datePublished": g["date"], "dateModified": g["date"],
                  "author": {"@id": f"{SITE}/#organization"},
                  "publisher": {"@id": f"{SITE}/#organization"},
                  "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en-US",
                  "image": f"{SITE}/img/opt/logo-512.png",
                  "about": {"@id": f"{SITE}/#business"},
                  "breadcrumb": {"@id": f"{url}#breadcrumb"}},
                 crumb_node(url, t),
                 faq_node(url, g["faq"])]
        others = [(x["h1"], f'/guides/{x["slug"]}/') for x in GUIDES if x["slug"] != g["slug"]]
        body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">Owner Guide</p>
  <h1 class="section-title">{e(g["h1"])}</h1>
  <p class="page-lede">{e(g["lede"])}</p>
</div>
<div class="prose"><div class="prose-col">
{prose_html(g["body"])}
</div></div>
{faq_html(g["faq"])}
{cta_html("Want This Done Properly?", f"Call or text {TEL} for a no-obligation quote from a detailer who works in these conditions every week.")}
{related_html("More guides", others)}
{related_html("Our services", [(s["name"], f'/services/{s["slug"]}/') for s in SERVICES])}
'''
        page(p, g["title"], g["meta"], graph, body, active=hub)
        PAGES.append((p, "0.6", "yearly", ""))


def build_static_pages():
    # ── PRICING ────────────────────────────────────────────────
    p, url = "/pricing/", SITE + "/pricing/"
    t = [("Home", "/"), ("Pricing", p)]
    pricing_faq = [
        ("Is the price on the website the price I pay?", "For a vehicle in normal condition, yes. Where condition means more work, we tell you before starting rather than adjusting the figure at collection."),
        ("Why do SUVs and trucks cost more?", "More interior volume, extra footwells and rows, a larger cargo area, more glass and jambs, and more panel area outside. It reflects genuine additional time."),
        ("Do you charge extra for door jambs or interior glass?", "No. Both are included in every package. They are part of what makes a detail different from a car wash."),
        ("Do you offer ceramic coating or paint correction?", "No. We do interior detailing and exterior wash and polish, and we would rather do those properly than list services we are not set up to deliver."),
    ]
    graph = [org_node(), business_node(), website_node(),
             {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": f"Pricing | {BIZ}",
              "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#business"},
              "inLanguage": "en-US", "breadcrumb": {"@id": f"{url}#breadcrumb"}},
             crumb_node(url, t), faq_node(url, pricing_faq)]
    body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">Pricing</p>
  <h1 class="section-title">Straight Pricing,<br>No Upsell Ladder</h1>
  <p class="page-lede">Two packages. Both prices below are what a vehicle in normal condition costs. Where condition means more work, we say so before we start.</p>
</div>
<div class="prose"><div class="prose-col">
<table class="spec">
  <thead><tr><th>Package</th><th>Cars</th><th>SUVs &amp; Trucks</th></tr></thead>
  <tbody>
    <tr><td>Sudz Quick Clean<br><span style="color:var(--text);font-weight:400;font-size:.85rem;">Interior only</span></td><td>$135</td><td>$150</td></tr>
    <tr><td>Sudz Up VIP Clean<br><span style="color:var(--text);font-weight:400;font-size:.85rem;">Interior + exterior</span></td><td>$200</td><td>$250</td></tr>
  </tbody>
</table>

<h2>What is in each package</h2>
<h3>Sudz Quick Clean &mdash; $135 / $150</h3>
<ul>
  <li>Complete interior vacuum, including under seats, along rails and beneath floor mats</li>
  <li>Vinyl, rubber and plastic treatment across hard surfaces</li>
  <li>Spot stain removal on targeted marks</li>
  <li>Door jambs cleaned</li>
  <li>Windows cleaned inside and out</li>
</ul>
<h3>Sudz Up VIP Clean &mdash; $200 / $250</h3>
<ul>
  <li>Everything in the Sudz Quick Clean</li>
  <li>Exterior hand wash</li>
  <li>Polish for a uniform, protected finish</li>
  <li>Wheels cleaned</li>
  <li>Tires shined</li>
</ul>

<h2>What can change the price</h2>
<p>Detailing is labour, so anything that adds time adds cost. The honest list of what does that:</p>
<ul>
  <li><strong>Heavy pet hair.</strong> Hair has to be mechanically agitated out of fabric before it can be extracted. On a heavily furred vehicle this alone can take an hour.</li>
  <li><strong>Widespread staining.</strong> Spot removal is included. Full extraction across every surface is a different job.</li>
  <li><strong>Odour contamination.</strong> Locating a source in the carpet backing or seat foam and extracting it properly takes time, and needs drying afterwards.</li>
  <li><strong>Extreme soil.</strong> Work vehicles with compacted mud or agricultural material need staged removal.</li>
  <li><strong>Vehicles never previously detailed.</strong> A car done annually takes a fraction of the time of one that has never been done.</li>
</ul>

<div class="callout">
  <span class="callout-label">How we quote</span>
  <p>Describe the vehicle honestly when you call and you will get a real figure. If it turns out to be significantly rougher than described, we call you with a revised number <strong>before</strong> starting &mdash; not at collection. And if we do not think a detail will produce a result worth the money, we will tell you that instead of taking the booking.</p>
</div>

<h2>What we do not offer</h2>
<p>We do not do ceramic coating, paint protection film, multi-stage paint correction or window tinting. Those are legitimate services and there are shops in the area that do them well. We would rather do interior detailing and exterior wash and polish properly than pad a price list with things we are not set up to deliver.</p>
</div></div>
{faq_html(pricing_faq)}
{cta_html("Get a Straight Quote", f"Call or text {TEL}. Describe the vehicle and you will get a real number, not a starting point.")}
{related_html("Our services", [(s["name"], f'/services/{s["slug"]}/') for s in SERVICES])}
'''
    page(p, f"Auto Detailing Prices in Hartford, WI | {BIZ}",
         "Auto detailing prices in Hartford, WI. Interior $135 cars / $150 SUVs and trucks. Full interior and exterior $200 / $250. No upsell ladder. Call 414-286-1609.",
         graph, body, active=p)
    PAGES.append((p, "0.9", "monthly", ""))

    # ── ABOUT ──────────────────────────────────────────────────
    p, url = "/about/", SITE + "/about/"
    t = [("Home", "/"), ("About", p)]
    graph = [org_node(), business_node(), website_node(),
             {"@type": ["AboutPage", "WebPage"], "@id": f"{url}#webpage", "url": url,
              "name": f"About | {BIZ}", "isPartOf": {"@id": f"{SITE}/#website"},
              "about": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US",
              "breadcrumb": {"@id": f"{url}#breadcrumb"}},
             crumb_node(url, t)]
    body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">About Us</p>
  <h1 class="section-title">True Quality<br>Is In The Details</h1>
  <p class="page-lede">Sudz Up Detailing LLC is an auto detailing business on WI-83 in Hartford, Wisconsin, serving Washington County and the neighbouring Dodge County communities.</p>
</div>
<div class="prose"><div class="prose-col">
<h2>How we work</h2>
<p>We take pride in elevating the standard of vehicle care. Every service is designed to restore, protect and enhance a vehicle inside and out, with precision and a commitment to doing the job properly rather than quickly.</p>
<p>That means a few specific things in practice. We move seats to reach the rails. We lift floor mats and clean the carpet underneath. We clear seams and vents with compressed air before vacuuming, because a vacuum nozzle cannot generate airflow inside a narrow gap. We do door jambs and interior glass as standard, because those are what separate a detail from a wash.</p>

<h2>Two packages, deliberately</h2>
<p>We offer the Sudz Quick Clean and the Sudz Up VIP Clean. That is it. There is no five-tier ladder engineered to make the middle option look sensible, and no menu of add-ons quoted separately once your vehicle is already on the lot.</p>
<p>The reason is straightforward: most people asking for a detail want their interior properly cleaned and, sometimes, the outside brought back with it. Two packages cover that honestly.</p>

<h2>What we will tell you</h2>
<p>We will tell you if you need the cheaper package. We will tell you before starting if a vehicle needs more work than the quote covers, rather than presenting a different figure at collection. And we will tell you if we do not think a detail will produce a result worth the money on a particular vehicle.</p>
<p>We will also be honest about limits. Detailing does not repair. Cracked dash tops, torn fabric, sagging headliners, stone chips and failed clear coat are beyond it. Long-term cigarette odour can be substantially reduced but rarely eliminated. Anyone guaranteeing otherwise without seeing the vehicle is not being straight with you.</p>

<h2>Every vehicle treated right</h2>
<p>Cars, trucks and SUVs. Work vehicles, family vehicles and weekend vehicles. A truck that is your workplace for fifty hours a week is exactly where a clean cabin makes a daily difference, and it is usually carrying the most abrasive material of anything we see.</p>

<h2>Local to Hartford</h2>
<p>We are based at {ADDR} in Hartford and we work across {", ".join(c["name"] for c in CITIES[:-1])} and {CITIES[-1]["name"]}. Everything on this site about road salt, brine, lake sand and gravel dust comes from working on vehicles in these conditions rather than from a template.</p>
</div></div>
{cta_html("Get In Touch", f"Call or text {TEL} for a no-obligation quote. Tell us the vehicle and what is bothering you about it.")}
{related_html("Where we work", [(c["name"] + ", WI", f'/auto-detailing/{c["slug"]}/') for c in CITIES])}
'''
    page(p, f"About {BIZ} | Auto Detailing in Hartford, WI",
         "About Sudz Up Detailing LLC, an auto detailing business on WI-83 in Hartford, Wisconsin serving Washington County. Two packages, straight pricing, honest limits.",
         graph, body, active=p)
    PAGES.append((p, "0.6", "yearly", ""))

    # ── CONTACT ────────────────────────────────────────────────
    p, url = "/contact/", SITE + "/contact/"
    t = [("Home", "/"), ("Contact", p)]
    contact_faq = [
        ("How do I book?", "Call or text 414-286-1609, or email SudzUpdetail2025@outlook.com. There is no online booking form — we would rather talk to you briefly and give you an accurate quote and time."),
        ("Do you have a booking form?", "No. A short call or text gets you a more accurate quote than a form, because we can ask about the vehicle's condition."),
        ("What should I tell you when I call?", "Vehicle size, rough condition, and any specific issue — a spill you know about, a smell, whether pets travel in it, whether anyone smokes in it. That determines how much time we set aside."),
        ("Do I need to empty my car first?", "Please do. Removing personal belongings lets us work faster and means we are not making judgement calls about what matters to you."),
    ]
    graph = [org_node(), business_node(), website_node(),
             {"@type": ["ContactPage", "WebPage"], "@id": f"{url}#webpage", "url": url,
              "name": f"Contact | {BIZ}", "isPartOf": {"@id": f"{SITE}/#website"},
              "about": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US",
              "breadcrumb": {"@id": f"{url}#breadcrumb"}},
             crumb_node(url, t), faq_node(url, contact_faq)]
    body = f'''{crumbs_html(t)}
<div class="page-head">
  <p class="section-eyebrow">Get In Touch</p>
  <h1 class="section-title">Ready To Book?</h1>
  <p class="page-lede">Call or text for a no-obligation quote and to schedule your detail. We will take it from there.</p>
</div>
<div class="prose"><div class="prose-col">
<div class="contact-btns" style="margin-bottom:2.5rem;">
  <a href="tel:+14142861609" class="btn-contact btn-contact-call">Call Us &mdash; {TEL}</a>
  <a href="sms:+14142861609" class="btn-contact btn-contact-text">Text Us &mdash; {TEL}</a>
</div>
{glance_html([("Phone / text", TEL), ("Email", EMAIL), ("Address", f"{ADDR}, {CITY} {ZIP}"), ("Hours", "Mon–Sun, 8am–6pm")])}

<h2>What to tell us</h2>
<p>A short call gets you a more accurate quote than any form would. The things worth mentioning:</p>
<ul>
  <li>Vehicle type &mdash; car, SUV, truck or van, and roughly how many seats</li>
  <li>Rough condition, honestly. There is no judgement and it is not a negotiation tactic; it determines how much time we set aside</li>
  <li>Any specific problem &mdash; a spill you know about, a smell, a stain you have already tried to treat</li>
  <li>Whether pets travel in the vehicle, and whether anyone smokes in it</li>
  <li>If you are selling, tell us when you plan to list, so we can sequence the detail before your photographs</li>
</ul>

<div class="callout">
  <span class="callout-label">Before you drop off</span>
  <p>Please take personal belongings out of the vehicle. It lets us work faster, and it means we are not deciding what is rubbish and what matters to you.</p>
</div>

<h2>Where we are</h2>
<p>{ADDR}, {CITY}, {REGION} {ZIP}. A few minutes from downtown Hartford in either direction. <a href="https://www.google.com/maps/search/?api=1&amp;query=2948+WI-83+Hartford+WI+53027" rel="noopener">Open in Google Maps</a>.</p>
<p>Call or text before heading over so we can confirm we are on site and ready for your vehicle.</p>
</div></div>
{faq_html(contact_faq)}
{related_html("Areas we serve", [(c["name"] + ", WI", f'/auto-detailing/{c["slug"]}/') for c in CITIES])}
'''
    page(p, f"Contact {BIZ} | Book Auto Detailing in Hartford, WI",
         "Book auto detailing in Hartford, WI. Call or text 414-286-1609 for a no-obligation quote. 2948 WI-83, Hartford, WI 53027. Open 8am to 6pm daily.",
         graph, body, active=p)
    PAGES.append((p, "0.9", "monthly", ""))


# ────────────────────────────────────────────────────────── crawl-layer files

def build_sitemap():
    urls = []
    for path, prio, freq, extra in PAGES:
        media = ("\n" + extra) if extra else ""
        urls.append(f"""  <url>
    <loc>{SITE}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>{media}
  </url>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
{chr(10).join(urls)}
</urlset>
"""
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)


def build_robots():
    agents = ["*", "Googlebot", "Googlebot-Image", "Googlebot-Video", "Bingbot", "GPTBot",
              "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot",
              "Google-Extended", "Applebot", "Applebot-Extended"]
    blocks = "\n\n".join(f"User-agent: {a}\nAllow: /" for a in agents)
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        f"# {BIZ} — https://sudzupdetail.com\n"
        f"# Search and AI crawlers are explicitly welcome.\n\n{blocks}\n\n"
        f"Disallow: /_build/\n\nSitemap: {SITE}/sitemap.xml\n")


def build_llms():
    svc = "\n".join(f'- {s["name"]} ({s["price"]}) — {SITE}/services/{s["slug"]}/\n  {s["card"]}'
                    for s in SERVICES)
    loc = "\n".join(f'- {c["name"]}, WI ({c["county"]}, {c["drive"]}) — {SITE}/auto-detailing/{c["slug"]}/'
                    for c in CITIES)
    gds = "\n".join(f'- {g["h1"]} — {SITE}/guides/{g["slug"]}/\n  {g["card"]}' for g in GUIDES)
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(f"""# {BIZ}

> Professional interior and exterior auto detailing in Hartford, Wisconsin,
> serving Washington County and neighbouring Dodge County communities.

## Business
- Name: {BIZ}
- Address: {ADDR}, {CITY}, {REGION} {ZIP}, United States
- Phone / Text: {TEL}
- Email: {EMAIL}
- Website: {SITE}/
- Hours: Monday-Sunday, 8:00 AM - 6:00 PM
- Vehicle types: cars, trucks, SUVs, vans

## Packages and pricing
- Sudz Quick Clean (interior only) - $135 cars / $150 SUVs and trucks.
  Interior vacuum, vinyl/rubber/plastic (VRP) treatment, spot stain removal,
  door jambs cleaned, windows cleaned inside and out.
- Sudz Up VIP Clean (interior + exterior) - $200 cars / $250 SUVs and trucks.
  Everything in the Quick Clean plus exterior hand wash, polish, wheels
  cleaned and tires shined.

Prices may vary based on vehicle condition. Quotes are given before work
starts, not at collection.

## Not offered
Ceramic coating, paint protection film, multi-stage paint correction and
window tinting are NOT offered by this business.

## Services
{svc}

## Service area
{loc}

## Owner guides
{gds}

## Booking
Call or text {TEL}, or email {EMAIL}.
There is no online booking form. Quotes are free and carry no obligation.
""")


def build_js():
    open(os.path.join(ROOT, "assets", "site.js"), "w", encoding="utf-8").write("""// Sudz Up Detailing — shared behaviour
(function () {
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () { links.classList.toggle('open'); });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en, i) {
        if (en.isIntersecting) {
          setTimeout(function () { en.target.classList.add('visible'); }, i * 70);
          obs.unobserve(en.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-up').forEach(function (el) { obs.observe(el); });
  } else {
    document.querySelectorAll('.fade-up').forEach(function (el) { el.classList.add('visible'); });
  }

  document.querySelectorAll('.faq-q').forEach(function (btn, i) {
    if (i === 0) {
      btn.closest('.faq-item').classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var open = item.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();

var lastFocus = null;
function toggleVideo(vidId, wrapId) {
  var vid = document.getElementById(vidId), wrap = document.getElementById(wrapId);
  if (!vid || !wrap) return;
  if (vid.paused) {
    document.querySelectorAll('.gallery-video video').forEach(function (v) {
      if (v !== vid && !v.paused) { v.pause(); v.closest('.gallery-video').classList.remove('playing'); }
    });
    vid.play().catch(function () {});
    wrap.classList.add('playing');
  } else {
    vid.pause();
    wrap.classList.remove('playing');
  }
}
function openLightbox(src, alt) {
  var lb = document.getElementById('lightbox'), im = document.getElementById('lightboxImg');
  if (!lb || !im) return;
  lastFocus = document.activeElement;
  im.src = src;
  im.alt = alt || 'Auto detailing work by Sudz Up Detailing, Hartford WI';
  lb.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLightbox(ev) {
  var lb = document.getElementById('lightbox');
  if (!lb) return;
  if (!ev || ev.target === lb || (ev.target.classList && ev.target.classList.contains('lightbox-close'))) {
    lb.classList.remove('open');
    document.getElementById('lightboxImg').src = '';
    document.body.style.overflow = '';
    if (lastFocus) { lastFocus.focus(); lastFocus = null; }
  }
}
document.addEventListener('keydown', function (ev) {
  if (ev.key === 'Escape') closeLightbox({ target: document.getElementById('lightbox') });
});
""")


def main():
    build_home()
    build_services()
    build_cities()
    build_guides()
    build_static_pages()
    build_sitemap()
    build_robots()
    build_llms()
    build_js()
    print(f"Built {len(PAGES)} pages")
    for path, prio, _, _ in sorted(PAGES):
        print(f"  {prio}  {path}")


if __name__ == "__main__":
    main()
