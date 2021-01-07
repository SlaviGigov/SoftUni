all = {}
n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    if name not in all:
        all[name] = []
    all[name].append(grade)
new = {}
for name in all.keys():
    all[name] = sum(all[name])/len(all[name])
    if all[name] >= 4.50:
        new[name] = all[name]

sorted_all = sorted(new.items(), key=lambda x : x[1], reverse=True)

for i in sorted_all:
    print(f"{i[0]} -> {i[1]:.2f}")