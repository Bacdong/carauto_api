from rest_framework import serializers
from .models import Category, Product, Variation


class GetCategoriesInfo(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GetProductsInfo(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    """ Info get or post data to API """

    name = serializers.CharField(max_length = 100)
    image = serializers.CharField(max_length = 255)
    brief = serializers.CharField(max_length = 100)
    category = serializers.IntegerField()
    status_product = serializers.BooleanField(default = True)

    def __str__(self):
        return self.name