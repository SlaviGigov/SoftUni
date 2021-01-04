target = input().split()
targets = list(map(int, target))

data = input()


def shoot(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums


def add_target(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print("Invalid placement!")
    return nums


def strike(nums, i, v):
    left_index = i - v
    right_index = i + v

    if left_index >= 0 and right_index < len(nums):
        left_part = nums[0:left_index]
        right_part = nums[right_index + 1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums


while not data == "End":
    command, index, value = data.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add_target(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)

    data = input()
print("|".join([str(el) for el in targets]))
