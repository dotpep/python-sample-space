from rest_framework import serializers
from .models import MenuItem
from .models import Category

from decimal import Decimal

# Data Validation
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

# Data Sanitization, injection
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(
    #    max_length=255,
    #    validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    #    )
    
    stock = serializers.IntegerField(source='inventory', required=True, min_value=0)
    #stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        
        extra_kwargs = {
            'price': {'min_value': 2},
            #'stock': {'source': 'inventory', 'min_value': 0},
            'title': {'validators': 
                    [UniqueValidator(queryset=MenuItem.objects.all())]
            }
        }
        
        # Data Sanitization
        #def validate_title(self, value):
        #    return bleach.clean(value)
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            # Sanitize HTML and JavaScript using bleach
            representation['title'] = bleach.clean(representation['title'])
            return representation
        
        # Data Validation
        #def validate_price(self, value):
        #    if (value < 2):
        #        raise serializers.ValidationError('Price should not be less than 2.0')

        #def validate_stock(self, value):
        #    if (value < 0):
        #        raise serializers.ValidationError('Stock cannot be negative')
        
        #def validate(self, attrs):
        #    attrs['title'] = bleach.clean(attrs['title'])
        #    if(attrs['price']<2):
        #        raise serializers.ValidationError('Price should not be less than 2.0')
        #    if(attrs['inventory']<0):
        #        raise serializers.ValidationError('Stock cannot be negative')
        #    return super().validate(attrs)
            
    
    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)
    