import random


# O(1) - Constant Time
def access_element(arr, index):
    return arr[index]


# O(n) - Linear Time
def linear_search(arr, target):
    iter_count = 0
    for item in arr:
        if item == target:
            return True, iter_count
        iter_count += 1

    return False, iter_count


# O(n^2) - Quadratic Time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# O(log n) - Logarithmic Time
def binary_search(arr, target):
    iter_count = 0
    left_start, right_end = 0, len(arr) - 1
    while left_start <= right_end:
        iter_count += 1

        middle = (left_start + right_end) // 2
        if arr[middle] == target:
            return middle, iter_count
        elif arr[middle] < target:
            left_start = middle + 1
        else:
            right_end = middle - 1
    return -1, iter_count


rand_arr = random.sample(range(1, 101), 100)
arr = range(0, 100)

constant_time = access_element(arr, 0)
linear_time = linear_search(arr, 27)

x = 1000000
logarithmic_time = binary_search(range(0, x), random.randint(0, x))

# print("unsortered: ", rand_arr)
# unsortered = rand_arr

# unsortered = print(rand_arr)
# quadratic_time = bubble_sort(rand_arr)
# sortered = rand_arr
# print(sortered)

print(logarithmic_time)
