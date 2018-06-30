from django.conf.urls import url, include

from product.urls.v1 import urlpatterns as product_urls_v1

urlpatterns = \
    product_urls_v1

url_api_patterns = [
    url(r'^v1/', include(urlpatterns, namespace='v1')),
]
