def add(p, c, k):
    if p in music:
        print(f"{p} is already in the collection!")
    else:
        music[p] = c, k
        return print(f"{p} by {c} in {k} added to the collection!")


def remove(p):
    if p in music:
        del music[p]
        return print(f"Successfully removed {p}!")
    else:
        return print(f"Invalid operation! {p} does not exist in the collection.")


def changekey(p, nk):
    if p in music:
        music[p] = music[p][0], nk
        return print(f"Changed the key of {p} to {nk}!")
    else:
        return print(f"Invalid operation! {p} does not exist in the collection.")


n = int(input())
music = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    music[piece] = composer, key

command = input()
while not command == "Stop":
    do = command.split("|")[0]
    if do == "Add":
        do, p, c, k = command.split("|")
        add(p,c,k)
    elif do == "Remove":
        do, p = command.split("|")
        remove(p)
    elif do == "ChangeKey":
        do, p, nk = command.split("|")
        changekey(p, nk)
    command = input()

sorted_music = sorted(music.items(), key = lambda x: (x, x[0]))
for k, v in sorted_music:
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")

# 83/100