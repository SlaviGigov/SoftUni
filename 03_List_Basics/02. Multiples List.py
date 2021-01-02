factor = int(input())
count = int(input())
nums = []
a = 1

while True:
    if a % factor == 0:
        nums.append(a)
    a += 1
    if len(nums) < count:
        continue
    else:
        break

print(nums)