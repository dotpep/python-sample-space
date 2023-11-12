from django.db import models

# Create your models here.
class PriceMixin(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True

class Pan(PriceMixin):
    VENDOR_TEFAL = "tefal", "Tefal"
    VENDOR_FISSMAN = "fissman", "Fissman"

    vendor_choices = [
        (VENDOR_TEFAL[0], VENDOR_TEFAL[1]), 
        (VENDOR_FISSMAN[0], VENDOR_FISSMAN[1])
    ]
    vendor = models.CharField(max_length=128, choices=vendor_choices)
    diameter = models.PositiveIntegerField()

    def __str__(self):
        return self.vendor + " : " + str(self.diameter) + " : " + str(self.price)