parts = input()
price = 0

while parts != "special" and parts != "regular":
    if float(parts) < 0:
        print(f"Invalid price!")
    else:
        price += float(parts)
    parts = input()

if parts == "special":
    s_price = price*1.2*0.9
else:
    s_price = price*1.2

if price == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n Price without taxes: {price:.2f}$\nTaxes: {price*0.2:.2f}$\n-----------\nTotal price: {s_price:.2f}$" )