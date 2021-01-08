data = input().split(", ")
winners = "$^#@"

def half(ticket):
    a = ticket[:10]
    b = ticket[10:]
    for x in winners:
        if x*6 in a and x*6 in b:
            print(f'ticket "{ticket}" - {min(a.count(x), b.count(x))}{x}')
            return True

for t in data:
    ticket = t.strip()

    if not len(ticket) == 20:
        print("invalid ticket")
    elif len(set(ticket)) == 1 and ticket[0] in winners:
        print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')
    elif half(ticket) is True:
        continue
    else:
        print(f'ticket "{ticket}" - no match')


