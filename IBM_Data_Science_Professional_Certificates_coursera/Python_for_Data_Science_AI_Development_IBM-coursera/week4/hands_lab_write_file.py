exmp1 = 'exmp1.txt'
exmp2 = 'exmp2.txt'

pattern_write = "writen pattern:\nLine1\nLine2\n"
pattern_append = "append pattern: \nLine3B\nLine4A\n"
pattern1 = "Line of A\nLine of B\nLine of C\n"
pattern2 = ["r+ : Reading and writing. Cannot truncate the file.\n",
            "w+ : Writing and reading. Truncates the file.\n",
            "a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab."]

def writefile1():
    # Write line to file
    with open(exmp1, 'w') as writefile:
        writefile.write("This is line B and A\n")
        writefile.write("This is also line B and A, \nbut another")
        writefile.write("Line \fF and \vA, \rbut: \tcheck\n \\ back-slash")

    # Read file
    # Verify if writing to file is successfully executed
    with open(exmp1, 'r') as testwritefile:
        print(testwritefile.read())

    # However, note that setting the mode to w overwrites all the existing data in the file.

    with open(exmp1, 'w') as writefile:
        writefile.write("Overwrite\n")
    with open(exmp1, 'r') as testwritefile:
        print(testwritefile.read())

    # appending files
    # Write a new line to text file

    with open(exmp1, 'a') as testwritefile:
        testwritefile.write("Append is line C\n")
        testwritefile.write("append is line D\n")
        testwritefile.write("APPEND is line E\n")


def testfile1():
    with open(exmp2, "w") as writefile:
        writefile.write(pattern_write)
    with open(exmp2, "a") as appendfile:
        appendfile.write(pattern_append)

def test_plus_mode():
    # Additional modes
    with open(exmp1, 'w+') as testwritefile:
        testwritefile.write(pattern1)
        print(testwritefile.read())


def revisit_plus_a():
    with open(exmp2, 'a+') as testwritefile:
        print("Initial Location: {}".format(testwritefile.tell()))

        data = testwritefile.read()
        if (not data):  # empty strings return false in python
            print('Read nothing')
        else:
            print(testwritefile.read())

        testwritefile.seek(0, 0)  # move 0 bytes from beginning.

        print("\nNew Location : {}".format(testwritefile.tell()))
        data = testwritefile.read()
        if (not data):
            print('Read nothing')
        else:
            print(data)

        print("Location after read: {}".format(testwritefile.tell()))


def between_plus_w_r():
    with open(exmp2, 'r+') as testwritefile:
        data = testwritefile.readlines()
        testwritefile.seek(0, 0)  # write at beginning of file

        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("finished\n")
        # Uncomment the line below
        # testwritefile.truncate()
        testwritefile.seek(0, 0)
        print(testwritefile.read())

def copy_file():
    # Copy file to another
    with open('Example2.txt', 'r') as readfile:
        with open('Example3.txt', 'w') as writefile:
            for line in readfile:
                writefile.write(line)

    # Verify if the copy is successfully executed
    with open('Example3.txt', 'r') as testwritefile:
        print(testwritefile.read())


