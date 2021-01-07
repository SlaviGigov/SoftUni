all = {}
text = []

do = input()
while not do == "stop":
    text.append(do)
    do = input()

for n in range(0, len(text), 2):
    key = text[n]
    value = int(text[n+1])
    if key not in all:
        all[key] = 0
    all[key] += value

for w in all.keys():
    print(f"{w} -> {all[w]}")
