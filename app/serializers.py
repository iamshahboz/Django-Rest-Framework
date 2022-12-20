from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Product
        fields = [
            'user',
            'id',
            'title',
            'content',
            'price'
        ]
    '''
    Custom validation with serializers
    To do that we pick the field we want to validate data from
    example
    def validate _<fieldname>


    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product title")

        return value '''



















