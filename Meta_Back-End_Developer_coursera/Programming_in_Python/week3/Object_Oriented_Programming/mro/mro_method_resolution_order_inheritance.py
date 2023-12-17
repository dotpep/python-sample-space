class A:
    num = 5

class B(A):
    num = 9

class C(B):
    pass

print(C.mro())
print(help(C))
