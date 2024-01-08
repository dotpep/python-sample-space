from django.contrib import admin
from django.urls import path, include

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Block refresh token (block client to generate JWT access tokens)
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LittleLemonAPI.urls')),
    # djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # block JWT refresh tokens
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
