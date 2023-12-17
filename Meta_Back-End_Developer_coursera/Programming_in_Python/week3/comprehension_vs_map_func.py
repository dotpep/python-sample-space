# difference between map() function and list comprehensions
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Map
print("Map")


def square(num):
    return num + 3


newdata = map(square, data)
print(newdata)

map_obj = newdata
print(map_obj)
print(type(map_obj))
for items in map_obj:
    print(items, end=" ")

# List comprehension
print("\n\nList comprehension")
newdata = [x + 3 for x in data]
print(newdata)
