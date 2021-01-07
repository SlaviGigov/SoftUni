basket = {}

product = input()

while not product == "buy":
    name, price, quant = product.split()
    if name not in basket:
      basket[name] = float(price), int(quant)
    else:
        pr, q = basket[name]
        basket[name] = float(price), int(q) + int(quant)

    product = input()

for fruit in basket.keys():
    a, b = basket[fruit]
    print(f"{fruit} -> {a*b:.2f}")
