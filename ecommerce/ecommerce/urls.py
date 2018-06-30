from rest_framework_swagger.views import get_swagger_view

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .v1_urls import url_api_patterns as v1_urls_api_patterns


schema_view = get_swagger_view(title='ECOMMERCE API')
all_api_urls_patterns = v1_urls_api_patterns

urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^$',
        TemplateView.as_view(template_name='base.html'),
        name='home'
    ),
    url(
        r'^docs/$',
        schema_view
    ),
    url(
        r'^api/',
        include(all_api_urls_patterns, namespace='api')
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
