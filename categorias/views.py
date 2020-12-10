from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CompradorForm, VendedorForm,ProductoForm
from . models import Producto, Vendedor, DetalleCompra, Comprador


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',)

def InicioAdmin(request):
    vendedores = Vendedor.objects.all()
    pedidos= DetalleCompra.objects.all()
    comprador= Comprador.objects.all()
    productos=Producto.objects.all()


    return render(request, 'InicioAdmin.html',{'vendedores': vendedores, 'pedidos': pedidos, 'comprador': comprador, 'productos':productos})
   

def InicioVendedor(request):
   
    productos = Producto.objects.all()
    #vendedor= Vendedor.objects.values_list('nombre_vendedor')
    pedidos= DetalleCompra.objects.all()

    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
           formulario.save()
           #data["mensaje"] = "Producto guardado correctamente"
    formulario=ProductoForm()
    return render(
        request,'InicioVendedor.html', {'form':formulario,'productos':productos, 'pedidos': pedidos})
   

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



    




#def ListarPedidos(request):
   # pedidos = DetalleCompra.objects.all()

   # data= {
        #'pedidos': pedidos
   # }
    #return render(request, 'InicioVendedor.html', data)

def EditarProductos(request, **kwargs):
    productos = Producto.objects.all()
    producto = Producto.objects.get(id_producto=kwargs.get('id'))
    form = ProductoForm(instance=producto)
    
    return render(request, 'InicioVendedor.html', {'form':form,'productos':productos, 'productoid':producto.id_producto})

def ModificarProductos(request, **kwargs):
    producto = Producto.objects.get(id_producto=kwargs.get('id'))
    form = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('../../Editar-producto/' + str(producto.id_producto))

def EliminarProductos(request, **kwargs):
    producto = Producto.objects.get(id_producto=kwargs.get('id'))
    producto.delete()
    return redirect(to="InicioVendedor")
    
def EliminarProductos2(request, id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    # return HttpResponseRedirect('../../../InicioAdmin/')
    return redirect(to="InicioAdmin")


def EliminarVendedor(request, **kwargs):
    vendedor = Vendedor.objects.get(id_vendedor=kwargs.get('id'))
    vendedor.delete()
    
    # return HttpResponse("vendedor")
    return redirect(to="InicioAdmin")

def EliminarComprador(request, **kwargs):
    comprador = Comprador.objects.get(id_comprador=kwargs.get('id'))
    comprador.delete()
    
    # return HttpResponse("comprador")
    return redirect(to="InicioAdmin")   
    #producto = get_object_or_404(Producto, id_producto=id)

    #data = {
        #'form': ProductoForm(instance= producto)
    #}

    #if  request.method == 'POST':
        #formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        #if formulario.is_valid():
           #formulario.save()
           #data["mensaje"] = "Producto modificado correctamente"
           #return redirect(to="ListarProductos")
       # data["form"] = formulario

    #return render(request, 'InicioVendedor.html', data)