from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet,ProductsViewSet, CustomerSerializer, OrderSerializer, ReviewSerializer, CheckOutDetailsSerializer

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'customer', CustomerSerializer)
router.register(r'order', OrderSerializer)
router.register(r'review', ReviewSerializer)
router.register(r'CheckOutDetails', CheckOutDetailsSerializer )
urlpatterns = router.urls


    