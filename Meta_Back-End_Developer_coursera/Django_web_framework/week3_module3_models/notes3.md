## Models & Migrations
Model(MVT architecsture django) in application tier and work with data tier (modular classes and methods to perform CRUD operations).
![[Pasted image 20231104170114.png|500]]

work with database may achieved in two ways:
1. work directly with database using custom SQL CRUD operation:
![[Pasted image 20231104170609.png|400]]
2. use framework (in Django) (crud in models)
![[Pasted image 20231104170722.png|400]]
![[Pasted image 20231104170907.png|400]]
![[Pasted image 20231104171026.png|400]]
2. use framework (like sqlalchemy orm's) 

---
![[Pasted image 20231104171218.png|600]]
in django - no need to define primary key (automatically adds, and you can override it if needed)

==You cannot create a database table by only defining a model class in Python. To complete you need to use something called Migrations.==

#### CRUD using django Model

**Create**
![[Pasted image 20231104171619.png|500]]
(requires create new object from class user and persisted using save function)

**Read**
![[Pasted image 20231104171750.png|500]]
(bound user objects)

**Update**
![[Pasted image 20231104172015.png|500]]
(use get and save methods) (check if a user exists with id = 1 and than update last_name = Smith)

**Delete**
![[Pasted image 20231104172259.png|500]]
(use delete method)

==Highlights==
- Each attribute of the model represents a field in the database table.
- Each model maps to a single database table.
- A model contains the essential fields and behaviors of the data you’re storing.

![[Pasted image 20231104172521.png|300]]

#### Model Relationships 
in relational database each table or entity represents one column or attribute with unique vale for each rows or records as known Primary Key.
if Primary Key of one table appears as one of fields in another table while having own primary key it becomes Foreign Key.

in designing related database table:
- avoid **data redundancy** unnecessary repetition of the same data in many rows
- ensure **data integrity**

---
**Types of Relationships**
- One-to-One,
- One-to-Many, 
- Many-to-Many.

---
##### **One-to-One relationship**
we have: college and principal model or entity (table), that one person can be a principal of only one college.

college:
```python
class College(models.Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField()
```

principal:
```python
class Principal(models.Model): 
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
```

In Principal model, `CollegeID` field is foreign key. 
The `on_delete` option specifies the behavior in case the associated object in the primary model is deleted.
- **CASCADE:** deletes the object containing the `ForeignKey`
- **PROTECT:** Prevent deletion of the referenced object.
- **RESTRICT:** Prevent deletion of the referenced object by raising `RestrictedError`
`on_delete` property in the `ForeignKey` field determines the action to take if the corresponding primary key in the related table is deleted.

- using `model.OneToOneField` for define foreign key (One-to-One relationship).

- `PrimaryKey` of principal model is automatically adds.
`class College(models.Model):` - in this syntax we using `import django` and specify `models` (inheritance django class method like save(), create() and so on. working with database) for use Django ORM 

---
SQL query (run migration on these models equivalent SQL queries). 
college:
```sql
CREATE TABLE "myapp_college"(
	"CollegeID" integer NOT NULL PRIMARY KEY, 
	"name" varchar(50) NOT NULL,
	"strength" integer NOT NULL,
	"website" varchar(200) NOT NULL);
```
principal:
```sql
CREATE TABLE "myapp_principal"(
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"Qualification" varchar(50) NOT NULL, 
	"email" varchar(50) NOT NULL,
	"CollegeID_id" integer NOT NULL 
	UNIQUE REFERENCES "myapp_college" ("CollegeID") 
	DEFERRABLE INITIALLY DEFERRED
);
```


---
##### **One-to-Many relationship**
we have: teacher and subject model, teacher is qualified to teach a subject but there can be more one teacher in college who teaches the same subject. 

teacher:
```python
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = model.IntegerField()
```

subject:
```python
class Teacher(models.Model): 
    TeacherID = models.ItegerField(primary_key=True) 
    subjectcode = models.ForeignKey( 
                Subject,  
                on_delete=models.CASCADE 
                  ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
```

- Teacher model has its own primary key. It has a `ForeignKey` relating this model with the subject model.
- using `model.ForeignKey` for define foreign key (One-to-Many relationship)

---
SQL query (run migration on these models equivalent SQL queries). 
subject:
```sql
CREATE TABLE "myapp_subject"(
	"Subjectcode" integer NOT NULL PRIMARY KEY, 
	"name" varchar(30) NOT NULL, 
	"credits" integer NOT NULL, 
	"Qualification" varchar(50) NOT NULL, 
	"email" varchar(50) NOT NULL
);
```
teacher:
```sql
CREATE TABLE "myapp_teacher"(
	"TeacherID" integer NOT NULL PRIMARY KEY, 
	"Qualification" varchar(50) NOT NULL, 
	"email" varchar(50) NOT NULL, 
	"subjectcode_id" integer NOT NULL 
	REFERENCES "myapp_subject" ("Subjectcode") 
	DEFERRABLE INITIALLY DEFERRED
);
```
index:
```sql
CREATE INDEX "myapp_teacher_subjectcode_id_bef86dea" 
ON "myapp_teacher" ("subjectcode_id");
```


##### **Many-to-Many relationship**
we have: teacher and subject, if more than one teacher can teach the same subject, a single teacher can teach more than one subject.
- Django implements this with a Many-to-Many Field type.

teacher:
```python
class Teacher(models.Model): 
    TeacherID = models.ItegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
```
subject:
```python
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = model.IntegerField() 
    teacher = model.ManyToManyField(Teacher)
```

- using `model.ManyToManyField` for define foreign key (Many-to-Many relationship).

---
When the migrations are done, the following SQL queries will be executed to establish a many-to-many relationship.

SQL query (run migration on these models SQL query (run migration on these models). ). 
teacher:
```sql
CREATE TABLE "myapp_teacher"(
	"TeacherID" integer NOT NULL PRIMARY KEY, 
	"Qualification" varchar(50) NOT NULL, 
	"email" varchar(50) NOT NULL
);
```
subject:
```sql
CREATE TABLE "myapp_subject"(
	"Subjectcode" integer NOT NULL PRIMARY KEY, 
	"name" varchar(30) NOT NULL, 
	"credits" integer NOT NULL
);
```
subject and teacher:
```sql
CREATE TABLE "myapp_subject_teacher"(
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"subject_id" integer NOT NULL 
	REFERENCES "myapp_subject" ("Subjectcode") 
	DEFERRABLE INITIALLY DEFERRED, 
	"teacher_id" integer NOT NULL 
	REFERENCES "myapp_teacher" ("TeacherID") 
	DEFERRABLE INITIALLY DEFERRED
);
```
unique index:
```sql
CREATE UNIQUE INDEX "myapp_subject_teacher_subject_id_teacher_id_9b6a3c00_uniq" 
ON "myapp_subject_teacher" ("subject_id", "teacher_id");
```
index 1:
```sql
CREATE INDEX "myapp_subject_teacher_subject_id_e87c76e7" 
ON "myapp_subject_teacher" ("subject_id");
```
index 2:
```sql
CREATE INDEX "myapp_subject_teacher_teacher_id_359f8cce" 
ON "myapp_subject_teacher" ("teacher_id");
```

##### SQL syntax and Model methods explanation
`models.OneToOneField` - for one-to-one relationships
`models.ForeignKey` -  for many-to-one relationships
`models.ManyToManyField` -  for many-to-many relationships

---
```шаг за шагом почему мы используем: 
1. создаем "myapp_subject_teacher" 
2. используем DEFERRABLE INITIALLY DEFERRED 
3. CREATE UNIQUE INDEX 
4. CREATE INDEX
```

1. **Создание `myapp_subject_teacher`**: Эта таблица создается для отслеживания связей между учителями и предметами. В реальном мире один учитель может преподавать несколько предметов, и один предмет может быть преподан несколькими учителями. Это называется отношением `многие ко многим`. В базах данных такие отношения обычно моделируются с помощью отдельной таблицы, которая содержит внешние ключи, ссылающиеся на связанные таблицы.
2. **Использование DEFERRABLE INITIALLY DEFERRED**: Это означает, что проверка внешних ключей будет отложена до конца транзакции. Это может быть полезно, если вы хотите вставить данные в несколько связанных таблиц в одной транзакции.
3. **CREATE UNIQUE INDEX**: Этот индекс гарантирует, что каждая пара учитель-предмет в таблице `myapp_subject_teacher` уникальна. Это предотвращает дублирование связей между учителями и предметами.
4. **CREATE INDEX**: Эти индексы создаются для ускорения поиска по полям `subject_id` и `teacher_id`. Когда вы создаете индекс для поля, база данных создает структуру данных (например, B-дерево), которая позволяет быстро находить строки по значению этого поля.

```
хочешь сказать когда мы хотим создать связь многие к многим мы должны создать отдельную таблицу для отслеживание связи многие к многим?
```

- Когда мы хотим создать связь `многие ко многим` между двумя таблицами в базе данных, мы обычно создаем третью таблицу, которую иногда называют `таблицей связей` или `таблицей перекрестных ссылок`.
- Эта таблица содержит внешние ключи, которые ссылаются на первичные ключи каждой из связанных таблиц. Каждая строка в этой таблице связей представляет уникальную связь между строками в двух других таблицах.
- В вашем примере таблица `myapp_subject_teacher` является такой таблицей связей, которая отслеживает связи между учителями и предметами. 


#### Creating models

`djago-admin startproject menuproject` - create project and `cd to/project`
`python manage.py startapp menuapp` - create app

1. add project settings.py line: `INSTALLED_APPS = menuapp.apps.MenuappConfig`
2. make migration
	- `python manage.py makemigrations`
	- `python manage.py migrate`
3. `python manage.py shell`
4. import your class into shell: `from menuapp.models import Menu`
5. returns all entries in database - `Menu.objects.all()` | it returns: `<QuerySet []>`
6. assigned this entry to an object m: `m = Menu.objects.create(name = 'pasta', cuisine = 'italian', price = 10)` | it returns:  `<QuerySet [<Menu: Menu object (1)>]>`
7. `n = Menu.objects.create(name = 'taco', cuisine = 'mexican', price = 2)`
8. create custom method (Dunder method prints a string)
```python
def __str__(self):
        return self.name + " : " + self.cuisine
```
9. update:
	- `p = Menu.objects.get(pk=2)`
	- `p.cuisine = 'chinese'`
	- `p.save()`
	- `Menu.objects.all()`
	- it returns: `<QuerySet [<Menu: pasta : italian>, <Menu: taco : chinese>]>`


```python
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    # django custom method - str represents a Dunder method prints a string
    def __str__(self):
        return self.name + " : " + self.cuisine
```


#### Migrations
migrations using for implements changes (our common task: alter the data model of application - add new columns like email in class model).
Use to changes to models.

django support rdbms (PostgreSQL, MySQL, SQLite). 
django in model CRUD operation made possible by using Object Relational Mapper (ORM).
![[Pasted image 20231104195243.png|500]]
![[Pasted image 20231104195313.png|300]]

adding new attribute will add a new column 
`city = models.CharField(max_length=30)` into `class User` module or table (entity).
![[Pasted image 20231104195559.png|300]]

---
Rename column and Delete model works with Migrations:
![[Pasted image 20231104195720.png|500]]
![[Pasted image 20231104195749.png|400]]

SQL:
![[Pasted image 20231104195827.png|500]]

Django ORM:
![[Pasted image 20231104195910.png|500]]

![[Pasted image 20231104200036.png|500]]
migration script:
- set of instructions
- apply and run
- No SQL syntax required

migration plus compare to SQL query:
- syncing (issues)
- version control (keeps history, tracks changes, remove problems, centralized)
- maintenance 

Good think about Migration like: version control system for your database schema.
![[Pasted image 20231104200748.png|500]]
![[Pasted image 20231104201032.png|500]]

#### How to use migrations (version control command)
django migrations command:
- `makemigrations`
- `migrate`
- `sqlmigrate`
- `showmigrations`

Django’s migration is a way to track and apply changes in the database models.
- `makemigrations` creates a script for each change detected by Django.
- `migrate` executes the script to update the database.

---
```python
class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
```

`python manage.py makemigrations`
Migration script 0001_initial.py (app/migrations). 
It indicates what script intends to do, which is: Create model Person.
- As mentioned, you need to run the `migrate` command to apply the tasks in the `migrations` file to be performed.
`python manage.py migrate`
![[Pasted image 20231104224825.png|600]]

---
##### Version Control
modify person class:
```python
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
```

`python manage.py makemigrations`
![[Pasted image 20231104225204.png|600]]

add new column age:
```python
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
```

`python manage.py showmigrations`
![[Pasted image 20231104230047.png|600]]

migrate:
```shell
>>> python manage.py migrate  
<<<      
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying myapp.0002_rename_name_person_person_name... OK
  Applying myapp.0003_person_age... OK
```

fall back upon table structure before adding `age` field:
```shell
>>> python manage.py migrate myapp 0002_rename_name_person_person_name
<<<
Operations to perform:
  Target specific migration: 0002_rename_name_person_person_name, from myapp
Running migrations:
  Rendering model states... DONE
  Unapplying myapp.0003_person_age... OK
```

show SQL query executed when certain migration script is run:
```shell
>>> python manage.py sqlmigrate myapp 0001_initial BEGIN;
<<<
BEGIN;
--
-- Create model Person
--
CREATE TABLE "myapp_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(20) NOT NULL, "email" varchar(254) NOT NULL, "phone" varchar(20) NOT NULL);
COMMIT;
```

---
![[Pasted image 20231104231553.png|500]]
![[Pasted image 20231104232007.png|500]]

##### Practice version control command
some practice in migration:
1. `python manage.py startapp myapp2`
2. 
```python 
class MenuItems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()
```
3. in project settings.py: `INSTALLED_APPS = ['myapp', 'myapp2.apps.Myapp2Config',]`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. 
```python
class MenuItems(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()
```
7. `python manage.py makemigrations`
8. `python manage.py showmigrations`
```shell
myapp
 [X] 0001_initial
 [X] 0002_rename_name_person_person_name
 [X] 0003_person_age
myapp2
 [X] 0001_initial
 [ ] 0002_rename_course_menuitems_category
 [ ] 0003_rename_name_menuitems_item_name
```
- X symbol represents the commits to the migrations.
9. `python manage.py migrate myapp2 0001 --plan`
```shell
Planned operations:myapp2.0003_rename_name_menuitems_item_name
    Undo Rename field name on menuitems to item_namemyapp2.0002_rename_course_menuitems_category
    Undo Rename field course on menuitems to category
```
10. `python manage.py migrate myapp2 0001`
```shell
Operations to perform:
  Target specific migration: 0001_initial, from myapp2
Running migrations:
  Rendering model states... DONE
  Unapplying myapp2.0003_rename_name_menuitems_item_name... OK
  Unapplying myapp2.0002_rename_course_menuitems_category... OK
```
11. `python manage.py sqlmigrate myapp2 0003`
```shell
BEGIN;
--
-- Rename field name on menuitems to item_name
--
ALTER TABLE "myapp2_menuitems" RENAME COLUMN "name" TO "item_name";
COMMIT;
```

##### History of changes
![[Pasted image 20231104233455.png|600]]
![[Pasted image 20231104233440.png|400]]
- make changes in the model
- apply the migration scripts

![[Pasted image 20231104233655.png|400]]
![[Pasted image 20231104233757.png|500]]
This is after the command make migrations, but before the command migrate.

![[Pasted image 20231104234818.png|500]]

`migrations.method`:
![[Pasted image 20231104234942.png|500]]
![[Pasted image 20231104235014.png|500]]

#### labs 1
models.py
```python
from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
```
admin.py:
```python
from django.contrib import admin

# Register your models here.
from .models import Drinks

admin.site.register(Drinks)
```

- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `drink_name = models.CharField(max_length=200)`
- `python3 manage.py showmigrations`
```shell
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
contenttypes
myapp
 [X] 0001_initial
 [X] 0002_rename_drink_drinks_drink_name
sessions
 [X] 0001_initial
```
![[Pasted image 20231105001231.png|400]]

#### Models using Foreign Key
![[Pasted image 20231105001603.png|600]]

**One-To-Many:**
1. app/models.py
```python
from django.db import models

# Create your models here.
# Menu Category
# Menu

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    prcie = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        default=None)
```
2. project/settings.py 
`INSTALLED_APPS = ['myapp.apps.MyappConfig',]`
3. app/admin.py
```python
from django.contrib import admin

# Register your models here.
from .models import Menu, MenuCategory

admin.site.register(Menu)
admin.site.register(MenuCategory)
```
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. add new records in table (model):
- shell:
```shell
>>> python manage.py shell
>>> from myapp.models import MenuCategory
>>> MenuCategory.objects.create(menu_category_name='Italian')
>>> MenuCategory.objects.create(menu_category_name='Greek')
>>> MenuCategory.objects.create(menu_category_name='Turkish')
>>> MenuCategory.objects.all()
```
- class MenuCategory:
```python
def __str__(self):
	return "pk: " + str(self.id) + " menu_category_name: " + self.menu_category_name
```
- class Menu:
```python
def __str__(self):
	return "pk:" + str(self.id) + " menu_item: " + self.menu_item + " price: " + str(self.price) + " category_id(foreign key): " + str(self.category_id.id)
```
- add records in class Menu:
```python
from myapp.models import Menu, MenuCategory

# Get object MenuCategory
category1 = MenuCategory.objects.get(id=1)
category2 = MenuCategory.objects.get(id=2)
category3 = MenuCategory.objects.get(id=3)

# Create new elements Menu
Menu.objects.create(menu_item='Lasanga', price=12, category_id=category1)
Menu.objects.create(menu_item='Pizza', price=15, category_id=category1)
Menu.objects.create(menu_item='Greek Salad', price=12, category_id=category2)
Menu.objects.create(menu_item='Baklava', price=6, category_id=category3)
Menu.objects.create(menu_item='Kofta', price=10, category_id=category3)
Menu.objects.create(menu_item='Fava', price=8, category_id=category2)

Menu.objects.all()
MenuCategory.objects.all() 
```
7. adding another attribute:
```python
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        default=None,
        related_name="category_name")
```

#### labs 2
models.py
```python
from django.db import models
# Create your models here.

# Create model DrinksCategory 
# Create model Drinks


class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        DrinksCategory, 
        on_delete=models.PROTECT,
        default=None)
```
admin.py
```python
from django.contrib import admin

# Import the models from models.py
from .models import Drinks, DrinksCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
```

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py shell`
```python
from myapp2.models import Drinks, DrinksCategory

cat = DrinksCategory(category_name='coffee')
cat.save()
```
- 
```python
from myapp.models import DrinksCategory, Drinks

fk = DrinksCategory.objects.get(pk=1)
drink = Drinks(drink='mocha', price=7, category_id=fk)
drink.save()
```
- `python manage.py showmigrations`
- `Drinks.objects.all()`
- `DrinksCategory.objects.all()`

#### Object Relationship Mapping - ORM
ORM - it's technique or technology (library, framework) in programming language with OOP (object oriented paradigm) lets you interact with database (like using SQL query).
in ORM - classes/object represents by tables or entity in SQL.
![[Pasted image 20231105201151.png|600]]

Python ORM:
- django ORM
- sqlalchemy (for FastAPI that not have own)

in Django ORM - this operation implement with `models.Model` class and subclass, and table called model, CRUD operation with method like (`save()`, `create()`, `delete()` etc.). (also django ORM have version control for database, `migration` command).

`QuerySet` - to retrieve object from database, you construct a `QuerySet` via a Manager of your model class. `QuerySet` represents a collection of objects from your database.

---
**QuerySet**
![[Pasted image 20231105201258.png|500]]
![[Pasted image 20231105201332.png|500]]
![[Pasted image 20231105201423.png|400]]

---
- def Custom Dunder method
```python
class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle')
        
	def __str__(self):
        return "name: " + self.name + ": customer: " + str(self.customer.name) # str(self.customer)
```
- `python manage.py makemigrations`
- `python manage.py migrate demoapp`
- `python manage.py shell`
Create object of Customer class (c). Give string parameter to constructor. Use `save()` method to save records (row) in Customer model (table):
```python
>>> from demoapp.models import Customer 
>>> c = Customer(name="Henry")
>>> c.save()
```

**Adding a model object**
Create `Customer.objects` with string parameters and use `create()` method of Manager to perform CRUD operations:
```python
>>> from demoapp.models import Customer
>>> Customer.objects.create(name="Hameed")
<Customer: Customer object (2)>
```
The `create()` method actually performs the `INSERT` operation of SQL.

---
Fetch `Customer.objects.get` primary key = 2 in Customer model (table), print pk = 2, name:
```shell
>>> from demoapp.models import Customer, Vehicle
>>> c=Customer.objects.get(pk=2) 
>>> c.name 
'Hameed'
```
Define variables for our records and give parameter as 
column : name : name of vehicle, 
customer : as id foreign key of Customer (c = pk: 2)
```shell
>>> v = Vehicle(name="Honda", customer=c) 
>>> v.save()
>>> v = Vehicle(name="Toyota", customer=c) 
>>> v.save()
```
column : name : name of vehicle, 
customer : as id foreign key of Customer (c = name: Henry) with `get()` method of Manager.
```shell
>>> c = Customer.objects.get(name="Henry") 
>>> Vehicle.objects.create(name="Ford", customer=c)
<Vehicle: Vehicle object (3)> 
>>> Vehicle.objects.create(name="Nissan", customer=c)
<Vehicle: Vehicle object (4)>
```

---
**Fetch model objects**
A `QuerySet` represents a collection of objects from database. It represents a `SELECT` query. To fetch all the objects, use the `all()` method of Manager.
```shell
>>> from demoapp.models import Customer, Vehicle
>>> Customer.objects.all()
<QuerySet [<Customer: Customer object (1)>, <Customer: Customer object (2)>]>
>>> Vehicle.objects.all()
<QuerySet [<Vehicle: Vehicle object (1)>, <Vehicle: Vehicle object (2)>, <Vehicle: Vehicle object (3)>, <Vehicle: Vehicle object (4)>]>
```
`all()` returns list of objects, iterate it using loop or list comprehension technique.
```python
>>> lst = Customer.objects.all()
>>> [c.name for c in lst]
['Henry', 'Hameed']
>>> # other list comprehenshin
>>> [a.name for a in lst]
>>> lst_veh = Vehicle.objects.all()
>>> [x.customer.name for x in lst_veh]
>>> [list(a.name for a in lst_veh), list(x.customer.name for x in lst_veh)]
```
apply filters to data fetched from model, is used to fetch objects satisfying given criteria.
In SQL terms, a `QuerySet` equates to a `SELECT` statement, it is like applying a `WHERE` clause.
`model.objects.filter(criteria)`
retrieve all the customers with names starting with 'H'
```python
>>> mydata = Customer.objects.filter(name__startswith='H')
>>> lst_veh = Vehicle.objects.all()
>>> for i in lst_veh:
>>> 	print(i.name, " : ", i.customer.name)
Honda  :  Hameed
Toyota  :  Hameed
Ford  :  Henry
Nissan  :  Henry
```

---
**Updating and removing a model object**
To update object, such as changing Customer's name, assign a new value to the name attribute and save.
```python
>>> c = Customer.objects.get(name="Henry") 
>>> c.name = "Helen" 
>>> c.save()
```
`delete()` method of model manager physically removes the corresponding row in the model's mapped table.
```python
>>> c.delete()
(3, {'demoapp.Vehicle': 2, 'demoapp.Customer': 1})
>>> Customer(name="Andrew").save()
>>> Customer(id=2, name="Kristina").save()
>>> Customer(id=1, name="Hameed").save() 
>>> pk1_fk = Customer.objects.get(pk=1)
>>> pk2_fk = Customer.objects.get(pk=2)
>>> pk3_fk = Customer.objects.get(pk=3)
>>> Vehicle(name="Supra", customer=pk3_fk).save()
>>> Vehicle(name="BMW", customer=pk1_fk).save()
>>> for i in Vehicle.objects.all():
>>> 	print(i.customer.name, " : ", i.name)
>>> vehicle = Vehicle.objects.get(name="Supra")
>>> vehicle.name = "Toyoto Supra"
>>> vehicle.save()

>>> Vehicle.objects.filter(name="Toyota")
>>> Vehicle(name = "Honda", customer = Customer.objects.get(pk=1)).save()
>>> Vehicle.objects.filter(name="Honda") & Vehicle.objects.filter(customer = 1)
```
You can perform the CRUD operations on a database table using the `QuerySet` API instead of executing raw SQL queries.

## Models and Forms
![[Pasted image 20231105210130.png|600]]
Forms using for Collect data from end-users:
![[Pasted image 20231105210021.png|350]]
Recall that web applications use forums to collect data input from users using HTML form tags.
Any form elements such as inputs are checkboxes, are sent to the server for processing when the form is submitted.

- django forms
- form class
- form models

using post method
![[Pasted image 20231106005622.png|500]]
- form class in django define all expected attribute that form will contain and render the form elements as HTML. 
- matches with server side code (benefits OOP) (form class and subclass).

models in django:
![[Pasted image 20231106010507.png|350]]
![[Pasted image 20231106010530.png|350]]
![[Pasted image 20231106011303.png|350]]


---
#### Django Fields
![[Pasted image 20231106011443.png|600]]

Field Type:
![[Pasted image 20231106011522.png|350]]

Field Arguments:
![[Pasted image 20231106011951.png|250]]

```python
from django import forms

class MyForm(forms.Form):
	variable = forms.FieldType(arguments)
	
	name = forms.CharField(required=False, label='Your name', initial='Enter your name')
	age = forms.IntegerField(help_text='A valid age is required.')
	email = forms.EmailField(help_text='@email.')
```

```python
from django import forms

from django.forms.widgets import NumberInput

FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]

class DemoForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter name: ", widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label="Enter email address: ")
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'})) # import forms.widgets NumberInput
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH, label="Select favorite dish: ")
    favorite_dish_radio = forms.ChoiceField(
    widget=forms.RadioSelect, 
    choices=FAVORITE_DISH, 
    label="Select favorite dish using radio: ")
```

---
Django Model **Field properties**

Django model is normal python class, ORM layer maps this model to a database table in Django project, each attribute of a model class represents a field of table. 

model.py
```python
from django.db import models

# Create your models here.
class Person(models.Model):
    nickname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50, default = 'Mumbai')
    tax_code = models.IntegerField(max_length=20, unique = True)
  
    def __str__(self):
        return self.name + " : " + str(self.age) + " : " + self.email

  

SEMESTER_CHOICES = (
    ("1", "Civil"),
    ("2", "Electrical"),
    ("3", "Mechanical"),
    ("4", "CompSci"),
)

  

class Student(models.Model):
    semester = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '1'
    )
    first_name = models.CharField(max_length=30, null = True)
    last_name = models.CharField(max_length=30, null = True)
```

- `default` - default value that will be called when a new object is created.
- `unique` - if parameter is True, ensure that each object will have a unique value for this field.
- `choices` - user should select a value, set this parameter to a list of two-item tuples.

Django automatically names the table as `appname_modelname`, which you can override by assigning the desired name to `db_table` parameter of the Meta class, to be declared inside the model class.
```python
class Student(CommonInfo): 
    # ... 
    class Meta(CommonInfo.Meta): 
        db_table = 'student_info'
```

---
Django Model **Field types**

- `CharField` - string, length specified by `max_length`, for longer string: `TextField`
- `IntegerField` - hold integer between -2147483648 to 2147483647, `BigIntegerField`, `SmallIntegerField` and `AutoField` to store integers of varying lengths, `max_value = 20`.
- `FloatField` - floating-point number, variant `DecimalField` stores a number with fixed digits in the fractional part, `max_digits = 5`. example: `price = forms.FloatField()` or in database: `price = models.DecimalField(max_digits=8, decimal_places=2) # from -999999.99 to 999999.99`
- `DateTimeField` - date and time as an object of Python's `datetime.datetime` class. The `DateField` stores `datetime.date` value.
- `EmailField` - actually a `CharField` with an in-built `EmailValidator`.
- `FileField` - is used to save file uploaded by the user to a designated path specified by the `upload_to` parameter.
- `ImageField` - variant of `FileField`, having the ability to validate if the uploaded file is an image.
- `URLField` - A `CharField` having in-built validation for URL.

```python
upload = forms.FileField(upload_to ='uploads/')
```

---
#### Relationship fields
- `OneToOneField` - one-to-one relationship
- `ForeignKey` - one-to-many relationship
- `ManyToManyField` - many-to-many relationship

`on_delete` - when is deleted do:
- `CASCADE`: deletes the object containing the `ForeignKey` 
	- deleting the reference object will also delete the referred object.
- `PROTECT`: Prevent deletion of the referenced object 
	- prevents the deletion of a referenced object if it has an object referencing it in the database, raise `ProtectedError`. 
- `RESTRICT`: Prevent deletion of the referenced object by raising `RestrictedError`
	- when you delete the referenced object, the `on_delete` option raises the `RestrictedError`.

---
**`ForeignKey` - one-to-many relationship**

```python
class Artist(models.Model): 
    name = models.CharField(max_length=10) 

class Album(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
```

```shell
>>> from myapp1.models import Artist, Album, Song
>>> artist1 = Artist.objects.create(name='Danny')
>>> artist2 = Artist.objects.create(name='John')
>>> album1 = Album.objects.create(artist=artist1)
>>> album2 = Album.objects.create(artist=artist2)
>>> song1 = Song.objects.create(artist=artist1, album=album1)
>>> song_two = Song.objects.create(artist=artis1, album=album2)

>>> Song.objects.get(id=1).delete()
(1, {'myapp1.Song': 1})
>>> Album.objects.get(id=1).delete()
    raise RestrictedError(
django.db.models.deletion.RestrictedError: ("Cannot delete some instances of model 'Album' because they are referenced through restricted foreign keys: 'Song.album'.", {<Song: Song object (2)>})
```

---
**`OneToOneField` - one-to-one relationship**
```python
class College(models.Model):
    CollegeID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website=models.URLField()

class Principal(models.Model):
    CollegeID = models.OneToOneField(
                College,
                on_delete=models.CASCADE
                )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

---
**`ManyToManyField` - many-to-many relationship**
```python
class Teacher(models.Model):
    TeacherID = models.ItegerField(primary_key=True)
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)
```
- django automatically creates an additional table for many to many relationship

#### Form API (templates form)

**Django Form:**
```python
class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name of Applicant', max_length=50)
    address = forms.CharField(label='Address', max_length=100)
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator'))
    field = forms.ChoiceField(choices=posts)
```
```shell
>>> from myapp1.forms import ApplicationForm
>>> f = ApplicationForm() 
>>> print(f)
<tr>
    <th><label for="id_name">Name of Applicant:</label></th>
    <td>
        <input type="text" name="name" maxlength="50" required id="id_name">
    </td>
</tr>
...
```

---
**Form Template**

myapp/forms.py
```python
from django import forms

SHIFTS = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")
```
myapp/templates/home.html
```html
<p>Hello</p>
<form action="" method="post" style="background-color: bisque;">
    {% csrf_token %}
    <!--{{form}} -->
    {{form.as_p}}

    <input type="submit" value="Submit">
</form>
```
myapp/views.py
```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.forms import InputForm

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)
```
myapp/urls.py
```python
from . import views
from django.contrib import admin
from django.urls import path
  
urlpatterns = [
    path('home/', views.form_view, name='home'),
]
```
formproject2/urls.py
```python
from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```



#### Model Form (save form inside database)
`from django import forms` - for create forms and interact with html forms.
`from django.db import models` - django ORM system for create and interact with database.

- `ModelForm` provides a means to save received data as a response, directly to the database.
- When you create a `ModelForm`, you must first import the model you want to bind with your form.
- The `ModelForm` class uses the model attributes as the HTML form elements.

---
**`Django_web_framework\week3_module3_models\formproject3_database`**
- myapp/models.py
- myapp/forms.py
- myapp/templates/home.html
- myapp/admin.py
- myapp/views.py
- myapp/urls.py
- formproject3_database/urls.py
- formproject3_database/settings.py

#### lab 1
**Scenario**
Adrian at Little Lemon would like to test the possibility of using a booking form on the website for online reservations. The purpose of the form will be to take a reservation request and store that request in a table in the database. Later it is hoped that a member of staff will be able to access and view this request from the Django administration control panel.

---
- `DateField` attribute has the parameter `auto_now` set to True and will not be displayed inside the form on the webpage. `auto_now` inside the `DateField` automatically set the field to the current date every time the object is saved.

myapp/models.py
```python
from django.db import models

# Create your models here.
class Booking(models.Model)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    quest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
```
myapp/admin.py
```python
from django.contrib import admin

# Register your models here.
from .models import Booking

admin.site.register(Booking)
```
myapp/forms.py
```python
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```
myapp/templates/booking.html
```python
<p> Booking for Little Lemon ! </p>
<form action = "" method = "post", style="background-color: #E0E0E2;">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
```
myapp/views.py
```python
from django.shortcuts import render
from myapp.forms import BookingForm

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)
```
myapp/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.form_view),
]
```
myproject/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
```

## Admin
Django provide future that create administration or admin site as part of application.
Suppose owner of Little lemon web restaurant want that you develop admin side of website to manipulate database and it can be updated by the restaurant staff.
- Django unified admin interface. (add, edit, delete)
- Django admin provides a dashboard where you can add, edit or update, delete.
- user permissions, group of users and history of changes that user did.
![[Pasted image 20231107191551.png|300]]
![[Pasted image 20231107191617.png|400]]

---
1. `python manage.py migrate`
2. `python manage.py createsuperuser`

---
Managing users in Django admin

unregister user
```python
from django.contrib.auth.models, import User 
# Unregister the provided model admin:  
admin.site.unregister(User)
```
register admin 
```python
from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    pass
```
prevent any admin user from changing content of one or more fields of a model.
- `UserAdmin` class has a property called `readonly_fields`. You can specify a list of fields that you want the user (or a super user) to be prevented from modifying.
- User model has field `date_joined`. Suppose you want that new user should never be changed. So, keep this field in the `readonly_fields` list.
- Modify the app’s admin.py by changing the NewAdmin class as follows.
```python
from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ]
```
If any user accidentally modifies the username field of the other user, it may create many problems. Like the other user may not be able to log in. (solutions is rest this privilege only with the super user and nobody else.)
- `UserAdmin` class (the base class for `NewAdmin` class that you have registered in the admin site) has a method known as `get_form()`. You need to override it to disable the username field in it.
- Next, verify if the current user is a super user. If yes, disable the username field in the form.
```python
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
form.base_fields['username'].disabled = True
        return form
```
- If you now log in as a `staff` user and try to modify the username of another user, it will not be allowed.
models.py
```python
from django.db import models 

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField()
```
admin.py
```python
from .models import Person 
admin.site.register(Person)
```
- admin interface: myapp that shows count of our Person object (1), use `__str__` for show string record of Person object by creating method in Person. (models.py myapp)
- customized string representation of the object
```python
def __str__(self): 
        return f"{self.last_name}, {self.first_name}"
```
To further customize how the models are displayed in the admin interface, decorate a subclass of `ModelAdmin` and register it with `@admin.register()` decorator (just as you did with `UserAdmin`). Set the `list_display` attribute of this class to display the fields in columns.
```python
from django.contrib import admin
from .models import Person
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
```

#### Little Lemon Reservation system in admin

models.py
```python
class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    contact = models.CharField('Phone number', max_length=20)
    date_time = models.DateTimeField()
    count_quest = models.IntegerField()
    notes = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.name}, {self.contact}, {self.date_time}, {self.count_quest}, {self.notes}"
```
admin.py (project)
```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
]
```
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser` (admin, 1234)
admin.py (myapp)
```python
from myapp.models import Reservation
#admin.site.register(Reservation)

@admin.register(Reservation)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "date_time", "count_quest", "notes")
```

#### Permissions
User and model permissions in django - control users are allowed to do which actions.
- authentication
- authorization

django group - list of permission assigned to one or more users

Type:
- Superuser - top level admin (staff by default)
- Staff user - access django admin interface
- User - everyone else is irregular user by default (not authorized to use admin site)
python objects, specific type of user is characterized by special attribute that are set inside user object.

- `python manage.py shell`
```shell
>>> from django.contrib.auth.models import User
>>> usr = User.objects.create_user('testusr', 'test@abc.com', 'pass123')
>>> usr.is_staff=True
>>> usr.save()
```
- `python manage.py createsuperuser --username=john --email=john@admin.com`

![[Pasted image 20231107212456.png|600]]
![[Pasted image 20231107212547.png|300]]

Does a user have permission? use `has_perm()`
![[Pasted image 20231107212645.png|600]]

---
**Enforcing Permissions**

If a model requires a user to gain access through special permissions, this can be granted through Django Admin.

*Model Permissions in Admin Interface
custom permission*
```python
class Product(models.Model): 
    ProductID: models.IntegerField() 
    name : models.TextField() 
    category : models.TextField
     
    class Meta: 
        permissions = [('can_change_category', 'Can change category')]
```

*Enforcing permissions at the view level*
If a user has logged in and has been authenticated, its details are available to the view function in the form of `request.user` object. If not, the value of `request.user` is an instance of `AnonymousUser`. In that case, the permission to call a view can be denied as follows:
```python
from django.core.exceptions import PermissionDenied  
def myview(request): 
    if request.user.is_anonymous(): 
        raise PermissionDenied()
```
Alternatively, you can decorate the view with a `login_required` decorator. It only allows access for logged users.
```python
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required 
@login_required 
def myview(request): 
    return HttpResponse("Hello World")
```
Let’s define a function `testpermission()`. It returns True if the user is authenticated and has a `change_category` permission.
```python
def testpermission(user):
	if user.is_authenticated() and user.has_perm("myapp.change_category"): 
		return True 
	else: 
		return False
```
This function is then used as an argument to the `@user_passes_test()` decorator. The view function defined below it will be invoked if the `testpermission()` function returns True.
```python
from django.contrib.auth.decorators import user_passes_test 
@user_passes_test(testpermission) 
def change_ctg(request): 
    #Logic for making change to category of product model instance
```
Another method to enforce permission at the view level is with the `@permission_required()` decorator. Unless the user possesses the permission mentioned as an argument, the view function won’t be called.
```python
from django.contrib.auth.decorators import permission_required
@permission_required("myapp.change_category") 
def store_creator(request): 
    # Logic for making change to category of product model instance
```
Assuming that a product model is present in `models.py`. The `ProductListView` class view renders a list of products only if the user has view permission on this model.
```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView 
from .models import Product 

class ProductListView(PermissionRequiredMixin, ListView): 
    permission_required = "myapp.view_product" 
    template_name = "product.html" 
    model = Product
```

*Enforcing permissions in Template*
```html
<html> 
<body> 
{% if user.is_authenticated %} 
         {#  to be rendeed if the user has been authenticated  #}
    {% endif %}  
<body>
</html>
```
```html
<html> 
<body> 
{% if perms.myapp.change_category %} 
  {#  To be rendered for users having required permission #} 
   {% endif %} 
<body> 
</html>
```

*Enforcing permissions in URL patterns*
```python
from django.conf.urls import url 
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [ 
    url(r'^users_only/', login_required(myview)), 
    url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview)), 
]
```

---
Users and Permissions
![[Pasted image 20231107215050.png|600]]

model admin class mothod
![[Pasted image 20231107215202.png|200]]

user objects
- group
- permissions - store and reference a single or multiple permission object, set(), add(), remove(), clear()

---

#### labs

models.py
```python
from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name
```
admin.py
```python
from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)
```
terminal
```python
# Command to perform migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Command to run server
python3 manage.py runserver

# Command to create a super user
python3 manage.py createsuperuser
```

## Database Configuration (MySQL)
by default django database configuration - SQLite (user-friendly and doesn't require config) 
SQLite for:
- small project
- rapid prototype

more Scalable or robust database like MySQL or (PostgreSQL, MariaDB, Oracle).
![[Pasted image 20231107223057.png|600]]
![[Pasted image 20231107223136.png|600]]
![[Pasted image 20231107223153.png|600]]
deliberate security measure:
![[Pasted image 20231107223217.png|400]]
![[Pasted image 20231107223231.png|600]]

---
![[Pasted image 20231107223552.png|400]]

---
**Install MySQL DB API Driver**
To interface a Python program with MySQL, ensure you have a DB API-compliant driver. There are a number of Python drivers for MySQL available. Django recommends `mysqlclient` to be used. Install it with pip installer.
- `pip3 install mysqlclient`
(any python three database connector libraries that compatible with Django)

You must configure at least one database in the `DATABASES` variable. For the configuration of the first database, its name should be `default`.
- `create database mydatabase;`
- `show databases;`
- `CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'password';`
- `GRANT ALL ON *.* TO 'admindjango'@'localhost';`
- `flush privileges;`
The settings include the **database engine**, name of the database, username, and password, along with the host IP address. This defaults to the localhost 127.0.0.10 and the port defaults to 3306.
```python
DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'mydatabase',   
        'USER': 'root',   
        'PASSWORD': '',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
        }   
    }   
}
```
- `sql_mode`: The session SQL mode will be set to the given string. It defaults to `STATIC_TRANS_TABLES` to prevent invalid or missing values from being stored in the database.
- default-character-set: The character set to be used. Default is utf8.
- `read_default_file`: MySQL configuration file to read.
- `init_command`: Initial command to issue to the server upon connection.

#### lab
settings.py
```python
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedback',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : '',
    }
}


INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
```shell
>>> python manage.py makemigrations
>>> python manage.py migrate
```
```mysql
mysql -u root -p
SHOW DATABASES;
CREATE DATABASE feedback;
```


## SRC
Models & Migrations
- [Models – official documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/ "Django official documentation page - Models")
- [Migrations – official documentation](https://docs.djangoproject.com/en/4.1/topics/migrations/ "Django official documentation page - Migrations")
- [Other Model Instance methods (including the String Dunder method)](https://docs.djangoproject.com/en/dev/ref/models/instances/#model-instance-methods)
- [Using Models – Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models "Django official documentation page - Django Tutorial for Using Models")
- [Detailed overview of Migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/ "Django official documentation page - Migrations")
- [Migration operations](https://docs.djangoproject.com/en/4.1/ref/migration-operations/ "Django official documentation page - Migration operations")
- [Understanding ORM](https://docs.djangoproject.com/en/4.1/ref/models/class/ "Django official documentation page - Model class reference")

- django orm (basics, crud, shell)
- django migration 
- dunder method python
- list comprehension python

- django orm vs sqlalchemy orm
- fastapi and sqlalchemy orm
- orm vs sql
- [database - What is an ORM, how does it work, and how should I use one? - Stack Overflow](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one)
- object-oriented paradigm
- mvc code
- DEFERRABLE INITIALLY DEFERRED sql
- graphql with django orm


---
Models and Forms
- [Models – official documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/ "Django official documentation page - Models")
- [Migrations – official documentation](https://docs.djangoproject.com/en/4.1/topics/migrations/ "Django official documentation page - Migrations")
- [Using Models – Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models "Django official documentation page - Django Tutorial for Using Models")
- [Detailed overview of Migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/#module-django.db.migrations "Django official documentation page - Migrations")
- [Migration operations:](https://docs.djangoproject.com/en/4.1/ref/migration-operations/ "Django official documentation page - Migration operations")

- django forms and model form
- django templates
- django form API

---
Admin
- [django-admin and manage.py – official documentation](https://docs.djangoproject.com/en/4.1/ref/django-admin/ "Django official documentation page - overview on django.admin and manage.py")
- [Using the Django authentication system](https://docs.djangoproject.com/en/4.1/topics/auth/default/ "Django official documentation page - Using the django authentication system")
- [Django Admin site – MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site "Django official documentation page - Django tutorial for admin site")
- [Django Admin-site – Comprehensive](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/ "Django official documentation page - The django admin site")
- [Django permissions – TestDriven](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/ "Django official documentation page -Customizing authentication in Django")

- django restaurant admin side of website
- django admin permissions
- django admin interface filter code for myapp model (database)

---
Database Configuration
- [Databases – Django official](https://docs.djangoproject.com/en/4.1/ref/databases/ "Django official documentation page - Databases")
- [MySQL notes – Django official](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes "Django official documentation page - MySQL notes")
- [Installing MySQL Client](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-db-api-drivers "Django official documentation page - MySQL DB API drivers")
- [Installing MySQL on MacOS](https://dev.mysql.com/doc/refman/5.7/en/macos-installation.html "Installing MySQL on MacOS")
- [Installing MySQL on Windows](https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html "Installing MySQL on Microsoft Windows")
- [Installing and configuring MySQL with Django](https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes "Django official documentation page - MySQL Notes")

- [Django - Introduction to PostgreSQL (w3schools.com)](https://www.w3schools.com/django/django_db_postgresql_intro.php)
- [MySQL Joins (w3schools.com)](https://www.w3schools.com/mysql/mysql_join.asp)
- mysql create user query
- mysql DCL and TCL query subsets