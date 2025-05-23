"""
URL configuration for CMPBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs de la app de prueba
    path('api/task/', include('task_api.urls')), # Esta línea refleje la app de prueba

    # URLs para la autenticación JWT (obtener y refrescar tokens)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Incluye las URLs de tus nuevas aplicaciones de CryptoMinePro
    path('api/users/', include('users.urls')),
    path('api/tools/', include('cryptotools.urls')),
    path('api/learn/', include('cryptolearn.urls')),
    path('api/blog/', include('blogmine.urls')),
]
