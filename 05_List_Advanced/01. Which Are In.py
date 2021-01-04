first = input().split(", ")
second = input().split(", ")
result = [w for w in first for w2 in second if w in w2]

print(sorted(set(result), key = result.index))