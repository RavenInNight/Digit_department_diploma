from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
# from orders.views import stripe_webhook_view
from django.conf.urls import include

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
