def random1():
    import random

    # choice - модуль рандомно выбирает один из слов [лист]
    coin = random.choice(["yep", "nope", "yes", "nope"])
    print(coin)


def random2():
    import random

    # randint - модуль рандома от 1 до 10 - указывающие в скобках
    number = random.randint(1, 5)
    print(number)


def random3():
    import random

    cards = ["jack", "queen", "king"]
    # shuffle - перетасовка случайных слов из [лист, списка]
    random.shuffle(cards)
    for card in cards:
        print(card)


random1()
random2()
