# 1/0
# ZeroDivisionError: division by zero

# y = a + 5
# NameError: name 'a' is not defined

# a = [1, 2, 3]
# a[10]
# IndexError: list index out of range

# Try Except
def example_try1():
    # potential code before try catch

    try:
    # code to try to execute
        pass
    except:
        pass
    # code to execute if there is an exception

    # code that will still execute if there is an exception


def try_except_test1():
    a = 1
    try:
        b = int(input("Please enter a number to divide a: "))
        a = a / b
        print("Success a=", a)
    except:
        print("There was an error")

# Try Except Specific

def example_try_specific1():
    # potential code before try catch

    try:
    # code to try to execute
        pass
    except (ZeroDivisionError, NameError):
        pass
    # code to execute if there is an exception of the given types

    # code that will execute if there is no exception or a one that we are handling

def example_try_specific2():
    # potential code before try catch

    try:
        pass
    # code to try to execute
    except ZeroDivisionError:
        pass
    # code to execute if there is a ZeroDivisionError
    except NameError:
        pass
    # code to execute if there is a NameError

    # code that will execute if there is no exception or a one that we are handling

def example_try_specific3():
    # potential code before try catch

    try:
        pass
    # code to try to execute
    except ZeroDivisionError:
        pass
    # code to execute if there is a ZeroDivisionError
    except NameError:
        pass
    # code to execute if there is a NameError
    except:
        pass
    # code to execute if ther is any exception

    # code that will execute if there is no exception or a one that we are handling

def try_specific1():
    a = 1
    try:
        b = int(input("Please enter a number to divide a: "))
        a = a / b
        print("Success a=",a)
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")


# Try Except Else and Finally

def example_try_else_final1():
    # potential code before try catch

    try:
        pass
    # code to try to execute
    except ZeroDivisionError:
        pass
    # code to execute if there is a ZeroDivisionError
    except NameError:
        pass
    # code to execute if there is a NameError
    except:
        pass
    # code to execute if ther is any exception
    else:
        pass
    # code to execute if there is no exception

    # code that will execute if there is no exception or a one that we are handling

def example_try_else_final2():
    # potential code before try catch

    try:
        pass
    # code to try to execute
    except ZeroDivisionError:
        pass
    # code to execute if there is a ZeroDivisionError
    except NameError:
        pass
    # code to execute if there is a NameError
    except:
        pass
    # code to execute if ther is any exception
    else:
        pass
    # code to execute if there is no exception
    finally:
        pass
    # code to execute at the end of the try except no matter what

    # code that will execute if there is no exception or a one that we are handling

def try_else1():
    a = 1

    try:
        b = int(input("Please enter a number to divide a: "))
        a = a/b
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")
    else:
        print("success a=",a)

def try_final1():
    a = 1

    try:
        b = int(input("Please enter a number to divide a: "))
        a = a / b
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")
    else:
        print("success a=", a)
    finally:
        print("Processing Complete")

try_final1()
