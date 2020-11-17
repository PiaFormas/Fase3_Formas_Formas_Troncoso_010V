from django.shortcuts import render
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

        'form':CompradorForm() 
        
    }
    if request.method == 'POST':
        formulario = CompradorForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           Comprador = authenticate(usuario_comprador=formulario.cleaned_data["Usuario Comprador"], pass_comprador=formulario.cleaned_data["Password Comprador"])
           data["mensaje"] = "Comprador Guardado"
        else:
            data["form"] = formulario
    
    return render(
        request,
        'RegistrarseComprador.html', data)

def RegistrarseVendedor(request):
    data = {

        'form1':VendedorForm() 
        
    }
    if request.method == 'POST':
        formulario = VendedorForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           Vendedor = authenticate(usuario_vendedor=formulario.cleaned_data["Usuario Comprador"], pass_comprador=formulario.cleaned_data["Password Vendedor"])
           data["mensaje"] = "Vendedor Guardado"
        else:
            data["form1"] = formulario
   
    return render(
        request,
        'RegistrarseVendedor.html', data)

def Listar_vendedores(request):
    vendedores = Vendedor.objects.all()

    data= {
        'vendedores': vendedores
    }
    return render(request, 'InicioVendedor.html', data)

def Listar_productos(request):
    productos = Producto.objects.all()

    data= {
        'productos': productos
    }
    return render(request, 'InicioVendedor.html', data)


def Listar_pedidos(request):
    pedidos = DetalleCompra.objects.all()

    data= {
        'pedidos': pedidos
    }
    return render(request, 'InicioVendedor.html', data)

#def Modificar_producto(request, id):

    #producto = get_object_or_404(Producto, id=id)

    #data = {
        #'form': ProductoForm(instance=producto)
   # }

   # if  request.method == 'POST':
      #  formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
       # if formulario.is_valid():
          #  formulario.save()
           # messages.success(request, "Modificado correctamente")
          #  return redirect(to="listar_productos")
       # data["form"] = formulario

    #return render(request, 'app/crud/modificar.html', data)