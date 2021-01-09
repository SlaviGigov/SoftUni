import re
pattern = r"\bwww\.([A-Za-z0-9-]+)(\.[a-z]+)+\b"
data = input()
while data:
    matches = re.finditer(pattern, data)
    for match in matches:
        print(match.group())
    data = input()