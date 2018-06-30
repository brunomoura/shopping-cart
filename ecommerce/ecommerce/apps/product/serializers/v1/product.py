from rest_framework import serializers

from ecommerce.custom_serializers import V1HyperLinkedModelSerializer

from product.models import Product


class ProductListSerializer(V1HyperLinkedModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:

        model = Product

        fields = (
            'category',
            'url',
            'pk',
            'name',
            'slug',
        )


class ProductDetailSerializer(V1HyperLinkedModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:

        model = Product

        fields = (
            'category',
            'url',
            'pk',
            'name',
            'slug',
            'description',
        )
