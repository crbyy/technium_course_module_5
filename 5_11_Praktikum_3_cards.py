import itertools



suits = ['Червы', 'Пики', 'Трефы', 'Бубны']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck = []

for suit in suits:
    for rank in ranks:
        card = f'{suit} {rank}'
        deck.append(card)

l = int(input("Укажите количество карт: "))
print(deck)
combinations = list(itertools.combinations(deck, l))

# print(combinations)
for combo in combinations:
    print(' '.join(combo))









