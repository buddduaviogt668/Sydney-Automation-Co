import os

old_name = "George Skarmoutsos"
new_name = "George Skarmoutsos"
count = 0

for filename in os.listdir("."):
    if filename.endswith(".html") or filename.endswith(".py"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            if old_name in content:
                content = content.replace(old_name, new_name)
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
        except Exception as e:
            pass

print(f"Replaced name in {count} files.")
