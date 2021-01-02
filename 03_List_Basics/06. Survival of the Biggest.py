text = input()
num = int(input())
nums = []

num_list = text.split(" ")
for m in num_list:
    nums.append(int(m))

for n in range(num):
    m = min(nums)
    nums.remove(m)

print(nums)