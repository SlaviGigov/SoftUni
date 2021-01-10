code = input()
do = input()

while not do == "Decode":
    do = do.split("|")
    if do[0] == "Move":
        left = code[int(do[1]):]
        right = code[:int(do[1])]
        code = left + right
    elif do[0] == "Insert":
        left = code[:int(do[1])]
        right = code[int(do[1]):]
        code = left + do[2] + right
    elif do[0] == "ChangeAll":
        code = code.replace(do[1], do[2])
    do = input()

print(f"The decrypted message is: {code}")

#100/100