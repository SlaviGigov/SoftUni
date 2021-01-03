password = input()
list_of_pass = []


def password_validator():
    result = True

    if not 6 <= len(password) <= 10:
        print(f"Password must be between 6 and 10 characters")
        result = False

    for letter in password:
        list_of_pass.append(ord(letter))

    n = 0
    for item in list_of_pass:
        if not (48 <= item <= 57 or (65 <= item <= 90) or (97 <= item <= 122)):
            print(f"Password must consist only of letters and digits")
            result = False
            break
    for item in list_of_pass:
        if 48 <= item <= 57:
            n += 1
    if n < 2:
        print(f"Password must have at least 2 digits")
        result = False

    if result == True:
        print(f"Password is valid")
    return

password_validator()