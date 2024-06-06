from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

URLS_API_PREFIX = "api/v1"

urlpatterns = [
    path('admin/', admin.site.urls),

    # SPECTACULAR
    path(f'{URLS_API_PREFIX}/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{URLS_API_PREFIX}/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{URLS_API_PREFIX}/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # SCHEMAS
    path(f'{URLS_API_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{URLS_API_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{URLS_API_PREFIX}/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # APPS
    path(f'{URLS_API_PREFIX}/', include("apps.auth.urls")),
    path(f'{URLS_API_PREFIX}/', include("apps.tasks.urls")),
]
