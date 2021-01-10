elements = [int(el) for el in input().split()]

do = input()

while not do == "end":
    in_1, in_2 = [int(el) for el in do.split()]
    if in_1 == in_2 or in_2 > len(elements) or in_1 > len(elements) or in_1 < 0 or in_2 < 0:
        print(f"Invalid input! Adding additional elements to the board")
    else:
        if elements[in_1] == elements[in_2]:
            print(f"Congrats! You have found matching elements - ${elements[in_1]}!")
            elements.remove(elements[in_1])
            elements.remove(elements[in_2])
        else:
            print(f"Try again!")
    do = input()