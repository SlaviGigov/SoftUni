#Mu Online
data = input().split("|")
health = 100
bitcoins = 0
best = 0

for room in data:
    best += 1
    monster = room.split()[0]
    points = int(room.split()[1])
    if monster == "potion":
        if health + points >= 100:
            points = 100 - health
            health = 100
        else:
            health += points
        print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")
    elif monster == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")
    else:
        health -= points
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best}")
        else:
            print(f"You slayed {monster}.")
    if health <= 0:
        break

if not health <= 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

#100/100 if/else
