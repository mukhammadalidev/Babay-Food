from rest_framework import serializers
from .models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()  # Nest ProductSerializer to include product details

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True)  # Serialize related OrderItems

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'status']
