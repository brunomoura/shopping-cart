from rest_framework import status
from rest_framework.test import APITestCase

from product.factories import CategoryFactory, ProductFactory
from product.models import Product, Category

from .helpers import ProductAPI


class ProductAPITest(APITestCase):

    def setUp(self):
        self.product_api = ProductAPI()

        CategoryFactory.create().save()
        self.category = Category.objects.first()

    def test_get_by_pk(self):
        ProductFactory.create(
            category=self.category
        ).save()
        product = Product.objects.first()

        response = self.product_api.get_by_pk(product.pk)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == product.name

    def test_list(self):
        response = self.product_api.list()

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

        ProductFactory.create(
            category=self.category
        ).save()

        response = self.product_api.list()

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        another_shoes_slug = 'another-shoes'
        ProductFactory.create(
            category=self.category,
            name='Another Shoes',
            slug=another_shoes_slug,
            price=200.00,
            stock=10
        ).save()

        response = self.product_api.list()

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        # Testing order by name
        assert response.data[0]['slug'] == another_shoes_slug
