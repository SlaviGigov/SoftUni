free_chairs = 0
game_on = True

for room in range(int(input())):
    chairs, needed = input().split()

    if len(chairs) < int(needed):
        print(f"{int(needed) - len(chairs)} more chairs needed in room {room+1}")
        game_on = False
    else:
        free_chairs += len(chairs) - int(needed)

if game_on:
    print(f"Game On, {free_chairs} free chairs left")

