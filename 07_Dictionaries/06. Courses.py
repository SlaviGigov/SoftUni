school = {}

do = input()

while not do == "end":
    course, name = do.split(" : ")
    if course not in school:
        school[course] = []
    school[course].append(name)
    do = input()

sorted_school = sorted(school.items(), key=lambda x : len(x[1]), reverse=True)

for course in sorted_school:
    print(f"{course[0]}: {len(course[1])}")
    for name in sorted(course[1]):
        print(f"-- {name}")
