class A:
    def x(self):
        return "Function inside A"

class B(A):
    def x(self):
        return "Function inside B"

class C(B):
    # def x(self):
    #     return "Function inside C"
    pass


c = C()
print(c.x())
