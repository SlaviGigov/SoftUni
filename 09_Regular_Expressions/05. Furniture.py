import re

pattern = r"(^>>)(?P<good>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
money = 0
data = input()
print("Bought furniture:")

while not data == "Purchase":
    matches = re.finditer(pattern, data)
    for match in matches:
        print(match.group("good"))
        money += float(match.group("price"))*int(match.group("quantity"))
    data = input()

print(f"Total money spend: {money:.2f}")