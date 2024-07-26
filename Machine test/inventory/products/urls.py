# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, AddStockView, RemoveStockView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'add-stock', AddStockView, basename='add-stock')
router.register(r'remove-stock', RemoveStockView, basename='remove-stock')

urlpatterns = [
    path('', include(router.urls)),
]
