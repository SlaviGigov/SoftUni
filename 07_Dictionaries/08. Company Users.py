all = {}
do = input()

while not do == "End":
    company, id = do.split(" -> ")
    if company not in all:
        all[company] = []
    if id not in all[company]:
        all[company].append(id)
    do = input()

for i in sorted(all.keys()):
    print(i)
    for n in all[i]:
        print(f"-- {n}")