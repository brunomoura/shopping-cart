from django.conf.urls import url, include

from product.urls import site_product_urls

urlpatterns = \
    site_product_urls

url_site_patterns = [
    url(r'^', include(urlpatterns)),
]
