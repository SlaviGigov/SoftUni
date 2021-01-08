data = input()
n = -1

for w in data:
    result = ""
    n += 1
    if w == ":":
        result = w
        result += data[n + 1]
        print(result)