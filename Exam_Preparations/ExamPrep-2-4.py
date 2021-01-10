n = int(input())
plants = {}
ratings = {}

for _ in range(n):
    plant, rare = input().split("<->")
    plants[plant] = int(rare)
    ratings[plant] = []

do = input()
while not do == "Exhibition":
    try:
        if do.split(":")[0] == "Rate":
            plant, rating = do.split(": ")[1].split(" - ")
            if plant not in plants:
                print("error")
                break
            else:
                ratings[plant].append(int(rating))

        elif do.split(":")[0] == "Update":
            plant, rare = do.split(": ")[1].split(" - ")
            if plant not in plants:
                print("error")
                break
            else:
                plants[plant] = float(rare)

        elif do.split(": ")[0] == "Reset":
            plant = do.split(": ")[1]
            if plant not in plants:
                print("error")
                break
            else:
                ratings[plant] = []
    except:
        print("error")

    do = input()

for k in ratings:
    if not ratings[k]:
        ratings[k] = 0
    else:
        ratings[k] = sum(ratings[k])/len(ratings[k])

for k in plants:
    plants[k] = plants[k], ratings[k]

sorted_plants = sorted(plants.items(), key = lambda x: (x[1][0], x[1][1]), reverse=True)

print(f"Plants for the exhibition:")
for k, v in sorted_plants:
    print(f"- {k}; Rarity: {int(v[0])}; Rating: {v[1]:.2f}")

#87/100
