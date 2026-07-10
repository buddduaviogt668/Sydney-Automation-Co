import os
from urllib.parse import urlparse

gsc_raw_text = """
https://sydneyautomationco.com.au/
https://www.sydneyautomationco.com.au/
https://sydneyautomationco.com.au/products
https://sydneyautomationco.com.au/cbus-vs-dynalite
https://sydneyautomationco.com.au/c-bus-apple-homekit-sydney
https://sydneyautomationco.com.au/cbus-maintenance-sydney
https://sydneyautomationco.com.au/dynalite-vs-cbus-sydney
https://sydneyautomationco.com.au/cbus-specialist-sydney
https://sydneyautomationco.com.au/cbus-repair-sydney
https://sydneyautomationco.com.au/dynalite-repair-sydney
https://sydneyautomationco.com.au/how-to-choose-cbus-specialist-sydney
https://sydneyautomationco.com.au/locations
https://sydneyautomationco.com.au/what-is-rapix-sydney-buildings
https://sydneyautomationco.com.au/dynalite-programmer-sydney
https://sydneyautomationco.com.au/c-bus-programmer-sydney
https://sydneyautomationco.com.au/c-bus-repairs-sydney
https://sydneyautomationco.com.au/contact
https://sydneyautomationco.com.au/shire
https://sydneyautomationco.com.au/about
https://sydneyautomationco.com.au/lighting-control-service-sydney
https://sydneyautomationco.com.au/dali2-compliance-nsw-commercial
https://sydneyautomationco.com.au/cbus-upgrade-sydney
https://sydneyautomationco.com.au/smart-home-automation-mosman
https://sydneyautomationco.com.au/c-bus-programmer-eastern-suburbs
https://sydneyautomationco.com.au/cbus-toolkit-software-cannot-connect-sydney
https://sydneyautomationco.com.au/cbus-dynalite-upgrade-guide
https://sydneyautomationco.com.au/book-service
https://sydneyautomationco.com.au/c-bus-programmer-sydney.html
https://sydneyautomationco.com.au/c-bus-repairs-sydney.html
https://sydneyautomationco.com.au/c-bus-programmer-northern-beaches
https://www.sydneyautomationco.com.au/cbus-maintenance-sydney.html
https://sydneyautomationco.com.au/dynalite-fault-finding-sydney-common-faults
https://sydneyautomationco.com.au/cbus-relay-making-buzzing-noise-sydney
https://sydneyautomationco.com.au/cbus-repair-mosman
https://sydneyautomationco.com.au/blog-strata-lighting-energy-savings-sydney
https://sydneyautomationco.com.au/carpark-lighting-upgrades-sydney
https://sydneyautomationco.com.au/smart-home-sydney-cbd
https://sydneyautomationco.com.au/blog
https://sydneyautomationco.com.au/dynalite-maintenance-sydney
https://sydneyautomationco.com.au/building-automation-maintenance-sydney
https://sydneyautomationco.com.au/building-manager-lighting-support-sydney
https://sydneyautomationco.com.au/cbus-fault-finding-sydney
https://sydneyautomationco.com.au/emergency-lighting-compliance-afss-sydney
https://sydneyautomationco.com.au/rapix-emergency-lighting-sydney
https://sydneyautomationco.com.au/cbus-fault-finding-sydney.html
https://sydneyautomationco.com.au/c-bus-programmer-north-shore
https://www.sydneyautomationco.com.au/building-lighting-upgrades-sydney.html
https://sydneyautomationco.com.au/c-bus-programmer-inner-west
https://sydneyautomationco.com.au/blog-cbus-dimmer-module-failure-sydney
https://sydneyautomationco.com.au/cbus-repair-burradoo
https://sydneyautomationco.com.au/blog-dynalite-voltage-drop-issues-sydney
https://sydneyautomationco.com.au/blog-dynalite-relay-module-testing-sydney
https://www.sydneyautomationco.com.au/electricians.html
https://sydneyautomationco.com.au/blog-cbus-relay-stuck-closed-sydney
https://sydneyautomationco.com.au/cbus-repair-manly
https://sydneyautomationco.com.au/blog-dali2-group-addressing-guide-sydney
https://www.sydneyautomationco.com.au/emergency-lighting-train-stations-infrastructure-sydney.html
https://sydneyautomationco.com.au/rapix-to-cbus-dynalite-migration-sydney
https://sydneyautomationco.com.au/blog-hotel-guest-room-automation-sydney
https://sydneyautomationco.com.au/c-bus-vs-dynalite-vs-knx-comparison-sydney
https://sydneyautomationco.com.au/blog/dynalite-troubleshooting-guide-sydney
https://sydneyautomationco.com.au/cbus-automation-north-shore-sydney
https://sydneyautomationco.com.au/c-bus-programmer-mosman
https://sydneyautomationco.com.au/electricians
https://sydneyautomationco.com.au/lighting-control-repair-sydney
https://sydneyautomationco.com.au/smart-home-automation-neutral-bay
https://sydneyautomationco.com.au/services
https://sydneyautomationco.com.au/facilities-lighting-maintenance-sydney
https://sydneyautomationco.com.au/smart-home-automation-lindfield
https://sydneyautomationco.com.au/smart-home-automation-double-bay
https://sydneyautomationco.com.au/smart-home-automation-turramurra
https://sydneyautomationco.com.au/dali-lighting-repair
https://sydneyautomationco.com.au/strata
https://sydneyautomationco.com.au/building-lighting-upgrades-sydney
https://sydneyautomationco.com.au/guides
https://sydneyautomationco.com.au/dali-lighting-control-system-sydney
https://sydneyautomationco.com.au/smart-home-automation-killara
https://sydneyautomationco.com.au/c-bus-programmer-sutherland-shire
https://www.sydneyautomationco.com.au/lighting-control-service-sydney.html
https://sydneyautomationco.com.au/smart-home-automation-pymble
https://sydneyautomationco.com.au/smart-home-installation-gordon
https://sydneyautomationco.com.au/emergency-lighting-hotels-hospitality-sydney
https://sydneyautomationco.com.au/contact.html
https://www.sydneyautomationco.com.au/building-automation-maintenance-sydney.html
https://sydneyautomationco.com.au/projects
https://sydneyautomationco.com.au/emergency-exit-lighting-maintenance-sydney
https://sydneyautomationco.com.au/4-years-building-facilities-management-jll-pbmg
https://sydneyautomationco.com.au/cbus-repair-cremorne
https://sydneyautomationco.com.au/blog-dali-2-compliance-guide-sydney-building-managers
https://sydneyautomationco.com.au/c-bus-programmer-parramatta
https://sydneyautomationco.com.au/cbus-specialist-sydney.html
https://sydneyautomationco.com.au/dali-lighting-control-system-sydney.html
https://sydneyautomationco.com.au/emergency-repair-sydney.html
https://sydneyautomationco.com.au/dynalite-service-contract-sydney
https://sydneyautomationco.com.au/brownfield-lighting-upgrade-cbus-dynalite-sydney
https://sydneyautomationco.com.au/cbus-smart-home-balmoral
https://sydneyautomationco.com.au/smart-home-automation-cremorne
https://sydneyautomationco.com.au/emergency-lighting-train-stations-infrastructure-sydney
https://sydneyautomationco.com.au/institutional-lighting-control-parramatta-western-sydney
https://sydneyautomationco.com.au/strata-managers-lighting-control-sydney
https://sydneyautomationco.com.au/cbus-repair-exeter
https://sydneyautomationco.com.au/c-bus-programmer-sydney-cbd
https://sydneyautomationco.com.au/lighting-automation-st-ives
https://sydneyautomationco.com.au/strata-lighting-compliance-sydney
https://sydneyautomationco.com.au/smart-home-automation-pymble.html
https://sydneyautomationco.com.au/hospitality-lighting-surry-hills
https://sydneyautomationco.com.au/smart-home-installation-bellevue-hill.html
https://sydneyautomationco.com.au/c-bus-programmer-hills-district
https://sydneyautomationco.com.au/dynalite-repair-neutral-bay
https://sydneyautomationco.com.au/cbus-service-contract-sydney
https://sydneyautomationco.com.au/rapix-lighting-control
https://sydneyautomationco.com.au/smart-home-automation-neutral-bay.html
https://sydneyautomationco.com.au/afss-emergency-lighting-services
https://sydneyautomationco.com.au/real-estate-cbus-audit-sydney
https://sydneyautomationco.com.au/lighting-control-service-contract-sydney
https://sydneyautomationco.com.au/emergency-repair-sydney
https://sydneyautomationco.com.au/smart-home-darling-point
https://sydneyautomationco.com.au/c-bus-programmer-dural
https://sydneyautomationco.com.au/smart-home-automation-vaucluse
https://sydneyautomationco.com.au/lighting-automation-st-ives.html
https://sydneyautomationco.com.au/cbus-dynalite-fault-codes-sydney
https://sydneyautomationco.com.au/c-bus-programmer-st-george
https://sydneyautomationco.com.au/blog-dynalite-third-party-integration-sydney
https://sydneyautomationco.com.au/cbus-repair-wetherill-park-industrial
https://sydneyautomationco.com.au/smart-home-automation-lane-cove
https://sydneyautomationco.com.au/luxury-strata-automation-eastern-suburbs
https://sydneyautomationco.com.au/industrial-and-warehouse-facilities-hurstville-dynalite-network-communication-and-bus-crashes
https://sydneyautomationco.com.au/facility-managers-cbus-dynalite-dali-guide
https://sydneyautomationco.com.au/dynalite-programmer-sydney.html
https://sydneyautomationco.com.au/dynalite-repair-burradoo
https://sydneyautomationco.com.au/c-bus-programmer-sylvania
https://sydneyautomationco.com.au/about-sydney-automation-co
https://sydneyautomationco.com.au/blog-dynalite-ddbc1200-error-codes-sydney
https://sydneyautomationco.com.au/cbus-programming-chatswood
https://sydneyautomationco.com.au/cbus-repair-bundanoon
https://sydneyautomationco.com.au/blog-dali2-commissioning-best-practices-sydney
https://sydneyautomationco.com.au/dynalite-repair-thirroul
https://sydneyautomationco.com.au/cbus-repair-bayview
https://sydneyautomationco.com.au/blog-dali2-firmware-update-guide-sydney
https://sydneyautomationco.com.au/blog-cbus-dali-gateway-config-guide-sydney
https://sydneyautomationco.com.au/smart-home-automation-miranda
https://sydneyautomationco.com.au/cbus-repair-balgownie
https://sydneyautomationco.com.au/cbus-repair-kiama
https://sydneyautomationco.com.au/lighting-control-barangaroo
https://sydneyautomationco.com.au/blog-dali2-system-architecture-sydney
https://sydneyautomationco.com.au/smart-home-automation-killara.html
https://sydneyautomationco.com.au/control4-lighting-repairs-cbus-replacement-sydney
https://sydneyautomationco.com.au/blog-future-automation-sydney-2026
https://sydneyautomationco.com.au/blog-cbus-ethernet-interface-offline-sydney
https://sydneyautomationco.com.au/blog-dali2-central-vs-distributed-emergency-sydney
https://sydneyautomationco.com.au/automation-sydney
https://sydneyautomationco.com.au/smart-home-automation-lindfield.html
https://sydneyautomationco.com.au/cbus-repair-point-piper
https://sydneyautomationco.com.au/cbus-repair-moss-vale
https://sydneyautomationco.com.au/blog-dali2-bus-power-supply-sizing-sydney
https://sydneyautomationco.com.au/blog-afss-emergency-log-book-app-sydney
https://sydneyautomationco.com.au/lutron-lighting-control-sydney-dynalite-alternative
https://sydneyautomationco.com.au/cbus-repair-coogee
https://sydneyautomationco.com.au/cbus-repair-berry
https://sydneyautomationco.com.au/cbus-repair-tamarama
https://sydneyautomationco.com.au/dynalite-repair-silverwater
https://sydneyautomationco.com.au/cbus-repair-whale-beach
https://sydneyautomationco.com.au/blog-dynalite-power-failure-recovery-sydney
https://sydneyautomationco.com.au/cbus-pci-interface-blinking-red-sydney
https://sydneyautomationco.com.au/cbus-scene-programming-guide-sutherland-shire.html
https://sydneyautomationco.com.au/blog-dali2-emergency-test-procedures-sydney
https://sydneyautomationco.com.au/c-bus-programmer-balmain
https://sydneyautomationco.com.au/dynalite-repair-mittagong
https://sydneyautomationco.com.au/cbus-repair-bowral
https://sydneyautomationco.com.au/cbus-repair-thirroul
https://sydneyautomationco.com.au/cbus-5500pc-network-bridge-failure-sydney
https://sydneyautomationco.com.au/obsolete-cbus-5000-series-relay-replacement-sydney
https://sydneyautomationco.com.au/cbus-dynalite-planning-checklist-new-builds-menai
https://sydneyautomationco.com.au/dynalite-not-working-sydney
https://sydneyautomationco.com.au/cbus-repair-mount-keira
https://sydneyautomationco.com.au/cbus-repair-avalon-beach
"""

urls = [line.strip() for line in gsc_raw_text.strip().split('\n') if line.strip()]
missing = []

for url in urls:
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    
    if not path:
        continue
        
    # Check both clean URL and .html
    possible1 = path + '.html'
    possible2 = path
    
    # Special handle for subdirectories like blog/
    if '/' in path:
        possible1 = path + '.html'
        possible2 = path
        
    if not (os.path.exists(possible1) or os.path.exists(possible2)):
        missing.append(url)

print(f"Total checked: {len(urls)}")
print(f"Total missing: {len(missing)}")
print("\nList of missing GSC URLs:")
for m in missing:
    print(f" - {m}")
