cards_text = input()
num = int(input())

cards = cards_text.split(" ")

top = cards[0]
bottom = cards[-1]

half = len(cards) // 2
shuffle_cards = []

for n in range(num):
    left_deck = []
    right_deck = []

    for i in range(1, half):
        left_deck.append(cards[i])

    for i in range(half, len(cards) - 1):
        right_deck.append(cards[i])

    for i in range(len(left_deck)):
        shuffle_cards.append(right_deck[i])
        shuffle_cards.append(left_deck[i])

    cards = shuffle_cards.copy()
    cards.append(bottom)
    cards.insert(0, top)
    shuffle_cards = []

print(cards)