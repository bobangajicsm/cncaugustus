# -*- coding: utf-8 -*-
"""Generates the CNC Metalworking Augustus site (EN default + SR) into ./out"""
import os, posixpath

OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://www.cncaugustus.com"   # promeniti ako domen bude drugačiji

LANGS = ["en", "de", "pl", "cs", "sr"]   # redosled u meniju
LANG_LABEL = {"en": "EN", "de": "DE", "pl": "PL", "cs": "CZ", "sr": "SR"}

PAGES = {
    "home":     {"en": "index.html",                         "de": "de/index.html",                     "pl": "pl/index.html",                      "cs": "cs/index.html",                    "sr": "sr/index.html"},
    "products": {"en": "products/index.html",                "de": "de/produkte/index.html",            "pl": "pl/produkty/index.html",             "cs": "cs/produkty/index.html",           "sr": "sr/proizvodi/index.html"},
    "window":   {"en": "products/window-opener.html",        "de": "de/produkte/fensteroeffner.html",   "pl": "pl/produkty/otwieracz-okien.html",   "cs": "cs/produkty/otvirac-oken.html",    "sr": "sr/proizvodi/otvarac-prozora.html"},
    "door":     {"en": "products/door-opener.html",          "de": "de/produkte/tueroeffner.html",      "pl": "pl/produkty/otwieracz-drzwi.html",   "cs": "cs/produkty/otvirac-dveri.html",   "sr": "sr/proizvodi/otvarac-vrata.html"},
    "cylinder": {"en": "products/replacement-cylinder.html", "de": "de/produkte/ersatzzylinder.html",   "pl": "pl/produkty/cylinder-zapasowy.html", "cs": "cs/produkty/nahradni-valec.html",  "sr": "sr/proizvodi/rezervni-cilindar.html"},
    "services": {"en": "services/index.html",                "de": "de/leistungen/index.html",          "pl": "pl/uslugi/index.html",               "cs": "cs/sluzby/index.html",             "sr": "sr/usluge/index.html"},
    "about":    {"en": "about/index.html",                   "de": "de/ueber-uns/index.html",           "pl": "pl/o-nas/index.html",                "cs": "cs/o-nas/index.html",              "sr": "sr/o-nama/index.html"},
    "contact":  {"en": "contact/index.html",                 "de": "de/kontakt/index.html",             "pl": "pl/kontakt/index.html",              "cs": "cs/kontakt/index.html",            "sr": "sr/kontakt/index.html"},
}

PHONE = "+381 65 9946547"
PHONE_TEL = "+381659946547"
EMAIL = "info@cncaugustus.com"
ADDRESS = "Svetislava Damjanovića 26, 22202 Mačvanska Mitrovica"
SOCIAL = {
    "instagram": "https://www.instagram.com/cnc_metalworking_augustus",
    "tiktok": "https://www.tiktok.com/@cnc.metalworking.augustu",
    "facebook": "https://www.facebook.com/profile.php?id=61586065602689",
}
FORM_ACTION = "https://formspree.io/f/REPLACE_WITH_FORM_ID"  # vidi README

# ---------------------------------------------------------------- icons
ICONS = {
    "factory": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20V9l6 4V9l6 4V9l8 5v6H2z"/><path d="M6 20v-4M10 20v-4M14 20v-4M18 20v-4"/></svg>',
    "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/></svg>',
    "sample": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6v7l5 9H4l5-9V3z"/><path d="M8 3h8"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-8 8H7l-4 3V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8z"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 6h13v10H1zM14 9h5l4 4v3h-9z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="17.5" cy="18.5" r="2"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2.1z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.7.1-1.1 0-1.7.2-2.1.4-.5.2-.9.4-1.2.8-.4.4-.6.7-.8 1.2-.2.4-.3 1-.4 2.1C2.8 8.5 2.8 8.9 2.8 12s0 3.5.1 4.7c0 1.1.2 1.7.4 2.1.2.5.4.9.8 1.2.4.4.7.6 1.2.8.4.2 1 .3 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1 0 1.7-.2 2.1-.4.5-.2.9-.4 1.2-.8.4-.4.6-.7.8-1.2.2-.4.3-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c0-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.2-.4-.4-.7-.6-1.2-.8-.4-.2-1-.3-2.1-.4C15.5 4 15.1 4 12 4zm0 3a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 1.8a3.2 3.2 0 1 0 0 6.4 3.2 3.2 0 0 0 0-6.4zm5.2-2.1a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24"><path d="M16.5 2h-3.2v13.2a2.8 2.8 0 1 1-2.8-2.8c.3 0 .6 0 .9.1V9.2a6 6 0 1 0 5.1 5.9V8.5a7.2 7.2 0 0 0 4.2 1.3V6.6a4.3 4.3 0 0 1-4.2-4.6z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3z"/></svg>',
}

# ---------------------------------------------------------------- content
T = {
"en": {
    "lang": "en",
    "nav": {"products": "Products", "services": "CNC services", "about": "About", "contact": "Contact", "cta": "Request a sample"},
    "footer_about": "Manufacturer of automatic window and door openers for greenhouses. Full in-house CNC production in Mačvanska Mitrovica, Serbia. Supplying distributors and greenhouse manufacturers worldwide.",
    "footer_products": "Products", "footer_company": "Company", "footer_contact": "Contact",
    "footer_hours": "Mon–Fri 08:00–16:00 (CET)",
    "rights": "All rights reserved.",
    "cta_band": {
        "h": "Test it before you order.",
        "p": "We send a free sample set to distributors and greenhouse manufacturers. Mount it, run it through a season, then talk quantities and prices with us directly.",
        "b1": "Request a free sample", "b2": "Download catalogue (PDF)",
    },
    "home": {
        "title": "Automatic Greenhouse Openers | Manufacturer | CNC Metalworking Augustus",
        "desc": "Manufacturer of automatic window and door openers for greenhouses. In-house CNC production, 50.000+ sets/year capacity, stock available, free samples for B2B buyers worldwide.",
        "eyebrow": "Manufacturer · Serbia · Worldwide delivery",
        "h1": "Automatic greenhouse openers, <em>straight from the factory</em>",
        "lead": "We machine, assemble and stock automatic window and door openers for greenhouses. The mechanism and the cylinder are made in-house on our own CNC lathes. Distributors and greenhouse manufacturers around the world, let's put one in your greenhouse.",
        "b1": "Request a free sample", "b2": "See the products",
        "tag": "Window opener · 20 kg",
        "strip": [("50.000+", "sets", "Annual capacity"), ("7", "", "CNC STAR lathes"), ("350", "m²", "Production floor"), ("6+", "yrs", "In precision machining"), ("2", "yrs", "Warranty on every set")],
        "prod_eyebrow": "Products", "prod_h": "Openers and spare parts from one supplier.",
        "prod_lead": "Sold as complete sets, ready to mount. Everything below is made and assembled at our facility.",
        "why_eyebrow": "Why buy direct", "why_h": "What you get when you buy from the factory",
        "why": [
            ("factory", "Made entirely in-house", "Mechanism and cylinder are both machined and assembled at our facility. No third-party cylinders, no surprises between batches."),
            ("box", "Stock ready for the season", "We produce through the off-season so that sets are on the shelf when your buying season starts in January."),
            ("sample", "Free sample first", "You test the opener in your own greenhouse before you commit to a quantity. No cost, no obligation."),
            ("check", "Consistent quality", "Certified European materials, measured tolerances and an inspection of every set before packing. Quality management certified to ISO 9001."),
            ("chat", "A direct line to production", "Your questions go to the people who make the product. Changes, packaging, labelling: we can talk it through."),
            ("truck", "Worldwide delivery", "We ship pallet quantities anywhere in the world, on terms agreed for the whole season."),
        ],
        "svc_eyebrow": "CNC services", "svc_h": "Turned parts and laser cutting for your own products",
        "svc_p": "The same lathes that make our openers are available for contract work: precision turned parts from 2 to 20 mm in steel, stainless, brass and aluminium, fiber laser cutting of sheet metal and surface finishing.",
        "svc_b": "About our CNC services",
    },
    "products": {
        "title": "Products | Automatic Window and Door Openers for Greenhouses",
        "desc": "Automatic greenhouse window opener (20 kg), door opener (30 kg) and replacement cylinder. Manufactured in-house, sold as complete sets, free samples for B2B buyers.",
        "h1": "Products", "lead": "Automatic openers for greenhouse windows and doors, plus the replacement cylinder that fits any opener on the market. All made in-house, all sold as complete sets.",
        "cat_b": "Download catalogue (PDF)",
    },
    "cards": {
        "window": ("Automatic window opener", "Heat-driven opener for greenhouse roof and side windows. Double-arm spring mechanism, Easy Clip mounting. Available in zinc or black.", ["20 kg", "45 cm", "16–30 °C", "Easy Clip"]),
        "door": ("Automatic door opener", "Stronger unit for greenhouse doors and larger vents. Opens to 90° for fast heat release.", ["30 kg", "90°", "18–35 °C"]),
        "cylinder": ("Replacement cylinder", "Universal heat-driven cylinder that fits any automatic opener. Aluminium body, stainless piston.", ["20 kg", "65 mm", "16–30 °C"]),
    },
    "detail_common": {"crumb": "Products", "specs_h": "Technical specifications", "feat_h": "Key features", "gallery_h": "Product views", "related_h": "Other products", "cta": "Request a sample", "cat": "Download catalogue (PDF)", "details": "Details"},
    "window": {
        "title": "Automatic Greenhouse Window Opener, 20 kg | CNC Metalworking Augustus",
        "desc": "Automatic greenhouse window opener with 20 kg lifting force, 45 cm opening and 16–30 °C operating range. No electricity or batteries. Zinc-coated steel, 2-year warranty.",
        "h1": "Automatic window opener", "sub": "Heat-driven opener for greenhouse windows. No electricity, no batteries, Easy Clip mounting in seconds.",
        "intro": [
            "The opener uses a heat-driven cylinder: as the air inside the greenhouse warms up, the cylinder expands and lifts the window; as it cools, the window closes. It starts to open at around 16 °C and is fully open at 30 °C, so ventilation follows the temperature without anyone touching it.",
            "A double-arm spring mechanism gives it a lifting force of up to 20 kg, enough for heavier polycarbonate and glass windows. The Easy Clip system mounts and removes the opener in seconds and fits a wide range of greenhouse frames.",
            "Built from zinc-coated steel for year-round outdoor use. Every set is inspected before packing and covered by a 2-year manufacturer's warranty.",
        ],
        "specs": [("Lifting force", "up to 20 kg"), ("Maximum opening", "45 cm"), ("Cylinder stroke", "65 mm"), ("Operating range", "16–30 °C"), ("Power", "none, heat-driven cylinder"), ("Material", "zinc-coated steel"), ("Finish", "zinc or black"), ("Mounting", "Easy Clip, no tools"), ("Warranty", "2 years")],
        "features": [("Starts at 16 °C, fully open at 30 °C", "Ventilation follows the temperature automatically."), ("20 kg lifting force", "Handles heavier windows with margin to spare."), ("Mounts in seconds", "Easy Clip fixing, fits most frame profiles."), ("Zinc-coated steel", "Corrosion resistant, built for years outdoors.")],
        "versions": ("Two versions", "Same mechanism, same specifications. The two versions are listed as separate items in the price list.", [("window-opener.jpg", "Window opener · Zinc", "Classic zinc-coated finish."), ("window-opener-black.jpg", "Window opener · Black", "Black finish.")]),
        "gallery": [("window-opener-detail.jpg", "Double-arm mechanism and mounting points"), ("window-opener-black-detail.jpg", "Black version, double-arm mechanism")],
    },
    "door": {
        "title": "Automatic Greenhouse Door Opener, 30 kg | CNC Metalworking Augustus",
        "desc": "Automatic greenhouse door opener with 30 kg force, 110 mm stroke and 90° opening. Operating range 18–35 °C. No electricity, zinc-coated steel, 2-year warranty.",
        "h1": "Automatic door opener", "sub": "Built for greenhouse doors and larger vents. Opens to 90°.",
        "intro": [
            "The door opener works on the same principle as the window opener, with a stronger cylinder and a longer stroke. It responds between 18 °C and 35 °C, pushing the door open as the greenhouse warms and closing it as the temperature drops.",
            "With a force of up to 30 kg and a 110 mm stroke it opens the door to 90°, which gives the fastest heat release on hot days. It is designed for heavier doors and larger openings where a window opener would not be enough.",
            "Zinc-coated steel construction for long outdoor service. Mounts quickly on most greenhouse door frames. 2-year manufacturer's warranty.",
        ],
        "specs": [("Force", "up to 30 kg"), ("Maximum opening", "90°"), ("Cylinder stroke", "110 mm"), ("Operating range", "18–35 °C"), ("Power", "none, heat-driven cylinder"), ("Material", "zinc-coated steel"), ("Warranty", "2 years")],
        "features": [("Opens to 90°", "Full opening for maximum airflow."), ("30 kg force", "Made for heavier doors and larger openings."), ("18–35 °C range", "Wider range for warmer climates and large volumes."), ("Zinc-coated steel", "Stable performance season after season.")],
        "gallery": [("door-opener-set.jpg", "Complete set: cylinder, spring, arms and mounting brackets"), ("door-opener-detail-1.jpg", "Cylinder, pivot joint and slotted mounting bracket"), ("door-opener-detail-2.jpg", "Spring anchored on the bracket bolt"), ("door-opener-detail-3.jpg", "Threaded piston rod with 110 mm stroke")],
    },
    "cylinder": {
        "title": "Replacement Cylinder for Automatic Greenhouse Openers | CNC Metalworking Augustus",
        "desc": "Universal replacement cylinder that fits any automatic greenhouse opener. 20 kg force, 65 mm stroke, 16–30 °C. Aluminium body, stainless steel piston, made in-house.",
        "h1": "Replacement cylinder", "sub": "Universal heat-driven cylinder for any automatic greenhouse opener.",
        "intro": [
            "The cylinder is the heart of every automatic opener and the part that eventually needs replacing. Ours fits every opener on the market, which makes it a practical spare for distributors and a service item for greenhouse owners.",
            "It delivers up to 20 kg of force with a 65 mm stroke and activates between 16 °C and 30 °C. The body is machined from aluminium and the piston from stainless steel, then finished in black.",
            "We make the cylinders ourselves, on the same lathes as the rest of the opener, so specifications are the same from batch to batch.",
        ],
        "specs": [("Force", "up to 20 kg"), ("Stroke", "65 mm"), ("Operating range", "16–30 °C"), ("Body", "aluminium, black finish"), ("Piston", "stainless steel"), ("Compatibility", "all automatic openers"), ("Warranty", "2 years")],
        "features": [("Fits every opener", "A universal replacement, whatever opener you run."), ("Made in-house", "Machined on our own lathes, same spec every batch."), ("Aluminium and stainless", "Light, corrosion resistant, built for outdoor use."), ("16–30 °C activation", "Matches the window opener exactly.")],
        "gallery": [("replacement-cylinder.jpg", "Replacement cylinder with stainless piston")],
    },
    "services": {
        "title": "CNC Turning and Laser Cutting | CNC Metalworking Augustus",
        "desc": "Precision CNC turned parts from 2 to 20 mm in steel, stainless, brass and aluminium. Fiber laser sheet cutting and surface finishing: zinc plating, anodizing, passivation, blackening, chrome plating.",
        "h1": "CNC services", "lead": "Contract machining on the same equipment that makes our openers. Send a drawing, a 3D model or a sample part and we will quote it.",
        "turning_h": "CNC turning", "turning_p": "Seven CNC STAR automatic lathes produce turned parts from 2 to 20 mm in diameter from bar stock: steel, stainless, brass and aluminium. Typical parts are connectors, spacers, fittings, bushings, pins, screws, nuts and shafts, in series from hundreds to hundreds of thousands.",
        "turning_list": ["Diameter 2 to 20 mm, bar-fed automatic lathes", "Steel, stainless steel, brass, aluminium", "Tolerances measured and documented per batch", "Repeat orders run from the same program, same result"],
        "laser_h": "Fiber laser cutting", "laser_p": "Sheet metal parts cut by fiber laser in steel, aluminium and brass. Clean edges that usually need no further finishing, complex contours and fine detail. Price depends on the number of piercings, the material and the sheet thickness.",
        "laser_list": ["Steel, aluminium, brass sheet", "Smooth edges, minimal post-processing", "From single pieces to series"],
        "finish_h": "Surface protection", "finish_p": "Finished parts can be delivered with the coating your application needs:",
        "finishes": ["Zinc plating", "Anodizing", "Passivation", "Blackening", "Chrome plating"],
        "cta_h": "Have a drawing?", "cta_p": "Send it with the quantity and material and we will come back with a price and lead time.", "cta_b": "Send a drawing",
    },
    "about": {
        "title": "About Us | CNC Metalworking Augustus, Mačvanska Mitrovica",
        "desc": "Family-owned CNC manufacturer in Mačvanska Mitrovica, Serbia. Six years in precision machining, full in-house production of automatic greenhouse openers.",
        "h1": "About us", "lead": "A family-owned CNC manufacturer in Mačvanska Mitrovica, Serbia. We started with precision turning and today make automatic greenhouse openers that ship worldwide.",
        "intro_h": "From turned parts to a finished product",
        "intro_p": [
            "CNC Metalworking Augustus began as a precision turning shop. The opener came out of that experience: a product where the quality of the machined cylinder decides whether the whole thing works, season after season.",
            "Today the complete set is made under one roof. The cylinder, the mechanism and the fixings are machined and assembled here, which keeps the specification stable and lets us answer technical questions directly.",
            "Our customers are distributors and greenhouse manufacturers. Most of them started with a single sample set in their own greenhouse.",
        ],
        "numbers": [("50.000+", "sets per year capacity"), ("350 m²", "production floor"), ("7", "CNC STAR lathes, 1 to 20 mm"), ("6+", "years in precision machining")],
        "prod_h": "Production", "prod_p": "Components are turned, assembled and checked through several controlled steps. We produce through the off-season to build stock, and add capacity when demand grows. Presses and auxiliary machines cover cutting, forming and drilling of the remaining components.",
        "quality_h": "Quality", "quality_p": "We use certified European materials and measure tolerances with modern equipment, so parts match from unit to unit and batch to batch. Every set is inspected before packing, and our quality management system is certified to ISO 9001. Samples are available on request for any product.",
        "cta_h": "Want to see it work?", "cta_p": "Request a sample set and test it in your own greenhouse.",
    },
    "contact": {
        "title": "Contact | Request a Sample or Price List | CNC Metalworking Augustus",
        "desc": "Request a free sample, a price list or a quote for CNC work. CNC Metalworking Augustus, Svetislava Damjanovića 26, Mačvanska Mitrovica, Serbia.",
        "h1": "Contact", "lead": "Ask for a sample, a price list or a quote. We reply within one working day.",
        "form_h": "Send us a request",
        "f_name": "Your name", "f_company": "Company", "f_email": "Email", "f_phone": "Phone (optional)", "f_country": "Country",
        "f_topic": "I am interested in", "topics": ["Free sample set", "Price list", "Quote for CNC work", "Other"],
        "f_qty": "Approximate annual quantity (optional)", "f_msg": "Message",
        "f_send": "Send request", "f_note": "Prefer email? Write to us directly at",
        "info_h": "Company details",
        "i_addr": "Address", "i_phone": "Phone", "i_mail": "Email", "i_hours": "Working hours",
        "hours": "Monday to Friday, 08:00–16:00 (CET)",
        "map_b": "Open in Google Maps",
    },
},
"sr": {
    "lang": "sr",
    "nav": {"products": "Proizvodi", "services": "CNC usluge", "about": "O nama", "contact": "Kontakt", "cta": "Zatražite uzorak"},
    "footer_about": "Proizvođač automatskih otvarača prozora i vrata za staklenike. Kompletna CNC proizvodnja u Mačvanskoj Mitrovici. Snabdevamo distributere i proizvođače staklenika širom sveta.",
    "footer_products": "Proizvodi", "footer_company": "Firma", "footer_contact": "Kontakt",
    "footer_hours": "Pon–Pet 08:00–16:00",
    "rights": "Sva prava zadržana.",
    "cta_band": {
        "h": "Probajte pre nego što naručite.",
        "p": "Distributerima i proizvođačima staklenika šaljemo besplatan probni komplet. Montirajte ga, pustite ga da radi sezonu, pa onda razgovaramo o količinama i cenama direktno.",
        "b1": "Zatražite besplatan uzorak", "b2": "Preuzmite katalog (PDF)",
    },
    "home": {
        "title": "Automatski otvarači za staklenike | Proizvođač | CNC Metalworking Augustus",
        "desc": "Proizvođač automatskih otvarača prozora i vrata za staklenike i plastenike. Sopstvena CNC proizvodnja, kapacitet 50.000+ kompleta godišnje, lager, besplatni uzorci za firme.",
        "eyebrow": "Proizvođač · Mačvanska Mitrovica · Isporuka širom sveta",
        "h1": "Automatski otvarači za staklenike, <em>direktno od proizvođača</em>",
        "lead": "Izrađujemo, sklapamo i držimo na lageru automatske otvarače prozora i vrata za staklenike i plastenike. I mehanizam i cilindar nastaju kod nas, na sopstvenim CNC strugovima. Distributeri i proizvođači staklenika širom sveta, hajde da jedan stavimo u vaš staklenik.",
        "b1": "Zatražite besplatan uzorak", "b2": "Pogledajte proizvode",
        "tag": "Otvarač prozora · 20 kg",
        "strip": [("50.000+", "kompl.", "Godišnji kapacitet"), ("7", "", "CNC STAR strugova"), ("350", "m²", "Proizvodni prostor"), ("6+", "god.", "U preciznoj obradi"), ("2", "god.", "Garancija na svaki komplet")],
        "prod_eyebrow": "Proizvodi", "prod_h": "Otvarači i rezervni delovi od jednog dobavljača.",
        "prod_lead": "Prodaju se kao kompletni setovi, spremni za montažu. Sve ispod se proizvodi i sklapa u našem pogonu.",
        "why_eyebrow": "Zašto direktno", "why_h": "Šta dobijate kada kupujete od proizvođača",
        "why": [
            ("factory", "Sve nastaje kod nas", "Mehanizam i cilindar se obrađuju i sklapaju u našem pogonu. Bez tuđih cilindara i bez razlika između serija."),
            ("box", "Lager spreman za sezonu", "Proizvodimo van sezone, pa su kompleti na polici kada u januaru krene kupovina."),
            ("sample", "Prvo besplatan uzorak", "Testirate otvarač u sopstvenom stakleniku pre nego što odlučite o količini. Bez troška i bez obaveze."),
            ("check", "Ujednačen kvalitet", "Sertifikovani evropski materijali, merene tolerancije i kontrola svakog kompleta pre pakovanja. Sistem kvaliteta sertifikovan po ISO 9001."),
            ("chat", "Direktna veza sa proizvodnjom", "Na pitanja odgovaraju ljudi koji proizvod prave. Izmene, pakovanje, obeležavanje: sve se može dogovoriti."),
            ("truck", "Isporuka širom sveta", "Paletne količine šaljemo bilo gde u svetu, po uslovima dogovorenim za celu sezonu."),
        ],
        "svc_eyebrow": "CNC usluge", "svc_h": "Struganje i lasersko sečenje za vaše proizvode",
        "svc_p": "Isti strugovi na kojima nastaju naši otvarači dostupni su i za uslužnu obradu: precizni strugani delovi od 2 do 20 mm od čelika, inoxa, mesinga i aluminijuma, lasersko sečenje lima i zaštita površine.",
        "svc_b": "Više o CNC uslugama",
    },
    "products": {
        "title": "Proizvodi | Automatski otvarači prozora i vrata za staklenike",
        "desc": "Automatski otvarač prozora za staklenik (20 kg), otvarač vrata (30 kg) i rezervni cilindar. Sopstvena proizvodnja, kompletni setovi, besplatni uzorci za firme.",
        "h1": "Proizvodi", "lead": "Automatski otvarači za prozore i vrata staklenika, plus rezervni cilindar koji odgovara svakom otvaraču na tržištu. Sve iz sopstvene proizvodnje, sve kao kompletni setovi.",
        "cat_b": "Preuzmite katalog (PDF)",
    },
    "cards": {
        "window": ("Automatski otvarač prozora", "Otvarač na toplotni pogon za krovne i bočne prozore staklenika. Dvokraki mehanizam sa oprugom, Easy Clip montaža. Dostupan u cinkovanoj i crnoj varijanti.", ["20 kg", "45 cm", "16–30 °C", "Easy Clip"]),
        "door": ("Automatski otvarač vrata", "Jača jedinica za vrata staklenika i veće otvore. Otvara do 90° za brzo ispuštanje toplote.", ["30 kg", "90°", "18–35 °C"]),
        "cylinder": ("Rezervni cilindar", "Univerzalni cilindar na toplotni pogon koji odgovara svakom automatskom otvaraču. Aluminijumsko telo, inox klip.", ["20 kg", "65 mm", "16–30 °C"]),
    },
    "detail_common": {"crumb": "Proizvodi", "specs_h": "Tehničke specifikacije", "feat_h": "Ključne karakteristike", "gallery_h": "Prikaz proizvoda", "related_h": "Ostali proizvodi", "cta": "Zatražite uzorak", "cat": "Preuzmite katalog (PDF)", "details": "Detalji"},
    "window": {
        "title": "Automatski otvarač prozora za staklenik, 20 kg | CNC Metalworking Augustus",
        "desc": "Automatski otvarač prozora za staklenike i plastenike: sila podizanja 20 kg, otvaranje 45 cm, radni opseg 16–30 °C. Bez struje i baterija. Cinkovani čelik, garancija 2 godine.",
        "h1": "Automatski otvarač prozora", "sub": "Otvarač na toplotni pogon za prozore staklenika. Bez struje, bez baterija, Easy Clip montaža za nekoliko sekundi.",
        "intro": [
            "Otvarač radi na cilindar koji pokreće toplota: kako se vazduh u stakleniku zagreva, cilindar se širi i podiže prozor, a kako se hladi, prozor se zatvara. Počinje da otvara na oko 16 °C, a potpuno je otvoren na 30 °C, pa provetravanje prati temperaturu bez ičijeg angažovanja.",
            "Dvokraki mehanizam sa oprugom daje silu podizanja do 20 kg, dovoljno za teže polikarbonatne i staklene prozore. Easy Clip sistem montira i skida otvarač za nekoliko sekundi i odgovara širokom spektru okvira.",
            "Izrađen od cinkovanog čelika za upotrebu napolju tokom cele godine. Svaki komplet se kontroliše pre pakovanja i pokriven je garancijom proizvođača od 2 godine.",
        ],
        "specs": [("Sila podizanja", "do 20 kg"), ("Maksimalno otvaranje", "45 cm"), ("Hod cilindra", "65 mm"), ("Radni opseg", "16–30 °C"), ("Napajanje", "nema, cilindar na toplotu"), ("Materijal", "cinkovani čelik"), ("Završna obrada", "cinkovana ili crna"), ("Montaža", "Easy Clip, bez alata"), ("Garancija", "2 godine")],
        "features": [("Kreće na 16 °C, otvoren na 30 °C", "Provetravanje prati temperaturu automatski."), ("Sila podizanja 20 kg", "Nosi teže prozore sa rezervom."), ("Montaža za sekunde", "Easy Clip fiksiranje, odgovara većini profila."), ("Cinkovani čelik", "Otporan na koroziju, napravljen za godine napolju.")],
        "versions": ("Dve verzije", "Isti mehanizam, iste specifikacije. Verzije se u cenovniku vode kao dva artikla.", [("window-opener.jpg", "Otvarač prozora · Cinkovani", "Klasična cinkovana završna obrada."), ("window-opener-black.jpg", "Otvarač prozora · Crni", "Crna završna obrada.")]),
        "gallery": [("window-opener-detail.jpg", "Dvokraki mehanizam i tačke montaže"), ("window-opener-black-detail.jpg", "Crna verzija, dvokraki mehanizam")],
    },
    "door": {
        "title": "Automatski otvarač vrata za staklenik, 30 kg | CNC Metalworking Augustus",
        "desc": "Automatski otvarač vrata za staklenike: potisna sila 30 kg, hod 110 mm, otvaranje do 90°. Radni opseg 18–35 °C. Bez struje, cinkovani čelik, garancija 2 godine.",
        "h1": "Automatski otvarač vrata", "sub": "Napravljen za vrata staklenika i veće otvore. Otvara do 90°.",
        "intro": [
            "Otvarač vrata radi na istom principu kao otvarač prozora, sa jačim cilindrom i dužim hodom. Reaguje između 18 °C i 35 °C: gura vrata dok se staklenik zagreva i zatvara ih kada temperatura padne.",
            "Sa silom do 30 kg i hodom od 110 mm otvara vrata do 90°, što daje najbrže ispuštanje toplote u vrele dane. Namenjen je težim vratima i većim otvorima gde otvarač prozora ne bi bio dovoljan.",
            "Konstrukcija od cinkovanog čelika za dug rad napolju. Brzo se montira na većinu okvira vrata staklenika. Garancija proizvođača 2 godine.",
        ],
        "specs": [("Potisna sila", "do 30 kg"), ("Maksimalno otvaranje", "90°"), ("Hod cilindra", "110 mm"), ("Radni opseg", "18–35 °C"), ("Napajanje", "nema, cilindar na toplotu"), ("Materijal", "cinkovani čelik"), ("Garancija", "2 godine")],
        "features": [("Otvara do 90°", "Potpuno otvaranje za maksimalan protok vazduha."), ("Sila 30 kg", "Za teža vrata i veće otvore."), ("Opseg 18–35 °C", "Širi opseg za toplije klime i velike zapremine."), ("Cinkovani čelik", "Stabilan rad sezonu za sezonom.")],
        "gallery": [("door-opener-set.jpg", "Kompletan set: cilindar, opruga, kraci i nosači za montažu"), ("door-opener-detail-1.jpg", "Cilindar, zglob i nosač sa prorezima"), ("door-opener-detail-2.jpg", "Opruga pričvršćena na vijak nosača"), ("door-opener-detail-3.jpg", "Klipnjača sa navojem, hod 110 mm")],
    },
    "cylinder": {
        "title": "Rezervni cilindar za automatske otvarače staklenika | CNC Metalworking Augustus",
        "desc": "Univerzalni rezervni cilindar koji odgovara svakom automatskom otvaraču staklenika. Sila 20 kg, hod 65 mm, 16–30 °C. Aluminijumsko telo, klip od nerđajućeg čelika, sopstvena proizvodnja.",
        "h1": "Rezervni cilindar", "sub": "Univerzalni cilindar na toplotni pogon za svaki automatski otvarač.",
        "intro": [
            "Cilindar je srce svakog automatskog otvarača i deo koji se vremenom menja. Naš odgovara svakom otvaraču na tržištu, pa je praktičan rezervni deo za distributere i servisni artikal za vlasnike staklenika.",
            "Daje silu do 20 kg uz hod od 65 mm i aktivira se između 16 °C i 30 °C. Telo je obrađeno od aluminijuma, klip od nerđajućeg čelika, završna obrada u crnoj boji.",
            "Cilindre proizvodimo sami, na istim strugovima kao i ostatak otvarača, pa su specifikacije iste iz serije u seriju.",
        ],
        "specs": [("Sila", "do 20 kg"), ("Hod", "65 mm"), ("Radni opseg", "16–30 °C"), ("Telo", "aluminijum, crna obrada"), ("Klip", "nerđajući čelik"), ("Kompatibilnost", "svi automatski otvarači"), ("Garancija", "2 godine")],
        "features": [("Odgovara svakom otvaraču", "Univerzalna zamena, koji god otvarač da koristite."), ("Sopstvena proizvodnja", "Obrađen na našim strugovima, ista specifikacija u svakoj seriji."), ("Aluminijum i inox", "Lak, otporan na koroziju, za upotrebu napolju."), ("Aktivacija 16–30 °C", "Potpuno usklađen sa otvaračem prozora.")],
        "gallery": [("replacement-cylinder.jpg", "Rezervni cilindar sa inox klipom")],
    },
    "services": {
        "title": "CNC struganje i lasersko sečenje | CNC Metalworking Augustus",
        "desc": "Precizni strugani delovi od 2 do 20 mm od čelika, inoxa, mesinga i aluminijuma. Lasersko sečenje lima fiber laserom i zaštita površine: cinkovanje, eloksiranje, pasivizacija, bruniranje, hromiranje.",
        "h1": "CNC usluge", "lead": "Uslužna obrada na istoj opremi na kojoj nastaju naši otvarači. Pošaljite crtež, 3D model ili uzorak dela i dobićete ponudu.",
        "turning_h": "CNC struganje", "turning_p": "Sedam CNC STAR automatskih strugova izrađuje strugane delove prečnika od 2 do 20 mm iz šipkastog materijala: čelik, inox, mesing i aluminijum. Tipični delovi su konektori, odstojnici, priključci, čaure, čivije, vijci, matice i osovine, u serijama od stotina do stotina hiljada komada.",
        "turning_list": ["Prečnik 2 do 20 mm, automatski strugovi sa dodavačem šipke", "Čelik, nerđajući čelik, mesing, aluminijum", "Tolerancije merene i dokumentovane po seriji", "Ponovljene narudžbine idu iz istog programa, isti rezultat"],
        "laser_h": "Lasersko sečenje fiber laserom", "laser_p": "Delovi od lima sečeni fiber laserom od čelika, aluminijuma i mesinga. Čiste ivice kojima najčešće ne treba dodatna obrada, složene konture i fini detalji. Cena zavisi od broja probijanja, vrste metala i debljine lima.",
        "laser_list": ["Lim od čelika, aluminijuma, mesinga", "Glatke ivice, minimalna naknadna obrada", "Od pojedinačnih komada do serija"],
        "finish_h": "Zaštita površine", "finish_p": "Gotove delove možemo isporučiti sa zaštitom koju vaša primena zahteva:",
        "finishes": ["Cinkovanje", "Eloksiranje", "Pasivizacija", "Bruniranje", "Hromiranje"],
        "cta_h": "Imate crtež?", "cta_p": "Pošaljite ga sa količinom i materijalom i javljamo vam cenu i rok.", "cta_b": "Pošaljite crtež",
    },
    "about": {
        "title": "O nama | CNC Metalworking Augustus, Mačvanska Mitrovica",
        "desc": "Porodična CNC firma iz Mačvanske Mitrovice. Šest godina u preciznoj obradi, kompletna sopstvena proizvodnja automatskih otvarača za staklenike.",
        "h1": "O nama", "lead": "Porodična CNC firma iz Mačvanske Mitrovice. Počeli smo sa preciznim struganjem, a danas pravimo automatske otvarače za staklenike koji se isporučuju širom sveta.",
        "intro_h": "Od struganih delova do gotovog proizvoda",
        "intro_p": [
            "CNC Metalworking Augustus je nastao kao radionica za precizno struganje. Otvarač je izašao iz tog iskustva: proizvod kod kojeg kvalitet obrađenog cilindra odlučuje da li cela stvar radi, sezonu za sezonom.",
            "Danas se kompletan set pravi pod jednim krovom. Cilindar, mehanizam i pribor za montažu se obrađuju i sklapaju ovde, što drži specifikaciju stabilnom i omogućava da na tehnička pitanja odgovorimo direktno.",
            "Naši kupci su distributeri i proizvođači staklenika. Većina je počela od jednog probnog kompleta u sopstvenom stakleniku.",
        ],
        "numbers": [("50.000+", "kompleta godišnje, kapacitet"), ("350 m²", "proizvodnog prostora"), ("7", "CNC STAR strugova, 1 do 20 mm"), ("6+", "godina u preciznoj obradi")],
        "prod_h": "Proizvodnja", "prod_p": "Komponente se stružu, sklapaju i kontrolišu kroz više kontrolisanih koraka. Proizvodimo van sezone da napravimo lager, a kapacitete širimo kako potražnja raste. Prese i pomoćne mašine pokrivaju sečenje, oblikovanje i bušenje ostalih komponenti.",
        "quality_h": "Kvalitet", "quality_p": "Koristimo sertifikovane evropske materijale, a tolerancije merimo modernom opremom, pa se delovi poklapaju od komada do komada i od serije do serije. Svaki komplet se kontroliše pre pakovanja, a sistem upravljanja kvalitetom sertifikovan je po standardu ISO 9001. Uzorci su dostupni na zahtev za svaki proizvod.",
        "cta_h": "Želite da vidite kako radi?", "cta_p": "Zatražite probni komplet i testirajte ga u sopstvenom stakleniku.",
    },
    "contact": {
        "title": "Kontakt | Zatražite uzorak ili cenovnik | CNC Metalworking Augustus",
        "desc": "Zatražite besplatan uzorak, cenovnik ili ponudu za CNC obradu. CNC Metalworking Augustus, Svetislava Damjanovića 26, Mačvanska Mitrovica.",
        "h1": "Kontakt", "lead": "Zatražite uzorak, cenovnik ili ponudu. Odgovaramo u roku od jednog radnog dana.",
        "form_h": "Pošaljite upit",
        "f_name": "Vaše ime", "f_company": "Firma", "f_email": "Email", "f_phone": "Telefon (opciono)", "f_country": "Zemlja",
        "f_topic": "Zanima me", "topics": ["Besplatan probni komplet", "Cenovnik", "Ponuda za CNC obradu", "Drugo"],
        "f_qty": "Okvirna godišnja količina (opciono)", "f_msg": "Poruka",
        "f_send": "Pošaljite upit", "f_note": "Više volite email? Pišite nam direktno na",
        "info_h": "Podaci o firmi",
        "i_addr": "Adresa", "i_phone": "Telefon", "i_mail": "Email", "i_hours": "Radno vreme",
        "hours": "Ponedeljak do petak, 08:00–16:00",
        "map_b": "Otvori u Google mapama",
    },
},
}

# ---------------------------------------------------------------- helpers
def rel(frm, to):
    d = posixpath.dirname(frm)
    r = posixpath.relpath(to, d) if d else to
    return r

def esc(s):
    return s

def head(lang, key, t, page, extra_css=""):
    me = PAGES[key][lang]; en = PAGES[key]["en"]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{PAGES[key][l]}">\n' for l in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page["title"]}</title>
<meta name="description" content="{page["desc"]}">
<link rel="canonical" href="{DOMAIN}/{me}">
{alts}<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{en}">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}/{me}">
<meta property="og:image" content="{DOMAIN}/assets/img/window-opener.jpg">
<link rel="icon" href="{rel(me,'favicon.ico')}" sizes="any">
<link rel="icon" type="image/png" href="{rel(me,'assets/img/favicon.png')}">
<link rel="apple-touch-icon" href="{rel(me,'assets/img/apple-touch-icon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel(me,'assets/css/style.css')}">
{extra_css}</head>
<body>
"""

def nav(lang, key, t):
    me = PAGES[key][lang]; n = t["nav"]
    def link(k, label):
        cls = ' class="active"' if key == k or (k == "products" and key in ("window","door","cylinder")) else ""
        return f'<li><a href="{rel(me, PAGES[k][lang])}"{cls}>{label}</a></li>'
    langs = "".join(f'<a href="{rel(me, PAGES[key][l])}" {"class=\"active\"" if l==lang else ""} hreflang="{l}" lang="{l}">{LANG_LABEL[l]}</a>' for l in LANGS)
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{rel(me, PAGES['home'][lang])}" aria-label="CNC Metalworking Augustus"><img src="{rel(me,'assets/img/logo-white.png')}" alt="CNC Metalworking Augustus" width="166" height="42"></a>
    <ul class="nav-links" id="navLinks">
      {link("products", n["products"])}
      {link("services", n["services"])}
      {link("about", n["about"])}
      {link("contact", n["contact"])}
    </ul>
    <div class="nav-right">
      <nav class="lang" aria-label="Language">
        {langs}
      </nav>
      <a class="btn btn-primary" href="{rel(me, PAGES['contact'][lang])}">{n["cta"]}</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

def footer(lang, key, t):
    me = PAGES[key][lang]; n = t["nav"]; c = T[lang]["cards"]
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{rel(me, PAGES['home'][lang])}"><img src="{rel(me,'assets/img/logo-white.png')}" alt="CNC Metalworking Augustus"></a>
        <p>{t["footer_about"]}</p>
        <div class="social">
          <a href="{SOCIAL['instagram']}" target="_blank" rel="noopener" aria-label="Instagram">{ICONS['instagram']}</a>
          <a href="{SOCIAL['tiktok']}" target="_blank" rel="noopener" aria-label="TikTok">{ICONS['tiktok']}</a>
          <a href="{SOCIAL['facebook']}" target="_blank" rel="noopener" aria-label="Facebook">{ICONS['facebook']}</a>
        </div>
        <img src="{rel(me,'assets/img/iso-9001-badge.png')}" alt="ISO 9001:2015 certified company" width="92" height="92" style="margin-top:1.2rem" loading="lazy">
      </div>
      <div>
        <h4>{t["footer_products"]}</h4>
        <ul>
          <li><a href="{rel(me, PAGES['window'][lang])}">{c['window'][0]}</a></li>
          <li><a href="{rel(me, PAGES['door'][lang])}">{c['door'][0]}</a></li>
          <li><a href="{rel(me, PAGES['cylinder'][lang])}">{c['cylinder'][0]}</a></li>
          <li><a href="{rel(me, PAGES['services'][lang])}">{n['services']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t["footer_company"]}</h4>
        <ul>
          <li><a href="{rel(me, PAGES['about'][lang])}">{n['about']}</a></li>
          <li><a href="{rel(me, PAGES['contact'][lang])}">{n['contact']}</a></li>
          <li><a href="{rel(me,'downloads/catalogue-2027.pdf')}">{t['cta_band']['b2']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t["footer_contact"]}</h4>
        <ul>
          <li>{ADDRESS}</li>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{t["footer_hours"]}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 CNC Metalworking Augustus. {t["rights"]}</span>
      <span>Mačvanska Mitrovica, Srbija</span>
    </div>
  </div>
</footer>
<script src="{rel(me,'assets/js/main.js')}"></script>
</body>
</html>
"""

def cta_band(lang, key, t):
    me = PAGES[key][lang]; b = t["cta_band"]
    return f"""<section class="cta-band">
  <div class="container">
    <div><h2>{b["h"]}</h2><p>{b["p"]}</p></div>
    <div class="actions">
      <a class="btn btn-primary btn-lg" href="{rel(me, PAGES['contact'][lang])}">{b["b1"]}</a>
      <a class="btn btn-outline" href="{rel(me,'downloads/catalogue-2027.pdf')}">{b["b2"]}</a>
    </div>
  </div>
</section>
"""

IMG = {"window": "window-opener-sm.jpg", "door": "door-opener-sm.jpg", "cylinder": "replacement-cylinder-sm.jpg"}

def product_cards(lang, key, t, exclude=None):
    me = PAGES[key][lang]; out = []
    for k in ("window", "door", "cylinder"):
        if k == exclude: continue
        name, desc, chips = t["cards"][k]
        chips_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
        out.append(f"""<a class="card" href="{rel(me, PAGES[k][lang])}">
  <div class="card-media"><img src="{rel(me,'assets/img/'+IMG[k])}" alt="{name}" loading="lazy"></div>
  <div class="card-body">
    <h3>{name}</h3>
    <div class="card-specs">{chips_html}</div>
    <p>{desc}</p>
    <span class="card-link">{t['detail_common']['details']}</span>
  </div>
</a>""")
    return "\n".join(out)

# ---------------------------------------------------------------- pages
def page_home(lang, t):
    key = "home"; me = PAGES[key][lang]; p = t["home"]
    strip = "".join(f'<div class="cell"><div class="val">{v}<small>{u}</small></div><div class="lbl">{l}</div></div>' for v,u,l in p["strip"])
    why = "".join(f'<div class="feature"><div class="icon">{ICONS[i]}</div><h3>{h}</h3><p>{d}</p></div>' for i,h,d in p["why"])
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-grid">
      <div>
        <div class="eyebrow">{p["eyebrow"]}</div>
        <h1>{p["h1"]}</h1>
        <p class="lead">{p["lead"]}</p>
        <div class="btn-group">
          <a class="btn btn-primary btn-lg" href="{rel(me, PAGES['contact'][lang])}">{p["b1"]}</a>
          <a class="btn btn-outline btn-lg" href="{rel(me, PAGES['products'][lang])}">{p["b2"]}</a>
        </div>
      </div>
      <div class="hero-media">
        <div class="plate"><img src="{rel(me,'assets/img/window-opener.jpg')}" alt="{t['cards']['window'][0]}" width="1400" height="1159" fetchpriority="high"></div>
        <div class="tag">{p["tag"]}</div>
      </div>
    </div>
  </div>
  <div class="spec-strip"><div class="container">{strip}</div></div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">{p["prod_eyebrow"]}</div>
      <h2>{p["prod_h"]}</h2>
      <p class="lead">{p["prod_lead"]}</p>
    </div>
    <div class="grid-3">{product_cards(lang, key, t)}</div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">{p["why_eyebrow"]}</div>
      <h2>{p["why_h"]}</h2>
    </div>
    <div class="grid-3">{why}</div>
  </div>
</section>

<section class="section">
  <div class="container split wide-media">
    <div><img src="{rel(me,'assets/img/cnc-hall.jpg')}" alt="CNC STAR lathes" loading="lazy" width="1800" height="1200"></div>
    <div>
      <div class="eyebrow">{p["svc_eyebrow"]}</div>
      <h2>{p["svc_h"]}</h2>
      <p class="lead">{p["svc_p"]}</p>
      <p style="margin-top:1.5rem"><a class="btn btn-outline-dark" href="{rel(me, PAGES['services'][lang])}">{p["svc_b"]}</a></p>
    </div>
  </div>
</section>

{cta_band(lang, key, t)}
</main>
""" + footer(lang, key, t)

def page_products(lang, t):
    key = "products"; me = PAGES[key][lang]; p = t["products"]
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="page-intro">
  <div class="container">
    <h1>{p["h1"]}</h1>
    <p class="lead">{p["lead"]}</p>
    <p style="margin-top:1.5rem"><a class="btn btn-outline" href="{rel(me,'downloads/catalogue-2027.pdf')}">{p["cat_b"]}</a></p>
  </div>
</section>
<section class="section">
  <div class="container"><div class="grid-3">{product_cards(lang, key, t)}</div></div>
</section>
{cta_band(lang, key, t)}
</main>
""" + footer(lang, key, t)

def page_detail(lang, t, key):
    me = PAGES[key][lang]; p = t[key]; dc = t["detail_common"]
    intro = "".join(f"<p>{x}</p>" for x in p["intro"])
    specs = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a,b in p["specs"])
    feats = "".join(f'<div class="feature"><div class="icon">{ICONS["check"]}</div><h3>{h}</h3><p>{d}</p></div>' for h,d in p["features"])
    gallery = "".join(f'<figure><img src="{rel(me,"assets/img/"+f)}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f,c in p["gallery"])
    versions = ""
    if "versions" in p:
        vh, vlead, vitems = p["versions"]
        vcards = "".join('<div class="card"><div class="card-media"><img src="' + rel(me,'assets/img/'+img) + '" alt="' + name + '" loading="lazy"></div><div class="card-body"><h3>' + name + '</h3><p>' + d + '</p></div></div>' for img,name,d in vitems)
        versions = '<section class="section section--white"><div class="container"><h2>' + vh + '</h2><p class="lead" style="margin-top:0.5rem">' + vlead + '</p><div class="grid-2" style="margin-top:2rem;max-width:820px">' + vcards + '</div></div></section>'
    hero_img = {"window": "window-opener.jpg", "door": "door-opener.jpg", "cylinder": "replacement-cylinder.jpg"}[key]
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="product-hero">
  <div class="container">
    <div class="crumbs"><a href="{rel(me, PAGES['products'][lang])}">{dc["crumb"]}</a> / {p["h1"]}</div>
    <div class="split">
      <div>
        <h1>{p["h1"]}</h1>
        <p class="lead">{p["sub"]}</p>
        <div class="btn-group" style="margin-top:1.5rem">
          <a class="btn btn-primary btn-lg" href="{rel(me, PAGES['contact'][lang])}">{dc["cta"]}</a>
          <a class="btn btn-outline" href="{rel(me,'downloads/catalogue-2027.pdf')}">{dc["cat"]}</a>
        </div>
      </div>
      <div class="plate"><img src="{rel(me,'assets/img/'+hero_img)}" alt="{p['h1']}" fetchpriority="high"></div>
    </div>
  </div>
</section>

{versions}

<section class="section">
  <div class="container split">
    <div class="lead" style="font-size:1.05rem">{intro}</div>
    <div>
      <h2 style="font-size:1.4rem">{dc["specs_h"]}</h2>
      <table class="spec-table">{specs}</table>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <h2>{dc["feat_h"]}</h2>
    <div class="grid-4" style="margin-top:2rem">{feats}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>{dc["gallery_h"]}</h2>
    <div class="gallery" style="margin-top:2rem">{gallery}</div>
  </div>
</section>

{cta_band(lang, key, t)}

<section class="section">
  <div class="container">
    <h2>{dc["related_h"]}</h2>
    <div class="grid-2" style="margin-top:2rem;max-width:820px">{product_cards(lang, key, t, exclude=key)}</div>
  </div>
</section>
</main>
""" + footer(lang, key, t)

def page_services(lang, t):
    key = "services"; me = PAGES[key][lang]; p = t["services"]
    tl = "".join(f"<li>{x}</li>" for x in p["turning_list"])
    ll = "".join(f"<li>{x}</li>" for x in p["laser_list"])
    fin = "".join(f'<div class="finish">{x}</div>' for x in p["finishes"])
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="page-intro">
  <div class="container"><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p></div>
</section>

<section class="section">
  <div class="container">
    <div class="service">
      <div class="media"><img src="{rel(me,'assets/img/cnc-hall.jpg')}" alt="{p['turning_h']}" loading="lazy"></div>
      <div>
                <h2>{p["turning_h"]}</h2>
        <p>{p["turning_p"]}</p>
        <ul class="check-list">{tl}</ul>
      </div>
    </div>
    <div class="service reverse">
      <div class="media"><img src="{rel(me,'assets/img/laser-cutting.jpg')}" alt="{p['laser_h']}" loading="lazy"></div>
      <div>
                <h2>{p["laser_h"]}</h2>
        <p>{p["laser_p"]}</p>
        <ul class="check-list">{ll}</ul>
      </div>
    </div>
    <div class="service">
      <div class="media"><img src="{rel(me,'assets/img/turned-parts.jpg')}" alt="{p['finish_h']}" loading="lazy"></div>
      <div>
                <h2>{p["finish_h"]}</h2>
        <p>{p["finish_p"]}</p>
        <div class="finish-grid" style="grid-template-columns:repeat(2,1fr);margin-top:1.25rem">{fin}</div>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div><h2>{p["cta_h"]}</h2><p>{p["cta_p"]}</p></div>
    <div class="actions"><a class="btn btn-primary btn-lg" href="{rel(me, PAGES['contact'][lang])}">{p["cta_b"]}</a></div>
  </div>
</section>
</main>
""" + footer(lang, key, t)

def page_about(lang, t):
    key = "about"; me = PAGES[key][lang]; p = t["about"]
    intro = "".join(f"<p>{x}</p>" for x in p["intro_p"])
    nums = "".join(f'<div class="number"><div class="val">{v}</div><div class="lbl">{l}</div></div>' for v,l in p["numbers"])
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="page-intro">
  <div class="container"><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p></div>
</section>

<section class="section">
  <div class="container split">
    <div><img src="{rel(me,'assets/img/facility.jpg')}" alt="CNC Metalworking Augustus, Mačvanska Mitrovica" loading="lazy"></div>
    <div><h2>{p["intro_h"]}</h2>{intro}</div>
  </div>
</section>

<section class="section section--white">
  <div class="container"><div class="numbers">{nums}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div><h2>{p["prod_h"]}</h2><p>{p["prod_p"]}</p></div>
    <div><div style="display:flex;align-items:flex-start;justify-content:space-between;gap:1.5rem"><h2>{p["quality_h"]}</h2><img src="{rel(me,'assets/img/iso-9001-badge.png')}" alt="ISO 9001:2015 certified company" width="112" height="112" style="flex:none;box-shadow:none;border-radius:0"></div><p>{p["quality_p"]}</p></div>
  </div>
</section>

<section class="section section--dark">
  <div class="container split">
    <div><img src="{rel(me,'assets/img/cnc-hall.jpg')}" alt="CNC STAR lathes" loading="lazy"></div>
    <div>
      <h2>{p["cta_h"]}</h2>
      <p class="lead">{p["cta_p"]}</p>
      <p style="margin-top:1.5rem"><a class="btn btn-primary btn-lg" href="{rel(me, PAGES['contact'][lang])}">{t['cta_band']['b1']}</a></p>
    </div>
  </div>
</section>
</main>
""" + footer(lang, key, t)

def page_contact(lang, t):
    key = "contact"; me = PAGES[key][lang]; p = t["contact"]
    topics = "".join(f'<option>{x}</option>' for x in p["topics"])
    return head(lang, key, t, p) + nav(lang, key, t) + f"""<main>
<section class="page-intro">
  <div class="container"><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p></div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="form-card">
      <h2 style="font-size:1.4rem">{p["form_h"]}</h2>
      <form data-contact action="{FORM_ACTION}" method="POST">
        <input type="hidden" name="_subject" value="Website request ({lang.upper()})">
        <input type="hidden" name="_language" value="{lang}">
        <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off">
        <div class="form-row">
          <div class="field"><label for="name">{p["f_name"]}</label><input id="name" name="name" required></div>
          <div class="field"><label for="company">{p["f_company"]}</label><input id="company" name="company" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="email">{p["f_email"]}</label><input id="email" name="email" type="email" required></div>
          <div class="field"><label for="phone">{p["f_phone"]}</label><input id="phone" name="phone" type="tel"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="country">{p["f_country"]}</label><input id="country" name="country" required></div>
          <div class="field"><label for="topic">{p["f_topic"]}</label><select id="topic" name="topic">{topics}</select></div>
        </div>
        <div class="field"><label for="qty">{p["f_qty"]}</label><input id="qty" name="quantity"></div>
        <div class="field"><label for="message">{p["f_msg"]}</label><textarea id="message" name="message" required></textarea></div>
        <button class="btn btn-primary btn-lg" type="submit">{p["f_send"]}</button>
        <p class="form-note">{p["f_note"]} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </form>
    </div>
    <div>
      <h2 style="font-size:1.4rem">{p["info_h"]}</h2>
      <ul class="info-list">
        <li><div class="ico">{ICONS['pin']}</div><div><strong>{p["i_addr"]}</strong>{ADDRESS}<br>Srbija / Serbia</div></li>
        <li><div class="ico">{ICONS['phone']}</div><div><strong>{p["i_phone"]}</strong><a href="tel:{PHONE_TEL}">{PHONE}</a></div></li>
        <li><div class="ico">{ICONS['mail']}</div><div><strong>{p["i_mail"]}</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li><div class="ico">{ICONS['clock']}</div><div><strong>{p["i_hours"]}</strong>{p["hours"]}</div></li>
      </ul>
      <div class="map">
        <iframe src="https://www.google.com/maps?q=Svetislava+Damjanovi%C4%87a+26,+Ma%C4%8Dvanska+Mitrovica,+Serbia&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="CNC Metalworking Augustus, Mačvanska Mitrovica"></iframe>
      </div>
      <p style="margin-top:0.75rem"><a href="https://www.google.com/maps/search/?api=1&query=Svetislava+Damjanovi%C4%87a+26,+Ma%C4%8Dvanska+Mitrovica" target="_blank" rel="noopener">{p["map_b"]} →</a></p>
    </div>
  </div>
</section>
</main>
""" + footer(lang, key, t)

# ---------------------------------------------------------------- build
def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

from i18n_extra import T_EXTRA
T.update(T_EXTRA)

for lang in LANGS:
    t = T[lang]
    write(PAGES["home"][lang], page_home(lang, t))
    write(PAGES["products"][lang], page_products(lang, t))
    for k in ("window", "door", "cylinder"):
        write(PAGES[k][lang], page_detail(lang, t, k))
    write(PAGES["services"][lang], page_services(lang, t))
    write(PAGES["about"][lang], page_about(lang, t))
    write(PAGES["contact"][lang], page_contact(lang, t))

# sitemap + robots
urls = [PAGES[k][l] for k in PAGES for l in LANGS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{u}</loc></url>\n" for u in urls) + "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("built", len(urls), "pages")
