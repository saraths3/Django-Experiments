from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    university = models.TextField(blank=True, default='Student of University of Kerala')
    married = models.BooleanField()