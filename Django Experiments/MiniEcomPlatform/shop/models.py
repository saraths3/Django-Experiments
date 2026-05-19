from django.db import models

# Create your models here.
# Customer id (Primary Key, auto) name → CharField(max_length=100) email → EmailField(unique=True) phone_number → CharField(max_length=15, blank=True) address → TextField(blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Product id (Primary Key, auto) name → CharField(max_length=150) description → TextField(blank=True) price → DecimalField(max_digits=10, decimal_places=2) stock → IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

# Order id (Primary Key, auto) customer → ForeignKey(Customer, on_delete=models.CASCADE) order_date → DateTimeField(auto_now_add=True) status → CharField(max_length=20, default=Pending)

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"


# Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"