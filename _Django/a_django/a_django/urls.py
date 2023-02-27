"""a_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import  settings


#from miapp import views
import miapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',miapp.views.index, name="index"),
    path('inicio/',miapp.views.index, name="inicio"),
    path('hola/',miapp.views.hola_mundo, name="hola_mundo"),
    path('pagina/',miapp.views.pagina, name="pagina"),
    path('pagina/<int:redirigir>',miapp.views.pagina, name="pagina"),
    path('contacto/',miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/',miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:ap>',miapp.views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', miapp.views.crear_articulo, name="crear-articulo"),
    path('articulo/', miapp.views.articulo, name='articulo'),
    path('editar-articulo/<int:id>',miapp.views.editar_articulo, name='editar_articulo'),
    path('articulos/',miapp.views.articulos, name='articulos'),
    path('borrar-articulo/<int:id>', miapp.views.borrar_articulos,name="borrar-articulo"),
    path('save-article',miapp.views.save_article, name="save_article"),
    path('create-article', miapp.views.create_article,name="create_article"),
    path('create-full-form',miapp.views.create_full_article,name='article-full')
]
#nombre del panel
admin.site.site_header = "Master proyectos"

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
