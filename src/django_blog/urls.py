from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .api import api

urlpatterns = [
    path("api/", api.urls),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("", include("blog.urls", namespace="blog")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
