def characters():
    a = ord(input())
    b = ord(input())
    all_l = []
    for n in range(a+1,b):
        all_l.append(chr(n))
    return " ".join(all_l)

print(characters())