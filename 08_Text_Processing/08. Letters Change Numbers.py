alphabet = {chr(el+97):el+1 for el in range(26)}

data = input().split()
result = 0

for el in data:
    first = el[0]
    second = el[-1]
    number = int(el[1:-1])
    if first.isupper():
        number /= alphabet[first.lower()]
    elif first.islower():
        number *= alphabet[first]
    if second.isupper():
        number -= alphabet[second.lower()]
    elif second.islower():
        number += alphabet[second]
    result += number

print(f"{result:.2f}")
