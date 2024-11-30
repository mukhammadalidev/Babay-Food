from rest_framework import serializers

from categories.models import Category
from categories.serializers import CategorySerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='name')
    class Meta:
        model = Product
        fields = '__all__'
