"""
Algorithmic complexity
time and space.
"""
import random

# constant time (0 iterations)
drinks = {1: "coffee", 2: "tea", 3: "juice"}
constant_time = drinks[2]


# linear time - growth time depending on size inputs (100 elements = 100 iterations)
for x in range(10000):
    linear_time = x


def find_num(num):
    iter_count = 0
    for x in range(100):
        if x == num:
            return f"total iterations: {iter_count}, to find: {x}"
        iter_count += 1


linear_time = find_num(97)


# logarithmic time
# using binary search (dividing half of range and check half if in 100 = 50, 25, 13, 6, 3, 2, 1)
def find_num_log(target, ranges):
    iterations_count = 0

    x = range(ranges)
    left_start = 0
    right_last = len(x) - 1

    while left_start <= right_last:
        iterations_count += 1
        middle = (left_start + right_last) // 2
        isNumber = x[middle]

        if target == isNumber:
            return f"total iterations: {iterations_count}, in range: {ranges}, to find: {middle}"
        elif target < isNumber:
            right_last = middle - 1
        else:
            left_start = middle + 1
    return -1


random_num = random.randint(1, 1000)

logarithmic_time = find_num_log(random_num, 1000)

# quadratic time
# nested loops range(x = 10, y = 10) when x make 1 iteration then y make 10 iterations (x:10 * y:10 = xy:100, xy:10^10)
for x in range(10):
    for y in range(10):
        quadratic_time = x, y


# exponential time
# using recursion (calling a function inside function itself )
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


exponential_time = fibonacci(24)

# print(exponential_time)
