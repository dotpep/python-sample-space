# One Dimensional Numpy - numpy 1d (ND arrays) - library for scientific computing.
# Linear Algebra
import numpy as np
import matplotlib.pyplot as plt

# The Basics and Array Creation

a = np.array([0, 1, 2, 3, 4])
type(a)
# <class 'numpy.ndarray'>

a.dtype
# int32

a.size
# 5 elements

# Attribute ndim represents the number of array dimension of the rank of the array
a.ndim
# Attribute shape is a tuple of integers indicating the size of array in each dimension
a.shape

b = np.array([3.1, 11.02, 6.2, 213.2])
type(b) # <class 'numpy.ndarray'>
b.dtype # float64


# Indexing and Slicing

c = np.array([20, 1, 2, 3, 4])

c[0] = 100
c[3] = 20
c
# [100   1   20   3   4]

d = c[1:4]
c[3:5] = 300, 400

# Basic Operations

# Vector addition and Subtraction

u = [1, 0]
v = [0, 1]

z = []

for n, m in zip(u, v):
    z.append(n - m)
    # also use + or -

z

# Array multiplication with a Scalar

y = np.array([1, 2])
z = 2 * y

z


# Product of two numpy arrays (hadamard)

u = np.array([1, 2])
v = np.array([3, 2])
z = u * v

z

# Dot Product

u = np.array([4, 4])
v = np.array([1, 2])

result = np.dot(u, v)
result

# Adding Constant to an numpy Array
u = np.array([1, 2, 3, -1])
# broadcasting
z = u + 1
z

# Universal Functions
# work nd arrays

a = np.array([1, -1, 1, -1])
# calculate average value
mean_a = a.mean()

mean_a

b = np.array([1, -2, 3, 4, 5])
# find maximum value
max_b = b.max()

max_b

# np.pi
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)

y # [0.0000000e+00 1.0000000e+00 1.2246468e-16]


# Plotting Mathematical Functions
# lin space
x = np.linspace(-1, 2, num=9)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

y

# import matplotlib.pyplot as plt

plt.plot(x, y)
