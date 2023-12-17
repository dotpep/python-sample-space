# inheritance example

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


# polymorphism example
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())

print(felix.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


# abstract example
class Computer:
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running")


class Phone(Computer):
    pass


com1 = Computer()
com1.process()
lap1 = Laptop()
lap1.process()
ph1 = Phone()
ph1.process()


# encapsulation example
class Item:
    def __init__(self, name, price, quantity):
        # validation
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)
item1.calculate_total_price()
item1.price = -100
item1.calculate_total_price()
item1.quantity = -5
item1.calculate_total_price()
item1.name = "Laptop"
item1.calculate_total_price()
item1.price = 100
item1.quantity = 5
item1.calculate_total_price()
item1.name = "Phone"
item1.calculate_total_price()
item1.price = -100
item1.quantity = -5
item1.calculate_total_price()

# abstraction example
from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def read(self):
        pass


class Pdf(Book):
    def read(self):
        print("reading pdf")


class Ebook(Book):
    def read(self):
        print("reading ebook")


pdf = Pdf()
pdf.read()
ebook = Ebook()
ebook.read()


# composition example
class Book:
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def __str__(self):
        return f"{self.name} - {self.page}"


class Library:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return f"{self.books}"

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


book1 = Book("Python", 100)
book3 = Book("C#", 300)
book4 = Book("C++", 400)
book5 = Book("C", 500)

# inheritance, polymorphism, encapsulation and abstract class in one example
