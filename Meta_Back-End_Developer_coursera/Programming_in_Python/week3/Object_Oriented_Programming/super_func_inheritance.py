class Fruit:
    def __init__(self, fruit: str):
        print("Fruit type: ", fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__("Apple")
        print("Apple is sweet")


apple = FruitFlavour()

class Fruit2:
    def __init__(self, fruit: str):
        self.fruit = fruit
        print("Fruit type: ", fruit)


class FruitFlavour2(Fruit2):
    def __init__(self, fruit: str, taste: str):
        super().__init__(fruit)
        print(f"{fruit} is {taste}")


lemon = FruitFlavour2("Lemon", "Sour")
