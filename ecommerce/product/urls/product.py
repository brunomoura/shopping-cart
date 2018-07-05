from django.conf.urls import url, include

from product.views import ProductListView


site_product_urls = [
    url(
        r'^products/', include(
            [
                url(
                    r'^$',
                    ProductListView.as_view(),
                    name='product-list'
                )
            ]
        )
    )
]
