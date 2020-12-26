q = int(input())
days = int(input())
total = 0
spirit = 0

for day in range(1,days+1):
    if day % 11 == 0:
        q += 2
    if day % 2 == 0:
        total += q*2
        spirit += 5
    if day % 3 == 0:
        total += q*5 + q*3
        spirit += 13
    if day % 5 == 0:
        total += q*15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total += 15 + 5 + 3
        if day == days:
            spirit -= 30

print(f"Total cost: {total}")
print(f"Total spirit: {spirit}")