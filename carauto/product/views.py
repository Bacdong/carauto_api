from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Variation
from .serializer import Category, Product, Variation
from .serializer import GetProductsInfo, ProductSerializer, GetCategoriesInfo


# Create your views here.
class GetProductsInfoFromAPIView(APIView):

    def get(self, request):

        list_product = Product.objects.all()
        my_data = GetProductsInfo(list_product, many = True)

        return Response(
            data = my_data.data,
            status = status.HTTP_200_OK,
        )

    def post(self, request):

        my_data = ProductSerializer(data = request.data)

        if not my_data.is_valid():
            return Response(
                message = 'Product info is valid, try again!',
                status = status.HTTP_400_BAD_REQUEST,
            )

        name = my_data.data['name']
        image = my_data.data['image']
        price = my_data.data['price']
        brief = my_data.data['brief']
        category = my_data.data['category']
        status_product = my_data.data['status_product']

        new_product = Product.objects.create(
            name = name,
            image = image,
            price = price,
            brief = brief,
            category = category,
            status_product = status_product,
        )

        return Response(
            message = 'Add product successfully!',
            data = new_product.id,
            status = status.HTTP_200_OK,
        )


class GetCategoriesFromAPIView(APIView):

    def get(self, request):

        list_category = Category.objects.all()
        my_data = GetCategoriesInfo(list_category, many = True)

        return Response(
            data = my_data.data,
            status = status.HTTP_200_OK,
        )
