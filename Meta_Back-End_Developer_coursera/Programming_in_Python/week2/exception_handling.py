def divide_by(a, b):
    return a / b


# print(divide_by(40, 0)) # ZeroDivisionError: division by zero

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "Something went wrong!")
    print(e.__class__)

# Starter code
items = [1, 2, 3, 4, 5]
# item = items[6]
# print(item)
try:
    item = items[6]
except IndexError:
    print("Item does not exist in the list")


# Starter code
def divide_by(a, b):
    return a / b


# ans = divide_by(40, 0)
# print(ans)

try:
    ans = divide_by(40, 0)
except ZeroDivisionError:
    print(0)

# Starter code
# with open('file_does_not_exist.txt', 'r') as file:
# print(file.read())

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file could not be found")


def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')


ans = divide_by(10, 0)
ans2 = divide_by(10, "a")
print(ans)
print(ans2)


myvariable = NotImplemented
print(myvariable)

def myfunc1():
    raise NotImplementedError


def myfunc2():
    pass
