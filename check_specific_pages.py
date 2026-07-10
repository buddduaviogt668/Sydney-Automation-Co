import os

pages = [
    'smart-home-automation-lindfield.html',
    'electricians.html',
    'strata.html',
    'guides.html',
    'lighting-control-rose-bay.html',
    'cbus-programming-chatswood.html',
    'lighting-automation-st-ives.html',
    'dynalite-vs-cbus-sydney.html',
    'cbus-vs-dynalite.html',
    'emergency-repair-sydney.html',
    'cbus-repair-kiama.html',
    'cbus-repair-mosman.html',
    'cbus-repair-pymble.html',
    'dynalite-programmer-clovelly.html',
    'dynalite-repair-bowral.html'
]

for p in pages:
    exists = os.path.exists(p)
    print(f"{p}: {'Exists' if exists else 'DELETED'}")
