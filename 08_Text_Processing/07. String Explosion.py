data = input()
boom = 0
result = ""

for i in range(len(data)):
    if data[i] == ">":
        boom += int(data[i+1])
        result += ">"
    elif boom > 0:
        boom -= 1
    elif boom == 0:
        result += data[i]

print(result)