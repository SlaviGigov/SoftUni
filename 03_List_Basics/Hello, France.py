items = input().split("|")
budget = float(input())

bought_i = []
profit = 0

for i in items:
    i_type, i_price = i.split("->")
    i_price = float(i_price)

    if i_type == "Clothes" and i_price > 50:
        continue
    elif i_type == "Shoes" and i_price > 35:
        continue
    elif i_type == "Accessories" and i_price > 20.5:
        continue

    if budget >= i_price:
        budget -= i_price
        current_profit = float(0.4*i_price)
        profit += current_profit
        bought_i.append(i_price+current_profit)

for e in bought_i:
    print(f"{e:.2f} ", end="")
print()
print(f"Profit: {profit:.2f}")

budget += sum(bought_i)

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

