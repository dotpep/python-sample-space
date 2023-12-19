# with statement, w mode, write method
# every time the file data is overwritten
def with_write_w():
    with open("example2.txt", "w") as File1:
        File1.write("This is line 0 A\n")
        File1.write("This is line 1 B\nThis is line 2 C")


# write loop
# write each element in a list to a file
def with_loop_w():
    Lines = ["Line of A\n", "Line of B\n", "Line of C\n"]

    with open("example3.txt", "w") as File2:
        for line in Lines:
            File2.write(line)


# append mode "a"
def with_append_a():
    with open("example2.txt", "a") as File1:
        File1.write("\nThis is Append2 with (n - register in front) Lines")


# copy to new file
def copy_to_new():
    with open("example3.txt", "r") as readfile:
        with open("example2.txt", "w") as writefile:
            for line in readfile:
                writefile.write(line)

with_loop_w()
