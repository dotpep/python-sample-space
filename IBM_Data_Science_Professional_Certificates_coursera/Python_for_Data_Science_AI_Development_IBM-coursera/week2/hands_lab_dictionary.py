release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

# Get value by keys
release_year_dict['Thriller']

# Delete Keys and Value
del(release_year_dict['Thriller'])
print(release_year_dict)

# Add new Keys and Value last of dictionary
add_dict = release_year_dict['Thriller'] = '1982'
print(add_dict)

# Get value by key
get_value_by_key = release_year_dict['The Bodyguard']
print(get_value_by_key)

# Get all the keys in dictionary
get_all_keys = release_year_dict.keys()
print(get_all_keys)

# Get all the values in dictionary
get_all_value = release_year_dict.values()
print(get_all_value)

# Verify the key is in the dictionary
verify_dict = 'The Bodyguard' in release_year_dict
print(verify_dict)

verify_dict = 'staybord' in release_year_dict
print(verify_dict)

