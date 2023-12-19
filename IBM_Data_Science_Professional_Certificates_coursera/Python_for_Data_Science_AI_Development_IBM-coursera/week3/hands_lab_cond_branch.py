# There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year.
# Write an if-else statement to determine who was born in a leap year.
Annie = 1996
Jane = 1999
if Annie % 4 == 0:
    print("Annie was born in a leap year")
elif Jane % 4 == 0:
    print("Jane was born in a leap year")
else:
    print("None of them were born in a leap year")

# In a school canteen, children under the age of 9 are only given milk porridge for breakfast.
# Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger.
# The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10.
# Use if-else statement to determine what the canteen master will offer to him.


# Test
age = 14
if age <= 9:
    print("milk porridge")
elif age <= 10 and 14:
    print("sandwich")
elif age <= 15 and 17:
    print("burger")
else:
    print("else breakfast child ages")

# answer
if age > 3 and age <= 9:
    print("You will get a bowl of porridge!")
elif age >= 10 and age <= 14:
    print("You will get a sandwich!")
elif age >= 15 and age <= 17:
    print("You will get a burger!")
