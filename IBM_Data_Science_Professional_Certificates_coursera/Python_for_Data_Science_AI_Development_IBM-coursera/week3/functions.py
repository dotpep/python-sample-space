# Python Built-in functions
# function len
# returns a number - how many elements are in the list, tuple
album_rating = [10, 8, 9, 9, 7, 7, 8, 9, 6, 8, 6]
l = len(album_rating)
print("length: ", l)

# function sum
# Sum determines the total of all the elements - returns it value
s = sum(album_rating)
print("summarize: ", s)

# quiz
print(len([sum([0, 0, 1])]))

# sorted vs sort (function vs method)
# function sorted
album_rating_sorted = sorted(album_rating)
print("new variable sorted func: ", album_rating_sorted)
print("variable using sorted func: ", album_rating)

# method sort
album_rating.sort()
print("without variable changing using sort method of list or tuple: ", album_rating)


# making function
# keyword return
def add1(a):
    b = a + 1
    return b


print(add1(5))
c = add1(10)
print(c)


# multiple parameters
def multi(a, b):
    c = a * b
    return c


print(multi(6, 5))
print(multi(10.5, 2))
print(multi("dot pep", 2))


# keyword pass
def NoWork():
    pass


def NoWork2():
    # return
    # pass
    return None


print(NoWork())
print(NoWork2())


# This function prints out the values and indexes of a loop or tuple.
# using if function enumerate()
def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print(f"Album: {i},\nRating is: {s}.")
    # return Stuff
    pass


album_rating = [10.0, 8.5, 9.5]
print(printStuff(album_rating))


# quiz
def Print(A):
    for a in A:
        print(a + '1')


Print(['a', 'b', 'c'])


# collecting arguments *
def ArtistNames(*names):
    for name in names:
        print(name)


ArtistNames("Colliope", "Fauna", "RobcD")


# Scope
# Global Scope
def AddDC(x):
    x = x + "DC"
    print(x)
    return x


# variable defined Global Scope is called Global Variable
# Global Variable
x = "AC"
z = AddDC(x)
x = "DC"
z = AddDC(x)


# Local Variable
# in this case: Date is local variable
def Thriller():
    Date = 1982
    return Date


Thriller()


# local variable without conflict - same variable name
def Thriller2():
    Date = 1982
    return Date


Date = 2017
print(Thriller())
print(Date)


# Variables
def ACDC(y):
    print(Rating)
    return Rating + y


Rating = 9

Z = ACDC(1)
print(Rating)
print(Z)


# Local Variables to Global variable using
# keyword global
def PinkFloyd():
    global ClaimedSales
    ClaimedSales = "45 million"
    return ClaimedSales


PinkFloyd()
print(PinkFloyd())
print(ClaimedSales)
