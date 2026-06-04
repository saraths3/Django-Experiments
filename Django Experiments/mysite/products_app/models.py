from django.db import models

# Create your models here.

class Catagorybase(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Productbase(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    images = models.ImageField(upload_to='products/')
    catagory = models.ForeignKey(Catagorybase, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name