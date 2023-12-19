# range function
n = 3
print(range(n))
print(range(10, 15))

# for loops
# (если или для for i в in range диапазоне(0, 5))
squares = ["red", "yellow", "green", "purple", "aqua"]
print(squares, "before - changing Squares color in list")
for i in range(0, 5):
    squares[i] = "white"

print(squares, "after - changing Squares color to White in list")

# iterate directly in python
squares = ["red", "yellow", "green"]
print(squares, "before iterate")
for square in squares:
    print(square)

print(squares, "after iterate")

# iterate in list - represent index each elements
for i, square in enumerate(squares):
    print(square, "square:")
    print(i, "index:")

# while loops
squares = ["orange", "orange", "purple", "orange", "aqua"]
new_squares = []
i = 0

while squares[i] == "orange":
    new_squares.append(squares[i])
    i = i + 1

print(squares)
print(new_squares)
