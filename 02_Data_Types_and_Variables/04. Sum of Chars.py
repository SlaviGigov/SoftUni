n = int(input())
total = 0

while n>0:
    x = input()
    total += ord(x)
    n -= 1

print(f"The sum equals: {total}")