str = "Looping"

# for item in str:
#     print(item)

# for item in range(1, len(str) + 1):
#     print(str[-item])

# for i in range(10):
#     print(str, "...", i + 1)

# for i in range(1, 11):
#     print(str, "...", i)


# favorites = ['Creme Brulee', 'Apple', 'Churros', 'Chocolate']
#
# for i in range(len(favorites)):
#     print(i + 1, favorites[i])
#
# print("\n")
#
# for idx, item in enumerate(favorites):
#     print(idx + 1, item)

num = int(input("num: "))

for n in range(num):
    if n == 5:
        continue
    print(n + 1)
else:
    print("Loop is ended")
print("Exit on loop")


x = 3
if x == 3:
    pass
else:
    print("x not equal 3")
