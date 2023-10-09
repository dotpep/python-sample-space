def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")
        print()


def print_column(height):
    print("?" * height)


def print_row(width):
    print("#\n" * width, end="")


main()
