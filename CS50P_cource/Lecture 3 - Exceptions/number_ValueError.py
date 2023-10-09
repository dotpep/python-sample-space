def main():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x not in Integer!")
        else:
            print(f"x is {x}")
            break


main()


def second():
    while True:
        try:
            x = int(input("What's second x?"))
            break
        except ValueError:
            print("second x not in Integer!")
    print(f"second x is {x}")

