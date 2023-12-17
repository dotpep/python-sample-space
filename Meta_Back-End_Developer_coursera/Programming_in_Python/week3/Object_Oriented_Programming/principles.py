# Encapsulation
import abc


class Alpha:
    def __init__(self):
        self._a = 2  # Protected member ‘a’
        self.__b = 4  # Private member ‘b’

    def info(self):
        return f"{self._a=}, {self.__b=}"


alpha = Alpha()
# print(alpha._a)
# print(alpha.info())

# Polymorphism
string = "poly"
num = 7
sequence = [1, 2, 3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3


# print(new_str, new_num, new_sequence)
# print(len(string))
# print(len(sequence))


# Inheritance
class Parent:
    def __init__(self, parent_attribute):
        self.parent_attribute = parent_attribute

    def parent_method(self):
        return f"Members of the parent class with {self.parent_attribute=}"


class Child(Parent):
    def __init__(self, parent_attribute, child_attribute):
        super().__init__(parent_attribute)
        self.child_attribute = child_attribute

    def child_method(self):
        return f"Inherited members from parent class \
        Additional members of the child class with {self.child_attribute=}"


parent = Parent("Parents")
child = Child("Parent child", "Child")

print(parent.parent_attribute)
print(parent.parent_method())

print(child.parent_attribute)
print(child.child_attribute)
print(child.parent_method())
print(child.child_method())


# Abstraction
class AbcClassName(abc.ABC):
    def __init__(self, base_start: int):
        self.base_start = base_start

    def abstract_method(self):
        return f"abstract method {self.base_start=}"


class BaseClassName(AbcClassName):
    def __init__(self, base_start):
        super().__init__(base_start)
        self.base_start = base_start * 2


abstract = AbcClassName(1)
my_class = BaseClassName(2)
print(abstract.base_start)
print(my_class.base_start)
