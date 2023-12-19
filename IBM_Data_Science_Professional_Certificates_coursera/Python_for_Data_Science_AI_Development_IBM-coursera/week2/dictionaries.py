DICT = {"Thriller": 1982, "Back in Black": 1980,
     "The Dark Side of the Moon": 1973, "The Bodyguard": 1992, "Bat Out of Hell": 1977, "Their Greatest Hits ": 1976,
     "Saturday Night Fever": 1977, "Rumours": 1977}

DICT2 = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

print(DICT2[(0, 1)])
print(DICT["Thriller"])

# add new item in Dictionary
DICT["Graduation"] = 2007

# delete item in Dictionary
del(DICT["Thriller"])

# verify element if an element is in Dictionary
verify1 = "The Bodyguard" in DICT
print(verify1)

verify0 = "Starboy" in DICT
print("none in dict: ", verify0)

# method keys to get the keys - object like a keys
keys_get = DICT.keys()
print(keys_get)

# method values to obtain the values
values_get = DICT.values()
print(values_get)

print(DICT)
