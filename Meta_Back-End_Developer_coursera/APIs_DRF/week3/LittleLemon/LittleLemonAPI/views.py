from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from decimal import Decimal

from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

# Pagination
from django.core.paginator import Paginator, EmptyPage

# Class based
from rest_framework import viewsets 
import django_filters

# Token authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Throttling
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

from .throttles import TenCallsPerMinute

# User account management with Djoser
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

# Renderers
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework_csv.renderers import CSVRenderer

@api_view()
@renderer_classes([CSVRenderer])
def csv_menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)

@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data': serialized_item.data}, template_name='menu-items.html')


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def injection(request):
    item = get_object_or_404(MenuItem, pk=24)
    serialized_item = MenuItemSerializer(item)
    return Response(str(serialized_item.data))


# Function based views
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
            items = items.filter(price__lte=Decimal(to_price))  # you can use Decimal or Float to validate data
        if search:
            items = items.filter(title__icontains=search)
            
        # Ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            #items = items.order_by(ordering)  # for one value query parameters
            ordering_fields = ordering.split(",")  # for many fields or values passed into ?ordering query parameters
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
    
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)  # show 404 error if there is no pk=id
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        items = Category.objects.all()
        serialized_item = CategorySerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = CategorySerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)


# Class based views
class ItemListFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    
    class Meta:
        model = MenuItem
        fields = ['min_price', 'max_price']


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['title', 'price', 'inventory']
    search_fields=['title', 'category__title']
    
    filter_class = ItemListFilter


# Token authentication
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "Some secret message"})


# User roles
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only Manager Should See This"})
    else:
        return Response({"message": "You are not authorized"}, 403)


# Throttling
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "successful"})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message": "messagge for the logged in users only"})


# Throttling in Class-based views
class ThrottleMenuItemsViewSet(viewsets.ModelViewSet):
    # Throttling
    #throttle_classes = [AnonRateThrottle, UserRateThrottle]
    #queryset = MenuItem.objects.all()
    #serializer_class = MenuItemSerializer
    
    # Conditional throttling
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]
    
    # Custom throttling classes
    #throttle_classes = [TenCallsPerMinute]
    #queryset = MenuItem.objects.all()
    #serializer_class = MenuItemSerializer
    

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
