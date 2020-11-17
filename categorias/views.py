from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate
from .forms import CompradorForm, VendedorForm,ProductoForm
from . models import Producto, Vendedor, DetalleCompra


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',)
def InicioVendedor(request):
    data= {
        
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "Producto guardado correctamente"
        else:
            data["form"] = formulario

    return render(
        request,'InicioVendedor.html', data)
   

def Productos(request):
    return render(
        request,
        'Productos.html',)
def Registrarse(request):
    return render(
        request,
        'Registrarse.html',)

def RegistrarseComprador(request):
    data = {
        'form': CompradorForm()     
    }

    if request.method == 'POST':
        formulario = CompradorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Comprador Guardado"
        else:
            data["form"] = formulario
    
    return render(
        request,
        'RegistrarseComprador.html', data)

def RegistrarseVendedor(request):
    data = {
        'form1': VendedorForm()   
    }

    if request.method == 'POST':
        formulario = VendedorForm(data=request.POST)
        if formulario.is_valid():
             formulario.save()
             data["mensaje"] = "Vendedor Guardado"
        else:
            data["form1"] = formulario
   
    return render(
        request,
        'RegistrarseVendedor.html', data)


def ListarVendedores(request):
    vendedores = Vendedor.objects.all()

    data= {
        'vendedores': vendedores
    }
    return render(request, 'InicioVendedor.html', data)

def ListarProductos(request):
    productos = Producto.objects.all()

    data= {
        'productos': productos
    }
    return render(request, 'InicioVendedor.html', data)


def ListarPedidos(request):
    pedidos = DetalleCompra.objects.all()

    data= {
        'pedidos': pedidos
    }
    return render(request, 'InicioVendedor.html', data)

def ModificarProductos(request, id):

    producto = get_object_or_404(Producto, id_producto=id)

    data = {
        'form': ProductoForm(instance= producto)
    }

    if  request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "Producto modificado correctamente"
           return redirect(to="ListarProductos")
        data["form"] = formulario

    return render(request, 'InicioVendedor.html', data)