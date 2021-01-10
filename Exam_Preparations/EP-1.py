password = input()
newpass = ""

def takeodd(key):
    password = ""
    for n in range(len(key)):
        if n%2 != 0:
            password += key[n]
    return password

def cut(do, current):
    a, index, lenght = do.split()
    password = current[:int(index)]
    password += current[int(index) + int(lenght):]
    return password

def sub(do, current):
    a, old, new = do.split()
    if old in current:
        password = current.replace(old, new)
        print(password)
        return password
    else:
        print(f"Nothing to replace!")
        password = current
        return password

do = input()

while not do == "Done":
    if do == "TakeOdd":
        password = takeodd(password)
        print(password)
    elif do[0] == "C":
        password = cut(do, password)
        print(password)
    elif do[0] == "S":
        password = sub(do, password)

    do = input()

print(f"Your password is: {password}")

#100/100