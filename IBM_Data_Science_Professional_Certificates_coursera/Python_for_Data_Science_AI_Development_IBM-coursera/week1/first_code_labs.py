import sys


def first_output():
    # Try your first Python output
    print('Hello, World!')
    # print() is a function. You passed the string 'Hello, Python!' as an argument to instruct Python on what to print.


def version_py():
    # import sys
    print(sys.version)
    # sys is a built-in module that contains many system-specific parameters and functions, including the Python version in use. Before using it, we must explictly import it.
    # this is comment
    """
    another long type of comment
    """


def types():
    test1 = "11 hello return"
    type(12)
    int(2.333)
    float(2)
    str("hello types, 44554")
    print(bool(1))
    return test1


def types_sys():
    print(sys.float_info)


def min_to_hour():
    box_minut = int(input("Write a Minutes to Hours: "))
    if int(box_minut):
        hours_num = box_minut / 60
        print(f"hours: {hours_num}, minutes: {box_minut}")
    else:
        print("write number, integer!")


min_to_hour()
