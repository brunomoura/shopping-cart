from django.test import TestCase
from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from product.models import Product, Category


class ProductListViewTest(TestCase):

    def setUp(self):
        CategoryFactory.create().save()
        self.category = Category.objects.first()

        ProductFactory.create(
            category=self.category,
            available=False
        ).save()

        ProductFactory.create(
            category=self.category,
            available=True,
            name='Another Shoes',
            slug='another-shoes'
        ).save()

    def test_view_url_exists(self):
        resp = self.client.get('/ecommerce/products/')
        assert resp.status_code == 200

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('product-list'))
        assert resp.status_code == 200

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('product-list'))
        assert resp.status_code == 200
        assert resp.status_code == 200
        self.assertTemplateUsed(resp, 'product/product_list.html')

    def test_lists_all_authors(self):
        resp = self.client.get(reverse('product-list'))
        assert resp.status_code == 200
        assert len(resp.context['product_list']) == 1
