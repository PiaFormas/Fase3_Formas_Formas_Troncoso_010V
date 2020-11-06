from django.contrib import admin

# Register your models here.

from . models import Comprador, Vendedor, Tarjeta, Producto, DetalleCompra, CuentaBanco

admin.site.register(Comprador)
admin.site.register(Vendedor)
admin.site.register(Tarjeta) 
admin.site.register(Producto) 
admin.site.register(DetalleCompra) 
admin.site.register(CuentaBanco)
    


