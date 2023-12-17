# set comprehension
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
set_b = {x for x in range(10, 20) if x not in [15, 17, 19]}
print(set_a)
print(set_b)
# this is: | concatenation operator for sets
set_c = set_a | set_b
print(set_c)

# Test
print("\nTest")
set1 = {x for x in range(1, 20, 2)}
print(set1)
set2 = {x for x in range(1, 20) if x % 2 == 0}
print(set2)

# Test 2
print("\nTest2")
data = [2, 3, 3, 5, 7, 7, 8, 11, 11, 12, 13, 17, 19, 23, 29, 29, 29, 29, 31]
set3 = {x for x in data if x not in range(1, 10)}

print(data)
print(set3)
print("len of data", len(data))
print("len of set3", len(set3))
