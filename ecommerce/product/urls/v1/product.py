from django.conf.urls import url, include

from product.views.v1 import product as views


product_urls = [
    url(
        r'^products/', include(
            [
                url(
                    r'^$',
                    views.ProductListAPIView.as_view(),
                    name='product-list'
                ),
                url(
                    r'^(?P<pk>\d+)/$',
                    views.ProductRetrieveAPIView.as_view(),
                    name='product-detail'
                )
            ]
        )
    )
]
