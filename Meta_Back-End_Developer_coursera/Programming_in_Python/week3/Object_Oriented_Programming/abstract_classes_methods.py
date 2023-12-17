from abc import ABC, abstractmethod


# class SomeAbstractClass(ABC):
#     @abstractmethod
#     def someabstractmethod(self):
#         pass

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass


class Donation(Employee):
    def donate(self):
        return int(input("How much would you like to donate: "))


amounts = []

john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)


sum_amounts = sum(amounts)

print(sum_amounts)
