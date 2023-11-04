**MOCs**




## Designing database scheme

#### Definition 
Before developing a database or a software application, you firs need to plan how you will organize your data. This plan is referred to as a schema.
Schema - Organization of information and its relationships.
![[Pasted image 20231028230237.png|500]]
In the context of a MySQL database, a schema means a collection of data structures or an abstract design of how data is stored in a database.

But schema is defined in different ways across different database systems.
A schema is how data is organized in the database and how it's related to other data.
![[Pasted image 20231028230448.png|500]]

---
**Most Important two Concepts is:**
![[Pasted image 20231028230559.png|500]]

---
SQL Server schema
![[Pasted image 20231028230919.png|500]]
![[Pasted image 20231028230954.png|400]]

![[Pasted image 20231028231043.png|600]]

#### What is a database schema?
Table = Entity
Column = Field (Attributes) and each of that have own datatype.
Relationship - describe how entity related each-others. 
- one-to-one
- many-to-one
- many-to-many

first step in create database is: designing the schema or structure of a database, how data is organized and relation between entity. 

think of it as the blueprint:
![[Pasted image 20231028235431.png|400]]
![[Pasted image 20231028235547.png|400]]
![[Pasted image 20231028235652.png|400]]

Before anyone can use a database to store and manipulate data, the database schema must first be designed. This process of database schema design is also known as data modeling.
The database schema is just the skeleton of the database, and it doesn’t store any actual data.

---
A well-designed database schema makes life easier for database engineers as well as developers. It helps to:
- Maintain a clean set of data in the database related to an application. 
- Avoid reverse-engineering of the underlying data model from time to time. 
- Write efficient queries to retrieve data for reporting purposes, analytics and so on. 
In other words, it prevents you from ending up with a database design that requires a database engineer to do a lot of reverse-engineering down the line, wasting time and effort that leads to increased costs for organizations.

#### Three-schema Architecture
Three levels of schema - known as (three-schema architecture). 
It can be diagrammatically depicted like this:
![[Pasted image 20231029001540.png]]

---
Database schema can be broadly divided into three categories. 
1. Conceptual or logical schema that defines entities, attributes and relationships. 
2. Internal or physical schema that defines how data is stored in a secondary storage. In other words, the actual storage of data and access paths. 
3. External or view schema that defines different user views.

---
**Conceptual or logical schema**
- describes the structure (entire database for all the users) and in terms of entities and features of the entities and the relationships between them.
- ER-D (Entity Relationship Diagram) - drawn to represent the logical schema.
- described only at a concept level. 
![[Pasted image 20231029000657.png]]

---
**Internal or physical schema**
- represents entire database but at a very low-level.
- describes how the data is really stored on disk in the form of tables, columns and records.
- what data is stored in the database and how.
![[Pasted image 20231029000844.png]]

---
**External or view schema**
- database like an external user would want to see it
- only describes the part of the database that the specific user is interested in.
- hides the nonrelevant details of the database from a user.
- example, a user from the sales department will see only sales-related data in a database. There can be many external schemas of a single database for different users.
![[Pasted image 20231029001108.png]]


---
#### Types of database schema

**Logical database schema** - (components within a schema) how data is organized in terms of tables.
it shows what entity (tables) should be in a database, and explain how the attributes (column) of different entity are linked together.
also called (ER modeling):
![[Pasted image 20231029010007.png|500]]
![[Pasted image 20231029010226.png]]
![[Pasted image 20231029010313.png]]

---
Physical schema - (how data is stored in disk, creating actual structure of database using code) how the physical structure of a database is stored on a desk. 
![[Pasted image 20231029010605.png]]


#### Labs Simple DB designing schema

```mysql
-- @block
CREATE DATABASE shopping_cart_db;
-- @block
USE shopping_cart_db;
-- @block
CREATE TABLE customer(
	customer_id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(100), 
	address VARCHAR(255), 
	email VARCHAR(100), 
	phone VARCHAR(10), 
	PRIMARY KEY (customer_id)
);
-- @block
CREATE TABLE product(
	product_id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(100), 
	price NUMERIC(8,2), 
	description VARCHAR(255), 
	PRIMARY KEY (product_id)
);
-- @block
CREATE TABLE cart_order(
	order_id INT NOT NULL AUTO_INCREMENT, 
	customer_id INT NOT NULL, 
	product_id INT NOT NULL, 
	quantity INT, 
	order_date DATE, 
	status VARCHAR(100), 
	PRIMARY KEY (order_id), 
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id), 
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);
-- @block
SHOW columns FROM cart_order;
```


#### Building a schema
Data types, views, stored procedures, primary keys and foreign keys are also schema objects.
Basically, a database schema consists of:
- all the important data pertaining to a given scenario and their relationships, 
- unique keys for all entries and database objects, 
- and a name and data type for each column in a table.

---
**This is the logical schema or the ER-D for the scenario.**
![[Pasted image 20231029011709.png]]

---
**The physical database schema**
```mysql
-- @block
CREATE DATABASE restaurant;
-- @block
USE restaurant;
-- @block
CREATE TABLE tbl(
    table_id INT, 
    location VARCHAR(255), 
    PRIMARY KEY (table_id) 
);
-- @block
CREATE TABLE waiter(
    waiter_id INT, 
    name VARCHAR(150), 
    contact_no VARCHAR(10), 
    shift VARCHAR(10), 
    PRIMARY KEY (waiter_id)
);
-- @block
CREATE TABLE table_order(
    order_id INT, 
    date_time DATETIME, 
    table_id INT, 
    waiter_id INT, 
    PRIMARY KEY (order_id), 
    FOREIGN KEY (table_id) REFERENCES tbl(table_id), 
    FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id)
);
-- @block
CREATE TABLE customer( 
    customer_id INT, 
    name VARCHAR(100),
    NIC_no VARCHAR(12),
    contact_no VARCHAR(10),
    PRIMARY KEY (customer_id)
);
-- @block
CREATE TABLE reservation(
    reservation_id INT,
    date_time DATETIME,
    no_of_pax INT,
    order_id INT,
    table_id INT, 
    customer_id INT, 
    PRIMARY KEY (reservation_id), 
    FOREIGN KEY (order_id) REFERENCES table_order(table_id), 
    FOREIGN KEY (table_id) REFERENCES tbl(table_id), 
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
-- @block
CREATE TABLE menu(
    menu_id INT, 
    description VARCHAR(255), 
    availability INT, 
    PRIMARY KEY (menu_id) 
);
-- @block
CREATE TABLE menu_item( 
    menu_item_id INT, 
    description VARCHAR(255), 
    price FLOAT, 
    availability INT, 
    menu_id INT, 
    PRIMARY KEY (menu_item_id), 
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id) 
);
-- @block
CREATE TABLE order_menu_item( 
    order_id INT, 
    menu_item_id INT, 
    quantity INT, 
    PRIMARY KEY (order_id,menu_item_id), 
    FOREIGN KEY (order_id) REFERENCES table_order(order_id), 
    FOREIGN KEY (menu_item_id) REFERENCES menu_item(menu_item_id) 
);
```

tbl
	The first table ‘tbl’ represents a tablein the restaurant. It has a unique ID and a location – where it’s placed in the restaurant. The unique ID is the primary key of this table.
waiter
	This next table contains data about waiters who work in the restaurant. They have a unique ID, a name, their contact number and which shift they usually work. The primary key of the table is the unique ID assigned to the waiter.
table_order
	The following syntax creates the table that stores data about orders for each table. It has the order ID and table ID fields. As well as a date_time field to capture the date and time of the order and the ID of the waiter who’s supposed to serve that table, for that order.

customer
	This table stores data about customers. It has a customer ID, name, NIC number to store the National Identity Card number and the contact number fields. The primary key is the unique customer ID field.
reservation
	The reservation table associates an order with a customer. It has a unique ID, a date and time, number of guests or pax expected, the order_id, table_id and the customer_id. Its primary key is the unique reservation_id. This table is linked with the tbl, table_order and customer tables.
menu
	This menu table stores all the menus of the restaurant. It has a menu_id which is the unique field that contains descriptions of the menu and its availability.
menu_item
	Every menu can have unique menu items and these menu items are stored against the menu, in the menu_item table. A menu items also has description, price and availability fields. This table links with the menu table.
order_menu_item
	This final table captures the menu items ordered for a specific order. It has the order_id, menu_item_id and the quantity ordered. It has a composite primary key of order_id and menu_item_id field combination and its linked with the table_order and menu_item tables.

## Relational database design

#### Types of relationships
this is relationship between any two tables:
Relational model.
Types of relationships
1. one-to-many
2. one-to-one
3. many-to-many

**one-to-many** - record of data in a row of one table is linked to multiple records in different rows of another.
![[Pasted image 20231029225031.png|500]]
![[Pasted image 20231029225047.png|500]]

**one-to-one** - one single record of one table is associated with one single record of another table.
![[Pasted image 20231029225234.png|500]]
![[Pasted image 20231029225325.png|500]]

**many-to-many** - one record of one table with multiple records of another table.
![[Pasted image 20231029225509.png|500]]
![[Pasted image 20231029225525.png|500]]

---
#### Relational model
Relational model concepts:
- Data,  
- Relationships (between entities or table in database),  
- and Constraints.

**Data**
- column (attribute)
- row (record or tuple) (like object with new unique values in oop)
- datatype
	- numeric
	- string or text
	- date
- degree (is number of columns or attributes within a relation.)
- cardinality (count of row records in table)

**Relation** 
- Key (uniquely identify a specific row) (relation key)
	- Primary key
	- Foreign key
- one-to-one, one-to-many, many-to-many

**Constraints**
- every relation needs to meet three conditions: 
1. Key constraints 
	- revolves around the key attribute(s) 
	- identifier can be used to refer a record
	- must be unique and without duplicate
	- cannot have NULL values
2. Domain constraints 
	- set of acceptable values that a column is allowed to contain, depends on the data type of the column.
3. Referential integrity constraints

**Types of relationships**
1. One-to-one 
2. One-to-many 
3. Many-to-many

#### Key
- Key constraints 
	- revolves around the key attribute(s) 
	- identifier can be used to refer a record
	- must be unique and without duplicate
	- cannot have NULL values (cannot be empty)

---
Primary Key
![[Pasted image 20231029232611.png|400]]
![[Pasted image 20231029232823.png|400]]
- must make sure to choose a candidate key with a value that cannot change.

What happens if you can't locate a unique value within the table? Maybe all rows of duplicated values.
![[Pasted image 20231029232942.png|400]]
![[Pasted image 20231029233052.png|400]]
Best approach is to combine the customer ID and project code columns to create a unique value for each specific record of data

---
Foreign Key
(how to determine which customer made which order) - cusomer id column into order table column as foreign key
![[Pasted image 20231029233352.png|400]]
![[Pasted image 20231029233514.png|400]]
![[Pasted image 20231029233654.png|400]]
![[Pasted image 20231029233741.png|400]]
![[Pasted image 20231029233952.png|400]]

---
some practice: 
```mysql
-- @block
CREATE DATABASE automobile;
-- @block
CREATE TABLE vehicle(
	vehicle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	owner_id INT, 
	plate_number VARCHAR(10), 
	phone_number TINYINT(10)
);
-- @block
CREATE TABLE owner(
	owner_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	owner_name VARCHAR(50), 
	owner_address VARCHAR(255)
);
-- @block
ALTER TABLE vehicle 
MODIFY owner_id INT NOT NULL;
-- @block
SHOW columns FROM vehicle;
SHOW columns FROM owner;
-- @block
ALTER TABLE vehicle 
ADD FOREIGN KEY (owner_id) REFERENCES owner(owner_id);
-- @block
SHOW columns FROM vehicle;
```
- PRI comes from primary; this means it’s a primary key. 
- UNI comes from unique; this means it’s a unique key. 
- MUL comes from multiple. If the key is MUL, it means that the related column is permitted to contain the same value in multiple cells of that column.

---
#### Entity and attribute
![[Pasted image 20231030001551.png|400]]
![[Pasted image 20231030001716.png|400]]

Attribute types in RDBMS:
- Simple attribute
- Composite attribute
- Single value attribute
- Multi value attribute
- Derived attribute
- Key attribute
![[Pasted image 20231030002534.png]]





## Database normalization
![[Pasted image 20231102025802.png|400]]
Normalization optimizes the database design by creating a single purpose for each table.
![[Pasted image 20231102030914.png|600]]
- First Normal Form (1NF)   
- Second Normal Form (2NF)   
- Third Normal Form (3NF)

Normalization is progressive process.
![[Pasted image 20231103003129.png|500]]

---
database without Normalization:
![[Pasted image 20231102030028.png|600]]
Database normalization challenges:
- Insert anomaly (Insertion of one record leads to the insertion of several more required data sets.)
- Update anomaly (Updating a record in a table column requires further updated in other columns)
- Deletion anomaly (Deletion of one record leads to the deletion of several more required data sets)

---
Unnormalized table:
- Example includes fictitious data required by a Medical Group Surgery based in London to generate relevant reports. Doctors work in multiple regions and various councils in London. And once patients book an appointment, they are given a slot ID at their local surgery. There might be multiple surgeries in the same council but with different postcodes, where one or more councils belong to a particular region. For example, East or West London.
![[Pasted image 20231102163818.png|600]]
```mysql
CREATE TABLE Surgery 
    (DoctorID VARCHAR(10), 
    DoctorName VARCHAR(50), 
    Region VARCHAR(20), 
    PatientID VARCHAR(10), 
    PatientName VARCHAR(50), 
    SurgeryNumber INT, 
    Council VARCHAR(20), 
    Postcode VARCHAR(10), 
    SlotID VARCHAR(5), 
    TotalCost Decimal
);
```

---

#### 1NF
Data atomicity rule - means you can only have one single instance value of the column attribute in any table cell
![[Pasted image 20231103001530.png|600]]
![[Pasted image 20231103001544.png|600]]
Instances of repeated data can cause data redundancy and inconsistency.

Atomicity - requires that all values be atomic (not shared), each attribute (column) has a unique name, and all record (rows) are unique (without duplication records and Primary key).

step 1:
```mysql
CREATE TABLE Patient(
	PatientID VARCHAR(10) NOT NULL, 
	PatientName VARCHAR(50), 
	SlotID VARCHAR(10) NOT NULL,
	TotalCost Decimal,
	CONSTRAINT PK_Patient PRIMARY KEY (PatientID, SlotID)
);
```
`CONSTRAINT PK_Patient PRIMARY KEY (PatientID, SlotID)` - patient ID and Slot ID, to identify each record uniquely as composite Primary Key.
![[Pasted image 20231102232452.png|400]]

step 2:
- Separating the table into two tables of data (doctor and surgery):
![[Pasted image 20231102232643.png|400]]

doctor table:
```mysql
CREATE TABLE Doctor(
	DoctorID VARCHAR(10),
	DoctorName VARCHAR(50), 
	PRIMARY KEY (DoctorID)
);
```

surgery table:
```mysql
CREATE TABLE Surgery(
	SurgeryNumber INT NOT NULL,
	Region VARCHAR(20), 
	Council VARCHAR(20), 
	Postcode VARCHAR(10), 
	PRIMARY KEY (SurgeryNumber));
```

![[Pasted image 20231102233056.png|400]]

---
#### 1NF step-by-step (Data atomicity)
1) unnormalized 
![[Pasted image 20231103001902.png|500]]
2) creating new row for each number
![[Pasted image 20231103002106.png|500]]
3) Primary Key is not unique
![[Pasted image 20231103002212.png|500]]
4) creating two columns for contact numbers
![[Pasted image 20231103002328.png|500]]
5) issue repeated data
![[Pasted image 20231103002412.png|500]]
6) identify repeating data, identify entities (column: Course name and Tutor name), redesign (slice into two entity)
![[Pasted image 20231103002704.png|500]]
7) link between two entity (relation)
![[Pasted image 20231103002840.png|500]]

#### 2NF
Must avoid Partial Dependency in relationship between data.
![[Pasted image 20231103003244.png|600]]
![[Pasted image 20231103004219.png|500]]

Partial Dependency - refers to table with a composite Primary Key. Namely a key that consists of a combination of two or more columns, where a non-key attribute value depends only on one part of the composite key.
![[Pasted image 20231102234019.png|400]]
Non-key attributes depend on one part of the composite key. 
- patient's name is a non-key attribute, and it can be determined by using the Patient ID only.
- you can determine the total cost by using the Slot ID only.

fixed by splitting patient table into two tables (patient and appointment):
![[Pasted image 20231102234226.png|600]]

patient table:
```mysql
CREATE TABLE Patient(
	PatientID VARCHAR(10) NOT NULL,
	PatientName, VARCHAR(50), 
	PRIMARY KEY (PatientID)
);
```

appointment table:
```mysql
CREATE TABLE Appointments(
	AppointmentID INT NOT NULL,
	SlotID, VARCHAR(10),
	TotalCost Decimal,
	PRIMARY KEY (AppointmentID)
);
```

#### 2NF step-by-step (Functional dependency, Partial dependency)
Functional dependency:
![[Pasted image 20231103003244.png|600]]
0) dependence between primary and non-primary key attribute
![[Pasted image 20231103003537.png|500]]
1) i can't find date of birth for specific student (because it has duplicated name and date of birth values) this means:
![[Pasted image 20231103004025.png|500]]

Partial dependency:
![[Pasted image 20231103004219.png|500]]
0) composite primary key (and dependence between attribute)
![[Pasted image 20231103004403.png|600]]
1) define dependence
![[Pasted image 20231103004744.png|600]]
2) split into three entity
![[Pasted image 20231103004959.png|600]]

#### 3NF
Must already be in the Second Normal Form (2NF).
Transitive Dependency - means that any non-key attribute in surgery table may not be functionally dependent on another non-key attribute in the same table.
![[Pasted image 20231103005552.png|600]]

In the surgery table, the postcode and the council are non-key attributes, and the postcode depends on the council. Therefore, if you change the council value, you must also change the postcode. This is called transitive dependency, which is not allowed in the third normal form.
![[Pasted image 20231102235559.png|600]]
In other words, changing the value of the council value in the above table has a direct impact on the postcode value, because each postcode in this example belongs to a specific council.

split into two tables(location, council):

location table:
```mysql
CREATE TABLE Location(
	SurgeryNumber INT NOT NULL,
	Postcode VARCHAR(10), 
	PRIMARY KEY (SurgeryNumber)
);
```

council table:
```mysql
CREATE TABLE Council(
	Council VARCHAR(20) NOT NULL,
	Region VARCHAR(20),
	PRIMARY KEY (Council)
);
```

---
#### 3NF step-by-step (Transitive Dependency)
- Solve repetitive data.
![[Pasted image 20231103005552.png|600]]
0) value of A determines value of B, value of B determines value of C. (this is dependence between non-key attribute)
![[Pasted image 20231103005806.png|600]]
1) non-key depends 
- Language determines Country and Country determines Language
![[Pasted image 20231103010051.png|600]]
2) split to two entity
![[Pasted image 20231103010524.png|600]]
- non-key attribute determined only by primary key 
![[Pasted image 20231103010610.png|600]]



#### Stages of Database Normalization
- 1nf
- 2nf
- 3nf
![[Pasted image 20231103000146.png]]
![[Pasted image 20231103001316.png]]

## lab Database schema design
Step 1: Define the database purpose.  
Step 2: Identify the database tables including 
- Tables attributes 
- Attributes data types 
- Primary key for each table  
Step 3: Create relationships between tables

|Table name|Description|Diagram|
|---|---|---|
|Employees|The employee table stores the data of all employees. The diagram presents 8 attributes with relevant datatypes. Employee ID is the primary key in this table.|1|
|Customers|The customer table stores customers data. <br><br>In the diagram, 8 attributes with relevant datatypes are presented. <br><br>Customer ID is the primary key in this table.|2|
|Invoices|The invoice table stores data on invoices.<br><br>In the diagram, 5 attributes with relevant datatypes are presented.<br><br>Invoice ID is the primary key in this table.|3|
|Artists|The artist table stores data on artists. <br><br>Only 2 attributes, the artist ID and artist name, are presented in the diagram alongside their relevant data types.<br><br>Artists ID is the primary key in this table.|4|
|Albums|The album table stores data about a list of tracks. <br><br>In the diagram, 3 attributes with relevant data types are presented. <br><br>Album ID is the primary key in this table.|5|
|Tracks|The tracks table stores the data of songs. <br><br>In the diagram there are 5 attributes with relevant data types. <br><br>Tracks ID is the primary key in this table.|6|


---
![[Pasted image 20231103013246.png]]

```mysql
CREATE DATABASE Chinook;
-- @block
CREATE TABLE employee(
	employee_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	last_name VARCHAR(20),
	first_name VARCHAR(20),
	title VARCHAR(30),
	reports_to INT,
	birth_date DATE,
	hire_date DATE,
	address VARCHAR(70)
);
-- @block
CREATE TABLE customer(
	customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	last_name VARCHAR(20),
	first_name VARCHAR(20),
	company VARCHAR(30),
	phone VARCHAR(20),
	email VARCHAR(100),
	address int(70),
	suppert_rep_id INT,
	FOREIGN KEY (suppert_rep_id) 
	REFERENCES employee(employee_id)
);
-- @block
CREATE TABLE location(
	location_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	country VARCHAR(40),
	city VARCHAR(50)
);
-- @block
CREATE TABLE artists(
	artist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(120),
	location_id INT,
	FOREIGN KEY (location_id)
	REFERENCES location(location_id)
);
-- @block
CREATE TABLE albums(
	album_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	title VARCHAR(160),
	artist_id INT,
	FOREIGN KEY (artist_id)
	REFERENCES artists(artist_id)
);
-- @block
CREATE TABLE tracks(
	track_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(200),
	unite_price DECIMAL,
	album_id INT,
	FOREIGN KEY (album_id) 
	REFERENCES albums(album_id)
);
-- @block
CREATE TABLE invoices(
	invoice_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	invoice_date DATE,
	billing_address VARCHAR(100),
	customer_id INT,
	track_id INT,
	FOREIGN KEY (customer_id) 
	REFERENCES customer(customer_id),
	FOREIGN KEY (track_id) 
	REFERENCES tracks(track_id)
);
```

---
improvement:
```mysql
ALTER TABLE customer
ADD country VARCHAR(50);
-- @block
ALTER TABLE invoices
DROP COLUMN track_id;
-- @block
CREATE TABLE invoice_items(
	invoice_item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	invoice_id INT,
	track_id INT,
	FOREIGN KEY (invoice_id) 
	REFERENCES invoices(invoice_id),
	FOREIGN KEY (track_id) 
	REFERENCES tracks(track_id)
);
```
![[Pasted image 20231103020735.png]]

---
original Chinook database schema:
![[Pasted image 20231103013410.png]]

## Function

```mysql
SELECT version();
-- check version
SELECT count(*) FROM table_name;
-- count of column * from table
```

## w5 Final Assignment 

```mysql
CREATE DATABASE SportsClub;
-- @block
CREATE TABLE Players (playerID INT, playerName VARCHAR(50), age INT, PRIMARY KEY(playerID));
-- @block
INSERT INTO Players (playerID, playerName, age) VALUES (1, "Jack", 25);
-- @block
SELECT playerName FROM Players WHERE playerID = 2;
-- @block
INSERT INTO Players (playerID, playerName, age) VALUES (2, "Karl", 20), (3, "Mark", 21), (4, "Andrew", 22);
SELECT playerName FROM Players WHERE playerID = 2;
-- @block
SELECT playerName FROM Players;
-- @block
UPDATE Players SET age = 22 WHERE playerID = 3;
-- @block
DELETE FROM Players WHERE playerID = 4;
-- @block
SELECT PlayerID % 2 = 0 FROM Players;
-- @block
SELECT * FROM Players WHERE PlayerID % 2 = 0;
-- incorrect
SELECT PlayerID, Name, CASE WHEN PlayerID % 2 = 0 THEN 'Even' ELSE 'Odd' END AS OddOrEven FROM Players;
-- incorrect
SELECT Name FROM Players WHERE age > 25;
-- @block
FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
```

## SRC
- [Prisma](https://www.prisma.io/dataguide/intro/intro-to-schemas
- [Lucidchart](https://www.lucidchart.com/pages/database-diagram/database-schema)
- [Educative](https://www.educative.io/blog/what-are-database-schemas-examples)
- [IBM](https://www.ibm.com/cloud/learn/database-schema)

- [Opentextbc1](https://opentextbc.ca/dbdesign01/chapter/chapter-8-entity-relationship-model/)
- [IBM](https://www.ibm.com/docs/en/ida/9.1.1?topic=entities-primary-foreign-keys)
- [Scaler](https://www.scaler.com/topics/dbms/relational-model-in-dbms/)
- [Oracle](https://www.oracle.com/database/what-is-a-relational-database/)

- [Database Design – 2nd Edition](https://opentextbc.ca/dbdesign01/chapter/chapter-12-normalization/)
- [Database Normalization](https://www.databasestar.com/database-normalization/)
- [Anomalies](https://www.bbc.co.uk/bitesize/guides/zc93tv4/revision/2)

---
research:
- database designing
- [Database Design Course - Learn how to design and plan a database for beginners - YouTube](https://www.youtube.com/watch?v=ztHopE5Wnpc)
- database server
- key in rdbms  
- difference between sql and rdbms or nosql and dbms
- nosql vs sql vs mongodb
- [Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF - YouTube](https://www.youtube.com/watch?v=GFQaEYEc8_8)
- er model
- designing database schema

- how to design er diagram (and types of relationships between entity)
- [MySQL Joins (w3schools.com)](https://www.w3schools.com/mysql/mysql_join.asp)
- sql joins
- database domain terms meaning
- database index terms meanings

- chinook schema [lerocha/chinook-database: Sample database for SQL Server, Oracle, MySQL, PostgreSQL, SQLite, DB2 (github.com)](https://github.com/lerocha/chinook-database)
- [drawsql.app chinook schema](https://drawsql.app/teams/test-team1-2/diagrams/chinook-schema-design-6-main-entity)

- - [MySQL Constraints (w3schools.com)](https://www.w3schools.com/mysql/mysql_constraints.asp)
- acid in database
- mongodb
- click house and redis (for cache)
- python orm sqlalchemy (async)
- setup sql server in ubuntu

- [MySQL Functions (w3schools.com)](https://www.w3schools.com/mysql/mysql_ref_functions.asp)
- sql custom script
- sql custom functions
- sql dcl and tcl subsets how to setup prefix and access

- mysql online compiler
- drawsql
- sqlalhemy and django, fastapi

- [Основы SQL - YouTube](https://www.youtube.com/playlist?list=PLtPJ9lKvJ4oh5SdmGVusIVDPcELrJ2bsT)
- [Базы данных - Listen IT (YouTube playlist)](https://youtube.com/playlist?list=PLLACapFZr4XvyQgxZaIOK-MJwblGVCL41&si=oHRmcVGjsvfrAr8S)
- [ЧТО КАЖДЫЙ ПРОГРАММИСТ ДОЛЖЕН ЗНАТЬ ПРО БАЗЫ ДАННЫХ - YouTube](https://www.youtube.com/watch?v=jcsG-IlJ-SA)
- [Курс SQL. Базы данных. ORACLE - YouTube](https://www.youtube.com/playlist?list=PLv8UEsK35VB8ju8Vr9WeO71F7SCRofJis)
- [Базы данных - YouTube](https://www.youtube.com/playlist?list=PL8cnOJKrvuSNBNvp5sLmiMNVe1djg6VFJ)

- [IBM Back-End Development Professional Certificate | Coursera](https://www.coursera.org/professional-certificates/ibm-backend-development?)
- [MySQL - The Basics // Learn SQL in 23 Easy Steps - YouTube](https://www.youtube.com/watch?v=Cz3WcZLRaWc)


- [List of English words for Spaced Repetition](https://translate.google.com/?source=gtx&sl=en&tl=ru&text=mandatory%2C%0Aretrieve%2C%0Atransmitted%2C%0Ainternal%2C%0Aordinary%2C%0Afurther%2C%0Adeclaration%2C%0Aobtains%2C%0Aensure%2C%0Atoward%2C%0Asubmitted%2C%0Ainvoked%2C%0AAdditionally%2C%0AInternal%2C%0Ahandle%2C%20handler%2C%20handling%2C%0Aexception%2C%0Aalign%2C%0Afurther%2C%20%0Aoverriding%2C%0A403%20permission%20denied%2C%0Arecall%2C%0Aimplementing%2C%0Ainheritance%2C%0Ainstance%2C%20%0Aconvenient%20%2C%0AIntegrity%20constraints%2C%0Adomain%2C%0Aconstraints%2C%0Aimplemented%2C%0Aestablished%2C%0Aaccordingly%2C%0Ainstance%2C%0Ainvoices%20%2C%0Aquantity%2C%0Afictitious%2C%0Aservice%20fee%2C%0Ablank%2C%0Acapstone%2C%0Acrucial%2C%0Aconstraints%2C%0ACardinality%2C%0ALikewise%2C%0Apurchase%2C%0APrimary%2C%0Asurgery%2C%0Adepicted%2C%0Areduce%2C%0APartially%2C%0Aconforms%2C%0A%0A%0A%0Aenormous%2C%0Apipeline%2C%0Ainsufficient%2C%0Acertainly%2C%0Awithin%20a%20database%2C%0Ain%20an%20existing%20database%2C%0Aexciting%2C%0Aestablish%2C%0Aoverwhelming%2C%0Aaccomplish%2C%0Atowards%2C%0Adedicate%2C%0Aensure%2C%0Aconsists%20of%2C%0Acrucial%2C%0Aspreedsheed%2C%0Atake%20suitable%20actions%2C%0Arevenue%2C%0Awhole%20pie%2C%0Aserves%20your%20purpose%2C%0Aappropriate%2C%0Asuitable%2C%0Aassessed.%0Aemerging%2C%0AHierarchical%2C%0Acomperhensive%2C%0Aallowance%2C%0Asatisfy%20specified%2C%0Aassume%2C%0Afetch%2C%0Ablueprint%2C%0Acover%2C%0Apermit%2C%0Abroadly%2C%0Adistinguish%2C%0Aexamine%2C%0Aconceptual%2C%0Aestablishing%2C%0Aexecute%2C%0AWhereas%2C%0Acrucial%2C%0Astraight%2C%0ADeletion%2C%0A%0A%0A%0A%0Aprimary%20key%2C%0Aforgein%20key%2C%0Aentity%2C%0Aquantity%2C%0A%0Acolumn%2C%20%0Arow%2C%0Akey%20value%2C%0ACharts%2C%0Avolume%2C%0Asemi%2C%0Aentity%2C%0Adecimal%2C%0AViolation%2C%0Aparentheses%2C%0Asemicolon%2C%0Aclause%2C%0Abitwise%2C%0Amodulo%2C%0Aoperand%2C%0Aremainder%2C%0Aodd%20and%20even%2C%0Ainclude%20and%20exclude%2C%0ADeduct%2C%0Aascending%20and%20descending%2C%0Aclause%2C%0APartial%20dependency%2C%0Adetermines%2C%0A%0A%0A%0A%0A%0A%0A%0Arest%20of%20my%20life%2C%0A%0A&op=translate)

---
work in phpmyadmin:
- [phpMyAdmin - Downloads](https://www.phpmyadmin.net/downloads/)
- [How To Install phpMyAdmin On Windows - YouTube](https://www.youtube.com/watch?v=dnBa2pTKYY0)
- [MySQL - phpMyAdmin - Урок 1 - Установка и начало работы - YouTube](https://www.youtube.com/watch?v=OSjR8wwaf5Y)
- [Установка и настройка phpMyAdmin. - YouTube](https://www.youtube.com/watch?v=-di9u9H6pzM)
- xampp
- 

---
postgresql
- 

---
sqlite
- 

---
sqlalchemy orm python
- 


