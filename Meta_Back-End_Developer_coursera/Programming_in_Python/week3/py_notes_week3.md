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
Introduction: In this exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product. 
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
this is pure func:
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

- 
---











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

- palindrome
- fibonacci
- logarithm

- best practices in programming
- decomposition in computer science
- refactoring

- [Programming styles in Python](https://newrelic.com/blog/nerd-life/python-programming-styles)
- [Different types of algorithms used in Python](https://www.thetechplatform.com/post/different-types-of-algorithms-in-data-structure) 
- [Introduction to Big-O notation](https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7)

---

