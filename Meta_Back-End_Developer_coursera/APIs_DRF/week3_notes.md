
## Filtering, ordering, searching and Pagination

### Filtering and searching

cloning setup week2 Little Lemon API project: 
```powershell
>>> Meta_Back-End_Developer_coursera\APIs_DRF> Copy-item -Force -Recurse -Verbose .\week2\LittleLemon\ -Destination .\week3\
>>> APIs_DRF\week3\LittleLemon> pipenv shell
Creating a virtualenv for this project...
Pipfile: D:\Programming\Python\Meta_Back-End_Developer_coursera\APIs_DRF\week3\LittleLemon\Pipfile
Using C:/Users/pepel/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
[ ===] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 4421ms
>>> APIs_DRF\week3\LittleLemon> & C:\Users\pepel\.virtualenvs\LittleLemon-SArJYjqv\Scripts\activate.ps1
```

views.py
```python
from decimal import Decimal

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()

        category_slug = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')

        if category_slug:
            items = items.filter(category__slug__iexact=category_slug)
        if to_price:
            items = items.filter(price__lte=Decimal(to_price))  # you can use Decimal or Float to validate data
        if search:
            items = items.filter(title__icontains=search)
            
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
```

### Ordering

views.py
```python
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()

        ordering = request.query_params.get('ordering')
        if ordering:
            #items = items.order_by(ordering)  # for one value query parameters
            ordering_fields = ordering.split(",")  # for many fields or values passed into ?ordering query parameters
            items = items.order_by(*ordering_fields)

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
```

### Importance of data validation

Little Lemon API requirements of data validation
![[Pasted image 20240103002842.png]]

serializers.py
```python
class MenuItemSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(
    #    max_length=255,
    #    validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    #    )
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
        
        #def validate_price(self, value):
        #    if (value < 2):
        #        raise serializers.ValidationError('Price should not be less than 2.0')

        #def validate_stock(self, value):
        #    if (value < 0):
        #        raise serializers.ValidationError('Stock cannot be negative')
        
        #def validate(self, attrs):
        #    if(attrs['price']<2):
        #        raise serializers.ValidationError('Price should not be less than 2.0')
        #    if(attrs['inventory']<0):
        #        raise serializers.ValidationError('Stock cannot be negative')
        #    return super().validate(attrs)

    def calculate_tax(self, product: MenuItem) -> float:
        return round(product.price * Decimal(1.1), 2)
```

---

|**Field**|**Value**|**Status**|
|---|---|---|
|price|0|Invalid, because the price of a menu item cannot be 0|
|stock|negative value|Invalid, because stock of a menu item cannot be lower than 0|
|title|Duplicate values|Invalid, because there should not be more than one menu item with the same name or title|

---
serializers.py
```python
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

---
Method 1: Conditions in the field

models.py
```python
price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
```
![[Pasted image 20240102230632.png|700]]

---
Method 2: Using keyword arguments in the Meta class

models.py
```python
class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
        }
```
```python
'stock':{'source':'inventory', 'min_value': 0}
```
```python
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock':{'source':'inventory', 'min_value': 0}
        }

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```
![[Pasted image 20240102230846.png|700]]

---
Method 3: Using validate_field() method

methods above the Meta class in the MenuItemSerializer.
```python
def validate_price(self, value):
        if (value < 2):
            raise serializers.ValidationError('Price should not be less than 2.0')

def validate_stock(self, value):
        if (value < 0):
            raise serializers.ValidationError('Stock cannot be negative')
```
![[Pasted image 20240102231138.png|700]]

---
Method 4: Using the validate() method

code above the Meta class in the MenuItemSerializer.
```python
def validate(self, attrs):
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
```
![[Pasted image 20240102231246.png|700]]

---
Unique validation

UniqueValidator
```python
from rest_framework.validators import UniqueValidator
```
```python
from rest_framework.validators import UniqueTogetherValidator
```

code above Meta class in MenuItemSerializer
```python
extra_kwargs = {
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=MenuItem.objects.all()
                    )
                ]
            }
        }
```
```python
title = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    )
```
![[Pasted image 20240102231513.png|500]]

---
UniqueTogetherValidator
```python
validators = [
            UniqueTogetherValidator(
                queryset=MenuItem.objects.all(),
                fields=['title', 'price']
            ),
        ]
```
![[Pasted image 20240102231550.png|500]]


### Data sanitization

examples:
views.py
```python
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def injection(request):
    item = get_object_or_404(MenuItem, pk=24)
    serialized_item = MenuItemSerializer(item)
    return Response(str(serialized_item.data))
```
```python
urlpatterns = [
    path('injection', views.injection),
]
```
```json
{
	"id": 24,
	"title": "Tomato Pasta <script>alert('hello')</script>",
	"price": "4.50",
	"stock": 20,
	"price_after_tax": 4.95,
	"category": {
		"id": 5,
		"slug": "dish",
		"title": "Main Dish"
	}
}
```
![[Pasted image 20240102234446.png|700]]

---
Install bleach packages that can help with cleaning this.

- `pipenv install bleach`
- serializers.py `import bleach`
```python
import bleach

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory', required=True, min_value=0)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'title': {'validators':
           [UniqueValidator(queryset=MenuItem.objects.all())]
            }
        }

        # Data Sanitization
        #def validate_title(self, value):
        #    return bleach.clean(value)

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            # Sanitize HTML and JavaScript using bleach
            representation['title'] = bleach.clean(representation['title'])
            return representation

        #def validate(self, attrs):
        #    attrs['title'] = bleach.clean(attrs['title'])
        #    if(attrs['price']<2):
        #        raise serializers.ValidationError('Price should not be less than 2.0')
        #    if(attrs['inventory']<0):
        #        raise serializers.ValidationError('Stock cannot be negative')
        #    return super().validate(attrs)
```


### Pagination

pagination is process of dividing a document into discreate page, divide returned data and display chunks of data, limited number of data like posts.

views.py
```python
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        
        # Pagination
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
            
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
```

### Class Based Filtering, Sorting and Pagination

Scaffold project, Setup:

views.py
```python
from rest_framework.response import Response 
from rest_framework import viewsets 
from .models import MenuItem 
from .serializers import MenuItemSerializer  

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

urls.py
```python
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
]
```
---
Django Filter Backend
To use `DjangoFilterBackend`, first install `django-filter`.
```powershell
pip install django-filter
```

Then add `'django_filters'` to Django's `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]
```

You should now either add the filter backend to your settings:
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
}
```


### Caching

cacheable - response can be saved for a while or specific amount of time.
caching - sends saved result instead of creating a new one.

caching may applied in:
- visitor (browser) - 
- reverse proxy server - 
- web server (server-side scripts, business logic) - Separate cache storage: 
	- simple files
	- a database
	- caching tools like redis or memcached
- database (RDBMS, DBMS) - Query cache
![[Pasted image 20240103181618.png|600]]

server side caching
![[Pasted image 20240103182327.png|600]]

client side caching
- use caching headers
- use local cache
- create call to server
![[Pasted image 20240103182626.png|600]]


### Filtering, Searching, Ordering and Pagination in views and settings

views.py
```python
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        # Filtering and Searching
        category_slug = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')

        if category_slug:
            items = items.filter(category__slug__iexact=category_slug)
        if to_price:
            items = items.filter(price__lte=Decimal(to_price))  # you can use Decimal or Float to validate data
        if search:
            items = items.filter(title__icontains=search)
            
        # Ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            #items = items.order_by(ordering)  # for one value query parameters
            ordering_fields = ordering.split(",")  # for many fields or values passed into ?ordering query parameters
            items = items.order_by(*ordering_fields)
            
        # Pagination
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        paginator = Paginator(items, per_page=perpage)

        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
            
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
```
```python
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']
```

---
settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
}
```

## Security an API in Django REST framework

### Token-based authentication in DRF

token send with api headers of HTTP response and request.

![[Pasted image 20240108182912.png|500]]

--- 
settings.py
- token based auth - `rest_framework.authtoken`
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'LittleLemonAPI',
]
```

- `& C:\Users\pepel\.virtualenvs\LittleLemon-SArJYjqv\Scripts\activate.ps1`
- `pipenv shell`
- `python .\manage.py migrate`
- `python .\manage.py createsuperuser`
![[Pasted image 20240108184038.png|500]]

---
views.py
```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# Token authentication
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "Some secret message"})
```

urls.py
```python
urlpatterns = [
    # Token authentication
    path('secret', views.secret)
]
```

- `http://127.0.0.1:8000/api/secret` returns: `{"detail": "Authentication credentials were not provided."}`
![[Pasted image 20240108184933.png|600]]

---
settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

- copy token
![[Pasted image 20240108185505.png|600]]
- select
![[Pasted image 20240108185619.png|600]]
![[Pasted image 20240108185718.png|600]]

---
 Generate Token

urls.py
```python
# genenerate api endpoint token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('secret/', views.secret),

    # generate token
    path('api-token-auth/', obtain_auth_token),
]
```

![[Pasted image 20240108190404.png|600]]

- to generate token you need pass: username and password that you created with `python .\manage.py createsuperuser`
![[Pasted image 20240108193152.png|600]]

if username and password is invalid returns
```json
{ 
	"non_field_errors": [ "Unable to log in with provided credentials." ] 
}
```

### User Roles

- create 1 group (manager) and 2 users (johndoe, jimmydoe).
- give 1 of them group (manager - johndoe)

views.py
```python
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only Manager Should See This"})
    else:
        return Response({"message": "You are not authorized"}, 403)
```
urls.py
```python
path('manager-view/', views.manager_view),
```

- generate token for user
![[Pasted image 20240108194455.png|500]]
```johndoe_manager_token
14827d74577e9b32d36579c3095b41624f05c5ec
```
```jimmydoe_token
b0ad703d316e5cd69281479252d8f21c0033685b
```

---
![[Pasted image 20240108195253.png|600]]

### Setting up API throttling

throttling is about limit your bandwidth access
- Anonymous Throttling for Unauthenticated Users (no token in api header)
- User Throttling for Authenticated Users (valid token)

views.py
```python
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "successful"})
  

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message": "messagge for the logged in users only"})
```

urls.py
```python
urlpatterns = [
    path('throttle-check/', views.throttle_check),
    path('throttle-check-auth/', views.throttle_check_auth),
]
```

settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '5/minute',
    }
}
```

- `'anon': '20/day',`

![[Pasted image 20240108201140.png|600]]

---
![[Pasted image 20240108201901.png|600]]
![[Pasted image 20240108201939.png|600]]

---
with the current settings when you use throttling classes all api endpoints limited to DEFAULT_THROTTLE_RATES.

throttles.py (app-levels)
```python
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'
```

settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '5/minute',

        'ten': '10/minute'
    }
}
```

views.py
```python
from .throttles import TenCallsPerMinute

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message": "messagge for the logged in users only"})
```

### Throttle in class-based views

views.py
```python
from rest_framework.response import Response 
from rest_framework import viewsets 
from .models import MenuItem 
from .serializers import MenuItemSerializer

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

urls.py
```python
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
]
```

settings.py
```python
REST_FRAMEWORK = {
	# Throttiling class based
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    
    # Throttling
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '5/minute',
        'ten': '10/minute'
    },
}
```

---
Conditional throttling
with conditional throttling you can throttle API endpoints only for specific HTTP methods like `GET` or `POST` calls.
- rewrite `get_throttles` method
- `POST` call in `ModelViewSet` is handled by `create` methods.
- `GET` call is `list` or `retrieve` methods.

views.py
```python
class ThrottleMenuItemsViewSet(viewsets.ModelViewSet):
    # Conditional throttling
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]
```

---
example of `ModelViewSet` handle HTTP methods:
```python
urlpatterns = [
    path('books', views.BookView.as_view(
        {
            'get': 'list',
            'post': 'create',
        })
    ),
    path('books/<int:pk>',views.BookView.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
    )
]
```

---
Custom throttling classes

views.py
```python
from .throttles import TenCallsPerMinute
class ThrottleMenuItemsViewSet(viewsets.ModelViewSet):
    # Custom throttling classes
    throttle_classes = [TenCallsPerMinute]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

throttles.py (app-levels)
```python
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'
```

settings.py
```python
REST_FRAMEWORK = {
	...
    'DEFAULT_THROTTLE_RATES': {
	    ...
        'ten': '10/minute'
    },
}
```

---
Real world examples of API rate limits

Here are some popular services and their current rate limit. This can help you to get some idea of how others are using such features in their API projects.

|**Service**|**Anonymous**|**Authenticated**|
|---|---|---|
|Facebook graph API|X|200/hour|
|Instagram API|X|200/hour|
|Instagram messenger API|X|100/second|
|WhatsApp messaging API|X|80/second|

### Intro to Djoser library for better authentication

Djoser - authentication and authorization library for DRF project.

- `pipenv shell`
- `pipenv install djoser`

configuration of djoser:
- include it `INSTALLED_APPS` under the `rest_framework` APP
- `REST_FRAMEWORK` default authentication classes `'rest_framework.authentication.SessionAuthentication'`
- djoser section with `"USER_ID_FIELD": "username"`
- add endpoints for djoster in project-levels `path('auth/', include('djoser.urls')), path('auth/', include('djoser.urls.authtoken')),`

settings.py
```python
INSTALLED_APPS = [
    'rest_framework',
    'LittleLemonAPI',
    
    # djoser - authentication and authorization library for DRF project (under rest_framework)
    'djoser',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
}

DJOSER = {
    "USER_ID_FIELD": "username",
    #"LOGIN_FIELD": "email"
}
```

urls.py (project-levels)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LittleLemonAPI.urls')),
    # djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
```

---
Djoser endpoints
![[Pasted image 20240108233030.png|600]]


### Registration and authentication endpoints with JWT

- `pipenv shell`
- `pipenv install djangorestframework-simplejwt`

settings.py
```python
# for JWT access token Life Time
import datetime

INSTALLED_APPS = [
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
  
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5)
}
```

urls.py (project-levels)
```python
from django.contrib import admin
from django.urls import path, include

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---
Generate JWT Token

![[Pasted image 20240109010204.png|700]]

---
Access to Secret Message

![[Pasted image 20240109010946.png|700]]

```python
SIMPLE_JWT = {
    #'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5)
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(seconds=20)
}
```
![[Pasted image 20240109011239.png|700]]

---
Regenerate Token

![[Pasted image 20240109011549.png|700]]

---
Block refresh token (block client to generate JWT access tokens)

settings.py
```python
INSTALLED_APPS = [
    # JWT
    'rest_framework_simplejwt',

    # Block refresh token (block client to generate JWT access tokens)
    'rest_framework_simplejwt.token_blacklist',
]
```

- `python .\manage.py migrate`
- `python .\manage.py runserver`

urls.py
```python
from django.contrib import admin
from django.urls import path, include

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Block refresh token (block client to generate JWT access tokens)
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # block JWT refresh tokens
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
```

![[Pasted image 20240109012433.png|700]]
![[Pasted image 20240109012532.png|700]]


### User account management

User registration system in django project using djoster.

![[Pasted image 20240109013924.png]]

---

views.py
```python
from rest_framework.permissions import IsAdminUser
# User account management with Djoser
@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    return Response({"message": "ok"})
```

urls.py
```python
urlpatterns = [
    # User account management with Djoser
    path('groups/manager/users', views.managers),
]
```

---
user token
![[Pasted image 20240109014553.png|700]]
admin token
![[Pasted image 20240109014619.png|700]]

---

views.py
```python
from django.contrib.auth.models import User, Group

# User account management with Djoser
@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        #managers.user_set.add(user)
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({"message": "ok"})
    return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
```

----
get johndoe token and check access
![[Pasted image 20240109015553.png|700]]

add johndoe to manager group with admin token
![[Pasted image 20240109015509.png|700]]





### SRC

Filtering, ordering, searching and Pagination:
- [Pagination - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/pagination/#pagination)
- [Filtering - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends)
- [Validators - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/validators/)
- [Filtering - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/filtering/#searchfilter)

- django query params
- django filter query parameter
- drf filtering api_view and class based views
- filtering in drf
- Decimal vs float python
- django-filters package for class based views
- django rest framework validate field
- pagination
- django pagination limit
- django price__lte in class based views
- django integer fields in models lte, gte (specific attributes)
- How to filter objects by price range in Django?
- Django pagination - How to limit the pages?

- injection with javascript for backend
- sql injection
- how to prevent injection in django
- [Security in Django | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/4.1/topics/security/)
- [Bleach — Bleach 6.1.0 20231006 documentation](https://bleach.readthedocs.io/en/latest/)

- django rest framework caching
- memcached vs redis
- redis with celery in django
- [memcached - a distributed memory object caching system](https://memcached.org/)
- [Redis](https://redis.io/)

---
Security an API in Django REST framework:
- [Djoser documentation](https://djoser.readthedocs.io/en/latest/)
- [Djoser source code](https://github.com/sunscrapers/djoser)
- [Simple JWT: A JSON Web Token authentication plugin for the Django REST framework](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Simple JWT source code](https://github.com/jazzband/djangorestframework-simplejwt)

- [Authentication - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication)
- [Throttling - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/throttling/#throttling)
- django rest framework authentication and authorization
- django user roles for authentication
- throttling
- [Internet Throttling: What Is It and What You Can Do About It | Tom's Guide (tomsguide.com)](https://www.tomsguide.com/us/internet-throttling-what-to-do,review-5154.html)
- django djoser
- [Getting started — djoser 2.2.2 documentation](https://djoser.readthedocs.io/en/latest/getting_started.html)
- json web token
- django rest framework simple jwt
- [datetime — Basic date and time types — Python 3.12.1 documentation](https://docs.python.org/3/library/datetime.html
- pyenv