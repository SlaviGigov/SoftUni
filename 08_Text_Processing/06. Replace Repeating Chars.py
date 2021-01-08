data = input()
result = data[0]

for n in range(1, len(data)):
    if data[n] != data[n-1]:
        result += data[n]

print(result)
#wrong