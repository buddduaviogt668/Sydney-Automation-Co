import os

check_list = [
    'cbus-maintenance-sydney.html',
    'how-to-choose-cbus-specialist-sydney.html',
    'what-is-rapix-sydney-buildings.html',
    'c-bus-repairs-sydney.html',
    'dynalite-fault-finding-sydney-common-faults.html',
    'cbus-relay-making-buzzing-noise-sydney.html',
    'dynalite-maintenance-sydney.html',
    'building-automation-maintenance-sydney.html',
    'building-manager-lighting-support-sydney.html',
    'cbus-fault-finding-sydney.html',
    'rapix-emergency-lighting-sydney.html',
    'cbus-automation-north-shore-sydney.html',
    'c-bus-vs-dynalite-vs-knx-comparison-sydney.html'
]

for file in check_list:
    exists = os.path.exists(file)
    print(f"{file}: {'Exists' if exists else 'DELETED'}")
