# Instantiate a custom Object
# class Recipe:
# def __new__(cls, *args, **kwargs):
#     pass
#
# def __init__(self):
#     pass

class Recipe:

    def __init__(self, dish: str, items: list, time: int):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")


# instantiate two object for our Recipe: pizza and pasta with own properties (arguments or parameter that takes)
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())
print(pasta.contents())
