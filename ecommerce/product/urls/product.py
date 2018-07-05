from django.conf.urls import url, include

from product.views import ProductListView, ProductCreateView


site_product_urls = [
    url(
        r'^products/', include(
            [
                url(
                    r'^$',
                    ProductListView.as_view(),
                    name='product-list'
                ),
                url(
                    r'^add/$',
                    ProductCreateView.as_view(),
                    name='product-add'
                )
            ]
        )
    )
]
