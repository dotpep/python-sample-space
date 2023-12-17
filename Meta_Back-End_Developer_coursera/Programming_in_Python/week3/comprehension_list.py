# list comprehension
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)


# Test 1
print("\nTest1")
odd = [x for x in range(50) if x % 2 == 1]
even = [x for x in data if x % 2 == 0]
even_range = [x for x in range(1, 50) if x % 2 == 0]
print("odd numbers in range(50): ", odd)
print("even numbers in range(50): ", even_range)
print("even numbers in data: ", even)


# Test 2
print("\nTest2")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list1 = [x for x in fruits if "a" in x]
print("if a in fruits: ", new_list1)
new_list2 = [x.upper() for x in fruits]
print("set fruits uppercase: ", new_list2)
new_list3 = [x for x in fruits if x != "apple"]
print("only accept items that are not apple:", new_list3)
new_list4 = [x if x != "banana" else "orange" for x in fruits]
print("return orange instead of banana: ", new_list4)


# Test 3
print("\nTest3")
z = ["alpha", "bravo", "charlie"]
new_z = [i[0] * 2 for i in z]
print(new_z)
new_z = [i[::-1] for i in z]
print(new_z)

# Comparison
# List comprehension:
data = [x + 3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3
