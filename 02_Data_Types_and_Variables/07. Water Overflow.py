n = int(input())
tank = 0

for i in range(1, n+1):
    l = int(input())
    if (tank + l) <= 255:
        tank += l
    else:
        print("Insufficient capacity!")

print(tank)
