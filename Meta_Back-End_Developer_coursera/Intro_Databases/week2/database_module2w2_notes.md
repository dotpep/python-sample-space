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




## Update and Delete




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


#### Update and Delete 




## SRC
- [W3schools](https://www.w3schools.com/sql/sql_datatypes.asp) 
- [W3resource](https://www.w3resource.com/mysql/mysql-data-types.php)
- [LearnSQL](https://learnsql.com/blog/understanding-numerical-data-types-sql/)
- [Microsoft](https://docs.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver16s)
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html)


---
- how to choose data type for a column in database table
- 