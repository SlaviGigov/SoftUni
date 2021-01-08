data = input()
result = ""

for w in data:
    result += chr(ord(w)+3)

print(result)