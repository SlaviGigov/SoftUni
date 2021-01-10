mama = int(input())
baba = int(input())
tati = int(input())
total_people = int(input())

time = 0

while True:
    time += 1
    if time % 4 == 0:
        time += 1
    total_people -= (baba + mama + tati)
    if total_people <= 0:
        break

print(f"Time needed: {time}h.")