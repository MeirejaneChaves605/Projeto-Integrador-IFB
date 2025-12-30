
from django.contrib import admin, auth
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views
from django.shortcuts import render


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home_view(request):
    return render(request, 'home.html', {'message': 'Bem-vindo ao Innova API! Acesse /admin para o painel de administração.'})

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', home_view, name='home'),
   
    path('api/v1/', include('portfolio.urls')),

    path('api/v1/token-auth/', auth_views.obtain_auth_token),
    
    path('api/v1/auth/token/', views.obtain_auth_token, name='obtain_auth_token'),
    
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
