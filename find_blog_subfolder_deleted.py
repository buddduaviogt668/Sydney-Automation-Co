import subprocess

# Let's search git history for deleted files under the 'blog/' directory
res = subprocess.run(
    ['git', 'log', '--all', '--full-history', '--oneline', '--name-only', '--diff-filter=D'],
    capture_output=True, text=True
)

deleted_files = set()
for line in res.stdout.split('\n'):
    line = line.strip()
    if line and (line.startswith('blog/') or 'blog' in line) and line.endswith('.html'):
        deleted_files.add(line)

print("Deleted files in git history containing 'blog':")
for f in sorted(deleted_files):
    print(f" - {f}")
