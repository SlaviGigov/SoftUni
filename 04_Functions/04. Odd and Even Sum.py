num = input()
odd_sum = []
even_sum = []

def odd_even():
    for n in num:
        if int(n)%2 == 0:
            even_sum.append(int(n))
        else:
            odd_sum.append(int(n))
    even = sum(even_sum)
    odd = sum(odd_sum)
    return print(f"Odd sum = {odd}, Even sum = {even}")

odd_even()