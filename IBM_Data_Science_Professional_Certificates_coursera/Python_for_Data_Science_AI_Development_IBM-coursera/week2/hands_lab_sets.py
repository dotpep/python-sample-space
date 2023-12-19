
# logic sets operations
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections - &, and
intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2
difference_set1 = album_set1.difference(album_set2)
print(difference_set1, "difference_set1")

difference_set2 = album_set2.difference(album_set1)
print(difference_set2, "difference_set2")

# Methods
# Use intersection method to find the intersection of album_list1 and album_list2
intersection = album_set1.intersection(album_set2)
print(intersection)

# Find the union of two sets
union = album_set1.union(album_set2)
print(union)

# Check if superset - False
issuperset = set(album_set1).issuperset(album_set2)
print(issuperset)

# Check if subset - False
subset = set(album_set2).issubset(album_set1)
print(subset)

# Check if superset - True
issuperset = album_set1.issuperset({"Back in Black", "AC/DC"})
print(issuperset)

# Check if subset - True
subset = set({"Back in Black", "AC/DC"}).issubset(album_set1)
print(subset)



# sum(A) == sum(B)
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))



