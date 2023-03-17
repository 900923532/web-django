from django.shortcuts import render,HttpResponse
from servicio.models import Servicio
# Create your views here.

def home(request):
    return render(request,"Proyectowebapp/Home.html")
def servicios(request):
    servicio = Servicio.objects.all()
    return render(request,"Proyectowebapp/servicios.html",{"servicio":servicio})
def tienda(request):
    return render(request,"Proyectowebapp/tienda.html")
def contactos(request):
    return render(request,"Proyectowebapp/contactos.html")
def blog(request):
    return render(request,"Proyectowebapp/blog.html")
