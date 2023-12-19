# Creating Sets
set1 = {"pop", "pop", "rock"}
print(set1)

# Convert Lists to Sets
album_list = ["dot pep", "Isekai", "Isekai", 1982]
album_set = set(album_list)
print(album_list)
print(album_set)

# Set Operations
A = {"Fantasy", "Ousama Ranking", "AC/DC"}
A.add("Middle-ages")
print(A)
# also add same item will not show or duplicate in sets.

A.remove("AC/DC")
print(A)
# add() & remove() - method

print("Ousama Ranking" in A)
# checking items (in)

print("Ousama Ranking" and "Isekai" in A)



# Mathematical Set Operations
album_set_1 = {"Sebastian", "Kato", "Kurumi", "Narberal Gamma", "Rimuru"}
album_set_2 = {"Sebastian", "Narberal Gamma", "Bojji", "Ainz"}
album_set_3 = album_set_1 and album_set_2
# use: &, and
print(album_set_3)

# union - new set that has all elements/items both album set 1 and 2 variable
print(album_set_1.union(album_set_2))

# encapsulates
album_set_2 = {"Sebastian", "Narberal Gamma"}
album_set_3 = album_set_1 & album_set_2
print(album_set_3)

# check if set is a subset using - issubset method
print(album_set_2.issubset(album_set_1))
