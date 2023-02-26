from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen")
    public = models.BooleanField(verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos",
        ordering =['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=110, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias",
        ordering =['created_at']