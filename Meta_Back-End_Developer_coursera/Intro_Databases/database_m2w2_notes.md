**MOCs**


## SQL data types

Data types - datatypes tell a database management system how to interpret the value if a column.

Numeric data types - datatypes that let columns store data as numbers within the database:
![[Pasted image 20231025233510.png|500]]
in MySQL:
- TINYINT - used for very small integer number value, 0-255.
- INT - used to store a very big number, max four billion.
- Positive and Negative numbers of these.

String data types - used when storing data with mixed of characters. (text: alphabet, numeric, special characters)
![[Pasted image 20231026005725.png|400]]
![[Pasted image 20231026005819.png|500]]
![[Pasted image 20231026005915.png|300]]
![[Pasted image 20231026010103.png|300]]
- TINYTEXT - less than 255 characters like short paragraphs.
- TEXT - less that 65,000 characters like an article.
- MEDIUMTEXT - defined columns of 16.7 million characters, for example text of a book.
- LONGTEXT- four gigabytes of text data.


#### Default values (sql statement)
database constraints as a method of enforcing rules on a column or table level.

Database constraints. (ограничение)
- NOT NULL (preserves empty value fields).
- DEFAULT (assigns default values).
Violation example. (нарушение)
Constraints - applied at column level.
Rule - applies to a specific column.
Foreign Key - used to prevent actions that would destroy table links.


NOT NULL SQL constraint - ensures data fields never left blank.
![[Pasted image 20231026013031.png|500]]
DEFAULT - sets a default value for a column if no value is specified.
![[Pasted image 20231026013323.png|500]]
![[Pasted image 20231026013353.png|400]]
Instead, it will be inserted automatically.

- Database default constraints are used to limit the value of data that can be stored in a table.

## Create and Read

#### CREATE and DROP
![[Pasted image 20231027000253.png|400]]

`CREATE DATABASE bookstore_db;`
`DROP DATABASE bookstore2_db;`
`USE bookstore_db;`
`create table customers(customer_name varchar(100), phone_number int);`
`show columns from customers;`
`show tables;`

#### ALTER TABLE
![[Pasted image 20231027003002.png|400]]
![[Pasted image 20231027003022.png|400]]

`ALTER TABLE customers ADD(customers_id INT);`
`ALTER TABLE customers DROP COLUMN customers_id;`
`ALTER TABLE customers ADD(email VARCHAR(50));`
`ALTER TABLE customers MODIFY email VARCHAR(100);`

#### INSERT INTO
![[Pasted image 20231027003813.png|500]]
multiple insert into statement:
![[Pasted image 20231027003842.png|400]]

```mysql
INSERT INTO customers(customer_name, phone_number, email) 
VALUES 
	("Jakes", 7731443, "ja7kes@gmail.com"), 
	("Goba", 887763, "bob3@mail.com"), 
	("Maxim", 445567, "maxxm@ru.com");
```
`SELECT * FROM customers;`


#### SELECT statement and INSERT INTO SELECT statement
![[Pasted image 20231027012502.png|500]]

---
![[Pasted image 20231027013439.png|500]]
![[Pasted image 20231027013533.png|500]]


## Update and Delete

```mysql
UPDATE customers 
SET phone_number = 773144, email = "jakes7@gmail.com" 
WHERE name = "Jakes";
```

for multiple UPDATE's
```mysql
-- @block
ALTER TABLE customers 
ADD (city varchar(50), post_code INT);
-- @block
UPDATE customers 
SET post_code = 055055 
WHERE city = 'Los Angeles';
-- @block
DELETE FROM customers WHERE name = "Goba";
-- @block
DELETE FROM customers WHERE city = "Los Angeles";
-- @block
DELETE FROM customers;
```

The `TRUNCATE TABLE` command deletes the data inside a table, but not the table itself.
```mysql
TRUNCATE TABLE customers;
```

## SQL command labs

#### SQL data types
1. `mysql -u your_username -p`
2. `CREATE DATABASE cm_devices;`
3. `SHOW DATABASES;`
4. `USE cm_devices;`
5. `CREATE TABLE devices (deviceID int, deviceName varchar(50), price decimal);`
6. `SHOW tables;`
7. `SHOW columns FROM devices;`

lab1 - numbers
```mysql
CREATE TABLE devices (
	device_id int, 
	device_name varchar(50), 
	price decimal
	);
```
lab1.2
```mysql
CREATE TABLE stock (
	device_id int, 
	quantity int, 
	total_price decimal
	);
```
lab2 - string
```mysql
CREATE TABLE customers (
	username CHAR(9), 
	fullName VARCHAR(100), 
	email VARCHAR(255)
	);
```
lab2.2
```mysql
CREATE TABLE feedback(
	feedback_id CHAR(8), 
	feedback_type VARCHAR(100), 
	comment TEXT(500)
	);
```
lab3 - default values (not null)
```mysql
CREATE TABLE address(
	customer_id int NOT NULL, 
	street varchar(100), 
	postcode varchar(50), 
	town varchar(50) DEFAULT "Harrow"
	);
```
lab3.2
```mysql
-- @block
DROP TABLE address;
-- @block
CREATE TABLE address (
	id int NOT NULL, 
	street VARCHAR(255), 
	postcode VARCHAR(10) DEFAULT "HA97DE", 
	town VARCHAR(30) DEFAULT "Harrow"
	);
```
lab4 - choose right data type
```mysql
CREATE TABLE invoice (
	customer_name varchar(50), 
	order_date date, 
	product_quantity int, 
	total_price decimal
	);
```
lab4.2
```mysql
CREATE TABLE contact (
	customer_account_number int, 
	phone_number int, 
	email_adress varchar(100)
	);
```


#### Create and Read

lab1
```mysql
-- DEFAULT CURRENT_DATE()
-- @block
ALTER TABLE customers ADD(join_date DATE);
-- @block
INSERT INTO customers 
VALUES 
	("Elizabeth", 9887774, "eli23@gmail.com", CURRENT_DATE());
-- @block
-- CURRENT_DATE() don't work with DEFAULT instead use TIMESTAMP
ALTER TABLE customers MODIFY join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
-- @block
INSERT INTO customers 
VALUES ("Nagato", 875474, "nagatosss@jp.com", "2023-10-09");
-- @block
UPDATE customers 
SET join_date = "2023-09-05" 
WHERE customer_name = "Goba";
-- @block
SELECT * FROM customers;
-- #block 
ALTER TABLE customers ADD(adress varchar(255));
-- @block
ALTER TABLE customers DROP COLUMN adress;
-- @block
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
-- @block
ALTER TABLE table_name CHANGE old_column_name new_column_name Data_Type;
-- @block
ALTER TABLE customers RENAME COLUMN customer_name TO name;
```

lab2
```mysql
-- @block
-- asterisk for retrieve all column
SELECT * FROM customers;
-- @block
SELECT name, join_date FROM customers;
-- @block
CREATE TABLE orders (
	order_date date, 
	address varchar(255), 
	customer_name varchar(50)
	);
-- @block
INSERT INTO _table2_ (_column1_, _column2_, _column3_, ...)  
SELECT _column1_, _column2_, _column3_, ...  
FROM _table1_  
WHERE _condition_;
-- @block
INSERT INTO orders(customer_name) SELECT name FROM customers;
-- lab2
CREATE DATABASE football_club;
USE football_club;
-- @block
CREATE TABLE players(id INT, player_name varchar(50), player_age TINYINT(100));
-- @block
CREATE TABLE games(
	game_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	game_date DATE, 
	score INT);
```



#### Update and Delete 

lab1
```mysql
-- @block
-- `TRUNCATE TABLE` command deletes the data inside a table, but not the table itself.
TRUNCATE TABLE customers;
-- @block
INSERT INTO customers 
(customer_id, customerName, customerAddress) 
VALUES
	(1, 'Jack', '115 Old street Belfast'),
	(2, 'James', '24 Carlson Rd London'),
	(4, 'Maria', '5 Fredrik Rd, Bedford'),
	(5, 'Jade', '10 Copland Ave Portsmouth '),
	(6, 'Yasmine', '15 Fredrik Rd, Bedford'),
	(3, 'Jimmy', '110 Copland Ave Portsmouth');
-- @block
DELETE FROM customers WHERE customer_id = 3;
```


## SRC
- [W3schools](https://www.w3schools.com/sql/sql_datatypes.asp) 
- [W3resource](https://www.w3resource.com/mysql/mysql-data-types.php)
- [LearnSQL](https://learnsql.com/blog/understanding-numerical-data-types-sql/)
- [Microsoft](https://docs.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver16s)
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html)

- [Tutorialspoint](https://www.tutorialspoint.com/sql/index.htm)
- [Javatpoint](https://www.javatpoint.com/sql-tutorial)
- [Tutorialrepublic](https://www.tutorialrepublic.com/sql-tutorial/sql-create-database-statement.php)
- [W3Schools](https://www.w3schools.com/sql)


---
- how to choose data type for a column in database table
- python sqlalchemy
- mysql scripts
- insert into sql multiple values
- database management system
- rdbms
- sql subsets
- crud operations