from django.urls import path
from . views import index,InicioVendedor,Productos,Registrarse,RegistrarseComprador,RegistrarseVendedor

urlpatterns = [
    path('',index,name='index'),
    path('InicioVendedor/',InicioVendedor,name='InicioVendedor'),
    path('Productos/',Productos,name='Productos'),
    path('Registrarse/',Registrarse,name='Registrarse'),
    path('RegistrarseComprador/',RegistrarseComprador,name='RegistrarseComprador'),
    path('RegistrarseVendedor/',RegistrarseVendedor,name='RegistrarseVendedor'),
    

]