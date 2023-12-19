# range object

# for loops
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Example of for loop
for i in range(0, 8):
    print(i)

# Exmaple of for loop, loop through list
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is', squares[i])

# Loop through the list and iterate on both index and element value
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# while loops

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while year != 1973:
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i, "repetitions to get out of loop.")

# quiz
# Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5, 5):
    print(i)

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)

# answer
for Genre in Genres:
    print(Genre)

# my sol
squares = ['red', 'yellow', 'green', 'purple', 'blue']
n = len(squares)
i = n
for i in range(n):
    print(squares[i])

# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7.
# Help him memorise both the tables by printing them using for loop.
print("Multiplication table of 6:")
for i in range(10):
    print("6 *", i, "=", 6 * i)
print("Multiplication table of 7:")
for i in range(10):
    print("7 *", i, "=", 7 * i)

# Multiplication table
for n in range(1, 11):
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} *", i, "=", n * i)

# Your brother needs to write an essay on the animals whose names are made of 7 letters.
# Help him find those animals through a while loop and create a separate list of such animals.
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
seven_letters = []

n = 7
i = 0
while i != len(animals) - 1:
    j = animals[i]
    print(j)
    if len(j) == n:
        seven_letters.append(j)
    i = i + 1

print(seven_letters)
print(len(animals))
