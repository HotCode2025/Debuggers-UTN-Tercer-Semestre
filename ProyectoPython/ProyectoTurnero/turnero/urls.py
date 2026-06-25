"""Enrutador principal: administrador, API y autenticación JWT."""
from django.contrib import admin
from django.urls import path, include
from turnos.views import LoginView
from rest_framework_simplejwt.views import  (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# /api/ contiene el dominio del turnero; login, refresh y verify son endpoints
# transversales usados por cualquier perfil.
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("turnos.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name= "token_refresh"),
    path("api/auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/auth/login/", LoginView.as_view(),name="token_obtain_pair"),
]

