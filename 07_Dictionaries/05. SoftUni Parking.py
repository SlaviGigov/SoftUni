parking = {}

def reg(name, car):
    if not name in parking.keys():
        parking[name] = car
        return print(f"{name} registered {car} successfully")
    else:
        return print(f"ERROR: already registered with plate number {car}")

def unreg(name):
    if name in parking.keys():
        del parking[name]
        return print(f"{name} unregistered successfully")
    else:
        return print(f"ERROR: user {name} not found")


for i in range(int(input())):
    do = input().split()
    if do[0] == "register":
        reg(do[1], do[2])
    else:
        unreg(do[1])

for user in parking.keys():
    print(f"{user} => {parking[user]}" )


