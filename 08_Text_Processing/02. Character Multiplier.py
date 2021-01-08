str1, str2 = input().split()
result = 0

if len(str2) > len(str1):
    x1 = str2
    x2 = str1
else:
    x1= str1
    x2 = str2

for n in range(len(x2)):
    result += ord(x1[n])*ord(x2[n])

for n in range(len(x1)-len(x2)):
    result += ord(x1[n+len(x2)])

print(result)
