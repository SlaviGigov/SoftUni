username = input()

do = input()
while not do == "Sign up":
    task = do.split()[0]
    if task == "Case":
        command = do.split()[1]
        if command == "lower":
            username = username.lower()
            print(username)
        elif command == "upper":
            username = username.upper()
            print(username)

    elif task == "Reverse":
        start = int(do.split()[1])
        end = int(do.split()[2])
        if 0 <= start and end <= len(username)-1:
            if end == (len(username) - 1):
                new = username[start:]
            else:
                new = username[start:end + 1]
            rnew = new[::-1]
            print(rnew)

    elif task == "Cut":
        substr = do.split()[1]
        if substr in username:
            username = username.replace(substr, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substr}.")

    elif task == "Replace":
        char = do.split()[1]
        username = username.replace(char, "*")
        print(username)

    elif task == "Check":
        v_char = do.split()[1]
        if v_char in username:
            print("Valid")
        else:
            print(f"Your username must contain {v_char}.")

    do = input()
