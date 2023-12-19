# open statement
# open txt file with name & mode: r - reading
File1 = open("example.txt", "r")

# data attribute
# name - to get the name of file
File1.name

# mode - to see what mode the object is in using
File1.mode

# You should always close the file object using the method close.
File1.close()

print(File1.read)

# with statement
# print the file content outside the indent as well.

with open("example.txt", "r") as File2:
    # method "read" - stores the values of the file in the variable "file_stuff" as a string.
    # file_stuff = File2.read()
    # method readlines - We can output every line as an element in a list
    file_stuff = File2.readlines()
    # method readline - to read first line of the file
    # file_stuff = File2.readline()
    print(file_stuff)

File2.name

# check file is closed
print(File2.closed)

# print the file content outside the indent as well.
print(file_stuff[1])
print(file_stuff[0][0:3])

