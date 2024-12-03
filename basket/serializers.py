from itertools import product

from rest_framework import serializers

from basket.models import Basket, BasketItem
from products.models import Product
from products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'



class BasketItemSerializer(serializers.ModelSerializer):
    basket = serializers.PrimaryKeyRelatedField(queryset=Basket.objects.all())
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')

    

    class Meta:
        model = BasketItem
        fields = '__all__'


