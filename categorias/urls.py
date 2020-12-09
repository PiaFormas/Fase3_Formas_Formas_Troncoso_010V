from django.urls import path
from . views import *

urlpatterns = [
    path('',index,name='index'),
    path('InicioVendedor/',InicioVendedor,name='InicioVendedor'),
    path('Productos/',Productos,name='Productos'),
    path('Registrarse/',Registrarse,name='Registrarse'),
    path('RegistrarseComprador/',RegistrarseComprador,name="RegistrarseComprador"),
    path('RegistrarseVendedor/',RegistrarseVendedor,name="RegistrarseVendedor"),
    #path('Listar-vendedores/',ListarVendedores,name="ListarVendedores"),
    #path('Listar-productos/',ListarProductos,name="ListarProductos"),
    #path('Listar-pedido/',ListarPedidos,name="ListarPedidos"),
    path('Modificar-producto/<id>/',ModificarProductos,name="ModificarProducto"),
    path('Editar-producto/<id>/',EditarProductos,name="EditarProductos"),
    path('Eliminar-producto/<id>/',EliminarProductos,name="EliminarProductos"),


    
    
    

]