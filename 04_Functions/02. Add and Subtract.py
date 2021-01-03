numl = []

def sum_numbers():
    return numl[0] + numl[1]

def subtract():
    return sum_numbers() - numl[2]

def add_and_subtract():
    for n in range(3):
        n = int(input())
        numl.append(n)
    sum_numbers()
    return subtract()

print(add_and_subtract())
