class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class Calculate(A, B):
    def __init__(self, a, b):
        super().__init__(a.a)
        self.b = b.b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b


first_value = A(5)
second_value = B(5)

calc = Calculate(first_value, second_value)

add = calc.add()
multiply = calc.multiply()

print(add)
print(multiply)
