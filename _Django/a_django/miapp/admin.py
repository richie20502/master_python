from django.contrib import admin
from .models import Article,Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
 
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','description')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)


#nombre del panel
title = "Master proyectos"
admin.site.site_header =  title
admin.site.site_title = title
admin.site.index_title = "Aplicaciones"