from django.contrib import admin

# Register your models here.

from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fc','fm')
admin.site.register(Categoria, CategoriaAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo','descripcion', 'subcategoria')
admin.site.register(Producto, ProductosAdmin)

