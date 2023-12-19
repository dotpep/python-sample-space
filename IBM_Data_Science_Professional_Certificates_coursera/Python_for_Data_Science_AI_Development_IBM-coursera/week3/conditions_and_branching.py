# Comparison Operators
# equals operator
a = 6
equals = a == 7
print(equals)

# greater operator:
i = 6
greater = i > 5
print(greater)

# greater than or equal
greater_or_equal = i >= 5
print(greater_or_equal)

# less than
# operator: +, ==, > | numbers like 5 is operand: 6
less = i < 6
print(less)

# two operands are not equal - only 6 == 6 is True
not_equal = i != 6
print(not_equal)

str_operators = "a" == "A"
print(str_operators)


# branching (if statement)
age = 18
if age >= 18:
    print("you can enter")
elif age == 17:
    print("visit us next year!")
else:
    print("move on")

# logic operators
album_year = 1989
if album_year < 1980 or album_year >= 1990:
    print("The Album was made in the 70s or 90s")
else:
    print("The Album was made in the 1980s")



