from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        #return "rating: " + str(self.rating) + " menuitem: " + str(self.menuitem_id)
        return f"rating: {self.rating}, menu-item: {self.menuitem_id}, user: {self.user=}"