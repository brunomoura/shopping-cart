from django.views.generic.list import ListView

from product.models import Product


class ProductListView(ListView):

    model = Product

    def get_queryset(self):
        return Product.objects.availables()
