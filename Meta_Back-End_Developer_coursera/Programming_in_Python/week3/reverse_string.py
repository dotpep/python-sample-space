str_word = "reversal"
word = "123456"

# slicing str[start:stop:step]
reversed_with_slicing = str_word[::-1]

# test slicing
length = len(str_word)
test1_slicing = str_word[6:length - 1]
test2_slicing = word[1:] + word[0]


# print(reversed_with_slicing)


# reverse string using recursion algorithm
def string_reverse(str):
    if len(str) == 0:
        return str
    return string_reverse(str[1:]) + str[0]


# print(string_reverse(str_word))


# reverse using loop
def reversed1(variable):
    result = ''
    for i in range(len(variable) - 1, -1, -1):
        result += variable[i]
    return result


# rev1 = reversed1(input())
# print(rev1)


def reversed2(variable):
    res = []
    for i in range(len(variable) - 1, -1, -1):
        res.append(variable[i])
    # print(type(res))
    res = ''.join(res)
    # print(type(res))
    return res


# rev2 = reversed2(input())
# print(rev2)


def reversed3(variable):
    if len(variable) == 1:
        return variable
    return variable[-1] + reversed3(variable[:-1])

# rev3 = reversed3(input())
# print(rev3)


def reversed4(variable):
    res = ''.join(reversed(variable))
    return res

# rev4 = reversed4(input())
# print(rev4)


# slicing
n = input()[::-1]
print(n)
