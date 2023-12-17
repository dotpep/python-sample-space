# dictionary comprehension
# Using range() function and no input list
usingrange = {x: x * 2 for x in range(12)}
print("Using range(): ", usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using one input list
numdict = {x: x ** 2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
# new_dict ={key:value for (key, value) in zip(list1, list2)}
months_dict = {key: value for key, value in zip(number, months)}
print("Using two lists: ", months_dict)


# Test
start_key_1index = {x + 1: (x + 1) ** 2 for x in range(12)}
print("start key index 1 instead 0", start_key_1index)
