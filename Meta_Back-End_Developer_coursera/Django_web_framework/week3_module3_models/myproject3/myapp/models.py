from django.db import models

# Create your models here.
# Menu Category
# Menu

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self):
        return "pk: " + str(self.id) + " menu_category_name: " + self.menu_category_name

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory, 
        on_delete=models.PROTECT, 
        default=None,
        related_name="category_name")
    
    def __str__(self):
	    return "pk:" + str(self.id) + " menu_item: " + self.menu_item + " price: " + str(self.price) + " category_id(foreign key): " + str(self.category_id.id)