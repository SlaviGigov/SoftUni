n = int(input())
result = 0

for i in range(1, n):
    if n%i == 0:
        result += i

if n == result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")