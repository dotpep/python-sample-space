### Function
Function (or method) in python
```python
bill = 175.00  
tax_rate = 15  
total_tax = (bill * tax_rate) / 100.00  
  
print("Total tax: ", total_tax)
```
```python
def calculate_tax(bill, tax_rate):  
return round((bill * tax_rate) / 100.00, 2) # 42.0461 to 42.05 (show 2 decimal numbers and round it)
  
print("Total tax: (with func)", calculate_tax(175.00, 15))  
print("Total tax: (with func 2)", calculate_tax(247.33, 17))  

tax_case3 = calculate_tax(2200.3566, 100)  
print("Total tax: (with func 3)", tax_case3)
```


---
#### Variable scope (func)
Variable scope
- Built-en Scope
- Global Scope
- Enclosing Scope
- Local Scope
![[Pasted image 20231121195503.png|300]]
![[Pasted image 20231121195806.png|500]]

```python
# global scope  
my_global = 10  
  
def func1():  
	enclosed_v = 8  
	# my_global = 1  
  
	def func2():  
		local_v = 5  
		# my_global = 1  
		print("Access to Global", my_global)  
		print("Access to Enclosed", enclosed_v)  

	func2()  
  
  
func1()  
# print("Cant access to Local", local_v)  
# print("Cant access to Enclosed", enclosed_v)  
# func2()
```
```python
x = 300  
def myfunc():  
	x = 200  
	print("Local scope x Variable in myfunc()", x)  
  
myfunc()  
print("Global scope variable x", x)

>>> Local scope x Variable in myfunc() 200
>>> Global scope variable x 300
```
```python
def myfunc():  
	global x  
	x = 300  
  
myfunc()  
print("local x but with (global)", x)

>>> local x but with (global) 300
```
```python
x = 300  
  
def myfunc():  
	global x  
	x = 200  
  
myfunc()  
  
print("change global scope val with (global keyword) inside func (local scope) ", x)

>>> change global scope val with (global keyword) inside func (local scope)  200
```


### Data Structure
Data structure are designed for save and work with more complex information, such as collection of data like list of people and etc.

![[Pasted image 20231121203228.png]]

Built-in data structure - is ==non-primitive== data structure, they are classed as objects. (defined for use in python as a piece of python syntax)
- list
- dictionary
- tuple
- set

User-Defined data structure - is data structure can all be created by the user.

- Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more performant.

---
Data Structure can be:
- Mutable - refers to data inside the data structure that can be modified. (list is mutable)
- Immutable - refers to data inside data structure will not allow modification once the data has been set. (tuple is immutable)

#### List
sequence of one or more data and dynamic array.

```python
>>> list = [1, 2, 3, 4, 5]
>>> list2  = ["A", "B", "C"]
>>> list3 = ["Hello", 1, True, 40.22]
>>>
>>> list[2]
3
>>> list2[0]
'A'
>>> list3[3]
40.22
>>> list4 = [1, [2, 3, 4], 5, 6]
>>> list4[1]
[2, 3, 4]
>>> list4[1][0]
2
>>> list
[1, 2, 3, 4, 5]
>>> print(*list)
1 2 3 4 5
>>> print(list, sep=" ")
[1, 2, 3, 4, 5]


---
>>> # insert works with (index, add value)
>>> list.insert(len(list), 6)
>>> print(list)
[1, 2, 3, 4, 5, 6]
>>> list
[1, 2, 3, 4, 5, 6]
>>> list.insert(0, 0.1)
>>> list
[0.1, 1, 2, 3, 4, 5, 6]
>>> list.insert(1, 1.5)
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6]
>>> list.insert(len(list), 7)
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6, 7]


---
>>> # append one value into list
>>> list.append(7.2)
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6, 7, 7.2]
>>> list.append(8)
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6, 7, 7.2, 8]
>>>


---
>>> # extend uses when you needed to add more one values of data
>>> list.append([8, 4])
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6, 7, 7.2, 8, [8, 4]]
>>> list.extend([9, 10, 11])
>>> list
[0.1, 1.5, 1, 2, 3, 4, 5, 6, 7, 7.2, 8, [8, 4], 9, 10, 11]


---
>>> # use pop and del for delete elements inside list working with (index)
>>> list.pop(0)
0.1
>>> list
[1.5, 1, 2, 3, 4, 5, 6, 7, 7.2, 8, [8, 4], 9, 10, 11]
>>> list.pop(len(list) - 1)
11
>>>
>>> del list[0]
>>> list
[1, 2, 3, 4, 5, 6, 7, 7.2, 8, [8, 4], 9, 10]
>>> del list[7]
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, [8, 4], 9, 10]
```

##### More List

```python
>>> thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
>>>
>>> thislist[2:5]
['cherry', 'orange', 'kiwi']
>>> thislist[:4]
['apple', 'banana', 'cherry', 'orange']
>>> thislist[2:]
['cherry', 'orange', 'kiwi', 'melon', 'mango']
>>> thislist[-1]
'mango'
>>> thislist[-4:-1]
['orange', 'kiwi', 'melon']
>>>
>>> thislist[1] = "blackcurrant"
>>> thislist
['apple', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
>>> thislist[1:3] = ["apple", "watermelon"]
>>> thislist
['apple', 'apple', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
>>> thislist[1:2] = ["cherry", "blackcurrant"]
>>> thislist
['apple', 'cherry', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
>>> thislist[1:3] = ["strawberry"]
>>> thislist
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
>>>
>>> tropical = ["mango", "pineapple", "papaya"]
>>> thislist.extend(tropical)
>>> thislist
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'mango', 'pineapple', 'papaya']
>>> thistuple = ("kiwi", "orange")
>>> thislist.extend(thistuple)
>>> thislist
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']
>>> thislist.remove("mango")
>>> thislist
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']
>>>
>>> tropical
['mango', 'pineapple', 'papaya']
>>> tropical.clear()
>>> tropical
[]
```

---

```python
>>> dir(fruits)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(fruits.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.
```

---
Sort list
```python
>>> thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
>>> thislist.sort()
>>> thislist
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
>>> thislist = [100, 50, 65, 82, 23]
>>> thislist.sort()
>>> thislist
[23, 50, 65, 82, 100]
>>> thislist = [100, 50, 65, 82, 23]
>>> thislist.sort(reverse = True)
>>> thislist
[100, 82, 65, 50, 23]
>>> # sort in descending order (by default is ascending and alphanumerically)
>>>
>>> def myfunc(n):
...   return abs(n - 50)
...
>>> thislist = [100, 50, 65, 82, 23]
>>> thislist.sort(key = myfunc)
>>> thislist
[50, 65, 23, 82, 100]
>>>
>>> # Case insensitive sort
>>> thislist = ["banana", "Orange", "Kiwi", "cherry"]
>>> thislist.sort()
>>> thislist
['Kiwi', 'Orange', 'banana', 'cherry']
>>> thislist.sort(key = str.lower)
>>> thislist
['banana', 'cherry', 'Kiwi', 'Orange']
>>> # reverse order (by list start with -1 index)
>>> thislist.reverse()
>>> thislist
['Orange', 'Kiwi', 'cherry', 'banana']
```

---

```python
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = thislist.copy()
>>> mylist
['apple', 'banana', 'cherry']

---
>>> mylist2 = list(thislist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, [8, 4], 9, 10]
>>> del list

---
>>> mylist2 = list(thislist)
>>> mylist2
['apple', 'banana', 'cherry']
```

---
Join
```python
>>> list1 = ["a", "b", "c"]
>>> list2 = [1, 2, 3]
>>>
>>> list3 = list1 + list2
>>> list3
['a', 'b', 'c', 1, 2, 3]

---
>>> list1
['a', 'b', 'c']
>>> list1.extend(list2)
>>> list1
['a', 'b', 'c', 1, 2, 3]

---
>>> list1 = ["a", "b", "c"]
>>> list2 = [1, 2, 3]
>>> [list1.append(x) for x in list2]
[None, None, None]
>>> list1
['a', 'b', 'c', 1, 2, 3]
```

#### List Comprehension

```python
>>> thislist = ['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']
>>> [x for x in thislist]
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'melon', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']

---
>>> fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
>>> newlist = [x for x in fruits if "a" in x]
>>> newlist
['apple', 'banana', 'mango']

---
>>> newlist_gen = [x for x in range(10)]
>>> newlist_gen
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> newlist_gen2 = [x for x in range(10) if x < 5]
>>> newlist_gen2
[0, 1, 2, 3, 4]

---
>>> newlist_upper = [x.upper() for x in fruits]
>>> newlist_upper
['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

---
>>> newlist = ['hello' for x in fruits]
>>> newlist
['hello', 'hello', 'hello', 'hello', 'hello']

---
>>> newlist = [x if x != "banana" else "orange" for x in fruits]
>>> newlist
['apple', 'orange', 'cherry', 'kiwi', 'mango']
```

##### Testing

```python
>>> a = [1, 2, 3]
>>> b = a
>>> b
[1, 2, 3]
>>> a
[1, 2, 3]
>>> [a[item] for item in range(len(b))]
[1, 2, 3]
>>> [a[item] + b[item] for item in range(len(b))]
[2, 4, 6]
>>> [a[item] + b[item] for item in range(len(b))]
[2, 4, 6]
>>> ab = [a[item] + b[item] for item in range(len(b))]
>>> ab
[2, 4, 6]
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> ab1 = a + b
>>> ab1
[1, 2, 3, 1, 2, 3]
>>> ab2 = [ab1[item] + ab1[item + 3] for item in range(3)]
>>> ab2
[2, 4, 6]
>>> ab2 + ab1
[2, 4, 6, 1, 2, 3, 1, 2, 3]
>>> ab2 + ab + ab1
[2, 4, 6, 2, 4, 6, 1, 2, 3, 1, 2, 3]
>>> sets_ab = set(ab2 + ab + ab1 + [4])
>>> sets_ab
{1, 2, 3, 4, 6}
>>> sets_ab = set(ab2 + ab + ab1 + [7])
>>> sets_ab
{1, 2, 3, 4, 6, 7}
>>> lists_ab = list(sets_ab)
>>> lists_ab
[1, 2, 3, 4, 6, 7]
>>> abx2 = [lists_ab[item] + lists_ab[item] for item in range(6)]
>>> abx2
[2, 4, 6, 8, 12, 14]
>>> abx2m1 = [lists_ab[item - 1] + lists_ab[item - 1] for item in range(6)]
>>> abx2m1
[14, 2, 4, 6, 8, 12]
>>> abx2m1 = [(lists_ab[item] - 1) + (lists_ab[item] - 1) for item in range(6)]
>>> abx2m1
[0, 2, 4, 6, 10, 12]
>>> abx2m1 = [(lists_ab[item] - 2) + (lists_ab[item] - 2) for item in range(6)]
>>> abx2m1
[-2, 0, 2, 4, 8, 10]
>>> abx2m1 = [(lists_ab[item] - 0.5) + (lists_ab[item] - 0.5) for item in range(6)]
>>> abx2m1
[1.0, 3.0, 5.0, 7.0, 11.0, 13.0]
>>>
>>> abx2m1_int = [int(abx2m1[item]) for item in range(len(abx2m1))]
>>> abx2m1_int
[1, 3, 5, 7, 11, 13]
>>>
>>> ab
[2, 4, 6]
>>> abx2
[2, 4, 6, 8, 12, 14]
>>> abfull = abx2m1_int + abx2
>>> abfull
[1, 3, 5, 7, 11, 13, 2, 4, 6, 8, 12, 14]
>>> sort_abfull = abfull.sort()
>>> sort_abfull
>>> abfull
[1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
>>> abfull.reverse()
>>> abfull
[14, 13, 12, 11, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### Tuple
tuple (кортеж)
can accept any mix of data types, tuple values is immutable.

```python
>>> my_tuple = (1, "string", 4.5, True)
>>> my_tuple[1]
'string'
>>> type(my_tuple[1])
<class 'str'>
>>> type(my_tuple)
<class 'tuple'>
>>> my_tuple = 1, "string", 4.5, True
>>> type(my_tuple)
<class 'tuple'>
>>> my_tuple.count('string')
1
>>> my_tuple.count('1')
0
>>> my_tuple.count(1)
2
>>> my_tuple.count(4.5)
1
>>> my_tuple.count(True)
2
>>> len(my_tuple)
4
>>> my_tuple.index(4.5)
2
>>> my_tuple[2]
4.5
>>> [x for x in my_tuple]
[1, 'string', 4.5, True]
>>> for x in my_tuple:
...     print(x)
...
1
string
4.5
True
>>> my_tuple[0] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

other
```python
>>> thistuple = ("apple", "banana", "cherry")
>>> if "apple" in thistuple:
...     print("Yes, 'apple' is in the tuple")
...
Yes, 'apple' is in the tuple
>>> thislist = list(thistuple)
>>> thislist[0] = "kiwi"
>>> thistuple = tuple(thislist)
>>> thistuple
('kiwi', 'banana', 'cherry')
>>> thistuple[0] = "apple"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> secondtuple = ("orange")
>>> thistuple += secondtuple
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "str") to tuple
>>> secondtuple = ("orange", )
>>> thistuple += secondtuple
>>> thistuple
('kiwi', 'banana', 'cherry', 'orange')
>>>
>>>
>>> fruits = thistuple
>>> fruits
('kiwi', 'banana', 'cherry', 'orange')
>>>
>>> (green, yellow, red, orange) = fruits
>>> green
'kiwi'
>>> yellow
'banana'
>>> red
'cherry'
>>> orange
'orange'
>>> del orange
>>> fruits_list = list(fruits)
>>> del fruits_list[3]
>>> fruits = tuple(fruits_list)
>>> del fruits_list
>>> fruits
('kiwi', 'banana', 'cherry')
>>> fruits_red = ("strawberry", "raspberry")
>>> fruits_list = list(fruits)
>>> fruits_list.extend(fruits_red)
>>> fruits_list
['kiwi', 'banana', 'cherry', 'strawberry', 'raspberry']
>>> fruits = tuple(fruits_list)
>>> fruits
('kiwi', 'banana', 'cherry', 'strawberry', 'raspberry')
>>> (green, yellow, *red) = fruits
>>> red
['cherry', 'strawberry', 'raspberry']
>>> type(red)
<class 'list'>
>>>
>>> i = 0
>>> while i < len(fruits):
...     print(fruits[i])
...     i += 1
...
kiwi
banana
cherry
strawberry
raspberry
>>>
>>>
>>> tuple1 = ("a", "b" , "c")
>>> tuple2 = (1, 2, 3)
>>>
>>> tuple3 = tuple1 + tuple2
>>> tuple3
('a', 'b', 'c', 1, 2, 3)
>>> mytuple = fruits * 2
>>> mytuple
('kiwi', 'banana', 'cherry', 'strawberry', 'raspberry', 'kiwi', 'banana', 'cherry', 'strawberry', 'raspberry')
```


#### Sets
Set items are unordered, unchangeable, and do not allow duplicate values.
- A set is **unordered**, items don’t have a defined order and cannot be referred to by index or key.
- Sets are **unchangeable** (immutable), but you can add new items and remove existing ones.
- **Duplicates are not allowed** in sets, each item must be unique.

- set is not a sequence

```python
>>> set_a = {1, 2, 3, 4, 5}
>>> set_a
{1, 2, 3, 4, 5}
>>> type(set_a)
<class 'set'>
>>> set_a.add(6)
>>> set_a
{1, 2, 3, 4, 5, 6}
>>> set_a.remove(2)
>>> set_a
{1, 3, 4, 5, 6}
>>> set_a.discard(3)
>>> set_a
{1, 4, 5, 6}
>>> set_b = {1, 2, 3, 4, 5, 6, 7, 8}
>>> set_c = set_a.union(set_b)
>>> set_c
{1, 2, 3, 4, 5, 6, 7, 8}
>>>
>>> set_a | set_b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> print(set_a | set_b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set_a.intersection(set_b)
{1, 4, 5, 6}
>>> set_a & set_b
{1, 4, 5, 6}
>>> print(set_a & set_b)
{1, 4, 5, 6}
>>> set_a and set_b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set_a or set_b
{1, 4, 5, 6}
>>> set_a in set_b
False
>>> set_a and set_b in set_a and set_b
False
>>> set_a or set_b in set_a or set_b
{1, 4, 5, 6}
>>> set_a.difference(set_b)
set()
>>> print(set_a.difference(set_b))
set()
>>> set_a - set_b
set()
>>> set_a
{1, 4, 5, 6}
>>> set_x = set_a * 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> set_x = set_a - set_b
>>> set_x
set()
>>>
>>>
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set3 = set1 - set2
>>> set3
{1, 2, 3}
>>>
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set3 = set1 ^ set2
>>> set3
{1, 2, 3, 6, 7, 8}
>>>
>>> set1.symmetric_difference(set2)
{1, 2, 3, 6, 7, 8}
>>> set1 ^ set2
{1, 2, 3, 6, 7, 8}
```

---
other

```python
>>> thisset = {"apple", "banana", "cherry"}
>>> type(thisset)
<class 'set'>
>>>
>>> thisset = {"apple", "banana", "cherry", "apple"}
>>> thisset
{'banana', 'apple', 'cherry'}
>>>
>>> # True and 1 is considered the same value (treated as duplicates)
>>> thisset = {"apple", "banana", "cherry", True, 1, 2}
>>> thisset
{True, 2, 'cherry', 'banana', 'apple'}
>>> # False and 0 are considered the same value
>>> thisset = {"apple", "banana", "cherry", False, True, 0}
>>> thiset
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thiset' is not defined. Did you mean: 'thisset'?
>>> thisset
{False, True, 'cherry', 'banana', 'apple'}
>>>
>>> len(thisset)
5
>>> set1 = {"apple", "banana", "cherry"}
>>> set2 = {1, 5, 7, 9, 3}
>>> set3 = {True, False, False}
>>> set1 = {"abc", 34, True, 40, "male"}
>>> set1
{True, 34, 'abc', 40, 'male'}
>>>
>>> thistuple = (1, 0, 2, True, False, 4.5, "apple")
>>> thistuple = thistuple * 3
>>> thistuple
(1, 0, 2, True, False, 4.5, 'apple', 1, 0, 2, True, False, 4.5, 'apple', 1, 0, 2, True, False, 4.5, 'apple')
>>> thisset = set(thistuple)
>>> thisset
{0, 1, 2, 4.5, 'apple'}
>>>
>>> for x in thisset:
...     print(x)
...
0
1
2
4.5
apple
>>> print("apple" in thisset)
True
>>>
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.add("orange")
>>> thisset
{'banana', 'apple', 'cherry', 'orange'}
>>> tropical = {"pineapple", "mango", "papaya"}
>>> thisset.update(tropical)
>>> thisset
{'pineapple', 'banana', 'cherry', 'papaya', 'mango', 'apple', 'orange'}
>>> mylist = ["kiwi", "orange"]
>>> thisset.update(mylist)
>>> thislist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thislist' is not defined. Did you mean: 'thisset'?
>>> thisset
{'pineapple', 'banana', 'cherry', 'papaya', 'kiwi', 'mango', 'apple', 'orange'}
>>>
>>> thisset.remove("banana")
>>> thisset
{'pineapple', 'cherry', 'papaya', 'kiwi', 'mango', 'apple', 'orange'}
>>>
>>> # If the item to remove does not exist, remove() will raise an error.
>>> # If the item to remove does not exist, discard() will NOT raise an error.
>>> thisset.discard("orange")
>>> "orange" in thisset
False
>>>
>>> x = thisset.pop()
>>> x
'pineapple'
>>> thisset
{'cherry', 'papaya', 'kiwi', 'mango', 'apple'}
>>> type(x)
<class 'str'>
>>> thisset.clear()
>>> thisset
set()
>>> del thisset
>>> thisset
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thisset' is not defined
>>>
>>>
>>> set1 = {"a", "b" , "c"}
>>> set2 = {1, 2, 3}
>>> set3 = set1.union(set2)
>>> set3
{'b', 1, 2, 3, 'a', 'c'}
>>> set1.update(set2)
>>> set1
{'b', 1, 2, 3, 'a', 'c'}
>>>
>>> # Keep ONLY the Duplicates
>>> # intersection_update() method will keep only the items that are present in both sets.
>>> x = {"apple", "banana", "cherry"}
>>> y = {"google", "microsoft", "apple"}
>>> x.intersection_update(y)
>>> x
{'apple'}
>>>
>>>
>>> x = {"apple", "banana", "cherry"}
>>> y = {"google", "microsoft", "apple"}
>>> z = x.intersection(y)
>>> z
{'apple'}
>>> x
{'banana', 'apple', 'cherry'}
>>>
>>>
>>> # Keep All, But NOT the Duplicates
>>> # symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
>>> x = {"apple", "banana", "cherry"}
>>> y = {"google", "microsoft", "apple"}
>>> x.symmetric_difference_update(y)
>>> x
{'microsoft', 'cherry', 'google', 'banana'}
>>> y
{'microsoft', 'google', 'apple'}
>>>
>>>
>>> x = {"apple", "banana", "cherry"}
>>> y = {"google", "microsoft", "apple"}
>>> z = x.symmetric_difference(y)
>>> z
{'microsoft', 'cherry', 'google', 'banana'}
>>> y
{'microsoft', 'google', 'apple'}
>>> x
{'banana', 'apple', 'cherry'}
>>>
>>>
>>> x = {"apple", "banana", "cherry", True}
>>> y = {"google", 1, "apple", 2}
>>>
>>> z = x.symmetric_difference(y)
>>> z
{2, 'cherry', 'google', 'banana'}
>>> type(z)
<class 'set'>
>>> z[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

#### Dictionaries

- Dictionaries are used to store data values in ==key : value== pairs.
- Dictionary is a collection which is ordered*, changeable and do not allow duplicates.

- dict is immutable
- won't allow duplicate values to be set (if {1: "Test", 1: "Not a test"}) returns {1: 'Not a test'}

```python
>>> mydict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
>>> mydict[2]
'Tea'
>>> mydict[1]
'Coffee'
>>> mydict[2] = 'Mint Tea'
>>> mydict[2]
'Mint Tea'
>>> del mydict[2]
>>> mydict
{1: 'Coffee', 3: 'Juice'}
>>>
>>> # dict iterations
>>> type(mydict)
<class 'dict'>
>>> mydict = {}
>>> mydict
{}
>>> type(mydict)
<class 'dict'>
>>> mydict = {1: "Test", "Name": "Jim"}
>>> mydict
{1: 'Test', 'Name': 'Jim'}
>>> mydict["Name"]
'Jim'
>>> mydict["Name"] = Adrian
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Adrian' is not defined
>>> mydict["Name"] = "Adrian"
>>> mydict["Name"]
'Adrian'
>>> mydict = {1: "Test", "Name": "Jim", 1: "Not a test"}
>>> mydict
{1: 'Not a test', 'Name': 'Jim'}
>>>
>>> del mydict[1]
>>> mydict
{'Name': 'Jim'}
>>>
>>> for x in mydict:
...     print(x)
...
Name
>>>
>>> for key, value in mydict.items():
...     print(key + " : " + value)
...
Name : Jim
```

---

```python
>>> thisdict = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> thisdict["model"]
'Mustang'
>>> len(thisdict)
3
>>> type(thisdict)
<class 'dict'>
>>>
>>> # dict constructor
>>> thisdict2 = dict(name = "John", age = 36, country = "Norway")
>>> thisdict2
{'name': 'John', 'age': 36, 'country': 'Norway'}
>>>
>>>
>>> x = thisdict.get("model")
>>> x
'Mustang'
>>> x = thisdict.keys()
>>> x
dict_keys(['brand', 'model', 'year'])
>>>
>>> thisdict["color"] = ["red", "white", "blue"]
>>> x
dict_keys(['brand', 'model', 'year', 'color'])
>>> thisdict["color"]
['red', 'white', 'blue']
>>> type(thisdict["color"])
<class 'list'>
>>> type(thisdict["color"][0])
<class 'str'>
>>> thisdict["color"][0]
'red'
>>>
>>>
>>> x = thisdict.values()
>>> x
dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue']])
>>> type(x)
<class 'dict_values'>
>>> y = thisdict.keys()
>>> type(y)
<class 'dict_keys'>
>>>
>>> thisdict["year"] = 2020
>>> x
dict_values(['Ford', 'Mustang', 2020, ['red', 'white', 'blue']])
>>> thisdict["color"].append("black")
>>> x
dict_values(['Ford', 'Mustang', 2020, ['red', 'white', 'blue', 'black']])
>>>
>>>
>>> z = thisdict.items()
>>> z
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', ['red', 'white', 'blue', 'black'])])
>>> thisdict["year"] = 2009
>>> z
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2009), ('color', ['red', 'white', 'blue', 'black'])])
>>>
>>> "black" in thisdict["color"]
True
>>> "yellow" in thisdict["color"]
False
```

---

```python
>>> # iteration
>>> thisdict = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> a = [x for x in thisdict.values()]
>>> a
['Ford', 'Mustang', 1964]
>>> type(a)
<class 'list'>
>>> a = [x for x in thisdict.keys()]
>>> a
['brand', 'model', 'year']
>>>
>>> c = [(key, values) for key, values in thisdict.items()]
>>> c
[('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]
>>>
>>>
>>> keys_list = [x for x in thisdict.keys()]
>>> values_list = [x for x in thisdict.values()]
>>> new_dict = dict(zip(keys_list, values_list))
>>> new_dict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


---
>>> thisdict = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> mydict = thisdict.copy()
>>> mydict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> mydict = dict(thisdict)
>>> mydict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> mydict = thisdict
>>> mydict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> del thisdict
>>> mydict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

---
nested dictionary
```python
myfamily = {  
  "child1" : {  
    "name" : "Emil",  
    "year" : 2004  
  },  
  "child2" : {  
    "name" : "Tobias",  
    "year" : 2007  
  },  
  "child3" : {  
    "name" : "Linus",  
    "year" : 2011  
  }  
}
```
```python
child1 = {  
  "name" : "Emil",  
  "year" : 2004  
}  
child2 = {  
  "name" : "Tobias",  
  "year" : 2007  
}  
child3 = {  
  "name" : "Linus",  
  "year" : 2011  
}  
  
myfamily = {  
  "child1" : child1,  
  "child2" : child2,  
  "child3" : child3  
}

---
>>> myfamily["child2"]["name"]
'Tobias'
```

#### args and kwargs in (func)

arguments for function 
- `*args` - Arbitrary Arguments
- `**kwargs` - Arbitrary Keyword Arguments

Keyword arguments, Non-keyword variables

args:
```python
def sum_of1(a, b):  
	return a + b  
  
print(sum_of1(4, 5))  
  
  
def sum_of2(*args):
	print(type(args))
	sum = 0  
	for x in args:  
		sum += x  
	return sum  
  
print(sum_of2(4, 5, 6, 7))
```
```python
<class 'tuple'>
9
22
```

---

kwargs:
```python
def sum_of(**kwargs):  
	print(type(**kwargs))
	sum = 0  
	for k, v in kwargs.items():  
		sum += v  
	return round(sum, 2)  
  
print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
```
```python
<class 'dict'>
10.53
```

---

```python
def sum_of(**kwargs):


    sum_of_order = 0
for k, v in kwargs.items():
    sum_of_order += v
return round(sum_of_order, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))

order_dict = dict(tea=1.99, salad=6.40)
print(sum_of(**order_dict))
```
```python
10.53
8.39
```




#### Python Collections (Arrays) and Choosing and using data structures

There are four collection data types in the Python programming language:

- **[List](https://www.w3schools.com/PYTHON/python_lists.asp)** is a collection which is ordered and changeable. Allows duplicate members.
- **[Tuple](https://www.w3schools.com/PYTHON/python_tuples.asp)** is a collection which is ordered and unchangeable. Allows duplicate members.
- **[Set](https://www.w3schools.com/PYTHON/python_sets.asp)** is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- **[Dictionary](https://www.w3schools.com/PYTHON/python_dictionaries.asp)** is a collection which is ordered** and changeable. No duplicate members.

![[Pasted image 20231125162023.png]]

list of employees that works a restaurant:
```python
employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}

print(get_employee(12458))
```

Instead of two employees, you may have 2000 or even 20,000. The code will have to iterate over the list sequentially until the number is matched.

```python
employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

  
def get_employee_from_dict(id):
    return employee_dict[id];
  

print(get_employee_from_dict(12458));
```
```python
def get_employee_from_dict(id, keys):
    return employee_dict[id][keys];

print(get_employee_from_dict(12458, "name"));

  
# type_choose_tuple = ("name", "department")
# print(get_employee_from_dict(12458, type_choose_tuple[1]));
```

```python
# self return error
employee_dict = {
    22458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];

print(get_employee_from_dict(12458));

#---
#Error on line 18:
#    print(get_employee_from_dict(12458));
#
#Error on line 15:
#    return employee_dict[id];
#KeyError: 12458
```


---

![[Pasted image 20231125161919.png]]
![[Pasted image 20231125161935.jpg]]

#### lab 1
1. Extend the script to have a new function called `calculate_subtotal`. It should accept one argument which is the order list and return the sum of the prices of the items in the order list.
2. Implement `calculate_tax()` which calculates the tax of the subtotal. The tax percentage is 15% of overall bill.
3. Implement `summarize_order()` which returns a list of the names of the items that the customer ordered and the total amount (including tax) that they have to pay. The orders should show the name and price.


### Basic Python Func

call a help documentation
```python
>>> fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
>>> dir(fruits)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(fruits.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>>
>>> help(print)
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

```

delete variable, type of variable, define length, define global variable in local scope (inside functions)
```python
>>> fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
>>> type(fruits)
<class 'list'>
>>> len(fruits)
5
>>> del fruits
>>> 
>>> def func1():
>>> 	global x = 10
```

iterate object and next element (when you use a for loop to iterate over the elements of a list or other collection, you are implicitly using iter() and next() built in func)
```python
>>> list_iter = iter([x for x in range(4)])
>>> next(list_iter)
0
>>> next(list_iter)
1
>>> next(list_iter)
2
>>> next(list_iter)
3
>>> next(list_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Errors, exceptions and file handling

#### Exception handling

```python
def divide_by(a, b):  
	return a / b  
  
  
# print(divide_by(40, 0)) # ZeroDivisionError: division by zero  
  
try:  
	ans = divide_by(40, 0)  
except ZeroDivisionError as e:  
	print(e, "we cannot divide by zero")  
except Exception as e:  
	print(e, "Something went wrong!")  
	print(e.__class__)  
  
# Starter code  
items = [1, 2, 3, 4, 5]  
# item = items[6]  
# print(item)  
try:  
	item = items[6]  
except IndexError:  
	print("Item does not exist in the list")  
  
  
# Starter code  
def divide_by(a, b):  
	return a / b  
  
  
# ans = divide_by(40, 0)  
# print(ans)  
  
try:  
	ans = divide_by(40, 0)  
except ZeroDivisionError:  
	print(0)  
  
# Starter code  
# with open('file_does_not_exist.txt', 'r') as file:  
# print(file.read())  
  
try:  
	with open('file_does_not_exist.txt', 'r') as file:  
		print(file.read())  
except FileNotFoundError:  
	print("The file could not be found")  
  
  
def divide_by(a, b):  
try:  
	return a / b  
except ZeroDivisionError:  
	return 0  
	except Exception as e:  
	print(e, 'Something went wrong!')  
  
  
ans = divide_by(10, 0)  
ans2 = divide_by(10, "a")  
print(ans)  
print(ans2)  
  
  
myvariable = NotImplemented  
print(myvariable)  
  
def myfunc1():  
	raise NotImplementedError  
  
  
def myfunc2():  
	pass
```

#### File Handling

`"r"` - Read - Default value. Opens a file for reading, error if the file does not exist
`"a"` - Append - Opens a file for appending, creates the file if it does not exist
`"w"` - Write - Opens a file for writing, creates the file if it does not exist
`"x"` - Create - Creates the specified file, returns an error if the file exists

`"t"` - Text - Default value. Text mode
`"b"` - Binary - Binary mode (e.g. images)


```python
file = open('test.txt', mode='r')  
  
data = file.readline()  
print(type(file))  
print(type(data))  
print(dir(file))  
print(help(file))  
  
print(data)  
  
file.close()
```
```python
<class '_io.TextIOWrapper'>
<class 'str'>
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '_
_hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fi
leno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writabl
e', 'write', 'write_through', 'writelines']
Help on TextIOWrapper object:

class TextIOWrapper(_TextIOBase)
 |  TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
 |
 |  Character and line based layer over a BufferedIOBase object, buffer.
 |

None
Hello there!
```

---

```python
with open('test.txt', mode='r') as file:  
	data = file.readline()  
	print(data)
```

---
creating files

```python
try:  
	write_mode = 'w'  
	append_mode = 'a'  
	  
	with open('sample/newfile.txt', append_mode) as file:  
		write_file = file.write("This is new file created!")  
		writelines_file = file.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])  
except FileNotFoundError as e:  
	print("ERROR", e)
```

---
reading files

```python
with open('newfile.txt', 'r') as file:  
	number_of_chars = 40  
	  
	data_read = file.read(number_of_chars)  
	data_readline = file.readline()  
	data_iter_readline = file.readlines()  
	  
	get_possible_method = dir(file)  
	  
	get_type = type(data_iter_readline)  
	get_by_index = data_iter_readline[0]  
	get_len = len(data_iter_readline)  
	  
	new_list = [line for line in data_iter_readline]  
	  
	print(get_possible_method)
```

---
others:

```python
>>> f = open("petnames.txt", "r")
>>> f
<_io.TextIOWrapper name='petnames.txt' mode='r' encoding='cp1251'>
>>> f_content = f.read()
>>> f_content_list = f_content.split("\n")
>>> f_content
'Ace\nAtlas\nBailey\nBear\nBlaze\nBoomer\nBuddy\nCoco\nCooper\nDuke\nDozer\nEcho\nGizmo\nHarley\nMac\nMax\nMilo\nOscar\nRex\nRocky\nRocket\nWolfie'
>>> f_content_list
['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']
>>> type(f_content_list)
<class 'list'>
>>> type(f_content)
<class 'str'>
>>> f.close()
```

---

```python
>>> import random
>>> f = open("petnames.txt", "r")
>>> f_content = f.read()
>>> f_content_list = f_content.split("\n")
>>> f.close()
>>>
>>> f_content_list
['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']
>>> random.choice(f_content_list)
'Blaze'
>>> random.choice(f_content_list)
'Echo'
```

---

```python
>>> import random
>>> f_name = input("Type the file name: ")
Type the file name: petnames.txt
>>> f = open(f_name) # "r" omitted as it's the default
>>> f_content = f.read()
>>> f_content_list = f_content.split("\n")
>>> f.close()
>>> random.choice(f_content_list)
'Max'
```


### Labs hands-on

#### lab 1 - menu ordering system

```python
menu = {  
	1: {  
		"name": 'espresso',  
		"price": 1.99  
	},  
	2: {  
		"name": 'coffee',  
		"price": 2.50  
	},  
	3: {  
		"name": 'cake',  
		"price": 2.79  
	},  
	4: {  
		"name": 'soup',  
		"price": 4.50  
	},  
	5: {  
		"name": 'sandwich',  
		"price": 4.99  
	}  
}  
  
  
def calculate_subtotal(order):  
	print('Calculating bill subtotal...')  
	global sum_of  
	sum_of = 0  
	for item in order:  
		sum_of += item["price"]  
	  
	return round(sum_of, 2)  
  
  
def calculate_tax(subtotal):  
	print('Calculating tax from subtotal...')  
	  
	tax_rate = 15  
	  
	global tax  
	tax = subtotal * (tax_rate / 100)  
	return round(tax, 2)  
  
  
def summarize_order(order):
	print_order(order)  
	
	# subtotal = sum(item["price"] for item in order)  
	subtotal = sum_of  
	  
	total = round(subtotal + tax, 2)  
	names = [item["name"] for item in order]  
	  
	return names, total  
  
  
def print_order(order):  
	print('You have ordered ' + str(len(order)) + ' items')  
	items = []  
	items = [item["name"] for item in order]  
	print(items)  
	return order  
  
  
def display_menu():  
	print("------- Menu -------")  
	for selection in menu:  
		print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")  
	print()  
  
  
def take_order():  
		display_menu()  
		order = []  
		count = 1  
		for i in range(3):  
			item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')  
			count += 1  
			order.append(menu[int(item)])  
		return order  
  
  
def main():  
	order = take_order()  
	print_order(order)  
	  
	subtotal = calculate_subtotal(order)  
	print("Subtotal for the order is: " + str(subtotal))  
	tax = calculate_tax(subtotal)  
	print("Tax for the order is: " + str(tax))  
	  
	items, total = summarize_order(order)  
	  
	print(total)  
  
  
if __name__ == "__main__":  
	main()

```

#### lab 2 - file handling

```python
def read_file(file_name):  
	with open(file_name, "r") as file:  
		data_read = file.read()  
		  
		return data_read  
  
  
def read_file_into_list(file_name):  
	with open(file_name, "r") as file:  
		readline_file_list = file.readlines()  
		  
		return readline_file_list  
  
  
def write_first_line_to_file(file_contents, output_filename):  
	convert_to_list = file_contents.split("\n")  
	get_first_line = convert_to_list[0]  
	  
	with open(output_filename, 'w') as file:  
		write_file = file.write(get_first_line) 
		 
		return write_file  
  
  
def read_even_numbered_lines(file_name):  
	with open(file_name, "r") as file:  
		readline_file = file.readlines()  
		  
		odd_list = readline_file[::2]  
		even_list = readline_file[1::2]  
		  
		return even_list  
  
  
def read_file_in_reverse(file_name):  
	with open(file_name, "r") as file:  
		readline_file = file.readlines()  
		print(readline_file)  
		  
		reverse_initial_list = readline_file.reverse()  
		  
		return readline_file  
  

  
def main():  
	# file_contents = read_file("sampletext.txt")  
	# print(read_file_into_list("sampletext.txt"))  
	# write_first_line_to_file(file_contents, "online.txt")  
	# print(read_even_numbered_lines("sampletext.txt"))  
	print(read_file_in_reverse("sampletext.txt"))  
  
  
if __name__ == "__main__":  
	main()

```

### SRC

Learn more about Python data structures (Python documentation) on the Python website: 
[Python.org - Data structures](https://docs.python.org/3/tutorial/datastructures.html) 
Explore common Python data structures at the Real Python website: 
[Real Python - Data structures](https://realpython.com/python-data-structures)

---

Learn more about exceptions and errors in Python on the Python website: 
[Exceptions and Errors in Python - Python docs](https://docs.python.org/3/library/exceptions.html)
Check out the PyNative website to learn more about file handling in Python: 
[File handling in Python](https://pynative.com/python/file-handling/)

---
- scope in python
- how see object elements in python
- [introspection - How do I look inside a Python object? - Stack Overflow](https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object)
- [Python *args (w3schools.com)](https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp)
- [Python **kwargs (w3schools.com)](https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp)

- mathematical operations on set python
- [Python - List Methods (w3schools.com)](https://www.w3schools.com/PYTHON/python_lists_methods.asp)
- [Python - Set Methods (w3schools.com)](https://www.w3schools.com/PYTHON/python_sets_methods.asp)
- [Python - Dictionary Methods (w3schools.com)](https://www.w3schools.com/PYTHON/python_dictionaries_methods.asp)

- [Python next() Function (w3schools.com)](https://www.w3schools.com/python/ref_func_next.asp)

- [Python Try Except (w3schools.com)](https://www.w3schools.com/python/python_try_except.asp)
- [Python File Open (w3schools.com)](https://www.w3schools.com/python/python_file_handling.asp)

- comparison build-in data structure in python
- list vs tuple vs dict vs set python
- [Python Data Structures - GeeksforGeeks](https://www.geeksforgeeks.org/python-data-structures/)

- stack frame in python
- [Scope, Frame and Stack — Understanding Recursion Using Python 1.0 documentation (understanding-recursion.readthedocs.io)](https://understanding-recursion.readthedocs.io/en/latest/02%20Scope,%20Frame%20and%20Stack.html)