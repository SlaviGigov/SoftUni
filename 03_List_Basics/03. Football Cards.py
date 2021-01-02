A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split(" ")

for i in cards:
    team, player = i.split("-")
    if team == "A" and int(player) in A:
        A.remove(int(player))
    elif team == "B" and int(player) in B:
        B.remove(int(player))

print(f"Team A - {len(A)}; Team B - {len(B)}")
if len(A) < 7 or len(B) < 7:
    print("Game was terminated")