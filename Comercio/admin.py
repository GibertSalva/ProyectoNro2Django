from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Direccion)

@admin.register(Cliente)
class ClienteAd (admin.ModelAdmin):
    list_display = ['rut' , 'nombre', 'telefono']
    list_filter = ['nombre' , 'telefono']

@admin.register(Producto)
class ProductoAd (admin.ModelAdmin):
    fieldsets = (('Descripcion', {'fields': ('idd', 'nombre',)}) , ('Variable', {'fields': ('precio', 'categoria' )}), )


@admin.register(Proveedore)
class ProveedoreFilt(admin.ModelAdmin):
    list_display = ['rut', 'nombre' , 'direccion', 'telefono']
    list_display_links = ['rut' , 'nombre'] 
    list_filter = ['nombre',]

@admin.register(Venta)
class VentaAd(admin.ModelAdmin):
    list_display = ['fecha', 'cliente', 'Descue']
    list_display_links = ['fecha' , 'cliente', ]
    actions = ['desconta']

    def desconta (self,request,queryset):
        return queryset.update(descuento = True)