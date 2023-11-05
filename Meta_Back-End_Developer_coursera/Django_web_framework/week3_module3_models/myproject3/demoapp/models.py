from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
	    return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )

    def __str__(self):
	    return "name: " + self.name + ": customer: " + str(self.customer.name) # str(self.customer)
    