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

class Teachers(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.IntegerField()
    email = models.EmailField()

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    discription = models.TextField()
    salary = models.IntegerField()


class userdata(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    