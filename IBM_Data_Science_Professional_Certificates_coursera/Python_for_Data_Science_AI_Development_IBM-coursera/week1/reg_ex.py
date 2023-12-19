import re
# RegEx (short for Regular Expression) is a tool for matching and handling strings.
# module provides several functions for working with regular expressions, including search, split, findall, and sub

s1 = "dot pep is the best"

# Define the pattern to search for
pattern = r"pep"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")
