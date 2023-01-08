from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from learning_django_2.store.models import Product
from learning_django_2.store.serializers import ProductSerializer


# Create your views here.

@api_view()
def product_list(request):
    return Response('ok')



@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)

    return Response(serializer.data)