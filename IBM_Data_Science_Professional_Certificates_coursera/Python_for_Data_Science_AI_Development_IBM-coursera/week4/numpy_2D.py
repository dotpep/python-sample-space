# Two Dimensional Numpy
# Linear Algebra
import numpy as np

# The Basics and Array Creation in 2D
# Indexing and Slicing in 2D
# Basic Operations in 2D

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
x = np.array(a)

x.ndim
# 2 матричных вложения

x.shape
# (3, 3) - показывает некие столбцы rows and columns - так как у нас 2 матричных вложения у нас только 2 числа и каждая по 3 на 3

x[2][2]
x[0:3]

x[0, 0:2]
print(x[0:2, 2])


x = [[1, 0], [0, 1]]
y = [[2, 1], [1, 2]]

x = np.array(x)
y = np.array(y)
z = x + y
z = x * y

z

a = [[0, 1, 1], [1, 0, 1]]
b = [[1, 1], [1, 1], [-1, 1]]

a = np.array(a)
b = np.array(b)
c = np.dot(a, b)

print(c)

print(a.size)

