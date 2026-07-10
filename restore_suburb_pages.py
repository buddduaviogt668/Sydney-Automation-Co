import subprocess
import os

# Get the full list of deleted files from the SEO cleanup commit
result = subprocess.run(
    ['git', 'diff', '--name-only', '--diff-filter=D', '33d10dd6^..33d10dd6'],
    capture_output=True, text=True
)

deleted_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]

# Filter to the suburb/service pages we want to restore
# We want all programmer and repair suburb pages
restore_patterns = [
    'c-bus-programmer-',
    'dynalite-programmer-',
    'cbus-repair-',
    'dynalite-repair-',
    'smart-home-automation-',
    'smart-home-',
    'lighting-automation-',
    'lighting-control-',
]

to_restore = []
for f in deleted_files:
    for pattern in restore_patterns:
        if f.startswith(pattern) and f.endswith('.html'):
            to_restore.append(f)
            break

print(f"Files to restore: {len(to_restore)}")

# Restore them using git checkout
restored = 0
failed = 0
for f in to_restore:
    result = subprocess.run(
        ['git', 'checkout', '33d10dd6^', '--', f],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        restored += 1
        if restored % 50 == 0:
            print(f"  Restored {restored} files so far...")
    else:
        failed += 1
        if failed <= 5:
            print(f"  FAILED: {f} - {result.stderr.strip()}")

print(f"\nDone! Restored: {restored}, Failed: {failed}")
