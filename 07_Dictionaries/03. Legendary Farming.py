top = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
a = 6


def wants(k, v):
    if k in top:
        top[k] += int(v)
    else:
        if k in junk:
            junk[k] += int(v)
        else:
            junk[k] = int(v)




def winner(stone):
    if stone == "shards":
        return "Shadowmourne obtained!"
    if stone == "fragments":
        return "Valanyr obtained!"
    if stone == "motes":
        return "Dragonwrath obtained!"


while True:
    elements = input().split()

    for n in range(0, len(elements), 2):
        wants(elements[n + 1].lower(), elements[n])
        for k, value in top.items():
            if value >= 250:
                top[k] = value - 250
                print(winner(k))
                a = 5
                break
        if a == 5:
            break
    if a == 5:
        break

for k, v in sorted(top.items(), key=lambda x:(-x[1],x[0])):
    print(f"{k}: {v}")
for k, v in sorted(junk.items(), key=lambda x:x[0]):
    print(f"{k}: {v}")