class Animal:
    def __init__(self, name: str):
        self.name: str = name

    def make_sound(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed: str = breed

    def bark(self):
        print(f"{self.name} barks")


class Puppy(Dog):
    def __init__(self, name: str, breed: str, age: int):
        super().__init__(name, breed)
        self.age: int = age

    def play(self):
        print(f"{self.name} plays.")

    def info(self):
        print(f"Animal: {self.name=} \
        \n--> Dog: {self.breed=} \
        \n--> Puppy: {self.age=}")


p = Puppy("Spot", "Labrador", 1)

p.make_sound()
p.bark()
p.play()

p.info()
