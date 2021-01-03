a = int(input())
b = int(input())
c = int(input())
numl = []
numl.append(a)
numl.append(b)
numl.append(c)


def smallest():
    return min(numl)

print(smallest())