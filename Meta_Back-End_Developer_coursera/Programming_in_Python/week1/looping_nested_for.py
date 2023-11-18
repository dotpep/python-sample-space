# list1 = range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
# list2 = range(1, 10)
#
# count = 0
#
# for i in list2:
#     count += 1
#     for j in list2:
#         count += 1
#
# print(count)


# Time Complexity
import time
start_time = time.time()

# outer loop
for i in range(100):
    # inner loop
    for j in range(10000):
        print(j, end=" ")
    print()

print(round((time.time() - start_time), 8))



# # outer loop
# for i in range(1):
#     # inner loop
#     for j in range(10):
#         print(j, end=" ")
#     print()


# # outer loop
# for i in range(0, 10, 2):
#     # inner loop
#     for j in range(0, 10, 2):
#         print(j, end=" ")
#     print()


# # outer loop
# for i in range(10):
#     # inner loop
#     for j in range(10):
#         print(i, " : ", j)
#     print("\n")