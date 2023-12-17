
### Python Programming

Variable

```python
>>> a = b = c = 10
>>> print(a, b, c)
10 10 10
>>> print(a + b + c)
30
>>> a, b, c = 1, 2, 3
>>> print(a, b, c)
1 2 3
>>> print(a + b, c)
3 3
>>> a = 11
>>> print(a)
11
>>> a = 2
>>> print(a)
2
>>> b = a
>>> print(a)
2
>>> a = 3
>>> print(b)
2
>>> num_a = 1
>>> num_b = num_a
>>> print(num_a, num_b)
1 1
>>> num_a = 2
>>> print(num_a, num_b)
2 1
>>> c = 3
>>> del c
>>> print(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
```

- `myClass`, `var_1` and `print_this_to_screen`
- `Variable` and `variable` two different variables
- `c = 10` - better use full name `count = 10`


---
python key words:

|   |   |   |   |   |
|---|---|---|---|---|
|`False`|`await`|`else`|`import`|`pass`|
|`None`|`break`|`except`|`in`|`raise`|
|`True`|`class`|`finally`|`is`|`return`|
|`and`|`continue`|`for`|`lambda`|`try`|
|`as`|`def`|`from`|`nonlocal`|`while`|
|`assert`|`del`|`global`|`not`|`with`|
|`async`|`elif`|`if`|`or`|`yield`|

---
PEP-8


---
data types

|   |   |
|---|---|
|Text Type:|`str`|
|Numeric Types:|`int`, `float`, `complex`|
|Sequence Types:|`list`, `tuple`, `range`|
|Mapping Type:|`dict`|
|Set Types:|`set`, `frozenset`|
|Boolean Type:|`bool`|
|Binary Types:|`bytes`, `bytearray`, `memoryview`|
|None Type:|`NoneType`|


```python
# Text Type: str
text = "my_text"

# Numeric Types: int, float, complex
numeric_integer = 10
numeric_float = 10.5
numeric_complex = 1 + 2j

# Sequence Types: list, tuple, range
sequence_list = [1, 2, 3]
sequence_tuple = (1.22, "two", 3), (-2, 33, [1, 2, 3], {"dict": "tuple", "dict2": "tuple2", "dict_list": [1, 2, 3]})
sequence_range = range(6)

# Mapping Type: dict
mapping_dict = {"name": "John", "age": 36}

# Set Types: set, frozenset
set_types = {"apple", "banana", "cherry"}
frozenset_types = frozenset({"apple", "banana", "cherry"})

# Boolean Type: bool
boolean_type = True

# Binary Types: bytes, bytearray, memoryview
binary_bytes = b"Hello"
binary_bytearray = bytearray(5)
binary_memoryview = memoryview(bytes(5))

# None Type: NoneType
none_type = None

# Character is simply string with length of 1 
char = "a"
print(char)

```

Define data type and using method for that purpose
```python
>>> print(type(numeric_integer))
<class 'int'>
>>> print(type(numeric_float))
<class 'float'>
>>> print(type(mapping_dict))
<class 'dict'>
>>> print(type(text))
<class 'str'>
>>> print(type(boolean_type))
<class 'bool'>

```

Array and Matrix using numpy
```python
# Data structure

import numpy as np

# array (1 dimensional) 1d (just list of elements)
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array 1d:\n", array)

# matrix (2 dimensional) - 2d
matrix = np.array([
		[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 9]
		])
print("Matrix 2d:\n", matrix)


# 3 dimensional matrix (3d)

matrix_3d = [
	[[1, 2], [3, 4]], 
	[[5, 6], [7, 8]], 
	[[9, 10], [11, 12]]
]


```

List, Tuple, Dictionary, Set 
```python
>>> complex = 10 + 10j
>>> print(complex)
(10+10j)

---
>>> sequence_list = ["1 but 0 index", "2 but 1 index", "3 but 2 index", "4 but 3 index", "5, 4 list last"]
>>> print(sequence_list[0])
>>> sequence_tuple = (1.22, "two", 3), (-2, 33, [1, 2, 3], {"dict": "tuple"})
>>> print(sequence_tuple[0])
(1, 2, 3)
>>> sequence_range = range(6)
>>> print(sequence_range)
range(0, 6)
>>> sequence_tuple = (1.22, "two", 3), (-2, 33, [1, 2, 3], {"dict": "tuple"})
>>> print(sequence_tuple[0])
(1.22, 'two', 3)
>>> print(sequence_tuple[1])
(-2, 33, [1, 2, 3], {'dict': 'tuple'})
>>> print(sequence_tuple[1][2])
[1, 2, 3]
>>> print(sequence_tuple[1][2][0])
1
>>> print(sequence_tuple[1][3]["dict"])
tuple

---
>>> mapping_dict = {"name": "John", "age": 36}
>>> print(mapping_dict["name"])
John
>>> print(mapping_dict.get("name"))
John
>>> print(mapping_dict["age"])
36

---
>>> set_types = {"apple", "banana", "cherry"}
>>> print(set_types)
{'cherry', 'banana', 'apple'}
>>> set_types.add("orange")
>>> print(set_types)
{'orange', 'cherry', 'banana', 'apple'}
>>> frozenset_types = frozenset({"apple", "banana", "cherry"})
>>> print(frozenset_types)
frozenset({'cherry', 'banana', 'apple'})
>>> frozenset_types.add("orange")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'


```

range generators
```python
range_generator = range(1, 100)
for i in range_generator:
    print(i)
```


Queue and Stack
```python
# Queue
from collections import deque

queue = deque(["apple", "banana", "cherry"])
# add an element to the end of the queue
queue.append("orange")  
# remove an element from the beginning of the queue
queue.popleft()

print(queue)
Output: deque(['banana', 'cherry', 'orange'])

---
# Stack
stack = ["apple", "banana", "cherry"]

# add an element to the top of the stack
stack.append("orange")
# remove an element from the top of the stack
stack.pop()

print(stack)
Output: ['apple', 'banana', 'cherry']


```

tuple, dictionary, list comprehension testing and (slicing)
```python
# tuple(list(dictionary)) and extract using List Comprehension

# Define a tuple that contains a list of dictionaries
tuple_dict = (
	[{"dict_1": 1, "dict_2": 2}, 
	{"item": 1, "item2": 2, "item3": 3.2},
	],
)

# Extract all keys named "item" from the dictionaries inside the list
items = [d["item"] for d in tuple_dict[0] if "item" in d]
print(items)  # Output: [1]


# Define a dictionary
my_dict = {"item": [1, 2, 3, 4, 5, 6]}

# Extract each item in the list
for i in my_dict["item"]:
    print(i)


# Define a dictionary
my_dict = {"item": [1, 2, 3, 4, 5, 6]}

# Use list comprehension to print each item
[print(i) for i in my_dict["item"]]

>>> my_dict = {"item": [1, 2, 3, 4, 5, 6]}
>>> [print(i) for i in my_dict["item"]]
1
2
3
4
5
6
[None, None, None, None, None, None]
>>> new_list = [i for i in my_dict["item"]]
>>> print(new_list)
[1, 2, 3, 4, 5, 6]

---
# Slicing
>>> print(new_list[-1])
6
>>> print(new_list[1::2])
[2, 4, 6]
>>> print(new_list[0::2])
[1, 3, 5]
>>> print(new_list[0:2])
[1, 2]
>>> print(new_list[1:4])
[2, 3, 4]

---
# Stairs using list comprehension and slicing
# Create a list of numbers from 1 to 30
numbers = list(range(1, 31))

# Create stairs using the list
stairs = [' '.join(map(str, numbers[:i])) for i in range(1, len(numbers)+1)]
for stair in stairs:
    print(stair)

print("\nStairs with only odd numbers:\n")

# Create stairs using only the odd numbers in the list
odd_numbers = numbers[::2]  # Use slicing to get only the odd numbers
odd_stairs = [' '.join(map(str, odd_numbers[:i])) for i in range(1, len(odd_numbers)+1)]
for odd_stair in odd_stairs:
    print(odd_stair)


"""
In Python, list comprehension is used to create a new list from an existing list (or other iterable). 
>>> for_odd_stair = [odd_stair for odd_stair in odd_stairs] 
>>> print(for_odd_stair)
list `for_stairs` or `for_odd_stair`, Python displays the entire list as a single string, which is why the output might not look like stairs.
"""
>>> for_odd_stair = [print(odd_stair) for odd_stair in odd_stairs]
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
1 3 5 7 9 11
1 3 5 7 9 11 13
1 3 5 7 9 11 13 15
1 3 5 7 9 11 13 15 17
1 3 5 7 9 11 13 15 17 19
1 3 5 7 9 11 13 15 17 19 21
1 3 5 7 9 11 13 15 17 19 21 23
1 3 5 7 9 11 13 15 17 19 21 23 25
1 3 5 7 9 11 13 15 17 19 21 23 25 27
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

```

---
String

```python
my_variable = "This is \  
to big to fit \  
on a single line \  
so we multi-lined it"  
  
print(my_variable)

> (venv) PS D:\Programming\Python> python test1.py          
> This is to big to fit on a single line so we multi-lined it

  
a = 'This is a multi' \  
' line string example'  
  
print(a)

> This is a multi line string example
---
>>> name = "John"
>>> print(name[0])
J
>>> print(name[-1])
n
>>> len(name)
4
>>> surname = "Johann"
>>> print(f"Name: \t {name} \nSurname: \t {surname} ")
Name:    John
Surname:         Johann
>>> a = 22
>>> b = 8
>>> info_num = "first num {} plus second num {} is {}".format(a, b, a + b)
>>> info_num
'first num 22 plus second num 8 is 30'
---
# Concatenation
a = "my favorite food is "
b = "mashed potatoes"
# You then print these strings together with self line:
# is called Concatenation
print(a + b)
> my favorite food is mashed potatoes

---
>>> location = input("where do you live?: ")
moscow
>>> input_words = "where do you live?: "
>>> location = input(input_words)
where do you live?: Moscow
>>> info = f"So you live in {location}"
>>> print(info)
So you live in Moscow
```


---
Type Casting (Implicit and Explicit)
is Converting data type into another (for example: database purpose)

- `str()`
- `int()`
- `float()`
```python
>>> a = 11
>>> b = 2
>>> a + b
13
>>> str(a) + str(b)
'112'
>>> text_1 = "1"
>>> text_2 = "2"
>>> text_1 + text_2
'12'
>>> int(text_1) + int(text_2)
3
>>> some_int = 10
>>> float(some_int)
10.0
```

- `ord()` - returns the Unicode point for a one-character string.
- `hex()` - converts an integer into a Hexadecimal string.
- `oct()` - converts an integer into an Octal string.
- `tuple()` - converts an Iterable into a Tuple.
- `set()` - converts an Iterable into a Set.
- `list()`- converts an Iterable into a List.
- `dict()`

```python
print(ord('A'))
# Output: 65

print(hex(255))
# Output: '0xff'

print(oct(8))
# Output: '0o10'

print(tuple([1, 2, 3]))
# Output: (1, 2, 3)

print(set([1, 2, 2, 3, 3, 3]))
# Output: {1, 2, 3}

print(list((1, 2, 3)))
# Output: [1, 2, 3]

print(dict([('one', 1), ('two', 2), ('three', 3)]))
# Output: {'one': 1, 'two': 2, 'three': 3}

---
# hex to int
num1 = hex(255)  # '0xff'
num2 = hex(192)  # '0xc0'

# Convert hex to number
num1_int = int(num1, 16)  # 255
num2_int = int(num2, 16)  # 192

# Now you can add them
sum_of = num1_int + num2_int
print(sum_of)  # Output: 447

---
my_list = ['apple', 'banana', 'cherry']
my_dict = {"key1": my_list[0]}
print(my_dict)
# Output: {'key1': 'apple'}

my_list = ['apple', 'banana', 'cherry']
my_dict = {f'key_{i}': my_list[i] for i in range(len(my_list))}
print(my_dict)
# Output: {'key0': 'apple', 'key1': 'banana', 'key2': 'cherry'}

```


convert IP address to Machine Code 
```python
ip = '192.168.1.1'
ip_binary = '.'.join(format(int(x), '08b') for x in ip.split('.'))
print(ip_binary)  
# Output: 11000000.10101000.00000001.00000001

---
ip_value_1 = int(input("ip value 1: "))  
ip_value_2 = int(input("ip value 2: "))  
ip_value_3 = int(input("ip value 3: "))  
ip_value_4 = int(input("ip value 4: "))  
  
ip = f'{ip_value_1}.{ip_value_2}.{ip_value_3}.{ip_value_4}'  
ip_binary = '.'.join(format(int(x), '08b') for x in ip.split('.'))  
print(ip_binary)

---
def get_ip_value(prompt):
    while True:
        ip_value = int(input(prompt))
        if 0 <= ip_value <= 255:
            return ip_value
        else:
            print("Invalid input. Please enter a number between 0 and 255.")

ip_values = [get_ip_value(f"ip value {i + 1}: ") for i in range(4)]

ip = '.'.join(map(str, ip_values))
ip_binary = '.'.join(format(x, '08b') for x in ip_values)
print(ip_binary)


```


---
User Input and Output
```python
>>> print("Hello", "You!", sep=", ")
Hello, You!
>>> print("Hello", "World", "You!", sep=", ")
Hello, World, You!
>>> print("Hello", "World", "Each words", "in Comma", "You!", sep=", ")
Hello, World, Each words, in Comma, You!
>>> a = 10
>>> b = 5
>>> ans = 10 + 5
>>> "adding the value of {} and {} = {}".format(a, b, ans)
'adding the value of 10 and 5 = 15'
>>> "i like {1} more than {0}".format("white", "black")
'i like black more than white'
>>> "i like {0} more than {1}".format("white", "black")
'i like white more than black'
>>> num1 = input("num1: ")
num1: 5
>>> num2 = input("num2: ")
num2: 6
>>> print(num1 + num2)
56
>>> num1 = int(input("num1: "))
num1: 4
>>> num2 = int(input("num2: "))
num2: 4
>>> print(num1 + num2)
8
>>> int_input = input()
3
>>> type(int_input)
<class 'str'>

---
>>> 10 == 10
True
>>> 10 != 10
False
>>> 10 > 11
False
>>> 10 < 11
True
>>> 10 <= 10
True
>>> 10 >= 10
True

---
>>> num1 = 10
>>> num2 = 12
>>> num1 += num2
>>> num1
22
>>> num1 -= num2
>>> num1
10
>>> num1 /= num2
>>> num1
0.8333333333333334

---
>>> num1 == float
False
>>> num1 == float(num1)
True
>>> num1 == str(num1)
False
>>> num1 == int(num1)
False
>>> num2 == float(num2)
True
>>> num2
12
>>> num2 == int(num2)
True
>>> int(num2) == float(num2)
True

---
>>> 10 == 10
True
>>> 10 == 10.00
True
>>> 10 + 10.00
20.0
>>> 10.0 + 10
20.0
>>> type(10 + 10.0)
<class 'float'>

---
>>> str_num1 = input("num1 ")
num1 5
>>> str_num2 = input("num2 ")
num2 5
>>> str_num1 + str_num2
'55'
>>> int(str_num1 + str_num2)
55
>>> int(str_num1) + int(str_num2)
10
>>> float_num1 = float(str_num1)
>>> float_num2 = float(str_num2)
>>> int(float_num1) + " is num1"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(float_num1) + " is num1"
'5.0 is num1'
```




---
lab
```python
>>> float_input1 = float(input("price of coffee: "))
price of coffee: 2.00
>>> float_input2 = float(input("price of sandwich: "))
price of sandwich: 4.99
>>> float_input3 = float(input("price of cake: "))
price of cake: 2.75
>>> "Your total bill is $", float_input1 + float_input2 + float_input3
('Your total bill is $', 9.74)
```

---
##### Build-in Functions

- "".join
- map()
- format()
```python

```

- object
- sep
- end
- file
- flush
```python

```

---
##### SRC
src:
- [Built-in Functions — Python 3.12.0 documentation](https://docs.python.org/3/library/functions.html)
- [Solve Python | HackerRank](https://www.hackerrank.com/domains/python)
- [Python Tutorial (w3schools.com)](https://www.w3schools.com/python/)


### Control flow and Conditionals


---
Logical Operators
- and
- or
- not()
```python
>>> True + True
2
>>> False + False
0
>>> False + True
1
>>> True / True
1.0

---
>>> True and True
True
>>> True and False
False
>>> True or True
True
>>> True or False
True
>>> False or False
False

---
>>> not(True)
False
>>> not(False)
True

---
>>> True and not(False)
True
>>> True and not(True)
False
>>> True or not(False)
True
>>> True or not(True)
True
>>> False or not(True)
False

---
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and True or True
True
>>> False and True or False
False
>>> True and True or True
True
>>> True and True or False
True
>>> False and True or True
True
>>> False and True or False
False
```

##### Control flow (if and loop)
---
if statement - conditions | conditional statement
- if
- else
- elif (else if)
```python
bill_total = 210  
discount1 = 10  
discount2 = 20  
  
  
if bill_total > 100 and bill_total < 200:  
print(f"Bill is greater than 100! discount: {discount1}")  
bill_total = bill_total - discount1  
elif bill_total > 200:  
print(f"Bill is greater than 200! discount: {discount2}")  
bill_total = bill_total - discount2  
else:  
print("Bill is less than 100!")  
  
print("Total bill: " + str(bill_total))
```
```python
temperature = 30  
humidity = 70  
  
if temperature > 25:  
print("It's hot today!")  
  
if humidity > 60:  
print("It's humid today!")  
  
if temperature > 25 and humidity > 60:  
print("It's a hot and humid day!")
```
```python
current = False  
  
if current:  
current = False  
print('Turning light off')  
  
if not current:  
current = True  
print('Turning light on')
```
```python
loyalty_customer = True
total_bill = 124

  
if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20

elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10

else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))
```

---
Match statement (switch in c#) in python 3.10
- match (switch)
- case
```python
# http_status = 200  
http_status = int(input("return http status code: "))  
# http_status = 200 or 500 or 444  
  
match http_status:  
	case 200 | 201:  
		print("Success")  
	case 400:  
		print("Bad request")  
	case 404:  
		print("Not Found")  
	case 500 | 501:  
		print("Server Error")  
	case _:  
		print("Unknown")  
  
  
if http_status == 200 or http_status == 201:  
	print("Success")  
elif http_status == 400:  
	print("Bad request")  
elif http_status == 404:  
	print("Not Found")  
elif http_status == 500 or http_status == 501:  
	print("Server Error")  
else:  
	print("Unknown")
```


---
looping constructs 

for
```python
str = "Looping"  
  
# for item in str:  
# print(item)  
  
# for item in range(1, len(str) + 1):  
# print(str[-item])  
  
# for i in range(10):  
# print(str, "...", i + 1)  
  
# for i in range(1, 11):  
# print(str, "...", i)  
  
```

- break
- continue
- pass
```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert) 
    else:
        print('No sorry, that dessert is not on my list')

output = """
No sorry, that dessert is not on my list 
No sorry, that dessert is not on my list 
Yes one of my favorite desserts is Churros 
No sorry, that dessert is not on my list 
No sorry, that dessert is not on my list
"""

# to fix that use (break)

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
	print('No sorry, not a dessert on my list')
```
```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)
```
```python
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)
```

break
```python
num = int(input("num: "))  
  
for n in range(num):  
	if n == 5:  
		break  
	print(n + 1)  
else:  
	print("Loop is ended")  
print("Exit on loop")
```

continue
```python
num = int(input("num: "))  
  
for n in range(num):  
	if n == 5:  
		continue  
	print(n + 1)  
else:  
	print("Loop is ended")  
print("Exit on loop")
```

pass
```python
x = 3  
if x == 3:  
	pass  
else:  
	print("x not equal 3")
```


while
```python
favorites = ['Creme Brulee', 'Apple', 'Churros', 'Chocolate']  
  
count = 0  
while count < len(favorites):  
print(f"I like self desert {favorites[count]}")  
count += 1
```

nested loop
```python
list1 = range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
list2 = range(1, 10)  
  
count = 0  
  
for i in list2:  
	count += 1  
	for j in list2:  
		count += 1  
  
print(count)

###

# outer loop  
for i in range(1):  
	# inner loop  
	for j in range(10):  
		print(j, end=" ")  
print()

###

# outer loop  
for i in range(10):  
	# inner loop  
	for j in range(10):  
		print(i, " : ", j)  
print("\n")

###

# outer loop  
for i in range(0, 10, 2):  
	# inner loop  
	for j in range(0, 10, 2):  
		print(j, end=" ")  
print()
```
```python
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
```

---
enumerate vs range
```python
for i in range(len(favorites)):  
print(i + 1, favorites[i])  
  
print("\n")  
  
for idx, item in enumerate(favorites):  
print(idx + 1, item)
```

enumerate
```python
>>> a = [10, 20, 30, 40]
>>> print(enumerate(a))
<enumerate object at 0x00000215CBCEFA80>
>>> print(type(enumerate(a)))
<class 'enumerate'>
>>> print(list(enumerate(a)))
[(0, 10), (1, 20), (2, 30), (3, 40)]
>>> # tuple with first element is index element and second is element 
>>> for item in enumerate(a):
...     print(item)
...
(0, 10)
(1, 20)
(2, 30)
(3, 40)
>>> for index, value in enumerate(a):
...     print(index, value)
...
0 10
1 20
2 30
3 40
>>> for index, value in enumerate(a):
...     if value % 20 == 0:
...             print(index, value)
...
1 20
3 40
>>> for index, value in enumerate(a):
...     value += 1
...     print(value)
...
11
21
31
41
>>> for index, value in enumerate(a):
...     a[index] += 1
...     print(a)
...
[11, 20, 30, 40]
[11, 21, 30, 40]
[11, 21, 31, 40]
[11, 21, 31, 41]

---
>>> # string
>>> s = "hello"
>>> for index, value in enumerate(s):
...     print(index, value)
...
0 h
1 e
2 l
3 l
4 o
>>> # string tuple
>>> t = {'apple', 'banana', 'mango'}
>>> for index, value in enumerate(t):
...     print(index, value)
...
0 apple
1 banana
2 mango
>>> # dictionary
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for index, value in enumerate(d):
...     print(index, value)
...
0 a
1 b
2 c
>>> # create range of nums 10 - 20
>>> for index, value in enumerate(range(10, 20)):
...     print(index, value)
...
0 10
1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
>>> for index, value in enumerate(t, 10):
...     print(index, value)
...
10 apple
11 banana
12 mango
>>> for index, value in enumerate(t, 1):
...     print(index, value)
...
1 apple
2 banana
3 mango
>>> for index, value in enumerate(t, 1):
...     print(index * 10, value)
...
10 apple
20 banana
30 mango
```

range
```python
>>> range(5)
range(0, 5)
>>> type(range(5))
<class 'range'>
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(15))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> list(range(1, 15))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(0, 100, 10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

---
>>> list(range(1, 101, 10))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
>>> list(range(1, 102, 10))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> list(range(0, 10, 1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]


---
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 20, 3))
[10, 13, 16, 19]
>>> sum(range(1, 101))
5050
>>> sum(range(1, 4))
6
>>> len(range(5, 15, 5))
2


---
>>> a, b, c = range(5, 8)
>>> a
5
>>> b
6
>>> c
7
>>> r = range(1, 7)
>>> len(r)
6
>>> r[0]
1
>>> r[-1]
6
>>> v = iter(range(5))
>>> v
<range_iterator object at 0x00000215CB86F850>
>>> next(v)
0
>>> next(v)
1
>>> v.__next__()
2
>>> v.__next__()
3
>>> next(v)
4
>>> next(v)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> n = iter([43, True, 'hello'])
>>> next(n)
43
>>> next(n)
True
>>> next(n)
'hello'
>>> next(n)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> m = iter("hi")
>>> next(m)
'h'
>>> next(m)
'i'
>>> next(m)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```


---
lab
```python
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0
for index, value in enumerate(num_list):
    if value > 100:
        print("Over 45")
        break
	count += 1
else:
    print("Under 45")
```
```python
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for num in num_list:
    if num > 45:
        print(num, 'Over 45')
    else:
        print(num, 'Under 45')
```
```python
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0
for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)
```



