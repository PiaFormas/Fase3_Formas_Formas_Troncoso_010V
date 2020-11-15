from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import CompradorForm, VendedorForm

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',)
def InicioVendedor(request):
    return render(
        request,
        'InicioVendedor.html',)

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