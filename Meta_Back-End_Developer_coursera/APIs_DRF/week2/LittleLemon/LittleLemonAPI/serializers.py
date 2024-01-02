from rest_framework import serializers
from .models import MenuItem
from .models import Category

from decimal import Decimal

# Serializers
#class MenuItemSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=255)
#    price = serializers.DecimalField(max_digits=6, decimal_places=2)
#    inventory = serializers.IntegerField()


# Model Serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory', required=False, min_value=0)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #category = serializers.StringRelatedField()  # show title of Category model using dunder str method
    category = CategorySerializer(read_only=True)  # method 1 to show Nested fields
    #category = serializers.HyperlinkedRelatedField(queryset = Category.objects.all(), view_name='category-detail')  # category as hyperlink
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        #depth = 1  # method 2 to show Nested fields
        
        extra_kwargs = {
            'price': {'min_value': 2},
            #'stock': {'min_value': 0}
        }
    
    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)