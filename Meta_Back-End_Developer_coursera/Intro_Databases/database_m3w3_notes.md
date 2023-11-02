**MOCs**





## SQL operators
![[Pasted image 20231028135421.png|400]]
![[Pasted image 20231028140322.png|400]]

arithmetic operators - used to perform mathematical calculations in a database.
comparison operators - used to compare two values or expressions.
(filter data, include data, exclude data). 
![[Pasted image 20231028135822.png|400]]
![[Pasted image 20231028135900.png|400]]
![[Pasted image 20231028135924.png|400]]

---
**Comparison operators** 

|**Operator**|**Description**|
|---|---|
|=|Checks if the values of two operands are equal or not. If yes, then condition becomes true.|
|!=|Checks if the values of two operands are equal or not. If values are not equal, then condition becomes true.|
|<>|Checks if the values of two operands are equal or not. If values are not equal, then condition becomes true.|
|>|Checks if the value of the left operand is greater than the value of the right operand. If yes, then condition becomes true.|
|<|Checks if the value of left operand is less than the value of right operand. If yes, then condition becomes true.|
|>=|Checks if the value of the left operand is greater than or equal to the value of right operand. If yes, then condition becomes true.|
|<=|Check if the value of the left operand is less than or equal to the value of the right operand. If yes then condition becomes true.|
|!<|Checks if the value of the left operand is not less than the value of the right operand. If yes, then condition becomes true.|
|!>|Checks if the value of the left operand is not greater than the value of the right operand. If yes, then condition becomes true.|


**Logical operators** 

|**Operator**|**Description**|
|---|---|
|**ALL**|Used to compare a single value to all the values in another value set.|
|**AND**|Allows for the existence of multiple conditions in an SQL statement's WHERE clause.|
|**ANY**|Used to compare a value to any applicable value in the list as per the condition.|
|**BETWEEN**|Used to search for values that are within a set of values, given the minimum value and the maximum value.|
|**EXISTS**|Used to search for the presence of a row in a specified table that meets a certain criterion.|
|**IN**|Used to compare a value to a list of literal values that have been specified.|
|**LIKE**|Used to compare a value to similar values using wildcard operators.|
|**NOT**|Reverses the meaning of the logical operator with which it is used. For example: NOT EXISTS, NOT BETWEEN, NOT IN, etc. **This is a negate operator.**|
|**OR**|Used to combine multiple conditions in an SQL statement's WHERE clause.|
|**IS NULL**|Used to compare a value with a NULL value.|
|**UNIQUE**|Searches every row of a specified table for uniqueness (no duplicates).|

---
```mysql
-- @block
SELECT 10 + 15;
-- @block
SELECT 101 % 10;
-- @block
CREATE TABLE employee (
	employee_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	empleyee_name varchar(50), 
	salary INT NOT NULL, 
	allowance INT DEFAULT 1000);
-- @block
ALTER TABLE employee RENAME COLUMN empleyee_name TO employee_name;
-- @block
INSERT INTO employee (employee_name, salary) 
VALUES 
	("Alex", 25000), 
	("John", 55000), 
	("James", 52000), 
	("Sam", 30000);
-- @block
SELECT * FROM employee;
-- @block
SELECT salary + allowance FROM employee;
-- @block
UPDATE employee 
SET salary = 29000 
WHERE employee_id IN (1, 4);
-- @block
SELECT * FROM employee 
WHERE salary + allowance = 30000;
-- @block
SELECT * FROM employee 
WHERE salary + allowance >= 31000;
-- @block
ALTER TABLE employee ADD tax INT DEFAULT 1000;
-- @block
UPDATE employee 
SET tax = tax * 2 
WHERE salary >= 50000;
-- @block
SELECT (salary + allowance) - tax FROM employee;
-- @block
SELECT (salary + allowance) - (tax * 2) FROM employee;
-- @block
SELECT * FROM employee 
WHERE tax * 2 = 4000;
-- @block
SELECT * FROM employee 
WHERE allowance / salary * 100 >= 3;
-- @block
ALTER TABLE employee ADD hours TIME;
-- @block
UPDATE employee 
SET hours = CASE employee_id 
	WHEN 1 THEN 10 
	WHEN 2 THEN 11 
	WHEN 3 THEN 7 
	WHEN 4 THEN 11 
	ELSE hours 
END;
-- @block
ALTER TABLE employee MODIFY hours TINYINT(24);
-- @block
SELECT hours % 2 FROM employee;
-- @block
ALTER TABLE employee RENAME COLUMN hours TO hours_in_day;
-- @block
SELECT employee_name, hours_in_day, (salary + allowance - tax) / 12 FROM employee;
-- @block
SELECT employee_name, 
(salary + allowance - CASE WHEN hours_in_day >= 10 
	 THEN tax / 2 
	 ELSE tax 
END) / 12 FROM employee;
-- @block
SELECT employee_name, salary / 12 FROM employee 
WHERE salary / 12 >= 4000;
-- @block
SELECT employee_name, salary FROM employee 
WHERE salary <> 52000;
-- @block
SELECT employee_name, salary FROM employee 
WHERE salary != 29000;
-- @block
SELECT * FROM employee WHERE hours_in_day <= 10;
```

operator IN:
```mysql
UPDATE employee 
SET salary = 29000 
WHERE employee_id IN (1, 4);
```
позволяет указать несколько значений в предложении `WHERE`.
(allows to specify multiple values in the `WHERE` clause).

`WHERE` - is condition.

## Sorting and Filtering data

#### ORDER BY clause
![[Pasted image 20231028200738.png|400]]
![[Pasted image 20231028200844.png|400]]
![[Pasted image 20231028200927.png|400]]

```mysql
-- @block
CREATE TABLE student (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	first_name VARCHAR(50), 
	last_name VARCHAR(100), 
	date_of_birth DATE, 
	nationality VARCHAR(40) DEFAULT "US"
);
-- @block
INSERT INTO student (first_name, last_name, date_of_birth, nationality) 
VALUES 
	("John", "Murphy", "1999-02-01", "US"), 
	("Sandra", "Hauge", "2000-06-20", "US"), 
	("Jerry", "Martin", "2000-03-30", "Australia"),
	("Heather", "Dawson", "1999-08-21", "UK"), 
	("Ryan", "Egan", "2000-04-30", "Chine");
-- @block
SELECT * FROM student 
ORDER BY nationality;
-- by default is return ASC
-- @block
SELECT * FROM student 
ORDER BY nationality DESC;
-- @block
SELECT * FROM student 
ORDER BY nationality ASC, date_of_birth DESC;
```

#### WHERE clause

WHERE clause - Filter and retrieve records that meet a specific condition.
![[Pasted image 20231028204648.png|400]]
![[Pasted image 20231028204832.png|400]]

SQL operators (that used in WHERE condition)
- arithmetic operators
- comparison operators
- logical operators
	- BETWEEN - Filter records within a numeric or time and date range
	- LIKE - Specify a pattern within the search criteria 
	- IN - Specify multiple possible values for a column
	- AND - logical and 
	- OR - logical or
![[Pasted image 20231028205542.png|600]]


```mysql
-- @block
ALTER TABLE student ADD faculty VARCHAR(50) DEFAULT "Science";
-- @block
UPDATE student 
SET faculty = "Engineer" 
WHERE id IN (2, 4, 7);
-- @block
SELECT * FROM student 
WHERE faculty = "Science";
-- @block
SELECT * FROM student 
WHERE date_of_birth 
BETWEEN "1999-01-01" AND "1999-011-28";
-- @block
SELECT * FROM student 
WHERE faculty LIKE "Sc%";
-- @block
SELECT * FROM student 
WHERE nationality IN ("US", "UK");
-- @block
SELECT * FROM student 
WHERE nationality IN ("US", "UK") 
AND faculty LIKE "En%";
-- @block
SELECT * FROM student 
WHERE nationality IN ("US", "UK") 
OR faculty LIKE "En%";
-- @block
SELECT * FROM student 
WHERE id < 5 AND nationality = "US" OR "UK";
```

#### SELECT DISTINCT clause
![[Pasted image 20231028220104.png|500]]

`SELECT country FROM student_tbl`
![[Pasted image 20231028220332.png|400]]
So how can you eliminate these duplicates and retrieve a unique set of results?f
![[Pasted image 20231028220431.png|500]]

You need to return values from a table while ensuring that there are no duplicates in your results. Can you use a SELECT DISTINCT statement to complete this task?
- Yes

```mysql
-- @block
SELECT DISTINCT nationality FROM student;
-- @block
SELECT DISTINCT faculty, nationality FROM student;
-- @block
SELECT COUNT(DISTINCT nationality) FROM student;
```

`COUNT()` - is SQL aggregate functions. 
Like:
```mysql
-- @block
SELECT COUNT(id) FROM student;
-- @block
SELECT MAX(id) FROM student;
-- @block
SELECT AVG(id) FROM student;
-- @block
SELECT MIN(id) FROM student;
```

## Lab ORDER BY and WHERE

setup:
```mysql
-- @block
CREATE DATABASE Chinook;
-- @block
USE Chinook;
-- @block
CREATE TABLE Customer (
	CustomerId INT NOT NULL, 
	FirstName VARCHAR(40) NOT NULL, 
	LastName VARCHAR(20) NOT NULL, 
	Company VARCHAR(80), 
	Address VARCHAR(70), 
	City VARCHAR(40), 
	State VARCHAR(40), 
	Country VARCHAR(40), 
	PostalCode VARCHAR(10), 
	Phone VARCHAR(24), 
	Fax VARCHAR(24), 
	Email VARCHAR(60) NOT NULL, 
	SupportRepId INT, 
	CONSTRAINT PK_Customer PRIMARY KEY (CustomerId));
-- @block
INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) 
VALUES 
	(1, 'Luís', 'Gonçalves', 'Embraer - Empresa Brasileira de Aeronáutica S.A.', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3),
	(2, 'Eduardo', 'Martins', 'Woodstock Discos', 'Rua Dr. Falcão Filho, 155', 'São Paulo', 'SP', 'Brazil', '01007-010', '+55 (11) 3033-5446', '+55 (11) 3033-4564', 'eduardo@woodstock.com.br', 4),
	(3, 'Alexandre', 'Rocha', 'Banco do Brasil S.A.', 'Av. Paulista, 2022', 'São Paulo', 'SP', 'Brazil', '01310-200', '+55 (11) 3055-3278', '+55 (11) 3055-8131', 'alero@uol.com.br', 5),
	(4, 'Roberto', 'Almeida', 'Riotur', 'Praça Pio X, 119', 'Rio de Janeiro', 'RJ', 'Brazil', '20040-020', '+55 (21) 2271-7000', '+55 (21) 2271-7070', 'roberto.almeida@riotur.gov.br', 3),
	(5, 'Mark', 'Philips', 'Telus', '8210 111 ST NW', 'Edmonton', 'AB', 'Canada', 'T6G 2C7', '+1 (780) 434-4554', '+1 (780) 434-5565', 'mphilips12@shaw.ca', 5),
	(6, 'Jennifer', 'Peterson', 'Rogers Canada', '700 W Pender Street', 'Vancouver', 'BC', 'Canada', 'V6C 1G8', '+1 (604) 688-2255', '+1 (604) 688-8756', 'jenniferp@rogers.ca', 3);
```

---
exercise:
```mysql
-- @block
SELECT CustomerID, FirstName, City, State, Country FROM Customer;
-- @block
SELECT CustomerID, FirstName, LastName, City, State, Country FROM Customer 
ORDER BY FirstName;
-- @block
SELECT CustomerID, FirstName, State, Country FROM Customer 
WHERE Country = "Canada";
-- @block
SELECT CustomerID, FirstName, State, Country FROM Customer WHERE Country = "Canada" 
ORDER BY CustomerID DESC;
```

## SRC

**SQL operators**
- [W3Schools](https://www.w3schools.com/sql/sql_operators.asp)
- [Javatpoint](https://www.javatpoint.com/sql-arithmetic-operators)
- [Tutorialspoint](https://www.tutorialspoint.com/sql/sql-operators.htm)
- [w3resource](https://www.w3resource.com/sql/comparison-operators/sql-comparison-operators.php)

researching:
- [MySQL Operators (w3schools.com)](https://www.w3schools.com/mysql/mysql_operators.asp)
- [MySQL CASE Statement (w3schools.com)](https://www.w3schools.com/mysql/mysql_case.asp)
- [MySQL IN Operator (w3schools.com)](https://www.w3schools.com/mysql/mysql_in.asp)

---
**Sorting and Filtering data**

- [W3Schools](https://www.w3schools.com/sql/sql_operators.asp)
- [Javatpoint](https://www.javatpoint.com/sql-arithmetic-operators)
- [Tutorialspoint](https://www.tutorialspoint.com/sql/sql-operators.htm)

researching:
- [MySQL AND, OR, NOT Operators (w3schools.com)](https://www.w3schools.com/mysql/mysql_and_or.asp)
- [MySQL ORDER BY Keyword (w3schools.com)](https://www.w3schools.com/mysql/mysql_orderby.asp#gsc.tab=0)
- [SQL SELECT DISTINCT Statement (w3schools.com)](https://www.w3schools.com/sql/sql_distinct.asp)

- SQL aggregate functions
- [MySQL Functions (w3schools.com)](https://www.w3schools.com/mysql/mysql_ref_functions.asp)
- [SQL MIN() and MAX() Functions (w3schools.com)](https://www.w3schools.com/sql/sql_min_max.asp)

- sql create trigger
- sql script
- pl/sql