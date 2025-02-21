from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include
from django.conf.urls.static import static
from .settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)


urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
