nums = [int(n) for n in input().split(", ")]
a = 10

while len(nums) > 0:
    result = [n for n in nums if n <= a]
    print(f"Group of {a}'s: {result}")
    a += 10
    for x in result:
        nums.remove(x)
    result.clear()