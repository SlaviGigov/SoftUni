text = input()
all = {}

for w in text:
    if w not in all:
        all[w] = 1
    else:
        all[w] += 1

for w in all.keys():
    if w != " ":
        print(f"{w} -> {all[w]}")
