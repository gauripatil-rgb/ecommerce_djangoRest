from .models import Category, Products,Customer,Order,Review,CheckOutDetails
from rest_framework import  viewsets
from .serializers import CategorySerializer, ProductsSerializer, CustomerSerializer, OrderSerializer,ReviewSerializer, CheckOutDetailsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CustomerSerializer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderSerializer(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewSerializer(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CheckOutDetailsSerializer(viewsets.ModelViewSet):
    queryset = CheckOutDetails.objects.all()
    serializer_class = CheckOutDetailsSerializer