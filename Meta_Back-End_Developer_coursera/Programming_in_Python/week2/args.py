def sum_of1(a, b):
    return a + b


print(sum_of1(4, 5))


def sum_of2(*args):
    # print(type(args))
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of2(4, 5, 6, 7.4))
