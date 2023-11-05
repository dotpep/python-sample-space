from django.db import models

# Create your models here.

# Field Types and Parameters (attribute)
class Person(models.Model):
    nickname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50, default = 'Mumbai')
    tax_code = models.IntegerField(max_length=20, unique = True, null = True)

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


# Relation Field Test

# One to many
class Artist(models.Model): 
    name = models.CharField(max_length=10) 

class Album(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT) 

class Song(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 
    album = models.ForeignKey(Album, on_delete=models.RESTRICT) 


# One to one
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


# many to many
# django automatically creates an additional table for many to many relationship
class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 

class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField() 
    teacher = models.ManyToManyField(Teacher) 
