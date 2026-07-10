import subprocess
import os

missing_pages = [
    'cbus-toolkit-software-cannot-connect-sydney.html',
    'cbus-dynalite-upgrade-guide.html',
    'blog-dynalite-voltage-drop-issues-sydney.html',
    'blog-dynalite-relay-module-testing-sydney.html',
    'blog-dali2-group-addressing-guide-sydney.html',
    'emergency-lighting-train-stations-infrastructure-sydney.html',
    'rapix-to-cbus-dynalite-migration-sydney.html',
    'blog-hotel-guest-room-automation-sydney.html',
    'dali-lighting-control-system-sydney.html',
    'dynalite-service-contract-sydney.html',
    'brownfield-lighting-upgrade-cbus-dynalite-sydney.html',
    'cbus-smart-home-balmoral.html',
    'institutional-lighting-control-parramatta-western-sydney.html',
    'cbus-service-contract-sydney.html',
    'rapix-lighting-control.html',
    'real-estate-cbus-audit-sydney.html',
    'cbus-dynalite-fault-codes-sydney.html',
    'blog-dynalite-third-party-integration-sydney.html',
    'cbus-repair-wetherill-park-industrial.html',
    'industrial-and-warehouse-facilities-hurstville-dynalite-network-communication-and-bus-crashes.html',
    'facility-managers-cbus-dynalite-dali-guide.html',
    'blog-dynalite-ddbc1200-error-codes-sydney.html',
    'blog-dali2-commissioning-best-practices-sydney.html',
    'blog-dali2-firmware-update-guide-sydney.html',
    'blog-dali2-system-architecture-sydney.html',
    'control4-lighting-repairs-cbus-replacement-sydney.html',
    'blog-dali2-central-vs-distributed-emergency-sydney.html',
    'blog-dali2-bus-power-supply-sizing-sydney.html',
    'lutron-lighting-control-sydney-dynalite-alternative.html',
    'blog-dynalite-power-failure-recovery-sydney.html',
    'cbus-pci-interface-blinking-red-sydney.html',
    'cbus-scene-programming-guide-sutherland-shire.html',
    'blog-dali2-emergency-test-procedures-sydney.html',
    'cbus-5500pc-network-bridge-failure-sydney.html',
    'obsolete-cbus-5000-series-relay-replacement-sydney.html',
    'cbus-dynalite-planning-checklist-new-builds-menai.html',
    'dynalite-not-working-sydney.html'
]

def restore_file(f):
    # Find the commit that deleted this file
    res = subprocess.run(
        ['git', 'log', '-n', '1', '--diff-filter=D', '--oneline', '--', f],
        capture_output=True, text=True
    )
    log_out = res.stdout.strip()
    if log_out:
        commit_hash = log_out.split()[0]
        # Check out from the commit BEFORE deletion
        checkout_res = subprocess.run(
            ['git', 'checkout', f'{commit_hash}^', '--', f],
            capture_output=True, text=True
        )
        if checkout_res.returncode == 0:
            print(f"Restored: {f} (deleted in {commit_hash})")
            return True
        else:
            print(f"Failed to checkout {f}: {checkout_res.stderr.strip()}")
    else:
        # Maybe it was deleted in the big 33d10dd6 commit but wasn't logged for some reason, try that first
        checkout_res = subprocess.run(
            ['git', 'checkout', '33d10dd6^', '--', f],
            capture_output=True, text=True
        )
        if checkout_res.returncode == 0:
            print(f"Restored from 33d10dd6^ fallback: {f}")
            return True
        else:
            print(f"Not found in history: {f}")
    return False

restored_count = 0
for f in missing_pages:
    if restore_file(f):
        restored_count += 1

print(f"\nSuccessfully restored {restored_count} out of {len(missing_pages)} pages.")
