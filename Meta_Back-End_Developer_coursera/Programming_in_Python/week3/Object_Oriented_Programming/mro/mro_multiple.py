# Example 1 - Multiple
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

# class C(A,B):
#     pass

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())
