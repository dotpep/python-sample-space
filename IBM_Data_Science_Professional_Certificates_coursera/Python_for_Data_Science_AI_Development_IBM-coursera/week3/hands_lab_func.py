# There are two types of functions :
# Pre-defined functions
# User defined functions
"""
What is a Function?
You can define functions to provide the required functionality. Here are simple rules to define a function in Python:

Functions blocks begin def followed by the function name and parentheses ().
There are input parameters or arguments that should be placed within these parentheses.
You can also define parameters inside these parentheses.
There is a body within every function that starts with a colon (:) and is indented.
You can also place documentation before the body.
The statement return exits a function, optionally passing back a value.
"""


# Function Definition

def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)


# Initializes Global variable

x = 3
# Makes function call and return function a y
y = square(x)
print(y)


# Define the function for combining strings
def con(a, b, c):
    return a + b + c


print(con("This ", "is ", "Made of these"))


# Functions Make Things Simple
def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if c < 0:
        c = 0
    else:
        c = 5
    return (c)


# block 3
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
print(c1)

# block 4
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
print(c2)

# Pre-defined functions

# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)

# Use sum() to add every element in a list or tuple together
print(sum(album_ratings))

# Show the length of the list or tuple
print(len(album_ratings))


# Using if/else Statements and Loops in Functions
# Function example
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)


# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])

# Compare Two Strings Directly using in operator
# add string
string = "Michael Jackson is the best"


# Define a funtion
def check_string(text):
    # Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'


check_string("Michael Jackson is the best")


# Compare two strings using == operator and function
def compareStrings(x, y):
    # Use if else statement to compare x and y
    if x == y:
        return 1


# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

# Use if else statement to compare the string
if check == 1:
    print("\nString Matched")
else:
    print("\nString not Matched")


# Python Program to Count words in a String using Dictionary
def freq(string):
    # step1: A list variable is declared and initialized to an empty list.
    words = []

    # step2: Break the string into list of words
    words = string.split()  # or string.lower().split()

    # step3: Declare a dictionary
    Dict = {}

    # step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)

    # step5: Print the dictionary
    print("The Frequency of words is:", Dict)


# step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


# Setting default argument values in your custom functions
# Example for setting param with default value
def isGoodRating(rating=4):
    if rating < 7:
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)


# Test the value with default value and with input

isGoodRating()
print(isGoodRating())
print(isGoodRating(10))

# Example of global variable
artist = "Michael Jackson"


def printer1(artist):
    # local variable to global
    global internal_var
    internal_var1 = artist
    internal_var = "Whitney Houston"
    print(artist, "is an artist")


printer1(artist)
# try runningthe following code
# printer1(internal_var1)
print("just gloabl variable artist: ", artist)
print("local variable to global - result: ", internal_var)

# Example of global variable

myFavouriteBand = "AC/DC"


def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0


print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"


def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0


print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# Collections and Functions

def printAll(*args):  # All the arguments are 'packed' into args which can be treated like a tuple
    # set_args = set(args) wrong way to using function set()
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)


# printAll with 3-5 arguments
# set_a1 = set['Horsefeather', 'Adonis', 'Bone', "Bone", "Bone"]
# set_b2 = set['Sidecar', 'Long Island', 'Mudslide', 'Carriage', "Carriage", "Carriage"]
printAll('Horsefeather', 'Adonis', 'Bone', "Bone", "Bone")
# printAll with 4-6 arguments
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage', "Carriage", "Carriage")


# quiz
# Write your code below and press Shift+Enter to execute
def count(string, passedkey):
    # container for words in my tuple
    words = []
    # tuple1 or string to list and split every word
    words = string.split()
    Dict = {}

    # loop for - to find pattern/passedkey in the words splited list
    for key in words:
        if key == passedkey:
            Dict[key] = words.count(key)
        else:
            print("None key/pattern in tuple!")

    print("Count:", Dict)


pattern = "little"
tuple1 = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
count(tuple1, pattern)

print( len([sum([0, 0, 1])]))
print(sorted([1, 3, 2]))

