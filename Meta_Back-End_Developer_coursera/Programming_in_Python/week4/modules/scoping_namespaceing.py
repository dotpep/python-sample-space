# LEGB (Local, Enclosed, Global, Built-in)

# global var and scope
x = 5


# built-in
def outer():
    # enclosed scope
    b = 2

    def inner():
        # local scope
        c = 3
        return c

    inner()
    return b


print(x)
print(outer())
