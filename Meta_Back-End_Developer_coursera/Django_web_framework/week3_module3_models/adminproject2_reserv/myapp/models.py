from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    contact = models.CharField('Phone number', max_length=20)
    date_time = models.DateTimeField()
    count_quest = models.IntegerField()
    notes = models.TextField(max_length=300, blank=True)


    def __str__(self):
        return f"{self.name}, {self.contact}, {self.date_time}, {self.count_quest}, {self.notes}"
    

