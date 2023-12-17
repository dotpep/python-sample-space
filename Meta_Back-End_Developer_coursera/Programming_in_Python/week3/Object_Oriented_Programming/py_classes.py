class House:
    """
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    """
    num_rooms: int = 5
    bathrooms: int = 2

    def cost_evaluation(self, rate: int):
        cost = rate * self.num_rooms
        return f"{cost=}"


house2 = House()
print(house2.cost_evaluation(7))

house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)
