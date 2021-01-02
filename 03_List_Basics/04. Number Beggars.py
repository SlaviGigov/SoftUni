treasure = input().split(", ")
beggars = int(input())
result = []

for n in range(beggars):
    result.append(0)
thief = 0
for gold in treasure:
    result[int(thief)] += int(gold)
    thief += 1
    if thief > beggars-1:
        thief = 0

print(result)
