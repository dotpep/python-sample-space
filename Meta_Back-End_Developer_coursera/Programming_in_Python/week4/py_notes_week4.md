### Modules

Everything in python is object and that object can import in anywhere.
Module give us reuse our implemented code in others programs.
- scope - modules create separate namespace
- reusability (modularity) or DRY
- simplicity

![[Pasted image 20231216033024.jpg]]

### Some python package, library, framework, tech stack



---

- **RedShift and S3:** Amazon services are used with their cloud services. S3 is a storage service and RedShift is a data warehousing service.
- **BigQuery:** Developed by Google, BigQuery is a Cloud service library that is useful with RESTful APIs.
- **PySpark:** This is an open-source framework used for large scale data processing and works with resilient distributed datasets.
- **Kafka:** This is a publish-subscribe messaging system that receives logs in the form of packages and is stored in partitioned spaces.
- **Pydoop:** Pydoop provides an interface between Hadoop and Python and support for handling its Hadoop distributed file systems.


### Testing Tools

evaluating, verifying in terms of performance, correctness, and completeness helps identify bugs, gaps in product, defects, and missing requirements with set expectations.

- unittest
- pytest
- tdd

#### Types of Testing

**Categorize testing:**
- White box testing - where we know about functionality and code design
- Black box testing - where no such information and test no idea of entire implementation

- Functional tests - based on business requirements stated, determine if functionalities and features in line with expectations. 
	- Non-functional tests - complex to define and involves such as overall performance and quality.
- Maintenance tests - when environments changed

---
**Four Main level of Testing**
- Unit/Component testing
- Integration testing
- System testing
- Acceptance testing

#### Test automation packages
this test can be automated:
- Unit (built-in package)
- Regression
- Integration

---
- PyTest (native python library) - functional, unit, parameterized, parallel 
- Robot (keyword-driven development capabilities) - acceptance testing, RPA, TDD
- Selenium (web applications) - browser and OS supports, browser-specific web drivers

#### PyTest

- install: `pip install pytest`
- Add suffix `test_` to the file that needs to be tested.
- Add suffix `test_` to the functions to be tested.
---
Running pytest:
- command for run: `python -m pytest test_addition.py`
- check specific function command: `python -m pytest test_addition.py::test_add`
---
Other options:
- run: `py.test test_file.py`
Flags:
- using flags: `python3 -m pytest abc.py -v` 
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed

---
##### Fixtures

Fixtures are a type of function that is applied to functions to be tested. These functions must run before that test is executed. The purpose of fixtures is to supply data from multiple sources including URLs and databases to the test before running the test. Fixtures are used in cases where code repeats initialization.

Format: `@pytest.fixture`

##### Markers

Markers are used to 'mark' specific functions to be executed by letting users create special names. There are many built-in markers such as xfail, xpass, skip and so on.

They follow a format such as: `@pytest.mark.<markername>`

---
For example:
- `@pytest.mark.alpha`
Running the specific marked test in the command line can be done with the following command:
- `pytest -m <markername> -v`
Which will be as follows for a marker called alpha.
- `pytest -m alpha -v`

##### Example code using PyTest (unit testing)

adding.py
```python
def add(a, b):  
	return a + b  
  
def sub(a, b):  
	return a - b
```
test_adding.py
```python
import addition  
import pytest  
  
def test_add():  
	assert addition.add(4, 5) == 9  
	# assert True  
	# assert False  
  
def test_sub():  
	assert addition.sub(4, 5) == -1  
	# pass  
  
if __name__ == "__main__":  
	test_add()  
	test_sub()
```

#### Test-driven development (TDD)

TDD - write tests first, and then code, so that tests will pass.
![[Pasted image 20231217193014.png|600]]
![[Pasted image 20231217193037.png|600]]

---
Advantages of TDD
![[Pasted image 20231217193154.png|600]]

---
Difference between TDD and traditional testing
- requirements and standards are highlighted from beginning.

#### Applying TDD methodology

test_findstring.py
```python
from findstring import is_present, no_digit    
  
def test_is_present():  
	assert is_present("Al")  
  
def test_no_digit():  
	assert no_digit("N7")
```
findstring.py
```python
def is_present(person):  
	names = ["Al", "Bo", "Chi", "Ma"]  
	if person in names:  
		return True  
	else:  
		return False  
  
def no_digit(person):  
	if person.isdigit():  
		return True  
	else:  
		return False  
```

---
test_mark_findstring.py
```python
from marked_findstring import mark_is_present, mark_no_digit  
import pytest  
  
@pytest.mark.parametrize("person, expected", [  
	("Al", True),  
	("Zoe", False),  
	("", False),  
])  
def test_mark_is_present(person, expected):  
	assert mark_is_present(person) == expected  
  
@pytest.mark.parametrize("person, expected", [  
	("N7", False),  
	("Leo", True),  
	("123", False),  
])  
def test_mark_no_digit(person, expected):  
	assert mark_no_digit(person) == expected
```
mark_findstring.py
```python
def mark_is_present(person):  
	"""Check if a person's name is present in a list of names.  
	Args:  
	person (str): The name of the person to check.  
	Returns:  
	bool: True if the name is present, False otherwise.  
	"""  
	names = ["Al", "Bo", "Chi", "Ma"]  
	return person in names  
  
def mark_no_digit(person):  
	"""Check if a person's name contains no digit.  
	Args:  
	person (str): The name of the person to check.  
	Returns:  
	bool: True if the name contains no digit, False otherwise.  
	"""  
	for char in person:  
		if char.isdigit():  
			return False  
	return True
```


#### Testing code example
must be:
- file and function name start with `test_` (test_somename)
- separate into modular structure

module: division.py (refactored after unpassed tests)
```python
def division(num1, num2):  	  
	if type(num1) not in [int, float] or type(num2) not in [int, float]:  
		raise TypeError  
		# return "Type Error"  
	  
	if num2 == 0:  
		raise ZeroDivisionError  
		# return "Division by Zero"  
	  
	return round(num1 / num2, 8)
```
module: test_division.py
```python
# def division(num1, num2):  
# return num1 / num2  
  
# print(division(4, 2))  
# print(division(4, 0))  
# print(division("a", 2))  
# print(division())  
  
# 0.1 + 0.2 = 0.30000000000000004  
# print(division(0.009, 0.003)) # 0.009 / 0.003 = 2.9999999999999996  
  
# assert division(4, 0) == ZeroDivisionError, "4 / 0 = 0"  
# assert 2 + 2 != 4, "2 + 2 = 4"  
  
from division import division  


def test_division():  
	assert division(4, 2) == 2  
	assert division(10, 2) == 5  
	assert division(0.009, 0.003) == 3, "Mantissa (Floating-point arithmetic)"  
	assert division(4, 0) == "Division by zero"  
  
  
def test_values():  
	assert division("a", 2) == "Type Error"  
	assert division([4], 2) == "Type Error"  
	assert division(4.4, 2) == 2.2  
	assert division(None, 2) == "Type Error"  
  
  
if __name__ == "__main__":  
	test_division()  
	test_values()  
	print("OK")
```
module: test_division_UnitTest.py (this is Unit Test)
```python
import unittest  
  
from division import division  
  
  
class DivisionTest(unittest.TestCase):  
	def test_division(self):  
		self.assertEquals(division(4, 2), 2)  
		self.assertEquals(division(10, 2), 5)  
		self.assertEquals(division(0.009, 0.003), 3)  
		self.assertRaises(ZeroDivisionError, division, 4, 0)  
	  
	def test_value(self):  
		self.assertRaises(TypeError, division, "a", 2)  
		self.assertRaises(TypeError, division, [4], 2)  
		self.assertRaises(TypeError, division, None, None)  
		self.assertEquals(division(4.4, 2), 1000)  
  
  
if __name__ == "__main__":  
	unittest.main()
```

### SRC

- module vs package vs library vs framework in python
- modular programming
- SOLID, patterns, folder structure, architecture design
- Atomicity in programming
- sockets
- threading
- protocols
- routing request
- authentication
- web python microframeworks
- asynchronous in python
- wsgi python
- https request handling in python

- [Popular Python packages for web development](https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/)
- [ML and AI libraries in Python](https://towardsdatascience.com/best-python-libraries-for-machine-learning-and-deep-learning-b0bd40c7e8c)
- [Data Science libraries in Python](https://www.dataquest.io/blog/15-python-libraries-for-data-science/)

---

- [Test-Driven Development](https://testdriven.io/blog/modern-tdd/)
- [Test-driven Development with PyTest](https://stackabuse.com/test-driven-development-with-pytest/)
- [PyTest Official website](https://docs.pytest.org/en/7.1.x/)
- [Test automation packages in Python](https://www.geeksforgeeks.org/best-python-modules-for-automation/)

- [Floating Point Math (30000000000000004.com)](https://0.30000000000000004.com/)
- [CS50P - Lecture 5 - Unit Tests - YouTube](https://www.youtube.com/watch?v=tIrcxwLqzjQ&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=10)
- [Pytest Tutorial – How to Test Python Code (youtube.com)](https://www.youtube.com/watch?v=cHYq1MRoyI0)
- [Python Tutorial: Unit Testing Your Code with the unittest Module - YouTube](https://www.youtube.com/watch?v=6tNS--WetLI)
- testing in python
- pytest
- selenium
- TDD
- types of testing
- [Pytest Курс - YouTube](https://www.youtube.com/playlist?list=PLeLN0qH0-mCVdHgdjlnKTl4jKuJgCK-4b)

- [unittest — Unit testing framework — Python 3.12.1 documentation](https://docs.python.org/3/library/unittest.html)
- [Get Started — pytest documentation](https://docs.pytest.org/en/7.4.x/getting-started.html)
- [Django documentation | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/5.0/)
- [Home - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/)