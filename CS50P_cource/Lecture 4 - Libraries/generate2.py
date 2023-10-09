import random

cards = ["jack", "queen", "king"]
# shuffle - перетасовка случайных слов из [лист, списка]
random.shuffle(cards)
for card in cards:
    print(card)
