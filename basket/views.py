from django.shortcuts import render
from rest_framework import viewsets

from basket.models import Basket, BasketItem
from basket.serializers import BasketSerializer, BasketItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class BasketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer

    def get_queryset(self):
        # Only return baskets belonging to the authenticated user
        return Basket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the authenticated user to the basket
        serializer.save(user=self.request.user)


class BasketItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketItemSerializer

    def get_queryset(self):
        # Filter basket items belonging to the authenticated user's basket
        return BasketItem.objects.filter(basket__user=self.request.user)