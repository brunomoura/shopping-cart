import factory

from product.models import Product

from .category import CategoryFactory


class ProductFactory(factory.Factory):

    class Meta:
        model = Product

    category = factory.SubFactory(CategoryFactory)
    name = 'New Shoes'
    slug = 'new-shoes'
    price = 100.00
    stock = 5
