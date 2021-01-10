houses = [int(el) for el in input().split("@")]
do = input()
cupid = 0

while not do == "Love!":
    jump, lenght = do.split()
    lenght = int(lenght)
    cupid += lenght
    if cupid >= len(houses):
        cupid = 0

    if houses[cupid] == 0:
        print(f"Place {cupid} already had Valentine's day.")
    else:
        houses[cupid] -= 2
        if houses[cupid] == 0:
            print(f"Place {cupid} has Valentine's day.")

    do = input()

print(f"Cupid's last position was {cupid}.")

if sum(houses) > 0:
    print(f"Cupid has failed {len([el for el in houses if el > 0])} places.")
else:
    print(f"Mission was successful.")
