class A:
    pass

class B(A):
    pass

a = A()
b = B()
print(isinstance(a, A))
print(isinstance(b, B))

print(isinstance(a, B))
print(isinstance(b, A))


print("")

class First:
    pass

class Second(First):
    pass

class Third:
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))
print(issubclass(First, Third))
