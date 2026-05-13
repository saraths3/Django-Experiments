from django.db import models

# Create your models here.
# class Student:
#     def __init__(self, name, age):
#         self.name = name;self.age = age

# s1 = Student('Sarath S', 22)

class MyStudents(models.Model):
    name = models.CharField(max_length = 20)
    roll = models.IntegerField()
    address = models.TextField() 
    bio = models.TextField(default='Student of University of Kerala')
    cource_section = (
        ('BSc','Bsc'),
        ('BBA', 'BBA'),
        ('BCA', 'BCA')
    )
    cource = models.CharField(max_length=30, null=True, choices=cource_section)
    dob = models.DateField(null=True)
    tob = models.TimeField(null=True)
    toa = models.DateTimeField(null=True)
    
class Teachers(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.IntegerField()
    email = models.EmailField()

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True)
    discription = models.TextField()
    salary = models.IntegerField(blank=True, null=True)
    dummydata = models.CharField(null= True)

class userdata(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField(max_length=100, blank=True)
    email = models.EmailField()
    fresher = models.BooleanField(default=True)