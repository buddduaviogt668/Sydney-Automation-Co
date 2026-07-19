#!/usr/bin/env python3
with open("projects.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

uluru_gallery = """,uluru:[{"src": "/uluru-01-venue.jpeg", "title": "Uluru Meeting Place \u2014 Ayers Rock Resort, Ballroom"}, {"src": "/uluru-02-banquet-setup.jpeg", "title": "Uluru Meeting Place \u2014 Banquet Setup"}, {"src": "/uluru-03-ballroom-evening.jpg", "title": "Uluru Meeting Place \u2014 Ballroom Evening"}, {"src": "/uluru-04-ballroom-setup.jpg", "title": "Uluru Meeting Place \u2014 Ballroom Pre-Event Setup"}, {"src": "/uluru-05-foyer-evening.jpg", "title": "Uluru Meeting Place \u2014 Foyer Evening"}, {"src": "/uluru-06-morning-setup.jpg", "title": "Uluru Meeting Place \u2014 Morning Setup"}]"""

old = "}]};\nvar currentGallery"
new = uluru_gallery + old

if old in html:
    html = html.replace(old, new)
    with open("projects.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Uluru gallery added to lightbox JS")
else:
    print("ERROR: pattern not found")
    print("Looking for:", repr(old[:50]))
    idx = html.find("var currentGallery")
    print("Context:", repr(html[idx-30:idx+30]))
