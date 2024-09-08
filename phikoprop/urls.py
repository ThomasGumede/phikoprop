from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("prop_home.urls", namespace="prop_home")),
    path("", include("rooms.urls", namespace="rooms")),
    path("", include("accounts.urls", namespace="accounts")),
     path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
