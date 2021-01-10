import re

data = input()
threshold = 1
result = {}

digits = re.findall("\d", data)
for n in digits:
    threshold *= int(n)

matches = re.findall(r"(:{2}|\*{2})(?P<match>[A-Z][a-z]{2,})(\1)", data)
for match in matches:
    a = "".join(match)
    result[a] = 0

for key in result:
    value = 0
    for letter in key[2:-2]:
        num = ord(letter)
        value += num
    result[key] = value

print(f"Cool threshold: {threshold}")
print(f"{len(result)} emojis found in the text. The cool ones are:")

for key, value in result.items():
    if value >= threshold:
        print(key)

# 100/100 findall