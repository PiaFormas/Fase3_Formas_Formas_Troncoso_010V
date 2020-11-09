from django.shortcuts import render
from . models import Comprador, Vendedor, Tarjeta, Producto, DetalleCompra, CuentaBanco

# Create your views here.
def index(request):
    num_compradores=Comprador.objects.all().count()
    num_vendedores=Vendedor.objects.all().count()
    num_productos=Producto.objects.all().count()
    num_cuentas=CuentaBanco.objects.all().count()
    num_tarjetas=Tarjeta.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_compradores':num_compradores,'num_vendedores':num_vendedores,'num_productos':num_productos,'num_cuentas':num_cuentas,'num_tarjetas':num_tarjetas},
)