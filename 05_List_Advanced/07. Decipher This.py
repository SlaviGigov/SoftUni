for word in input().split():
    letter = []
    letters = []

    for w in word:
        if w.isdigit() is True:
            letter.append(w)
            first = chr(int("".join(letter)))
        else:
            letters.append(w)
    letters.insert(0,first)
    letters[1], letters[-1] = letters[-1], letters[1]
    print("".join(letters), end=" ")