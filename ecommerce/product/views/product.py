from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from product.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.availables()


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')
