loot = input().split("|")

do = input()

while not do == "Yohoho!":
    command = do.split()
    if command[0] == "Loot":
        for el in command[1:]:
            if el not in loot:
                loot.insert(0, el)

    if command[0] == "Drop" and 0 <= int(command[1]) <= len(loot):
        dropped = loot[int(command[1])]
        loot.remove(dropped)
        loot.append(dropped)

    if command[0] == "Steal":
        if len(loot) <= int(command[1]):
            stollen = len(loot)
            print(", ".join(loot))
            loot.clear()
        else:
            stollen = len(loot) - int(command[1])
            print(", ".join(loot[stollen:]))
            for el in loot[stollen:]:
                loot.remove(el)

    do = input()

total_lenght = 0
for el in loot:
    total_lenght += len(el)

if len(loot) > 0:
    print(f"Average treasure gain: {(total_lenght/len(loot)):.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")