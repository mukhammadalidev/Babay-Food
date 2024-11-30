from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # All orders
    serializer_class = OrderSerializer  # The serializer for Order model

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()  # All order items
    serializer_class = OrderItemSerializer  # The serializer for OrderItem model
