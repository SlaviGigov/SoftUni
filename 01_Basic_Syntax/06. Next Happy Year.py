year = int(input())
year += 1

while True:
    if len(str(year)) == len(set(str(year))):
        print(year)
        break
    else:
        year += 1