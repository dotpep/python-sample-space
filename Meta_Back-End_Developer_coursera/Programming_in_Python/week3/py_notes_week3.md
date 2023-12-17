### Procedural Programming

![[Pasted image 20231128170306.png|500]]

#### Algorithm 

Define Palindrome 
- string - examples are _civic_, _radar_, _level_, _rotor_, _kayak_, _madam_, and _refer_, *rotator*, *deified*, *racecar* and _reviver_;
- number - 
- and may words, sentence, numeric, dates, speech, classical music, biological structure, computation theory

```python
# Algorithm for a Palindrome  
  
def isPalindrome(str):  
	startIndex = 0  
	endIndex = len(str) - 1  
	  
	for x in str:  
		if str[startIndex] != str[endIndex]:  
			return False  
	return True  
  
  
word = "racecars"  
  
print(isPalindrome(word))
```

---
```python
>>> str = "racecar"
>>> len(str)
7
>>> str[0]
'r'
>>> str[6]
'r'
>>> str[-1]
'r'
>>>
>>> str[0] == str[6]
True
>>> str[0 + 1] == str[6 - 1]
True
>>> str[0 + 2] == str[6 - 2]
True
>>> str[0 + 3] == str[6 - 3]
True
>>>
>>>
>>> str[0] == str[6]
True
>>> str[1] == str[5]
True
>>> str[2] == str[4]
True
>>> str[3] == str[3]
True
>>> str[0] == str[-1]
True
>>> str[1] == str[-2]
True
>>> str[2] == str[-3]
```

---
Exercise: Make a cup of coffee
Introduction: In self exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product. 
Instructions: 
Step 1: Start with the inputs - what is needed to make a cup of instant coffee?
Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.
Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it. 
Step 4: The algorithm when complete should have as its final result a cup of coffee.
Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out.

---
pseudocode:

ingredients:
cup, boiling water, instant coffee == True

prefer to add:
milk and/or sugar

1. put water into kettle
2. wait until True == water is boiled in kettle
3. put boiled water in kettle into cup
4. put instant coffee into cup
5. choose milk or/and sugar
6. if milk is true then put milk into cup of hot coffee
7. else if sugar is true then put sugar into cup of hot coffee
8. else if sugar and milk is true then put it both
9. else put nothing into cup of hot coffee
10. return coffee


#### Algorithmic complexity (Big-O notation)

time and space.

**Big O notation**

1. constant time (0 iterations)
2. linear time - growth time depending on size inputs (100 elements = 100 iterations)
3. logarithmic time - using binary search (dividing half of range and check half if in 100 = 50, 25, 13, 6, 3, 2, 1)
4. quadratic time - nested loops range(x = 10, y = 10) when x make 1 iteration then y make 10 iterations (x:10 * y:10 = xy:100, xy:10^10)
5. exponential time - using recursion for Fibonacci (calling a function inside function itself )

---
constant time - O(1)
```python
drinks = {1: "coffee", 2: "tea", 3: "juice"}  
constant_time = drinks[2]
```
```python
def access_element(arr, index):  
	return arr[index]
```

---
linear time - O(n)
```python
for x in range(10000):  
linear_time = x  
  
def find_num(num):  
	iter_count = 0  
	for x in range(100):  
		if x == num:  
			return f"total iterations: {iter_count}, to find: {x}"  
		iter_count += 1  
  
linear_time = find_num(97)
```
```python
def linear_search(arr, target):  
	iter_count = 0  
	for item in arr:  
		if item == target:  
			return True, iter_count  
		iter_count += 1  
	  
	return False, iter_count
```

---
logarithmic time - O(log n)
```python
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
```
```python
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
```

---
quadratic time - O(n^2)
```python
for x in range(10):  
	for y in range(10):  
		quadratic_time = x, y
```
```python
def bubble_sort(arr):  
	n = len(arr)  
	for i in range(n):  
		for j in range(0, n - i - 1):  
			if arr[j] > arr[j + 1]:  
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---
exponential time - O(2^n) 
```python
def fibonacci(n):  
	if n <= 1:  
		return n  
	return fibonacci(n - 1) + fibonacci(n - 2)  
  
  
exponential_time = fibonacci(24)  
```

---
##### A Quick Breakdown

1. **Fastest**:
    - **O(1) - Constant Time**: Lightning-fast! The algorithm's speed doesn't depend on how much data you have. It's like finding your favorite book on a perfectly organized bookshelf – it takes the same amount of time, whether you have 10 books or 1,000 books.
2. **Pretty Fast**:
    - **O(log n) - Logarithmic Time**: Still quite speedy! It grows slowly as you add more data. Think of it as finding a name in a phone book by repeatedly splitting it in half – it gets faster even if the phone book gets bigger.
3. **Moderate**:
    - **O(n) - Linear Time**: Respectable speed! If you have twice as much data, it takes about twice as long. It's like looking through a list of names one by one to find a match.
4. **Slower**:
    - **O(n log n) - Linearithmic Time**: It's faster than quadratic but slower than linear. Comparable to sorting a deck of cards quickly using smart techniques.
5. **Slower Still**:
    - **O(n^2) - Quadratic Time**: Getting slower as you add data. Like checking every combination of items on a list against each other – not great for large lists.
6. **Quite Slow**:    
    - **O(2^n) - Exponential Time**: Now we're talking about slow! It grows rapidly as you add data. Imagine a puzzle where you have to try every possible combination – it's really slow even for small puzzles.
7. **Incredibly Slow**:
    - **O(n!) - Factorial Time**: The slowest of all! It's like solving a complex puzzle where the number of possible arrangements explodes as you add more pieces. Practically unusable for large problems.

---
**Why Big O Notation Matters**

Big O notation is crucial for several reasons:
1. **Algorithm Comparison**: It allows us to objectively compare different algorithms and choose the most efficient one for a specific task.
2. **Performance Optimization**: Understanding Big O helps identify bottlenecks in code and optimize algorithms for better performance.
3. **Scalability**: Efficient algorithms are vital as applications and data sizes grow.
4. **Resource Management**: In resource-constrained environments, like embedded systems, choosing efficient algorithms is essential.
5. **Coding Interviews**: Big O notation is often tested in technical interviews and coding challenges, demonstrating your ability to analyze and optimize algorithms.

---
**Analyzing Code with Big O Notation**

To analyze code using Big O notation, follow these steps:
1. **Identify the Input Size**: Determine what "n" represents in your code, often related to the size of the input data.
2. **Identify Loops and Iterations**: Look for loops in your code, as they often determine the primary factors affecting time complexity.
3. **Count Operations Inside Loops**: Count the number of operations inside each loop that depend on the input size "n."
4. **Combine Complexity**: If you have nested loops, multiply their complexities to determine the overall time complexity.
5. **Choose the Dominant Term**: In cases of combined complexity, focus on the term with the highest growth rate, as it will dominate the overall time complexity.
6. **Simplify**: Simplify the expression as much as possible by removing constant factors.

### Functional Programming

![[Pasted image 20231202175109.png|400]]

```python
>>> coffees = ["Espresso", "Latte", "Cappuccino", "Americano", "Decaf"]
>>> def reverse(str):
...     return str[::-1]
...
>>> reversed_coffees = map(reverse, coffees)
>>> [x for x in reversed_coffees]
['osserpsE', 'ettaL', 'oniccuppaC', 'onaciremA', 'faceD']
```

---
#### Pure Functions
Pure Functions - no effect beyond its own scope.

There isn't pure function: 
```python
>>> global_list = [1, 2, 3]
>>> def add_to(item):
...     return global_list.append(item)
...
>>> add_to(4)
>>> global_list
[1, 2, 3, 4]
```

---
Altering Functions - how to alter a normal func to a pure func
self is pure func:
```python
>>> global_list = [1, 2, 3, 4]
>>> def add_to_list(lst, item):
...     nl = lst.copy()
...     nl.append(item)
...     return nl
...
>>> add_to_list(global_list, 5)
[1, 2, 3, 4, 5]
>>> add_to_list(global_list, 6)
[1, 2, 3, 4, 6]
>>> global_list
[1, 2, 3, 4]
>>> nl
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nl' is not defined
```

---
#### Recursion
Recursion Algorithm - function that calls itself (repeating) like for loop

```python
def find_factorial_recursive(n):  
	if n == 1:  
		return 1  
	else:  
		return n * find_factorial_recursive(n - 1)  
  
  
print(find_factorial_recursive(5))
```
---
Explanation of recursion

![[Pasted image 20231202185957.png|400]]
```python
>>> n = 5
>>> iter_n = n * (n - 1)
>>> iter_n
20
>>> iter_n = iter_n * (n - 2)
>>> iter_n
60
>>> iter_n = iter_n * (n - 3)
>>> iter_n
120
>>> iter_n = iter_n * (n - 4)
>>> iter_n
120
>>> iter_n = iter_n * (n - 5)
>>> iter_n
0

---
>>> if n == 1 return 1
n = 120
```

---
Advantages:
- neat code - Recursive code can make your code neater and less bulky.
- sub-problems - Complex tasks can be broken down into easier-to-read sub-problems .
- easy sequences - Generation of sequences can be easier to understand than nested loops.
Disadvantages:
- hard to follow
- memory
- debugging

---
Tower of Hanoi

```python
# Recursive function for Tower of Hanoi  
def hanoi(disks, source, helper, destination):  
# Base Condition  
if disks == 1:  
print("Disk {} moves from tower {} to tower {}".format(disks, source, destination))  
return 1  
  
# Recursive calls in which function calls itself  
hanoi(disks - 1, source, destination, helper)  
print("Disk {} moves from tower {} to tower {}".format(disks, source, destination))  
hanoi(disks - 1, helper, destination, source)  
  
  
disks = int(input("Number of disks to be displaced: "))  
  
hanoi(disks, "A:source", "B:helper", "C:destination")
```

---
#### Reverse String

```python
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


# using recursion
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
  
rev_fu = ''.join([x for x in reversed(input())])  
rev_fu2 = ''.join((list(reversed("123"))))  
print(rev_fu)
```

---
#### Map and Filter built-in-function

```python
menu = ["espresso", "mocha", "cappuccino", "cortado", "americano"]  
  
  
def find_coffee(coffee):  
	if coffee[0] == 'c':  
		return coffee  
  
  
map_coffee = map(find_coffee, menu)  
print(map_coffee)  
for x in map_coffee:  
	print(x)  
  
  
filter_coffee = filter(find_coffee, menu)  
print(filter_coffee)  
for x in filter_coffee:  
	print(x)
```

---
#### Comprehensions in python
Comprehensions in Python are a way to create a new sequence from an already existing sequence.
- list comprehension
- dictionary comprehension  
- set comprehension 
- generator comprehension

---
##### list comprehension 
`[<expression> for x in <sequence> if <condition>]`

```python
# list comprehension  
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  
  
# Ex1: List comprehension: updating the same list  
data = [x + 3 for x in data]  
print("Updating the list: ", data)  
  
# Ex2: List comprehension: creating a different list with updated values  
new_data = [x * 2 for x in data]  
print("Creating new list: ", new_data)  
  
# Ex3: With an if-condition: Multiples of four:  
fourx = [x for x in new_data if x % 4 == 0]  
print("Divisible by four", fourx)  
  
# Ex4: Alternatively, we can update the list with the if condition as well  
fourxsub = [x - 1 for x in new_data if x % 4 == 0]  
print("Divisible by four minus one: ", fourxsub)  
  
# Ex5: Using range function:  
nines = [x for x in range(100) if x % 9 == 0]  
print("Nines: ", nines)  
  
  
# Test 1  
print("\nTest1")  
odd = [x for x in range(50) if x % 2 == 1]  
even = [x for x in data if x % 2 == 0]  
even_range = [x for x in range(1, 50) if x % 2 == 0]  
print("odd numbers in range(50): ", odd)  
print("even numbers in range(50): ", even_range)  
print("even numbers in data: ", even)  
  
  
# Test 2  
print("\nTest2")  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
new_list1 = [x for x in fruits if "a" in x]  
print("if a in fruits: ", new_list1)  
new_list2 = [x.upper() for x in fruits]  
print("set fruits uppercase: ", new_list2)  
new_list3 = [x for x in fruits if x != "apple"]  
print("only accept items that are not apple:", new_list3)  
new_list4 = [x if x != "banana" else "orange" for x in fruits]  
print("return orange instead of banana: ", new_list4)  
  
  
# Test 3  
print("\nTest3")  
z = ["alpha", "bravo", "charlie"]  
new_z = [i[0] * 2 for i in z]  
print(new_z)  
new_z = [i[::-1] for i in z]  
print(new_z)  


# Comparison  
# List comprehension:  
data = [x + 3 for x in data]  
  
# Regular for loop:  
for x in range(len(data)):  
	data[x] = data[x] + 3
```
```output
Updating the list:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]
Creating new list:  [10, 12, 16, 20, 28, 32, 40, 44, 52, 64, 68]
Divisible by four [12, 16, 20, 28, 32, 40, 44, 52, 64, 68]
Divisible by four minus one:  [11, 15, 19, 27, 31, 39, 43, 51, 63, 67]
Nines:  [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
```

---
##### dictionary comprehension
`dict = { key:value for key, value in <sequence> if <condition> }`

```python
# dictionary comprehension  
# Using range() function and no input list  
usingrange = {x: x * 2 for x in range(12)}  
print("Using range(): ", usingrange)  
  
# Lists  
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]  
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  
  
# Using one input list  
numdict = {x: x ** 2 for x in number}  
print("Using one input list to create dict: ", numdict)  
  
# Using two input lists  
# new_dict ={key:value for (key, value) in zip(list1, list2)}  
months_dict = {key: value for key, value in zip(number, months)}  
print("Using two lists: ", months_dict)  
  
  
# Test  
start_key_1index = {x + 1: (x + 1) ** 2 for x in range(12)}  
print("start key index 1 instead 0", start_key_1index)
```
```output
Using range():  {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}
Using one input list to create dict:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
Using two lists:  {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
```

---
##### set comprehension
- works like list comprehension

```python
# set comprehension  
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}  
set_b = {x for x in range(10, 20) if x not in [15, 17, 19]}  
print(set_a)  
print(set_b)  
# self is: | concatenation operator for sets  
set_c = set_a | set_b  
print(set_c)  
  
# Test  
print("\nTest")  
set1 = {x for x in range(1, 20, 2)}  
print(set1)  
set2 = {x for x in range(1, 20) if x % 2 == 0}  
print(set2)  
  
# Test 2  
print("\nTest2")  
data = [2, 3, 3, 5, 7, 7, 8, 11, 11, 12, 13, 17, 19, 23, 29, 29, 29, 29, 31]  
set3 = {x for x in data if x not in range(1, 10)}  
  
print(data)  
print(set3)  
print("len of data", len(data))  
print("len of set3", len(set3))
```
```output
{10, 11, 13, 15, 17, 18, 19}
```

---
##### generator comprehension
- works like list comprehension

```python
# generator comprehension  
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  
gen_obj = (x for x in data)  
  
print(gen_obj)  
print(type(gen_obj))  
for items in gen_obj:  
	print(items, end=" ")
```
```output
<generator object <genexpr> at 0x102a87d60> 
<class 'generator'> 
2 3 5 7 11 13 17 19 23 29 31 
```


#### Map vs Comprehension
```python
# difference between map() function and list comprehensions  
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  
  
# Map  
print("Map")  
  
  
def square(num):  
return num + 3  
  
  
newdata = map(square, data)  
print(newdata)  
  
map_obj = newdata  
print(map_obj)  
print(type(map_obj))  
for items in map_obj:  
print(items, end=" ")  
  
# List comprehension  
print("\n\nList comprehension")  
newdata = [x + 3 for x in data]  
print(newdata)
```

#### lab 1 - Mapping key-values to Dictionary data structures

```python
# Lab 1 - Mapping key-values to Dictionary data structures  
# Input data: List of dictionaries  
employee_list = [  
{"id": 12345, "name": "John", "department": "Kitchen"},  
{"id": 12456, "name": "Paul", "department": "House Floor"},  
{"id": 12478, "name": "Sarah", "department": "Management"},  
{"id": 12434, "name": "Lisa", "department": "Cold Storage"},  
{"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},  
{"id": 12419, "name": "Gill", "department": "Cashier"}  
]  
  
  
# Function to be passed to the map() function. Do not change self.  
def mod(employee_list):  
temp = employee_list['name'] + "_" + employee_list["department"]  
return temp  
  
  
def to_mod_list(employee_list):  
	""" Modifies the employee list of dictionaries into list of 
	Args:  
	employee_list: list of employee objects  
	Returns:  
	list - A list of strings consisting of name + department.  
	"""  
	map_mod_concat = map(mod, employee_list)  
	map_obj = [x for x in map_mod_concat]  
	return map_obj  
  
  
def generate_usernames(mod_list):  
	""" Generates a list of usernames  
	Args:  
	mod_list: list of employee-department strings  
	Returns:  
	list - A list of usernames consisting of name + department delimited by underscores.  
	"""  
	new_list = [x.replace(" ", "_") for x in mod_list]  
	return new_list  
  
  
def map_id_to_initial(employee_list):  
	""" Maps employee id to first initial  
	Args:  
	employee_list: list of employee objects  
	Returns:  
	dict - A dictionary mapping an employee's id (value) to their first initial (key).  
	"""  
	id_list_first_index = [str(x["id"])[0] for x in employee_list]  
	id_list_reversed_first_index = [str(x["id"])[::-1][0] for x in employee_list]  
	id_list_first_each_2_elements = [str(x["id"])[0::2] for x in employee_list]  
	
	name_list_first_letter = [x["name"][0] for x in employee_list]  
	id_list = [x["id"] for x in employee_list]  
	  
	new_dict = {key: value for key, value in zip(name_list_first_letter, id_list)}  
	  
	return new_dict  
  
  
def main():  
	mod_emp_list = to_mod_list(employee_list)  
	print("Modified employee list: " + str(mod_emp_list) + "\n")  
	  
	print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")  
	  
	print(f"Initials and ids: {map_id_to_initial(employee_list)}")  
  
  
if __name__ == "__main__":  
	main()
```

### Object Oriented Programming
OOP - one of python programming paradigm that defined as a style of writing program and translate real-world problems, principles, concepts into code.
- easy to understand
- reusable move between project (dry)
- abstraction

- classes - logical code block that contains attributes and behavior or logic 
	- defined by `class`
	- attribute can be variable
	- behavior can be function
	- may have: constructor, 
	- class provides a blueprint for creating an object
- objects - instances or blueprint of class, you can create any of them
- methods - are functions defined inside a class that determine behavior or logic of object instance

---
three object blueprint of one class with variables and methods
![[Pasted image 20231204023721.png|500]]

calling class copies as new variable to create class blueprint new object (instantiation or creating an instance of class)
![[Pasted image 20231204023911.png|500]]

creating function inside class called method (there is no difference between) and calling as class employee object instance  
![[Pasted image 20231204024314.png|500]]

---
Concepts of OOP
- Inheritance
- Polymorphism 
- Encapsulation
- Method overloading
- method overriding
- constructors 

---
- Inheritance - creating a new class which is derivative of an existing one. 
	- original is called parent class or superclass
	- any derivatives are referred to as subclass or child class.
- Polymorphism - means having many forms, ability if a function to change its behavior or logic when called by different object or single function can act differently depending on the object or the causes.
- Encapsulation - can bind methods and variable from direct access by wrapping them within a single unit of scope such as a class, or limits access to method and variables by encasing them in a single unit of scope, and these helps prevent unwanted modifications, reducing occurrence of errors and outputs. and can defined by `__` as private, `_` as protected
- Abstraction - refers to ability to hide implementation details to make data saver and more secure, python does not support abstraction directly and uses inheritance to achieve it and ABC module.


polymorphism example: built-in class, "+" operators works differently depending on type of data (modifying functionality called polymorphism):
![[Pasted image 20231204025210.png|500]]


---
**class:**
- attribute (variable declared in class)
- method (just function in class and makes some logic, behaviors)
- everything in python is object
- creating class creates new type of object that create instances 

#### Term definition

- object
- instance
- initialization
- abstract
- 

#### Inheritance

#### Encapsulation

#### Polymorphism

#### Abstract class and method

#### Operator Overloading

#### Constructor

#### MRO - Method Resolution Order (type of inheritance and object)
type of inheritance(like tree, DOM object in js, html, sql entity relationships):
- single inheritance
- multiple inheritance
- multi level inheritance
- hierarchical inheritance
- hybrid inheritance

---
![[Pasted image 20231210050124.png|500]]

---
algorithms to built MRO:
- Depth-First search algorithm (DFS)
- C3 Linearization algorithms (rules:)
	- adheres to Monotonicity
	- fallows inheritance graph
	- visits super class after local classes
![[Pasted image 20231210050513.png|500]]


---
Methods to find MRO:
- MRO attribute `mro()`
- Help function `help()`

#### Magic Methods or Dunder methods

#### Built-in function for class and objects

- `assert`
- `issubclass()` and `isinstance()` 
- `super()`
- `copy` and `deepcopy()`



### SRC

**Procedural programming, Algorithms, Big O notation**

- how to write an algorithm
- algorithm chart
- pseudocode
- big O notation

- procedural programming
- dynamic programming
- divide and conquer algorithm
- greedy algorithm
- recursive algorithm
- binary search algorithm
- bubble sort algorithm
- a* algorithm

- [Programming styles in Python](https://newrelic.com/blog/nerd-life/python-programming-styles)
- [Different types of algorithms used in Python](https://www.thetechplatform.com/post/different-types-of-algorithms-in-data-structure) 
- [Introduction to Big-O notation](https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7)

---
**Functional programming**

- traditional and pure functional programming
- Functional programming
- Declarative programming
- Imperative programming

- [Python map() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_map.asp)
- [Python filter() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_filter.asp)
- [Python String join() Method (w3schools.com)](https://www.w3schools.com/python/ref_string_join.asp)
- [Python - List Comprehension (w3schools.com)](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [Python zip() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_zip.asp)
- [Python String replace() Method (w3schools.com)](https://www.w3schools.com/python/ref_string_replace.asp)

- comprehension in python
- python built-in method object
- [Python printing "<built-in method ... object" instead of list - Stack Overflow](https://stackoverflow.com/questions/39988898/python-printing-built-in-method-object-instead-of-list)
- concatenation operator for sets python

- [Python Map, reduce and list comprehension](https://www.knowledgehut.com/blog/programming/python-map-list-comprehension)
- [Recursion in Python](https://realpython.com/python-recursion/)
- [Functional Programming in Python](https://stackabuse.com/functional-programming-in-python/)

---
**Object Oriented Programming**

- [OOP Principles](https://www.geeksforgeeks.org/python-oops-concepts/)
- [In-depth understanding of MRO](https://www.python.org/download/releases/2.3/mro/)
- [OOP Principles/ Classes and objects](https://realpython.com/python3-object-oriented-programming/)

- inheritance
- encapsulation
- polymorphism
- abstract class
- operators overloading
- MRO - Method Resolution Order

- class
- object
- attribute
- method vs function
- constructor
- instance

- assert in python
- issubclass and isinstance python
- super func initialization python
- abs, abstractmethod and abc library
- @property decorator, wrapper
- magic methods python
- init vs new in class
- python method resolution order

- spaghetti code in oop
- metaclass in python

- how to define inheritance, abstract class
- naming of class

- [CS50P - Lecture 8 - Object-Oriented Programming (youtube.com)](https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14)

- [Объектно-ориентированное программирование в Python - CodeChick](https://codechick.io/tutorials/python/python-what-is-oop)
- [Python | Классы и объекты (metanit.com)](https://metanit.com/python/tutorial/7.1.php)
- [Python Classes (w3schools.com)](https://www.w3schools.com/python/python_classes.asp)
- [C# OOP (Object-Oriented Programming) (w3schools.com)](https://www.w3schools.com/cs/cs_oop.php)

---
**Others** 

- palindrome
- fibonacci
- logarithm
- factorial
- tower of hanoi

- best practices in programming
- decomposition in computer science
- refactoring
- Rubber duck debugging method
- spaghetti code