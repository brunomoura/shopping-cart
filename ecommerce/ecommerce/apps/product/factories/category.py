import factory

from product.models import Category


class CategoryFactory(factory.Factory):

    class Meta:
        model = Category

    name = 'Shoes'
    slug = 'hoes'
