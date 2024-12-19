"""
URL configuration for CECEM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from inicio.views import inicioview
from inicio.views import base
from inicio.views import contacto
from inicio.views import about
from inicio.views import cursos
from inicio.views import infocurso
from inicio.views import taller_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicioview),
    path("index/",inicioview,name='index'),
    path('base/',base),
    path('acerca/',about,name='about'),
    path('cursos/',cursos,name='cursos'),
    path('contacto/',contacto,name='contacto'),
    path('infocurso/',infocurso,name='infocurso'),
    path('talleres/',taller_view,name='talleres')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)