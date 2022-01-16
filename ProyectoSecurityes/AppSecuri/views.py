from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'AppSecuri/index.html')



def acerca(request):
    return render(request, 'AppSecuri/acerca.html')


def precios(request):
    return render(request, 'AppSecuri/precios.html')


def servicios(request):
    return render(request, 'AppSecuri/servicios.html')

def contacto(request):
    return render(request, 'AppSecuri/contacto.html')




