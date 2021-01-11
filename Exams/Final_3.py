do = input()
all = {}

while not do == "Log out":
    task = do.split(":")[0]
    if task == "New follower":
        name = do.split(":")[1]
        if name not in all:
            all[name] = 0, 0

    elif task == "Like":
        name = do.split(":")[1]
        likes = int(do.split(":")[2])
        if name not in all:
            all[name] = likes, 0
        else:
            all[name] = (int(all[name][0]) + likes), int(all[name][1])

    elif task == "Comment":
        name = do.split(":")[1]
        if name not in all:
            all[name] = 0, 1
        else:
            all[name] = int(all[name][0]), int(all[name][1])+1

    elif task == "Blocked":
        name = do.split(":")[1]
        if name in all:
            del all[name]
        else:
            print(f"{name} doesn't exist.")

    do = input()

print(f"{len(all)} followers")
fin_all = {}
for k,v in all.items():
    fin_all[k] = int(v[0]) + int(v[1])

sot_fin_all = sorted(fin_all.items(), key = lambda x:(-x[1],x[0]))
for el in sot_fin_all:
    print(f"{el[0]}: {el[1]}")