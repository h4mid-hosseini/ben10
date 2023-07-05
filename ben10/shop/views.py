from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializers
from .models import Product
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class ProductViews(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        user = request.user
        product = Product.objects.filter(owner__id=user.id)
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        self.check_object_permissions(request, product)
        data = JSONParser().parse(request)
        serializer = ProductSerializers(data=data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        self.check_object_permissions(request, product)
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)
