def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial


def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)


print(find_factorial_recursive(5))
