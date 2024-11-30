from django.shortcuts import render
from rest_framework import viewsets

from basket.models import Basket, BasketItem
from basket.serializers import BasketSerializer, BasketItemSerializer


# Create your views here.
class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer