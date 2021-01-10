people = int(input())
lift = [int(el) for el in input().split()]
wagons = []

for space in lift:
    free_space = 4 - space
    if free_space > 0 and people > 0:
        people -= free_space
        if people >= 0:
            wagons.append("4")
        else:
            n = 4 + people
            wagons.append(str(n))
    else:
        wagons.append(str(space))

if people >= 0:
    print(f"There isn't enough space! {people} people in a queue!\n{' '.join(wagons)}")
else:
    print(f"The lift has empty spots!\n{' '.join(wagons)}")

