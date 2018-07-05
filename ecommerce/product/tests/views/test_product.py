from unittest.mock import patch, MagicMock

from django.test import TestCase, RequestFactory
from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from product.models import Product, Category
from product.views import ProductCreateView


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


class ProductCreateViewTest(TestCase):

    def setUp(self):
        CategoryFactory.create().save()
        self.category = Category.objects.first()

        self.factory = RequestFactory()

    @patch('product.models.Product.save', MagicMock(name="save"))
    def test_post(self):
        data = {
            'category': str(self.category.id),
            'name': 'Nike Shoes',
            'slug': 'nike_shoes',
            'description': 'New Nike shoes',
            'price': 100,
            'stock': 10
        }
        request = self.factory.post(reverse('product-add'), data)
        response = ProductCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.save.called)
        self.assertEqual(Product.save.call_count, 1)
