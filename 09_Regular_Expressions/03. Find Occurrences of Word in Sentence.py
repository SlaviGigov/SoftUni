import re

data = input().lower()
x = input().lower()
pattern = f"\\b{x}\\b"
matches = re.findall(pattern, data)
print(len(matches))