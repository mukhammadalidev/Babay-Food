from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BasketViewSet,BasketItemViewSet

router =DefaultRouter()
router.register(r'basket', BasketViewSet, basename='basket')
router.register(r'basket-item', BasketItemViewSet, basename='basket-item')

urlpatterns  = [
path('', include(router.urls)),
]