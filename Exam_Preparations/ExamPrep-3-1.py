# P!rates
cities = {}

data = input()
while not data == "Sail":
    city, pop, gold = data.split("||")
    if city in cities:
        cities[city] = cities[city][0] + int(pop), cities[city][1] + int(gold)
    else:
        cities[city] = int(pop), int(gold)
    data = input()

do = input()
while not do == "End":
    event = do.split("=>")[0]
    town = do.split('=>')[1]
    if event == "Plunder":
        print(f"{town} plundered! {do.split('=>')[3]} gold stolen, {do.split('=>')[2]} citizens killed.")
        cities[town] = cities[town][0] - int(do.split('=>')[2]), cities[town][1] - int(do.split('=>')[3])
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
        # elif cities[town][1] <= 0:
        #     del cities[town]
    elif event == "Prosper":
        gold = do.split("=>")[2]
        if int(gold) < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town] = cities[town][0], cities[town][1] + int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    do = input()

sorted_cities = sorted(cities.items(), key = lambda x: (-x[1][1], x[0]))

if len(cities)<1:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for k, v in sorted_cities:
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")

# 100/100