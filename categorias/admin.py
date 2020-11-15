from django.contrib import admin

# Register your models here.

from . models import Comprador, Vendedor, Producto, DetalleCompra

admin.site.register(Comprador)
admin.site.register(Vendedor)
admin.site.register(Producto) 
admin.site.register(DetalleCompra) 



