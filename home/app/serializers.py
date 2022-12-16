from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price'
        ]
