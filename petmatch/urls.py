from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include("petmatchapp.urls", namespace="petmatchapp")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)