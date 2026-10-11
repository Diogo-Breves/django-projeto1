"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.http import HttpResponse
from django.conf.urls.static import static #Necessário para importar os arquivos estáticos do projeto
from django.conf import settings #Modo correto para importar os settings do projeto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Necessário para mapear os arquivos de midia configurados no settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Necessário para mapear os arquivos estáticos configurados no settings
