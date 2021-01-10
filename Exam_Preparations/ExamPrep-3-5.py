#Dragon Army
n = int(input())
dragons = {}

for _ in range(n):
    type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10

    if type not in dragons:
        dragons[type] = {name:[int(damage), int(health), int(armor)]}
    elif type in dragons and name in dragons:
        dragons[type] = {name: [int(damage), int(health), int(armor)]}
    else:
        dragons[type].update({name:[int(damage), int(health), int(armor)]})

for k, v in dragons.items():
    a_damage = sum([el[0] for k, el in v.items()])/len(dragons[k])
    a_health = sum([el[1] for k, el in v.items()])/len(dragons[k])
    a_armor = sum([el[2] for k, el in v.items()])/len(dragons[k])
    print(f"{k}::({a_damage:.2f}/{a_health:.2f}/{a_armor:.2f})")
    s_v = sorted(v.items(), key=lambda x:x[0])
    for el in s_v:
        print(f"-{el[0]} -> damage: {el[1][0]}, health: {el[1][1]}, armor: {el[1][2]}")

#100/100 very, very hard - Dictionaries