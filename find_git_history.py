import subprocess

files = [
    'c-bus-repairs-sydney.html',
    'dynalite-fault-finding-sydney-common-faults.html',
    'cbus-fault-finding-sydney.html'
]

for f in files:
    # Use git log to find if the file ever existed and when it was deleted
    res = subprocess.run(['git', 'log', '--all', '--full-history', '--oneline', '--', f], capture_output=True, text=True)
    print(f"Log for {f}:")
    print(res.stdout.strip())
