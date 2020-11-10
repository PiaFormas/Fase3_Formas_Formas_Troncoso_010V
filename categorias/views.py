from django.shortcuts import render

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
    return render(
        request,
        'RegistrarseComprador',)

def RegistrarseVendedor(request):
    return render(
        request,
        'RegistrarseVendedor',)