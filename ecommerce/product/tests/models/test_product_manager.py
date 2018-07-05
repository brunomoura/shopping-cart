from django.test import TestCase

from product.factories import ProductFactory, CategoryFactory
from product.models import Product, Category


class ProductCustomModelManagerTestCase(TestCase):

    def setUp(self):
        CategoryFactory.create().save()
        self.category = Category.objects.first()

    def test_availables(self):
        ProductFactory.create(
            category=self.category,
            available=False
        ).save()
        products_availables = Product.objects.availables()

        assert products_availables.count() == 0

        ProductFactory.create(
            category=self.category,
            available=True,
            name='Another Shoes',
            slug='another-shoes'
        ).save()
        products_availables = Product.objects.availables()

        assert products_availables.count() == 1
