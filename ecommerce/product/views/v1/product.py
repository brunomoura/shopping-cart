from rest_framework import generics

from product.serializers.v1 import ProductListSerializer, \
    ProductDetailSerializer
from product.models import Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    ordering_fields = (
        'name'
    )

    def get_queryset(self):
        products = Product.objects\
            .filter(
                available=True
            )
        return products


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
