students = {}
lessons = {}

do = input()

while not do == "exam finished":
    if "banned" in do:
        name, ban = do.split("-")
        students.pop(name)
    else:
        name, lesson, points = do.split("-")
        if name not in students:
            students[name] = int(points)
        else:
            if students[name] < int(points):
                students[name] = int(points)

        if lesson not in lessons:
            lessons[lesson] = 0
        lessons[lesson] += 1

    do = input()

# order by value and then by name:
print("Results:")
s_by_points = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))
for k, v in s_by_points.items():
    print(f"{k} | {v}")

print("Submissions:")
s_by_points = dict(sorted(lessons.items(), key=lambda x: x[1], reverse=True))
for k, v in s_by_points.items():
    print(f"{k} - {v}")