data = input().split(", ")

for item in data:
    meti = item[::-1]
    if item == meti:
        print("True")
    else:
        print("False")