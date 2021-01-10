import re
pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)(\1)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(\1)(?P<cal>[0-9][0-9]{0,3}|10000)(\1)"

matches = re.finditer(pattern, input())

all_cal = 0
food = []
for match in matches:
    result = match.groupdict()
    all_cal += int(match.group("cal"))
    food.append(result)

print(f"You have food to last you for: {all_cal//2000} days!")

for k in food:
    print(f"Item: {k['name']}, Best before: {k['date']}, Nutrition: {k['cal']}")

# 100/100 - usage of groupdict()