import re
pattern = r"\d+"
data = input()
numbers = []
while data:
    match = re.findall(pattern, data)
    if match:
        numbers.extend(match)
    data = input()

print(*numbers, sep=" ")