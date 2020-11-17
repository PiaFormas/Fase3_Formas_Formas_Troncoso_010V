from django.urls import path
from . views import index,InicioVendedor,Productos,Registrarse,RegistrarseComprador,RegistrarseVendedor,Listar_vendedores,Listar_productos,Listar_pedidos

urlpatterns = [
    path('',index,name='index'),
    path('InicioVendedor/',InicioVendedor,name='InicioVendedor'),
    path('Productos/',Productos,name='Productos'),
    path('Registrarse/',Registrarse,name='Registrarse'),
    path('RegistrarseComprador/',RegistrarseComprador,name="RegistrarseComprador"),
    path('RegistrarseVendedor/',RegistrarseVendedor,name="RegistrarseVendedor"),
    path('Listar-vendedores/',Listar_vendedores,name="ListarVendedores"),
    path('Listar-productos/',Listar_productos,name="ListarProductos"),
    path('Listar-pedido/',Listar_pedidos,name="ListarPedidos"),



    
    
    

]