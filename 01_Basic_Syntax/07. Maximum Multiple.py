div = int(input())
lim = int(input())
n = 0

while True:
    x = lim - n
    if x % div == 0:
        print(x)
        break
    else:
        n += 1